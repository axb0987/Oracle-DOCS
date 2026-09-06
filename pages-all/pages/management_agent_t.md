# Management Agent Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html
- Fetched: 2026-09-05 19:17 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#dcoc-content-body)

## Management Agent Common Types

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_AUTO_UPGRADABLE_CONFIG_T Type

The tenancy-level agent AutoUpgradable configuration.

Syntax
```

```

Fields

Field Description

`is_agent_auto_upgradable`

(required) true if the agents can be upgraded automatically; false if they must be upgraded manually.

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_AVAILABILITY_HISTORY_SUMMARY_T Type

Availability history of Management Agent.

Syntax
```

```

Fields

Field Description

`management_agent_id`

(required) agent identifier

`availability_status`

(required) The availability status of managementAgent

Allowed values are: 'ACTIVE', 'SILENT', 'NOT_AVAILABLE'

`time_availability_status_started`

(optional) The time at which the Management Agent moved to the availability status. An RFC3339 formatted datetime string

`time_availability_status_ended`

(optional) The time till which the Management Agent was known to be in the availability status. An RFC3339 formatted datetime string

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_CREATE_MANAGEMENT_AGENT_INSTALL_KEY_DETAILS_T Type

The information about new Management Agent install Key.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Management Agent install Key Name

`allowed_key_install_count`

(optional) Total number of install for this keys

`time_expires`

(optional) date after which key would expire after creation

`compartment_id`

(required) Compartment Identifier

`is_unlimited`

(optional) If set to true, the install key has no expiration date or usage limit. Defaults to false

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_DEPLOY_PLUGINS_DETAILS_T Type

The information required to deploy new Management Agent Plugins.

Syntax
```

```

Fields

Field Description

`plugin_ids`

(required) Plugin Id

`agent_compartment_id`

(required) Management Agent Compartment Identifier

`agent_ids`

(required) List of Agent identifiers

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_PLUGIN_DETAILS_T Type

The information about the current management agent plugins that agent is having.

Syntax
```

```

Fields

Field Description

`plugin_id`

(optional) Plugin Id

`plugin_name`

(required) Management Agent Plugin Name

`plugin_display_name`

(optional) Management Agent Plugin Identifier, can be renamed

`plugin_version`

(optional) Plugin Version

`plugin_status`

(optional) Plugin Status

Allowed values are: 'RUNNING', 'STOPPED', 'INVALID', 'FAILED'

`plugin_status_message`

(optional) Status message of the Plugin

`is_enabled`

(optional) flag indicating whether the plugin is in enabled mode or disabled mode.

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_PROPERTY_T Type

Property item in name/value pair, with optional unit type.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the property

`l_values`

(required) Values of the property

`units`

(optional) Unit for the property

Allowed values are: 'PERCENTAGE', 'MB'

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_PLUGIN_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_management_agent_management_agent_plugin_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_PROPERTY_TBL Type

Nested table type of dbms_cloud_oci_management_agent_management_agent_property_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_T Type

The details of the Management Agent inventory including the associated plugins.

Syntax
```

```

Fields

Field Description

`id`

(required) agent identifier

`install_key_id`

(optional) agent install key identifier

`display_name`

(optional) Management Agent Name

`platform_type`

(optional) Platform Type

Allowed values are: 'LINUX', 'WINDOWS', 'SOLARIS', 'MACOSX'

`platform_name`

(optional) Platform Name

`platform_version`

(optional) Platform Version

`version`

(required) Management Agent Version

`resource_artifact_version`

(optional) Version of the deployment artifact instantiated by this Management Agent. The format for Standalone resourceMode is YYMMDD.HHMM, and the format for other modes (whose artifacts are based upon Standalone but can advance independently) is YYMMDD.HHMM.VVVVVVVVVVVV. VVVVVVVVVVVV is always a numeric value between 000000000000 and 999999999999

`host`

(optional) Management Agent host machine name

`host_id`

(optional) Host resource ocid

`install_path`

(optional) Path where Management Agent is installed

`plugin_list`

(optional) list of managementAgentPlugins associated with the agent

`compartment_id`

(required) Compartment Identifier

`is_agent_auto_upgradable`

(optional) true if the agent can be upgraded automatically; false if it must be upgraded manually. This flag is derived from the tenancy level auto upgrade preference.

`time_created`

(optional) The time the Management Agent was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the Management Agent was updated. An RFC3339 formatted datetime string

`time_last_heartbeat`

(optional) The time the Management Agent has last recorded its health status in telemetry. This value will be null if the agent has not recorded its health status in last 7 days. An RFC3339 formatted datetime string

`availability_status`

(optional) The current availability status of managementAgent

Allowed values are: 'ACTIVE', 'SILENT', 'NOT_AVAILABLE'

`lifecycle_state`

(optional) The current state of managementAgent

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'TERMINATED', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`is_customer_deployed`

(optional) true, if the agent image is manually downloaded and installed. false, if the agent is deployed as a plugin in Oracle Cloud Agent.

`install_type`

(optional) The install type, either AGENT or GATEWAY

Allowed values are: 'AGENT', 'GATEWAY'

`management_agent_properties`

(optional) Additional properties for this Management Agent

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_AGGREGATION_DIMENSIONS_T Type

The Aggregation of Management Agent Dimensions

Syntax
```

```

Fields

Field Description

`availability_status`

(optional) The availability status of managementAgent

Allowed values are: 'ACTIVE', 'SILENT', 'NOT_AVAILABLE'

`platform_type`

(optional) Platform Type

Allowed values are: 'LINUX', 'WINDOWS', 'SOLARIS', 'MACOSX'

`version`

(optional) Agent image version

`has_plugins`

(optional) Whether or not a managementAgent has at least one plugin

`install_type`

(optional) The install type, either AGENT or GATEWAY

Allowed values are: 'AGENT', 'GATEWAY'

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_AGGREGATION_T Type

A count of Management Agents sharing the values for specified dimensions.

Syntax
```

```

Fields

Field Description

`dimensions`

(optional)

`l_count`

(optional) The number of Management Agents in this group

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_management_agent_management_agent_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_AGGREGATION_COLLECTION_T Type

The summary of Management Agent count items

Syntax
```

```

Fields

Field Description

`items`

(required) List in which each item describes an aggregation of Managment Agents

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_ERROR_T Type

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

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_OBJECT_DETAILS_T Type

Details of the Objectstorage object

Syntax
```

```

Fields

Field Description

`object_namespace`

(required) Objectstorage namespace reference providing the original location of this object

`object_bucket`

(required) Objectstorage bucket reference providing the original location of this object

`object_name`

(required) Objectstorage object name reference providing the original location of this object

`object_url`

(optional) Object storage URL for download

`checksum`

(optional) Object content SHA256 Hash

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_IMAGE_T Type

Supported Agent downloads

Syntax
```

```

Fields

Field Description

`id`

(required) Agent image resource id

`platform_type`

(required) Agent image platform type

Allowed values are: 'LINUX', 'WINDOWS', 'SOLARIS', 'MACOSX'

`platform_name`

(optional) Agent image platform display name

`package_type`

(optional) The installation package type

Allowed values are: 'RPM', 'ZIP'

`package_architecture_type`

(optional) The installation package target architecture type

Allowed values are: 'X86_64', 'SPARC', 'X86', 'M1'

`version`

(required) Agent image version

`l_size`

(optional) Agent image size in bytes

`checksum`

(optional) Agent image content SHA256 Hash

`object_url`

(optional) Object storage URL for download

`image_object_storage_details`

(optional)

`lifecycle_state`

(optional) The current state of Management Agent Image

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'TERMINATED', 'DELETING', 'DELETED', 'FAILED'

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_IMAGE_SUMMARY_T Type

Supported Agent downloads

Syntax
```

```

Fields

Field Description

`id`

(required) Agent image resource id

`platform_type`

(required) Agent image platform type

Allowed values are: 'LINUX', 'WINDOWS', 'SOLARIS', 'MACOSX'

`platform_name`

(optional) Agent image platform display name

`package_type`

(optional) The installation package type

Allowed values are: 'RPM', 'ZIP'

`package_architecture_type`

(optional) The installation package target architecture type

Allowed values are: 'X86_64', 'SPARC', 'X86', 'M1'

`version`

(required) Agent image version

`l_size`

(optional) Agent image size in bytes

`checksum`

(optional) Agent image content SHA256 Hash

`object_url`

(optional) Object storage URL for download

`image_object_storage_details`

(optional)

`lifecycle_state`

(optional) The current state of Management Agent Image

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'TERMINATED', 'DELETING', 'DELETED', 'FAILED'

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_INSTALL_KEY_T Type

The details of the Agent install Key

Syntax
```

```

Fields

Field Description

`id`

(required) Agent install Key identifier

`display_name`

(optional) Management Agent Install Key Name

`key`

(optional) Management Agent Install Key

`created_by_principal_id`

(optional) Principal id of user who created the Agent Install key

`compartment_id`

(required) Compartment Identifier

`allowed_key_install_count`

(optional) Total number of install for this keys

`current_key_install_count`

(optional) Total number of install for this keys

`lifecycle_state`

(optional) Status of Key

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'TERMINATED', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`time_expires`

(optional) date after which key would expire after creation

`time_created`

(optional) The time when Management Agent install Key was created. An RFC3339 formatted date time string

`time_updated`

(optional) The time when Management Agent install Key was updated. An RFC3339 formatted date time string

`is_unlimited`

(optional) If set to true, the install key has no expiration date or usage limit. Defaults to false

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_INSTALL_KEY_SUMMARY_T Type

The summary of the Agent Install Key details.

Syntax
```

```

Fields

Field Description

`id`

(required) Agent Install Key identifier

`display_name`

(optional) Management Agent Install Key Name

`created_by_principal_id`

(optional) Principal id of user who created the Agent Install key

`allowed_key_install_count`

(optional) Total number of install for this keys

`current_key_install_count`

(optional) Total number of install for this keys

`lifecycle_state`

(optional) Status of Key

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'TERMINATED', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`time_created`

(optional) The time when Management Agent install Key was created. An RFC3339 formatted date time string

`time_expires`

(optional) date after which key would expire after creation

`compartment_id`

(required) Compartment Identifier

`is_unlimited`

(optional) If set to true, the install key has no expiration date or usage limit. Properties allowedKeyInstallCount and timeExpires are ignored if set to true. Defaults to false.

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_PLUGIN_T Type

Summary of the ManagementAgentPlugin.

Syntax
```

```

Fields

Field Description

`id`

(required) Management Agent Plugin Id

`name`

(required) Management Agent Plugin Name

`version`

(optional) Management Agent Plugin Version

`supported_platform_types`

(optional) Supported Platform Types

Allowed values are: 'LINUX', 'WINDOWS', 'SOLARIS', 'MACOSX'

`display_name`

(optional) Management Agent Plugin Display Name

`description`

(optional) Management Agent Plugin description

`is_console_deployable`

(optional) A flag to indicate whether a given plugin can be deployed from Agent Console UI or not.

`lifecycle_state`

(required) The current state of Management Agent Plugin

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'TERMINATED', 'DELETING', 'DELETED', 'FAILED'

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_PLUGIN_AGGREGATION_DIMENSIONS_T Type

The Aggregation of Management Agent Plugin Dimensions

Syntax
```

```

Fields

Field Description

`plugin_name`

(optional) Management Agent Plugin Name

`plugin_display_name`

(optional) Management Agent Plugin Display Name

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_PLUGIN_AGGREGATION_T Type

A count of Management Agents Plugins sharing the values for specified dimensions.

Syntax
```

```

Fields

Field Description

`dimensions`

(optional)

`l_count`

(optional) The number of Management Agent Plugins in this group

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_PLUGIN_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_management_agent_management_agent_plugin_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_PLUGIN_AGGREGATION_COLLECTION_T Type

The summary of Management Agent Plugin count items

Syntax
```

```

Fields

Field Description

`items`

(required) List in which each item describes an aggregation of Managment Agent Plugins

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_PLUGIN_SUMMARY_T Type

Summary of the ManagementAgentPlugin.

Syntax
```

```

Fields

Field Description

`id`

(required) Management Agent Plugin Id

`name`

(required) Management Agent Plugin Name

`version`

(optional) Management Agent Plugin Version

`supported_platform_types`

(optional) Supported Platform Types

Allowed values are: 'LINUX', 'WINDOWS', 'SOLARIS', 'MACOSX'

`display_name`

(optional) Management Agent Plugin Display Name

`description`

(optional) Management Agent Plugin description

`is_console_deployable`

(optional) A flag to indicate whether a given plugin can be deployed from Agent Console UI or not.

`lifecycle_state`

(required) The current state of Management Agent Plugin

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'TERMINATED', 'DELETING', 'DELETED', 'FAILED'

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_SUMMARY_T Type

The summary of the Management Agent inventory including the associated plugins.

Syntax
```

```

Fields

Field Description

`id`

(required) agent identifier

`install_key_id`

(optional) agent install key identifier

`display_name`

(optional) Management Agent Name

`platform_type`

(optional) Platform Type

Allowed values are: 'LINUX', 'WINDOWS', 'SOLARIS', 'MACOSX'

`platform_name`

(optional) Platform Name

`platform_version`

(optional) Platform Version

`version`

(required) Management Agent Version

`resource_artifact_version`

(optional) Version of the deployment artifact instantiated by this Management Agent. The format for Standalone resourceMode is YYMMDD.HHMM, and the format for other modes (whose artifacts are based upon Standalone but can advance independently) is YYMMDD.HHMM.VVVVVVVVVVVV. VVVVVVVVVVVV is always a numeric value between 000000000000 and 999999999999

`is_agent_auto_upgradable`

(optional) true if the agent can be upgraded automatically; false if it must be upgraded manually. This flag is derived from the tenancy level auto upgrade preference.

`time_created`

(optional) The time the Management Agent was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the Management Agent was last updated. An RFC3339 formatted datetime string

`host`

(optional) Management Agent host machine name

`host_id`

(optional) Host resource ocid

`plugin_list`

(optional) list of managementAgentPlugins associated with the agent

`compartment_id`

(required) Compartment Identifier

`time_last_heartbeat`

(optional) The time the Management Agent has last recorded its heartbeat. An RFC3339 formatted datetime string

`availability_status`

(optional) The current availability status of managementAgent

Allowed values are: 'ACTIVE', 'SILENT', 'NOT_AVAILABLE'

`lifecycle_state`

(optional) The current state of managementAgent

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'TERMINATED', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`is_customer_deployed`

(optional) true, if the agent image is manually downloaded and installed. false, if the agent is deployed as a plugin in Oracle Cloud Agent.

`install_type`

(optional) The install type, either AGENT or GATEWAY

Allowed values are: 'AGENT', 'GATEWAY'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_SET_AUTO_UPGRADABLE_CONFIG_DETAILS_T Type

Details for configuring tenancy-level agent AutoUpgradable configuration.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) Tenancy identifier i.e, Root compartment identifier

`is_agent_auto_upgradable`

(required) true if the agents can be upgraded automatically; false if they must be upgraded manually.

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_UPDATE_MANAGEMENT_AGENT_DETAILS_T Type

Details required to update console-managed properties of the Management Agent.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) New displayName of Agent.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_UPDATE_MANAGEMENT_AGENT_INSTALL_KEY_DETAILS_T Type

Details required to change Management Agent install key.

Syntax
```

```

Fields

Field Description

`is_key_active`

(optional) if set to true the install key state would be set to Active and if false to Inactive

`display_name`

(optional) New displayName of Agent install key.

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_WORK_REQUEST_RESOURCE_T Type

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

`source_id`

(optional) The identifier of the source the work request is requesting.

`source_name`

(optional) The name of the source the work request is requesting.

`source_version`

(optional) The version of the source the work request is requesting.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata

`time_accepted`

(optional) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 5.6.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 5.6.

`time_finished`

(optional) The date and time the request was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 5.6.

`metadata`

(optional) Additional metadata about the resource that has been operated upon by this work request. For WorkRequests operationType WORK_DELIVERY the metadata will contain: workDeliveryStatus indicating the status of the work delivery item as a WorkDeliveryStatus value, workSubmissionKey the WorkSubmission request id, and workSubmissionDetails containing any details of result

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_management_agent_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_WORK_REQUEST_T Type

A description of workrequest status

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'DEPLOY_PLUGIN', 'UPGRADE_PLUGIN', 'CREATE_UPGRADE_PLUGINS', 'AGENTIMAGE_UPGRADE'

`status`

(required) Status of current work request.

Allowed values are: 'CREATED', 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The id of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 5.6.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 5.6.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_WORK_REQUEST_ERROR_T Type

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

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_WORK_REQUEST_LOG_ENTRY_T Type

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

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_WORK_REQUEST_SUMMARY_T Type

A description of workrequest status

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'DEPLOY_PLUGIN', 'UPGRADE_PLUGIN', 'CREATE_UPGRADE_PLUGINS', 'AGENTIMAGE_UPGRADE'

`status`

(required) Status of current work request.

Allowed values are: 'CREATED', 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The id of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

`resources`

(optional) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 5.6.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 5.6.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_MANAGEMENT_AGENT_WORK_SUBMISSION_KEY_T Type

Work Submission Identifier

Syntax
```

```

Fields

Field Description

`work_submission_key`

(required) Work Submission Identifier

- [Management Agent Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-94FDF290-BEF8-4472-AAA8-72E8BEB8516C)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-3B01AD82-218F-4038-8298-AA633421C342)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_AUTO_UPGRADABLE_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-07DE2F75-A115-4408-8718-2489E57CE160)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_AVAILABILITY_HISTORY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-ADA0DE6C-192C-407D-B7B4-8F1D56090BCA)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_CREATE_MANAGEMENT_AGENT_INSTALL_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-A12B8331-9776-4C3F-B384-EBF7652FEC38)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_DEPLOY_PLUGINS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-C034D827-C664-4188-8BB2-C79963937835)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_PLUGIN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-FBAC1CB2-D889-4AEC-A6FB-8B80ABD8B582)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_PROPERTY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-6E40D323-CE37-4DD8-B9B2-48716FF37317)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_PLUGIN_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-B86CCD49-E989-4A2A-B2DE-F77937FCBD42)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_PROPERTY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-FE82C137-8279-40BE-84B3-529840745392)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-215D3A64-9D8D-49E1-9AFF-6662ABC342F7)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_AGGREGATION_DIMENSIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-5A78D076-DDCB-4581-9569-6E6FB3E2CBD9)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-247998DF-6D6C-4924-B55C-11458D942C0E)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-E3671303-B921-4D09-B0CB-0376C23E42AD)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-771C15D0-4E8F-468E-A35D-1CC097B00E22)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-CB7D5791-AB83-4D9F-BB84-F06CD8FA6C5A)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_OBJECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-3662459D-A193-4244-B4C4-84ED1C5C16AD)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_IMAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-BC5B49C0-EB2F-4085-831B-5177D2693643)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_IMAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-EDD663A2-F44C-4FCA-810B-38CAF3D3EEDB)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_INSTALL_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-625A4216-558D-4E87-87B1-25D4662F593F)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_INSTALL_KEY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-88F2B355-8C45-4AAC-B477-661286911D99)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_PLUGIN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-B63CD2BA-1839-40EE-BB65-43BD56AA3C01)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_PLUGIN_AGGREGATION_DIMENSIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-58ACA71A-C04F-47C5-BE80-BBAD0DE22B37)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_PLUGIN_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-98F0B84E-4DDC-48F5-80A2-BA6C394CDEA9)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_PLUGIN_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-B370E4B1-8CA9-43C8-81D6-7426286B329A)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_PLUGIN_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-11B2839E-90EC-419C-8FA1-459143BBC4AF)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_PLUGIN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-164FD77E-460D-47D6-ABD2-B06E93635E1B)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_MANAGEMENT_AGENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-72690F86-5E2D-40AF-B7BE-8CB5CB14E7B1)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_SET_AUTO_UPGRADABLE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-1822FFF2-2A84-45AE-AEDC-0DFE6471DACB)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_UPDATE_MANAGEMENT_AGENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-B682B2BA-BEF2-497C-971E-957F3601B740)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_UPDATE_MANAGEMENT_AGENT_INSTALL_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-A91A4FE7-BF7A-465B-9379-0D269CF258B9)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-175540A2-9660-49DC-8705-3A84E41A8370)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-2F7F3950-9C63-496F-BC9B-E8498F137815)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-EB6736AD-C67B-4379-8C10-AEFC9CA9B3CF)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-E7CD8F02-90AE-4E33-B086-5ADB93C255AB)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-F9DF4A14-5A39-4B57-98E8-6FBFBC2BC447)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-20A4147C-0768-454E-8436-03B44D7EB31A)
- [DBMS_CLOUD_OCI_MANAGEMENT_AGENT_WORK_SUBMISSION_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_agent_t.html#ADSDK-GUID-68576B7B-890A-44C4-922A-CC9C72DACA45)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
