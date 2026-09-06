# Cloud Bridge Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html
- Fetched: 2026-09-05 19:02 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#dcoc-content-body)

## Cloud Bridge Common Types

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_ADD_AGENT_DEPENDENCY_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`agent_dependency_id`

(required) The OCID of the agentDependency, which is added to the source environment.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_PLUGIN_SUMMARY_T Type

Summary of the plugin in an Agent.

Syntax
```

```

Fields

Field Description

`name`

(required) Plugin identifier, which can be renamed.

`agent_id`

(required) Agent identifier.

`plugin_version`

(required) Plugin version.

`time_created`

(required) The time when the plugin was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time when the plugin was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the plugin.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(required) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_PLUGIN_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_bridge_plugin_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_AGENT_T Type

Description of Agent.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(required) Agent identifier, can be renamed.

`compartment_id`

(required) Compartment identifier.

`agent_type`

(required) Type of the Agent.

Allowed values are: 'APPLIANCE'

`agent_version`

(required) Agent identifier.

`os_version`

(required) OS version.

`time_created`

(required) The time when the Agent was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time when the Agent was updated. An RFC3339 formatted datetime string.

`time_last_sync_received`

(optional) The time when the last heartbeat of the Agent was noted. An RFC3339 formatted datetime string.

`heart_beat_status`

(optional) The current heartbeat status of the Agent based on its timeLastSyncReceived value.

Allowed values are: 'HEALTHY', 'UNHEALTHY', 'FAILED', 'INACTIVE'

`environment_id`

(required) Environment identifier.

`agent_pub_key`

(optional) Resource principal public key.

`time_expire_agent_key_in_ms`

(optional) The time since epoch for when the public key will expire. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the Agent.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state of the Agent in more detail. For example, it can be used to provide actionable information for a resource in Failed state.

`plugin_list`

(optional) List of plugins associated with the agent.

`freeform_tags`

(required) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_AGENT_SUMMARY_T Type

Summary of the Agent.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(required) Agent identifier, which can be renamed.

`compartment_id`

(required) Compartment identifier.

`agent_type`

(required) Type of Agent.

`agent_version`

(required) Agent identifier.

`os_version`

(required) OS version.

`time_created`

(required) The time when the Agent was created. An RFC3339 formatted datetime string.

`time_updated`

(required) The time when the Agent was updated. An RFC3339 formatted datetime string.

`time_last_sync_received`

(optional) The time when the last heartbeat of the Agent was noted. An RFC3339 formatted datetime string.

`heart_beat_status`

(optional) Current heartbeat status of the Agent based on its timeLastSyncReceived value.

`environment_id`

(required) Environment identifier.

`lifecycle_state`

(required) The current state of the Agent.

`lifecycle_details`

(required) A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(required) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_AGENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_bridge_agent_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_AGENT_COLLECTION_T Type

Displays results of an Agent search. Contains both AgentSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of Agents.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_AGENT_DEPENDENCY_T Type

Description of the AgentDependency, which is a sub-resource of the external environment.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(required) Display name of the Agent dependency.

`compartment_id`

(required) Compartment identifier

`dependency_name`

(required) Name of the dependency type. This should match the whitelisted enum of dependency names.

`dependency_version`

(optional) Version of the Agent dependency.

`description`

(optional) Description about the Agent dependency.

`namespace`

(required) Object storage namespace associated with the customer's tenancy.

`bucket`

(required) Object storage bucket where the Agent dependency is uploaded.

`object_name`

(required) Name of the dependency object uploaded by the customer.

`time_created`

(optional) The time when the AgentDependency was created. An RFC3339 formatted datetime string.

`e_tag`

(optional) The eTag associated with the dependency object returned by Object Storage.

`checksum`

(optional) The checksum associated with the dependency object returned by Object Storage.

`lifecycle_state`

(optional) The current state of AgentDependency.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_AGENT_DEPENDENCY_SUMMARY_T Type

Description of the AgentDependency, which is a sub-resource of the external environment.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(required) Display name of the Agent dependency.

`compartment_id`

(required) Compartment identifier.

`dependency_name`

(required) Name of the dependency type. This should match the whitelisted enum of dependency names.

`dependency_version`

(optional) Version of the Agent dependency.

`description`

(optional) Description about the Agent dependency.

`namespace`

(required) Object storage namespace associated with the customer's tenancy.

`bucket`

(required) Object storage bucket where the Agent dependency is uploaded.

`object_name`

(required) Name of the dependency object uploaded by the customer.

`time_created`

(optional) The time when the AgentDependency was created. An RFC3339 formatted datetime string.

`e_tag`

(optional) The eTag associated with the dependency object returned by Object Storage.

`checksum`

(optional) The checksum associated with the dependency object returned by Object Storage.

`lifecycle_state`

(optional) The current state of the external environment.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_AGENT_DEPENDENCY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_bridge_agent_dependency_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_AGENT_DEPENDENCY_COLLECTION_T Type

Results of an AgentDependency list. Contains both AgentDependency items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of EnvironmentDependencies.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_APPLIANCE_IMAGE_SUMMARY_T Type

Description of the ApplianceImage.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`file_name`

(required) The name of the appliance Image file.

`display_name`

(required) The name of the image to be displayed.

`version`

(required) The version of the image file.

`size_in_m_bs`

(required) The size of the image file in megabytes.

`checksum`

(required) The checksum of the image file.

`platform`

(required) The virtualization platform that the image file supports.

`format`

(required) The file format of the image file.

`time_created`

(required) The time when the appliance image was created.An RFC3339 formatted datetime string.

`time_updated`

(required) The time when the appliance image was last updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the appliance image.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`download_url`

(required) The URL from which the appliance image can be downloaded.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_APPLIANCE_IMAGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_bridge_appliance_image_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_APPLIANCE_IMAGE_COLLECTION_T Type

Results of an ApplianceImage search.

Syntax
```

```

Fields

Field Description

`items`

(required) List of appliance images.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_T Type

Description of an asset.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Asset display name.

`inventory_id`

(required) Inventory ID to which an asset belongs to.

`id`

(required) Asset OCID that is immutable on creation.

`compartment_id`

(required) The OCID of the compartment to which an asset belongs to.

`source_key`

(required) The source key that the asset belongs to.

`external_asset_key`

(required) The key of the asset from the external environment.

`asset_type`

(required) The type of asset.

Allowed values are: 'VMWARE_VM', 'VM'

`time_created`

(required) The time when the asset was created. An RFC3339 formatted datetime string.

`time_updated`

(required) The time when the asset was updated. An RFC3339 formatted datetime string.

`asset_source_ids`

(optional) List of asset source OCID.

`lifecycle_state`

(required) The current state of the asset.

Allowed values are: 'ACTIVE', 'DELETED'

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_AGGREGATION_T Type

The result of an analytics aggregation on a set of assets.

Syntax
```

```

Fields

Field Description

`dimensions`

(optional) The dimensions along which assets can be aggregated for analytics.

`l_count`

(optional) Returns the total number of observations from the group of assets.

`l_max`

(optional) Returns the highest value from all the assets.

`mean`

(optional) Returns the value of sum divided by count from the group of assets.

`l_min`

(optional) Returns the lowest value from the group of assets.

`l_sum`

(optional) Returns all values added together from the group of assets.

`aggregated_property`

(required) Aggregated property.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_cloud_bridge_asset_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_AGGREGATION_COLLECTION_T Type

The result of an analytics aggregation on a set of assets.

Syntax
```

```

Fields

Field Description

`items`

(required) List of asset aggregations.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_SUMMARY_T Type

Summary of the asset.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Asset display name.

`inventory_id`

(required) Inventory ID that the asset belongs to.

`id`

(required) Asset OCID that is immutable on creation.

`compartment_id`

(required) The OCID of the compartment that the asset belongs to.

`source_key`

(required) The source key to which the asset belongs.

`external_asset_key`

(required) The key of the asset from the external environment.

`asset_type`

(required) The type of asset.

Allowed values are: 'VMWARE_VM', 'VM'

`time_created`

(required) The time when the asset was created. An RFC3339 formatted datetime string.

`time_updated`

(required) The time when the asset was updated. An RFC3339 formatted datetime string.

`asset_source_ids`

(optional) List of asset source OCID.

`lifecycle_state`

(required) The current state of the asset.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_bridge_asset_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_COLLECTION_T Type

Results of a set of asset summary.

Syntax
```

```

Fields

Field Description

`items`

(required) List of assets.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_SOURCE_T Type

Asset source.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of asset source. Indicates external origin of the assets that are read by assigning this asset source.

Allowed values are: 'VMWARE'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment for the resource.

`display_name`

(required) A user-friendly name for the asset source. Does not have to be unique, and it's mutable. Avoid entering confidential information.

`environment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the environment.

`inventory_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the inventory that will contain created assets.

`assets_compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that is going to be used to create assets.

`discovery_schedule_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of an attached discovery schedule.

`lifecycle_state`

(required) The current state of the asset source.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'UPDATING', 'NEEDS_ATTENTION'

`lifecycle_details`

(required) The detailed state of the asset source.

`time_created`

(required) The time when the asset source was created in the RFC3339 format.

`time_updated`

(required) The point in time that the asset source was last updated in the RFC3339 format.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_SOURCE_SUMMARY_T Type

Summary of an asset source provided in the list.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of asset source. Indicates external origin of the assets that are read by assigning this asset source.

Allowed values are: 'VMWARE'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment for the resource.

`environment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the environment.

`display_name`

(required) A user-friendly name for the asset source. Does not have to be unique, and it's mutable. Avoid entering confidential information.

`lifecycle_state`

(required) The current state of the asset source.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'UPDATING', 'NEEDS_ATTENTION'

`lifecycle_details`

(required) The detailed state of the asset source.

`inventory_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the inventory that will contain created assets.

`assets_compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that is going to be used to create assets.

`time_created`

(optional) The time when the asset source was created in RFC3339 format.

`time_updated`

(optional) The point in time that the asset source was last updated in RFC3339 format.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_SOURCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_bridge_asset_source_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_SOURCE_COLLECTION_T Type

Results of an asset source search. Contains asset source items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of asset sources.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_SOURCE_CONNECTION_T Type

Descriptor of a connection to an asset source.

Syntax
```

```

Fields

Field Description

`connection_type`

(required) The type of connection for an asset source.

Allowed values are: 'DISCOVERY', 'REPLICATION'

`connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cloud bridge connector used for migration operations.

`asset_source_key`

(required) Type-specific identifier for an asset source.

`lifecycle_state`

(required) The current state of the connection.

Allowed values are: 'ACTIVE', 'UPDATING', 'NEEDS_ATTENTION', 'DELETED', 'CREATING'

`lifecycle_details`

(required) The detailed sub-state of the connection.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_SOURCE_CONNECTION_TBL Type

Nested table type of dbms_cloud_oci_cloud_bridge_asset_source_connection_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_SOURCE_CONNECTION_COLLECTION_T Type

List of connections for an asset source.

Syntax
```

```

Fields

Field Description

`items`

(required) List of connections.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_SOURCE_CREDENTIALS_T Type

Credentials for an asset source.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Authentication type

Allowed values are: 'BASIC'

`secret_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret in a vault. If the the type of the credentials is BASIC`, the secret must contain the username and password in JSON format, which is in the form of `{ \"username\": \"&lt;VMwareUser&gt;\", \"password\": \"&lt;VMwarePassword&gt;\" }`.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_CHANGE_AGENT_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_CHANGE_AGENT_DEPENDENCY_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_CHANGE_ASSET_COMPARTMENT_DETAILS_T Type

The information to be updated for changing asset compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_CHANGE_ASSET_SOURCE_COMPARTMENT_DETAILS_T Type

Details for which compartment to move the resource to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_CHANGE_ASSET_TAGS_DETAILS_T Type

The information about tags to be updated.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_CHANGE_DISCOVERY_SCHEDULE_COMPARTMENT_DETAILS_T Type

Information about the compartment into which the discovery schedule should be moved.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the discovery schedule should be moved.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_CHANGE_ENVIRONMENT_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_GPU_DEVICE_T Type

GPU device details.

Syntax
```

```

Fields

Field Description

`name`

(optional) GPU device name.

`description`

(optional) GPU device description.

`cores_count`

(optional) Number of GPU cores.

`memory_in_m_bs`

(optional) GPU memory size in MBs.

`manufacturer`

(optional) The manufacturer of GPU.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_NIC_T Type

The VNIC configuration.

Syntax
```

```

Fields

Field Description

`label`

(optional) Provides a label and summary information for the device.

`switch_name`

(optional) Switch name.

`mac_address`

(optional) Mac address of the VM.

`mac_address_type`

(optional) Mac address type.

`network_name`

(optional) Network name.

`ip_addresses`

(optional) List of IP addresses.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_DISK_T Type

The assets disk.

Syntax
```

```

Fields

Field Description

`name`

(optional) Disk name.

`boot_order`

(optional) Order of boot volumes.

`uuid`

(optional) Disk UUID for the virtual disk, if available.

`uuid_lun`

(optional) Disk UUID LUN for the virtual disk, if available.

`size_in_m_bs`

(optional) The size of the volume in MBs.

`location`

(optional) Location of the boot/data volume.

`persistent_mode`

(optional) The disk persistent mode.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_NVDIMM_T Type

The asset's NVDIMM configuration.

Syntax
```

```

Fields

Field Description

`label`

(optional) Provides a label and summary information for the device.

`unit_number`

(optional) The unit number of NVDIMM.

`controller_key`

(optional) Controller key.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_NVDIMM_CONTROLLER_T Type

The asset's NVDIMM configuration.

Syntax
```

```

Fields

Field Description

`label`

(optional) Provides a label and summary information for the device.

`bus_number`

(optional) Bus number.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_SCSI_CONTROLLER_T Type

The assets SCSI controller.

Syntax
```

```

Fields

Field Description

`label`

(optional) Provides a label and summary information for the device.

`unit_number`

(optional) The unit number of the SCSI controller.

`shared_bus`

(optional) Shared bus.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_GPU_DEVICE_TBL Type

Nested table type of dbms_cloud_oci_cloud_bridge_gpu_device_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_NIC_TBL Type

Nested table type of dbms_cloud_oci_cloud_bridge_nic_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_DISK_TBL Type

Nested table type of dbms_cloud_oci_cloud_bridge_disk_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_NVDIMM_TBL Type

Nested table type of dbms_cloud_oci_cloud_bridge_nvdimm_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_COMPUTE_PROPERTIES_T Type

Compute related properties.

Syntax
```

```

Fields

Field Description

`primary_ip`

(optional) Primary IP address of the compute instance.

`dns_name`

(optional) Fully Qualified DNS Name.

`description`

(optional) Information about the asset.

`cores_count`

(optional) Number of CPUs.

`cpu_model`

(optional) CPU model name.

`gpu_devices_count`

(optional) Number of GPU devices.

`gpu_devices`

(optional) List of GPU devices attached to a virtual machine.

`threads_per_core_count`

(optional) Number of threads per core.

`memory_in_m_bs`

(optional) Memory size in MBs.

`is_pmem_enabled`

(optional) Whether Pmem is enabled. Decides if NVDIMMs are used as a permanent memory.

`pmem_in_m_bs`

(optional) Pmem size in MBs.

`operating_system`

(optional) Operating system.

`operating_system_version`

(optional) Operating system version.

`host_name`

(optional) Host name of the VM.

`power_state`

(optional) The current power state of the virtual machine.

`guest_state`

(optional) Guest state.

`is_tpm_enabled`

(optional) Whether Trusted Platform Module (TPM) is enabled.

`connected_networks`

(optional) Number of connected networks.

`nics_count`

(optional) Number of network ethernet cards.

`nics`

(optional) List of network ethernet cards attached to a virtual machine.

`storage_provisioned_in_m_bs`

(optional) Provision storage size in MBs.

`disks_count`

(optional) Number of disks.

`disks`

(optional) Lists the set of disks belonging to the virtual machine. This list is unordered.

`firmware`

(optional) Information about firmware type for this virtual machine.

`latency_sensitivity`

(optional) Latency sensitivity.

`nvdimms`

(optional) The properties of the NVDIMMs attached to a virtual machine.

`nvdimm_controller`

(optional)

`scsi_controller`

(optional)

`hardware_version`

(optional) Hardware version.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_CREATE_AGENT_DEPENDENCY_DETAILS_T Type

The information about new AgentDependency.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Display name of the Agent dependency.

`dependency_name`

(required) Name of the dependency type. This should match the whitelisted enum of dependency names.

`compartment_id`

(required) Compartment identifier.

`dependency_version`

(optional) Version of the Agent dependency.

`description`

(optional) Description about the Agent dependency.

`namespace`

(required) Object storage namespace associated with the customer's tenancy.

`bucket`

(required) Object storage bucket where the dependency is uploaded.

`object_name`

(required) Name of the dependency object uploaded by the customer.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_CREATE_AGENT_DETAILS_T Type

Information about the new Agent.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Agent identifier.

`agent_type`

(required) Agent identifier.

`agent_version`

(required) Agent identifier.

`compartment_id`

(required) Compartment identifier.

`environment_id`

(required) Environment identifier.

`os_version`

(required) OS version.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_CREATE_ASSET_DETAILS_T Type

The information about the new asset.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Asset display name.

`inventory_id`

(required) Inventory ID to which an asset belongs.

`compartment_id`

(required) The OCID of the compartment that the asset belongs to.

`source_key`

(required) The source key to which the asset belongs.

`external_asset_key`

(required) The key of the asset from the external environment.

`asset_type`

(required) The type of asset.

Allowed values are: 'VMWARE_VM', 'VM'

`asset_source_ids`

(optional) List of asset source OCID.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_CREATE_ASSET_SOURCE_DETAILS_T Type

Asset source creation request.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Asset source type.

Allowed values are: 'VMWARE'

`display_name`

(optional) A user-friendly name for the asset source. Does not have to be unique, and it's mutable. Avoid entering confidential information. The name is generated by the service if it is not explicitly provided.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment for the resource.

`environment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the environment.

`inventory_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the inventory that will contain created assets.

`assets_compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that is going to be used to create assets.

`discovery_schedule_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the discovery schedule that is going to be attached to the created asset.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_CREATE_DISCOVERY_SCHEDULE_DETAILS_T Type

Information about discovery schedule to be created.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the discovery schedule is created.

`execution_recurrences`

(required) Recurrence specification for the discovery schedule execution.

`display_name`

(optional) A user-friendly name for the discovery schedule. Does not have to be unique, and it's mutable. Avoid entering confidential information. The name is generated by the service if it is not explicitly provided.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_CREATE_ENVIRONMENT_DETAILS_T Type

The information about the new source environment.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Environment identifier.

`compartment_id`

(required) Compartment identifier.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_CREATE_INVENTORY_DETAILS_T Type

Description for creating inventory details.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Inventory displayName.

`compartment_id`

(required) The OCID of the tenantId.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_CREATE_VM_WARE_ASSET_SOURCE_DETAILS_T Type

Description of an asset source.

Syntax
```

```

`dbms_cloud_oci_cloud_bridge_create_vm_ware_asset_source_details_t`is a subtype of the`dbms_cloud_oci_cloud_bridge_create_asset_source_details_t`type.

Fields

Field Description

`vcenter_endpoint`

(required) Endpoint for VMware asset discovery and replication in the form of ```https://&lt;host&gt;:&lt;port&gt;/sdk```

`discovery_credentials`

(required)

`replication_credentials`

(optional)

`are_historical_metrics_collected`

(optional) Flag indicating whether historical metrics are collected for assets, originating from this asset source.

`are_realtime_metrics_collected`

(optional) Flag indicating whether real-time metrics are collected for assets, originating from this asset source.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_VM_PROPERTIES_T Type

Virtual machine related properties.

Syntax
```

```

Fields

Field Description

`hypervisor_vendor`

(optional) Hypervisor vendor.

`hypervisor_version`

(optional) Hypervisor version.

`hypervisor_host`

(optional) Host name/IP address of VM on which the host is running.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_CUSTOMER_TAG_T Type

The customer defined tags.

Syntax
```

```

Fields

Field Description

`name`

(optional) The tag name.

`description`

(optional) The tag description.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_CUSTOMER_TAG_TBL Type

Nested table type of dbms_cloud_oci_cloud_bridge_customer_tag_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_VMWARE_VM_PROPERTIES_T Type

VMware virtual machine related properties.

Syntax
```

```

Fields

Field Description

`l_cluster`

(optional) Cluster name.

`customer_fields`

(optional) Customer fields.

`customer_tags`

(optional) Customer defined tags.

`instance_uuid`

(optional) vCenter-specific identifier of the virtual machine.

`path`

(optional) Path directory of the asset.

`vmware_tools_status`

(optional) VMware tools status.

`is_disks_uuid_enabled`

(optional) Whether changed block tracking for this VM's disk is active.

`is_disks_cbt_enabled`

(optional) Indicates that change tracking is supported for virtual disks of this virtual machine. However, even if change tracking is supported, it might not be available for all disks of the virtual machine.

`fault_tolerance_state`

(optional) Fault tolerance state.

`fault_tolerance_bandwidth`

(optional) Fault tolerance bandwidth.

`fault_tolerance_secondary_latency`

(optional) Fault tolerance to secondary latency.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_VMWARE_V_CENTER_PROPERTIES_T Type

VMware vCenter related properties.

Syntax
```

```

Fields

Field Description

`vcenter_key`

(optional) vCenter unique key.

`vcenter_version`

(optional) Dot-separated version string.

`data_center`

(optional) Data center name.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_CREATE_VMWARE_VM_ASSET_DETAILS_T Type

Create VMware VM type of asset.

Syntax
```

```

`dbms_cloud_oci_cloud_bridge_create_vmware_vm_asset_details_t`is a subtype of the`dbms_cloud_oci_cloud_bridge_create_asset_details_t`type.

Fields

Field Description

`compute`

(optional)

`vm`

(optional)

`vmware_vm`

(optional)

`vmware_v_center`

(optional)

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_DISCOVERY_SCHEDULE_T Type

Discovery schedule.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the discovery schedule.

`display_name`

(required) A user-friendly name for the discovery schedule. Does not have to be unique, and it's mutable. Avoid entering confidential information.

`execution_recurrences`

(required) Recurrence specification for the discovery schedule execution.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the discovery schedule exists.

`lifecycle_state`

(required) Current state of the discovery schedule.

Allowed values are: 'ACTIVE', 'DELETED'

`lifecycle_details`

(required) The detailed state of the discovery schedule.

`time_created`

(required) The time when the discovery schedule was created in RFC3339 format.

`time_updated`

(required) The time when the discovery schedule was last updated in RFC3339 format.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_DISCOVERY_SCHEDULE_SUMMARY_T Type

Summarized information about a discovery schedule.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the discovery schedule.

`display_name`

(required) A user-friendly name for the discovery schedule. Does not have to be unique, and it's mutable. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the discovery schedule exists.

`lifecycle_state`

(required) Current state of the discovery schedule.

Allowed values are: 'ACTIVE', 'DELETED'

`lifecycle_details`

(required) The detailed state of the discovery schedule.

`time_created`

(required) The time when the discovery schedule was created in RFC3339 format.

`time_updated`

(required) The time when the discovery schedule was last updated in RFC3339 format.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_DISCOVERY_SCHEDULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_bridge_discovery_schedule_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_DISCOVERY_SCHEDULE_COLLECTION_T Type

Results of a discovery schedule search. Contains discovery schedule summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) Discovery schedule summaries.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_ENVIRONMENT_T Type

Description of the source environment.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(required) Environment identifier, which can be renamed.

`compartment_id`

(required) Compartment identifier.

`time_created`

(required) The time when the source environment was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time when the source environment was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the source environment.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(required) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_ENVIRONMENT_SUMMARY_T Type

Summary of a source environment.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(required) Environment identifier, which can be renamed.

`compartment_id`

(required) Compartment identifier.

`time_created`

(required) The time when the source environment was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time when the source environment was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the source environment.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(required) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_ENVIRONMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_bridge_environment_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_ENVIRONMENT_COLLECTION_T Type

Results of an environment search. Contains both EnvironmentSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of all source environments.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_ERROR_T Type

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

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_HISTORICAL_METRIC_T Type

Metric details.

Syntax
```

```

Fields

Field Description

`name`

(required) Metric name.

`aggregation`

(required) Aggregation time interval.

`value`

(required) Aggregation value.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_HISTORICAL_METRIC_SUMMARY_T Type

Metric details.

Syntax
```

```

Fields

Field Description

`name`

(required) Metric name.

`aggregation`

(required) Aggregation time interval.

`value`

(required) Aggregation value.

`time_created`

(optional) The time the HistoricalMetric was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the HistoricalMetric was updated. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_HISTORICAL_METRIC_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_bridge_historical_metric_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_HISTORICAL_METRIC_COLLECTION_T Type

List of historical metric.

Syntax
```

```

Fields

Field Description

`items`

(required) List of asset historical metrics.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_IMPORT_INVENTORY_DETAILS_T Type

Details for importing assets from a file.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartmentId that resources import.

`resource_type`

(optional) Import inventory resource type.

Allowed values are: 'ASSET'

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_IMPORT_INVENTORY_VIA_ASSETS_DETAILS_T Type

Details for importing assets from a file.

Syntax
```

```

`dbms_cloud_oci_cloud_bridge_import_inventory_via_assets_details_t`is a subtype of the`dbms_cloud_oci_cloud_bridge_import_inventory_details_t`type.

Fields

Field Description

`data`

(optional) The file body to be sent in the request.

`asset_type`

(optional) The type of asset.

Allowed values are: 'VMWARE_VM', 'VM'

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_INVENTORY_T Type

Description of inventory.

Syntax
```

```

Fields

Field Description

`id`

(required) Inventory OCID.

`display_name`

(required) Inventory display name.

`lifecycle_state`

(required) The current state of the inventory.

Allowed values are: 'ACTIVE', 'DELETED', 'DELETING', 'CREATING', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.

`compartment_id`

(required) The OCID of the tenantId.

`time_created`

(required) The time when the inventory was created. An RFC3339 formatted datetime string.

`time_updated`

(required) The time when the inventory was updated. An RFC3339 formatted datetime string.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_INVENTORY_SUMMARY_T Type

Description of inventory.

Syntax
```

```

Fields

Field Description

`id`

(required) Inventory OCID.

`display_name`

(optional) Inventory display name.

`lifecycle_state`

(required) The current state of the inventory.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.

`compartment_id`

(optional) The OCID of the tenantId.

`time_created`

(optional) The time when the inventory was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time when the inventory was updated. An RFC3339 formatted datetime string.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_INVENTORY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_bridge_inventory_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_INVENTORY_COLLECTION_T Type

Result of inventory summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) List of inventories.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_PLUGIN_T Type

Description of plugin

Syntax
```

```

Fields

Field Description

`name`

(required) Plugin identifier, which can be renamed.

`agent_id`

(required) Agent identifier.

`plugin_version`

(required) Plugin version.

`desired_state`

(optional) State to which the customer wants the plugin to move to.

Allowed values are: 'ENABLED', 'DISABLED'

`time_created`

(required) The time when the Agent was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time when the Agent was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the plugin.

Allowed values are: 'UPDATING', 'ACTIVE', 'INACTIVE', 'NEEDS_ATTENTION', 'DELETED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_REMOVE_AGENT_DEPENDENCY_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`agent_dependency_id`

(required) The OCID of the agentDependency that should be removed from the source environment.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_HISTORICAL_METRIC_TBL Type

Nested table type of dbms_cloud_oci_cloud_bridge_historical_metric_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_SUBMIT_HISTORICAL_METRICS_DETAILS_T Type

Post historical metric details.

Syntax
```

```

Fields

Field Description

`historical_metrics`

(required) List of asset historical metrics.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_UPDATE_AGENT_DEPENDENCY_DETAILS_T Type

The information about new AgentDependency.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Display name of the Agent dependency.

`dependency_name`

(optional) Name of the dependency type. This should match the whitelisted enum of dependency names.

`dependency_version`

(optional) Version of the Agent dependency.

`description`

(optional) Description about the Agent dependency.

`namespace`

(optional) Object storage namespace associated with the customer's tenancy.

`bucket`

(optional) Object storage bucket where the dependency is uploaded.

`object_name`

(optional) Name of the dependency object uploaded by the customer.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_UPDATE_AGENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Agent identifier.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_UPDATE_ASSET_DETAILS_T Type

The information of asset to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Asset display name.

`asset_type`

(required) Asset type

Allowed values are: 'VMWARE_VM', 'VM'

`asset_source_ids`

(optional) List of asset source OCID.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_UPDATE_ASSET_SOURCE_DETAILS_T Type

The information about the new asset source.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Source type.

Allowed values are: 'VMWARE'

`display_name`

(optional) A user-friendly name for the asset source. Does not have to be unique, and it's mutable. Avoid entering confidential information.

`assets_compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that is going to be used to create assets.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_UPDATE_DISCOVERY_SCHEDULE_DETAILS_T Type

Information about discovery schedule to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name for the discovery schedule. Does not have to be unique, and it's mutable. Avoid entering confidential information.

`execution_recurrences`

(optional) Recurrence specification for the discovery schedule execution.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_UPDATE_ENVIRONMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Environment identifier.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_UPDATE_INVENTORY_DETAILS_T Type

Description for updating inventory details.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Inventory displayName.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_UPDATE_PLUGIN_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`desired_state`

(optional) State to which the customer wants the plugin to move to.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_UPDATE_VM_ASSET_DETAILS_T Type

The information of VM asset to be updated.

Syntax
```

```

`dbms_cloud_oci_cloud_bridge_update_vm_asset_details_t`is a subtype of the`dbms_cloud_oci_cloud_bridge_update_asset_details_t`type.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_UPDATE_VM_WARE_ASSET_SOURCE_DETAILS_T Type

Asset source update details.

Syntax
```

```

`dbms_cloud_oci_cloud_bridge_update_vm_ware_asset_source_details_t`is a subtype of the`dbms_cloud_oci_cloud_bridge_update_asset_source_details_t`type.

Fields

Field Description

`vcenter_endpoint`

(optional) Endpoint for VMware asset discovery and replication in the form of ```https://&lt;host&gt;:&lt;port&gt;/sdk```

`discovery_credentials`

(optional)

`replication_credentials`

(optional)

`are_historical_metrics_collected`

(optional) Flag indicating whether historical metrics are collected for assets, originating from this asset source.

`are_realtime_metrics_collected`

(optional) Flag indicating whether real-time metrics are collected for assets, originating from this asset source.

`discovery_schedule_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the discovery schedule that is going to be assigned to an asset source.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_UPDATE_VMWARE_VM_ASSET_DETAILS_T Type

The information of VMware VM asset to be updated.

Syntax
```

```

`dbms_cloud_oci_cloud_bridge_update_vmware_vm_asset_details_t`is a subtype of the`dbms_cloud_oci_cloud_bridge_update_asset_details_t`type.

Fields

Field Description

`compute`

(optional)

`vm`

(optional)

`vmware_vm`

(optional)

`vmware_v_center`

(optional)

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_VM_ASSET_T Type

VM type of asset.

Syntax
```

```

`dbms_cloud_oci_cloud_bridge_vm_asset_t`is a subtype of the`dbms_cloud_oci_cloud_bridge_asset_t`type.

Fields

Field Description

`compute`

(optional)

`vm`

(optional)

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_VM_WARE_ASSET_SOURCE_T Type

Description of an asset source.

Syntax
```

```

`dbms_cloud_oci_cloud_bridge_vm_ware_asset_source_t`is a subtype of the`dbms_cloud_oci_cloud_bridge_asset_source_t`type.

Fields

Field Description

`vcenter_endpoint`

(required) Endpoint for VMware asset discovery and replication in the form of ```https://&lt;host&gt;:&lt;port&gt;/sdk```

`discovery_credentials`

(required)

`replication_credentials`

(optional)

`are_historical_metrics_collected`

(optional) Flag indicating whether historical metrics are collected for assets, originating from this asset source.

`are_realtime_metrics_collected`

(optional) Flag indicating whether real-time metrics are collected for assets, originating from this asset source.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_VM_WARE_ASSET_SOURCE_SUMMARY_T Type

Description of an asset source.

Syntax
```

```

`dbms_cloud_oci_cloud_bridge_vm_ware_asset_source_summary_t`is a subtype of the`dbms_cloud_oci_cloud_bridge_asset_source_summary_t`type.

Fields

Field Description

`vcenter_endpoint`

(required) Endpoint for VMware asset discovery and replication in the form of ```https://&lt;host&gt;:&lt;port&gt;/sdk```

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_VMWARE_VM_ASSET_T Type

VMware VM type of asset.

Syntax
```

```

`dbms_cloud_oci_cloud_bridge_vmware_vm_asset_t`is a subtype of the`dbms_cloud_oci_cloud_bridge_asset_t`type.

Fields

Field Description

`compute`

(optional)

`vm`

(optional)

`vmware_vm`

(optional)

`vmware_v_center`

(optional)

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_WORK_REQUEST_RESOURCE_T Type

A resource that a work request creates and operates on.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type that the work request affects.

`action_type`

(required) The way in which this resource is affected by the work is tracked in the work request. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource. At that point, the resource will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED', 'FAILED'

`identifier`

(required) The identifier of the resource that the work request affects.

`entity_uri`

(optional) The URI path where you can perform a GET operation to access the resource metadata.

`metadata`

(optional) Additional information that helps to explain the resource.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_cloud_bridge_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_WORK_REQUEST_T Type

A description of work request status.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of work request.

Allowed values are: 'CREATE_ENVIRONMENT', 'UPDATE_ENVIRONMENT', 'DELETE_ENVIRONMENT', 'MOVE_ENVIRONMENT', 'CREATE_OCB_AGENT', 'UPDATE_OCB_AGENT', 'DELETE_OCB_AGENT', 'MOVE_OCB_AGENT', 'CREATE_AGENT_DEPENDENCY', 'UPDATE_AGENT_DEPENDENCY', 'DELETE_AGENT_DEPENDENCY', 'MOVE_AGENT_DEPENDENCY', 'CREATE_INVENTORY', 'DELETE_INVENTORY', 'IMPORT_INVENTORY', 'DELETE_ASSET_SOURCE', 'REFRESH_ASSET_SOURCE', 'CREATE_ASSET_SOURCE', 'UPDATE_ASSET_SOURCE'

`status`

(required) Status of the current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The OCID of the work request.

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource that the work request affects. If the work request affects multiple resources, and these resources are not in the same compartment, the service team can choose the primary resource whose compartment should be used.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of request completed.

`time_accepted`

(required) The date and time when the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time when the request started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time when the object was complete, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occurred. Error codes are listed at, https://docs.cloud.oracle.com/Content/API/References/apierrors.htm

`message`

(required) A human-readable description of the issue encountered.

`l_timestamp`

(required) The time when the error occurred. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_cloud_bridge_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestError objects.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time when the log message was written. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_cloud_bridge_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a workRequestLog search. Contains both workRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestLogEntries.

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of work request.

Allowed values are: 'CREATE_ENVIRONMENT', 'UPDATE_ENVIRONMENT', 'DELETE_ENVIRONMENT', 'MOVE_ENVIRONMENT', 'CREATE_OCB_AGENT', 'UPDATE_OCB_AGENT', 'DELETE_OCB_AGENT', 'MOVE_OCB_AGENT', 'CREATE_AGENT_DEPENDENCY', 'UPDATE_AGENT_DEPENDENCY', 'DELETE_AGENT_DEPENDENCY', 'MOVE_AGENT_DEPENDENCY', 'CREATE_INVENTORY', 'DELETE_INVENTORY', 'IMPORT_INVENTORY', 'DELETE_ASSET_SOURCE', 'REFRESH_ASSET_SOURCE', 'CREATE_ASSET_SOURCE', 'UPDATE_ASSET_SOURCE'

`status`

(required) Status of the current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The OCID of the work request.

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and these resources are not in the same compartment, the service team can choose the primary resource whose compartment should be used.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time when the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time when the request started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time when the object was complete, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_bridge_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_BRIDGE_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestSummary objects.

- [Cloud Bridge Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-5B859B1E-14C1-40C7-B5B4-6D456942F5DC)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-EB88C783-42B9-4B7D-9443-A802BC1FE63F)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_ADD_AGENT_DEPENDENCY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-73850380-895C-4705-B155-76C5A6565D3F)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_PLUGIN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-7FA546F2-8D6E-458A-B060-58416A73950B)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_PLUGIN_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-B0636378-C1DC-400C-AE94-D56FB18E5B66)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_AGENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-68FA696F-3B7B-467F-B26F-F3D024371EBB)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_AGENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-AB74B96C-FA8E-45A6-8DE5-CC5192FA3EC6)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_AGENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-F477FBDB-3B7B-451E-A8A1-E3FBE120C3F9)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_AGENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-26DDFE0D-A139-4A12-AD58-9A06799ABC89)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_AGENT_DEPENDENCY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-457FF3B4-A9D8-46BD-8227-B0B29D896631)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_AGENT_DEPENDENCY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-5584BC3A-22F6-4DFD-BA81-28C2BEC40BFB)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_AGENT_DEPENDENCY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-385A6626-2153-4F77-B4BB-90434AC8FD77)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_AGENT_DEPENDENCY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-0BA8727B-F79E-483D-8C26-C26C97873B4B)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_APPLIANCE_IMAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-7D33D5D7-5F7D-4468-B30D-CBAAAC936F40)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_APPLIANCE_IMAGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-2A736452-0B91-45CF-BCF5-744C9F89807A)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_APPLIANCE_IMAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-05C2A1D8-95A4-4315-8122-A733F7FA9B71)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-9D3BE855-A33E-4C3D-B7EF-ADFCBA08B2E2)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-84CB3844-970F-42D6-B5AB-ABE656343133)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-1E79D0A4-A777-4E88-9967-F1B84594513C)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-D600F72A-D562-40ED-9881-F97ED53AA696)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-CD0F1D5E-75AF-41F8-A523-B85E83B9CD57)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-DD8E261C-7571-4975-9C41-A4A47EC047D7)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-80E5341C-0BC0-49A0-8BA1-FA59F2A9CE70)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-0CFC0199-8FDD-4927-AD1F-F9EA4C374E3A)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_SOURCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-F8BA1DD8-5613-4771-93D9-F60081E1E699)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_SOURCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-BA0A142B-EEE8-40FA-A6A0-5895A0D15CAC)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_SOURCE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-5D6EDF49-0187-48D8-AA74-6E88ABBB6FF6)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_SOURCE_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-5778F017-7E27-44FB-8F60-BDBE84533B71)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_SOURCE_CONNECTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-E62199FE-CE31-4638-9583-209092D08800)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_SOURCE_CONNECTION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-706D7E19-0451-46F5-A4EE-0841C6699E32)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_ASSET_SOURCE_CREDENTIALS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-374442B3-319A-447B-A535-0D3277028857)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_CHANGE_AGENT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-934D03AB-4AB7-4AFE-A4A8-EAD8CE277918)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_CHANGE_AGENT_DEPENDENCY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-A039D0CD-ABCB-43A8-9738-65C8136F4055)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_CHANGE_ASSET_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-B9D06E91-FAAC-4CAF-A22C-8FC3EEA620AC)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_CHANGE_ASSET_SOURCE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-F44DDED0-FBE8-44B8-8CDE-616DC7DDB91A)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_CHANGE_ASSET_TAGS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-A5E765F7-EE23-4FA5-95B8-83C12C2C7B52)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_CHANGE_DISCOVERY_SCHEDULE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-0ADEF569-6A37-42BF-8EA8-7D29925FB136)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_CHANGE_ENVIRONMENT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-DDE706AA-131E-4BC5-A1C7-F8939124082F)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_GPU_DEVICE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-C580C8E8-4315-417E-B5E9-A49FFBD501A7)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_NIC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-D0BCFA6A-DDAB-4162-85BC-7E4C017A4435)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_DISK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-8E6B5639-5D1E-4CFF-AFD7-5003FCDC60B8)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_NVDIMM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-4A1F1216-3C7A-4137-B3D1-132161AC9BEB)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_NVDIMM_CONTROLLER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-CF8551E8-A9E7-4A7A-889C-EEE2DBC1A737)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_SCSI_CONTROLLER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-D5EDFEE3-BADC-4F84-A58B-E9A95C9C0543)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_GPU_DEVICE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-A44A4152-FB2F-490B-AFE2-18998FBDA1D5)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_NIC_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-7A03C203-3EE4-45AB-B057-B66DB2CC3DA3)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_DISK_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-78AFF6BC-153A-4D5A-930C-BDDB5B151EBB)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_NVDIMM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-0BBBEF7D-5987-421C-8E26-1DBD9418D2FE)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_COMPUTE_PROPERTIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-BC3CD017-0386-4FF5-8AF4-4EB8120418E0)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_CREATE_AGENT_DEPENDENCY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-B1C6A6A2-ED17-4F40-A7D4-55A928AD7C77)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_CREATE_AGENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-C668113A-B097-44CF-843B-F02839C20576)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_CREATE_ASSET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-54F02D1A-7F6A-4058-9C06-782CE337381D)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_CREATE_ASSET_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-3DEB45F5-5EED-47DC-894E-8F13B9DFAB19)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_CREATE_DISCOVERY_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-66B127D3-1BE3-451D-B785-D262DDA5CD6B)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_CREATE_ENVIRONMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-80BD5926-108A-4C1A-ACC1-9C1BCB950C6F)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_CREATE_INVENTORY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-1A83F626-AF2A-4E5A-A8A2-0E3859C49994)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_CREATE_VM_WARE_ASSET_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-0F8F2308-2F4A-4EC5-B247-E176F393BF88)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_VM_PROPERTIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-ED87A92A-85A1-4AA0-BB04-41A7BA35C19E)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_CUSTOMER_TAG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-B9CB17D6-3B58-4328-A88E-68EC30B690BE)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_CUSTOMER_TAG_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-3BBEC2FF-B18C-4AA4-B901-88102BDB4928)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_VMWARE_VM_PROPERTIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-6D11AE1E-37D7-44F6-8D90-96E24293F9EC)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_VMWARE_V_CENTER_PROPERTIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-EF84EA70-B557-4E79-894E-369C50311734)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_CREATE_VMWARE_VM_ASSET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-79614B11-7AD9-4466-B800-608740761927)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_DISCOVERY_SCHEDULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-43B046A9-D203-4195-B935-A58AA916839F)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_DISCOVERY_SCHEDULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-C9DEC32F-77DE-4402-B1E1-A4051322F790)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_DISCOVERY_SCHEDULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-BD3630BF-0F88-487D-B9B7-122F399E8EEF)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_DISCOVERY_SCHEDULE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-3DA0DC08-A49A-42CF-B54B-4BC74472EA39)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_ENVIRONMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-A8857F5E-353F-468F-B2CF-6003BCD6CF67)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_ENVIRONMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-54DF145C-0F1D-4A30-924C-9A07BC35E8E1)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_ENVIRONMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-7748D17C-E7E9-4821-A8B3-B4FEEB7CF6BD)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_ENVIRONMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-D514F530-18E1-486C-8685-EDA0052D0788)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-F6699431-BC00-4990-B9AC-58AA548A2B4E)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_HISTORICAL_METRIC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-B9D0EA48-C2A1-466C-A430-510ECDEBDCDE)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_HISTORICAL_METRIC_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-2CA9EB94-8207-4209-ACD7-639EDF835367)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_HISTORICAL_METRIC_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-AF24BFF6-E397-424B-8D81-A75B764C14FC)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_HISTORICAL_METRIC_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-B3085EFA-FEB7-40DA-9DF8-5D46D16F6DD3)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_IMPORT_INVENTORY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-8D3401FD-9786-4970-8121-50093F075496)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_IMPORT_INVENTORY_VIA_ASSETS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-E7247CA5-5BBD-460F-BC8C-56F1A22E599A)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_INVENTORY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-D00DB22C-78F4-4FCF-98E7-7A9BC129B213)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_INVENTORY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-A732F6E5-F6F9-4530-8B37-456639351BD7)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_INVENTORY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-57F2FCCF-EC83-4B39-9503-DEA77D885B37)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_INVENTORY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-23C4D949-3666-4D71-904C-F37C031DF1F1)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_PLUGIN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-9D371165-205E-41DE-95B6-5FD780A9E78E)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_REMOVE_AGENT_DEPENDENCY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-A4C01ADE-B3E4-4885-8811-C578407CE903)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_HISTORICAL_METRIC_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-ED5453B4-9990-4015-B11F-4B8CFF5B4529)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_SUBMIT_HISTORICAL_METRICS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-7FF62CAF-8CF6-41BF-8F86-70C49E2DCE2C)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_UPDATE_AGENT_DEPENDENCY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-809AFBEA-F428-402C-A228-E18218A5CCAE)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_UPDATE_AGENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-5F447856-22A7-44A9-979B-8CF87C9BD246)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_UPDATE_ASSET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-E17CC7D3-2DFB-473A-A484-0494C31CCBBD)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_UPDATE_ASSET_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-C875AC99-A34E-4418-8ECC-99D7A6E90954)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_UPDATE_DISCOVERY_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-5B97C53E-1AF8-4F36-8484-6E7827083DE4)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_UPDATE_ENVIRONMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-0B97C5EA-6DE3-4ECD-A625-399D55E08E28)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_UPDATE_INVENTORY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-F58A4EF0-9211-4C18-81DB-7DF00F9D8975)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_UPDATE_PLUGIN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-9AE94299-DF7D-447F-A88D-6507680BA2C3)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_UPDATE_VM_ASSET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-3F33C347-1B0B-4C53-912F-E1AE8F06DCD4)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_UPDATE_VM_WARE_ASSET_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-084754C4-5067-4E80-B32A-3BA9C61D9C57)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_UPDATE_VMWARE_VM_ASSET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-81299345-2289-4E50-AC67-D24F821C64F9)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_VM_ASSET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-D49A7DC7-90F7-4A6B-B716-1BB5059E43ED)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_VM_WARE_ASSET_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-ED1353D0-FA0B-444F-B6A4-F935B766E9D6)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_VM_WARE_ASSET_SOURCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-3F033374-45F3-4619-A2D3-54A7D9D6FA78)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_VMWARE_VM_ASSET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-15399C31-913D-4B0C-B026-2A5DED392524)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-FD8B66E9-B29A-4B3D-AA8D-95A7D4AC74D3)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-BF97A1CC-3707-4A40-835A-B1BC79F2E842)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-D34D6CCF-FDF6-4001-A741-0CB1185A4302)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-5459A0C4-80C7-40DA-BEAE-C0198F65DAB0)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-21C19C8A-366F-4D2A-97ED-F278E11A2686)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-2282DC3D-4BEB-4172-9BEF-1706E3216F17)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-02598047-8E4F-4945-80BE-82DA07E9C19A)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-FFF12372-2E90-433F-ABD2-2080B9F2242B)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-1BCF95A2-A21F-4B42-9560-C4BBEB311B9F)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-9857850D-582E-4A5C-BB1A-538FF50272F3)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-02CFD2C3-49B9-4835-9E96-099B31CE46C8)
- [DBMS_CLOUD_OCI_CLOUD_BRIDGE_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_bridge_t.html#ADSDK-GUID-7A26B05E-E429-4246-91BC-C33202746878)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
