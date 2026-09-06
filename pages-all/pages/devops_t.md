# DevOps Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html
- Fetched: 2026-09-05 19:16 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#dcoc-content-body)

## DevOps Common Types

### DBMS_CLOUD_OCI_DEVOPS_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_WAIT_CRITERIA_T Type

Specifies wait criteria for the Wait stage.

Syntax
```

```

Fields

Field Description

`wait_type`

(required) Wait criteria type.

Allowed values are: 'ABSOLUTE_WAIT'

### DBMS_CLOUD_OCI_DEVOPS_ABSOLUTE_WAIT_CRITERIA_T Type

Specifies the absolute wait criteria. You can specify fixed length of wait duration.

Syntax
```

```

`dbms_cloud_oci_devops_absolute_wait_criteria_t`is a subtype of the`dbms_cloud_oci_devops_wait_criteria_t`type.

Fields

Field Description

`wait_duration`

(required) The absolute wait duration. An ISO 8601 formatted duration string. Minimum waitDuration should be 5 seconds. Maximum waitDuration can be up to 2 days.

### DBMS_CLOUD_OCI_DEVOPS_WAIT_CRITERIA_SUMMARY_T Type

Specifies wait criteria for the Wait stage.

Syntax
```

```

Fields

Field Description

`wait_type`

(required) wait criteria type

Allowed values are: 'ABSOLUTE_WAIT'

### DBMS_CLOUD_OCI_DEVOPS_ABSOLUTE_WAIT_CRITERIA_SUMMARY_T Type

Specifies the absolute wait criteria, user can specify fixed length of wait duration.

Syntax
```

```

`dbms_cloud_oci_devops_absolute_wait_criteria_summary_t`is a subtype of the`dbms_cloud_oci_devops_wait_criteria_summary_t`type.

Fields

Field Description

`wait_duration`

(optional) The absolute wait duration. Minimum wait duration must be 5 seconds. Maximum wait duration can be up to 2 days.

### DBMS_CLOUD_OCI_DEVOPS_ACTUAL_BUILD_RUNNER_SHAPE_CONFIG_T Type

Build Runner Shape configuration.

Syntax
```

```

Fields

Field Description

`ocpus`

(required) The total number of OCPUs set for the instance.

`memory_in_g_bs`

(required) The total amount of memory set for the instance in gigabytes.

### DBMS_CLOUD_OCI_DEVOPS_APPROVAL_ACTION_T Type

Information about the approval action of DevOps deployment stages.

Syntax
```

```

Fields

Field Description

`subject_id`

(required) The subject ID of the user who approves or disapproves a DevOps deployment stage.

`action`

(required) The action of the user on the DevOps deployment stage.

Allowed values are: 'APPROVE', 'REJECT'

`reason`

(optional) The reason for approving or rejecting the deployment.

### DBMS_CLOUD_OCI_DEVOPS_APPROVAL_POLICY_T Type

Specifies the approval policy.

Syntax
```

```

Fields

Field Description

`approval_policy_type`

(required) Approval policy type.

Allowed values are: 'COUNT_BASED_APPROVAL'

### DBMS_CLOUD_OCI_DEVOPS_APPROVE_DEPLOYMENT_DETAILS_T Type

The stage information for submitting for approval.

Syntax
```

```

Fields

Field Description

`deploy_stage_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the stage which is marked for approval.

`reason`

(optional) The reason for approving or rejecting the deployment.

`action`

(required) The action of Approve or Reject.

Allowed values are: 'APPROVE', 'REJECT'

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_ROLLBACK_POLICY_T Type

Specifies the rollback policy. This is initiated on the failure of certain stage types.

Syntax
```

```

Fields

Field Description

`policy_type`

(required) Specifies type of the deployment stage rollback policy.

Allowed values are: 'AUTOMATED_STAGE_ROLLBACK_POLICY', 'NO_STAGE_ROLLBACK_POLICY'

### DBMS_CLOUD_OCI_DEVOPS_AUTOMATED_DEPLOY_STAGE_ROLLBACK_POLICY_T Type

Specifies the automated rollback policy for a stage on failure.

Syntax
```

```

`dbms_cloud_oci_devops_automated_deploy_stage_rollback_policy_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_rollback_policy_t`type.

### DBMS_CLOUD_OCI_DEVOPS_BACKEND_SET_IP_COLLECTION_T Type

Collection of backend environment IP addresses.

Syntax
```

```

Fields

Field Description

`items`

(optional) The IP address of the backend server. A server could be a compute instance or a load balancer.

### DBMS_CLOUD_OCI_DEVOPS_CONNECTION_VALIDATION_RESULT_T Type

The result of validating the credentials of a connection.

Syntax
```

```

Fields

Field Description

`result`

(optional) The latest result of whether the credentials pass the validation.

Allowed values are: 'PASS', 'FAIL'

`time_validated`

(optional) The latest timestamp when the connection was validated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`message`

(optional) A message describing the result of connection validation in more detail.

### DBMS_CLOUD_OCI_DEVOPS_CONNECTION_T Type

The properties that define a connection to external repositories.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`description`

(optional) Optional description about the connection.

`display_name`

(optional) Connection display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.

`compartment_id`

(required) The OCID of the compartment containing the connection.

`project_id`

(required) The OCID of the DevOps project.

`connection_type`

(required) The type of connection.

Allowed values are: 'GITHUB_ACCESS_TOKEN', 'GITLAB_ACCESS_TOKEN', 'GITLAB_SERVER_ACCESS_TOKEN', 'BITBUCKET_SERVER_ACCESS_TOKEN', 'BITBUCKET_CLOUD_APP_PASSWORD', 'VBS_ACCESS_TOKEN'

`time_created`

(optional) The time the connection was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) The time the connection was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`last_connection_validation_result`

(optional)

`lifecycle_details`

(optional) A detailed message describing the current state. For example, can be used to provide actionable information for a resource in Failed state.

`lifecycle_state`

(optional) The current state of the connection.

Allowed values are: 'ACTIVE', 'DELETING'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_CLOUD_APP_PASSWORD_CONNECTION_T Type

The properties that define a connection of the type `BITBUCKET_CLOUD_APP_PASSWORD`. This type corresponds to a connection in Bitbucket Cloud that is authenticated with a App Password along with username.

Syntax
```

```

`dbms_cloud_oci_devops_bitbucket_cloud_app_password_connection_t`is a subtype of the`dbms_cloud_oci_devops_connection_t`type.

Fields

Field Description

`username`

(required) Public Bitbucket Cloud Username in plain text

`app_password`

(required) OCID of personal Bitbucket Cloud AppPassword saved in secret store

### DBMS_CLOUD_OCI_DEVOPS_CONNECTION_SUMMARY_T Type

Summary information for a connection.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(optional) Connection display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.

`description`

(optional) Optional description about the connection.

`compartment_id`

(required) The OCID of the compartment containing the connection.

`project_id`

(required) The OCID of the DevOps project.

`connection_type`

(required) The type of connection.

`time_created`

(optional) The time the connection was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) The time the connection was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`last_connection_validation_result`

(optional)

`lifecycle_details`

(optional) A detailed message describing the current state. For example, can be used to provide actionable information for a resource in Failed state.

`lifecycle_state`

(optional) The current state of the connection.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_CLOUD_APP_PASSWORD_CONNECTION_SUMMARY_T Type

Summary information for a connection of the type `BITBUCKET_CLOUD_APP_PASSWORD`. This type corresponds to a connection in Bitbucket Cloud that is authenticated with a username and app password.

Syntax
```

```

`dbms_cloud_oci_devops_bitbucket_cloud_app_password_connection_summary_t`is a subtype of the`dbms_cloud_oci_devops_connection_summary_t`type.

Fields

Field Description

`username`

(required) Public Bitbucket Cloud Username in plain text

`app_password`

(required) OCID of personal Bitbucket Cloud AppPassword saved in secret store

### DBMS_CLOUD_OCI_DEVOPS_FILTER_T Type

The filters for the trigger.

Syntax
```

```

Fields

Field Description

`trigger_source`

(required) Source of the trigger. Allowed values are, GITHUB and GITLAB.

### DBMS_CLOUD_OCI_DEVOPS_TRIGGER_ACTION_T Type

The trigger action to be performed.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of action that will be taken. Allowed value is TRIGGER_BUILD_PIPELINE.

Allowed values are: 'TRIGGER_BUILD_PIPELINE'

`filter`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_TRIGGER_ACTION_TBL Type

Nested table type of dbms_cloud_oci_devops_trigger_action_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_TRIGGER_INFO_T Type

Trigger details that need to be used for the BuildRun

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Name for Trigger.

`actions`

(required) The list of actions that are to be performed for this Trigger

### DBMS_CLOUD_OCI_DEVOPS_BUILD_RUN_SOURCE_T Type

The source from which the build run is triggered.

Syntax
```

```

Fields

Field Description

`source_type`

(required) The source from which the build run is triggered.

Allowed values are: 'MANUAL', 'GITHUB', 'GITLAB', 'GITLAB_SERVER', 'BITBUCKET_CLOUD', 'BITBUCKET_SERVER', 'DEVOPS_CODE_REPOSITORY', 'VBS'

### DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_CLOUD_BUILD_RUN_SOURCE_T Type

Specifies details of build run through Bitbucket Cloud.

Syntax
```

```

`dbms_cloud_oci_devops_bitbucket_cloud_build_run_source_t`is a subtype of the`dbms_cloud_oci_devops_build_run_source_t`type.

Fields

Field Description

`trigger_id`

(required) The trigger that invoked the build run.

`trigger_info`

(required)

### DBMS_CLOUD_OCI_DEVOPS_BUILD_SOURCE_T Type

Build source required for the Build stage.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the build source. This must be unique within a build source collection. The name can be used by customers to locate the working directory pertinent to this repository.

`connection_type`

(required) The type of source provider.

Allowed values are: 'GITHUB', 'GITLAB', 'GITLAB_SERVER', 'BITBUCKET_CLOUD', 'BITBUCKET_SERVER', 'DEVOPS_CODE_REPOSITORY', 'VBS'

`repository_url`

(required) URL for the repository.

`branch`

(required) Branch name.

### DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_CLOUD_BUILD_SOURCE_T Type

Bitbucket Cloud Build Source for Build Stage

Syntax
```

```

`dbms_cloud_oci_devops_bitbucket_cloud_build_source_t`is a subtype of the`dbms_cloud_oci_devops_build_source_t`type.

Fields

Field Description

`connection_id`

(required) Connection identifier pertinent to Bitbucket Cloud source provider

### DBMS_CLOUD_OCI_DEVOPS_FILE_FILTER_T Type

Attributes to support include/exclude files for triggering build runs.

Syntax
```

```

Fields

Field Description

`file_paths`

(optional) The file paths/glob pattern for files.

### DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_CLOUD_FILTER_ATTRIBUTES_T Type

Attributes to filter Bitbucket Cloud events.

Syntax
```

```

Fields

Field Description

`head_ref`

(optional) Branch for push event; source branch for pull requests.

`base_ref`

(optional) The target branch for pull requests; not applicable for push requests.

`file_filter`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_CLOUD_FILTER_EXCLUSION_ATTRIBUTES_T Type

Attributes to filter Bitbucket Cloud events. File filter criteria - Changes only affecting excluded files will not invoke a build. if both include and exclude filter are used then exclusion filter will be applied on the result set of inclusion filter.

Syntax
```

```

Fields

Field Description

`file_filter`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_CLOUD_FILTER_T Type

The filter for Bitbucket Cloud events.

Syntax
```

```

`dbms_cloud_oci_devops_bitbucket_cloud_filter_t`is a subtype of the`dbms_cloud_oci_devops_filter_t`type.

Fields

Field Description

`events`

(optional) The events, for example, PUSH, PULL_REQUEST_MERGE.

Allowed values are: 'PUSH', 'PULL_REQUEST_CREATED', 'PULL_REQUEST_UPDATED', 'PULL_REQUEST_MERGED'

`include`

(optional)

`exclude`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_TRIGGER_T Type

Trigger the deployment pipeline to deploy the artifact.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(optional) Trigger display name. Avoid entering confidential information.

`description`

(optional) Description about the trigger.

`project_id`

(required) The OCID of the DevOps project to which the trigger belongs to.

`compartment_id`

(required) The OCID of the compartment that contains the trigger.

`trigger_source`

(required) Source of the trigger.

Allowed values are: 'GITHUB', 'GITLAB', 'GITLAB_SERVER', 'BITBUCKET_CLOUD', 'BITBUCKET_SERVER', 'VBS', 'DEVOPS_CODE_REPOSITORY'

`time_created`

(optional) The time the trigger was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) The time the trigger was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`lifecycle_state`

(optional) The current state of the trigger.

Allowed values are: 'ACTIVE', 'DELETING'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`actions`

(required) The list of actions that are to be performed for this trigger.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_CLOUD_TRIGGER_T Type

Trigger specific to Bitbucket Cloud

Syntax
```

```

`dbms_cloud_oci_devops_bitbucket_cloud_trigger_t`is a subtype of the`dbms_cloud_oci_devops_trigger_t`type.

Fields

Field Description

`trigger_url`

(required) The endpoint that listens to trigger events.

`connection_id`

(optional) The OCID of the connection resource used to get details for triggered events.

### DBMS_CLOUD_OCI_DEVOPS_TRIGGER_CREATE_RESULT_T Type

Details of the trigger create response.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(optional) Trigger display name. Avoid entering confidential information.

`description`

(optional) Description about the trigger.

`project_id`

(required) The OCID of the DevOps project to which the trigger belongs to.

`compartment_id`

(required) The OCID of the compartment that contains the trigger.

`trigger_source`

(required) Source of the trigger. Allowed values are, GITHUB and GITLAB.

`time_created`

(optional) The time the trigger was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) The time the trigger was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`lifecycle_state`

(optional) The current state of the trigger.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`actions`

(required) The list of actions that are to be performed for this trigger.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_CLOUD_TRIGGER_CREATE_RESULT_T Type

Trigger create response specific to Bitbucket Cloud.

Syntax
```

```

`dbms_cloud_oci_devops_bitbucket_cloud_trigger_create_result_t`is a subtype of the`dbms_cloud_oci_devops_trigger_create_result_t`type.

Fields

Field Description

`trigger_url`

(required) The endpoint that listens to trigger events. Contains the secret as a query parameter.

`connection_id`

(optional) The OCID of the connection resource used to get details for triggered events.

### DBMS_CLOUD_OCI_DEVOPS_TRIGGER_SUMMARY_T Type

Summary of the trigger.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(optional) Trigger display name. Avoid entering confidential information.

`description`

(optional) Description about the trigger.

`project_id`

(required) The OCID of the DevOps project to which the trigger belongs to.

`compartment_id`

(required) The OCID of the compartment that contains the trigger.

`trigger_source`

(required) Source of the trigger. Allowed values are, GITHUB and GITLAB.

`time_created`

(optional) The time the trigger was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) The time the trigger was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`lifecycle_state`

(optional) The current state of the trigger.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_CLOUD_TRIGGER_SUMMARY_T Type

Summary of the Bitbucket Cloud trigger.

Syntax
```

```

`dbms_cloud_oci_devops_bitbucket_cloud_trigger_summary_t`is a subtype of the`dbms_cloud_oci_devops_trigger_summary_t`type.

Fields

Field Description

`connection_id`

(optional) The OCID of the connection resource used to get details for triggered events.

### DBMS_CLOUD_OCI_DEVOPS_TLS_VERIFY_CONFIG_T Type

TLS configuration used by build service to verify TLS connection.

Syntax
```

```

Fields

Field Description

`tls_verify_mode`

(required) The type of TLS verification.

Allowed values are: 'CA_CERTIFICATE_VERIFY'

### DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_SERVER_ACCESS_TOKEN_CONNECTION_T Type

The properties that define a connection of the type `BITBUCKET_SERVER_ACCESS_TOKEN`. This type corresponds to a connection in Bitbucket that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_devops_bitbucket_server_access_token_connection_t`is a subtype of the`dbms_cloud_oci_devops_connection_t`type.

Fields

Field Description

`access_token`

(required) The OCID of personal access token saved in secret store.

`base_url`

(required) The Base URL of the hosted BitbucketServer.

`tls_verify_config`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_SERVER_BUILD_RUN_SOURCE_T Type

Specifies details of build run through Bitbucket Server.

Syntax
```

```

`dbms_cloud_oci_devops_bitbucket_server_build_run_source_t`is a subtype of the`dbms_cloud_oci_devops_build_run_source_t`type.

Fields

Field Description

`trigger_id`

(required) The trigger that invoked the build run.

`trigger_info`

(required)

### DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_SERVER_BUILD_SOURCE_T Type

Bitbucket Server Build Source for Build Stage

Syntax
```

```

`dbms_cloud_oci_devops_bitbucket_server_build_source_t`is a subtype of the`dbms_cloud_oci_devops_build_source_t`type.

Fields

Field Description

`connection_id`

(required) Connection identifier pertinent to Bitbucket Server source provider

### DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_SERVER_FILTER_ATTRIBUTES_T Type

Attributes to filter Bitbucket Server events.

Syntax
```

```

Fields

Field Description

`head_ref`

(optional) Branch for push event; source branch for pull requests.

`base_ref`

(optional) The target branch for pull requests; not applicable for push requests.

### DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_SERVER_FILTER_T Type

The filter for Bitbucket Server events.

Syntax
```

```

`dbms_cloud_oci_devops_bitbucket_server_filter_t`is a subtype of the`dbms_cloud_oci_devops_filter_t`type.

Fields

Field Description

`events`

(optional) The events, for example, PUSH, PULL_REQUEST_MERGE.

Allowed values are: 'PUSH', 'PULL_REQUEST_OPENED', 'PULL_REQUEST_MODIFIED', 'PULL_REQUEST_MERGED'

`include`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_SERVER_TOKEN_CONNECTION_SUMMARY_T Type

Summary information for a connection of the type `BITBUCKET_SERVER_ACCESS_TOKEN`. This type corresponds to a connection in Bitbucket that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_devops_bitbucket_server_token_connection_summary_t`is a subtype of the`dbms_cloud_oci_devops_connection_summary_t`type.

Fields

Field Description

`access_token`

(required) The OCID of personal access token saved in secret store.

`base_url`

(required) The Base URL of the hosted BitbucketServer.

`tls_verify_config`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_SERVER_TRIGGER_T Type

Trigger specific to Bitbucket Server

Syntax
```

```

`dbms_cloud_oci_devops_bitbucket_server_trigger_t`is a subtype of the`dbms_cloud_oci_devops_trigger_t`type.

Fields

Field Description

`trigger_url`

(required) The endpoint that listens to trigger events.

### DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_SERVER_TRIGGER_CREATE_RESULT_T Type

Trigger create response specific to Bitbucket Server.

Syntax
```

```

`dbms_cloud_oci_devops_bitbucket_server_trigger_create_result_t`is a subtype of the`dbms_cloud_oci_devops_trigger_create_result_t`type.

Fields

Field Description

`secret`

(required) The secret used to validate the incoming trigger call. This is visible only after the resource is created.

`trigger_url`

(required) The endpoint that listens to trigger events.

### DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_SERVER_TRIGGER_SUMMARY_T Type

Summary of the Bitbucket Server trigger.

Syntax
```

```

`dbms_cloud_oci_devops_bitbucket_server_trigger_summary_t`is a subtype of the`dbms_cloud_oci_devops_trigger_summary_t`type.

### DBMS_CLOUD_OCI_DEVOPS_EXPORTED_VARIABLE_T Type

Values for exported variables.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the parameter (case-sensitive). Parameter name must be ^[a-zA-Z][a-zA-Z_0-9]*$.

`value`

(required) Value of the argument.

### DBMS_CLOUD_OCI_DEVOPS_EXPORTED_VARIABLE_TBL Type

Nested table type of dbms_cloud_oci_devops_exported_variable_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_EXPORTED_VARIABLE_COLLECTION_T Type

Specifies list of exported variables.

Syntax
```

```

Fields

Field Description

`items`

(required) List of exported variables.

### DBMS_CLOUD_OCI_DEVOPS_DELIVERED_ARTIFACT_T Type

Details of the artifacts delivered through the Deliver Artifacts stage.

Syntax
```

```

Fields

Field Description

`deploy_artifact_id`

(required) The OCID of the deployment artifact definition.

`output_artifact_name`

(required) Name of the output artifact defined in the build specification file.

`artifact_type`

(required) Type of artifact delivered.

Allowed values are: 'GENERIC_ARTIFACT', 'OCIR'

### DBMS_CLOUD_OCI_DEVOPS_DELIVERED_ARTIFACT_TBL Type

Nested table type of dbms_cloud_oci_devops_delivered_artifact_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_DELIVERED_ARTIFACT_COLLECTION_T Type

Specifies the list of artifacts delivered through the Deliver Artifacts stage.

Syntax
```

```

Fields

Field Description

`items`

(required) List of artifacts delivered through the Deliver Artifacts stage.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_ARTIFACT_OVERRIDE_ARGUMENT_T Type

Values for artifact parameters to be supplied at the time of deployment.

Syntax
```

```

Fields

Field Description

`deploy_artifact_id`

(required) The OCID of the artifact to which this parameter applies.

`name`

(required) Name of the parameter (case-sensitive).

`value`

(required) Value of the parameter.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_ARTIFACT_OVERRIDE_ARGUMENT_TBL Type

Nested table type of dbms_cloud_oci_devops_deploy_artifact_override_argument_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_ARTIFACT_OVERRIDE_ARGUMENT_COLLECTION_T Type

Specifies the list of artifact override arguments at the time of deployment.

Syntax
```

```

Fields

Field Description

`items`

(required) List of artifact override arguments at the time of deployment.

### DBMS_CLOUD_OCI_DEVOPS_VULNERABILITY_AUDIT_SUMMARY_T Type

Summary of vulnerability audit.

Syntax
```

```

Fields

Field Description

`vulnerability_audit_id`

(required) The OCID of the vulnerability audit.

`commit_hash`

(optional) Commit hash used while retrieving the pom file for vulnerabilityAudit.

`build_stage_id`

(required) Build stage OCID where scan was configured.

### DBMS_CLOUD_OCI_DEVOPS_VULNERABILITY_AUDIT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_devops_vulnerability_audit_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_VULNERABILITY_AUDIT_SUMMARY_COLLECTION_T Type

List of vulnerability audit summary.

Syntax
```

```

Fields

Field Description

`items`

(required) List of vulnerability audit summary.

### DBMS_CLOUD_OCI_DEVOPS_BUILD_OUTPUTS_T Type

Outputs from the build.

Syntax
```

```

Fields

Field Description

`exported_variables`

(optional)

`delivered_artifacts`

(optional)

`artifact_override_parameters`

(optional)

`vulnerability_audit_summary_collection`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_PARAMETER_T Type

Parameter name for which the values will be supplied at the time of running the build.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the parameter (case-sensitive). Parameter name must be ^[a-zA-Z][a-zA-Z_0-9]*$. Example: 'Build_Pipeline_param' is not same as 'build_pipeline_Param'

`default_value`

(required) Default value of the parameter.

`description`

(optional) Description of the parameter.

### DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_PARAMETER_TBL Type

Nested table type of dbms_cloud_oci_devops_build_pipeline_parameter_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_PARAMETER_COLLECTION_T Type

Specifies list of parameters present in a build pipeline. An UPDATE operation replaces the existing parameters list entirely.

Syntax
```

```

Fields

Field Description

`items`

(required) List of parameters defined for a build pipeline.

### DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_T Type

A set of stages forming a directed acyclic graph that defines the build process.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`description`

(optional) Optional description about the build pipeline.

`display_name`

(optional) Build pipeline display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.

`compartment_id`

(required) The OCID of the compartment where the build pipeline is created.

`project_id`

(required) The OCID of the DevOps project.

`time_created`

(optional) The time the build pipeline was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) The time the build pipeline was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`lifecycle_state`

(optional) The current state of the build pipeline.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`build_pipeline_parameters`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_SUMMARY_T Type

Summary of the build pipeline.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`description`

(optional) Optional description about the build pipeline.

`display_name`

(optional) Build pipeline display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.

`compartment_id`

(required) The OCID of the compartment where the build pipeline is created.

`project_id`

(required) The OCID of the DevOps project.

`time_created`

(optional) The time the build pipeline was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) The time the build pipeline was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`lifecycle_details`

(optional) A detailed message describing the current state. For example, can be used to provide actionable information for a resource in Failed state.

`lifecycle_state`

(optional) The current state of the build pipeline.

`build_pipeline_parameters`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_devops_build_pipeline_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_COLLECTION_T Type

Results of a pipeline search.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of build pipeline summary items.

### DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_STAGE_PREDECESSOR_T Type

Metadata for defining a stage's predecessor.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the predecessor stage. If a stage is the first stage in the pipeline, then the ID is the pipeline's OCID.

### DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_STAGE_PREDECESSOR_TBL Type

Nested table type of dbms_cloud_oci_devops_build_pipeline_stage_predecessor_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_STAGE_PREDECESSOR_COLLECTION_T Type

The collection containing the predecessors of a stage.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of build pipeline stage predecessors for a stage.

### DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_STAGE_T Type

A single node in a build pipeline. A stage takes a specific designated action. There are many types of stages such as 'BUILD' and 'DELIVER_ARTIFACT'.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(optional) Stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.

`description`

(optional) Optional description about the build stage.

`project_id`

(required) The OCID of the DevOps project.

`build_pipeline_id`

(required) The OCID of the build pipeline.

`compartment_id`

(required) The OCID of the compartment where the pipeline is created.

`build_pipeline_stage_type`

(required) Defines the stage type, which is one of the following: BUILD, DELIVER_ARTIFACT, WAIT, and TRIGGER_DEPLOYMENT_PIPELINE.

Allowed values are: 'WAIT', 'BUILD', 'DELIVER_ARTIFACT', 'TRIGGER_DEPLOYMENT_PIPELINE'

`time_created`

(optional) The time the stage was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) The time the stage was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`lifecycle_state`

(optional) The current state of the stage.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`build_pipeline_stage_predecessor_collection`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_STAGE_SUMMARY_T Type

Summary of the Stage.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(optional) Stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.

`project_id`

(required) The OCID of the DevOps project.

`build_pipeline_id`

(required) The OCID of the build pipeline.

`compartment_id`

(required) The OCID of the compartment where the pipeline is created.

`build_pipeline_stage_type`

(required) Defines the stage type, which is one of the following: BUILD, DELIVER_ARTIFACT, WAIT, and TRIGGER_DEPLOYMENT_PIPELINE.

`time_created`

(optional) The time the stage was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) The time the stage was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`lifecycle_state`

(optional) The current state of the stage.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`description`

(optional) Optional description about the build stage.

`build_pipeline_stage_predecessor_collection`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_STAGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_devops_build_pipeline_stage_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_STAGE_COLLECTION_T Type

Result of a stage search.

Syntax
```

```

Fields

Field Description

`items`

(required) Summary of the list of stages found for the search.

### DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_STAGE_RUN_PROGRESS_T Type

The details about the run progress of a stage in a build run.

Syntax
```

```

Fields

Field Description

`stage_display_name`

(optional) Build Run display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.

`build_pipeline_stage_type`

(optional) Stage types.

`build_pipeline_stage_id`

(optional) The stage OCID.

`time_started`

(optional) The time the stage started executing. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_finished`

(optional) The time the stage finished executing. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`status`

(optional) The current status of the stage.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`build_pipeline_stage_predecessors`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_BUILD_RUN_ARGUMENT_T Type

Values for pipeline parameters to be supplied at the time of running the build.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the parameter (case-sensitive). Parameter name must be ^[a-zA-Z][a-zA-Z_0-9]*$. Example: 'Build_Pipeline_param' is not same as 'build_pipeline_Param'

`value`

(required) Value of the argument.

### DBMS_CLOUD_OCI_DEVOPS_BUILD_RUN_ARGUMENT_TBL Type

Nested table type of dbms_cloud_oci_devops_build_run_argument_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_BUILD_RUN_ARGUMENT_COLLECTION_T Type

Specifies list of arguments passed along with the build run.

Syntax
```

```

Fields

Field Description

`items`

(required) List of arguments provided at the time of running the build.

### DBMS_CLOUD_OCI_DEVOPS_BUILD_RUN_PROGRESS_T Type

The run progress details of a build run.

Syntax
```

```

Fields

Field Description

`time_started`

(optional) The time the build run started. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_finished`

(optional) The time the build run finished. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`build_pipeline_stage_run_progress`

(optional) Map of stage OCIDs to build pipeline stage run progress model.

### DBMS_CLOUD_OCI_DEVOPS_COMMIT_INFO_T Type

Commit details that need to be used for the build run.

Syntax
```

```

Fields

Field Description

`repository_url`

(required) Repository URL.

`repository_branch`

(required) Name of the repository branch.

`commit_hash`

(required) Commit hash pertinent to the repository URL and the specified branch.

### DBMS_CLOUD_OCI_DEVOPS_BUILD_RUN_T Type

Each time you attempt to run a build pipeline you create one build run. A build can be running currently, or it can be a record of the run that happened in the past. The set of build runs constitutes a build pipeline's history.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(optional) Build run display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.

`compartment_id`

(optional) The OCID of the compartment where the build is running.

`project_id`

(optional) The OCID of the DevOps project.

`build_pipeline_id`

(optional) The OCID of the build pipeline.

`build_run_source`

(required)

`build_run_arguments`

(optional)

`time_created`

(optional) The time the build run was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) The time the build run was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`lifecycle_state`

(optional) The current state of the build run.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'DELETING'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`build_run_progress`

(optional)

`commit_info`

(optional)

`build_outputs`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_BUILD_RUN_PROGRESS_SUMMARY_T Type

The summary run progress details of a build run.

Syntax
```

```

Fields

Field Description

`time_started`

(optional) The time the build run started. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_finished`

(optional) The time the build run finished. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

### DBMS_CLOUD_OCI_DEVOPS_BUILD_RUN_SUMMARY_T Type

Summary of the build run.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`compartment_id`

(required) The OCID of the compartment where the build is running.

`display_name`

(optional) Build run display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.

`project_id`

(required) The OCID of the DevOps project.

`build_pipeline_id`

(required) The OCID of the build pipeline.

`build_run_source`

(required)

`build_run_arguments`

(optional)

`build_run_progress_summary`

(optional)

`time_created`

(optional) The time the build run was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) The time the build run was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`lifecycle_state`

(optional) The current state of the build run.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`commit_info`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_BUILD_RUN_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_devops_build_run_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_BUILD_RUN_SUMMARY_COLLECTION_T Type

List of build run summary.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of build run summary items.

### DBMS_CLOUD_OCI_DEVOPS_BUILD_RUNNER_SHAPE_CONFIG_T Type

The information about build runner.

Syntax
```

```

Fields

Field Description

`build_runner_type`

(required) Name of the build runner shape in which the execution occurs. If not specified, the default shape is chosen.

Allowed values are: 'CUSTOM', 'DEFAULT'

### DBMS_CLOUD_OCI_DEVOPS_BUILD_SOURCE_TBL Type

Nested table type of dbms_cloud_oci_devops_build_source_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_BUILD_SOURCE_COLLECTION_T Type

Collection of build sources.

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of build sources. In case of UPDATE operation, replaces existing build sources list. Merging with existing build sources is not supported.

### DBMS_CLOUD_OCI_DEVOPS_NETWORK_CHANNEL_T Type

Specifies the configuration needed when the target OCI resource, i.e., OKE cluster, resides in customer's private network.

Syntax
```

```

Fields

Field Description

`network_channel_type`

(required) Network channel type.

Allowed values are: 'PRIVATE_ENDPOINT_CHANNEL', 'SERVICE_VNIC_CHANNEL'

### DBMS_CLOUD_OCI_DEVOPS_BUILD_STAGE_T Type

Specifies the build stage.

Syntax
```

```

`dbms_cloud_oci_devops_build_stage_t`is a subtype of the`dbms_cloud_oci_devops_build_pipeline_stage_t`type.

Fields

Field Description

`image`

(required) Image name for the build environment.

Allowed values are: 'OL7_X86_64_STANDARD_10'

`build_spec_file`

(optional) The path to the build specification file for this environment. The default location of the file if not specified is build_spec.yaml.

`stage_execution_timeout_in_seconds`

(optional) Timeout for the build stage execution. Specify value in seconds.

`build_source_collection`

(required)

`primary_build_source`

(optional) Name of the build source where the build_spec.yml file is located. If not specified, then the first entry in the build source collection is chosen as primary build source.

`build_runner_shape_config`

(optional)

`private_access_config`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_BUILD_STAGE_RUN_STEP_T Type

The details about each step in a build stage.

Syntax
```

```

Fields

Field Description

`name`

(optional) Name of the step.

`state`

(optional) State of the step.

Allowed values are: 'WAITING', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED'

`time_started`

(optional) Time when the step started.

`time_finished`

(optional) Time when the step finished.

### DBMS_CLOUD_OCI_DEVOPS_BUILD_STAGE_RUN_STEP_TBL Type

Nested table type of dbms_cloud_oci_devops_build_stage_run_step_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_BUILD_STAGE_RUN_PROGRESS_T Type

Specifies the run details for Build stage.

Syntax
```

```

`dbms_cloud_oci_devops_build_stage_run_progress_t`is a subtype of the`dbms_cloud_oci_devops_build_pipeline_stage_run_progress_t`type.

Fields

Field Description

`actual_build_runner_shape`

(optional) Name of Build Runner shape where this Build Stage is running.

`actual_build_runner_shape_config`

(optional)

`image`

(required) Image name for the Build Environment

Allowed values are: 'OL7_X86_64_STANDARD_10'

`build_spec_file`

(optional) The path to the build specification file for this Environment. The default location if not specified is build_spec.yaml

`stage_execution_timeout_in_seconds`

(optional) Timeout for the Build Stage Execution. Value in seconds.

`build_source_collection`

(required)

`primary_build_source`

(optional) Name of the BuildSource in which the build_spec.yml file need to be located. If not specified, the 1st entry in the BuildSource collection will be chosen as Primary.

`steps`

(optional) The details about all the steps in a Build stage

`exported_variables`

(optional)

`private_access_config`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_BUILD_STAGE_SUMMARY_T Type

Specifies the build stage.

Syntax
```

```

`dbms_cloud_oci_devops_build_stage_summary_t`is a subtype of the`dbms_cloud_oci_devops_build_pipeline_stage_summary_t`type.

Fields

Field Description

`image`

(required) Image for the build environment.

`build_spec_file`

(optional) The path to the build specification file for this environment. The default location of the file if not specified is build_spec.yaml.

`stage_execution_timeout_in_seconds`

(optional) Timeout for the build stage execution. Specify value in seconds.

`build_source_collection`

(optional)

`primary_build_source`

(optional) Name of the build source where the build_spec.yml file is located. If not specified, the first entry in the build source collection is chosen as primary build source.

`build_runner_shape_config`

(optional)

`private_access_config`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_CA_CERT_VERIFY_T Type

Enable TLS verification with CA certificate.

Syntax
```

```

`dbms_cloud_oci_devops_ca_cert_verify_t`is a subtype of the`dbms_cloud_oci_devops_tls_verify_config_t`type.

Fields

Field Description

`ca_certificate_bundle_id`

(required) The OCID of OCI certificate service CA bundle.

### DBMS_CLOUD_OCI_DEVOPS_CANCEL_BUILD_RUN_DETAILS_T Type

Information about canceling the build run.

Syntax
```

```

Fields

Field Description

`reason`

(required) The reason for canceling the build run.

### DBMS_CLOUD_OCI_DEVOPS_CANCEL_DEPLOYMENT_DETAILS_T Type

The information regarding the deployment to be canceled.

Syntax
```

```

Fields

Field Description

`reason`

(required) The reason for canceling the deployment.

### DBMS_CLOUD_OCI_DEVOPS_CHANGE_PROJECT_COMPARTMENT_DETAILS_T Type

The OCID of the compartment to which the project must be moved to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to which the resource must be moved.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_PREDECESSOR_T Type

Metadata for defining a stage's predecessor.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the predecessor stage. If a stage is the first stage in the pipeline, then the ID is the pipeline's OCID.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_PREDECESSOR_TBL Type

Nested table type of dbms_cloud_oci_devops_deploy_stage_predecessor_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_PREDECESSOR_COLLECTION_T Type

Collection containing the predecessors of a stage.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of stage predecessors for a stage.

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_ROLLOUT_POLICY_T Type

Specifies the rollout policy for compute instance group stages.

Syntax
```

```

Fields

Field Description

`policy_type`

(required) The type of policy used for rolling out a deployment stage.

Allowed values are: 'COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT', 'COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE'

`batch_delay_in_seconds`

(optional) The duration of delay between batch rollout. The default delay is 1 minute.

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_T Type

Specifies a failure policy for a compute instance group rolling deployment stage.

Syntax
```

```

Fields

Field Description

`policy_type`

(required) Specifies if the failure instance size is given by absolute number or by percentage.

Allowed values are: 'COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT', 'COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE'

### DBMS_CLOUD_OCI_DEVOPS_LOAD_BALANCER_CONFIG_T Type

Specifies configuration for load balancer traffic shift stages. The load balancer specified here should be an Application load balancer type. Network load balancers are not supported.

Syntax
```

```

Fields

Field Description

`load_balancer_id`

(required) The OCID of the load balancer.

`listener_name`

(required) Name of the load balancer listener.

`backend_port`

(optional) Listen port for the backend server.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_T Type

A single node in a pipeline. It is usually associated with some action on a specific set of OCI resources such as environments. For example, updating a Function or a Kubernetes cluster.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`description`

(optional) Optional description about the deployment stage.

`display_name`

(optional) Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.

`project_id`

(required) The OCID of a project.

`deploy_pipeline_id`

(required) The OCID of a pipeline.

`compartment_id`

(required) The OCID of a compartment.

`deploy_stage_type`

(required) Deployment stage type.

Allowed values are: 'WAIT', 'COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT', 'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT', 'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT', 'COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT', 'COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT', 'COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL', 'OKE_BLUE_GREEN_DEPLOYMENT', 'OKE_BLUE_GREEN_TRAFFIC_SHIFT', 'OKE_CANARY_DEPLOYMENT', 'OKE_CANARY_TRAFFIC_SHIFT', 'OKE_CANARY_APPROVAL', 'OKE_DEPLOYMENT', 'DEPLOY_FUNCTION', 'INVOKE_FUNCTION', 'LOAD_BALANCER_TRAFFIC_SHIFT', 'MANUAL_APPROVAL', 'OKE_HELM_CHART_DEPLOYMENT', 'SHELL'

`time_created`

(optional) Time the deployment stage was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) Time the deployment stage was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`lifecycle_state`

(optional) The current state of the deployment stage.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`deploy_stage_predecessor_collection`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOY_STAGE_T Type

Specifies the Instance Group Blue-Green deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_blue_green_deploy_stage_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_t`type.

Fields

Field Description

`deploy_environment_id_a`

(required) First compute instance group environment OCID for deployment.

`deploy_environment_id_b`

(required) Second compute instance group environment OCID for deployment.

`deployment_spec_deploy_artifact_id`

(required) The OCID of the artifact that contains the deployment specification.

`deploy_artifact_ids`

(optional) The list of file artifact OCIDs to deploy.

`rollout_policy`

(required)

`failure_policy`

(optional)

`test_load_balancer_config`

(optional)

`production_load_balancer_config`

(required)

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_EXECUTION_STEP_T Type

Details about each steps in stage execution for a target environment.

Syntax
```

```

Fields

Field Description

`name`

(optional) Name of the step.

`state`

(optional) State of the step.

Allowed values are: 'WAITING', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELED'

`time_started`

(optional) Time when the step started.

`time_finished`

(optional) Time when the step finished.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_EXECUTION_STEP_TBL Type

Nested table type of dbms_cloud_oci_devops_deploy_stage_execution_step_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_EXECUTION_PROGRESS_DETAILS_T Type

Details about stage execution for each target environment.

Syntax
```

```

Fields

Field Description

`target_id`

(optional) The function ID, instance ID or the cluster ID. For Wait stage it will be the stage ID.

`target_group`

(optional) Group for the target environment for example, the batch number for an Instance Group deployment.

`steps`

(optional) Details about all the steps for one target environment.

`rollback_steps`

(optional) Details about all the rollback steps for one target environment.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_EXECUTION_PROGRESS_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_devops_deploy_stage_execution_progress_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type

Details about the execution progress of a stage in a deployment.

Syntax
```

```

Fields

Field Description

`deploy_stage_display_name`

(optional) Stage display name. Avoid entering confidential information.

`deploy_stage_type`

(optional) Deployment stage type.

`deploy_stage_id`

(optional) The OCID of the stage.

`time_started`

(optional) Time the stage started executing. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_finished`

(optional) Time the stage finished executing. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`status`

(optional) The current state of the stage.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'ROLLBACK_IN_PROGRESS', 'ROLLBACK_SUCCEEDED', 'ROLLBACK_FAILED'

`deploy_stage_predecessors`

(optional)

`deploy_stage_execution_progress_details`

(optional) Details about stage execution for all the target environments.

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type

Specifies the Instance Group Blue-Green deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_blue_green_deploy_stage_execution_progress_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_execution_progress_t`type.

Fields

Field Description

`environment_id`

(optional) The OCID of the environment where the artifacts were deployed.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_SUMMARY_T Type

Summary of the deployment stage.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`description`

(optional) Optional description about the deployment stage.

`display_name`

(optional) Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.

`project_id`

(required) The OCID of a project.

`deploy_pipeline_id`

(required) The OCID of a pipeline.

`compartment_id`

(required) The OCID of a compartment.

`deploy_stage_type`

(required) Deployment stage type.

`time_created`

(optional) Time the deployment stage was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) Time the deployment stage was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`lifecycle_state`

(optional) The current state of the deployment stage.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`deploy_stage_predecessor_collection`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOY_STAGE_SUMMARY_T Type

Specifies the Instance Group Blue-Green deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_blue_green_deploy_stage_summary_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_summary_t`type.

Fields

Field Description

`deploy_environment_id_a`

(required) First compute instance group environment OCID for deployment.

`deploy_environment_id_b`

(required) Second compute instance group environment OCID for deployment.

`deployment_spec_deploy_artifact_id`

(required) The OCID of the artifact that contains the deployment specification.

`deploy_artifact_ids`

(optional) The list of file artifact OCIDs to deploy.

`rollout_policy`

(required)

`failure_policy`

(optional)

`test_load_balancer_config`

(optional)

`production_load_balancer_config`

(required)

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT_DEPLOY_STAGE_T Type

Specifies the instance group blue-green deployment load balancer traffic shift stage.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_blue_green_traffic_shift_deploy_stage_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_t`type.

Fields

Field Description

`compute_instance_group_blue_green_deployment_deploy_stage_id`

(required) The OCID of the upstream compute instance group blue-green deployment stage in this pipeline.

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type

Specifies the Instance Group Blue-Green deployment load balancer traffic shift stage.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_blue_green_traffic_shift_deploy_stage_execution_progress_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_execution_progress_t`type.

Fields

Field Description

`environment_id`

(optional) The OCID of the environment where traffic is going.

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT_DEPLOY_STAGE_SUMMARY_T Type

Specifies the instance group blue-green deployment load balancer traffic shift stage.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_blue_green_traffic_shift_deploy_stage_summary_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_summary_t`type.

Fields

Field Description

`compute_instance_group_blue_green_deployment_deploy_stage_id`

(required) The OCID of the upstream compute instance group blue-green deployment stage in this pipeline.

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_SELECTOR_T Type

Defines how the instances in a instance group environment is selected.

Syntax
```

```

Fields

Field Description

`selector_type`

(required) Defines the type of the instance selector for the group.

Allowed values are: 'INSTANCE_IDS', 'INSTANCE_QUERY'

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_BY_IDS_SELECTOR_T Type

Specifies the Compute instance group environment by listing the OCIDs of the compute instances.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_by_ids_selector_t`is a subtype of the`dbms_cloud_oci_devops_compute_instance_group_selector_t`type.

Fields

Field Description

`compute_instance_ids`

(required) Compute instance OCID identifiers that are members of this group.

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_BY_QUERY_SELECTOR_T Type

Specifies the Compute instance group environment filtered by the RQS query expression.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_by_query_selector_t`is a subtype of the`dbms_cloud_oci_devops_compute_instance_group_selector_t`type.

Fields

Field Description

`l_region`

(required) Region identifier referred by the deployment environment. Region identifiers are listed at https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm

`query`

(required) Query expression confirming to the OCI Search Language syntax to select compute instances for the group. The language is documented at https://docs.oracle.com/en-us/iaas/Content/Search/Concepts/querysyntax.htm

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL_DEPLOY_STAGE_T Type

Specifies the canary approval stage.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_canary_approval_deploy_stage_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_t`type.

Fields

Field Description

`compute_instance_group_canary_traffic_shift_deploy_stage_id`

(required) A compute instance group canary traffic shift stage OCID for load balancer.

`approval_policy`

(required)

### DBMS_CLOUD_OCI_DEVOPS_APPROVAL_ACTION_TBL Type

Nested table type of dbms_cloud_oci_devops_approval_action_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type

Specifies the Canary approval stage.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_canary_approval_deploy_stage_execution_progress_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_execution_progress_t`type.

Fields

Field Description

`approval_actions`

(optional) Specifies the Canary approval actions.

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL_DEPLOY_STAGE_SUMMARY_T Type

Specifies the canary approval stage.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_canary_approval_deploy_stage_summary_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_summary_t`type.

Fields

Field Description

`compute_instance_group_canary_traffic_shift_deploy_stage_id`

(required) A compute instance group canary traffic shift stage OCID for load balancer.

`approval_policy`

(required)

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_CANARY_DEPLOY_STAGE_T Type

Specifies the Instance Group Canary deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_canary_deploy_stage_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_t`type.

Fields

Field Description

`compute_instance_group_deploy_environment_id`

(required) A compute instance group environment OCID for Canary deployment.

`deployment_spec_deploy_artifact_id`

(required) The OCID of the artifact that contains the deployment specification.

`deploy_artifact_ids`

(optional) The list of file artifact OCIDs to deploy.

`rollout_policy`

(required)

`test_load_balancer_config`

(optional)

`production_load_balancer_config`

(required)

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_CANARY_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type

Specifies the Instance Group Canary deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_canary_deploy_stage_execution_progress_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_execution_progress_t`type.

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_CANARY_DEPLOY_STAGE_SUMMARY_T Type

Specifies the Instance Group Canary deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_canary_deploy_stage_summary_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_summary_t`type.

Fields

Field Description

`compute_instance_group_deploy_environment_id`

(required) A compute instance group environment OCID for Canary deployment.

`deployment_spec_deploy_artifact_id`

(required) The OCID of the artifact that contains the deployment specification.

`deploy_artifact_ids`

(optional) The list of file artifact OCIDs to deploy.

`rollout_policy`

(required)

`test_load_balancer_config`

(optional)

`production_load_balancer_config`

(required)

### DBMS_CLOUD_OCI_DEVOPS_LOAD_BALANCER_TRAFFIC_SHIFT_ROLLOUT_POLICY_T Type

Description of rollout policy for load balancer traffic shift stage.

Syntax
```

```

Fields

Field Description

`batch_count`

(required) Specifies number of batches for this stage.

`batch_delay_in_seconds`

(optional) Specifies delay in seconds between batches. The default delay is 1 minute.

`ramp_limit_percent`

(optional) Indicates the criteria to stop.

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT_DEPLOY_STAGE_T Type

Specifies the instance group canary deployment load balancer traffic shift stage.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_canary_traffic_shift_deploy_stage_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_t`type.

Fields

Field Description

`compute_instance_group_canary_deploy_stage_id`

(required) The OCID of an upstream compute instance group canary deployment stage ID in this pipeline.

`rollout_policy`

(required)

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type

Specifies the Instance Group Canary deployment load balancer traffic shift stage.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_canary_traffic_shift_deploy_stage_execution_progress_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_execution_progress_t`type.

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT_DEPLOY_STAGE_SUMMARY_T Type

Specifies the instance group canary deployment load balancer traffic shift stage.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_canary_traffic_shift_deploy_stage_summary_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_summary_t`type.

Fields

Field Description

`compute_instance_group_canary_deploy_stage_id`

(required) A compute instance group canary stage OCID for load balancer.

`rollout_policy`

(required)

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_SELECTOR_TBL Type

Nested table type of dbms_cloud_oci_devops_compute_instance_group_selector_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_SELECTOR_COLLECTION_T Type

A collection of selectors. The combination of instances matching the selectors are included in the instance group.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of selectors for the instance group. Union operator is used for combining the instances selected by each selector.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_ENVIRONMENT_T Type

The target OCI resources, such as Compute instances, Container Engine for Kubernetes(OKE) clusters, or Function, where artifacts are deployed.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`description`

(optional) Optional description about the deployment environment.

`display_name`

(optional) Deployment environment display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.

`project_id`

(required) The OCID of a project.

`compartment_id`

(required) The OCID of a compartment.

`deploy_environment_type`

(required) Deployment environment type.

Allowed values are: 'OKE_CLUSTER', 'COMPUTE_INSTANCE_GROUP', 'FUNCTION'

`time_created`

(optional) Time the deployment environment was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) Time the deployment environment was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`lifecycle_state`

(optional) The current state of the deployment environment.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_DEPLOY_ENVIRONMENT_T Type

Specifies the Compute instance group environment. The combination of instances matching the selectors are included in the instance group.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_deploy_environment_t`is a subtype of the`dbms_cloud_oci_devops_deploy_environment_t`type.

Fields

Field Description

`compute_instance_group_selectors`

(required)

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_ENVIRONMENT_SUMMARY_T Type

Summary of the deployment environment.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`description`

(optional) Optional description about the deployment environment.

`display_name`

(optional) Deployment environment display name, which can be renamed and is not necessarily unique.

`project_id`

(required) The OCID of a project.

`compartment_id`

(required) The OCID of a compartment.

`deploy_environment_type`

(required) Deployment environment type.

`time_created`

(optional) Time the deployment environment was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) Time the deployment environment was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`lifecycle_state`

(optional) The current state of the deployment environment.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_DEPLOY_ENVIRONMENT_SUMMARY_T Type

Specifies the Compute instance group environment.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_deploy_environment_summary_t`is a subtype of the`dbms_cloud_oci_devops_deploy_environment_summary_t`type.

Fields

Field Description

`compute_instance_group_selectors`

(required)

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_DEPLOY_STAGE_T Type

Specifies the Instance Group Rolling deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_deploy_stage_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_t`type.

Fields

Field Description

`compute_instance_group_deploy_environment_id`

(required) A compute instance group environment OCID for rolling deployment.

`deployment_spec_deploy_artifact_id`

(required) The OCID of the artifact that contains the deployment specification.

`deploy_artifact_ids`

(optional) Additional file artifact OCIDs.

`rollout_policy`

(required)

`rollback_policy`

(optional)

`failure_policy`

(optional)

`load_balancer_config`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type

Specifies the execution details for the Instance Group Rolling deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_deploy_stage_execution_progress_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_execution_progress_t`type.

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_DEPLOY_STAGE_SUMMARY_T Type

Specifies the Instance Group Rolling deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_deploy_stage_summary_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_summary_t`type.

Fields

Field Description

`compute_instance_group_deploy_environment_id`

(required) A compute instance group environment OCID for rolling deployment.

`deployment_spec_deploy_artifact_id`

(required) The OCID of the artifact that contains the deployment specification.

`deploy_artifact_ids`

(optional) Additional file artifact OCIDs.

`rollout_policy`

(required)

`rollback_policy`

(optional)

`failure_policy`

(optional)

`load_balancer_config`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT_T Type

Specifies a failure policy by count for a compute instance group rolling deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_failure_policy_by_count_t`is a subtype of the`dbms_cloud_oci_devops_compute_instance_group_failure_policy_t`type.

Fields

Field Description

`failure_count`

(required) The threshold count of failed instances in the group, which when reached or exceeded sets the stage as Failed.

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE_T Type

Specifies a failure policy by percentage for a compute instance group rolling deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_failure_policy_by_percentage_t`is a subtype of the`dbms_cloud_oci_devops_compute_instance_group_failure_policy_t`type.

Fields

Field Description

`failure_percentage`

(required) The failure percentage threshold, which when reached or exceeded sets the stage as Failed. Percentage is computed as the ceiling value of the number of failed instances over the total count of the instances in the group.

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT_T Type

Specifies a linear rollout strategy for a compute instance group rolling deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_linear_rollout_policy_by_count_t`is a subtype of the`dbms_cloud_oci_devops_compute_instance_group_rollout_policy_t`type.

Fields

Field Description

`batch_count`

(required) The number that will be used to determine how many instances will be deployed concurrently.

### DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE_T Type

Specifies a linear rollout strategy for a compute instance group rolling deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_compute_instance_group_linear_rollout_policy_by_percentage_t`is a subtype of the`dbms_cloud_oci_devops_compute_instance_group_rollout_policy_t`type.

Fields

Field Description

`batch_percentage`

(required) The percentage that will be used to determine how many instances will be deployed concurrently.

### DBMS_CLOUD_OCI_DEVOPS_CONNECTION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_devops_connection_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_CONNECTION_COLLECTION_T Type

Collection of connections.

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of connections.

### DBMS_CLOUD_OCI_DEVOPS_CONTAINER_CONFIG_T Type

Specifies the container configuration.

Syntax
```

```

Fields

Field Description

`container_config_type`

(required) Container configuration type.

Allowed values are: 'CONTAINER_INSTANCE_CONFIG'

### DBMS_CLOUD_OCI_DEVOPS_SHAPE_CONFIG_T Type

Determines the size and amount of resources available to the instance.

Syntax
```

```

Fields

Field Description

`ocpus`

(required) The total number of OCPUs available to the instance.

`memory_in_g_bs`

(optional) The total amount of memory available to the instance, in gigabytes.

### DBMS_CLOUD_OCI_DEVOPS_CONTAINER_INSTANCE_CONFIG_T Type

Specifies ContainerInstance configuration.

Syntax
```

```

`dbms_cloud_oci_devops_container_instance_config_t`is a subtype of the`dbms_cloud_oci_devops_container_config_t`type.

Fields

Field Description

`compartment_id`

(optional) The OCID of the compartment where the ContainerInstance will be created.

`availability_domain`

(optional) Availability domain where the ContainerInstance will be created.

`shape_name`

(required) The shape of the ContainerInstance. The shape determines the resources available to the ContainerInstance.

`shape_config`

(required)

`network_channel`

(required)

### DBMS_CLOUD_OCI_DEVOPS_CONTAINER_REGISTRY_DELIVERED_ARTIFACT_T Type

Details of the container registry artifacts delivered through the Deliver Artifacts stage.

Syntax
```

```

`dbms_cloud_oci_devops_container_registry_delivered_artifact_t`is a subtype of the`dbms_cloud_oci_devops_delivered_artifact_t`type.

Fields

Field Description

`delivered_artifact_hash`

(required) The hash of the container registry artifact pushed by the Deliver Artifacts stage.

`image_uri`

(optional) The imageUri of the OCIR artifact pushed by the DeliverArtifactStage

### DBMS_CLOUD_OCI_DEVOPS_COUNT_BASED_APPROVAL_POLICY_T Type

Count based stage approval policy.

Syntax
```

```

`dbms_cloud_oci_devops_count_based_approval_policy_t`is a subtype of the`dbms_cloud_oci_devops_approval_policy_t`type.

Fields

Field Description

`number_of_approvals_required`

(required) A minimum number of approvals required for stage to proceed.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_WAIT_CRITERIA_DETAILS_T Type

Specifies wait criteria for the Wait stage.

Syntax
```

```

Fields

Field Description

`wait_type`

(required) Wait criteria type.

Allowed values are: 'ABSOLUTE_WAIT'

### DBMS_CLOUD_OCI_DEVOPS_CREATE_ABSOLUTE_WAIT_CRITERIA_DETAILS_T Type

Specifies the absolute wait criteria. You can specify fixed length of wait duration.

Syntax
```

```

`dbms_cloud_oci_devops_create_absolute_wait_criteria_details_t`is a subtype of the`dbms_cloud_oci_devops_create_wait_criteria_details_t`type.

Fields

Field Description

`wait_duration`

(required) The absolute wait duration. Minimum wait duration must be 5 seconds. Maximum wait duration can be up to 2 days.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_CONNECTION_DETAILS_T Type

The details for creating a connection.

Syntax
```

```

Fields

Field Description

`description`

(optional) Optional description about the connection.

`display_name`

(optional) Optional connection display name. Avoid entering confidential information.

`project_id`

(required) The OCID of the DevOps project.

`connection_type`

(required) The type of connection.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_CREATE_BITBUCKET_CLOUD_APP_PASSWORD_CONNECTION_DETAILS_T Type

The details for creating a connection of the type `BITBUCKET_CLOUD_APP_PASSWORD`. This type corresponds to a connection in Bitbucket Cloud that is authenticated with username and app password.

Syntax
```

```

`dbms_cloud_oci_devops_create_bitbucket_cloud_app_password_connection_details_t`is a subtype of the`dbms_cloud_oci_devops_create_connection_details_t`type.

Fields

Field Description

`username`

(required) Public Bitbucket Cloud Username in plain text(not more than 30 characters)

`app_password`

(required) OCID of personal Bitbucket Cloud AppPassword saved in secret store

### DBMS_CLOUD_OCI_DEVOPS_CREATE_TRIGGER_DETAILS_T Type

Information about the new trigger.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Trigger display name. Avoid entering confidential information.

`description`

(optional) Optional description about the trigger.

`project_id`

(required) The OCID of the DevOps project to which the trigger belongs to.

`trigger_source`

(required) Source of the trigger. Allowed values are, GITHUB and GITLAB.

`actions`

(required) The list of actions that are to be performed for this trigger.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_CREATE_BITBUCKET_CLOUD_TRIGGER_DETAILS_T Type

The trigger for Bitbucket Cloud as the caller.

Syntax
```

```

`dbms_cloud_oci_devops_create_bitbucket_cloud_trigger_details_t`is a subtype of the`dbms_cloud_oci_devops_create_trigger_details_t`type.

Fields

Field Description

`connection_id`

(optional) The OCID of the connection resource used to get details for triggered events.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_BITBUCKET_SERVER_ACCESS_TOKEN_CONNECTION_DETAILS_T Type

The details for creating a connection of the type `BITBUCKET_SERVER_ACCESS_TOKEN`. This type corresponds to a connection in Bitbucket that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_devops_create_bitbucket_server_access_token_connection_details_t`is a subtype of the`dbms_cloud_oci_devops_create_connection_details_t`type.

Fields

Field Description

`access_token`

(required) The OCID of personal access token saved in secret store.

`base_url`

(required) The Base URL of the hosted BitbucketServer.

`tls_verify_config`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_CREATE_BITBUCKET_SERVER_TRIGGER_DETAILS_T Type

The trigger for Bitbucket Server as the caller.

Syntax
```

```

`dbms_cloud_oci_devops_create_bitbucket_server_trigger_details_t`is a subtype of the`dbms_cloud_oci_devops_create_trigger_details_t`type.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_BUILD_PIPELINE_DETAILS_T Type

Information about the new build pipeline to be created.

Syntax
```

```

Fields

Field Description

`description`

(optional) Optional description about the build pipeline.

`display_name`

(optional) Build pipeline display name. Avoid entering confidential information.

`project_id`

(required) The OCID of the DevOps project.

`build_pipeline_parameters`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_CREATE_BUILD_PIPELINE_STAGE_DETAILS_T Type

The information about a new stage.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.

`description`

(optional) Optional description about the stage.

`build_pipeline_stage_type`

(required) Defines the stage type, which is one of the following: BUILD, DELIVER_ARTIFACT, WAIT, and TRIGGER_DEPLOYMENT_PIPELINE.

`build_pipeline_id`

(required) The OCID of the build pipeline.

`build_pipeline_stage_predecessor_collection`

(required)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_CREATE_BUILD_RUN_DETAILS_T Type

Information about the new build run.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Build run display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.

`build_pipeline_id`

(required) The OCID of the build pipeline.

`commit_info`

(optional)

`build_run_arguments`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_CREATE_BUILD_STAGE_DETAILS_T Type

Specifies the build stage.

Syntax
```

```

`dbms_cloud_oci_devops_create_build_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_create_build_pipeline_stage_details_t`type.

Fields

Field Description

`image`

(required) Image name for the build environment

`build_spec_file`

(optional) The path to the build specification file for this environment. The default location of the file if not specified is build_spec.yaml.

`stage_execution_timeout_in_seconds`

(optional) Timeout for the build stage execution. Specify value in seconds.

`build_source_collection`

(required)

`primary_build_source`

(optional) Name of the build source where the build_spec.yml file is located. If not specified, the first entry in the build source collection is chosen as primary build source.

`build_runner_shape_config`

(optional)

`private_access_config`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_CREATE_DEPLOY_STAGE_DETAILS_T Type

The information about new deployment stage.

Syntax
```

```

Fields

Field Description

`description`

(optional) Optional description about the deployment stage.

`display_name`

(optional) Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.

`deploy_stage_type`

(required) Deployment stage type.

`deploy_pipeline_id`

(required) The OCID of a pipeline.

`deploy_stage_predecessor_collection`

(required)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_CREATE_COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOY_STAGE_DETAILS_T Type

Specifies the Instance Group Blue-Green deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_create_compute_instance_group_blue_green_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deploy_stage_details_t`type.

Fields

Field Description

`deploy_environment_id_a`

(required) First compute instance group environment OCID for deployment.

`deploy_environment_id_b`

(required) Second compute instance group environment OCID for deployment.

`deployment_spec_deploy_artifact_id`

(required) The OCID of the artifact that contains the deployment specification.

`deploy_artifact_ids`

(optional) The list of file artifact OCIDs to deploy.

`rollout_policy`

(required)

`failure_policy`

(optional)

`test_load_balancer_config`

(optional)

`production_load_balancer_config`

(required)

### DBMS_CLOUD_OCI_DEVOPS_CREATE_COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT_DEPLOY_STAGE_DETAILS_T Type

Specifies the instance group blue-green deployment load balancer traffic shift stage.

Syntax
```

```

`dbms_cloud_oci_devops_create_compute_instance_group_blue_green_traffic_shift_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deploy_stage_details_t`type.

Fields

Field Description

`compute_instance_group_blue_green_deployment_deploy_stage_id`

(required) The OCID of the upstream compute instance group blue-green deployment stage in this pipeline.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL_DEPLOY_STAGE_DETAILS_T Type

Specifies the canary approval stage.

Syntax
```

```

`dbms_cloud_oci_devops_create_compute_instance_group_canary_approval_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deploy_stage_details_t`type.

Fields

Field Description

`compute_instance_group_canary_traffic_shift_deploy_stage_id`

(required) A compute instance group canary traffic shift stage OCID for load balancer.

`approval_policy`

(required)

### DBMS_CLOUD_OCI_DEVOPS_CREATE_COMPUTE_INSTANCE_GROUP_CANARY_DEPLOY_STAGE_DETAILS_T Type

Specifies the Instance Group Canary deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_create_compute_instance_group_canary_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deploy_stage_details_t`type.

Fields

Field Description

`compute_instance_group_deploy_environment_id`

(required) A compute instance group environment OCID for Canary deployment.

`deployment_spec_deploy_artifact_id`

(required) The OCID of the artifact that contains the deployment specification.

`deploy_artifact_ids`

(optional) The list of file artifact OCIDs to deploy.

`rollout_policy`

(required)

`test_load_balancer_config`

(optional)

`production_load_balancer_config`

(required)

### DBMS_CLOUD_OCI_DEVOPS_CREATE_COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT_DEPLOY_STAGE_DETAILS_T Type

Specifies the instance group canary deployment load balancer traffic shift stage.

Syntax
```

```

`dbms_cloud_oci_devops_create_compute_instance_group_canary_traffic_shift_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deploy_stage_details_t`type.

Fields

Field Description

`compute_instance_group_canary_deploy_stage_id`

(required) A compute instance group canary stage OCID for load balancer.

`rollout_policy`

(required)

### DBMS_CLOUD_OCI_DEVOPS_CREATE_DEPLOY_ENVIRONMENT_DETAILS_T Type

The information about new deployment environment.

Syntax
```

```

Fields

Field Description

`description`

(optional) Optional description about the deployment environment.

`display_name`

(optional) Deployment environment display name. Avoid entering confidential information.

`deploy_environment_type`

(required) Deployment environment type.

`project_id`

(required) The OCID of a project.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_CREATE_COMPUTE_INSTANCE_GROUP_DEPLOY_ENVIRONMENT_DETAILS_T Type

Specifies the Compute instance group environment.

Syntax
```

```

`dbms_cloud_oci_devops_create_compute_instance_group_deploy_environment_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deploy_environment_details_t`type.

Fields

Field Description

`compute_instance_group_selectors`

(required)

### DBMS_CLOUD_OCI_DEVOPS_CREATE_COMPUTE_INSTANCE_GROUP_DEPLOY_STAGE_DETAILS_T Type

Specifies the Instance Group Rolling deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_create_compute_instance_group_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deploy_stage_details_t`type.

Fields

Field Description

`compute_instance_group_deploy_environment_id`

(required) A compute instance group environment OCID for rolling deployment.

`deployment_spec_deploy_artifact_id`

(required) The OCID of the artifact that contains the deployment specification.

`deploy_artifact_ids`

(optional) Additional file artifact OCIDs.

`rollout_policy`

(required)

`rollback_policy`

(optional)

`failure_policy`

(optional)

`load_balancer_config`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_DELIVER_ARTIFACT_T Type

Artifact information that need to be pushed to the artifactory stores.

Syntax
```

```

Fields

Field Description

`artifact_name`

(required) Name of the artifact specified in the build_spec.yaml file.

`artifact_id`

(required) Artifact identifier that contains the artifact definition.

### DBMS_CLOUD_OCI_DEVOPS_DELIVER_ARTIFACT_TBL Type

Nested table type of dbms_cloud_oci_devops_deliver_artifact_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_DELIVER_ARTIFACT_COLLECTION_T Type

Specifies an array of artifacts that need to be pushed to the artifactory stores.

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of artifacts that were generated in the Build stage and need to be pushed to the artifactory stores. In case of UPDATE operation, replaces existing artifacts list. Merging with existing artifacts is not supported.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_DELIVER_ARTIFACT_STAGE_DETAILS_T Type

Specifies the Deliver Artifacts stage.

Syntax
```

```

`dbms_cloud_oci_devops_create_deliver_artifact_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_create_build_pipeline_stage_details_t`type.

Fields

Field Description

`deliver_artifact_collection`

(required)

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_ARTIFACT_SOURCE_T Type

Specifies source of an artifact.

Syntax
```

```

Fields

Field Description

`deploy_artifact_source_type`

(required) Specifies types of artifact sources.

Allowed values are: 'INLINE', 'OCIR', 'GENERIC_ARTIFACT', 'HELM_CHART'

### DBMS_CLOUD_OCI_DEVOPS_CREATE_DEPLOY_ARTIFACT_DETAILS_T Type

Information about a new deployment artifact.

Syntax
```

```

Fields

Field Description

`description`

(optional) Optional description about the deployment artifact.

`display_name`

(optional) Deployment artifact display name. Avoid entering confidential information.

`deploy_artifact_type`

(required) Type of the deployment artifact.

`deploy_artifact_source`

(required)

`argument_substitution_mode`

(required) Mode for artifact parameter substitution.

`project_id`

(required) The OCID of a project.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_DEPLOYMENT_ARGUMENT_T Type

Values for pipeline parameters to be supplied at the time of deployment.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the parameter (case-sensitive).

`value`

(required) value of the argument.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOYMENT_ARGUMENT_TBL Type

Nested table type of dbms_cloud_oci_devops_deployment_argument_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_DEPLOYMENT_ARGUMENT_COLLECTION_T Type

Specifies list of arguments passed along with the deployment.

Syntax
```

```

Fields

Field Description

`items`

(required) List of arguments provided at the time of deployment.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_OVERRIDE_ARGUMENT_T Type

Values for stage override of the pipeline parameters to be supplied at the time of deployment.

Syntax
```

```

Fields

Field Description

`deploy_stage_id`

(required) The OCID of the stage.

`name`

(required) Name of the parameter (case-sensitive).

`value`

(required) Value of the parameter.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_OVERRIDE_ARGUMENT_TBL Type

Nested table type of dbms_cloud_oci_devops_deploy_stage_override_argument_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_OVERRIDE_ARGUMENT_COLLECTION_T Type

Specifies the list of arguments to be overriden per Stage at the time of deployment.

Syntax
```

```

Fields

Field Description

`items`

(required) List of artifact override arguments at the time of deployment.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_DEPLOYMENT_DETAILS_T Type

The information about new deployment.

Syntax
```

```

Fields

Field Description

`deploy_pipeline_id`

(required) The OCID of a pipeline.

`deployment_type`

(required) Specifies type for this deployment.

`display_name`

(optional) Deployment display name. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_CREATE_DEPLOY_PIPELINE_DEPLOYMENT_DETAILS_T Type

Details of the new deployment to be created that will run all the stages in the pipeline.

Syntax
```

```

`dbms_cloud_oci_devops_create_deploy_pipeline_deployment_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deployment_details_t`type.

Fields

Field Description

`deployment_arguments`

(optional)

`deploy_stage_override_arguments`

(optional)

`deploy_artifact_override_arguments`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_PARAMETER_T Type

Parameter name for which the values will be supplied at the time of deployment.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the parameter (case-sensitive). Parameter name must be ^[a-zA-Z][a-zA-Z_0-9]*$.

`default_value`

(optional) Default value of the parameter.

`description`

(optional) Description of the parameter.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_PARAMETER_TBL Type

Nested table type of dbms_cloud_oci_devops_deploy_pipeline_parameter_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_PARAMETER_COLLECTION_T Type

Specifies list of parameters present in the deployment pipeline. In case of Update operation, replaces existing parameters list. Merging with existing parameters is not supported.

Syntax
```

```

Fields

Field Description

`items`

(required) List of parameters defined for a deployment pipeline.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_DEPLOY_PIPELINE_DETAILS_T Type

The information about new deployment pipeline to be created.

Syntax
```

```

Fields

Field Description

`description`

(optional) Optional description about the deployment pipeline.

`display_name`

(optional) Deployment pipeline display name. Avoid entering confidential information.

`project_id`

(required) The OCID of a project.

`deploy_pipeline_parameters`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_CREATE_DEPLOY_PIPELINE_REDEPLOYMENT_DETAILS_T Type

Details of the new deployment to be created based on a previously executed deployment.

Syntax
```

```

`dbms_cloud_oci_devops_create_deploy_pipeline_redeployment_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deployment_details_t`type.

Fields

Field Description

`previous_deployment_id`

(required) Specifies the OCID of the previous deployment to be redeployed.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_DEVOPS_CODE_REPOSITORY_TRIGGER_DETAILS_T Type

The trigger for DevOps code repository as the caller.

Syntax
```

```

`dbms_cloud_oci_devops_create_devops_code_repository_trigger_details_t`is a subtype of the`dbms_cloud_oci_devops_create_trigger_details_t`type.

Fields

Field Description

`repository_id`

(optional) The OCID of the DevOps code repository.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_FUNCTION_DEPLOY_ENVIRONMENT_DETAILS_T Type

Specifies the Function environment.

Syntax
```

```

`dbms_cloud_oci_devops_create_function_deploy_environment_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deploy_environment_details_t`type.

Fields

Field Description

`function_id`

(required) The OCID of the Function.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_FUNCTION_DEPLOY_STAGE_DETAILS_T Type

Specifies the Function stage.

Syntax
```

```

`dbms_cloud_oci_devops_create_function_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deploy_stage_details_t`type.

Fields

Field Description

`function_deploy_environment_id`

(required) Function environment OCID.

`docker_image_deploy_artifact_id`

(required) A Docker image artifact OCID.

`config`

(optional) User provided key and value pair configuration, which is assigned through constants or parameter.

`max_memory_in_m_bs`

(optional) Maximum usable memory for the Function (in MB).

`function_timeout_in_seconds`

(optional) Timeout for execution of the Function. Value in seconds.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_GITHUB_ACCESS_TOKEN_CONNECTION_DETAILS_T Type

The details for creating a connection of the type `GITHUB_ACCESS_TOKEN`. This type corresponds to a connection in GitHub that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_devops_create_github_access_token_connection_details_t`is a subtype of the`dbms_cloud_oci_devops_create_connection_details_t`type.

Fields

Field Description

`access_token`

(required) The OCID of personal access token saved in secret store.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_GITHUB_TRIGGER_DETAILS_T Type

The trigger for GitHub as the caller.

Syntax
```

```

`dbms_cloud_oci_devops_create_github_trigger_details_t`is a subtype of the`dbms_cloud_oci_devops_create_trigger_details_t`type.

Fields

Field Description

`connection_id`

(optional) The OCID of the connection resource used to get details for triggered events.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_GITLAB_ACCESS_TOKEN_CONNECTION_DETAILS_T Type

The details for creating a connection of the type `GITLAB_ACCESS_TOKEN`. This type corresponds to a connection in GitLab that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_devops_create_gitlab_access_token_connection_details_t`is a subtype of the`dbms_cloud_oci_devops_create_connection_details_t`type.

Fields

Field Description

`access_token`

(required) The OCID of personal access token saved in secret store.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_GITLAB_SERVER_ACCESS_TOKEN_CONNECTION_DETAILS_T Type

The details for creating a connection of the type `GITLAB_SERVER_ACCESS_TOKEN`. This type corresponds to a connection in GitLab self hosted server that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_devops_create_gitlab_server_access_token_connection_details_t`is a subtype of the`dbms_cloud_oci_devops_create_connection_details_t`type.

Fields

Field Description

`access_token`

(required) The OCID of personal access token saved in secret store.

`base_url`

(required) The baseUrl of the hosted GitLabServer.

`tls_verify_config`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_CREATE_GITLAB_SERVER_TRIGGER_DETAILS_T Type

The trigger for GitLab as the caller.

Syntax
```

```

`dbms_cloud_oci_devops_create_gitlab_server_trigger_details_t`is a subtype of the`dbms_cloud_oci_devops_create_trigger_details_t`type.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_GITLAB_TRIGGER_DETAILS_T Type

The trigger for GitLab as the caller.

Syntax
```

```

`dbms_cloud_oci_devops_create_gitlab_trigger_details_t`is a subtype of the`dbms_cloud_oci_devops_create_trigger_details_t`type.

Fields

Field Description

`connection_id`

(optional) The OCID of the connection resource used to get details for triggered events.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_INVOKE_FUNCTION_DEPLOY_STAGE_DETAILS_T Type

Specifies Invoke Function stage.

Syntax
```

```

`dbms_cloud_oci_devops_create_invoke_function_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deploy_stage_details_t`type.

Fields

Field Description

`function_deploy_environment_id`

(required) Function environment OCID.

`deploy_artifact_id`

(optional) Optional artifact OCID. The artifact will be included in the body for the function invocation during the stage's execution. If the DeployArtifact.argumentSubstituitionMode is set to SUBSTITUTE_PLACEHOLDERS, then the pipeline parameter values will be used to replace the placeholders in the artifact content.

`is_async`

(required) A boolean flag specifies whether this stage executes asynchronously.

`is_validation_enabled`

(required) A boolean flag specifies whether the invoked function should be validated.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_LOAD_BALANCER_TRAFFIC_SHIFT_DEPLOY_STAGE_DETAILS_T Type

Specifies load balancer traffic shift stage.

Syntax
```

```

`dbms_cloud_oci_devops_create_load_balancer_traffic_shift_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deploy_stage_details_t`type.

Fields

Field Description

`blue_backend_ips`

(required)

`green_backend_ips`

(required)

`traffic_shift_target`

(required) Specifies the target or destination backend set. Example: BLUE - Traffic from the existing backends of managed Load Balance Listener to blue Backend IPs, as per rolloutPolicy. GREEN - Traffic from the existing backends of managed Load Balance Listener to blue Backend IPs ser as per rolloutPolicy.

`rollout_policy`

(required)

`load_balancer_config`

(required)

`rollback_policy`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_CREATE_MANUAL_APPROVAL_DEPLOY_STAGE_DETAILS_T Type

Specifies the manual approval stage.

Syntax
```

```

`dbms_cloud_oci_devops_create_manual_approval_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deploy_stage_details_t`type.

Fields

Field Description

`approval_policy`

(required)

### DBMS_CLOUD_OCI_DEVOPS_OKE_BLUE_GREEN_STRATEGY_T Type

Specifies the required blue-green release strategy for OKE deployment.

Syntax
```

```

Fields

Field Description

`strategy_type`

(required) Blue-Green strategy type.

Allowed values are: 'NGINX_BLUE_GREEN_STRATEGY'

### DBMS_CLOUD_OCI_DEVOPS_CREATE_OKE_BLUE_GREEN_DEPLOY_STAGE_DETAILS_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster Blue-Green deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_create_oke_blue_green_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deploy_stage_details_t`type.

Fields

Field Description

`oke_cluster_deploy_environment_id`

(required) Kubernetes cluster environment OCID for deployment.

`kubernetes_manifest_deploy_artifact_ids`

(required) List of Kubernetes manifest artifact OCIDs.

`blue_green_strategy`

(required)

### DBMS_CLOUD_OCI_DEVOPS_CREATE_OKE_BLUE_GREEN_TRAFFIC_SHIFT_DEPLOY_STAGE_DETAILS_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster blue-green deployment traffic shift stage.

Syntax
```

```

`dbms_cloud_oci_devops_create_oke_blue_green_traffic_shift_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deploy_stage_details_t`type.

Fields

Field Description

`oke_blue_green_deploy_stage_id`

(required) The OCID of the upstream OKE blue-green deployment stage in this pipeline.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_OKE_CANARY_APPROVAL_DEPLOY_STAGE_DETAILS_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster canary deployment approval stage.

Syntax
```

```

`dbms_cloud_oci_devops_create_oke_canary_approval_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deploy_stage_details_t`type.

Fields

Field Description

`oke_canary_traffic_shift_deploy_stage_id`

(required) The OCID of an upstream OKE canary deployment traffic shift stage in this pipeline.

`approval_policy`

(required)

### DBMS_CLOUD_OCI_DEVOPS_OKE_CANARY_STRATEGY_T Type

Specifies the required canary release strategy for OKE deployment.

Syntax
```

```

Fields

Field Description

`strategy_type`

(required) Canary strategy type.

Allowed values are: 'NGINX_CANARY_STRATEGY'

### DBMS_CLOUD_OCI_DEVOPS_CREATE_OKE_CANARY_DEPLOY_STAGE_DETAILS_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster Canary deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_create_oke_canary_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deploy_stage_details_t`type.

Fields

Field Description

`oke_cluster_deploy_environment_id`

(required) Kubernetes cluster environment OCID for deployment.

`kubernetes_manifest_deploy_artifact_ids`

(required) List of Kubernetes manifest artifact OCIDs.

`canary_strategy`

(required)

### DBMS_CLOUD_OCI_DEVOPS_CREATE_OKE_CANARY_TRAFFIC_SHIFT_DEPLOY_STAGE_DETAILS_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster canary deployment traffic shift stage.

Syntax
```

```

`dbms_cloud_oci_devops_create_oke_canary_traffic_shift_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deploy_stage_details_t`type.

Fields

Field Description

`oke_canary_deploy_stage_id`

(required) The OCID of an upstream OKE canary deployment stage in this pipeline.

`rollout_policy`

(required)

### DBMS_CLOUD_OCI_DEVOPS_CREATE_OKE_CLUSTER_DEPLOY_ENVIRONMENT_DETAILS_T Type

Specifies the Kubernetes cluster environment.

Syntax
```

```

`dbms_cloud_oci_devops_create_oke_cluster_deploy_environment_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deploy_environment_details_t`type.

Fields

Field Description

`cluster_id`

(required) The OCID of the Kubernetes cluster.

`network_channel`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_CREATE_OKE_DEPLOY_STAGE_DETAILS_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_create_oke_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deploy_stage_details_t`type.

Fields

Field Description

`oke_cluster_deploy_environment_id`

(required) Kubernetes cluster environment OCID for deployment.

`kubernetes_manifest_deploy_artifact_ids`

(required) List of Kubernetes manifest artifact OCIDs.

`namespace`

(optional) Default namespace to be used for Kubernetes deployment when not specified in the manifest.

`rollback_policy`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_HELM_SET_VALUE_T Type

Defines a helm set value

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the parameter (case-sensitive).

`value`

(required) Value of the parameter.

### DBMS_CLOUD_OCI_DEVOPS_HELM_SET_VALUE_TBL Type

Nested table type of dbms_cloud_oci_devops_helm_set_value_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_HELM_SET_VALUE_COLLECTION_T Type

Specifies the name and value pairs to set helm values.

Syntax
```

```

Fields

Field Description

`items`

(required) List of parameters defined to set helm value.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_OKE_HELM_CHART_DEPLOY_STAGE_DETAILS_T Type

Specifies the Helm chart deployment to a Kubernetes cluster stage.

Syntax
```

```

`dbms_cloud_oci_devops_create_oke_helm_chart_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deploy_stage_details_t`type.

Fields

Field Description

`oke_cluster_deploy_environment_id`

(required) Kubernetes cluster environment OCID for deployment.

`helm_chart_deploy_artifact_id`

(required) Helm chart artifact OCID.

`values_artifact_ids`

(optional) List of values.yaml file artifact OCIDs.

`release_name`

(required) Default name of the chart instance. Must be unique within a Kubernetes namespace.

`namespace`

(optional) Default namespace to be used for Kubernetes deployment when not specified in the manifest.

`timeout_in_seconds`

(optional) Time to wait for execution of a helm stage. Defaults to 300 seconds.

`rollback_policy`

(optional)

`set_values`

(optional)

`set_string`

(optional)

`are_hooks_enabled`

(optional) Disable pre/post upgrade hooks. Set to false by default.

`should_reuse_values`

(optional) During upgrade, reuse the values of the last release and merge overrides from the command line. Set to false by default.

`should_reset_values`

(optional) During upgrade, reset the values to the ones built into the chart. It overrides shouldReuseValues. Set to false by default.

`is_force_enabled`

(optional) Force resource update through delete; or if required, recreate. Set to false by default.

`should_cleanup_on_fail`

(optional) Allow deletion of new resources created during when an upgrade fails. Set to false by default.

`max_history`

(optional) Limit the maximum number of revisions saved per release. Use 0 for no limit. Set to 10 by default

`should_skip_crds`

(optional) If set, no CRDs are installed. By default, CRDs are installed only if they are not present already. Set to false by default.

`should_skip_render_subchart_notes`

(optional) If set, renders subchart notes along with the parent. Set to false by default.

`should_not_wait`

(optional) Does not wait until all the resources are in a ready state to mark the release as successful if set to true. Set to false by default.

`is_debug_enabled`

(optional) Enables helm --debug option to stream output to tf stdout. Set to false by default.

### DBMS_CLOUD_OCI_DEVOPS_NOTIFICATION_CONFIG_T Type

Notification configuration for the project.

Syntax
```

```

Fields

Field Description

`topic_id`

(required) The topic ID for notifications.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_PROJECT_DETAILS_T Type

The information about new project to be created.

Syntax
```

```

Fields

Field Description

`name`

(required) Project name (case-sensitive).

`description`

(optional) Project description.

`notification_config`

(required)

`compartment_id`

(required) The OCID of the compartment where the project is created.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_TRIGGER_SCHEDULE_T Type

Specifies a trigger schedule. Timing information for when to initiate automated syncs.

Syntax
```

```

Fields

Field Description

`schedule_type`

(required) Different types of trigger schedule: NONE - No automated synchronization schedule. DEFAULT - Trigger schedule is every 30 minutes. CUSTOM - Custom triggering schedule.

Allowed values are: 'NONE', 'DEFAULT', 'CUSTOM'

`custom_schedule`

(optional) Valid if type is CUSTOM. Following RFC 5545 recurrence rules, we can specify starting time, occurrence frequency, and interval size. Example for frequency could be DAILY/WEEKLY/HOURLY or any RFC 5545 supported frequency, which is followed by start time of this window. You can control the start time with BYHOUR, BYMINUTE and BYSECONDS. It is followed by the interval size.

### DBMS_CLOUD_OCI_DEVOPS_MIRROR_REPOSITORY_CONFIG_T Type

Configuration information for mirroring the repository.

Syntax
```

```

Fields

Field Description

`connector_id`

(optional) Upstream git repository connection identifer.

`repository_url`

(optional) URL of external repository you want to mirror.

`trigger_schedule`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_CREATE_REPOSITORY_DETAILS_T Type

Information about the new repository.

Syntax
```

```

Fields

Field Description

`name`

(required) Unique name of a repository.

`project_id`

(required) The OCID of the DevOps project containing the repository.

`default_branch`

(optional) The default branch of the repository.

`repository_type`

(required) Type of repository. Allowed values: `MIRRORED` `HOSTED`

`mirror_repository_config`

(optional)

`description`

(optional) Details of the repository. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_CREATE_SHELL_DEPLOY_STAGE_DETAILS_T Type

Specifies the shell stage.

Syntax
```

```

`dbms_cloud_oci_devops_create_shell_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deploy_stage_details_t`type.

Fields

Field Description

`container_config`

(required)

`command_spec_deploy_artifact_id`

(required) The OCID of the artifact that contains the command specification.

`timeout_in_seconds`

(optional) Time to wait for execution of a shell stage. Defaults to 36000 seconds.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_SINGLE_DEPLOY_STAGE_DEPLOYMENT_DETAILS_T Type

Details of a new deployment to be created that will run a single stage of the pipeline.

Syntax
```

```

`dbms_cloud_oci_devops_create_single_deploy_stage_deployment_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deployment_details_t`type.

Fields

Field Description

`deploy_stage_id`

(required) Specifies the OCID of the stage to be redeployed.

`deployment_arguments`

(optional)

`deploy_stage_override_arguments`

(optional)

`deploy_artifact_override_arguments`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_CREATE_SINGLE_DEPLOY_STAGE_REDEPLOYMENT_DETAILS_T Type

Details of a new deployment to be created that will rerun a single stage from a previously executed deployment.

Syntax
```

```

`dbms_cloud_oci_devops_create_single_deploy_stage_redeployment_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deployment_details_t`type.

Fields

Field Description

`previous_deployment_id`

(optional) Specifies the OCID of the previous deployment to be redeployed.

`deploy_stage_id`

(required) Specifies the OCID of the stage to be redeployed.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_TRIGGER_DEPLOYMENT_STAGE_DETAILS_T Type

Specifies the Trigger Deployment stage, which runs another pipeline of the application.

Syntax
```

```

`dbms_cloud_oci_devops_create_trigger_deployment_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_create_build_pipeline_stage_details_t`type.

Fields

Field Description

`deploy_pipeline_id`

(required) A target deployment pipeline OCID that will run in this stage.

`is_pass_all_parameters_enabled`

(required) A boolean flag that specifies whether all the parameters must be passed when the deployment is triggered.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_VBS_ACCESS_TOKEN_CONNECTION_DETAILS_T Type

The details for creating a connection of the type `VBS_ACCESS_TOKEN`. This type corresponds to a connection in Visual Builder Studio that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_devops_create_vbs_access_token_connection_details_t`is a subtype of the`dbms_cloud_oci_devops_create_connection_details_t`type.

Fields

Field Description

`access_token`

(required) The OCID of personal access token saved in secret store.

`base_url`

(required) The Base URL of the hosted VBS server.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_VBS_TRIGGER_DETAILS_T Type

The trigger for VBS as the caller.

Syntax
```

```

`dbms_cloud_oci_devops_create_vbs_trigger_details_t`is a subtype of the`dbms_cloud_oci_devops_create_trigger_details_t`type.

Fields

Field Description

`connection_id`

(optional) The OCID of the connection resource used to get details for triggered events.

### DBMS_CLOUD_OCI_DEVOPS_CREATE_WAIT_DEPLOY_STAGE_DETAILS_T Type

Specifies the Wait stage. User can specify a criteria for wait time or give an absolute duration.

Syntax
```

```

`dbms_cloud_oci_devops_create_wait_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_create_deploy_stage_details_t`type.

Fields

Field Description

`wait_criteria`

(required)

### DBMS_CLOUD_OCI_DEVOPS_CREATE_WAIT_STAGE_DETAILS_T Type

Specifies the Wait stage. You can specify variable wait times or an absolute duration.

Syntax
```

```

`dbms_cloud_oci_devops_create_wait_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_create_build_pipeline_stage_details_t`type.

Fields

Field Description

`wait_criteria`

(required)

### DBMS_CLOUD_OCI_DEVOPS_CUSTOM_BUILD_RUNNER_SHAPE_CONFIG_T Type

Specifies the custom build runner shape config.

Syntax
```

```

`dbms_cloud_oci_devops_custom_build_runner_shape_config_t`is a subtype of the`dbms_cloud_oci_devops_build_runner_shape_config_t`type.

Fields

Field Description

`ocpus`

(required) The total number of OCPUs set for the instance.

`memory_in_g_bs`

(required) The total amount of memory set for the instance in gigabytes.

### DBMS_CLOUD_OCI_DEVOPS_DEFAULT_BUILD_RUNNER_SHAPE_CONFIG_T Type

Specifies the default build runner shape config.

Syntax
```

```

`dbms_cloud_oci_devops_default_build_runner_shape_config_t`is a subtype of the`dbms_cloud_oci_devops_build_runner_shape_config_t`type.

### DBMS_CLOUD_OCI_DEVOPS_DELIVER_ARTIFACT_STAGE_T Type

Specifies the Deliver Artifacts stage.

Syntax
```

```

`dbms_cloud_oci_devops_deliver_artifact_stage_t`is a subtype of the`dbms_cloud_oci_devops_build_pipeline_stage_t`type.

Fields

Field Description

`deliver_artifact_collection`

(required)

### DBMS_CLOUD_OCI_DEVOPS_DELIVER_ARTIFACT_STAGE_RUN_PROGRESS_T Type

Specifies Deliver Artifacts stage specific run details.

Syntax
```

```

`dbms_cloud_oci_devops_deliver_artifact_stage_run_progress_t`is a subtype of the`dbms_cloud_oci_devops_build_pipeline_stage_run_progress_t`type.

Fields

Field Description

`delivered_artifacts`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_DELIVER_ARTIFACT_STAGE_SUMMARY_T Type

Specifies the Deliver Artifacts stage.

Syntax
```

```

`dbms_cloud_oci_devops_deliver_artifact_stage_summary_t`is a subtype of the`dbms_cloud_oci_devops_build_pipeline_stage_summary_t`type.

Fields

Field Description

`deliver_artifact_collection`

(required)

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_ARTIFACT_T Type

Artifacts are deployment manifests that are referenced in a pipeline stage for automated deployment to the target environment. DevOps artifacts can be an OCI Container image repository, Kubernetes manifest, an Artifact Registry artifact, or defined inline.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`description`

(optional) Optional description about the artifact to be deployed.

`display_name`

(optional) Deployment artifact identifier, which can be renamed and is not necessarily unique. Avoid entering confidential information.

`project_id`

(required) The OCID of a project.

`compartment_id`

(required) The OCID of a compartment.

`deploy_artifact_type`

(required) Type of the deployment artifact.

Allowed values are: 'DEPLOYMENT_SPEC', 'JOB_SPEC', 'KUBERNETES_MANIFEST', 'GENERIC_FILE', 'DOCKER_IMAGE', 'HELM_CHART', 'COMMAND_SPEC'

`argument_substitution_mode`

(required) Mode for artifact parameter substitution.

Allowed values are: 'NONE', 'SUBSTITUTE_PLACEHOLDERS'

`deploy_artifact_source`

(required)

`time_created`

(optional) Time the deployment artifact was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) Time the deployment artifact was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`lifecycle_state`

(optional) Current state of the deployment artifact.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A detailed message describing the current state. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_ARTIFACT_SUMMARY_T Type

Summary of the deployment artifact.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`description`

(optional) Optional description about the deployment artifact.

`display_name`

(optional) Deployment artifact identifier, which can be renamed and is not necessarily unique. Avoid entering confidential information.

`project_id`

(required) The OCID of a project.

`compartment_id`

(required) The OCID of a compartment.

`deploy_artifact_type`

(required) Type of the deployment artifact.

`deploy_artifact_source`

(required)

`argument_substitution_mode`

(required) Mode for artifact parameter substitution.

`time_created`

(optional) Time the deployment artifact was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) Time the deployment artifact was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`lifecycle_state`

(optional) Current state of the deployment artifact.

`lifecycle_details`

(optional) A detailed message describing the current state. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_ARTIFACT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_devops_deploy_artifact_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_ARTIFACT_COLLECTION_T Type

Results of a deployment artifact search.

Syntax
```

```

Fields

Field Description

`items`

(required) Deployment artifact summary items found for the search.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_ENVIRONMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_devops_deploy_environment_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_ENVIRONMENT_COLLECTION_T Type

Results of a deployment environment search.

Syntax
```

```

Fields

Field Description

`items`

(required) Deployment environment summary items found for the search.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_STAGE_T Type

Stage used in the pipeline for an artifact or environment.

Syntax
```

```

Fields

Field Description

`deploy_stage_id`

(required) The OCID of a stage

`display_name`

(optional) Display name of the stage. Avoid entering confidential information.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_STAGE_TBL Type

Nested table type of dbms_cloud_oci_devops_deploy_pipeline_stage_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_STAGE_COLLECTION_T Type

List of stages.

Syntax
```

```

Fields

Field Description

`items`

(required) List of stages.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_ARTIFACT_T Type

Artifact used in the pipeline.

Syntax
```

```

Fields

Field Description

`deploy_artifact_id`

(required) The OCID of an artifact

`display_name`

(optional) Display name of the artifact. Avoid entering confidential information.

`deploy_pipeline_stages`

(required)

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_ARTIFACT_TBL Type

Nested table type of dbms_cloud_oci_devops_deploy_pipeline_artifact_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_ARTIFACT_COLLECTION_T Type

List of all artifacts used in the pipeline.

Syntax
```

```

Fields

Field Description

`items`

(required) List of all artifacts used in the pipeline.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_ENVIRONMENT_T Type

Environment used in the pipeline.

Syntax
```

```

Fields

Field Description

`deploy_environment_id`

(required) The OCID of an Environment

`display_name`

(optional) Display name of the environment. Avoid entering confidential information.

`deploy_pipeline_stages`

(required)

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_ENVIRONMENT_TBL Type

Nested table type of dbms_cloud_oci_devops_deploy_pipeline_environment_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_ENVIRONMENT_COLLECTION_T Type

List of all environments used in the pipeline.

Syntax
```

```

Fields

Field Description

`items`

(required) List of all environments used in the pipeline.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_T Type

A set of stages whose predecessor relation forms a directed acyclic graph.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`description`

(optional) Optional description about the deployment pipeline.

`display_name`

(optional) Deployment pipeline display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.

`project_id`

(required) The OCID of a project.

`compartment_id`

(required) The OCID of the compartment where the pipeline is created.

`deploy_pipeline_artifacts`

(optional)

`deploy_pipeline_environments`

(optional)

`time_created`

(optional) Time the deployment pipeline was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) Time the deployment pipeline was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`lifecycle_state`

(optional) The current state of the deployment pipeline.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`deploy_pipeline_parameters`

(required)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_SUMMARY_T Type

Summary of the deployment pipeline.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`description`

(optional) Optional description about the deployment pipeline.

`display_name`

(optional) Deployment pipeline display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.

`project_id`

(required) The OCID of a project.

`compartment_id`

(required) The OCID of a compartment where the pipeline is created.

`time_created`

(optional) Time the deployment pipeline was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) Time the deployment pipeline was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`lifecycle_state`

(optional) The current state of the deployment pipeline.

`deploy_pipeline_parameters`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_devops_deploy_pipeline_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_COLLECTION_T Type

Results of an pipeline search.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of deployment pipeline summary items.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOYMENT_EXECUTION_PROGRESS_T Type

The execution progress details of a deployment.

Syntax
```

```

Fields

Field Description

`time_started`

(optional) Time the deployment is started. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_finished`

(optional) Time the deployment is finished. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`deploy_stage_execution_progress`

(optional) Map of stage OCIDs to deploy stage execution progress model.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOYMENT_T Type

A single execution or run of a pipeline.

Syntax
```

```

Fields

Field Description

`deploy_pipeline_artifacts`

(optional)

`deploy_pipeline_environments`

(optional)

`deployment_type`

(required) Specifies type of deployment.

Allowed values are: 'PIPELINE_DEPLOYMENT', 'PIPELINE_REDEPLOYMENT', 'SINGLE_STAGE_DEPLOYMENT', 'SINGLE_STAGE_REDEPLOYMENT'

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(optional) Deployment identifier which can be renamed and is not necessarily unique. Avoid entering confidential information.

`project_id`

(required) The OCID of a project.

`deploy_pipeline_id`

(required) The OCID of a pipeline.

`compartment_id`

(required) The OCID of a compartment.

`time_created`

(optional) Time the deployment was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) Time the deployment was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`lifecycle_state`

(optional) The current state of the deployment.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`deployment_arguments`

(optional)

`deploy_stage_override_arguments`

(optional)

`deploy_artifact_override_arguments`

(optional)

`deployment_execution_progress`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_DEPLOYMENT_T Type

Deployment of all the stages in the pipeline.

Syntax
```

```

`dbms_cloud_oci_devops_deploy_pipeline_deployment_t`is a subtype of the`dbms_cloud_oci_devops_deployment_t`type.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOYMENT_SUMMARY_T Type

Summary of the deployment.

Syntax
```

```

Fields

Field Description

`deployment_type`

(required) Specifies type for this deployment.

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(optional) Deployment identifier which can be renamed and is not necessarily unique. Avoid entering confidential information.

`project_id`

(required) The OCID of a project.

`deploy_pipeline_id`

(required) The OCID of a pipeline.

`compartment_id`

(required) The OCID of a compartment.

`time_created`

(optional) Time the deployment was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) Time the deployment was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`lifecycle_state`

(optional) The current state of the deployment.

`deployment_arguments`

(optional)

`deploy_stage_override_arguments`

(optional)

`deploy_artifact_override_arguments`

(optional)

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_DEPLOYMENT_SUMMARY_T Type

Summary of a full pipeline deployment.

Syntax
```

```

`dbms_cloud_oci_devops_deploy_pipeline_deployment_summary_t`is a subtype of the`dbms_cloud_oci_devops_deployment_summary_t`type.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_REDEPLOYMENT_T Type

Redeployment of the full pipeline of a previous deployment.

Syntax
```

```

`dbms_cloud_oci_devops_deploy_pipeline_redeployment_t`is a subtype of the`dbms_cloud_oci_devops_deployment_t`type.

Fields

Field Description

`previous_deployment_id`

(required) Specifies the OCID of the previous deployment to be redeployed.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_REDEPLOYMENT_SUMMARY_T Type

Summary of a full pipeline redeployment.

Syntax
```

```

`dbms_cloud_oci_devops_deploy_pipeline_redeployment_summary_t`is a subtype of the`dbms_cloud_oci_devops_deployment_summary_t`type.

Fields

Field Description

`previous_deployment_id`

(required) Specifies the OCID of the previous deployment to be redeployed.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_devops_deploy_stage_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_COLLECTION_T Type

Result of a stage search.

Syntax
```

```

Fields

Field Description

`items`

(required) Deployment stage summary items found for the search.

### DBMS_CLOUD_OCI_DEVOPS_DEPLOYMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_devops_deployment_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_DEPLOYMENT_COLLECTION_T Type

Results of a deployment search.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of deployment summary items.

### DBMS_CLOUD_OCI_DEVOPS_DEVOPS_CODE_REPOSITORY_BUILD_RUN_SOURCE_T Type

Specifies details of build run through DevOps code repository.

Syntax
```

```

`dbms_cloud_oci_devops_devops_code_repository_build_run_source_t`is a subtype of the`dbms_cloud_oci_devops_build_run_source_t`type.

Fields

Field Description

`trigger_id`

(required) The trigger that invoked the build run.

`trigger_info`

(required)

`repository_id`

(required) The DevOps code repository identifier that invoked the build run.

### DBMS_CLOUD_OCI_DEVOPS_DEVOPS_CODE_REPOSITORY_BUILD_SOURCE_T Type

DevOps code repository build source for Build stage.

Syntax
```

```

`dbms_cloud_oci_devops_devops_code_repository_build_source_t`is a subtype of the`dbms_cloud_oci_devops_build_source_t`type.

Fields

Field Description

`repository_id`

(required) The DevOps code repository ID.

### DBMS_CLOUD_OCI_DEVOPS_DEVOPS_CODE_REPOSITORY_FILTER_ATTRIBUTES_T Type

Attributes to filter DevOps code repository events.

Syntax
```

```

Fields

Field Description

`head_ref`

(optional) Branch for push event.

`file_filter`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_DEVOPS_CODE_REPOSITORY_FILTER_EXCLUSION_ATTRIBUTES_T Type

Attributes to filter DevopsCodeRepository events. File filter criteria - Changes only affecting excluded files will not invoke a build. if both include and exclude filter are used then exclusion filter will be applied on the result set of inclusion filter.

Syntax
```

```

Fields

Field Description

`file_filter`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_DEVOPS_CODE_REPOSITORY_FILTER_T Type

The filter for GitLab events.

Syntax
```

```

`dbms_cloud_oci_devops_devops_code_repository_filter_t`is a subtype of the`dbms_cloud_oci_devops_filter_t`type.

Fields

Field Description

`events`

(optional) The events only support PUSH.

Allowed values are: 'PUSH'

`include`

(optional)

`exclude`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_DEVOPS_CODE_REPOSITORY_TRIGGER_T Type

Trigger specific to OCI DevOps Code Repository service.

Syntax
```

```

`dbms_cloud_oci_devops_devops_code_repository_trigger_t`is a subtype of the`dbms_cloud_oci_devops_trigger_t`type.

Fields

Field Description

`repository_id`

(required) The OCID of the DevOps code repository.

### DBMS_CLOUD_OCI_DEVOPS_DEVOPS_CODE_REPOSITORY_TRIGGER_CREATE_RESULT_T Type

Trigger create response specific to GitLab.

Syntax
```

```

`dbms_cloud_oci_devops_devops_code_repository_trigger_create_result_t`is a subtype of the`dbms_cloud_oci_devops_trigger_create_result_t`type.

Fields

Field Description

`repository_id`

(required) The OCID of the DevOps code repository.

### DBMS_CLOUD_OCI_DEVOPS_DEVOPS_CODE_REPOSITORY_TRIGGER_SUMMARY_T Type

Summary of the DevOps code repository trigger.

Syntax
```

```

`dbms_cloud_oci_devops_devops_code_repository_trigger_summary_t`is a subtype of the`dbms_cloud_oci_devops_trigger_summary_t`type.

Fields

Field Description

`repository_id`

(required) The OCID of the DevOps code repository.

### DBMS_CLOUD_OCI_DEVOPS_DIFF_LINE_DETAILS_T Type

Details about a line within the difference.

Syntax
```

```

Fields

Field Description

`base_line`

(optional) The number of a line in the base version.

`target_line`

(optional) The number of a line in the target version.

`line_content`

(optional) The contents of a line.

`conflict_marker`

(optional) Indicates whether a line in a conflicted section of the difference is from the base version, the target version, or if its just a marker indicating the beginning, middle, or end of a conflicted section.

Allowed values are: 'BASE', 'TARGET', 'MARKER', 'NONE'

### DBMS_CLOUD_OCI_DEVOPS_DIFF_LINE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_devops_diff_line_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_DIFF_SECTION_T Type

Details about a section of changes within a difference chunk.

Syntax
```

```

Fields

Field Description

`l_type`

(optional) Type of change.

`lines`

(optional) The lines within changed section.

### DBMS_CLOUD_OCI_DEVOPS_DIFF_SECTION_TBL Type

Nested table type of dbms_cloud_oci_devops_diff_section_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_DIFF_CHUNK_T Type

Details about a group of changes.

Syntax
```

```

Fields

Field Description

`base_line`

(optional) Line number in base version where changes begin.

`base_span`

(optional) Number of lines chunk spans in base version.

`target_line`

(optional) Line number in target version where changes begin.

`target_span`

(optional) Number of lines chunk spans in target version.

`diff_sections`

(optional) List of difference section.

### DBMS_CLOUD_OCI_DEVOPS_DIFF_CHUNK_TBL Type

Nested table type of dbms_cloud_oci_devops_diff_chunk_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_DIFF_SUMMARY_T Type

Response object for showing differences for a file between two revisions.

Syntax
```

```

Fields

Field Description

`old_path`

(optional) The path on the base version to the changed object.

`new_path`

(optional) The path on the target version to the changed object.

`old_id`

(optional) The ID of the changed object on the base version.

`new_id`

(optional) The ID of the changed object on the target version.

`are_conflicts_in_file`

(optional) Indicates whether the changed file contains conflicts.

`is_large`

(optional) Indicates whether the file is large.

`is_binary`

(optional) Indicates whether the file is binary.

`changes`

(required) List of changed section in the file.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_DIFF_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_devops_diff_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_DIFF_COLLECTION_T Type

Result of a compare difference.

Syntax
```

```

Fields

Field Description

`items`

(required) List of objects describing differences for all changed files.

### DBMS_CLOUD_OCI_DEVOPS_DIFF_RESPONSE_ENTRY_T Type

Entry for description of change on a file.

Syntax
```

```

Fields

Field Description

`change_type`

(required) Type of change made to file.

`object_type`

(optional) The type of the changed object.

`commit_id`

(optional) The ID of the commit where the change is coming from.

`old_path`

(optional) The path on the target to the changed object.

`new_path`

(optional) The path on the source to the changed object.

`old_id`

(optional) The ID of the changed object on the target.

`new_id`

(optional) The ID of the changed object on the source.

`url`

(optional) The URL of the changed object.

`added_lines_count`

(optional) The number of lines added in whole difference.

`deleted_lines_count`

(optional) The number of lines deleted in whole difference.

`are_conflicts_in_file`

(optional) Indicates whether the changed file contains conflicts.

### DBMS_CLOUD_OCI_DEVOPS_DIFF_RESPONSE_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_devops_diff_response_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_DIFF_RESPONSE_T Type

Response object for obtaining list of changed files.

Syntax
```

```

Fields

Field Description

`are_all_changes_included`

(optional) Boolean value to indicate if all changes are included in the response.

`change_type_count`

(optional) Count of each type of change in difference.

`common_commit`

(optional) The ID of the common commit between source and target.

`commits_ahead_count`

(optional) The number of commits source is ahead of target by.

`commits_behind_count`

(optional) The number of commits source is behind target by.

`added_lines_count`

(optional) The number of lines added in whole difference.

`deleted_lines_count`

(optional) The number of lines deleted in whole difference.

`changes`

(required) List of changes in the difference.

### DBMS_CLOUD_OCI_DEVOPS_ERROR_T Type

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

### DBMS_CLOUD_OCI_DEVOPS_FILE_DIFF_RESPONSE_T Type

Response object for showing differences for a file between two commits.

Syntax
```

```

Fields

Field Description

`old_path`

(optional) The path on the base version to the changed object.

`new_path`

(optional) The path on the target version to the changed object.

`old_id`

(optional) The ID of the changed object on the base version.

`new_id`

(optional) The ID of the changed object on the target version.

`are_conflicts_in_file`

(optional) Indicates whether the changed file contains conflicts.

`is_large`

(optional) Indicates whether the file is large.

`is_binary`

(optional) Indicates whether the file is binary.

`changes`

(required) List of changed section in the file.

### DBMS_CLOUD_OCI_DEVOPS_FILE_LINE_DETAILS_T Type

Object containing the details of a line in a file.

Syntax
```

```

Fields

Field Description

`line_number`

(required) The line number.

`line_content`

(required) The content of the line.

### DBMS_CLOUD_OCI_DEVOPS_FUNCTION_DEPLOY_ENVIRONMENT_T Type

Specifies the Function environment.

Syntax
```

```

`dbms_cloud_oci_devops_function_deploy_environment_t`is a subtype of the`dbms_cloud_oci_devops_deploy_environment_t`type.

Fields

Field Description

`function_id`

(required) The OCID of the Function.

### DBMS_CLOUD_OCI_DEVOPS_FUNCTION_DEPLOY_ENVIRONMENT_SUMMARY_T Type

Specifies the Function environment.

Syntax
```

```

`dbms_cloud_oci_devops_function_deploy_environment_summary_t`is a subtype of the`dbms_cloud_oci_devops_deploy_environment_summary_t`type.

Fields

Field Description

`function_id`

(required) The OCID of the Function.

### DBMS_CLOUD_OCI_DEVOPS_FUNCTION_DEPLOY_STAGE_T Type

Specifies the Function stage.

Syntax
```

```

`dbms_cloud_oci_devops_function_deploy_stage_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_t`type.

Fields

Field Description

`function_deploy_environment_id`

(required) Function environment OCID.

`docker_image_deploy_artifact_id`

(required) A Docker image artifact OCID.

`config`

(optional) User provided key and value pair configuration, which is assigned through constants or parameter.

`max_memory_in_m_bs`

(optional) Maximum usable memory for the Function (in MB).

`function_timeout_in_seconds`

(optional) Timeout for execution of the Function. Value in seconds.

### DBMS_CLOUD_OCI_DEVOPS_FUNCTION_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type

Specifies the execution details for Function deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_function_deploy_stage_execution_progress_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_execution_progress_t`type.

### DBMS_CLOUD_OCI_DEVOPS_FUNCTION_DEPLOY_STAGE_SUMMARY_T Type

Specifies the Function stage.

Syntax
```

```

`dbms_cloud_oci_devops_function_deploy_stage_summary_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_summary_t`type.

Fields

Field Description

`function_deploy_environment_id`

(required) Function environment OCID.

`docker_image_deploy_artifact_id`

(required) A Docker image artifact OCID.

`config`

(optional) User provided key and value pair configuration, which is assigned through constants or parameter.

`max_memory_in_m_bs`

(optional) Maximum usable memory for the Function (in MB).

`function_timeout_in_seconds`

(optional) Timeout for execution of the Function. Value in seconds.

### DBMS_CLOUD_OCI_DEVOPS_GENERIC_DELIVERED_ARTIFACT_T Type

Details of the generic artifacts delivered through the Deliver Artifacts stage.

Syntax
```

```

`dbms_cloud_oci_devops_generic_delivered_artifact_t`is a subtype of the`dbms_cloud_oci_devops_delivered_artifact_t`type.

Fields

Field Description

`artifact_repository_id`

(optional) The OCID of the artifact registry repository used by the DeliverArtifactStage

`delivered_artifact_id`

(required) The OCID of the artifact pushed by the Deliver Artifacts stage.

`path`

(optional) Path of the repository where artifact was pushed

`version`

(optional) Version of the artifact pushed

### DBMS_CLOUD_OCI_DEVOPS_GENERIC_DEPLOY_ARTIFACT_SOURCE_T Type

Specifies the Artifact Registry source details.

Syntax
```

```

`dbms_cloud_oci_devops_generic_deploy_artifact_source_t`is a subtype of the`dbms_cloud_oci_devops_deploy_artifact_source_t`type.

Fields

Field Description

`repository_id`

(required) The OCID of a repository.

`deploy_artifact_path`

(required) Specifies the artifact path in the repository.

`deploy_artifact_version`

(required) Users can set this as a placeholder value that refers to a pipeline parameter, for example, ${appVersion}.

### DBMS_CLOUD_OCI_DEVOPS_GITHUB_ACCESS_TOKEN_CONNECTION_T Type

The properties that define a connection of the type `GITHUB_ACCESS_TOKEN`. This type corresponds to a connection in GitHub that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_devops_github_access_token_connection_t`is a subtype of the`dbms_cloud_oci_devops_connection_t`type.

Fields

Field Description

`access_token`

(required) The OCID of personal access token saved in secret store.

### DBMS_CLOUD_OCI_DEVOPS_GITHUB_ACCESS_TOKEN_CONNECTION_SUMMARY_T Type

Summary information for a connection of the type `GITHUB_ACCESS_TOKEN`. This type corresponds to a connection in GitHub that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_devops_github_access_token_connection_summary_t`is a subtype of the`dbms_cloud_oci_devops_connection_summary_t`type.

Fields

Field Description

`access_token`

(required) The OCID of personal access token saved in secret store.

### DBMS_CLOUD_OCI_DEVOPS_GITHUB_BUILD_RUN_SOURCE_T Type

Specifies details of build run through GitHub.

Syntax
```

```

`dbms_cloud_oci_devops_github_build_run_source_t`is a subtype of the`dbms_cloud_oci_devops_build_run_source_t`type.

Fields

Field Description

`trigger_id`

(required) The trigger that invoked the build run.

`trigger_info`

(required)

### DBMS_CLOUD_OCI_DEVOPS_GITHUB_BUILD_SOURCE_T Type

GitHub build source for Build stage.

Syntax
```

```

`dbms_cloud_oci_devops_github_build_source_t`is a subtype of the`dbms_cloud_oci_devops_build_source_t`type.

Fields

Field Description

`connection_id`

(required) Connection identifier pertinent to GitHub source provider.

### DBMS_CLOUD_OCI_DEVOPS_GITHUB_FILTER_ATTRIBUTES_T Type

Attributes to filter GitHub events.

Syntax
```

```

Fields

Field Description

`head_ref`

(optional) Branch for push event; source branch for pull requests.

`base_ref`

(optional) The target branch for pull requests; not applicable for push requests.

`file_filter`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_GITHUB_FILTER_EXCLUSION_ATTRIBUTES_T Type

Attributes to filter GitHub events. File filter criteria - Changes only affecting excluded files will not invoke a build. if both include and exclude filter are used then exclusion filter will be applied on the result set of inclusion filter.

Syntax
```

```

Fields

Field Description

`file_filter`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_GITHUB_FILTER_T Type

The filter for GitHub events.

Syntax
```

```

`dbms_cloud_oci_devops_github_filter_t`is a subtype of the`dbms_cloud_oci_devops_filter_t`type.

Fields

Field Description

`events`

(optional) The events, for example, PUSH, PULL_REQUEST_MERGE.

Allowed values are: 'PUSH', 'PULL_REQUEST_CREATED', 'PULL_REQUEST_UPDATED', 'PULL_REQUEST_REOPENED', 'PULL_REQUEST_MERGED'

`include`

(optional)

`exclude`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_GITHUB_TRIGGER_T Type

Trigger specific to GitHub.

Syntax
```

```

`dbms_cloud_oci_devops_github_trigger_t`is a subtype of the`dbms_cloud_oci_devops_trigger_t`type.

Fields

Field Description

`trigger_url`

(required) The endpoint that listens to trigger events.

`connection_id`

(optional) The OCID of the connection resource used to get details for triggered events.

### DBMS_CLOUD_OCI_DEVOPS_GITHUB_TRIGGER_CREATE_RESULT_T Type

Trigger create response specific to GitHub.

Syntax
```

```

`dbms_cloud_oci_devops_github_trigger_create_result_t`is a subtype of the`dbms_cloud_oci_devops_trigger_create_result_t`type.

Fields

Field Description

`secret`

(required) The secret used to validate the incoming trigger call. This is visible only after the resource is created.

`trigger_url`

(required) The endpoint that listens to trigger events.

`connection_id`

(optional) The OCID of the connection resource used to get details for triggered events.

### DBMS_CLOUD_OCI_DEVOPS_GITHUB_TRIGGER_SUMMARY_T Type

Summary of the GitHub trigger.

Syntax
```

```

`dbms_cloud_oci_devops_github_trigger_summary_t`is a subtype of the`dbms_cloud_oci_devops_trigger_summary_t`type.

Fields

Field Description

`connection_id`

(optional) The OCID of the connection resource used to get details for triggered events.

### DBMS_CLOUD_OCI_DEVOPS_GITLAB_ACCESS_TOKEN_CONNECTION_T Type

The properties that define a connection of the type `GITLAB_ACCESS_TOKEN`. This type corresponds to a connection in GitLab that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_devops_gitlab_access_token_connection_t`is a subtype of the`dbms_cloud_oci_devops_connection_t`type.

Fields

Field Description

`access_token`

(required) The OCID of personal access token saved in secret store.

### DBMS_CLOUD_OCI_DEVOPS_GITLAB_ACCESS_TOKEN_CONNECTION_SUMMARY_T Type

Summary information for a connection of the type `GITLAB_ACCESS_TOKEN`. This type corresponds to a connection in GitLab that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_devops_gitlab_access_token_connection_summary_t`is a subtype of the`dbms_cloud_oci_devops_connection_summary_t`type.

Fields

Field Description

`access_token`

(required) The OCID of personal access token saved in secret store.

### DBMS_CLOUD_OCI_DEVOPS_GITLAB_BUILD_RUN_SOURCE_T Type

Specifies details of build run through GitLab.

Syntax
```

```

`dbms_cloud_oci_devops_gitlab_build_run_source_t`is a subtype of the`dbms_cloud_oci_devops_build_run_source_t`type.

Fields

Field Description

`trigger_id`

(required) The trigger that invoked the build run.

`trigger_info`

(required)

### DBMS_CLOUD_OCI_DEVOPS_GITLAB_BUILD_SOURCE_T Type

GitLab build source for Build stage.

Syntax
```

```

`dbms_cloud_oci_devops_gitlab_build_source_t`is a subtype of the`dbms_cloud_oci_devops_build_source_t`type.

Fields

Field Description

`connection_id`

(required) Connection identifier pertinent to GitLab source provider.

### DBMS_CLOUD_OCI_DEVOPS_GITLAB_FILTER_ATTRIBUTES_T Type

Attributes to filter GitLab events.

Syntax
```

```

Fields

Field Description

`head_ref`

(optional) Branch for push event; source branch for pull requests.

`base_ref`

(optional) The target branch for pull requests; not applicable for push requests.

`file_filter`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_GITLAB_FILTER_EXCLUSION_ATTRIBUTES_T Type

Attributes to filter GitLab events. File filter criteria - Changes only affecting excluded files will not invoke a build. if both include and exclude filter are used then exclusion filter will be applied on the result set of inclusion filter.

Syntax
```

```

Fields

Field Description

`file_filter`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_GITLAB_FILTER_T Type

The filter for GitLab events.

Syntax
```

```

`dbms_cloud_oci_devops_gitlab_filter_t`is a subtype of the`dbms_cloud_oci_devops_filter_t`type.

Fields

Field Description

`events`

(optional) The events, for example, PUSH, PULL_REQUEST_MERGE.

Allowed values are: 'PUSH', 'PULL_REQUEST_CREATED', 'PULL_REQUEST_UPDATED', 'PULL_REQUEST_REOPENED', 'PULL_REQUEST_MERGED'

`include`

(optional)

`exclude`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_GITLAB_SERVER_ACCESS_TOKEN_CONNECTION_T Type

The properties that define a connection of the type `GITLAB_SERVER_ACCESS_TOKEN`. This type corresponds to a connection in GitLab self-hosted server that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_devops_gitlab_server_access_token_connection_t`is a subtype of the`dbms_cloud_oci_devops_connection_t`type.

Fields

Field Description

`access_token`

(required) The OCID of personal access token saved in secret store.

`base_url`

(required) The baseUrl of the hosted GitLabServer.

`tls_verify_config`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_GITLAB_SERVER_ACCESS_TOKEN_CONNECTION_SUMMARY_T Type

Summary information for a connection of the type `GITLAB_SERVER_ACCESS_TOKEN`. This type corresponds to a connection in GitLab that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_devops_gitlab_server_access_token_connection_summary_t`is a subtype of the`dbms_cloud_oci_devops_connection_summary_t`type.

Fields

Field Description

`access_token`

(required) The OCID of personal access token saved in secret store.

`base_url`

(required) The baseUrl of the hosted GitLabServer.

`tls_verify_config`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_GITLAB_SERVER_BUILD_RUN_SOURCE_T Type

Specifies details of build run through GitLab self-hosted Server.

Syntax
```

```

`dbms_cloud_oci_devops_gitlab_server_build_run_source_t`is a subtype of the`dbms_cloud_oci_devops_build_run_source_t`type.

Fields

Field Description

`trigger_id`

(required) The trigger that invoked the build run.

`trigger_info`

(required)

### DBMS_CLOUD_OCI_DEVOPS_GITLAB_SERVER_BUILD_SOURCE_T Type

GitLab self-hosted Server Build Source for Build Stage

Syntax
```

```

`dbms_cloud_oci_devops_gitlab_server_build_source_t`is a subtype of the`dbms_cloud_oci_devops_build_source_t`type.

Fields

Field Description

`connection_id`

(required) Connection identifier pertinent to GitLab Server source provider

### DBMS_CLOUD_OCI_DEVOPS_GITLAB_SERVER_FILTER_ATTRIBUTES_T Type

Attributes to filter GitLab self-hosted server events.

Syntax
```

```

Fields

Field Description

`head_ref`

(optional) Branch for push event; source branch for pull requests.

`base_ref`

(optional) The target branch for pull requests; not applicable for push requests.

`file_filter`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_GITLAB_SERVER_FILTER_EXCLUSION_ATTRIBUTES_T Type

Attributes to filter GitLab self-hosted server events. File filter criteria - Changes only affecting excluded files will not invoke a build. if both include and exclude filter are used then exclusion filter will be applied on the result set of inclusion filter.

Syntax
```

```

Fields

Field Description

`file_filter`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_GITLAB_SERVER_FILTER_T Type

The filter for GitLab self-hosted events.

Syntax
```

```

`dbms_cloud_oci_devops_gitlab_server_filter_t`is a subtype of the`dbms_cloud_oci_devops_filter_t`type.

Fields

Field Description

`events`

(optional) The events, for example, PUSH, PULL_REQUEST_MERGE.

Allowed values are: 'PUSH', 'PULL_REQUEST_CREATED', 'PULL_REQUEST_UPDATED', 'PULL_REQUEST_REOPENED', 'PULL_REQUEST_MERGED'

`include`

(optional)

`exclude`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_GITLAB_SERVER_TRIGGER_T Type

Trigger specific to GitLab self-hosted server.

Syntax
```

```

`dbms_cloud_oci_devops_gitlab_server_trigger_t`is a subtype of the`dbms_cloud_oci_devops_trigger_t`type.

Fields

Field Description

`trigger_url`

(required) The endpoint that listens to trigger events.

### DBMS_CLOUD_OCI_DEVOPS_GITLAB_SERVER_TRIGGER_CREATE_RESULT_T Type

Trigger create response specific to GitLab self-hosted server.

Syntax
```

```

`dbms_cloud_oci_devops_gitlab_server_trigger_create_result_t`is a subtype of the`dbms_cloud_oci_devops_trigger_create_result_t`type.

Fields

Field Description

`secret`

(required) The secret used to validate the incoming trigger call. This is visible only after the resource is created.

`trigger_url`

(required) The endpoint that listens to trigger events.

### DBMS_CLOUD_OCI_DEVOPS_GITLAB_SERVER_TRIGGER_SUMMARY_T Type

Summary of the GitLab self-hosted server trigger.

Syntax
```

```

`dbms_cloud_oci_devops_gitlab_server_trigger_summary_t`is a subtype of the`dbms_cloud_oci_devops_trigger_summary_t`type.

### DBMS_CLOUD_OCI_DEVOPS_GITLAB_TRIGGER_T Type

Trigger specific to GitLab.

Syntax
```

```

`dbms_cloud_oci_devops_gitlab_trigger_t`is a subtype of the`dbms_cloud_oci_devops_trigger_t`type.

Fields

Field Description

`trigger_url`

(required) The endpoint that listens to trigger events.

`connection_id`

(optional) The OCID of the connection resource used to get details for triggered events.

### DBMS_CLOUD_OCI_DEVOPS_GITLAB_TRIGGER_CREATE_RESULT_T Type

Trigger create response specific to GitLab.

Syntax
```

```

`dbms_cloud_oci_devops_gitlab_trigger_create_result_t`is a subtype of the`dbms_cloud_oci_devops_trigger_create_result_t`type.

Fields

Field Description

`secret`

(required) The secret used to validate the incoming trigger call. This is visible only after the resource is created.

`trigger_url`

(required) The endpoint that listens to trigger events.

`connection_id`

(optional) The OCID of the connection resource used to get details for triggered events.

### DBMS_CLOUD_OCI_DEVOPS_GITLAB_TRIGGER_SUMMARY_T Type

Summary of the GitLab trigger.

Syntax
```

```

`dbms_cloud_oci_devops_gitlab_trigger_summary_t`is a subtype of the`dbms_cloud_oci_devops_trigger_summary_t`type.

Fields

Field Description

`connection_id`

(optional) The OCID of the connection resource used to get details for triggered events.

### DBMS_CLOUD_OCI_DEVOPS_VERIFICATION_KEY_SOURCE_T Type

The source of the verification material.

Syntax
```

```

Fields

Field Description

`verification_key_source_type`

(required) Specifies type of verification material.

Allowed values are: 'VAULT_SECRET', 'INLINE_PUBLIC_KEY', 'NONE'

### DBMS_CLOUD_OCI_DEVOPS_HELM_REPOSITORY_DEPLOY_ARTIFACT_SOURCE_T Type

Specifies Helm chart source details.

Syntax
```

```

`dbms_cloud_oci_devops_helm_repository_deploy_artifact_source_t`is a subtype of the`dbms_cloud_oci_devops_deploy_artifact_source_t`type.

Fields

Field Description

`chart_url`

(required) The URL of an OCIR repository.

`deploy_artifact_version`

(required) Users can set this as a placeholder value that refers to a pipeline parameter, for example, ${appVersion}.

`helm_verification_key_source`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_INLINE_DEPLOY_ARTIFACT_SOURCE_T Type

Specifies the inline deployment artifact source details.

Syntax
```

```

`dbms_cloud_oci_devops_inline_deploy_artifact_source_t`is a subtype of the`dbms_cloud_oci_devops_deploy_artifact_source_t`type.

Fields

Field Description

`base64_encoded_content`

(required) base64 Encoded String

### DBMS_CLOUD_OCI_DEVOPS_INLINE_PUBLIC_KEY_VERIFICATION_KEY_SOURCE_T Type

Specifies the Inline public key verification source details

Syntax
```

```

`dbms_cloud_oci_devops_inline_public_key_verification_key_source_t`is a subtype of the`dbms_cloud_oci_devops_verification_key_source_t`type.

Fields

Field Description

`current_public_key`

(required) Current version of Base64 encoding of the public key which is in binary GPG exported format.

`previous_public_key`

(optional) Previous version of Base64 encoding of the public key which is in binary GPG exported format. This would be used for key rotation scenarios.

### DBMS_CLOUD_OCI_DEVOPS_INVOKE_FUNCTION_DEPLOY_STAGE_T Type

Specifies Invoke Function stage.

Syntax
```

```

`dbms_cloud_oci_devops_invoke_function_deploy_stage_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_t`type.

Fields

Field Description

`function_deploy_environment_id`

(required) Function environment OCID.

`deploy_artifact_id`

(optional) Optional artifact OCID. The artifact will be included in the body for the function invocation during the stage's execution. If the DeployArtifact.argumentSubstituitionMode is set to SUBSTITUTE_PLACEHOLDERS, then the pipeline parameter values will be used to replace the placeholders in the artifact content.

`is_async`

(required) A boolean flag specifies whether this stage executes asynchronously.

`is_validation_enabled`

(required) A boolean flag specifies whether the invoked function must be validated.

### DBMS_CLOUD_OCI_DEVOPS_INVOKE_FUNCTION_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type

Specifies the Invoke Function stage specific execution details.

Syntax
```

```

`dbms_cloud_oci_devops_invoke_function_deploy_stage_execution_progress_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_execution_progress_t`type.

### DBMS_CLOUD_OCI_DEVOPS_INVOKE_FUNCTION_DEPLOY_STAGE_SUMMARY_T Type

Specifies Invoke Function stage.

Syntax
```

```

`dbms_cloud_oci_devops_invoke_function_deploy_stage_summary_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_summary_t`type.

Fields

Field Description

`function_deploy_environment_id`

(required) Function environment OCID.

`deploy_artifact_id`

(optional) Optional artifact OCID. The artifact will be included in the body for the function invocation during the stage's execution. If the DeployArtifact.argumentSubstituitionMode is set to SUBSTITUTE_PLACEHOLDERS, then the pipeline parameter values will be used to replace the placeholders in the artifact content.

`is_async`

(required) A boolean flag specifies whether this stage executes asynchronously.

`is_validation_enabled`

(required) A boolean flag specifies whether the invoked function must be validated.

### DBMS_CLOUD_OCI_DEVOPS_LOAD_BALANCER_TRAFFIC_SHIFT_DEPLOY_STAGE_T Type

Specifies load balancer traffic shift stage.

Syntax
```

```

`dbms_cloud_oci_devops_load_balancer_traffic_shift_deploy_stage_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_t`type.

Fields

Field Description

`blue_backend_ips`

(required)

`green_backend_ips`

(required)

`traffic_shift_target`

(required) Specifies the target or destination backend set. Example: BLUE - Traffic from the existing backends of managed Load Balance Listener to blue Backend IPs, as per rolloutPolicy. GREEN - Traffic from the existing backends of managed Load Balance Listener to green Backend IPs as per rolloutPolicy.

Allowed values are: 'AUTO_SELECT', 'BLUE', 'GREEN'

`rollout_policy`

(required)

`load_balancer_config`

(required)

`rollback_policy`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_LOAD_BALANCER_TRAFFIC_SHIFT_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type

Specifies the load balancer Traffic Shift stage execution details.

Syntax
```

```

`dbms_cloud_oci_devops_load_balancer_traffic_shift_deploy_stage_execution_progress_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_execution_progress_t`type.

### DBMS_CLOUD_OCI_DEVOPS_LOAD_BALANCER_TRAFFIC_SHIFT_DEPLOY_STAGE_SUMMARY_T Type

Specifies load balancer traffic shift stage.

Syntax
```

```

`dbms_cloud_oci_devops_load_balancer_traffic_shift_deploy_stage_summary_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_summary_t`type.

Fields

Field Description

`blue_backend_ips`

(required)

`green_backend_ips`

(required)

`traffic_shift_target`

(required) Specifies the target or destination backend set. Example: BLUE - Traffic from the existing backends of managed Load Balance Listener to blue Backend IPs, as per rolloutPolicy. GREEN - Traffic from the existing backends of managed Load Balance Listener to blue Backend IPs as per rolloutPolicy.

`rollout_policy`

(required)

`load_balancer_config`

(required)

`rollback_policy`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_MANUAL_APPROVAL_DEPLOY_STAGE_T Type

Specifies the manual approval stage.

Syntax
```

```

`dbms_cloud_oci_devops_manual_approval_deploy_stage_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_t`type.

Fields

Field Description

`approval_policy`

(required)

### DBMS_CLOUD_OCI_DEVOPS_MANUAL_APPROVAL_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type

Specifies the manual approval stage specific execution details.

Syntax
```

```

`dbms_cloud_oci_devops_manual_approval_deploy_stage_execution_progress_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_execution_progress_t`type.

Fields

Field Description

`approval_actions`

(optional) Specifies the Canary approval actions.

### DBMS_CLOUD_OCI_DEVOPS_MANUAL_APPROVAL_DEPLOY_STAGE_SUMMARY_T Type

Specifies the manual approval stage.

Syntax
```

```

`dbms_cloud_oci_devops_manual_approval_deploy_stage_summary_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_summary_t`type.

Fields

Field Description

`approval_policy`

(required)

### DBMS_CLOUD_OCI_DEVOPS_MANUAL_BUILD_RUN_SOURCE_T Type

Specifies details of build runs triggered manually through the API.

Syntax
```

```

`dbms_cloud_oci_devops_manual_build_run_source_t`is a subtype of the`dbms_cloud_oci_devops_build_run_source_t`type.

### DBMS_CLOUD_OCI_DEVOPS_NGINX_BLUE_GREEN_STRATEGY_T Type

Specifies the NGINX blue green release strategy.

Syntax
```

```

`dbms_cloud_oci_devops_nginx_blue_green_strategy_t`is a subtype of the`dbms_cloud_oci_devops_oke_blue_green_strategy_t`type.

Fields

Field Description

`namespace_a`

(required) Namespace A for deployment. Example: namespaceA - first Namespace name.

`namespace_b`

(required) Namespace B for deployment. Example: namespaceB - second Namespace name.

`ingress_name`

(required) Name of the Ingress resource.

### DBMS_CLOUD_OCI_DEVOPS_NGINX_CANARY_STRATEGY_T Type

Specifies the NGINX canary release strategy.

Syntax
```

```

`dbms_cloud_oci_devops_nginx_canary_strategy_t`is a subtype of the`dbms_cloud_oci_devops_oke_canary_strategy_t`type.

Fields

Field Description

`namespace`

(required) Canary namespace to be used for Kubernetes canary deployment. Example: canary - Name of the Canary namespace.

`ingress_name`

(required) Name of the Ingress resource.

### DBMS_CLOUD_OCI_DEVOPS_NO_DEPLOY_STAGE_ROLLBACK_POLICY_T Type

Specifies the no rollback policy for a Stage on failure.

Syntax
```

```

`dbms_cloud_oci_devops_no_deploy_stage_rollback_policy_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_rollback_policy_t`type.

### DBMS_CLOUD_OCI_DEVOPS_NONE_VERIFICATION_KEY_SOURCE_T Type

Allows user to opt out of Verification key source

Syntax
```

```

`dbms_cloud_oci_devops_none_verification_key_source_t`is a subtype of the`dbms_cloud_oci_devops_verification_key_source_t`type.

### DBMS_CLOUD_OCI_DEVOPS_OCIR_DEPLOY_ARTIFACT_SOURCE_T Type

Specifies the OCIR details.

Syntax
```

```

`dbms_cloud_oci_devops_ocir_deploy_artifact_source_t`is a subtype of the`dbms_cloud_oci_devops_deploy_artifact_source_t`type.

Fields

Field Description

`image_uri`

(required) Specifies OCIR image path - optionally include tag.

`image_digest`

(optional) Specifies image digest for the version of the image.

### DBMS_CLOUD_OCI_DEVOPS_OKE_BLUE_GREEN_DEPLOY_STAGE_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster Blue-Green deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_oke_blue_green_deploy_stage_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_t`type.

Fields

Field Description

`oke_cluster_deploy_environment_id`

(required) Kubernetes cluster environment OCID for deployment.

`kubernetes_manifest_deploy_artifact_ids`

(required) List of Kubernetes manifest artifact OCIDs

`blue_green_strategy`

(required)

### DBMS_CLOUD_OCI_DEVOPS_OKE_BLUE_GREEN_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster Blue-Green deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_oke_blue_green_deploy_stage_execution_progress_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_execution_progress_t`type.

Fields

Field Description

`namespace`

(optional) Namespace either environment A or environment B where artifacts are deployed. Example: blue - Name of the namespace where blue artifacts were deployed. green - Name of the namespace where green artifacts were deployed.

### DBMS_CLOUD_OCI_DEVOPS_OKE_BLUE_GREEN_DEPLOY_STAGE_SUMMARY_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster Blue-Green deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_oke_blue_green_deploy_stage_summary_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_summary_t`type.

Fields

Field Description

`oke_cluster_deploy_environment_id`

(required) Kubernetes cluster environment OCID for deployment.

`kubernetes_manifest_deploy_artifact_ids`

(required) List of Kubernetes manifest artifact OCIDs.

`blue_green_strategy`

(required)

### DBMS_CLOUD_OCI_DEVOPS_OKE_BLUE_GREEN_TRAFFIC_SHIFT_DEPLOY_STAGE_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster blue-green deployment traffic shift stage.

Syntax
```

```

`dbms_cloud_oci_devops_oke_blue_green_traffic_shift_deploy_stage_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_t`type.

Fields

Field Description

`oke_blue_green_deploy_stage_id`

(required) The OCID of the upstream OKE blue-green deployment stage in this pipeline.

### DBMS_CLOUD_OCI_DEVOPS_OKE_BLUE_GREEN_TRAFFIC_SHIFT_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster Blue-Green deployment traffic shift stage.

Syntax
```

```

`dbms_cloud_oci_devops_oke_blue_green_traffic_shift_deploy_stage_execution_progress_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_execution_progress_t`type.

Fields

Field Description

`namespace`

(optional) Namespace where traffic is going. Example: blue - Traffic is going to blue namespace. green - Traffic is going to green namespace.

### DBMS_CLOUD_OCI_DEVOPS_OKE_BLUE_GREEN_TRAFFIC_SHIFT_DEPLOY_STAGE_SUMMARY_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster blue-green deployment traffic shift stage.

Syntax
```

```

`dbms_cloud_oci_devops_oke_blue_green_traffic_shift_deploy_stage_summary_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_summary_t`type.

Fields

Field Description

`oke_blue_green_deploy_stage_id`

(required) The OCID of the upstream OKE blue-green deployment stage in this pipeline.

### DBMS_CLOUD_OCI_DEVOPS_OKE_CANARY_APPROVAL_DEPLOY_STAGE_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster canary deployment approval stage.

Syntax
```

```

`dbms_cloud_oci_devops_oke_canary_approval_deploy_stage_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_t`type.

Fields

Field Description

`oke_canary_traffic_shift_deploy_stage_id`

(required) The OCID of an upstream OKE canary deployment traffic shift stage in this pipeline.

`approval_policy`

(required)

### DBMS_CLOUD_OCI_DEVOPS_OKE_CANARY_APPROVAL_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster Canary approval stage.

Syntax
```

```

`dbms_cloud_oci_devops_oke_canary_approval_deploy_stage_execution_progress_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_execution_progress_t`type.

Fields

Field Description

`approval_actions`

(optional) Specifies the Canary approval actions.

### DBMS_CLOUD_OCI_DEVOPS_OKE_CANARY_APPROVAL_DEPLOY_STAGE_SUMMARY_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster canary deployment approval stage.

Syntax
```

```

`dbms_cloud_oci_devops_oke_canary_approval_deploy_stage_summary_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_summary_t`type.

Fields

Field Description

`oke_canary_traffic_shift_deploy_stage_id`

(required) The OCID of an upstream OKE canary deployment traffic shift stage in this pipeline.

`approval_policy`

(required)

### DBMS_CLOUD_OCI_DEVOPS_OKE_CANARY_DEPLOY_STAGE_T Type

Specifies the Container Engine for Kubernetes (OKE) Canary deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_oke_canary_deploy_stage_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_t`type.

Fields

Field Description

`oke_cluster_deploy_environment_id`

(required) Kubernetes cluster environment OCID for deployment.

`kubernetes_manifest_deploy_artifact_ids`

(required) List of Kubernetes manifest artifact OCIDs.

`canary_strategy`

(required)

### DBMS_CLOUD_OCI_DEVOPS_OKE_CANARY_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster Canary deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_oke_canary_deploy_stage_execution_progress_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_execution_progress_t`type.

Fields

Field Description

`namespace`

(optional) The namespace of OKE Canary deployment.

### DBMS_CLOUD_OCI_DEVOPS_OKE_CANARY_DEPLOY_STAGE_SUMMARY_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster Canary deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_oke_canary_deploy_stage_summary_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_summary_t`type.

Fields

Field Description

`oke_cluster_deploy_environment_id`

(required) Kubernetes cluster environment OCID for deployment.

`kubernetes_manifest_deploy_artifact_ids`

(required) List of Kubernetes manifest artifact OCIDs.

`canary_strategy`

(required)

### DBMS_CLOUD_OCI_DEVOPS_OKE_CANARY_TRAFFIC_SHIFT_DEPLOY_STAGE_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster canary deployment traffic shift stage.

Syntax
```

```

`dbms_cloud_oci_devops_oke_canary_traffic_shift_deploy_stage_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_t`type.

Fields

Field Description

`oke_canary_deploy_stage_id`

(required) The OCID of an upstream OKE canary deployment stage in this pipeline.

`rollout_policy`

(required)

### DBMS_CLOUD_OCI_DEVOPS_OKE_CANARY_TRAFFIC_SHIFT_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster Canary deployment traffic shift stage.

Syntax
```

```

`dbms_cloud_oci_devops_oke_canary_traffic_shift_deploy_stage_execution_progress_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_execution_progress_t`type.

### DBMS_CLOUD_OCI_DEVOPS_OKE_CANARY_TRAFFIC_SHIFT_DEPLOY_STAGE_SUMMARY_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster canary deployment traffic shift stage.

Syntax
```

```

`dbms_cloud_oci_devops_oke_canary_traffic_shift_deploy_stage_summary_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_summary_t`type.

Fields

Field Description

`oke_canary_deploy_stage_id`

(required) The OCID of an upstream OKE canary deployment stage in this pipeline.

`rollout_policy`

(required)

### DBMS_CLOUD_OCI_DEVOPS_OKE_CLUSTER_DEPLOY_ENVIRONMENT_T Type

Specifies the Kubernetes cluster environment.

Syntax
```

```

`dbms_cloud_oci_devops_oke_cluster_deploy_environment_t`is a subtype of the`dbms_cloud_oci_devops_deploy_environment_t`type.

Fields

Field Description

`cluster_id`

(required) The OCID of the Kubernetes cluster.

`network_channel`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_OKE_CLUSTER_DEPLOY_ENVIRONMENT_SUMMARY_T Type

Specifies the Kubernetes cluster environment.

Syntax
```

```

`dbms_cloud_oci_devops_oke_cluster_deploy_environment_summary_t`is a subtype of the`dbms_cloud_oci_devops_deploy_environment_summary_t`type.

Fields

Field Description

`cluster_id`

(required) The OCID of the Kubernetes cluster.

`network_channel`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_OKE_DEPLOY_STAGE_T Type

Specifies the Container Engine for Kubernetes(OKE) cluster deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_oke_deploy_stage_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_t`type.

Fields

Field Description

`oke_cluster_deploy_environment_id`

(required) Kubernetes cluster environment OCID for deployment.

`kubernetes_manifest_deploy_artifact_ids`

(required) List of Kubernetes manifest artifact OCIDs.

`namespace`

(required) Default namespace to be used for Kubernetes deployment when not specified in the manifest.

`rollback_policy`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_OKE_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type

Specifies the execution details for a Container Engine for Kubernetes (OKE) cluster deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_oke_deploy_stage_execution_progress_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_execution_progress_t`type.

### DBMS_CLOUD_OCI_DEVOPS_OKE_DEPLOY_STAGE_SUMMARY_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_oke_deploy_stage_summary_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_summary_t`type.

Fields

Field Description

`oke_cluster_deploy_environment_id`

(required) Kubernetes cluster environment OCID for deployment.

`kubernetes_manifest_deploy_artifact_ids`

(required) List of Kubernetes manifest artifact OCIDs.

`namespace`

(required) Default namespace to be used for Kubernetes deployment when not specified in the manifest.

`rollback_policy`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_OKE_HELM_CHART_DEPLOY_STAGE_T Type

Specifies the OKE cluster deployment stage using helm charts.

Syntax
```

```

`dbms_cloud_oci_devops_oke_helm_chart_deploy_stage_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_t`type.

Fields

Field Description

`oke_cluster_deploy_environment_id`

(required) Kubernetes cluster environment OCID for deployment.

`helm_chart_deploy_artifact_id`

(required) Helm chart artifact OCID.

`values_artifact_ids`

(optional) List of values.yaml file artifact OCIDs.

`release_name`

(required) Release name of the Helm chart.

`namespace`

(optional) Default namespace to be used for Kubernetes deployment when not specified in the manifest.

`timeout_in_seconds`

(optional) Time to wait for execution of a helm stage. Defaults to 300 seconds.

`rollback_policy`

(optional)

`set_values`

(optional)

`set_string`

(optional)

`are_hooks_enabled`

(optional) Disable pre/post upgrade hooks. Set to false by default.

`should_reuse_values`

(optional) During upgrade, reuse the values of the last release and merge overrides from the command line. Set to false by default.

`should_reset_values`

(optional) During upgrade, reset the values to the ones built into the chart. It overrides shouldReuseValues. Set to false by default.

`is_force_enabled`

(optional) Force resource update through delete; or if required, recreate. Set to false by default.

`should_cleanup_on_fail`

(optional) Allow deletion of new resources created during when an upgrade fails. Set to false by default.

`max_history`

(optional) Limit the maximum number of revisions saved per release. Use 0 for no limit. Set to 10 by default

`should_skip_crds`

(optional) If set, no CRDs are installed. By default, CRDs are installed only if they are not present already. Set to false by default.

`should_skip_render_subchart_notes`

(optional) If set, renders subchart notes along with the parent. Set to false by default.

`should_not_wait`

(optional) Waits until all the resources are in a ready state to mark the release as successful. Set to false by default.

`is_debug_enabled`

(optional) Enables helm --debug option to stream output to tf stdout. Set to false by default.

### DBMS_CLOUD_OCI_DEVOPS_OKE_HELM_CHART_DEPLOY_STAGE_SUMMARY_T Type

Specifies the OKE cluster deployment stage using Helm charts.

Syntax
```

```

`dbms_cloud_oci_devops_oke_helm_chart_deploy_stage_summary_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_summary_t`type.

Fields

Field Description

`oke_cluster_deploy_environment_id`

(required) Kubernetes cluster environment OCID for deployment.

`helm_chart_deploy_artifact_id`

(required) Helm chart artifact OCID.

`values_artifact_ids`

(optional) List of values.yaml file artifact OCIDs.

`release_name`

(required) Release name of the Helm chart.

`namespace`

(optional) Default namespace to be used for Kubernetes deployment when not specified in the manifest.

`timeout_in_seconds`

(optional) Time to wait for execution of a helm stage. Defaults to 300 seconds.

`rollback_policy`

(optional)

`set_values`

(optional)

`set_string`

(optional)

`are_hooks_enabled`

(optional) Disable pre/post upgrade hooks.

`should_reuse_values`

(optional) During upgrade, reuse the values of the last release and merge overrides from the command line. Set to false by default.

`should_reset_values`

(optional) During upgrade, reset the values to the ones built into the chart. It overrides shouldReuseValues. Set to false by default.

`is_force_enabled`

(optional) Force resource update through delete; or if required, recreate. Set to false by default.

`should_cleanup_on_fail`

(optional) Allow deletion of new resources created during when an upgrade fails. Set to false by default.

`max_history`

(optional) Limit the maximum number of revisions saved per release. Use 0 for no limit. Set to 10 by default

`should_skip_crds`

(optional) If set, no CRDs are installed. By default, CRDs are installed only if they are not present already. Set to false by default.

`should_skip_render_subchart_notes`

(optional) If set, renders subchart notes along with the parent. Set to false by default.

`should_not_wait`

(optional) Waits until all the resources are in a ready state to mark the release as successful. Set to false by default.

`is_debug_enabled`

(optional) Enables helm --debug option to stream output. Set to false by default.

### DBMS_CLOUD_OCI_DEVOPS_OKE_HELM_CHART_DEPLOYMENT_STAGE_EXECUTION_PROGRESS_T Type

Specifies the execution details for Kubernetes (OKE) helm chart deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_oke_helm_chart_deployment_stage_execution_progress_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_execution_progress_t`type.

Fields

Field Description

`release_name`

(optional) Release name of the Helm chart.

`chart_url`

(optional) The URL of an OCIR repository.

`version`

(optional) The version of the helm chart stored in OCIR repository.

`namespace`

(optional) Default namespace to be used for Kubernetes deployment when not specified in the manifest.

`helm_diff`

(optional) Helm Diff output Example: Helm diff was successful data: - greeting: Version 1.0 + greeting: Version 1.1

### DBMS_CLOUD_OCI_DEVOPS_PRIVATE_ENDPOINT_CHANNEL_T Type

Specifies the configuration to access private endpoint.

Syntax
```

```

`dbms_cloud_oci_devops_private_endpoint_channel_t`is a subtype of the`dbms_cloud_oci_devops_network_channel_t`type.

Fields

Field Description

`subnet_id`

(required) The OCID of the subnet where VNIC resources will be created for private endpoint.

`nsg_ids`

(optional) An array of network security group OCIDs.

### DBMS_CLOUD_OCI_DEVOPS_PROJECT_T Type

DevOps project groups resources needed to implement the CI/CD workload. DevOps resources include artifacts, pipelines, and environments.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`name`

(required) Project name (case-sensitive).

`description`

(optional) Project description.

`compartment_id`

(required) The OCID of the compartment where the project is created.

`namespace`

(optional) Namespace associated with the project.

`notification_config`

(required)

`time_created`

(optional) Time the project was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) Time the project was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`lifecycle_state`

(optional) The current state of the project.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_PROJECT_SUMMARY_T Type

Summary of the project.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`name`

(required) Project name (case-sensitive).

`description`

(optional) Project description.

`compartment_id`

(required) The OCID of the compartment where the project is created.

`namespace`

(optional) Namespace associated with the project.

`notification_config`

(optional)

`time_created`

(optional) Time the project was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) Time the project was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`lifecycle_details`

(optional) A detailed message describing the current state. For example, can be used to provide actionable information for a resource in Failed state.

`lifecycle_state`

(optional) The current state of the project.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_PROJECT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_devops_project_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_PROJECT_COLLECTION_T Type

Results of an project search.

Syntax
```

```

Fields

Field Description

`items`

(required) List of project summary items.

### DBMS_CLOUD_OCI_DEVOPS_PUT_REPOSITORY_REF_DETAILS_T Type

The information needed to create a reference. If the reference already exists, then it can be used to update the reference.

Syntax
```

```

Fields

Field Description

`ref_type`

(required) The type of reference (BRANCH or TAG).

Allowed values are: 'BRANCH', 'TAG'

### DBMS_CLOUD_OCI_DEVOPS_PUT_REPOSITORY_BRANCH_DETAILS_T Type

The information needed to create a branch.

Syntax
```

```

`dbms_cloud_oci_devops_put_repository_branch_details_t`is a subtype of the`dbms_cloud_oci_devops_put_repository_ref_details_t`type.

Fields

Field Description

`commit_id`

(required) Commit ID pointed to by the new branch.

### DBMS_CLOUD_OCI_DEVOPS_PUT_REPOSITORY_TAG_DETAILS_T Type

The information needed to create a lightweight tag.

Syntax
```

```

`dbms_cloud_oci_devops_put_repository_tag_details_t`is a subtype of the`dbms_cloud_oci_devops_put_repository_ref_details_t`type.

Fields

Field Description

`object_id`

(required) SHA-1 hash value of the object pointed to by the tag.

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_T Type

Repositories containing the source code to build and deploy.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the repository. This value is unique and immutable.

`name`

(optional) Unique name of a repository. This value is mutable.

`compartment_id`

(required) The OCID of the repository's compartment.

`namespace`

(optional) Tenancy unique namespace.

`project_id`

(required) The OCID of the DevOps project containing the repository.

`project_name`

(optional) Unique project name in a namespace.

`ssh_url`

(optional) SSH URL that you use to git clone, pull and push.

`http_url`

(optional) HTTP URL that you use to git clone, pull and push.

`description`

(optional) Details of the repository. Avoid entering confidential information.

`default_branch`

(optional) The default branch of the repository.

`repository_type`

(optional) Type of repository: MIRRORED - Repository created by mirroring an existing repository. HOSTED - Repository created and hosted using OCI DevOps code repository.

Allowed values are: 'MIRRORED', 'HOSTED'

`mirror_repository_config`

(optional)

`time_created`

(optional) The time the repository was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) The time the repository was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`lifecycle_state`

(optional) The current state of the repository.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING'

`lifecyle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`branch_count`

(optional) The count of the branches present in the repository.

`commit_count`

(optional) The count of the commits present in the repository.

`size_in_bytes`

(optional) The size of the repository in bytes.

`trigger_build_events`

(optional) Trigger build events supported for this repository: PUSH - Build is triggered when a push event occurs. COMMIT_UPDATES - Build is triggered when new commits are mirrored into a repository.

Allowed values are: 'PUSH', 'COMMIT_UPDATES'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_AUTHOR_SUMMARY_T Type

Object containing summary of authors in a repository.

Syntax
```

```

Fields

Field Description

`author_name`

(required) Author name.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_AUTHOR_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_devops_repository_author_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_AUTHOR_COLLECTION_T Type

Result of list authors.

Syntax
```

```

Fields

Field Description

`items`

(required) List of author objects.

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_REF_T Type

Reference object with name and commit ID.

Syntax
```

```

Fields

Field Description

`ref_name`

(required) Unique reference name inside a repository.

`ref_type`

(required) The type of reference (BRANCH or TAG).

Allowed values are: 'BRANCH', 'TAG'

`full_ref_name`

(required) Unique full reference name inside a repository.

`repository_id`

(required) The OCID of the repository containing the reference.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_BRANCH_T Type

Branch related information.

Syntax
```

```

`dbms_cloud_oci_devops_repository_branch_t`is a subtype of the`dbms_cloud_oci_devops_repository_ref_t`type.

Fields

Field Description

`commit_id`

(required) Commit ID pointed to by the new branch.

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_REF_SUMMARY_T Type

Summary of a reference.

Syntax
```

```

Fields

Field Description

`ref_name`

(required) Reference name inside a repository.

`ref_type`

(required) The type of reference (BRANCH or TAG).

`full_ref_name`

(required) Unique full reference name inside a repository.

`repository_id`

(required) The OCID of the repository containing the reference.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_BRANCH_SUMMARY_T Type

Branch related information.

Syntax
```

```

`dbms_cloud_oci_devops_repository_branch_summary_t`is a subtype of the`dbms_cloud_oci_devops_repository_ref_summary_t`type.

Fields

Field Description

`commit_id`

(required) Commit ID pointed to by the new branch.

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_SUMMARY_T Type

Summary of the repository.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the repository. This value is unique and immutable.

`name`

(optional) Unique name of a repository. This value is mutable.

`compartment_id`

(required) The OCID of the repository's compartment.

`project_id`

(required) The OCID of the DevOps project containing the repository.

`namespace`

(optional) Tenancy unique namespace.

`project_name`

(optional) Unique project name in a namespace.

`description`

(optional) Details of the repository. Avoid entering confidential information.

`default_branch`

(optional) The default branch of the repository.

`repository_type`

(optional) Type of repository. Allowed values: `MIRRORED` `HOSTED`

`ssh_url`

(optional) SSH URL that you use to git clone, pull and push.

`http_url`

(optional) HTTP URL that you use to git clone, pull and push.

`mirror_repository_config`

(optional)

`time_created`

(optional) The time the repository was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_updated`

(optional) The time the repository was updated. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`lifecycle_state`

(optional) The current state of the repository.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_devops_repository_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_COLLECTION_T Type

Results of a repository search. Contains repository summary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of repositories.

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_COMMIT_T Type

Commit object with commit information.

Syntax
```

```

Fields

Field Description

`commit_id`

(required) Commit hash pointed to by reference name.

`commit_message`

(required) The commit message.

`author_name`

(optional) Name of the author of the repository.

`author_email`

(optional) Email of the author of the repository.

`committer_name`

(optional) Name of who creates the commit.

`committer_email`

(optional) Email of who creates the commit.

`parent_commit_ids`

(optional) An array of parent commit IDs of created commit.

`time_created`

(optional) The time at which commit was created.

`tree_id`

(optional) Tree information for the specified commit.

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_COMMIT_SUMMARY_T Type

Commit summary with commit information.

Syntax
```

```

Fields

Field Description

`commit_id`

(required) Commit hash pointed to by reference name.

`commit_message`

(required) The commit message.

`author_name`

(required) Name of the author of the repository.

`author_email`

(required) Email of the author of the repository.

`committer_name`

(required) Name of who creates the commit.

`committer_email`

(required) Email of who creates the commit.

`parent_commit_ids`

(required) An array of parent commit IDs of created commit.

`time_created`

(required) The time to create the commit.

`tree_id`

(required) Tree information for the specified commit.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_COMMIT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_devops_repository_commit_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_COMMIT_COLLECTION_T Type

Result of a commit search.

Syntax
```

```

Fields

Field Description

`items`

(required) List of commit objects.

### DBMS_CLOUD_OCI_DEVOPS_FILE_LINE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_devops_file_line_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_FILE_LINES_T Type

Object containing the lines of a file in a repository.

Syntax
```

```

Fields

Field Description

`lines`

(required) The list of lines in the file.

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_MIRROR_RECORD_T Type

Object containing information about a mirror record.

Syntax
```

```

Fields

Field Description

`mirror_status`

(required) Mirror status of current mirror entry. QUEUED - Mirroring Queued RUNNING - Mirroring is Running PASSED - Mirroring Passed FAILED - Mirroring Failed

Allowed values are: 'NONE', 'QUEUED', 'RUNNING', 'PASSED', 'FAILED'

`work_request_id`

(optional) Workrequest ID to track current mirror operation.

`time_enqueued`

(optional) The time to enqueue a mirror operation.

`time_started`

(optional) The time to start a mirror operation.

`time_ended`

(optional) The time taken to complete a mirror operation. Value is null if not completed.

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_MIRROR_RECORD_SUMMARY_T Type

Object containing information about a mirror record.

Syntax
```

```

Fields

Field Description

`mirror_status`

(required) Mirror status of current mirror entry. QUEUED - Mirroring Queued RUNNING - Mirroring is Running PASSED - Mirroring Passed FAILED - Mirroring Failed

Allowed values are: 'NONE', 'QUEUED', 'RUNNING', 'PASSED', 'FAILED'

`work_request_id`

(optional) Workrequest ID to track current mirror operation.

`time_enqueued`

(optional) The time to enqueue a mirror operation.

`time_started`

(optional) The time to start a mirror operation.

`time_completed`

(optional) The time to complete a mirror operation.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_MIRROR_RECORD_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_devops_repository_mirror_record_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_MIRROR_RECORD_COLLECTION_T Type

The collection of mirror entry.

Syntax
```

```

Fields

Field Description

`items`

(required) List of mirror entry objects.

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_OBJECT_T Type

Object containing information about files and directories in a repository.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of git object.

Allowed values are: 'BLOB', 'TREE', 'COMMIT'

`size_in_bytes`

(required) Size in bytes.

`sha`

(required) SHA-1 hash of git object.

`is_binary`

(optional) Flag to determine if the object contains binary file content or not.

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_PATH_SUMMARY_T Type

Object containing information about files and directories in a repository.

Syntax
```

```

Fields

Field Description

`l_type`

(optional) File or directory.

`size_in_bytes`

(optional) Size of file or directory.

`name`

(optional) Name of file or directory.

`path`

(optional) Path to file or directory in a repository.

`sha`

(optional) SHA-1 checksum of blob or tree.

`submodule_git_url`

(optional) The git URL of the submodule.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_PATH_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_devops_repository_path_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_PATH_COLLECTION_T Type

Result of list paths in a repository.

Syntax
```

```

Fields

Field Description

`items`

(required) List of objects describing files or directories in a repository.

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_REF_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_devops_repository_ref_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_REF_COLLECTION_T Type

Result of a reference search.

Syntax
```

```

Fields

Field Description

`items`

(required) List of references.

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_TAG_T Type

The information needed to create a lightweight tag.

Syntax
```

```

`dbms_cloud_oci_devops_repository_tag_t`is a subtype of the`dbms_cloud_oci_devops_repository_ref_t`type.

Fields

Field Description

`object_id`

(required) SHA-1 hash value of the object pointed to by the tag.

### DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_TAG_SUMMARY_T Type

The information needed to create a lightweight tag.

Syntax
```

```

`dbms_cloud_oci_devops_repository_tag_summary_t`is a subtype of the`dbms_cloud_oci_devops_repository_ref_summary_t`type.

Fields

Field Description

`object_id`

(required) SHA-1 hash value of the object pointed to by the tag.

### DBMS_CLOUD_OCI_DEVOPS_SERVICE_VNIC_CHANNEL_T Type

Specifies the configuration to access private resources in customer tenancy using service managed VNIC.

Syntax
```

```

`dbms_cloud_oci_devops_service_vnic_channel_t`is a subtype of the`dbms_cloud_oci_devops_network_channel_t`type.

Fields

Field Description

`subnet_id`

(required) The OCID of the subnet where private resources exist.

`nsg_ids`

(optional) An array of network security group OCIDs.

### DBMS_CLOUD_OCI_DEVOPS_SHELL_DEPLOY_STAGE_T Type

Specifies the shell stage.

Syntax
```

```

`dbms_cloud_oci_devops_shell_deploy_stage_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_t`type.

Fields

Field Description

`container_config`

(required)

`command_spec_deploy_artifact_id`

(required) The OCID of the artifact that contains the command specification.

`timeout_in_seconds`

(optional) Time to wait for execution of a shell stage. Defaults to 36000 seconds.

### DBMS_CLOUD_OCI_DEVOPS_SHELL_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type

Specifies the shell stage specific execution details.

Syntax
```

```

`dbms_cloud_oci_devops_shell_deploy_stage_execution_progress_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_execution_progress_t`type.

### DBMS_CLOUD_OCI_DEVOPS_SHELL_DEPLOY_STAGE_SUMMARY_T Type

Specifies the shell stage.

Syntax
```

```

`dbms_cloud_oci_devops_shell_deploy_stage_summary_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_summary_t`type.

Fields

Field Description

`container_config`

(required)

`command_spec_deploy_artifact_id`

(required) The OCID of the artifact that contains the command specification.

`timeout_in_seconds`

(optional) Time to wait for execution of a shell stage. Defaults to 36000 seconds.

### DBMS_CLOUD_OCI_DEVOPS_SINGLE_DEPLOY_STAGE_DEPLOYMENT_T Type

Deployment of a single stage within the pipeline.

Syntax
```

```

`dbms_cloud_oci_devops_single_deploy_stage_deployment_t`is a subtype of the`dbms_cloud_oci_devops_deployment_t`type.

Fields

Field Description

`deploy_stage_id`

(required) Specifies the OCID of the stage to be deployed.

### DBMS_CLOUD_OCI_DEVOPS_SINGLE_DEPLOY_STAGE_DEPLOYMENT_SUMMARY_T Type

Summary of single stage deployment.

Syntax
```

```

`dbms_cloud_oci_devops_single_deploy_stage_deployment_summary_t`is a subtype of the`dbms_cloud_oci_devops_deployment_summary_t`type.

Fields

Field Description

`deploy_stage_id`

(required) Specifies the OCID of the stage to be deployed.

### DBMS_CLOUD_OCI_DEVOPS_SINGLE_DEPLOY_STAGE_REDEPLOYMENT_T Type

Redeployment of a single stage of a previous deployment.

Syntax
```

```

`dbms_cloud_oci_devops_single_deploy_stage_redeployment_t`is a subtype of the`dbms_cloud_oci_devops_deployment_t`type.

Fields

Field Description

`previous_deployment_id`

(optional) Specifies the OCID of the previous deployment to be redeployed.

`deploy_stage_id`

(required) Specifies the OCID of the stage to be redeployed.

### DBMS_CLOUD_OCI_DEVOPS_SINGLE_DEPLOY_STAGE_REDEPLOYMENT_SUMMARY_T Type

Summary of a single stage redeployment.

Syntax
```

```

`dbms_cloud_oci_devops_single_deploy_stage_redeployment_summary_t`is a subtype of the`dbms_cloud_oci_devops_deployment_summary_t`type.

Fields

Field Description

`previous_deployment_id`

(optional) Specifies the OCID of the previous deployment to be redeployed.

`deploy_stage_id`

(required) Specifies the OCID of the stage to be redeployed.

### DBMS_CLOUD_OCI_DEVOPS_TRIGGER_BUILD_PIPELINE_ACTION_T Type

The action to trigger a build pipeline.

Syntax
```

```

`dbms_cloud_oci_devops_trigger_build_pipeline_action_t`is a subtype of the`dbms_cloud_oci_devops_trigger_action_t`type.

Fields

Field Description

`build_pipeline_id`

(required) The OCID of the build pipeline to be triggered.

### DBMS_CLOUD_OCI_DEVOPS_TRIGGER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_devops_trigger_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_TRIGGER_COLLECTION_T Type

Results of a trigger search. Contains boh trigger summary items and other information such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of triggers.

### DBMS_CLOUD_OCI_DEVOPS_TRIGGER_DEPLOYMENT_PIPELINE_STAGE_RUN_PROGRESS_T Type

Specifies Trigger Deployment Pipleline stage specific run details.

Syntax
```

```

`dbms_cloud_oci_devops_trigger_deployment_pipeline_stage_run_progress_t`is a subtype of the`dbms_cloud_oci_devops_build_pipeline_stage_run_progress_t`type.

Fields

Field Description

`exported_variables`

(optional)

`artifact_override_parameters`

(optional)

`deployment_id`

(optional) Identifier of the deployment triggered.

### DBMS_CLOUD_OCI_DEVOPS_TRIGGER_DEPLOYMENT_STAGE_T Type

Specifies the Trigger Deployment stage, which runs another pipeline of the application.

Syntax
```

```

`dbms_cloud_oci_devops_trigger_deployment_stage_t`is a subtype of the`dbms_cloud_oci_devops_build_pipeline_stage_t`type.

Fields

Field Description

`deploy_pipeline_id`

(required) A target deployment pipeline OCID that will run in this stage.

`is_pass_all_parameters_enabled`

(required) A boolean flag that specifies whether all the parameters must be passed when the deployment is triggered.

### DBMS_CLOUD_OCI_DEVOPS_TRIGGER_DEPLOYMENT_STAGE_SUMMARY_T Type

Specifies the Trigger Deployment stage, which runs another pipeline of the application.

Syntax
```

```

`dbms_cloud_oci_devops_trigger_deployment_stage_summary_t`is a subtype of the`dbms_cloud_oci_devops_build_pipeline_stage_summary_t`type.

Fields

Field Description

`deploy_pipeline_id`

(required) A target deployment pipeline OCID that will run in this stage.

`is_pass_all_parameters_enabled`

(required) A boolean flag that specifies whether all the parameters must be passed when the deployment is triggered.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_WAIT_CRITERIA_DETAILS_T Type

Specifies wait criteria for the Wait stage.

Syntax
```

```

Fields

Field Description

`wait_type`

(required) Wait criteria type.

Allowed values are: 'ABSOLUTE_WAIT'

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_ABSOLUTE_WAIT_CRITERIA_DETAILS_T Type

Specifies the absolute wait criteria. You can specify fixed length of wait duration.

Syntax
```

```

`dbms_cloud_oci_devops_update_absolute_wait_criteria_details_t`is a subtype of the`dbms_cloud_oci_devops_update_wait_criteria_details_t`type.

Fields

Field Description

`wait_duration`

(optional) The absolute wait duration. Minimum wait duration must be 5 seconds. Maximum wait duration can be up to 2 days.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_CONNECTION_DETAILS_T Type

The details for updating a connection.

Syntax
```

```

Fields

Field Description

`description`

(optional) Optional description about the connection.

`display_name`

(optional) Optional connection display name. Avoid entering confidential information.

`connection_type`

(required) The type of connection.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_BITBUCKET_CLOUD_APP_PASSWORD_CONNECTION_DETAILS_T Type

The details for updating a connection of the type `BITBUCKET_CLOUD_APP_PASSWORD`. This type corresponds to a connection in Bitbucket Cloud that is authenticated with username and app password.

Syntax
```

```

`dbms_cloud_oci_devops_update_bitbucket_cloud_app_password_connection_details_t`is a subtype of the`dbms_cloud_oci_devops_update_connection_details_t`type.

Fields

Field Description

`username`

(optional) Public Bitbucket Cloud Username in plain text(not more than 30 characters)

`app_password`

(optional) OCID of personal Bitbucket Cloud AppPassword saved in secret store

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_TRIGGER_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Trigger display name. Avoid entering confidential information.

`description`

(optional) Optional description about the trigger.

`trigger_source`

(required) Source of the trigger. Allowed values are, GITHUB and GITLAB.

`actions`

(optional) The list of actions that are to be performed for this trigger.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_BITBUCKET_CLOUD_TRIGGER_DETAILS_T Type

Update trigger specific to Bitbucket Cloud.

Syntax
```

```

`dbms_cloud_oci_devops_update_bitbucket_cloud_trigger_details_t`is a subtype of the`dbms_cloud_oci_devops_update_trigger_details_t`type.

Fields

Field Description

`connection_id`

(optional) The OCID of the connection resource used to get details for triggered events.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_BITBUCKET_SERVER_ACCESS_TOKEN_CONNECTION_DETAILS_T Type

The details for updating a connection of the type `BITBUCKET_SERVER_ACCESS_TOKEN`. This type corresponds to a connection in Bitbucket that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_devops_update_bitbucket_server_access_token_connection_details_t`is a subtype of the`dbms_cloud_oci_devops_update_connection_details_t`type.

Fields

Field Description

`access_token`

(optional) OCID of personal access token saved in secret store

`base_url`

(optional) The Base URL of the hosted BitbucketServer.

`tls_verify_config`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_BITBUCKET_SERVER_TRIGGER_DETAILS_T Type

Update trigger specific to Bitbucket Server.

Syntax
```

```

`dbms_cloud_oci_devops_update_bitbucket_server_trigger_details_t`is a subtype of the`dbms_cloud_oci_devops_update_trigger_details_t`type.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_BUILD_PIPELINE_DETAILS_T Type

The information to be updated for the given build pipeline.

Syntax
```

```

Fields

Field Description

`description`

(optional) Optional description about the build pipeline.

`display_name`

(optional) Build pipeline display name. Avoid entering confidential information.

`build_pipeline_parameters`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_BUILD_PIPELINE_STAGE_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.

`description`

(optional) Optional description about the build stage.

`build_pipeline_stage_type`

(required) Stage types.

`build_pipeline_stage_predecessor_collection`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_BUILD_RUN_DETAILS_T Type

The build run information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Build run display name. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_BUILD_STAGE_DETAILS_T Type

Specifies the build stage.

Syntax
```

```

`dbms_cloud_oci_devops_update_build_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_update_build_pipeline_stage_details_t`type.

Fields

Field Description

`image`

(optional) Image name for the build environment.

`build_spec_file`

(optional) The path to the build specification file for this environment. The default location of the file if not specified is build_spec.yaml.

`stage_execution_timeout_in_seconds`

(optional) Timeout for the build stage execution. Specify value in seconds.

`build_source_collection`

(optional)

`primary_build_source`

(optional) Name of the build source where the build_spec.yml file is located. If not specified, the first entry in the build source collection is chosen as primary build source.

`build_runner_shape_config`

(optional)

`private_access_config`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_DEPLOY_STAGE_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`description`

(optional) Optional description about the deployment stage.

`display_name`

(optional) Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.

`deploy_stage_type`

(required) Deployment stage type.

`deploy_stage_predecessor_collection`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOY_STAGE_DETAILS_T Type

Specifies the Instance Group Blue-Green deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_update_compute_instance_group_blue_green_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deploy_stage_details_t`type.

Fields

Field Description

`deployment_spec_deploy_artifact_id`

(optional) The OCID of the artifact that contains the deployment specification.

`deploy_artifact_ids`

(optional) The list of file artifact OCIDs to deploy.

`rollout_policy`

(optional)

`failure_policy`

(optional)

`test_load_balancer_config`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT_DEPLOY_STAGE_DETAILS_T Type

Specifies the instance group blue-green deployment load balancer traffic shift stage.

Syntax
```

```

`dbms_cloud_oci_devops_update_compute_instance_group_blue_green_traffic_shift_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deploy_stage_details_t`type.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL_DEPLOY_STAGE_DETAILS_T Type

Specifies the canary approval stage.

Syntax
```

```

`dbms_cloud_oci_devops_update_compute_instance_group_canary_approval_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deploy_stage_details_t`type.

Fields

Field Description

`approval_policy`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_COMPUTE_INSTANCE_GROUP_CANARY_DEPLOY_STAGE_DETAILS_T Type

Specifies the Instance Group Canary deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_update_compute_instance_group_canary_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deploy_stage_details_t`type.

Fields

Field Description

`deployment_spec_deploy_artifact_id`

(optional) The OCID of the artifact that contains the deployment specification.

`deploy_artifact_ids`

(optional) The list of file artifact OCIDs to deploy.

`rollout_policy`

(optional)

`test_load_balancer_config`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT_DEPLOY_STAGE_DETAILS_T Type

Specifies load balancer traffic shift stage.

Syntax
```

```

`dbms_cloud_oci_devops_update_compute_instance_group_canary_traffic_shift_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deploy_stage_details_t`type.

Fields

Field Description

`rollout_policy`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_DEPLOY_ENVIRONMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`description`

(optional) Optional description about the deployment environment.

`display_name`

(optional) Deployment environment display name. Avoid entering confidential information.

`deploy_environment_type`

(required) Deployment environment type.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_COMPUTE_INSTANCE_GROUP_DEPLOY_ENVIRONMENT_DETAILS_T Type

Specifies the Compute instance group environment.

Syntax
```

```

`dbms_cloud_oci_devops_update_compute_instance_group_deploy_environment_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deploy_environment_details_t`type.

Fields

Field Description

`compute_instance_group_selectors`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_COMPUTE_INSTANCE_GROUP_DEPLOY_STAGE_DETAILS_T Type

Specifies the Instance Group Rolling deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_update_compute_instance_group_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deploy_stage_details_t`type.

Fields

Field Description

`compute_instance_group_deploy_environment_id`

(optional) A compute instance group environment OCID for rolling deployment.

`deployment_spec_deploy_artifact_id`

(optional) The OCID of the artifact that contains the deployment specification.

`deploy_artifact_ids`

(optional) Additional file artifact OCIDs.

`rollout_policy`

(optional)

`rollback_policy`

(optional)

`failure_policy`

(optional)

`load_balancer_config`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_DELIVER_ARTIFACT_STAGE_DETAILS_T Type

Specifies the Deliver Artifacts stage.

Syntax
```

```

`dbms_cloud_oci_devops_update_deliver_artifact_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_update_build_pipeline_stage_details_t`type.

Fields

Field Description

`deliver_artifact_collection`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_DEPLOY_ARTIFACT_DETAILS_T Type

The information to be updated for the artifact.

Syntax
```

```

Fields

Field Description

`description`

(optional) Optional description about the deployment artifact.

`display_name`

(optional) Deployment artifact display name. Avoid entering confidential information.

`deploy_artifact_type`

(optional) Type of the deployment artifact.

`deploy_artifact_source`

(optional)

`argument_substitution_mode`

(optional) Mode for artifact parameter substitution.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_DEPLOYMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`deployment_type`

(required) Specifies type for this deployment.

`display_name`

(optional) Deployment display name. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_DEPLOY_PIPELINE_DEPLOYMENT_DETAILS_T Type

Update details for a pipeline deployment.

Syntax
```

```

`dbms_cloud_oci_devops_update_deploy_pipeline_deployment_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deployment_details_t`type.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_DEPLOY_PIPELINE_DETAILS_T Type

The information to be updated for the given deloyment pipeline.

Syntax
```

```

Fields

Field Description

`description`

(optional) Optional description about the deloyment pipeline.

`display_name`

(optional) Deloyment pipeline display name. Avoid entering confidential information.

`deploy_pipeline_parameters`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_DEPLOY_PIPELINE_REDEPLOYMENT_DETAILS_T Type

Update details for a pipeline redeployment.

Syntax
```

```

`dbms_cloud_oci_devops_update_deploy_pipeline_redeployment_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deployment_details_t`type.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_DEVOPS_CODE_REPOSITORY_TRIGGER_DETAILS_T Type

Update trigger specific to OCI DevOps code repository.

Syntax
```

```

`dbms_cloud_oci_devops_update_devops_code_repository_trigger_details_t`is a subtype of the`dbms_cloud_oci_devops_update_trigger_details_t`type.

Fields

Field Description

`repository_id`

(optional) The OCID of the DevOps code repository.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_FUNCTION_DEPLOY_ENVIRONMENT_DETAILS_T Type

Specifies the Function environment.

Syntax
```

```

`dbms_cloud_oci_devops_update_function_deploy_environment_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deploy_environment_details_t`type.

Fields

Field Description

`function_id`

(optional) The OCID of the Function.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_FUNCTION_DEPLOY_STAGE_DETAILS_T Type

Specifies the Function stage.

Syntax
```

```

`dbms_cloud_oci_devops_update_function_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deploy_stage_details_t`type.

Fields

Field Description

`function_deploy_environment_id`

(optional) Function environment OCID.

`docker_image_deploy_artifact_id`

(optional) A Docker image artifact OCID.

`config`

(optional) User provided key and value pair configuration, which is assigned through constants or parameter.

`max_memory_in_m_bs`

(optional) Maximum usable memory for the Function (in MB).

`function_timeout_in_seconds`

(optional) Timeout for execution of the Function. Value in seconds.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_GITHUB_ACCESS_TOKEN_CONNECTION_DETAILS_T Type

The details for updating a connection of the type `GITHUB_ACCESS_TOKEN`. This type corresponds to a connection in GitHub that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_devops_update_github_access_token_connection_details_t`is a subtype of the`dbms_cloud_oci_devops_update_connection_details_t`type.

Fields

Field Description

`access_token`

(optional) OCID of personal access token saved in secret store

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_GITHUB_TRIGGER_DETAILS_T Type

Update trigger specific to GitHub.

Syntax
```

```

`dbms_cloud_oci_devops_update_github_trigger_details_t`is a subtype of the`dbms_cloud_oci_devops_update_trigger_details_t`type.

Fields

Field Description

`connection_id`

(optional) The OCID of the connection resource used to get details for triggered events.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_GITLAB_ACCESS_TOKEN_CONNECTION_DETAILS_T Type

The details for updating a connection of the type `GITLAB_ACCESS_TOKEN`. This type corresponds to a connection in GitLab that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_devops_update_gitlab_access_token_connection_details_t`is a subtype of the`dbms_cloud_oci_devops_update_connection_details_t`type.

Fields

Field Description

`access_token`

(optional) The OCID of personal access token saved in secret store.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_GITLAB_SERVER_ACCESS_TOKEN_CONNECTION_DETAILS_T Type

The details for updating a connection of the type `GITLAB_SERVER_ACCESS_TOKEN`. This type corresponds to a connection in GitLab self-hosted server that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_devops_update_gitlab_server_access_token_connection_details_t`is a subtype of the`dbms_cloud_oci_devops_update_connection_details_t`type.

Fields

Field Description

`access_token`

(optional) The OCID of personal access token saved in secret store.

`base_url`

(optional) The baseUrl of the hosted GitLabServer.

`tls_verify_config`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_GITLAB_SERVER_TRIGGER_DETAILS_T Type

Update trigger specific to GitLab self-hosted server.

Syntax
```

```

`dbms_cloud_oci_devops_update_gitlab_server_trigger_details_t`is a subtype of the`dbms_cloud_oci_devops_update_trigger_details_t`type.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_GITLAB_TRIGGER_DETAILS_T Type

Update trigger specific to GitLab.

Syntax
```

```

`dbms_cloud_oci_devops_update_gitlab_trigger_details_t`is a subtype of the`dbms_cloud_oci_devops_update_trigger_details_t`type.

Fields

Field Description

`connection_id`

(optional) The OCID of the connection resource used to get details for triggered events.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_INVOKE_FUNCTION_DEPLOY_STAGE_DETAILS_T Type

Specifies Invoke Function stage.

Syntax
```

```

`dbms_cloud_oci_devops_update_invoke_function_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deploy_stage_details_t`type.

Fields

Field Description

`function_deploy_environment_id`

(optional) Function environment OCID.

`deploy_artifact_id`

(optional) Optional artifact OCID. The artifact will be included in the body for the function invocation during the stage's execution. If the DeployArtifact.argumentSubstituitionMode is set to SUBSTITUTE_PLACEHOLDERS, then the pipeline parameter values will be used to replace the placeholders in the artifact content.

`is_async`

(optional) A boolean flag specifies whether this stage executes asynchronously.

`is_validation_enabled`

(optional) A boolean flag specifies whether the invoked function must be validated.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_LOAD_BALANCER_TRAFFIC_SHIFT_DEPLOY_STAGE_DETAILS_T Type

Specifies load balancer traffic shift stage.

Syntax
```

```

`dbms_cloud_oci_devops_update_load_balancer_traffic_shift_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deploy_stage_details_t`type.

Fields

Field Description

`blue_backend_ips`

(optional)

`green_backend_ips`

(optional)

`traffic_shift_target`

(optional) Specifies the target or destination backend set. Example: BLUE - Traffic from the existing backends of managed Load Balance Listener to blue Backend IPs, as per rolloutPolicy. GREEN - Traffic from the existing backends of managed Load Balance Listener to blue Backend IPs ser as per rolloutPolicy.

`rollout_policy`

(optional)

`load_balancer_config`

(optional)

`rollback_policy`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_MANUAL_APPROVAL_DEPLOY_STAGE_DETAILS_T Type

Specifies the manual approval stage.

Syntax
```

```

`dbms_cloud_oci_devops_update_manual_approval_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deploy_stage_details_t`type.

Fields

Field Description

`approval_policy`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_OKE_BLUE_GREEN_DEPLOY_STAGE_DETAILS_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster Blue-Green deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_update_oke_blue_green_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deploy_stage_details_t`type.

Fields

Field Description

`kubernetes_manifest_deploy_artifact_ids`

(optional) List of Kubernetes manifest artifact OCIDs, the manifests should not include any job resource.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_OKE_BLUE_GREEN_TRAFFIC_SHIFT_DEPLOY_STAGE_DETAILS_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster blue-green deployment traffic shift stage.

Syntax
```

```

`dbms_cloud_oci_devops_update_oke_blue_green_traffic_shift_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deploy_stage_details_t`type.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_OKE_CANARY_APPROVAL_DEPLOY_STAGE_DETAILS_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster canary deployment approval stage.

Syntax
```

```

`dbms_cloud_oci_devops_update_oke_canary_approval_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deploy_stage_details_t`type.

Fields

Field Description

`approval_policy`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_OKE_CANARY_DEPLOY_STAGE_DETAILS_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster Canary deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_update_oke_canary_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deploy_stage_details_t`type.

Fields

Field Description

`kubernetes_manifest_deploy_artifact_ids`

(optional) List of Kubernetes manifest artifact OCIDs.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_OKE_CANARY_TRAFFIC_SHIFT_DEPLOY_STAGE_DETAILS_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster canary deployment traffic shift stage.

Syntax
```

```

`dbms_cloud_oci_devops_update_oke_canary_traffic_shift_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deploy_stage_details_t`type.

Fields

Field Description

`rollout_policy`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_OKE_CLUSTER_DEPLOY_ENVIRONMENT_DETAILS_T Type

Specifies the Kubernetes cluster environment.

Syntax
```

```

`dbms_cloud_oci_devops_update_oke_cluster_deploy_environment_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deploy_environment_details_t`type.

Fields

Field Description

`cluster_id`

(optional) The OCID of the Kubernetes cluster.

`network_channel`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_OKE_DEPLOY_STAGE_DETAILS_T Type

Specifies the Container Engine for Kubernetes (OKE) cluster deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_update_oke_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deploy_stage_details_t`type.

Fields

Field Description

`oke_cluster_deploy_environment_id`

(optional) Kubernetes cluster environment OCID for deployment.

`kubernetes_manifest_deploy_artifact_ids`

(optional) List of Kubernetes manifest artifact OCIDs.

`namespace`

(optional) Default namespace to be used for Kubernetes deployment when not specified in the manifest.

`rollback_policy`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_OKE_HELM_CHART_DEPLOY_STAGE_DETAILS_T Type

Specifies the Kubernetes cluster deployment stage.

Syntax
```

```

`dbms_cloud_oci_devops_update_oke_helm_chart_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deploy_stage_details_t`type.

Fields

Field Description

`oke_cluster_deploy_environment_id`

(optional) Kubernetes cluster environment OCID for deployment.

`helm_chart_deploy_artifact_id`

(optional) Helm chart artifact OCID.

`values_artifact_ids`

(optional) List of values.yaml file artifact OCIDs.

`release_name`

(optional) Name of the Helm chart release.

`namespace`

(optional) Default namespace to be used for Kubernetes deployment when not specified in the manifest.

`timeout_in_seconds`

(optional) Time to wait for execution of a helm stage. Defaults to 300 seconds.

`rollback_policy`

(optional)

`set_values`

(optional)

`set_string`

(optional)

`are_hooks_enabled`

(optional) Disable pre/post upgrade hooks.

`should_reuse_values`

(optional) During upgrade, reuse the values of the last release and merge overrides from the command line. Set to false by default.

`should_reset_values`

(optional) During upgrade, reset the values to the ones built into the chart. It overrides shouldReuseValues. Set to false by default.

`is_force_enabled`

(optional) Force resource update through delete; or if required, recreate. Set to false by default.

`should_cleanup_on_fail`

(optional) Allow deletion of new resources created during when an upgrade fails. Set to false by default.

`max_history`

(optional) Limit the maximum number of revisions saved per release. Use 0 for no limit. Set to 10 by default

`should_skip_crds`

(optional) If set, no CRDs are installed. By default, CRDs are installed only if they are not present already. Set to false by default.

`should_skip_render_subchart_notes`

(optional) If set, renders subchart notes along with the parent. Set to false by default.

`should_not_wait`

(optional) Waits until all the resources are in a ready state to mark the release as successful. Set to false by default.

`is_debug_enabled`

(optional) Enables helm --debug option to stream output to tf stdout. Set to false by default.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_PROJECT_DETAILS_T Type

The information to be updated for the given project.

Syntax
```

```

Fields

Field Description

`description`

(optional) Project description.

`notification_config`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_REPOSITORY_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`name`

(optional) Unique name of a repository.

`description`

(optional) Details of the repository. Avoid entering confidential information.

`default_branch`

(optional) The default branch of the repository.

`repository_type`

(optional) Type of repository. Allowed values: `MIRRORED` `HOSTED`

`mirror_repository_config`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_SHELL_DEPLOY_STAGE_DETAILS_T Type

Specifies the shell stage.

Syntax
```

```

`dbms_cloud_oci_devops_update_shell_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deploy_stage_details_t`type.

Fields

Field Description

`container_config`

(optional)

`command_spec_deploy_artifact_id`

(optional) The OCID of the artifact that contains the command specification.

`timeout_in_seconds`

(optional) Time to wait for execution of a shell stage. Defaults to 36000 seconds.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_SINGLE_DEPLOY_STAGE_DEPLOYMENT_DETAILS_T Type

Update details for a single stage deployment.

Syntax
```

```

`dbms_cloud_oci_devops_update_single_deploy_stage_deployment_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deployment_details_t`type.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_SINGLE_DEPLOY_STAGE_REDEPLOYMENT_DETAILS_T Type

Update details for a single stage redeployment.

Syntax
```

```

`dbms_cloud_oci_devops_update_single_deploy_stage_redeployment_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deployment_details_t`type.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_TRIGGER_DEPLOYMENT_STAGE_DETAILS_T Type

Specifies the Trigger Deployment stage, which runs another pipeline of the application.

Syntax
```

```

`dbms_cloud_oci_devops_update_trigger_deployment_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_update_build_pipeline_stage_details_t`type.

Fields

Field Description

`deploy_pipeline_id`

(optional) A target deployment pipeline OCID that will run in this stage.

`is_pass_all_parameters_enabled`

(optional) A boolean flag that specifies whether all the parameters must be passed when the deployment is triggered.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_VBS_ACCESS_TOKEN_CONNECTION_DETAILS_T Type

The details for updating a connection of the type `VBS_ACCESS_TOKEN`. This type corresponds to a connection in Visual Builder Studio that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_devops_update_vbs_access_token_connection_details_t`is a subtype of the`dbms_cloud_oci_devops_update_connection_details_t`type.

Fields

Field Description

`access_token`

(optional) OCID of personal access token saved in secret store

`base_url`

(optional) The Base URL of the hosted VBS server.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_VBS_TRIGGER_DETAILS_T Type

Update trigger specific to VBS.

Syntax
```

```

`dbms_cloud_oci_devops_update_vbs_trigger_details_t`is a subtype of the`dbms_cloud_oci_devops_update_trigger_details_t`type.

Fields

Field Description

`connection_id`

(optional) The OCID of the connection resource used to get details for triggered events.

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_WAIT_DEPLOY_STAGE_DETAILS_T Type

Specifies the Wait stage. User can specify a criteria for wait time or give an absolute duration.

Syntax
```

```

`dbms_cloud_oci_devops_update_wait_deploy_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_update_deploy_stage_details_t`type.

Fields

Field Description

`wait_criteria`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_UPDATE_WAIT_STAGE_DETAILS_T Type

Specifies the Wait stage. You can specify variable wait times or an absolute duration.

Syntax
```

```

`dbms_cloud_oci_devops_update_wait_stage_details_t`is a subtype of the`dbms_cloud_oci_devops_update_build_pipeline_stage_details_t`type.

Fields

Field Description

`wait_criteria`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_VAULT_SECRET_VERIFICATION_KEY_SOURCE_T Type

Specifies the Vault verification source details

Syntax
```

```

`dbms_cloud_oci_devops_vault_secret_verification_key_source_t`is a subtype of the`dbms_cloud_oci_devops_verification_key_source_t`type.

Fields

Field Description

`vault_secret_id`

(required) The OCID of the Vault Secret containing the verification key versions.

### DBMS_CLOUD_OCI_DEVOPS_VBS_ACCESS_TOKEN_CONNECTION_T Type

The properties that define a connection of the type `VBS_ACCESS_TOKEN`. This type corresponds to a connection in Visual Builder Studio that is authenticated with a Personal Access Token.

Syntax
```

```

`dbms_cloud_oci_devops_vbs_access_token_connection_t`is a subtype of the`dbms_cloud_oci_devops_connection_t`type.

Fields

Field Description

`access_token`

(required) The OCID of personal access token saved in secret store.

`base_url`

(required) The Base URL of the hosted Visual Builder Studio server.

### DBMS_CLOUD_OCI_DEVOPS_VBS_ACCESS_TOKEN_CONNECTION_SUMMARY_T Type

Summary information for a connection of the type `VBS_ACCESS_TOKEN`. This type corresponds to a connection in Visual Builder Studio that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_devops_vbs_access_token_connection_summary_t`is a subtype of the`dbms_cloud_oci_devops_connection_summary_t`type.

Fields

Field Description

`access_token`

(required) The OCID of personal access token saved in secret store.

`base_url`

(required) The Base URL of the hosted VBS server.

### DBMS_CLOUD_OCI_DEVOPS_VBS_BUILD_RUN_SOURCE_T Type

Specifies details of build run through VBS Server.

Syntax
```

```

`dbms_cloud_oci_devops_vbs_build_run_source_t`is a subtype of the`dbms_cloud_oci_devops_build_run_source_t`type.

Fields

Field Description

`trigger_id`

(required) The trigger that invoked the build run.

`trigger_info`

(required)

### DBMS_CLOUD_OCI_DEVOPS_VBS_BUILD_SOURCE_T Type

VBS Server Build Source for Build Stage

Syntax
```

```

`dbms_cloud_oci_devops_vbs_build_source_t`is a subtype of the`dbms_cloud_oci_devops_build_source_t`type.

Fields

Field Description

`connection_id`

(required) Connection identifier pertinent to VBS Server source provider

### DBMS_CLOUD_OCI_DEVOPS_VBS_FILTER_ATTRIBUTES_T Type

Attributes to filter VBS events.

Syntax
```

```

Fields

Field Description

`head_ref`

(optional) Branch for push event; source branch for pull requests.

`base_ref`

(optional) The target branch for pull requests; not applicable for push requests.

`repository_name`

(optional) The repository name for trigger events.

`file_filter`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_VBS_FILTER_EXCLUSION_ATTRIBUTES_T Type

Attributes to filter VBS events. File filter criteria - Changes only affecting excluded files will not invoke a build. if both include and exclude filter are used then exclusion filter will be applied on the result set of inclusion filter.

Syntax
```

```

Fields

Field Description

`file_filter`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_VBS_FILTER_T Type

The filter for VBS events.

Syntax
```

```

`dbms_cloud_oci_devops_vbs_filter_t`is a subtype of the`dbms_cloud_oci_devops_filter_t`type.

Fields

Field Description

`events`

(optional) The events, for example, PUSH, PULL_REQUEST_MERGE.

Allowed values are: 'PUSH', 'MERGE_REQUEST_CREATED', 'MERGE_REQUEST_UPDATED', 'MERGE_REQUEST_MERGED'

`include`

(optional)

`exclude`

(optional)

### DBMS_CLOUD_OCI_DEVOPS_VBS_TRIGGER_T Type

Trigger specific to VBS

Syntax
```

```

`dbms_cloud_oci_devops_vbs_trigger_t`is a subtype of the`dbms_cloud_oci_devops_trigger_t`type.

Fields

Field Description

`trigger_url`

(required) The endpoint that listens to trigger events.

`connection_id`

(optional) The OCID of the connection resource used to get details for triggered events.

### DBMS_CLOUD_OCI_DEVOPS_VBS_TRIGGER_CREATE_RESULT_T Type

Trigger create response specific to VBS.

Syntax
```

```

`dbms_cloud_oci_devops_vbs_trigger_create_result_t`is a subtype of the`dbms_cloud_oci_devops_trigger_create_result_t`type.

Fields

Field Description

`secret`

(required) The secret used to validate the incoming trigger call. This is visible only after the resource is created.

`trigger_url`

(required) The endpoint that listens to trigger events.

`connection_id`

(optional) The OCID of the connection resource used to get details for triggered events.

### DBMS_CLOUD_OCI_DEVOPS_VBS_TRIGGER_SUMMARY_T Type

Summary of the VBS trigger.

Syntax
```

```

`dbms_cloud_oci_devops_vbs_trigger_summary_t`is a subtype of the`dbms_cloud_oci_devops_trigger_summary_t`type.

Fields

Field Description

`connection_id`

(optional) The OCID of the connection resource used to get details for triggered events.

### DBMS_CLOUD_OCI_DEVOPS_WAIT_DEPLOY_STAGE_T Type

Specifies the Wait stage. User can specify a criteria for wait time or give an absolute duration.

Syntax
```

```

`dbms_cloud_oci_devops_wait_deploy_stage_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_t`type.

Fields

Field Description

`wait_criteria`

(required)

### DBMS_CLOUD_OCI_DEVOPS_WAIT_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type

Specifies Wait stage specific execution details.

Syntax
```

```

`dbms_cloud_oci_devops_wait_deploy_stage_execution_progress_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_execution_progress_t`type.

### DBMS_CLOUD_OCI_DEVOPS_WAIT_DEPLOY_STAGE_SUMMARY_T Type

Specifies the Wait stage. User can specify a criteria for wait time or give an absolute duration.

Syntax
```

```

`dbms_cloud_oci_devops_wait_deploy_stage_summary_t`is a subtype of the`dbms_cloud_oci_devops_deploy_stage_summary_t`type.

Fields

Field Description

`wait_criteria`

(required)

### DBMS_CLOUD_OCI_DEVOPS_WAIT_STAGE_T Type

Specifies the Wait stage. You can specify variable wait times or an absolute duration.

Syntax
```

```

`dbms_cloud_oci_devops_wait_stage_t`is a subtype of the`dbms_cloud_oci_devops_build_pipeline_stage_t`type.

Fields

Field Description

`wait_criteria`

(required)

### DBMS_CLOUD_OCI_DEVOPS_WAIT_STAGE_RUN_PROGRESS_T Type

Specifies Wait stage specific run details.

Syntax
```

```

`dbms_cloud_oci_devops_wait_stage_run_progress_t`is a subtype of the`dbms_cloud_oci_devops_build_pipeline_stage_run_progress_t`type.

### DBMS_CLOUD_OCI_DEVOPS_WAIT_STAGE_SUMMARY_T Type

Specifies the Wait stage. You can specify variable wait times or an absolute duration.

Syntax
```

```

`dbms_cloud_oci_devops_wait_stage_summary_t`is a subtype of the`dbms_cloud_oci_devops_build_pipeline_stage_summary_t`type.

Fields

Field Description

`wait_criteria`

(required)

### DBMS_CLOUD_OCI_DEVOPS_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way how the work is tracked in the work request affects this resource. A resource that is created, updated, or deleted remains in the IN PROGRESS state until the work is complete for that resource. Thereafter it transitions to CREATED, UPDATED, or DELETED state.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED', 'FAILED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that the user can use to access the resource metadata.

### DBMS_CLOUD_OCI_DEVOPS_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_devops_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_WORK_REQUEST_T Type

Details of the work request status.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'CREATE_PROJECT', 'UPDATE_PROJECT', 'DELETE_PROJECT', 'MOVE_PROJECT', 'CREATE_DEPLOY_PIPELINE', 'UPDATE_DEPLOY_PIPELINE', 'DELETE_DEPLOY_PIPELINE', 'CREATE_DEPLOY_STAGE', 'UPDATE_DEPLOY_STAGE', 'DELETE_DEPLOY_STAGE', 'CREATE_DEPLOY_ARTIFACT', 'UPDATE_DEPLOY_ARTIFACT', 'DELETE_DEPLOY_ARTIFACT', 'CREATE_DEPLOY_ENVIRONMENT', 'UPDATE_DEPLOY_ENVIRONMENT', 'DELETE_DEPLOY_ENVIRONMENT', 'CREATE_DEPLOYMENT', 'UPDATE_DEPLOYMENT', 'DELETE_DEPLOYMENT', 'CREATE_BUILD_PIPELINE', 'UPDATE_BUILD_PIPELINE', 'DELETE_BUILD_PIPELINE', 'CREATE_BUILD_PIPELINE_STAGE', 'UPDATE_BUILD_PIPELINE_STAGE', 'DELETE_BUILD_PIPELINE_STAGE', 'CREATE_CONNECTION', 'UPDATE_CONNECTION', 'DELETE_CONNECTION', 'CREATE_TRIGGER', 'UPDATE_TRIGGER', 'DELETE_TRIGGER', 'EXECUTE_TRIGGER', 'CREATE_REPOSITORY', 'UPDATE_REPOSITORY', 'DELETE_REPOSITORY', 'MIRROR_REPOSITORY', 'SCHEDULE_CASCADING_PROJECT_DELETION', 'CANCEL_SCHEDULED_CASCADING_PROJECT_DELETION'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'WAITING', 'NEEDS_ATTENTION'

`id`

(required) The OCID of the work request.

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) Date and time the request was created, Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_started`

(optional) Date and time the request was started. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_finished`

(optional) Date and time the request was completed. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

### DBMS_CLOUD_OCI_DEVOPS_WORK_REQUEST_SUMMARY_T Type

Details of the work request status.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'CREATE_PROJECT', 'UPDATE_PROJECT', 'DELETE_PROJECT', 'MOVE_PROJECT', 'CREATE_DEPLOY_PIPELINE', 'UPDATE_DEPLOY_PIPELINE', 'DELETE_DEPLOY_PIPELINE', 'CREATE_DEPLOY_STAGE', 'UPDATE_DEPLOY_STAGE', 'DELETE_DEPLOY_STAGE', 'CREATE_DEPLOY_ARTIFACT', 'UPDATE_DEPLOY_ARTIFACT', 'DELETE_DEPLOY_ARTIFACT', 'CREATE_DEPLOY_ENVIRONMENT', 'UPDATE_DEPLOY_ENVIRONMENT', 'DELETE_DEPLOY_ENVIRONMENT', 'CREATE_DEPLOYMENT', 'UPDATE_DEPLOYMENT', 'DELETE_DEPLOYMENT', 'CREATE_BUILD_PIPELINE', 'UPDATE_BUILD_PIPELINE', 'DELETE_BUILD_PIPELINE', 'CREATE_BUILD_PIPELINE_STAGE', 'UPDATE_BUILD_PIPELINE_STAGE', 'DELETE_BUILD_PIPELINE_STAGE', 'CREATE_CONNECTION', 'UPDATE_CONNECTION', 'DELETE_CONNECTION', 'CREATE_TRIGGER', 'UPDATE_TRIGGER', 'DELETE_TRIGGER', 'EXECUTE_TRIGGER', 'CREATE_REPOSITORY', 'UPDATE_REPOSITORY', 'DELETE_REPOSITORY', 'MIRROR_REPOSITORY', 'SCHEDULE_CASCADING_PROJECT_DELETION', 'CANCEL_SCHEDULED_CASCADING_PROJECT_DELETION'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'WAITING', 'NEEDS_ATTENTION'

`id`

(required) The OCID of the work request.

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests must be scoped to the same compartment as the resource that the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, the service team must pick the primary resource whose compartment must be used.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) Date and time the request was created. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_started`

(optional) Date and time the request was started. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

`time_finished`

(optional) Date and time the request was completed. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

### DBMS_CLOUD_OCI_DEVOPS_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_devops_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_WORK_REQUEST_COLLECTION_T Type

List of work requests.

Syntax
```

```

Fields

Field Description

`items`

(required) Work request items found for the search.

### DBMS_CLOUD_OCI_DEVOPS_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed in[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) Time the error occured. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

### DBMS_CLOUD_OCI_DEVOPS_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_devops_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_WORK_REQUEST_ERROR_COLLECTION_T Type

List of work request errors encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`items`

(required) Work request error items.

### DBMS_CLOUD_OCI_DEVOPS_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) Time the log message was written. Format defined by[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339).

### DBMS_CLOUD_OCI_DEVOPS_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_devops_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DEVOPS_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

List of log messages from the execution of a work request.

Syntax
```

```

Fields

Field Description

`items`

(required) Work request log entry items.

- [DevOps Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-74E9B3FC-5A2D-4BAD-B023-F888B68D5D87)
- [DBMS_CLOUD_OCI_DEVOPS_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-4CF1DBFA-91AD-4BAF-B975-ECA142CF0CD9)
- [DBMS_CLOUD_OCI_DEVOPS_WAIT_CRITERIA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-74EDEC23-3D2E-4868-809B-78306DC9B63F)
- [DBMS_CLOUD_OCI_DEVOPS_ABSOLUTE_WAIT_CRITERIA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-BAC95D80-907F-4549-9B1D-5BC26EA9C4D5)
- [DBMS_CLOUD_OCI_DEVOPS_WAIT_CRITERIA_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E60E7854-4CF6-4C5B-9BC0-915C7CB43788)
- [DBMS_CLOUD_OCI_DEVOPS_ABSOLUTE_WAIT_CRITERIA_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-8AF6C9CF-6436-4D1C-82A6-EF2A91ED9DBD)
- [DBMS_CLOUD_OCI_DEVOPS_ACTUAL_BUILD_RUNNER_SHAPE_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-500A33DE-3D44-4357-93DA-1E03033E47CB)
- [DBMS_CLOUD_OCI_DEVOPS_APPROVAL_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-3881CC70-960E-40E0-8C61-60938424F6C3)
- [DBMS_CLOUD_OCI_DEVOPS_APPROVAL_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-01711FC3-9451-4547-9ADF-628BCACA81AF)
- [DBMS_CLOUD_OCI_DEVOPS_APPROVE_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-0AA38E8D-DEE1-434A-96F7-C0C66BFAE6F9)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_ROLLBACK_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-AFB8733A-6AB9-4CC7-ABE3-04BA813B736A)
- [DBMS_CLOUD_OCI_DEVOPS_AUTOMATED_DEPLOY_STAGE_ROLLBACK_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-945067BA-E05C-4204-8B38-925DB6E9EB13)
- [DBMS_CLOUD_OCI_DEVOPS_BACKEND_SET_IP_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-30916918-CCC3-4792-988C-8C91D425B94B)
- [DBMS_CLOUD_OCI_DEVOPS_CONNECTION_VALIDATION_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-A10531B0-FC3E-4CA4-B207-F8662CBFEF50)
- [DBMS_CLOUD_OCI_DEVOPS_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-6B16D77B-3062-4774-BFDB-6D22639835E0)
- [DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_CLOUD_APP_PASSWORD_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-633DDE76-222C-41ED-A043-E3C196930C45)
- [DBMS_CLOUD_OCI_DEVOPS_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-A93C4297-3E01-43A3-9E96-E6224DA50956)
- [DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_CLOUD_APP_PASSWORD_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-D893B557-130C-4356-B64A-494AF90DF9BF)
- [DBMS_CLOUD_OCI_DEVOPS_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-FAA42B84-24EA-4F76-9E9D-F0BDCA012F73)
- [DBMS_CLOUD_OCI_DEVOPS_TRIGGER_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-9920EAFC-A932-4FC6-871E-17DE3FC3A19B)
- [DBMS_CLOUD_OCI_DEVOPS_TRIGGER_ACTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-7F00A512-8F39-470D-B95D-44BDB0123AF9)
- [DBMS_CLOUD_OCI_DEVOPS_TRIGGER_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-CD09E07D-1C9B-49E5-8E30-37AA555107A6)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_RUN_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-81D65106-5C23-4375-B44C-E8DC32B57D41)
- [DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_CLOUD_BUILD_RUN_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-515BC61D-FD94-4A5A-8A16-5DF2AAA6435A)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-F315E13F-CA62-41BA-A0C0-C560B73CCBDE)
- [DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_CLOUD_BUILD_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-D24FE13F-263C-4EE7-9420-451798538508)
- [DBMS_CLOUD_OCI_DEVOPS_FILE_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E9F8910C-AF2D-4803-8015-484024315502)
- [DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_CLOUD_FILTER_ATTRIBUTES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-42710426-2EAD-476C-AF17-5BCD14F6E2F2)
- [DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_CLOUD_FILTER_EXCLUSION_ATTRIBUTES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-058CF6E0-E33F-467F-96C6-DE32BE18C4FC)
- [DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_CLOUD_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-229D199B-560B-401B-A26E-4180E5ED80AD)
- [DBMS_CLOUD_OCI_DEVOPS_TRIGGER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-1936EFC6-434A-4970-98E0-AC7C94642675)
- [DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_CLOUD_TRIGGER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-8726405F-3F45-4614-BA4F-8D8248BD949F)
- [DBMS_CLOUD_OCI_DEVOPS_TRIGGER_CREATE_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-8EBEC631-E937-40E2-9F02-582C6ED58CC5)
- [DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_CLOUD_TRIGGER_CREATE_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-40F5ECA7-28EB-4B11-A612-2460A3BCA812)
- [DBMS_CLOUD_OCI_DEVOPS_TRIGGER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E2B20E07-8C80-4280-89F3-35D40A7FD331)
- [DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_CLOUD_TRIGGER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-04B30EF5-07D8-46A2-B92E-14544019C5E8)
- [DBMS_CLOUD_OCI_DEVOPS_TLS_VERIFY_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-99E65404-DA3F-48EB-ACAB-6BBC26DCEE8E)
- [DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_SERVER_ACCESS_TOKEN_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-C6456193-F51A-4823-958F-12B3291560A5)
- [DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_SERVER_BUILD_RUN_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-DAA1AF95-6A20-4400-8439-891363BA380A)
- [DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_SERVER_BUILD_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-2D3607CA-7E19-4AA0-8EDB-F35E68E1F432)
- [DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_SERVER_FILTER_ATTRIBUTES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-FA0F9EE9-6552-4E43-8F9D-BD58750F34C5)
- [DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_SERVER_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-AA2D9FD2-AD9B-4A08-96CE-5EB0B4AC24AE)
- [DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_SERVER_TOKEN_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-5E6948DD-FAB3-4C0B-B77D-BDA064873B3F)
- [DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_SERVER_TRIGGER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-0EA82C18-5794-4D7E-AF13-517F8AF2841C)
- [DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_SERVER_TRIGGER_CREATE_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-8290F084-336D-4120-8867-B016BBD3ACD6)
- [DBMS_CLOUD_OCI_DEVOPS_BITBUCKET_SERVER_TRIGGER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-16F31275-4787-4DE9-A38A-732791CE88E3)
- [DBMS_CLOUD_OCI_DEVOPS_EXPORTED_VARIABLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-80EF1BFD-DB4B-4C5D-A243-30571E9969A9)
- [DBMS_CLOUD_OCI_DEVOPS_EXPORTED_VARIABLE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-9C65EE18-8814-46A6-9160-8B47AF768B94)
- [DBMS_CLOUD_OCI_DEVOPS_EXPORTED_VARIABLE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-D2CC5C13-4795-4140-8C32-4BAB947E4618)
- [DBMS_CLOUD_OCI_DEVOPS_DELIVERED_ARTIFACT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-00A80D5F-9F44-490B-A719-2954715A5C34)
- [DBMS_CLOUD_OCI_DEVOPS_DELIVERED_ARTIFACT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E83FEFAA-144F-422D-90DF-59621BB61178)
- [DBMS_CLOUD_OCI_DEVOPS_DELIVERED_ARTIFACT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-6BC2A9BD-485A-44E1-9CC5-4CFB20F21210)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_ARTIFACT_OVERRIDE_ARGUMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-432C73F4-DC85-4D40-996C-A18656664EAC)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_ARTIFACT_OVERRIDE_ARGUMENT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-9611A683-C107-4947-ACB2-0E64743BDB58)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_ARTIFACT_OVERRIDE_ARGUMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-85DB9B3E-6B70-4E21-8C19-2B1C706669D3)
- [DBMS_CLOUD_OCI_DEVOPS_VULNERABILITY_AUDIT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-EF1F4C07-8303-4FEA-B70B-2E5DBC3447EE)
- [DBMS_CLOUD_OCI_DEVOPS_VULNERABILITY_AUDIT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-8771E8EF-A33B-490C-8F2F-5FB2734CC172)
- [DBMS_CLOUD_OCI_DEVOPS_VULNERABILITY_AUDIT_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-BC0D269E-FAA5-4388-A1E7-B4122BC20AAE)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_OUTPUTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-9F788088-5E8F-4AB1-B35C-DCC391F30815)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_PARAMETER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-8C8FD74E-D1D1-4543-BCD6-0EDC9D7154D1)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_PARAMETER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-C33CDCBE-BB2E-4514-993B-31544CCF34DD)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_PARAMETER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E8AB4DF2-D487-415B-BD1B-5D329B1B3C4C)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-BCAC3F06-76B3-4724-A258-7CCA137FE36B)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-AD46072D-4193-41D5-9C91-19517D2E3D51)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-421BBA73-AEAF-4253-9383-BCCE38EF0E5E)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-5477EE26-6DFD-4CE3-A94A-EBDE564099F9)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_STAGE_PREDECESSOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-67B03C0F-55A8-46CD-9993-022ECEBB0C5B)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_STAGE_PREDECESSOR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-9A3E80EB-FB06-4491-9126-88A14D4FCB38)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_STAGE_PREDECESSOR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-68A0AF24-7DB1-4980-BA1E-6E96CB0A8055)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-07CFB993-7E60-4587-9AF1-17417C6C5EE9)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-ACB3CA51-07A5-4830-A5F3-FC1B71E37D2E)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_STAGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-CE43BABE-69B8-4D25-AF1A-B55B8084E8AB)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_STAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-92006524-7F94-4A08-B4A2-E3525F139A7E)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_PIPELINE_STAGE_RUN_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-1C7183DB-35A7-4E52-8FBF-5FE6055BFD6E)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_RUN_ARGUMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-33201634-3B07-40BA-8FF3-DDD8E8037171)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_RUN_ARGUMENT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-9E63AA89-419F-4D7C-8407-582862E43290)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_RUN_ARGUMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-0125B450-D49B-40FF-8A1B-2B08F1CE0BAC)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_RUN_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-869091AB-C7C5-4BAC-9B16-0349737CD898)
- [DBMS_CLOUD_OCI_DEVOPS_COMMIT_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-036CE12A-CED6-4F1D-9872-5B4C57C557A8)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_RUN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-F8CC1210-7D4B-42F7-8F29-E604D746CFD7)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_RUN_PROGRESS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-AC20CB02-7973-4F90-8EA0-60CC67C5FBE9)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_RUN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-373521E5-C0D6-42CF-80BB-BDF1B2743478)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_RUN_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-71D0B6FF-BB26-4E29-B360-6603450D69CE)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_RUN_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-8C92F7C0-3492-409F-B204-F77B3272FD1C)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_RUNNER_SHAPE_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-343FB059-83F7-449D-A5EB-186A75EC1886)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_SOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-C83E44D3-35B5-4FB5-A685-8CC6BAAFCDD2)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_SOURCE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E8AF1475-6C7C-4624-8EB9-6A0929136966)
- [DBMS_CLOUD_OCI_DEVOPS_NETWORK_CHANNEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-7C18D3BB-8890-49BB-9F11-4E72BE68453E)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-3E59095F-9806-4699-BAA6-B98C9F9AC51F)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_STAGE_RUN_STEP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-AA3B296E-D525-48E4-BAC2-593495C59CDC)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_STAGE_RUN_STEP_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-87BB829F-C796-4105-8CC4-9AF8C17FCC1E)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_STAGE_RUN_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-BC6618F1-EA2A-4A14-B6C4-92B115FD1BEB)
- [DBMS_CLOUD_OCI_DEVOPS_BUILD_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-13AC087A-5103-44DC-B3AB-827528AACC06)
- [DBMS_CLOUD_OCI_DEVOPS_CA_CERT_VERIFY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B169DA95-96A6-44CE-A4BC-6B325187571B)
- [DBMS_CLOUD_OCI_DEVOPS_CANCEL_BUILD_RUN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-22D3469D-5BE3-4451-B208-D5EEEEB47334)
- [DBMS_CLOUD_OCI_DEVOPS_CANCEL_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-24F0AD5E-4C94-4A63-B7F9-F254BC8C0972)
- [DBMS_CLOUD_OCI_DEVOPS_CHANGE_PROJECT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-795C4D58-7782-40E1-8AD1-72C6D2EB5AC3)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_PREDECESSOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-06AC4E15-791E-43C9-AB77-88E1D4D8469B)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_PREDECESSOR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-755BF0AC-D191-4177-850F-E510316A89C3)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_PREDECESSOR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-C8D1B862-6967-4D83-A8D0-CB3141A3B6F8)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_ROLLOUT_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-310C840B-CD64-4B5C-8F32-762148094E0D)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B513E4A9-A085-4F05-9D09-DA3812AB7521)
- [DBMS_CLOUD_OCI_DEVOPS_LOAD_BALANCER_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-6F7884F4-43F7-4150-A235-E0ABB291E3AA)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-319DC330-E31D-4295-B987-9A906FE4B424)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOY_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-BC93FD0F-43DC-44DE-9C8F-80A58AB221CE)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_EXECUTION_STEP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-894F240A-F185-4A05-8D63-411B783D32B3)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_EXECUTION_STEP_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B7ED165E-44D2-4EAC-9E95-A33B4891E400)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_EXECUTION_PROGRESS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B58E9F7B-E6CF-401A-AF1A-D448AE9AFFBC)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_EXECUTION_PROGRESS_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-52DF3712-D17F-45DB-BE64-D7135900EDD5)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B0BBC933-6AB9-438B-A6EB-488EC0B34972)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-C1003134-ECF2-44E3-9FE3-DC14AEF5F2AA)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-9AC4CD01-2599-4383-84BB-14C46BDE78B3)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOY_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-3AC62322-D5AB-42D4-8B1A-167AABA4DAA4)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT_DEPLOY_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B4BCE76A-9418-459C-A227-9802CE8B581F)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-68A7649B-C5B3-40B8-913D-E15E05329516)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT_DEPLOY_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-EB473547-1FB8-4DEF-908A-BABBC6C9A4E5)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_SELECTOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-9D083787-EBC0-4F23-9C48-BF2337DEB550)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_BY_IDS_SELECTOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-5FBB84BC-568E-49DD-8B81-2D65ED6F10CC)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_BY_QUERY_SELECTOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B3C7A6BA-5C1B-4327-B5A4-B6FACF3C9B33)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL_DEPLOY_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-C2C78B62-E3CB-43F4-924A-18097546C391)
- [DBMS_CLOUD_OCI_DEVOPS_APPROVAL_ACTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-59EE1F99-6D78-4D1D-88C7-0ADC747267E9)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-CB82DF40-C5F8-4346-93D0-EC5AA5F7EA82)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL_DEPLOY_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-62548AE5-867F-4E71-AFB4-4AA50E28591A)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_CANARY_DEPLOY_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-43C3A016-4E16-4556-88CF-57D50E11E7C2)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_CANARY_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-21572D8B-BB05-41EA-8C0F-B11A1BBA681C)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_CANARY_DEPLOY_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-6837483F-D023-4ECF-AD8A-E473B5EEFA7E)
- [DBMS_CLOUD_OCI_DEVOPS_LOAD_BALANCER_TRAFFIC_SHIFT_ROLLOUT_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-5207FE88-028B-47D0-9BC5-7C305DC9E789)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT_DEPLOY_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E8A7EF7E-DAFE-4E31-AA3D-8094F681357A)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-2CFF6B1F-CB71-49A1-8709-0A3040450B52)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT_DEPLOY_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-F2E25273-58B2-403E-A64F-FAF78EDA786B)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_SELECTOR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-CB2B408F-E9FA-4871-B5BF-7C6239FDEB3B)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_SELECTOR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-1743C8F0-27E9-4254-A964-5C13DB275281)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_ENVIRONMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-6831F245-333E-4431-86CB-8ED467F54192)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_DEPLOY_ENVIRONMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-13DC4732-393F-4EC6-9B64-FA09616E0C22)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_ENVIRONMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-96A6B619-893A-4861-8354-74BCE6611E3C)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_DEPLOY_ENVIRONMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-5A28EE84-92C3-42D2-A3A2-2C05FC0657F7)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_DEPLOY_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B492A830-6863-4C17-8BD9-EB832EFA278A)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-1E4C1371-3F21-40FF-BAED-F957ADC6A91A)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_DEPLOY_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-C190E4C1-1ED7-4CD9-904F-527FE741B086)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-76BD2E70-0E61-444D-B66D-7EE1727A76B9)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-23E444D9-BDE0-486E-BC36-C700E99B9288)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-60E7EECB-37A2-43EC-A490-A2892D6226D8)
- [DBMS_CLOUD_OCI_DEVOPS_COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-3A9133F7-8D4A-4414-B4AC-1953683F8DEA)
- [DBMS_CLOUD_OCI_DEVOPS_CONNECTION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-94C587D4-4CE3-4630-9DA4-3A167BDCE30F)
- [DBMS_CLOUD_OCI_DEVOPS_CONNECTION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-4A657FA4-EEDB-4FF0-A4E6-C126BF5A5D3C)
- [DBMS_CLOUD_OCI_DEVOPS_CONTAINER_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E4393613-6F5B-4449-8C8F-7F94DC9D3BB4)
- [DBMS_CLOUD_OCI_DEVOPS_SHAPE_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-2D348EF8-1549-45B0-9736-206E21C1EC94)
- [DBMS_CLOUD_OCI_DEVOPS_CONTAINER_INSTANCE_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-2179BABA-8A43-498F-995F-3630B700CAA0)
- [DBMS_CLOUD_OCI_DEVOPS_CONTAINER_REGISTRY_DELIVERED_ARTIFACT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-0FE496F0-2337-4602-ACC9-719F2AC80096)
- [DBMS_CLOUD_OCI_DEVOPS_COUNT_BASED_APPROVAL_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-881C71D8-0823-48A5-BA6C-6AA43548AA8B)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_WAIT_CRITERIA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-CF0D3180-EB36-4E99-A267-70FB18B0E0FF)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_ABSOLUTE_WAIT_CRITERIA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-60DA6E19-927C-4EFD-9FE0-CEFEE10BA0B9)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-93F26194-ACB2-4F92-AE41-C73989515D3A)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_BITBUCKET_CLOUD_APP_PASSWORD_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-02F173A5-A39E-473C-80BC-D65CD977972B)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_TRIGGER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-D5232D39-7BBD-4940-9652-AE307519CDC3)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_BITBUCKET_CLOUD_TRIGGER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-F74C6A1C-E002-4973-A244-AC0DBD71A64D)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_BITBUCKET_SERVER_ACCESS_TOKEN_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-4C5E70FE-9131-4B82-ADC4-0010E78D4551)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_BITBUCKET_SERVER_TRIGGER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-95C629B8-D3A9-48A8-9FBF-B7ACAF45118A)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_BUILD_PIPELINE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E780646A-793D-4242-B727-9098FFD98F04)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_BUILD_PIPELINE_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-ED105C71-255E-457E-B1E2-E3790ABA5148)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_BUILD_RUN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-2A584CB4-99AE-458E-9B4A-CBD24A2EAEE6)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_BUILD_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-A0151271-1E5E-4E56-9E6F-07BBBD3B1898)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-60748AB9-2AB5-4783-BC8A-2D19DA73752D)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-6965D1AE-4C93-4CF5-95A2-B9AAF2C8E002)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-57EA4F08-293E-4AD8-9E83-B815BBCD621F)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-EF987991-4AAE-4B04-ADB2-7BECE3CE4A5E)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_COMPUTE_INSTANCE_GROUP_CANARY_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-F01804D6-544C-4EEE-A5D7-B9C3E34FE767)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-F40DF3D5-4DF0-4400-9FC4-4140E82DC67D)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_DEPLOY_ENVIRONMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-EF86E448-3C5C-4367-86DA-6E67C2257099)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_COMPUTE_INSTANCE_GROUP_DEPLOY_ENVIRONMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-2B6E3EFD-F27D-4CA0-A8DB-9BB0A1779324)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_COMPUTE_INSTANCE_GROUP_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-7B92AEB7-F28C-43AC-BA91-0C01E16D081F)
- [DBMS_CLOUD_OCI_DEVOPS_DELIVER_ARTIFACT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-0A8AAA7C-8EAD-423B-9065-C90937748234)
- [DBMS_CLOUD_OCI_DEVOPS_DELIVER_ARTIFACT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B8F55A7E-3347-4D67-B374-A296BD46B25F)
- [DBMS_CLOUD_OCI_DEVOPS_DELIVER_ARTIFACT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E58B84C2-A394-4DA1-98F9-959ECD963349)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_DELIVER_ARTIFACT_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-6C96CBBD-071C-4F20-9D48-8780474451C0)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_ARTIFACT_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-CE2A6F7E-9B11-4615-B3BD-FA310DE75C48)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_DEPLOY_ARTIFACT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-3CD67AEF-5A98-4B91-9DD5-02157F1D8031)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOYMENT_ARGUMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-BD496D69-FED9-48E3-8EC9-5A91548FCF99)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOYMENT_ARGUMENT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-EF70AA11-0B16-43B7-80C9-FF8364134F89)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOYMENT_ARGUMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-EBF202E5-5C76-4C71-B08B-37F764901E92)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_OVERRIDE_ARGUMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-9403B03B-4EB8-4295-B223-334CE89C5EB2)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_OVERRIDE_ARGUMENT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E650E241-9F26-484B-A255-B06145981C35)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_OVERRIDE_ARGUMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-9600FF1A-09F9-40BE-8943-3304B392D9BB)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-56CCB0AB-026B-44D5-932B-D174E9085E89)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_DEPLOY_PIPELINE_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-9A78DA62-3455-4FAC-AD4C-DB677A4BEBCC)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_PARAMETER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-357939D6-CBE1-4169-8DAF-24463FD081DF)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_PARAMETER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-D75AC0AF-02E6-4A58-A301-6153EA3B9527)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_PARAMETER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-049B92C4-C1E4-49E9-B3E0-634301B98FD6)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_DEPLOY_PIPELINE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-CB00858E-C765-4F2F-B973-0D1A5A0037A7)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_DEPLOY_PIPELINE_REDEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-9DE742F7-C8A1-465C-BCA4-D6E6D37C6F0D)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_DEVOPS_CODE_REPOSITORY_TRIGGER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-0FEA1877-353F-42C5-8D79-3D1DD4520A60)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_FUNCTION_DEPLOY_ENVIRONMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-1908D8D9-9475-4346-8BFE-3E07890B8C63)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_FUNCTION_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-9D89284E-4652-4867-AE26-19F01E1DC9BD)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_GITHUB_ACCESS_TOKEN_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-6427AA0C-E914-4224-A2DE-C508AEBF7851)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_GITHUB_TRIGGER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-4B977FE6-6A64-4A58-B51F-3AB0D35E75CB)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_GITLAB_ACCESS_TOKEN_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-9E628A00-65A3-40EE-8490-2DF4017C2B40)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_GITLAB_SERVER_ACCESS_TOKEN_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E17DCB67-3409-4843-8817-22AA85CC1E76)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_GITLAB_SERVER_TRIGGER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-F6BEAC15-511F-4B78-80E3-EE176F326D39)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_GITLAB_TRIGGER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-ADA41DB9-6DA1-4B24-BC3B-4C801C275FDA)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_INVOKE_FUNCTION_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-929AE860-03DD-4A6F-ACD8-D5135204D21F)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_LOAD_BALANCER_TRAFFIC_SHIFT_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-9C0FDCCB-E149-47DF-8C2E-F423B05807F0)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_MANUAL_APPROVAL_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-04512CA5-A926-4591-98FC-8E0347576D9B)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_BLUE_GREEN_STRATEGY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-059D3FBA-6C80-489C-AABD-E951D96FA029)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_OKE_BLUE_GREEN_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-5ECA5E61-5D43-40F7-ADBD-27A0998EB1E4)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_OKE_BLUE_GREEN_TRAFFIC_SHIFT_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-3030D2C0-0573-4006-ACB6-DFE13A789C53)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_OKE_CANARY_APPROVAL_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E3EE09EE-D275-4303-9174-E1D6E5E1C295)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_CANARY_STRATEGY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-DF3AA084-53A8-4CBC-8164-8552D405EEED)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_OKE_CANARY_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-0F63AE90-5EBC-40E4-8C67-9E3B2C7BE5BC)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_OKE_CANARY_TRAFFIC_SHIFT_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B6760B64-3864-417E-B375-1F55EDACD78F)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_OKE_CLUSTER_DEPLOY_ENVIRONMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-F16316CC-D8F6-4EFE-8125-D3B191C4A410)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_OKE_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-03D2D8A2-35E0-42CA-8F51-5969A5042E44)
- [DBMS_CLOUD_OCI_DEVOPS_HELM_SET_VALUE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-28865BE2-E930-4432-A000-7F150FE7BF8F)
- [DBMS_CLOUD_OCI_DEVOPS_HELM_SET_VALUE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-500D68AF-D993-4C96-A1F6-A05FB7E3996E)
- [DBMS_CLOUD_OCI_DEVOPS_HELM_SET_VALUE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-2476574C-7425-47EE-852F-1EC69926A758)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_OKE_HELM_CHART_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-8D672282-3B53-4AFC-8010-6D8F3EFFA87C)
- [DBMS_CLOUD_OCI_DEVOPS_NOTIFICATION_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-98EA53F7-6940-43E5-8118-02526C07C5E5)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_PROJECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-C83A984C-9BB1-4266-B3D2-BA847E0CD272)
- [DBMS_CLOUD_OCI_DEVOPS_TRIGGER_SCHEDULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E61161EC-30A5-4370-BABC-B953DA61BF11)
- [DBMS_CLOUD_OCI_DEVOPS_MIRROR_REPOSITORY_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-3F3A11D0-9CE6-477C-8118-E6E88082D7E5)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_REPOSITORY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-C4B99FB6-67A4-4607-AEC0-9AF0B0C5A86F)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_SHELL_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-36B6DA30-0C3A-42F2-B05C-4295D8FA46AB)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_SINGLE_DEPLOY_STAGE_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-5A5A3FCB-FA74-4EEE-AC8F-9849E8DE4CC5)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_SINGLE_DEPLOY_STAGE_REDEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-0661FCFC-2C72-40DD-87E1-9E699DBE2E9E)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_TRIGGER_DEPLOYMENT_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-ECF8663C-F7A2-488B-925D-E64A547B731D)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_VBS_ACCESS_TOKEN_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B0F15C02-27D6-4BE8-B4EA-D6A26E3C63F8)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_VBS_TRIGGER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B4D19FB4-60E6-49DA-87BC-A06C48E455AB)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_WAIT_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-8051A5CB-D806-46C4-86DD-8580E930D525)
- [DBMS_CLOUD_OCI_DEVOPS_CREATE_WAIT_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-9B4368E2-D572-436E-B042-8CA4DC708632)
- [DBMS_CLOUD_OCI_DEVOPS_CUSTOM_BUILD_RUNNER_SHAPE_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-4A157FFA-0262-4B13-9101-E69BEA4F1B2A)
- [DBMS_CLOUD_OCI_DEVOPS_DEFAULT_BUILD_RUNNER_SHAPE_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-F351F33A-A280-4E1C-B55E-1929958E8806)
- [DBMS_CLOUD_OCI_DEVOPS_DELIVER_ARTIFACT_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-FFDBE6E3-7146-4F9C-B84F-9276A4C24381)
- [DBMS_CLOUD_OCI_DEVOPS_DELIVER_ARTIFACT_STAGE_RUN_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-52FF7F71-3F17-474A-8571-7F9587A56D0D)
- [DBMS_CLOUD_OCI_DEVOPS_DELIVER_ARTIFACT_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-A0C28A11-A74B-44B0-8BC1-9C2EAC48B435)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_ARTIFACT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-52772FAA-B449-4410-8F21-5580942692BC)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_ARTIFACT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-9D53029F-8B6F-4494-B878-D17FEE637544)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_ARTIFACT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-D0EA5115-7E25-4F38-91F0-A1129DD06440)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_ARTIFACT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-35A53A28-3134-494C-BC54-7FDD38D119AF)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_ENVIRONMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E5B081B5-E704-4BCC-8BE4-EABB553A55EE)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_ENVIRONMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-EE02632E-5B31-4FB8-9E52-6DD1C6A0A2D6)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-5AAA5964-C530-47D8-B7F2-D0A204BC6799)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_STAGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-D5B852BC-EEAA-40DD-A777-E10E4CDAC0AA)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_STAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-D6A34294-B628-4432-98CF-396B4F9EA502)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_ARTIFACT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-DE1AB867-CD02-4330-8FD4-B18C407DFA8F)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_ARTIFACT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-5C3B6C21-C654-409D-86AA-35E270BBC316)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_ARTIFACT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-1A83EC2E-F4B9-4CC5-B449-08708197AB1E)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_ENVIRONMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-1394E872-7660-4D0B-A161-62685C9986D9)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_ENVIRONMENT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-A7DAC3FD-78DF-4573-B552-58BB451809CA)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_ENVIRONMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-39963AC7-A1CF-4EDF-922D-8A5CD1D3016D)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-5A316BC1-B21A-4742-86DD-8241B26449D0)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-59979820-6E55-47D2-B468-BBEDE6C8E97C)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-5048C0D0-3E11-4314-ACED-1D1B3B2DC6B1)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-6E66A887-B240-408D-BAAF-C6DB54EB834D)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOYMENT_EXECUTION_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-1E727A10-CCD0-43B4-A024-7B018EDA6EEB)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOYMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-F714C4CD-9E04-48FD-A496-ECECD83DBD60)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_DEPLOYMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-23C82BCB-FEAB-4280-8DCA-9AFFB100A363)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOYMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E1F5237E-BB31-43E7-8C81-700D56D3415E)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_DEPLOYMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B20DC12B-D017-4A39-A836-F55274D7D17E)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_REDEPLOYMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B9BB51CA-4F6C-4E9B-B808-023A8CAB269A)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_PIPELINE_REDEPLOYMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-345BBB56-A6F9-46B1-8EF5-F65888C5AA25)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-07EE7EA4-1BD0-41B8-B068-06EBB0C24EB9)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOY_STAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E8F29C7F-2D35-4464-8777-D3D63ADEF781)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOYMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-852134E7-BFE6-455B-9D06-2E933DE3517F)
- [DBMS_CLOUD_OCI_DEVOPS_DEPLOYMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-FADC7520-9DC3-4AF0-A96B-07F3A6391C83)
- [DBMS_CLOUD_OCI_DEVOPS_DEVOPS_CODE_REPOSITORY_BUILD_RUN_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-3062F11E-0BE0-4202-BD90-A2B3F06BEA42)
- [DBMS_CLOUD_OCI_DEVOPS_DEVOPS_CODE_REPOSITORY_BUILD_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-2799F443-D3CA-4311-AA26-4089001A9E57)
- [DBMS_CLOUD_OCI_DEVOPS_DEVOPS_CODE_REPOSITORY_FILTER_ATTRIBUTES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-C45996DB-3DCA-4609-A160-300BFAA6D550)
- [DBMS_CLOUD_OCI_DEVOPS_DEVOPS_CODE_REPOSITORY_FILTER_EXCLUSION_ATTRIBUTES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-C9390B61-59A2-43FA-9C3E-3F4E91879E40)
- [DBMS_CLOUD_OCI_DEVOPS_DEVOPS_CODE_REPOSITORY_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-CE1B5B9E-42EA-46D3-94CE-A6A6E397962B)
- [DBMS_CLOUD_OCI_DEVOPS_DEVOPS_CODE_REPOSITORY_TRIGGER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-3DEB34E9-4FDD-422C-ADB0-3727B7F906A3)
- [DBMS_CLOUD_OCI_DEVOPS_DEVOPS_CODE_REPOSITORY_TRIGGER_CREATE_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-A832B93D-CF8E-4AA3-B80B-EC58A676CA8C)
- [DBMS_CLOUD_OCI_DEVOPS_DEVOPS_CODE_REPOSITORY_TRIGGER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-05174E78-8E4F-4DCE-A61F-92E40218FC0C)
- [DBMS_CLOUD_OCI_DEVOPS_DIFF_LINE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-A58403AF-89B8-44F9-973C-CFCDFFFC0237)
- [DBMS_CLOUD_OCI_DEVOPS_DIFF_LINE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-C3299747-7ABD-42B5-9B2B-128677C68614)
- [DBMS_CLOUD_OCI_DEVOPS_DIFF_SECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-C3AD3E15-6079-4140-AA11-D7143B71C32E)
- [DBMS_CLOUD_OCI_DEVOPS_DIFF_SECTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-8AC0B838-FACD-4847-9370-F3EF8D11104C)
- [DBMS_CLOUD_OCI_DEVOPS_DIFF_CHUNK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-8392F198-5914-41E1-85CB-456625FD6A8B)
- [DBMS_CLOUD_OCI_DEVOPS_DIFF_CHUNK_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-BEBECB6B-B85F-4947-ACA5-54029C87EBA2)
- [DBMS_CLOUD_OCI_DEVOPS_DIFF_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-2173DC11-1DE1-4C79-BD97-A43E34145E38)
- [DBMS_CLOUD_OCI_DEVOPS_DIFF_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-F3F6019C-B8F6-447F-AC89-49D591CB3DF9)
- [DBMS_CLOUD_OCI_DEVOPS_DIFF_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-90FE173E-E101-4776-8E30-5A1AFE22AFFE)
- [DBMS_CLOUD_OCI_DEVOPS_DIFF_RESPONSE_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-85EE08E8-2862-48A8-8DAB-12A1BC082C32)
- [DBMS_CLOUD_OCI_DEVOPS_DIFF_RESPONSE_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B1452BE8-42C3-42B2-9AB6-2A6D6F676D7F)
- [DBMS_CLOUD_OCI_DEVOPS_DIFF_RESPONSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-34399C89-8FD2-4D53-812A-6AAF83F001E2)
- [DBMS_CLOUD_OCI_DEVOPS_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-914AAE52-9C29-4FD4-BAC0-DD89CCCCFC23)
- [DBMS_CLOUD_OCI_DEVOPS_FILE_DIFF_RESPONSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-961FB3D9-9687-461C-8E11-893977A312F1)
- [DBMS_CLOUD_OCI_DEVOPS_FILE_LINE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-A005EF51-5F87-4CC5-BCD6-CF63B801606F)
- [DBMS_CLOUD_OCI_DEVOPS_FUNCTION_DEPLOY_ENVIRONMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-F13BB716-EA62-4DB4-9776-FB0A7340457C)
- [DBMS_CLOUD_OCI_DEVOPS_FUNCTION_DEPLOY_ENVIRONMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E9179937-2750-4EFC-8E43-24EE9CD68180)
- [DBMS_CLOUD_OCI_DEVOPS_FUNCTION_DEPLOY_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-AFB516A8-7179-43B0-B57C-80198980A150)
- [DBMS_CLOUD_OCI_DEVOPS_FUNCTION_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-1DF0B0AA-13A1-410A-AE93-ECA5780C77D0)
- [DBMS_CLOUD_OCI_DEVOPS_FUNCTION_DEPLOY_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-5C77723E-16A0-441D-9840-533726C87120)
- [DBMS_CLOUD_OCI_DEVOPS_GENERIC_DELIVERED_ARTIFACT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-2CD6F60F-3F86-41A2-87F9-4E4F3E9003E5)
- [DBMS_CLOUD_OCI_DEVOPS_GENERIC_DEPLOY_ARTIFACT_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-D45E4570-A143-4EC3-869E-680C1699F28B)
- [DBMS_CLOUD_OCI_DEVOPS_GITHUB_ACCESS_TOKEN_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-A759791A-3744-4F3C-B4F6-A658203AE94C)
- [DBMS_CLOUD_OCI_DEVOPS_GITHUB_ACCESS_TOKEN_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-328E565E-21DD-4CAF-B451-4A44F4112D55)
- [DBMS_CLOUD_OCI_DEVOPS_GITHUB_BUILD_RUN_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-C9BA7AA7-CD2C-449C-B76B-3A796F65EB67)
- [DBMS_CLOUD_OCI_DEVOPS_GITHUB_BUILD_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-03B4077D-E025-47A7-A54C-B9B15E7E14A8)
- [DBMS_CLOUD_OCI_DEVOPS_GITHUB_FILTER_ATTRIBUTES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-A0F812FC-AB45-4C90-B736-9567DE2EEA84)
- [DBMS_CLOUD_OCI_DEVOPS_GITHUB_FILTER_EXCLUSION_ATTRIBUTES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-8E3BA6C0-8188-4015-868A-B1EF2AC9D970)
- [DBMS_CLOUD_OCI_DEVOPS_GITHUB_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-8EF0DFC3-2C9E-4729-8E31-C20DCEE25EA4)
- [DBMS_CLOUD_OCI_DEVOPS_GITHUB_TRIGGER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-7BE49E7F-2801-48F6-BE03-B98EC8913B5C)
- [DBMS_CLOUD_OCI_DEVOPS_GITHUB_TRIGGER_CREATE_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-DB81FBD9-B76F-45F1-AD45-6DBFB4D4462D)
- [DBMS_CLOUD_OCI_DEVOPS_GITHUB_TRIGGER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-D006A7AC-EBC8-4934-BB38-9F31695D4381)
- [DBMS_CLOUD_OCI_DEVOPS_GITLAB_ACCESS_TOKEN_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-022F9113-0976-457F-BF2F-A9FBE841914F)
- [DBMS_CLOUD_OCI_DEVOPS_GITLAB_ACCESS_TOKEN_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-C59CF4B7-106E-49AD-AB26-19F1EA517E51)
- [DBMS_CLOUD_OCI_DEVOPS_GITLAB_BUILD_RUN_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-D77B9291-26A5-4FEA-9072-E24BCD5E6B36)
- [DBMS_CLOUD_OCI_DEVOPS_GITLAB_BUILD_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-9BB2789D-DC0E-4704-977A-3CBAF2C2D519)
- [DBMS_CLOUD_OCI_DEVOPS_GITLAB_FILTER_ATTRIBUTES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-99DA1B5B-751D-49E4-B9A6-C8FC63D4DF4A)
- [DBMS_CLOUD_OCI_DEVOPS_GITLAB_FILTER_EXCLUSION_ATTRIBUTES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E8135F31-53CD-4D27-B5D6-D55E57A522B0)
- [DBMS_CLOUD_OCI_DEVOPS_GITLAB_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-BD296C82-25E1-41A4-843A-0D3F38BA3EF5)
- [DBMS_CLOUD_OCI_DEVOPS_GITLAB_SERVER_ACCESS_TOKEN_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-FABB52E4-7A94-4400-AFA3-79FE89F55409)
- [DBMS_CLOUD_OCI_DEVOPS_GITLAB_SERVER_ACCESS_TOKEN_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-37112B83-4374-4C0D-A2C2-3FC45427E786)
- [DBMS_CLOUD_OCI_DEVOPS_GITLAB_SERVER_BUILD_RUN_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-AD3A3193-0427-4B4B-9952-2EACFF9914C8)
- [DBMS_CLOUD_OCI_DEVOPS_GITLAB_SERVER_BUILD_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-FFDE9165-F6D5-4CBF-BA21-00DBBA5310E7)
- [DBMS_CLOUD_OCI_DEVOPS_GITLAB_SERVER_FILTER_ATTRIBUTES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-BD11D23C-25F2-4B05-BDBD-FD0F2348F8FB)
- [DBMS_CLOUD_OCI_DEVOPS_GITLAB_SERVER_FILTER_EXCLUSION_ATTRIBUTES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-5861E72F-84A4-4668-AD38-C13A30B14B13)
- [DBMS_CLOUD_OCI_DEVOPS_GITLAB_SERVER_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-9B7571E2-E04B-4BEB-A4FD-CDC9FE4CD570)
- [DBMS_CLOUD_OCI_DEVOPS_GITLAB_SERVER_TRIGGER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-F8F10E21-5FC9-44D5-9101-390C3BDA93E0)
- [DBMS_CLOUD_OCI_DEVOPS_GITLAB_SERVER_TRIGGER_CREATE_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-A36A1452-8D37-45FD-9F6C-CD57E8C367A1)
- [DBMS_CLOUD_OCI_DEVOPS_GITLAB_SERVER_TRIGGER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-51154EE9-0005-4A27-92E1-15BEBE4F9115)
- [DBMS_CLOUD_OCI_DEVOPS_GITLAB_TRIGGER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-307844C6-34C4-4FB6-9366-36EDA0FEB8F6)
- [DBMS_CLOUD_OCI_DEVOPS_GITLAB_TRIGGER_CREATE_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-48033E68-BD3C-482F-A71F-532C02B89645)
- [DBMS_CLOUD_OCI_DEVOPS_GITLAB_TRIGGER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-375BC558-24CC-4297-BD1F-57B02A996E3C)
- [DBMS_CLOUD_OCI_DEVOPS_VERIFICATION_KEY_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-55451091-72D2-4783-A404-DFE89EB2FF36)
- [DBMS_CLOUD_OCI_DEVOPS_HELM_REPOSITORY_DEPLOY_ARTIFACT_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-DA119729-2B7D-48EA-A4A7-94B9898B8A2E)
- [DBMS_CLOUD_OCI_DEVOPS_INLINE_DEPLOY_ARTIFACT_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-8079D151-77B1-495F-9C7B-6012C6A3202D)
- [DBMS_CLOUD_OCI_DEVOPS_INLINE_PUBLIC_KEY_VERIFICATION_KEY_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-5618E4C5-6343-40B2-861F-DFBDC4C2AFAF)
- [DBMS_CLOUD_OCI_DEVOPS_INVOKE_FUNCTION_DEPLOY_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-BBD9BB33-989B-4DE3-83F8-ED42FA4838D9)
- [DBMS_CLOUD_OCI_DEVOPS_INVOKE_FUNCTION_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-F071E837-1855-4959-9DE2-A147B275C669)
- [DBMS_CLOUD_OCI_DEVOPS_INVOKE_FUNCTION_DEPLOY_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-BF512616-A28C-494F-8F52-369DC8A8447D)
- [DBMS_CLOUD_OCI_DEVOPS_LOAD_BALANCER_TRAFFIC_SHIFT_DEPLOY_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E6F7A848-19C9-48B7-B629-1794B6138E35)
- [DBMS_CLOUD_OCI_DEVOPS_LOAD_BALANCER_TRAFFIC_SHIFT_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-FDC6A33E-457B-45C9-9134-C7963270F8EB)
- [DBMS_CLOUD_OCI_DEVOPS_LOAD_BALANCER_TRAFFIC_SHIFT_DEPLOY_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-BFF7B50D-28A1-4EA8-9F68-ACBC37F7F9B4)
- [DBMS_CLOUD_OCI_DEVOPS_MANUAL_APPROVAL_DEPLOY_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-8CD86BC0-C1D3-4521-A852-37FC1A6BF586)
- [DBMS_CLOUD_OCI_DEVOPS_MANUAL_APPROVAL_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-4995BB43-0837-4755-B95C-90A0E66F0FFC)
- [DBMS_CLOUD_OCI_DEVOPS_MANUAL_APPROVAL_DEPLOY_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-0233592C-3E08-4CE3-94E0-831AEBE647A9)
- [DBMS_CLOUD_OCI_DEVOPS_MANUAL_BUILD_RUN_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-6F16A5A2-0885-4AB5-A7F3-23CA3CC36B99)
- [DBMS_CLOUD_OCI_DEVOPS_NGINX_BLUE_GREEN_STRATEGY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B03E1E22-1047-410F-872C-BA2006EBA9A7)
- [DBMS_CLOUD_OCI_DEVOPS_NGINX_CANARY_STRATEGY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-F26B1E96-52C7-4CED-9F62-A835E61A96FD)
- [DBMS_CLOUD_OCI_DEVOPS_NO_DEPLOY_STAGE_ROLLBACK_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-677388B4-D8D9-4056-A84E-1FE93DD401B3)
- [DBMS_CLOUD_OCI_DEVOPS_NONE_VERIFICATION_KEY_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-1D2850D5-3973-4094-A658-0E8330C6B16C)
- [DBMS_CLOUD_OCI_DEVOPS_OCIR_DEPLOY_ARTIFACT_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-517459CB-BC2B-455B-974D-4785024F1FC9)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_BLUE_GREEN_DEPLOY_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-98F3C869-05CD-46F1-92FF-23E9C6BE3F19)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_BLUE_GREEN_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-1E6DA636-1D65-4A96-A998-DAD6975F2378)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_BLUE_GREEN_DEPLOY_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-A31DB527-6879-4F1E-AF0E-65C1E6C9EE61)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_BLUE_GREEN_TRAFFIC_SHIFT_DEPLOY_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B9DE1067-29F2-451A-A62B-489036B84EB8)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_BLUE_GREEN_TRAFFIC_SHIFT_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-084CB84B-4B68-4762-90DA-6B42E6BB3295)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_BLUE_GREEN_TRAFFIC_SHIFT_DEPLOY_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-1C66A584-B0C5-4F00-B2F2-8D960BC8EBD1)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_CANARY_APPROVAL_DEPLOY_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-16B4984D-3CE5-4FCF-A06A-8D0AA70472FE)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_CANARY_APPROVAL_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-F07BCE73-7DD8-4EE9-BDDC-C9A7AD65A275)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_CANARY_APPROVAL_DEPLOY_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-FACDA57E-1144-4505-AE6E-66A18723D24B)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_CANARY_DEPLOY_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-FDBB60C2-6403-4CE0-A939-6B456B5FF135)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_CANARY_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-FC935EAA-4837-4B7C-B912-89025D8C0382)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_CANARY_DEPLOY_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-81C1AAAA-FFAE-47DE-B788-810C93276916)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_CANARY_TRAFFIC_SHIFT_DEPLOY_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B0A61B32-9FE8-421A-967D-C451EE83B0E3)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_CANARY_TRAFFIC_SHIFT_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-3F330675-62D3-477B-A52E-A7DBBE4DC01A)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_CANARY_TRAFFIC_SHIFT_DEPLOY_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-5A517BE3-232E-4F4E-830A-8CBF3CC31B6A)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_CLUSTER_DEPLOY_ENVIRONMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-AF6094FD-8256-4E99-AB65-1FD81E98B73D)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_CLUSTER_DEPLOY_ENVIRONMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-A5B39F22-9AA1-4255-ACD0-4C4E3F41A79A)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_DEPLOY_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-1DFE43A4-CEDE-4EF3-B694-4D51D93E17C8)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-14A8FE12-29B6-43E8-85E6-B0146E9CC82D)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_DEPLOY_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-00E08FBE-E277-4BAA-A8D0-880AF92E25FD)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_HELM_CHART_DEPLOY_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-6E126511-C87F-42FA-B633-A9D88686E2C2)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_HELM_CHART_DEPLOY_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-19F87076-FD26-4982-8A5A-90CB6B53EF04)
- [DBMS_CLOUD_OCI_DEVOPS_OKE_HELM_CHART_DEPLOYMENT_STAGE_EXECUTION_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-510D0D8F-9156-4D14-9674-F193FAE42B2B)
- [DBMS_CLOUD_OCI_DEVOPS_PRIVATE_ENDPOINT_CHANNEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-EFCD6D7F-E9FD-42D9-BD43-A081B05D6AE1)
- [DBMS_CLOUD_OCI_DEVOPS_PROJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-3A263D40-4DFE-4B73-B18E-A0B09146A4ED)
- [DBMS_CLOUD_OCI_DEVOPS_PROJECT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-02A9776B-7587-43E1-A31C-E654A1165201)
- [DBMS_CLOUD_OCI_DEVOPS_PROJECT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-2BDF9F58-9193-4527-8B5C-A44F20A7D153)
- [DBMS_CLOUD_OCI_DEVOPS_PROJECT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-5DE139E3-D7C2-4B20-B922-C443F1FCAA1E)
- [DBMS_CLOUD_OCI_DEVOPS_PUT_REPOSITORY_REF_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-EBA94A0D-892E-4423-8E66-F342FDAD8B73)
- [DBMS_CLOUD_OCI_DEVOPS_PUT_REPOSITORY_BRANCH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-22635EA0-95CA-43CF-BD1C-1AAA72E4ED2A)
- [DBMS_CLOUD_OCI_DEVOPS_PUT_REPOSITORY_TAG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-3371F67E-3C21-41E8-9724-D8CB6C1371C6)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-3EC13DC4-DC72-49C5-826A-538B69605F3A)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_AUTHOR_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E981B9A3-03E4-465D-B6FD-0BFC88DA0A14)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_AUTHOR_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E5732817-17B3-4CD2-AD7E-FEDF8C2AA7F3)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_AUTHOR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-6C2AA052-F697-4826-96CE-FB732AAD83A4)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_REF_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-82C287C7-E617-4E88-81D3-382CBF129F0E)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_BRANCH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-4B6FF9D8-8B27-4603-94E6-46E3CC2E336C)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_REF_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-63EE7FC7-930A-4578-80DC-5D835E1EBADD)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_BRANCH_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-78483317-E9DE-4C1D-A6BC-82F9FD11D019)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-6C98CBBC-3326-49E0-AA72-2F9C7039058D)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-D5E5171E-6DEF-428D-8660-9B4F1C924EAB)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E80FEB37-853B-4F95-AA28-AF7964DB21BB)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_COMMIT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-077F6302-59E8-44A2-A159-CED588906F9E)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_COMMIT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-6C2D33CE-4ACF-4980-ACDF-CCDBD0A75CC9)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_COMMIT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-CB91B706-F826-42D9-BB2D-9DD44869F6E9)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_COMMIT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-F2B994E3-E360-4E4D-8D6F-9B97B72759B4)
- [DBMS_CLOUD_OCI_DEVOPS_FILE_LINE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B9443E71-F562-464B-898F-069444B3A021)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_FILE_LINES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-6AAF7AFF-83B9-4063-A7B5-FB1DBB325726)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_MIRROR_RECORD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-D9B0B434-66F6-40F4-93B4-0C4D02D01C80)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_MIRROR_RECORD_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B2D04F43-B27A-456A-AA9B-EF0F64685A83)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_MIRROR_RECORD_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-772AEB24-5302-47C4-A413-3CA343EA4D89)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_MIRROR_RECORD_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-F0A24263-749E-4BB5-AFA3-D37078358D6F)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_OBJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-2A8D09E1-2D32-46B0-AC3D-231996B97373)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_PATH_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-891171BC-0240-4550-B65B-9BD3C420E788)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_PATH_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-FB71AC85-5850-4F35-9F2B-CA31C0382ABA)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_PATH_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-865373F7-11D8-4850-9848-D1834F16D60E)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_REF_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-3086C8D5-6C98-403F-AA4B-DCB2287F868D)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_REF_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-BE57C804-9475-471F-B6CA-5C0D9A54F8F2)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_TAG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-FA7876E1-8699-40AD-BB83-096229282FEA)
- [DBMS_CLOUD_OCI_DEVOPS_REPOSITORY_TAG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-AAE6F5F0-8E33-4AC6-B24B-9FEA0F3AB9F8)
- [DBMS_CLOUD_OCI_DEVOPS_SERVICE_VNIC_CHANNEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-EC1F1815-F0DB-4A55-9094-0984B5FA2B2A)
- [DBMS_CLOUD_OCI_DEVOPS_SHELL_DEPLOY_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-D7DBA232-D016-4FC1-9980-1FF63383888B)
- [DBMS_CLOUD_OCI_DEVOPS_SHELL_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-9B55661D-9BF1-4148-A1CB-C167AAAFCA72)
- [DBMS_CLOUD_OCI_DEVOPS_SHELL_DEPLOY_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-54BCA516-1859-4EA2-906C-2BCBBCDF4685)
- [DBMS_CLOUD_OCI_DEVOPS_SINGLE_DEPLOY_STAGE_DEPLOYMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-1B4CE761-567E-4373-9F6F-97E71F4AF01D)
- [DBMS_CLOUD_OCI_DEVOPS_SINGLE_DEPLOY_STAGE_DEPLOYMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-D0E60562-551D-4D68-B1F9-C4CAA3ADBE9D)
- [DBMS_CLOUD_OCI_DEVOPS_SINGLE_DEPLOY_STAGE_REDEPLOYMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-38C3E7C2-0C60-46C1-844C-C5C584F7F987)
- [DBMS_CLOUD_OCI_DEVOPS_SINGLE_DEPLOY_STAGE_REDEPLOYMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-0D7E579B-3338-4747-B59B-79B5DA9DD92E)
- [DBMS_CLOUD_OCI_DEVOPS_TRIGGER_BUILD_PIPELINE_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-5D466F74-97EF-4436-9BA6-4E098FB8A4E9)
- [DBMS_CLOUD_OCI_DEVOPS_TRIGGER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-710EE08E-0D07-44B1-9369-CB92134602F2)
- [DBMS_CLOUD_OCI_DEVOPS_TRIGGER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-BA20D5AD-27C0-4442-98B0-1EF8D654E156)
- [DBMS_CLOUD_OCI_DEVOPS_TRIGGER_DEPLOYMENT_PIPELINE_STAGE_RUN_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-FA0A4FB2-198A-4D91-87D7-39CAA2F8779A)
- [DBMS_CLOUD_OCI_DEVOPS_TRIGGER_DEPLOYMENT_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-5CE3BFF3-47BE-4F6F-B391-D5A1E1E0A39A)
- [DBMS_CLOUD_OCI_DEVOPS_TRIGGER_DEPLOYMENT_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-025D8B0E-B52E-4132-9830-185CC5D5FCFF)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_WAIT_CRITERIA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-885D8982-5B7C-4BE3-87DF-40F6D3B182C1)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_ABSOLUTE_WAIT_CRITERIA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-ACE554A1-CB51-4086-A412-CD5F6FA6447F)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-66C6670B-2BC5-4FFA-BBCE-285620DEA9A0)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_BITBUCKET_CLOUD_APP_PASSWORD_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-0525CD4C-EDF9-4765-9487-76B301403EB8)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_TRIGGER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-D2626ECB-672C-4557-8E3A-C3EDC9387EA3)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_BITBUCKET_CLOUD_TRIGGER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-C3DA9D15-E737-4442-B31B-81CE6BA364B8)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_BITBUCKET_SERVER_ACCESS_TOKEN_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-D8A1540E-1BCC-4BA8-BC75-7757D750DC3F)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_BITBUCKET_SERVER_TRIGGER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-62C936DF-EEA1-4137-A58F-3A50E6399E0B)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_BUILD_PIPELINE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-DB5B89B9-0169-4FFE-9966-9C40C9A7064F)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_BUILD_PIPELINE_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-4859170B-A854-4A93-A12E-CF4C613747B2)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_BUILD_RUN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-4FF80C9B-311B-45C6-AECE-2E39DCE746BE)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_BUILD_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-BB0024E9-DB30-49C7-84BC-837805C6643C)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B1177FA4-DF0E-41BB-B2CA-6958ADE023E8)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-FFD34D8C-3D0D-4D00-9A4F-86DA10DF64D5)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-F2CFB474-8FD0-4D52-AB12-884F92AB703E)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E4CA97AA-F7F8-4756-8F8A-8F317F0A6670)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_COMPUTE_INSTANCE_GROUP_CANARY_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-8FDE1014-E775-4B94-85B4-0A15DE8D56EA)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E4275721-FC64-4ABF-8D35-FA2F84B4C635)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_DEPLOY_ENVIRONMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-6CF42DF4-28E3-4EB8-825B-D0E053D5517B)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_COMPUTE_INSTANCE_GROUP_DEPLOY_ENVIRONMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-C1ECC976-404C-4AAA-907D-5ED19B8F6C70)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_COMPUTE_INSTANCE_GROUP_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-1F7665BF-FCF3-4C37-8847-FFD8DAD344FC)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_DELIVER_ARTIFACT_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-D6215CA6-F555-4E53-884C-F52FFC58FA45)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_DEPLOY_ARTIFACT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B503FBC2-FFA1-4B50-BC9E-9742EF812971)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-BFD6A29D-7F0E-4F3C-BDFE-9C2CD9981780)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_DEPLOY_PIPELINE_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B110A811-2974-4BE4-BB41-B2DCBC1DEC2B)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_DEPLOY_PIPELINE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-C4FE7460-BDAC-416D-916C-C67B5D62FD46)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_DEPLOY_PIPELINE_REDEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-3A4E7A19-58CD-4C3E-B26E-35700F596C7D)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_DEVOPS_CODE_REPOSITORY_TRIGGER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-4EC7EE3F-A1AA-4B3D-BA5A-D536B308CC2E)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_FUNCTION_DEPLOY_ENVIRONMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-22FF94F1-4DE3-4F78-A6AF-9EACE40BCB38)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_FUNCTION_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-28A3C575-E409-4040-BC78-A47FEBB3AA13)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_GITHUB_ACCESS_TOKEN_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B7659972-5F0E-4319-819B-676AE7DCA4FD)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_GITHUB_TRIGGER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-D7379D88-8097-47E5-9991-F63CD6829EA5)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_GITLAB_ACCESS_TOKEN_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-45E1FDBB-F734-4A27-BF9D-3ABBFF5B0C58)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_GITLAB_SERVER_ACCESS_TOKEN_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-7A4B637F-B10B-416A-A815-63BB4B8B6E9D)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_GITLAB_SERVER_TRIGGER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-A41877B0-3F32-4CDA-BA40-DABE880EDEB0)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_GITLAB_TRIGGER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-DC308E8B-E4AB-4FD5-BD36-EB5BCA0DE387)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_INVOKE_FUNCTION_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E0AB4D9A-9272-43AF-AA6B-93D91346B194)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_LOAD_BALANCER_TRAFFIC_SHIFT_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-F1A92912-3901-4995-A041-E61C9CF07EF8)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_MANUAL_APPROVAL_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-CF18D738-B546-433D-92AF-37C9324BFAD6)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_OKE_BLUE_GREEN_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E5811A0C-1FF5-47CD-B11A-16A151F14C6D)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_OKE_BLUE_GREEN_TRAFFIC_SHIFT_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-C749F909-808E-4819-92DA-2592D7C2E9E4)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_OKE_CANARY_APPROVAL_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-637E7547-5965-4455-B6C5-4FB25E6CAE36)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_OKE_CANARY_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-6FF324DA-8896-479E-8DBB-619BDBFB1BFA)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_OKE_CANARY_TRAFFIC_SHIFT_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-1D7F0548-2F42-4E2B-933D-06BAC7194942)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_OKE_CLUSTER_DEPLOY_ENVIRONMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-339D964B-E5C4-487A-859A-DCDB8D07A6FC)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_OKE_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-722ED155-385C-4286-A1F5-FB6D2E47E872)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_OKE_HELM_CHART_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-7FA36788-F702-42C6-9B40-F26CC313A461)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_PROJECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-2712C2EF-881E-4AEC-9830-85C88E85416B)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_REPOSITORY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-731CD962-0DFC-4579-BE7E-1CB3B34878FD)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_SHELL_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-F06A2DAA-E4C7-4CF5-8368-FBF82A133036)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_SINGLE_DEPLOY_STAGE_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-0DB32676-CA42-4B1E-B050-BAFCA2B603F9)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_SINGLE_DEPLOY_STAGE_REDEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-5709F159-AABB-4001-B973-57C3CB10271A)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_TRIGGER_DEPLOYMENT_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-965D49EC-21F4-4AB7-BA4B-824756D68A6E)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_VBS_ACCESS_TOKEN_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-D139A314-9B94-4F4E-B4E4-DC1BA9F75F88)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_VBS_TRIGGER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-66DDD339-29EB-4843-B4D3-5B42D3C64D3F)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_WAIT_DEPLOY_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-4AC81A89-BB0D-4526-9BFD-ED0AFBF1507C)
- [DBMS_CLOUD_OCI_DEVOPS_UPDATE_WAIT_STAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-90EAD435-6E66-4A6E-B909-A7380DD71C03)
- [DBMS_CLOUD_OCI_DEVOPS_VAULT_SECRET_VERIFICATION_KEY_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-264874DC-81DD-4EA0-871B-B52F49D5FF50)
- [DBMS_CLOUD_OCI_DEVOPS_VBS_ACCESS_TOKEN_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-2F5710E6-A1BC-4E35-AB1E-5CE2E69C549E)
- [DBMS_CLOUD_OCI_DEVOPS_VBS_ACCESS_TOKEN_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-CD5EB34E-0C10-4789-AC63-78A6DAA7DAD8)
- [DBMS_CLOUD_OCI_DEVOPS_VBS_BUILD_RUN_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-3D6A3532-8A58-4A09-82C7-8E04B1050B2E)
- [DBMS_CLOUD_OCI_DEVOPS_VBS_BUILD_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-AE1331F3-957D-478B-AC87-40BBCA5EF8A6)
- [DBMS_CLOUD_OCI_DEVOPS_VBS_FILTER_ATTRIBUTES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-4249AF30-62F9-4810-9FAC-77721FF91CD8)
- [DBMS_CLOUD_OCI_DEVOPS_VBS_FILTER_EXCLUSION_ATTRIBUTES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-F7BE6AF6-46D1-4552-90EB-93C50C02EC79)
- [DBMS_CLOUD_OCI_DEVOPS_VBS_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-3565BAFA-EEF2-4313-8217-F9358D94A554)
- [DBMS_CLOUD_OCI_DEVOPS_VBS_TRIGGER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-363D7124-77A7-44E4-AA3C-1EE50DA7C7C6)
- [DBMS_CLOUD_OCI_DEVOPS_VBS_TRIGGER_CREATE_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-981C1573-297E-4B42-BC49-AB76C15032AC)
- [DBMS_CLOUD_OCI_DEVOPS_VBS_TRIGGER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-92BB77FB-4CED-460E-A0BF-F710A25396E4)
- [DBMS_CLOUD_OCI_DEVOPS_WAIT_DEPLOY_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-831FA02E-3D35-4A61-832C-5C4F9524CD92)
- [DBMS_CLOUD_OCI_DEVOPS_WAIT_DEPLOY_STAGE_EXECUTION_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B6DEC056-77DE-4078-BEA2-5683E0590B5B)
- [DBMS_CLOUD_OCI_DEVOPS_WAIT_DEPLOY_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-881E436E-1B6B-4097-B496-2EC58BDD9B0D)
- [DBMS_CLOUD_OCI_DEVOPS_WAIT_STAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-BDDB63DC-FA4A-458B-A170-6624DC3A3F8A)
- [DBMS_CLOUD_OCI_DEVOPS_WAIT_STAGE_RUN_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-D66B4878-D128-478D-979E-03111FF18263)
- [DBMS_CLOUD_OCI_DEVOPS_WAIT_STAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B8D3E130-9FED-42E6-9406-A72C30B5F11C)
- [DBMS_CLOUD_OCI_DEVOPS_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-047C84DD-C0E1-42F5-9288-629DCA144EE7)
- [DBMS_CLOUD_OCI_DEVOPS_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-CC48A4E3-C66C-42FE-8A14-F1BB54509250)
- [DBMS_CLOUD_OCI_DEVOPS_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-FDC3CA73-4E80-418C-91CE-14A574620F59)
- [DBMS_CLOUD_OCI_DEVOPS_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-B7A59A26-05A2-4512-A26F-83C6219AD3F5)
- [DBMS_CLOUD_OCI_DEVOPS_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-F1EA0114-D12B-4FEE-BD5C-7B8637F437A0)
- [DBMS_CLOUD_OCI_DEVOPS_WORK_REQUEST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-5D3D34CD-EFFB-4006-8282-7AE218FA23DC)
- [DBMS_CLOUD_OCI_DEVOPS_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-81D9B43D-5219-471A-9279-BBB7E0459F1B)
- [DBMS_CLOUD_OCI_DEVOPS_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-D337CA51-CE0F-4753-BBAF-38EB2F3DAA4B)
- [DBMS_CLOUD_OCI_DEVOPS_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-E03203C0-B3C6-48BB-A5A9-DC6CB7C2122A)
- [DBMS_CLOUD_OCI_DEVOPS_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-ED11A1BF-C674-413B-A260-E4597F4CAF17)
- [DBMS_CLOUD_OCI_DEVOPS_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-1A84BDB0-2DE4-4295-8A8E-B4F0D2621B84)
- [DBMS_CLOUD_OCI_DEVOPS_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/devops_t.html#ADSDK-GUID-D3ACE2F3-3528-4BF5-8E12-47870A6191B1)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
