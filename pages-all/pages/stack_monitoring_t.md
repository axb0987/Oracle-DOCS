# Stack Monitoring Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html
- Fetched: 2026-09-05 19:20 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#dcoc-content-body)

## Stack Monitoring Common Types

### DBMS_CLOUD_OCI_STACK_MONITORING_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_ANOMALY_DATA_POINT_T Type

anomaly evaluation result fo the data point

Syntax
```

```

Fields

Field Description

`anomaly`

(required) if the value is anomaly or not 0 indicates not an anomaly -1 indicates value is below the threshold +1 indicates value is above the threshold

`low`

(optional) lower threshold for the metric value

`high`

(optional) upper threshold for the metric value

`l_timestamp`

(required) timestamp of when the metric was collected

`value`

(required) value for the metric data point

### DBMS_CLOUD_OCI_STACK_MONITORING_ANOMALY_DATA_POINT_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_anomaly_data_point_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_ANOMALY_METRIC_DATA_T Type

Anomaly Metric Details

Syntax
```

```

Fields

Field Description

`dimensions`

(optional) list of dimensions for the metric

`data_points`

(required) list of anomaly data points for the metric

### DBMS_CLOUD_OCI_STACK_MONITORING_ASSOCIATE_MONITORED_RESOURCES_DETAILS_T Type

The information required to create new monitored resource association.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) Compartment Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`association_type`

(required) Association type to be created between source and destination resources.

`source_resource_id`

(required) Source Monitored Resource Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`destination_resource_id`

(required) Destination Monitored Resource Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

### DBMS_CLOUD_OCI_STACK_MONITORING_ASSOCIATED_MONITORED_RESOURCE_T Type

The information about monitored resource.

Syntax
```

```

Fields

Field Description

`id`

(required) Monitored resource identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`name`

(optional) Monitored Resource Name.

`display_name`

(optional) Monitored resource display name.

`l_type`

(optional) Monitored Resource Type.

`compartment_id`

(optional) Compartment Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`host_name`

(optional) Monitored Resource Host Name.

`external_id`

(optional) External resource is any OCI resource identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)which is not a Stack Monitoring service resource. Currently supports only following resource types - Container database, non-container database, pluggable database and OCI compute instance.

`management_agent_id`

(optional) Management Agent Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`lifecycle_state`

(optional) The current state of the monitored resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`license`

(optional) License edition of the monitored resource.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION'

`association`

(optional) Association details of the resource.

### DBMS_CLOUD_OCI_STACK_MONITORING_ASSOCIATED_MONITORED_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_associated_monitored_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_ASSOCIATED_RESOURCES_SUMMARY_T Type

The information about monitored resource.

Syntax
```

```

Fields

Field Description

`id`

(required) Monitored resource identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`name`

(optional) Monitored Resource Name.

`display_name`

(optional) Monitored resource display name.

`l_type`

(optional) Monitored Resource Type.

`compartment_id`

(optional) Compartment Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`host_name`

(optional) Monitored Resource Host Name.

`external_id`

(optional) External resource is any OCI resource identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)which is not a Stack Monitoring service resource. Currently supports only following resource types - Container database, non-container database, pluggable database and OCI compute instance.

`management_agent_id`

(optional) Management Agent Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`lifecycle_state`

(optional) The current state of the monitored resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`license`

(optional) License edition of the monitored resource.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION'

`associated_resources`

(optional) List of associated monitored resources.

### DBMS_CLOUD_OCI_STACK_MONITORING_ASSOCIATED_RESOURCES_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_associated_resources_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_ASSOCIATED_RESOURCES_COLLECTION_T Type

Results of a resources search. Contains AssociatedResourcesSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of associated monitored resources.

### DBMS_CLOUD_OCI_STACK_MONITORING_ASSOCIATION_DETAILS_T Type

The information about monitored resource association.

Syntax
```

```

Fields

Field Description

`source_resource_id`

(required) Source Monitored Resource Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`association_type`

(required) Association Type.

### DBMS_CLOUD_OCI_STACK_MONITORING_ASSOCIATION_RESOURCE_DETAILS_T Type

Association Resource Details.

Syntax
```

```

Fields

Field Description

`name`

(optional) Monitored Resource Name.

`l_type`

(optional) Monitored Resource Type.

`compartment_id`

(optional) Compartment Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

### DBMS_CLOUD_OCI_STACK_MONITORING_CONFIG_T Type

A configuration item that, for example defines whether resources of a specific type should be discovered automatically. In this case, the 'configType' is set to 'AUTO_PROMOTE' and additional fields like 'resourceType' and 'isEnabled' determine if such resources are to be discovered automatically (also referred to as 'Automatic Promotion').

Syntax
```

```

Fields

Field Description

`id`

(required) The Unique Oracle ID (OCID) that is immutable on creation.

`compartment_id`

(required) The OCID of the compartment containing the configuration.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`time_created`

(optional) The time the configuration was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the Config was updated.

`lifecycle_state`

(required) The current state of the configuration.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`config_type`

(required) The type of configuration.

Allowed values are: 'AUTO_PROMOTE', 'LICENSE_AUTO_ASSIGN', 'LICENSE_ENTERPRISE_EXTENSIBILITY'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_AUTO_PROMOTE_CONFIG_DETAILS_T Type

A configuration of the AUTO_PROMOTE type, consists of a resource type and a boolean value that determines if this resource needs to be automatically promoted/discovered. For example, when a Management Agent registration event occurs and if isEnabled is TRUE for a HOST resource type, a HOST resource will be automatically discovered using that Management Agent.

Syntax
```

```

`dbms_cloud_oci_stack_monitoring_auto_promote_config_details_t`is a subtype of the`dbms_cloud_oci_stack_monitoring_config_t`type.

Fields

Field Description

`resource_type`

(required) The type of resource to configure for automatic promotion.

Allowed values are: 'HOST'

`is_enabled`

(required) True if automatic promotion is enabled, false if it is not enabled.

### DBMS_CLOUD_OCI_STACK_MONITORING_CONFIG_SUMMARY_T Type

Summary of the configuration.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`compartment_id`

(required) Compartment Identifier.

`display_name`

(optional) Config Identifier, can be renamed.

`time_created`

(optional) The time the the configuration was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the configuration was updated.

`lifecycle_state`

(required) The current state of the configuration.

`config_type`

(required) The type of configuration.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_AUTO_PROMOTE_CONFIG_SUMMARY_T Type

Summary of an AUTO_PROMOTE config.

Syntax
```

```

`dbms_cloud_oci_stack_monitoring_auto_promote_config_summary_t`is a subtype of the`dbms_cloud_oci_stack_monitoring_config_summary_t`type.

Fields

Field Description

`resource_type`

(required) The type of resource to configure for automatic promotion.

Allowed values are: 'HOST'

`is_enabled`

(required) True if automatic promotion is enabled, false if it is not enabled.

### DBMS_CLOUD_OCI_STACK_MONITORING_BASELINEABLE_METRIC_T Type

Summary for the baseline-able metric

Syntax
```

```

Fields

Field Description

`created_by`

(optional) Created user id

`last_updated_by`

(optional) last Updated user id

`time_created`

(optional) creation date

`time_last_updated`

(optional) last updated time

`id`

(required) OCID of the metric

`lifecycle_state`

(optional) The current lifecycle state of the metric extension

Allowed values are: 'ACTIVE', 'DELETED'

`tenancy_id`

(optional) OCID of the tenancy

`compartment_id`

(optional) OCID of the compartment

`name`

(required) name of the metric

`l_column`

(required) metric column name

`namespace`

(required) namespace of the metric

`resource_group`

(required) Resource group of the metric

`is_out_of_box`

(required) Is the metric created out of box, default false

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_BASELINEABLE_METRIC_SUMMARY_T Type

Summary for the baseline-able metric

Syntax
```

```

Fields

Field Description

`id`

(required) OCID of the metric

`lifecycle_state`

(optional) The current lifecycle state of the metric extension

Allowed values are: 'ACTIVE', 'DELETED'

`tenancy_id`

(optional) OCID of the tenancy

`compartment_id`

(optional) OCID of the compartment

`name`

(required) name of the metric

`l_column`

(required) metric column name

`namespace`

(required) namespace of the metric

`resource_group`

(required) Resource group of the metric

`is_out_of_box`

(required) Is the metric created out of box, default false

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_BASELINEABLE_METRIC_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_baselineable_metric_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_BASELINEABLE_METRIC_SUMMARY_COLLECTION_T Type

List summary of Baseline-able metrics

Syntax
```

```

Fields

Field Description

`items`

(required) list of baseline-able metric summary

### DBMS_CLOUD_OCI_STACK_MONITORING_CHANGE_CONFIG_COMPARTMENT_DETAILS_T Type

Details for which compartment to move the resource to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_STACK_MONITORING_CHANGE_METRIC_EXTENSION_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_STACK_MONITORING_CHANGE_MONITORED_RESOURCE_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_STACK_MONITORING_CHANGE_MONITORED_RESOURCE_TASK_COMPARTMENT_DETAILS_T Type

The information required for change of compartment for stack monitoring resource task.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_STACK_MONITORING_CONFIG_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_config_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_CONFIG_COLLECTION_T Type

Contains a list of configurations.

Syntax
```

```

Fields

Field Description

`items`

(required) List of configurations.

### DBMS_CLOUD_OCI_STACK_MONITORING_CONNECTION_DETAILS_T Type

Connection details for the database.

Syntax
```

```

Fields

Field Description

`protocol`

(required) Protocol used in DB connection string when connecting to external database service.

Allowed values are: 'TCP', 'TCPS'

`port`

(required) Listener Port number used for connection requests.

`connector_id`

(optional) Database connector Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`service_name`

(required) Service name used for connection requests.

`db_unique_name`

(optional) UniqueName used for database connection requests.

`db_id`

(optional) dbId of the database.

`ssl_secret_id`

(optional) SSL Secret Identifier for TCPS connector in OCI Vault[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

### DBMS_CLOUD_OCI_STACK_MONITORING_CREATE_CONFIG_DETAILS_T Type

Create a configuration.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The display name of the configuration.

`compartment_id`

(required) Compartment in which the configuration is created.

`config_type`

(required) The type of configuration.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_CREATE_AUTO_PROMOTE_CONFIG_DETAILS_T Type

The details of an AUTO_PROMOTE configuration.

Syntax
```

```

`dbms_cloud_oci_stack_monitoring_create_auto_promote_config_details_t`is a subtype of the`dbms_cloud_oci_stack_monitoring_create_config_details_t`type.

Fields

Field Description

`resource_type`

(required) The type of resource to configure for automatic promotion.

Allowed values are: 'HOST'

`is_enabled`

(required) True if automatic promotion is enabled, false if it is not enabled.

### DBMS_CLOUD_OCI_STACK_MONITORING_CREATE_BASELINEABLE_METRIC_DETAILS_T Type

Summary for the baseline-able metric

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) OCID of the compartment

`name`

(required) name of the metric

`l_column`

(required) metric column name

`namespace`

(required) namespace of the metric

`resource_group`

(required) Resource group of the metric

### DBMS_CLOUD_OCI_STACK_MONITORING_PROPERTY_DETAILS_T Type

Property Details

Syntax
```

```

Fields

Field Description

`properties_map`

(optional) Key/Value pair of Property

### DBMS_CLOUD_OCI_STACK_MONITORING_CREDENTIAL_DETAILS_T Type

DiscoveryJob Credential Details.

Syntax
```

```

Fields

Field Description

`l_credential_name`

(required) Name of Credential

`credential_type`

(required) Name of Credential Type

`properties`

(required)

### DBMS_CLOUD_OCI_STACK_MONITORING_CREDENTIAL_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_credential_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_CREDENTIAL_COLLECTION_T Type

List of DiscoveryJOb Credential Details.

Syntax
```

```

Fields

Field Description

`items`

(required) List of DiscoveryJob credentials.

### DBMS_CLOUD_OCI_STACK_MONITORING_DISCOVERY_DETAILS_T Type

The request of DiscoveryJob Resource details.

Syntax
```

```

Fields

Field Description

`agent_id`

(required) The OCID of Management Agent

`resource_type`

(required) Resource Type.

Allowed values are: 'WEBLOGIC_DOMAIN', 'EBS_INSTANCE', 'SQL_SERVER', 'APACHE_TOMCAT', 'ORACLE_DATABASE', 'OCI_ORACLE_DB', 'OCI_ORACLE_CDB', 'OCI_ORACLE_PDB', 'HOST', 'ORACLE_PSFT', 'ORACLE_MFT', 'APACHE_HTTP_SERVER', 'ORACLE_GOLDENGATE'

`resource_name`

(required) The Name of resource type

`license`

(optional) License edition of the monitored resource.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION'

`properties`

(required)

`credentials`

(optional)

`tags`

(optional)

### DBMS_CLOUD_OCI_STACK_MONITORING_CREATE_DISCOVERY_JOB_DETAILS_T Type

The request of DiscoveryJob details.

Syntax
```

```

Fields

Field Description

`discovery_type`

(optional) Add option submits new discovery Job. Add with retry option to re-submit failed discovery job. Refresh option refreshes the existing discovered resources.

Allowed values are: 'ADD', 'ADD_WITH_RETRY', 'REFRESH'

`discovery_client`

(optional) Client who submits discovery job.

`compartment_id`

(required) The OCID of Compartment

`discovery_details`

(required)

`should_propagate_tags_to_discovered_resources`

(optional) If this parameter set to true, the specified tags will be applied to all resources discovered in the current request. Default is true.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_CREATE_LICENSE_AUTO_ASSIGN_CONFIG_DETAILS_T Type

The details of a LICENSE_AUTO_ASSIGN configuration.

Syntax
```

```

`dbms_cloud_oci_stack_monitoring_create_license_auto_assign_config_details_t`is a subtype of the`dbms_cloud_oci_stack_monitoring_create_config_details_t`type.

Fields

Field Description

`license`

(required) License edition.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION'

### DBMS_CLOUD_OCI_STACK_MONITORING_CREATE_LICENSE_ENTERPRISE_EXTENSIBILITY_CONFIG_DETAILS_T Type

The details of a LICENSE_ENTERPRISE_EXTENSIBILITY configuration.

Syntax
```

```

`dbms_cloud_oci_stack_monitoring_create_license_enterprise_extensibility_config_details_t`is a subtype of the`dbms_cloud_oci_stack_monitoring_create_config_details_t`type.

Fields

Field Description

`is_enabled`

(required) True if enterprise extensibility is enabled, false if it is not enabled.

### DBMS_CLOUD_OCI_STACK_MONITORING_METRIC_T Type

Details of a metric which is part of this metric extension

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the metric.

`display_name`

(optional) Display name of the metric.

`is_dimension`

(optional) Current metric need to be included as dimension or not

`compute_expression`

(optional) Compute Expression to calculate the value of this metric

`data_type`

(required) Data type of value of this metric

Allowed values are: 'STRING', 'NUMBER'

`is_hidden`

(optional) Flag to marks whether a metric has to be uploaded or not. When isHidden = false -&gt; Metric is uploaded, isHidden = true -&gt; Metric is NOT uploaded

`metric_category`

(optional) Metric category

Allowed values are: 'LOAD', 'UTILIZATION', 'CAPACITY', 'AVAILABILITY'

`unit`

(optional) Unit of metric value

### DBMS_CLOUD_OCI_STACK_MONITORING_METRIC_EXTENSION_QUERY_PROPERTIES_T Type

Collection method and query properties details of metric extension

Syntax
```

```

Fields

Field Description

`collection_method`

(required) Type of possible collection methods.

Allowed values are: 'OS_COMMAND', 'SQL', 'JMX'

### DBMS_CLOUD_OCI_STACK_MONITORING_METRIC_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_metric_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_CREATE_METRIC_EXTENSION_DETAILS_T Type

The information about new metric extension resource. The combination of metric extension name and resource type should be unique in a compartment.

Syntax
```

```

Fields

Field Description

`name`

(required) Metric Extension Resource name.

`display_name`

(required) Metric Extension display name.

`resource_type`

(required) Resource type to which Metric Extension applies

`compartment_id`

(required) Compartment Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)

`description`

(optional) Description of the metric extension.

`collection_recurrences`

(required) Schedule of metric extension should use RFC 5545 format i.e. recur-rule-part = \"FREQ\";INTERVAL where FREQ rule part identifies the type of recurrence rule. Valid values are \"MINUTELY\",\"HOURLY\",\"DAILY\" to specify repeating events based on an interval of a minute, an hour and a day or more. Example- FREQ=DAILY;INTERVAL=1

`metric_list`

(required) List of metrics which are part of this metric extension

`query_properties`

(required)

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_PROPERTY_T Type

Property of monitored resource.

Syntax
```

```

Fields

Field Description

`name`

(optional) Property Name.

`value`

(optional) Property Value.

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_CREDENTIAL_T Type

Monitored Resource Credential Details.

Syntax
```

```

Fields

Field Description

`source`

(optional) The source type and source name combination, delimited with (.) separator. {source type}.{source name} and source type max char limit is 63.

`name`

(optional) The name of the credential, within the context of the source.

`l_type`

(optional) The type of the credential ( ex. JMXCreds,DBCreds).

`description`

(optional) The user-specified textual description of the credential.

`credential_type`

(optional) Type of credentials specified in the credentials element. Three possible values - EXISTING, PLAINTEXT and ENCRYPTED. * EXISTING - Credential is already stored in agent and only credential name need to be passed for existing credential. * PLAINTEXT - The credential properties will have credentials in plain text format. * ENCRYPTED - The credential properties will have credentials stored in vault in encrypted format using KMS client which uses master key for encryption. The same master key will be used to decrypt the credentials before passing on to the management agent.

Allowed values are: 'EXISTING', 'PLAINTEXT', 'ENCRYPTED'

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_ALIAS_SOURCE_CREDENTIAL_T Type

Monitored Resource Alias Reference Source Credential.

Syntax
```

```

Fields

Field Description

`source`

(required) The source type and source name combination,delimited with (.) separator. This refers to the pre-existing source which alias cred should point to. Ex. {source type}.{source name} and source type max char limit is 63.

`name`

(required) The name of the pre-existing source credential which alias cred should point to. This should refer to the pre-existing source attribute which is bound to credential name.

`service`

(required) The name of the service owning the credential. Example: stack-monitoring or dbmgmt

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_ALIAS_CREDENTIAL_T Type

Monitored Resource Alias Credential Details

Syntax
```

```

Fields

Field Description

`source`

(required) The source type and source name combination,delimited with (.) separator. Example: {source type}.{source name} and source type max char limit is 63.

`name`

(required) The name of the alias, within the context of the source.

`credential`

(required)

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_PROPERTY_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_monitored_resource_property_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_CREDENTIAL_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_monitored_resource_credential_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_ALIAS_CREDENTIAL_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_monitored_resource_alias_credential_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_CREATE_MONITORED_RESOURCE_DETAILS_T Type

The information about new monitored resource to be created. The combination of monitored resource name and type should be unique across tenancy.

Syntax
```

```

Fields

Field Description

`name`

(required) Monitored Resource Name.

`display_name`

(optional) Monitored resource display name.

`l_type`

(required) Monitored Resource Type.

`compartment_id`

(required) Compartment Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`host_name`

(optional) Host name of the monitored resource.

`external_id`

(optional) External resource is any OCI resource identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)which is not a Stack Monitoring service resource. Currently supports only OCI compute instance.

`management_agent_id`

(optional) Management Agent Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`resource_time_zone`

(optional) Time zone in the form of tz database canonical zone ID. Specifies the preference with a value that uses the IANA Time Zone Database format (x-obmcs-time-zone). For example - America/Los_Angeles

`license`

(optional) License edition of the monitored resource. If not provided the default license type for the compartment will be used.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION'

`properties`

(optional) List of monitored resource properties.

`database_connection_details`

(optional)

`credentials`

(optional)

`aliases`

(optional)

`additional_credentials`

(optional) List of MonitoredResourceCredentials. This property complements the existing \"credentials\" property by allowing user to specify more than one credential. If both \"credential\" and \"additionalCredentials\" are specified, union of the values is used as list of credentials applicable for this resource. If any duplicate found in the combined list of \"credentials\" and \"additionalCredentials\", an error will be thrown.

`additional_aliases`

(optional) List of MonitoredResourceAliasCredentials. This property complements the existing \"aliases\" property by allowing user to specify more than one credential alias. If both \"aliases\" and \"additionalAliases\" are specified, union of the values is used as list of aliases applicable for this resource. If any duplicate found in the combined list of \"alias\" and \"additionalAliases\", an error will be thrown.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_TASK_DETAILS_T Type

The request details for the performing the task.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Task type.

Allowed values are: 'IMPORT_OCI_TELEMETRY_RESOURCES'

### DBMS_CLOUD_OCI_STACK_MONITORING_CREATE_MONITORED_RESOURCE_TASK_DETAILS_T Type

The request details for the stack monitoring resource task.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment identifier.

`name`

(optional) Name of the task. If not provided by default the following names will be taken OCI tasks - namespace plus timestamp.

`task_details`

(required)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_RESOURCE_TYPE_METADATA_DETAILS_T Type

The metadata details for resource type.

Syntax
```

```

Fields

Field Description

`format`

(required) ResourceType metadata format to be used. Currently supports only one format. Possible values - SYSTEM_FORMAT. * SYSTEM_FORMAT - The resource type metadata is defined in machine friendly format.

Allowed values are: 'SYSTEM_FORMAT'

### DBMS_CLOUD_OCI_STACK_MONITORING_CREATE_MONITORED_RESOURCE_TYPE_DETAILS_T Type

The information about new monitored resource type. The resource type name should be unique across tenancy. A set of resource types are created by the service by default. These resource types are available for all tenancies. Service provided resource types can not be duplicated or overwritten in any tenancy.

Syntax
```

```

Fields

Field Description

`name`

(required) A unique monitored resource type name. The name must be unique across tenancy. Name can not be changed.

`display_name`

(optional) Monitored resource type display name.

`description`

(optional) A friendly description.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tenancy containing the resource type.

`metric_namespace`

(optional) Metric namespace for resource type.

`metadata`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_CREDENTIAL_PROPERTY_T Type

Monitored resource credential property.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the credential property, should confirm with names of properties of this credential's type. Example: For JMXCreds type, credential property name for weblogic user is 'Username'.

`value`

(required) The value of the credential property name. Example: For JMXCreds type, credential property value for 'Username' property is 'weblogic'.

### DBMS_CLOUD_OCI_STACK_MONITORING_DATA_POINT_T Type

metric data point

Syntax
```

```

Fields

Field Description

`l_timestamp`

(required) timestamp of when the metric was collected

`value`

(required) value for the metric data point

### DBMS_CLOUD_OCI_STACK_MONITORING_DISABLE_METRIC_EXTENSION_DETAILS_T Type

The Resource IDs for which metric extension will be disabled

Syntax
```

```

Fields

Field Description

`resource_ids`

(required) List of Resource IDs [OCIDs]. Currently supports upto 20 resources per request

### DBMS_CLOUD_OCI_STACK_MONITORING_DISASSOCIATE_MONITORED_RESOURCES_DETAILS_T Type

The information required to create new monitored resource association.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) Compartment Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`association_type`

(optional) Association type between source and destination resources.

`source_resource_id`

(optional) Source Monitored Resource Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`destination_resource_id`

(optional) Destination Monitored Resource Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

### DBMS_CLOUD_OCI_STACK_MONITORING_DISCOVERY_JOB_T Type

The DiscoveryJob details.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of Discovery job

`compartment_id`

(optional) The OCID of the Compartment

`discovery_type`

(optional) Add option submits new discovery Job. Add with retry option to re-submit failed discovery job. Refresh option refreshes the existing discovered resources.

Allowed values are: 'ADD', 'ADD_WITH_RETRY', 'REFRESH'

`status`

(optional) Specifies the status of the discovery job

Allowed values are: 'SUCCESS', 'FAILURE', 'INPROGRESS', 'INACTIVE', 'CREATED', 'DELETED'

`status_message`

(optional) The short summary of the status of the discovery job

`tenant_id`

(optional) The OCID of Tenant

`user_id`

(optional) The OCID of user in which the job is submitted

`discovery_client`

(optional) Client who submits discovery job.

`discovery_details`

(optional)

`time_updated`

(optional) The time the discovery Job was updated.

`lifecycle_state`

(optional) The current state of the DiscoveryJob Resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_DISCOVERY_JOB_SUMMARY_T Type

The Summary of DiscoveryJob details.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of Discovery job

`resource_type`

(optional) Resource Type

Allowed values are: 'WEBLOGIC_DOMAIN', 'EBS_INSTANCE', 'SQL_SERVER', 'APACHE_TOMCAT', 'ORACLE_DATABASE', 'OCI_ORACLE_DB', 'OCI_ORACLE_CDB', 'OCI_ORACLE_PDB', 'HOST', 'ORACLE_PSFT', 'ORACLE_MFT', 'APACHE_HTTP_SERVER', 'ORACLE_GOLDENGATE'

`resource_name`

(optional) The name of resource type

`license`

(optional) License edition of the monitored resource.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION'

`compartment_id`

(optional) The OCID of the Compartment

`discovery_type`

(optional) Add option submits new discovery Job. Add with retry option to re-submit failed discovery job. Refresh option refreshes the existing discovered resources.

Allowed values are: 'ADD', 'ADD_WITH_RETRY', 'REFRESH'

`status`

(optional) Specifies the status of the discovery job

Allowed values are: 'SUCCESS', 'FAILURE', 'INPROGRESS', 'INACTIVE', 'CREATED', 'DELETED'

`status_message`

(optional) The short summary of the status of the discovery job

`tenant_id`

(optional) The OCID of Tenant

`user_id`

(optional) The OCID of user in which the job is submitted

`time_updated`

(optional) The time the discovery Job was updated.

`lifecycle_state`

(optional) The current state of the DiscoveryJob Resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_DISCOVERY_JOB_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_discovery_job_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_DISCOVERY_JOB_COLLECTION_T Type

Result of the discovery Job search

Syntax
```

```

Fields

Field Description

`items`

(required) List of Discovery jobs

### DBMS_CLOUD_OCI_STACK_MONITORING_DISCOVERY_JOB_LOG_SUMMARY_T Type

Log of a specific job

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of Discovery job

`log_type`

(required) Type of log (INFO, WARNING, ERROR or SUCCESS)

Allowed values are: 'INFO', 'WARNING', 'ERROR', 'SUCCESS'

`log_message`

(required) Log message

`time_created`

(required) Time the Job log was created

### DBMS_CLOUD_OCI_STACK_MONITORING_DISCOVERY_JOB_LOG_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_discovery_job_log_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_DISCOVERY_JOB_LOG_COLLECTION_T Type

List of logs of a job

Syntax
```

```

Fields

Field Description

`items`

(required) List of logs

### DBMS_CLOUD_OCI_STACK_MONITORING_ENABLE_METRIC_EXTENSION_DETAILS_T Type

The Resource IDs for which metric extension will be enabled

Syntax
```

```

Fields

Field Description

`resource_ids`

(required) List of Resource IDs [OCIDs]. Currently supports upto 20 resources per request

### DBMS_CLOUD_OCI_STACK_MONITORING_ENABLED_RESOURCE_DETAILS_T Type

Details of a resource on which Metric Extension is enabled

Syntax
```

```

Fields

Field Description

`resource_id`

(required) The OCID of the resource on which Metric Extension is enabled

### DBMS_CLOUD_OCI_STACK_MONITORING_CREDENTIAL_PROPERTY_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_credential_property_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_ENCRYPTED_CREDENTIALS_T Type

Encrypted credentials [indicated by the type property in CredentialStore].

Syntax
```

```

`dbms_cloud_oci_stack_monitoring_encrypted_credentials_t`is a subtype of the`dbms_cloud_oci_stack_monitoring_monitored_resource_credential_t`type.

Fields

Field Description

`key_id`

(required) The master key should be created in OCI Vault owned by the client of this API. The user should have permission to access the vault key.

`properties`

(required) The credential properties list. Credential property values will be encrypted format.

### DBMS_CLOUD_OCI_STACK_MONITORING_ERROR_T Type

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

### DBMS_CLOUD_OCI_STACK_MONITORING_DATA_POINT_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_data_point_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_METRIC_DATA_T Type

Metric Details

Syntax
```

```

Fields

Field Description

`dimensions`

(optional) list of dimensions for the metric

`training_data_points`

(required) list of data points for the metric for training of baseline

`evaluation_data_points`

(required) list of data points for the metric for evaluation of anomalies

### DBMS_CLOUD_OCI_STACK_MONITORING_METRIC_DATA_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_metric_data_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_EVALUATE_BASELINEABLE_METRIC_DETAILS_T Type

Details for Baseline Metric Data to evaluate

Syntax
```

```

Fields

Field Description

`resource_id`

(required) OCID of the resource

`items`

(required) List of Metric data

### DBMS_CLOUD_OCI_STACK_MONITORING_ANOMALY_METRIC_DATA_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_anomaly_metric_data_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_EVALUATE_BASELINEABLE_METRIC_RESULT_T Type

Result for Baseline Metric Data evaluation

Syntax
```

```

Fields

Field Description

`resource_id`

(required) OCID of the resource

`items`

(required) List of Metric data

### DBMS_CLOUD_OCI_STACK_MONITORING_IMPORT_OCI_TELEMETRY_RESOURCES_TASK_DETAILS_T Type

Request details for importing resources from Telemetry like resources from OCI Native Services and prometheus.

Syntax
```

```

`dbms_cloud_oci_stack_monitoring_import_oci_telemetry_resources_task_details_t`is a subtype of the`dbms_cloud_oci_stack_monitoring_monitored_resource_task_details_t`type.

Fields

Field Description

`source`

(required) Source from where the metrics pushed to telemetry. Possible values: * OCI_TELEMETRY_NATIVE - The metrics are pushed to telemetry from OCI Native Services. * OCI_TELEMETRY_PROMETHEUS - The metrics are pushed to telemetry from Prometheus.

Allowed values are: 'OCI_TELEMETRY_NATIVE', 'OCI_TELEMETRY_PROMETHEUS'

`namespace`

(required) Name space to be used for OCI Native service resources discovery.

`resource_group`

(optional) The resource group to use while fetching metrics from telemetry. If not specified, resource group will be skipped in the list metrics request.

`availability_proxy_metrics`

(optional) List of metrics to be used to calculate the availability of the resource. Resource is considered to be up if at least one of the specified metrics is available for the resource during the specified interval using the property 'availabilityProxyMetricCollectionIntervalInSeconds'. If no metrics are specified, availability will not be calculated for the resource.

`availability_proxy_metric_collection_interval`

(optional) Metrics collection interval in seconds used when calculating the availability of the resource based on metrics specified using the property 'availabilityProxyMetrics'.

### DBMS_CLOUD_OCI_STACK_MONITORING_JMX_QUERY_PROPERTIES_T Type

Query Properties applicable to JMX type of collection method

Syntax
```

```

`dbms_cloud_oci_stack_monitoring_jmx_query_properties_t`is a subtype of the`dbms_cloud_oci_stack_monitoring_metric_extension_query_properties_t`type.

Fields

Field Description

`managed_bean_query`

(required) JMX Managed Bean Query or Metric Service Table name

`jmx_attributes`

(required) List of JMX attributes or Metric Service Table columns separated by semi-colon

`identity_metric`

(optional) Semi-colon separated list of key properties from Managed Bean ObjectName to be used as key metrics

`auto_row_prefix`

(optional) Prefix for an auto generated metric, in case multiple rows with non unique key values are returned

`is_metric_service_enabled`

(optional) Indicates if Metric Service is enabled on server domain

### DBMS_CLOUD_OCI_STACK_MONITORING_METRIC_EXTENSION_UPDATE_QUERY_PROPERTIES_T Type

Collection method and query properties details of metric extension during update

Syntax
```

```

Fields

Field Description

`collection_method`

(required) Type of possible collection methods.

Allowed values are: 'OS_COMMAND', 'SQL', 'JMX'

### DBMS_CLOUD_OCI_STACK_MONITORING_JMX_UPDATE_QUERY_PROPERTIES_T Type

Query Properties applicable to JMX type of collection method

Syntax
```

```

`dbms_cloud_oci_stack_monitoring_jmx_update_query_properties_t`is a subtype of the`dbms_cloud_oci_stack_monitoring_metric_extension_update_query_properties_t`type.

Fields

Field Description

`managed_bean_query`

(optional) JMX Managed Bean Query or Metric Service Table name

`jmx_attributes`

(optional) List of JMX attributes or Metric Service Table columns separated by semi-colon

`identity_metric`

(optional) Semi-colon separated list of key properties from Managed Bean ObjectName to be used as key metrics

`auto_row_prefix`

(optional) Prefix for an auto generated metric, in case multiple rows with non unique key values are returned

`is_metric_service_enabled`

(optional) Indicates if Metric Service is enabled on server domain

### DBMS_CLOUD_OCI_STACK_MONITORING_LICENSE_AUTO_ASSIGN_CONFIG_DETAILS_T Type

A configuration of the LICENSE_AUTO_ASSIGN type, consists of an enumeration value which indicates which license should be assigned by default to new resources.

Syntax
```

```

`dbms_cloud_oci_stack_monitoring_license_auto_assign_config_details_t`is a subtype of the`dbms_cloud_oci_stack_monitoring_config_t`type.

Fields

Field Description

`license`

(required) License edition.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION'

### DBMS_CLOUD_OCI_STACK_MONITORING_LICENSE_AUTO_ASSIGN_CONFIG_SUMMARY_T Type

Summary of a LICENSE_AUTO_ASSIGN configuration.

Syntax
```

```

`dbms_cloud_oci_stack_monitoring_license_auto_assign_config_summary_t`is a subtype of the`dbms_cloud_oci_stack_monitoring_config_summary_t`type.

Fields

Field Description

`license`

(required) License edition.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION'

### DBMS_CLOUD_OCI_STACK_MONITORING_LICENSE_ENTERPRISE_EXTENSIBILITY_CONFIG_DETAILS_T Type

A configuration of the LICENSE_ENTERPRISE_EXTENSIBILITY type, consists of a boolean which determines whether enterprise extensibility is enabled.

Syntax
```

```

`dbms_cloud_oci_stack_monitoring_license_enterprise_extensibility_config_details_t`is a subtype of the`dbms_cloud_oci_stack_monitoring_config_t`type.

Fields

Field Description

`is_enabled`

(required) True if enterprise extensibility is enabled, false if it is not enabled.

### DBMS_CLOUD_OCI_STACK_MONITORING_LICENSE_ENTERPRISE_EXTENSIBILITY_CONFIG_SUMMARY_T Type

Summary of a LICENSE_ENTERPRISE_EXTENSIBILITY configuration.

Syntax
```

```

`dbms_cloud_oci_stack_monitoring_license_enterprise_extensibility_config_summary_t`is a subtype of the`dbms_cloud_oci_stack_monitoring_config_summary_t`type.

Fields

Field Description

`is_enabled`

(required) True if enterprise extensibility is enabled, false if it is not enabled.

### DBMS_CLOUD_OCI_STACK_MONITORING_MANAGE_LICENSE_DETAILS_T Type

License information for a given resource.

Syntax
```

```

Fields

Field Description

`license`

(required) License edition of the monitored resource.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION'

### DBMS_CLOUD_OCI_STACK_MONITORING_ENABLED_RESOURCE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_enabled_resource_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_METRIC_EXTENSION_T Type

Detailed information of the Metric Extension resource

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of Metric Extension resource

`name`

(required) Metric Extension resource name

`display_name`

(required) Metric Extension resource display name

`description`

(optional) Description of the metric extension.

`resource_type`

(required) Resource type to which Metric Extension applies

`compartment_id`

(required) Compartment Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)

`tenant_id`

(required) Tenant Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)

`collection_method`

(required) Collection Method Metric Extension applies

`status`

(required) The current status of the metric extension i.e. whether it is Draft or Published

Allowed values are: 'DRAFT', 'PUBLISHED'

`lifecycle_state`

(optional) The current lifecycle state of the metric extension

Allowed values are: 'ACTIVE', 'DELETED'

`created_by`

(optional) Created by user

`last_updated_by`

(optional) Last updated by user

`time_created`

(optional) Metric Extension creation time. An RFC3339 formatted datetime string.

`time_updated`

(optional) Metric Extension update time. An RFC3339 formatted datetime string.

`collection_recurrences`

(required) Schedule of metric extension should use RFC 5545 format -&gt; recur-rule-part = \"FREQ\";\"INTERVAL\" where FREQ rule part identifies the type of recurrence rule. Valid values are \"MINUTELY\",\"HOURLY\",\"DAILY\" to specify repeating events based on an interval of a minute, an hour and a day or more. Example- FREQ=DAILY;INTERVAL=1

`metric_list`

(required) List of metrics which are part of this metric extension

`query_properties`

(required)

`enabled_on_resources`

(optional) List of resource objects on which this metric extension is enabled.

`enabled_on_resources_count`

(optional) Count of resources on which this metric extension is enabled.

`resource_uri`

(optional) The URI path that the user can do a GET on to access the metric extension metadata

### DBMS_CLOUD_OCI_STACK_MONITORING_METRIC_EXTENSION_SUMMARY_T Type

Summary information about metric extension resources

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of metric extension.

`name`

(required) Metric Extension Resource name.

`display_name`

(optional) Metric Extension resource display name.

`description`

(optional) Description of the metric extension.

`resource_type`

(required) Resource type to which Metric Extension applies

`compartment_id`

(required) Compartment Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)

`status`

(required) The current state of the metric extension.

Allowed values are: 'DRAFT', 'PUBLISHED'

`lifecycle_state`

(optional) The current lifecycle state of the metric extension

Allowed values are: 'ACTIVE', 'DELETED'

`time_created`

(optional) Metric Extension creation time. An RFC3339 formatted datetime string

`time_updated`

(optional) Metric Extension updation time. An RFC3339 formatted datetime string

`collection_method`

(optional) Type of possible collection methods.

Allowed values are: 'OS_COMMAND', 'SQL', 'JMX'

`enabled_on_resources_count`

(optional) Count of resources on which this metric extension is enabled.

`resource_uri`

(optional) The URI path that the user can do a GET on to access the metric extension metadata

### DBMS_CLOUD_OCI_STACK_MONITORING_METRIC_EXTENSION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_metric_extension_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_METRIC_EXTENSION_COLLECTION_T Type

Results of a metric extension search. Contains list of MetricExtension items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of metric extensions.

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_T Type

The response object for create monitored resource and get monitored resource operations. This contains information about the monitored resource. Credentials and credential aliases attributes will be returned as null due to security reasons.

Syntax
```

```

Fields

Field Description

`id`

(required) Monitored resource identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`name`

(required) Monitored resource name.

`display_name`

(optional) Monitored resource display name.

`l_type`

(required) Monitored Resource Type.

`compartment_id`

(required) Compartment Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`tenant_id`

(required) Tenancy Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`host_name`

(optional) Monitored resource host name.

`external_id`

(optional) The external resource identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). External resource is any OCI resource which is not a Stack Monitoring service resource. Currently supports only following resource types - Container database, non-container database, pluggable database and OCI compute instance.

`management_agent_id`

(optional) Management Agent Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`resource_time_zone`

(optional) Time zone in the form of tz database canonical zone ID.

`time_created`

(optional) The date and time when the monitored resource was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.

`time_updated`

(optional) The date and time when the monitored resource was last updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.

`lifecycle_state`

(optional) Lifecycle state of the monitored resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`license`

(optional) License edition of the monitored resource.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION'

`properties`

(optional) List of monitored resource properties.

`database_connection_details`

(optional)

`credentials`

(optional)

`aliases`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_ASSOCIATION_T Type

Association details between two monitored resources.

Syntax
```

```

Fields

Field Description

`association_type`

(required) Association Type.

`compartment_id`

(required) Compartment Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`tenant_id`

(required) Tenancy Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`source_resource_id`

(required) Source Monitored Resource Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`destination_resource_id`

(required) Destination Monitored Resource Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`source_resource_details`

(optional)

`destination_resource_details`

(optional)

`time_created`

(optional) The time when the association was created. An RFC3339 formatted datetime string.

`category`

(optional) Association category. Possible values are: - System created (SYSTEM), - User created using API (USER_API) - User created using tags (USER_TAG_ASSOC).

Allowed values are: 'SYSTEM', 'USER_API', 'USER_TAG_ASSOC'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_ASSOCIATION_SUMMARY_T Type

Summary of the monitored resource association.

Syntax
```

```

Fields

Field Description

`association_type`

(required) Association type between source and destination resources.

`source_resource_id`

(required) Source Monitored Resource Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`destination_resource_id`

(required) Destination Monitored Resource Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`time_created`

(optional) The association creation time. An RFC3339 formatted datetime string.

`source_resource_details`

(optional)

`destination_resource_details`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_ASSOCIATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_monitored_resource_association_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_ASSOCIATIONS_COLLECTION_T Type

List of MonitoredResourceAssociationSummary elements.

Syntax
```

```

Fields

Field Description

`items`

(required) List of Monitored Resource Associations.

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_SUMMARY_T Type

The information about monitored resource.

Syntax
```

```

Fields

Field Description

`id`

(required) Monitored resource identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`name`

(required) Monitored Resource Name.

`display_name`

(optional) Monitored resource display name.

`l_type`

(required) Monitored Resource Type.

`compartment_id`

(optional) Compartment Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`host_name`

(optional) Monitored Resource Host Name.

`external_id`

(optional) External resource is any OCI resource identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)which is not a Stack Monitoring service resource.

`management_agent_id`

(optional) Management Agent Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`time_created`

(optional) Monitored resource creation time. An RFC3339 formatted datetime string.

`time_updated`

(optional) Monitored resource update time. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the monitored resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`properties`

(optional) List of monitored resource properties.

`license`

(optional) License edition of the monitored resource.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_monitored_resource_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_COLLECTION_T Type

Results of a resources search. Contains MonitoredResourceSummary items and other data.

Syntax
```

```

Fields

Field Description

`items`

(required) List of monitored resources.

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_MEMBER_SUMMARY_T Type

Monitored resource member details.

Syntax
```

```

Fields

Field Description

`resource_id`

(optional) Monitored resource identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`resource_name`

(optional) Monitored Resource Name.

`resource_display_name`

(optional) Monitored resource display name.

`resource_type`

(optional) Monitored Resource Type.

`host_name`

(optional) Monitored Resource Host Name.

`external_id`

(optional) External resource is any OCI resource identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)which is not a Stack Monitoring service resource. Currently supports only following resource types - Container database, non-container database, pluggable database and OCI compute instance.

`compartment_id`

(optional) Compartment Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`parent_id`

(optional) Parent monitored resource identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`lifecycle_state`

(optional) The current state of the Resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`license`

(optional) License edition of the monitored resource.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_MEMBER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_monitored_resource_member_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_MEMBERS_COLLECTION_T Type

Results of a member search.

Syntax
```

```

Fields

Field Description

`items`

(required) List of member resources.

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_TASK_T Type

The request details for importing resources from Telemetry.

Syntax
```

```

Fields

Field Description

`id`

(required) Task identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`name`

(required) Name of the task.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment identifier.

`tenant_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tenancy.

`task_details`

(required)

`work_request_ids`

(optional) Identifiers[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for work requests submitted for this task.

`time_created`

(optional) The date and time when the stack monitoring resource task was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.

`time_updated`

(optional) The date and time when the stack monitoring resource task was last updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.

`lifecycle_state`

(optional) The current state of the stack monitoring resource task.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'NEEDS_ATTENTION'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_TASK_SUMMARY_T Type

The summary details for the task.

Syntax
```

```

Fields

Field Description

`id`

(required) Task identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`name`

(required) Name of the task.

`task_details`

(required)

`work_request_ids`

(optional) Identifiers[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for work requests submitted for this task.

`time_created`

(optional) The date and time when the stack monitoring resource task was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.

`time_updated`

(optional) The date and time when the stack monitoring resource task was last updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.

`lifecycle_state`

(optional) The current state of the stack monitoring resource task.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'NEEDS_ATTENTION'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_TASK_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_monitored_resource_task_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_TASKS_COLLECTION_T Type

A Collection of stack monitoring resource task summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) List of stack monitoring resource task summaries.

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_TYPE_T Type

The response object for create monitored resource type and get monitored resource type operations.

Syntax
```

```

Fields

Field Description

`id`

(required) Monitored resource type identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`name`

(required) A unique monitored resource type name. The name must be unique across tenancy. Name can not be changed.

`display_name`

(optional) Monitored resource type display name.

`description`

(optional) A friendly description.

`metric_namespace`

(optional) Metric namespace for resource type.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tenancy containing the resource type.

`lifecycle_state`

(optional) Lifecycle state of the monitored resource type.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(optional) The date and time when the monitored resource type was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.

`time_updated`

(optional) The date and time when the monitored resource was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.

`metadata`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_TYPE_SUMMARY_T Type

The summary of monitored resource type.

Syntax
```

```

Fields

Field Description

`id`

(required) Monitored resource type identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`name`

(required) A unique monitored resource type name. The name must be unique across tenancy. Name can not be changed.

`display_name`

(optional) Monitored resource type display name.

`description`

(optional) A friendly description.

`metric_namespace`

(optional) Metric namespace for resource type.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tenancy containing the resource type.

`lifecycle_state`

(optional) Lifecycle state of the monitored resource type.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`metadata`

(optional)

`time_created`

(optional) The date and time when the monitored resource type was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.

`time_updated`

(optional) The date and time when the monitored resource was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_TYPE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_monitored_resource_type_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_TYPES_COLLECTION_T Type

A Collection of monitored resource type summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) List of monitored resource type summaries.

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCES_COUNT_AGGREGATION_T Type

The count of resources for specified dimension.

Syntax
```

```

Fields

Field Description

`dimensions`

(required) Qualifiers provided in a metric definition. Available dimensions vary based on groupBy parameter. Each dimension takes the form of a key-value pair. Example: `\"resourceType\": \"oci_autonomous_database\"`

`l_count`

(required) the value of this metric

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCES_COUNT_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_monitored_resources_count_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCES_COUNT_AGGREGATION_COLLECTION_T Type

The resource count grouped by given criteria.

Syntax
```

```

Fields

Field Description

`items`

(required) The counts related to the resource and resource types.

### DBMS_CLOUD_OCI_STACK_MONITORING_SCRIPT_FILE_DETAILS_T Type

Script details applicable to any OS Command based Metric Extension which needs to run a script to collect data

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the script file

`content`

(required) Content of the script file as base64 encoded string

### DBMS_CLOUD_OCI_STACK_MONITORING_OS_COMMAND_QUERY_PROPERTIES_T Type

Query Properties applicable to OS_COMMAND type of collection method

Syntax
```

```

`dbms_cloud_oci_stack_monitoring_os_command_query_properties_t`is a subtype of the`dbms_cloud_oci_stack_monitoring_metric_extension_query_properties_t`type.

Fields

Field Description

`command`

(required) OS command to execute without arguments

`delimiter`

(required) Character used to delimit multiple metric values in single line of output

`script_details`

(optional)

`arguments`

(optional) Arguments required by either command or script

`starts_with`

(optional) String prefix used to identify metric output of the OS Command

### DBMS_CLOUD_OCI_STACK_MONITORING_OS_COMMAND_UPDATE_QUERY_PROPERTIES_T Type

Query Properties applicable to OS_COMMAND type of collection method

Syntax
```

```

`dbms_cloud_oci_stack_monitoring_os_command_update_query_properties_t`is a subtype of the`dbms_cloud_oci_stack_monitoring_metric_extension_update_query_properties_t`type.

Fields

Field Description

`command`

(optional) OS command to execute without arguments

`delimiter`

(optional) Character used to delimit multiple metric values in single line of output

`script_details`

(optional)

`arguments`

(optional) Arguments required by either command or script

`starts_with`

(optional) String prefix used to identify metric output of the OS Command

### DBMS_CLOUD_OCI_STACK_MONITORING_PLAIN_TEXT_CREDENTIALS_T Type

Plain text credentials [indicated by the type property in CredentialStore].

Syntax
```

```

`dbms_cloud_oci_stack_monitoring_plain_text_credentials_t`is a subtype of the`dbms_cloud_oci_stack_monitoring_monitored_resource_credential_t`type.

Fields

Field Description

`properties`

(required) The credential properties list. Credential property values will be either in plain text format or encrypted for encrypted credentials.

### DBMS_CLOUD_OCI_STACK_MONITORING_PRE_EXISTING_CREDENTIALS_T Type

Pre existing credentials [indicated by the type property in CredentialStore].

Syntax
```

```

`dbms_cloud_oci_stack_monitoring_pre_existing_credentials_t`is a subtype of the`dbms_cloud_oci_stack_monitoring_monitored_resource_credential_t`type.

### DBMS_CLOUD_OCI_STACK_MONITORING_SEARCH_ASSOCIATED_RESOURCES_DETAILS_T Type

The criteria for searching associated monitored resources.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) Compartment Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`resource_type`

(optional) A filter to return associated resources that match resources of type. Either resourceId or resourceType should be provided.

`resource_id`

(optional) Monitored resource identifier for which the associated resources should be fetched. Either resourceId or resourceType should be provided.

`limit_level`

(optional) The field which determines the depth of hierarchy while searching for associated resources. Possible values - 0 for all levels. And positive number to indicate different levels. Default value is 1, which indicates 1st level associations.

`association_types`

(optional) Association types filter to be searched for finding associated resources.

### DBMS_CLOUD_OCI_STACK_MONITORING_SEARCH_MONITORED_RESOURCE_ASSOCIATIONS_DETAILS_T Type

The information required to search monitored resource associations.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) Compartment Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`source_resource_id`

(optional) Source Monitored Resource Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`source_resource_name`

(optional) Source Monitored Resource Name.

`source_resource_type`

(optional) Source Monitored Resource Type.

`destination_resource_id`

(optional) Destination Monitored Resource Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`destination_resource_name`

(optional) Source Monitored Resource Name.

`destination_resource_type`

(optional) Source Monitored Resource Type.

`association_type`

(optional) Association type filter to search associated resources.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for assocType is descending.

Allowed values are: 'TIME_CREATED', 'ASSOC_TYPE'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

### DBMS_CLOUD_OCI_STACK_MONITORING_SEARCH_MONITORED_RESOURCE_MEMBERS_DETAILS_T Type

The search criteria for listing monitored resource member targets.

Syntax
```

```

Fields

Field Description

`destination_resource_id`

(optional) Destination Monitored Resource Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit_level`

(optional) The field which determines the depth of hierarchy while searching for members.

### DBMS_CLOUD_OCI_STACK_MONITORING_SEARCH_MONITORED_RESOURCES_DETAILS_T Type

The property search criteria for listing monitored resources.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) Compartment Identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`name`

(optional) A filter to return resources that match exact resource name.

`name_contains`

(optional) A filter to return resources that match resource name pattern given. The match is not case sensitive.

`l_type`

(optional) A filter to return resources that match resource type.

`host_name`

(optional) A filter to return resources with host name match.

`external_id`

(optional) External resource is any OCI resource identifier[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)which is not a Stack Monitoring service resource. Currently supports only following resource types - Container database, non-container database, pluggable database and OCI compute instance.

`host_name_contains`

(optional) A filter to return resources with host name pattern.

`management_agent_id`

(optional) A filter to return resources with matching management agent id.

`lifecycle_state`

(optional) A filter to return resources with matching lifecycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`license`

(optional) License edition of the monitored resource.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION'

`time_created_greater_than_or_equal_to`

(optional) Search for resources that were created within a specific date range, using this parameter to specify the earliest creation date for the returned list (inclusive). Specifying this parameter without the corresponding `timeCreatedLessThan` parameter will retrieve resources created from the given `timeCreatedGreaterThanOrEqualTo` to the current time, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by[RFC 3339](https://tools.ietf.org/html/rfc3339). **Example:** 2016-12-19T16:39:57.600Z

`time_created_less_than`

(optional) Search for resources that were created within a specific date range, using this parameter to specify the latest creation date for the returned list (exclusive). Specifying this parameter without the corresponding `timeCreatedGreaterThanOrEqualTo` parameter will retrieve all resources created before the specified end date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by[RFC 3339](https://tools.ietf.org/html/rfc3339). **Example:** 2016-12-19T16:39:57.600Z

`time_updated_greater_than_or_equal_to`

(optional) Search for resources that were updated within a specific date range, using this parameter to specify the earliest update date for the returned list (inclusive). Specifying this parameter without the corresponding `timeUpdatedLessThan` parameter will retrieve resources updated from the given `timeUpdatedGreaterThanOrEqualTo` to the current time, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by[RFC 3339](https://tools.ietf.org/html/rfc3339). **Example:** 2016-12-19T16:39:57.600Z

`time_updated_less_than`

(optional) Search for resources that were updated within a specific date range, using this parameter to specify the latest creation date for the returned list (exclusive). Specifying this parameter without the corresponding `timeUpdatedGreaterThanOrEqualTo` parameter will retrieve all resources updated before the specified end date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by[RFC 3339](https://tools.ietf.org/html/rfc3339). **Example:** 2016-12-19T16:39:57.600Z

`resource_time_zone`

(optional) Time zone in the form of tz database canonical zone ID. Specifies the preference with a value that uses the IANA Time Zone Database format (x-obmcs-time-zone). For example - America/Los_Angeles

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for resources is ascending.

Allowed values are: 'TIME_CREATED', 'RESOURCE_NAME'

`property_equals`

(optional) Criteria based on resource property.

### DBMS_CLOUD_OCI_STACK_MONITORING_SQL_DETAILS_T Type

Details of Sql content which needs to execute to collect Metric Extension data

Syntax
```

```

Fields

Field Description

`script_file_name`

(optional) If a script needs to be executed, then provide file name of the script

`content`

(required) Sql statement or script file content as base64 encoded string

### DBMS_CLOUD_OCI_STACK_MONITORING_SQL_IN_PARAM_DETAILS_T Type

Position and value for an IN parameter of PL/SQL statement

Syntax
```

```

Fields

Field Description

`in_param_position`

(required) Position of IN parameter

`in_param_value`

(required) Value of IN parameter

### DBMS_CLOUD_OCI_STACK_MONITORING_SQL_OUT_PARAM_DETAILS_T Type

Position and SQL Type of PL/SQL OUT parameter

Syntax
```

```

Fields

Field Description

`out_param_position`

(required) Position of PL/SQL procedure OUT parameter

`out_param_type`

(required) SQL Type of PL/SQL procedure OUT parameter

Allowed values are: 'SQL_CURSOR', 'ARRAY'

### DBMS_CLOUD_OCI_STACK_MONITORING_SQL_IN_PARAM_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_sql_in_param_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_SQL_QUERY_PROPERTIES_T Type

Query Properties applicable to SQL type of collection method

Syntax
```

```

`dbms_cloud_oci_stack_monitoring_sql_query_properties_t`is a subtype of the`dbms_cloud_oci_stack_monitoring_metric_extension_query_properties_t`type.

Fields

Field Description

`sql_type`

(required) Type of SQL data collection method i.e. either a Statement or SQL Script File

Allowed values are: 'STATEMENT', 'SQL_SCRIPT'

`sql_details`

(required)

`in_param_details`

(optional) List of values and position of PL/SQL procedure IN parameters

`out_param_details`

(optional)

### DBMS_CLOUD_OCI_STACK_MONITORING_SQL_UPDATE_QUERY_PROPERTIES_T Type

Query Properties applicable to SQL type of collection method

Syntax
```

```

`dbms_cloud_oci_stack_monitoring_sql_update_query_properties_t`is a subtype of the`dbms_cloud_oci_stack_monitoring_metric_extension_update_query_properties_t`type.

Fields

Field Description

`sql_type`

(optional) Type of SQL data collection method i.e. either a Statement or SQL Script File

Allowed values are: 'STATEMENT', 'SQL_SCRIPT'

`sql_details`

(optional)

`in_param_details`

(optional) List of values and position of PL/SQL procedure IN parameters

`out_param_details`

(optional)

### DBMS_CLOUD_OCI_STACK_MONITORING_UNIQUE_PROPERTY_SET_T Type

List of properties.

Syntax
```

```

Fields

Field Description

`properties`

(required) List of properties.

### DBMS_CLOUD_OCI_STACK_MONITORING_UNIQUE_PROPERTY_SET_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_unique_property_set_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_SYSTEM_FORMAT_RESOURCE_TYPE_METADATA_DETAILS_T Type

The resource type metadata is defined in machine friendly format.

Syntax
```

```

`dbms_cloud_oci_stack_monitoring_system_format_resource_type_metadata_details_t`is a subtype of the`dbms_cloud_oci_stack_monitoring_resource_type_metadata_details_t`type.

Fields

Field Description

`required_properties`

(optional) List of required properties for resource type.

`agent_properties`

(optional) List of properties needed by the agent for monitoring the resource. Valid only if resource type is OCI management agent based. When specified, these properties are passed to the management agent during resource create or update.

`valid_properties_for_create`

(optional) List of valid properties for resource type while creating the monitored resource. If resources of this type specifies any other properties during create operation, the operation will fail.

`valid_properties_for_update`

(optional) List of valid properties for resource type while updating the monitored resource. If resources of this type specifies any other properties during update operation, the operation will fail.

`unique_property_sets`

(optional) List of property sets used to uniquely identify the resources. This check is made during create or update of stack monitoring resource. The resource has to pass unique check for each set in the list. For example, database can have user, password and SID as one unique set. Another unique set would be user, password and service name.

`valid_property_values`

(optional) List of valid values for the properties. This is useful when resource type wants to restrict only certain values for some properties. For instance for 'osType' property, supported values can be restricted to be either Linux or Windows. Example: `{ \"osType\": [\"Linux\",\"Windows\",\"Solaris\"]}`

### DBMS_CLOUD_OCI_STACK_MONITORING_TEST_METRIC_EXTENSION_DATA_T Type

The Test result details

Syntax
```

```

Fields

Field Description

`test_run_id`

(required) Test Run Id

`test_run_metric_suffix`

(required) Test Run Metric Suffix

`test_run_namespace_name`

(required) Test Run Namespace name

`test_run_resource_group_name`

(optional) Test Run Resource Group name

### DBMS_CLOUD_OCI_STACK_MONITORING_TEST_METRIC_EXTENSION_DETAILS_T Type

The resource Id on which test will be run

Syntax
```

```

Fields

Field Description

`resource_ids`

(required) List of Resource IDs [OCID]. Currently supports only one resource id per request.

### DBMS_CLOUD_OCI_STACK_MONITORING_UPDATE_AND_PROPAGATE_TAGS_DETAILS_T Type

The information about monitored resource tags. Request will fail if at least one of freeformTags or definedTags are not specified. Provided tags will be added or updated in the existing list of tags for the affected resources. Resources to be updated are identified based on association types specified. If association types are not specified, then tags will be updated only for the current resource.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`association_types`

(optional) Association types that will be traversed recursively starting from the current resource, to identify resources for which the tags will be updated. If no association type is specified, only current resource will be updated. Default is empty list, which means no related resources will be updated.

### DBMS_CLOUD_OCI_STACK_MONITORING_UPDATE_CONFIG_DETAILS_T Type

Change the configuration.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The display name of the configuration.

`config_type`

(optional) The type of configuration.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_UPDATE_AUTO_PROMOTE_CONFIG_DETAILS_T Type

Change the details of an AUTO_PROMOTE config

Syntax
```

```

`dbms_cloud_oci_stack_monitoring_update_auto_promote_config_details_t`is a subtype of the`dbms_cloud_oci_stack_monitoring_update_config_details_t`type.

Fields

Field Description

`is_enabled`

(optional) True if automatic promotion is enabled, false if it is not enabled.

### DBMS_CLOUD_OCI_STACK_MONITORING_UPDATE_BASELINEABLE_METRIC_DETAILS_T Type

Summary for the baseline-able metric

Syntax
```

```

Fields

Field Description

`id`

(required) OCID of the metric

`lifecycle_state`

(optional) The current lifecycle state of the metric extension

Allowed values are: 'ACTIVE', 'DELETED'

`tenancy_id`

(optional) OCID of the tenancy

`compartment_id`

(optional) OCID of the compartment

`name`

(required) name of the metric

`l_column`

(required) metric column name

`namespace`

(required) namespace of the metric

`resource_group`

(required) Resource group of the metric

`is_out_of_box`

(required) Is the metric created out of box, default false

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_UPDATE_LICENSE_AUTO_ASSIGN_CONFIG_DETAILS_T Type

Change the details of a LICENSE_AUTO_ASSIGN configuration.

Syntax
```

```

`dbms_cloud_oci_stack_monitoring_update_license_auto_assign_config_details_t`is a subtype of the`dbms_cloud_oci_stack_monitoring_update_config_details_t`type.

Fields

Field Description

`license`

(optional) License edition.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION'

### DBMS_CLOUD_OCI_STACK_MONITORING_UPDATE_LICENSE_ENTERPRISE_EXTENSIBILITY_CONFIG_DETAILS_T Type

Change the details of a LICENSE_ENTERPRISE_EXTENSIBILITY configuration.

Syntax
```

```

`dbms_cloud_oci_stack_monitoring_update_license_enterprise_extensibility_config_details_t`is a subtype of the`dbms_cloud_oci_stack_monitoring_update_config_details_t`type.

Fields

Field Description

`is_enabled`

(optional) True if enterprise extensibility is enabled, false if it is not enabled.

### DBMS_CLOUD_OCI_STACK_MONITORING_UPDATE_METRIC_EXTENSION_DETAILS_T Type

The information about updating a metric extension resource

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Metric Extension resource display name.

`description`

(optional) Description of the metric extension.

`collection_recurrences`

(optional) Schedule of metric extension should use RFC 5545 format -&gt; recur-rule-part = \"FREQ\";\"INTERVAL\" where FREQ rule part identifies the type of recurrence rule. Valid values are \"MINUTELY\",\"HOURLY\",\"DAILY\" to specify repeating events based on an interval of a minute, an hour and a day or more. Example- FREQ=DAILY;INTERVAL=1

`metric_list`

(optional) List of metrics which are part of this metric extension

`query_properties`

(optional)

### DBMS_CLOUD_OCI_STACK_MONITORING_UPDATE_MONITORED_RESOURCE_DETAILS_T Type

The information about updating a monitored resource.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Monitored resource display name.

`host_name`

(optional) Host name of the monitored resource.

`resource_time_zone`

(optional) Time zone in the form of tz database canonical zone ID. Specifies the preference with a value that uses the IANA Time Zone Database format (x-obmcs-time-zone). For example - America/Los_Angeles

`properties`

(optional) List of monitored resource properties.

`database_connection_details`

(optional)

`credentials`

(optional)

`aliases`

(optional)

`additional_credentials`

(optional) List of MonitoredResourceCredentials. This property complements the existing \"credentials\" property by allowing user to specify more than one credential. If both \"credential\" and \"additionalCredentials\" are specified, union of the values is used as list of credentials applicable for this resource. If any duplicate found in the combined list of \"credentials\" and \"additionalCredentials\", an error will be thrown.

`additional_aliases`

(optional) List of MonitoredResourceAliasCredentials. This property complements the existing \"aliases\" property by allowing user to specify more than one credential alias. If both \"aliases\" and \"additionalAliases\" are specified, union of the values is used as list of aliases applicable for this resource. If any duplicate found in the combined list of \"alias\" and \"additionalAliases\", an error will be thrown.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_UPDATE_MONITORED_RESOURCE_TASK_DETAILS_T Type

The request details for the stack monitoring resource task.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_UPDATE_MONITORED_RESOURCE_TYPE_DETAILS_T Type

The information to be updated for the monitored resource type.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Monitored resource type display name.

`description`

(optional) A friendly description.

`metric_namespace`

(optional) Metric namespace for resource type.

`metadata`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_STACK_MONITORING_WORK_REQUEST_RESOURCE_T Type

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

### DBMS_CLOUD_OCI_STACK_MONITORING_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_WORK_REQUEST_T Type

A description of workrequest status

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_RESOURCES', 'UPDATE_RESOURCES', 'DELETE_RESOURCES', 'MOVE_RESOURCES', 'ENABLE_EXTERNAL_DATABASE', 'DISABLE_EXTERNAL_DATABASE', 'ADD_SOURCES_TO_AGENT', 'ENABLE_METRIC_EXTENSION', 'DISABLE_METRIC_EXTENSION', 'TEST_METRIC_EXTENSION', 'BULK_ADD_RESOURCES', 'BULK_DELETE_RESOURCES', 'UPDATE_AND_PROPAGATE_TAGS', 'IMPORT_RESOURCES'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The id of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used.

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

### DBMS_CLOUD_OCI_STACK_MONITORING_WORK_REQUEST_ERROR_T Type

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

### DBMS_CLOUD_OCI_STACK_MONITORING_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestError objects.

### DBMS_CLOUD_OCI_STACK_MONITORING_WORK_REQUEST_LOG_ENTRY_T Type

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

### DBMS_CLOUD_OCI_STACK_MONITORING_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a workRequestLog search. Contains both workRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestLogEntries.

### DBMS_CLOUD_OCI_STACK_MONITORING_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_RESOURCES', 'UPDATE_RESOURCES', 'DELETE_RESOURCES', 'MOVE_RESOURCES', 'ENABLE_EXTERNAL_DATABASE', 'DISABLE_EXTERNAL_DATABASE', 'ADD_SOURCES_TO_AGENT', 'ENABLE_METRIC_EXTENSION', 'DISABLE_METRIC_EXTENSION', 'TEST_METRIC_EXTENSION', 'BULK_ADD_RESOURCES', 'BULK_DELETE_RESOURCES', 'UPDATE_AND_PROPAGATE_TAGS', 'IMPORT_RESOURCES'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

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

### DBMS_CLOUD_OCI_STACK_MONITORING_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_stack_monitoring_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STACK_MONITORING_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestSummary objects.

- [Stack Monitoring Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-562D3272-719A-4516-8A4C-C9AAD5B9EF93)
- [DBMS_CLOUD_OCI_STACK_MONITORING_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-DFAEC283-B0F2-453B-861C-D4E600555429)
- [DBMS_CLOUD_OCI_STACK_MONITORING_ANOMALY_DATA_POINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-C51E3970-2DC3-4C3A-A020-09E4615482C2)
- [DBMS_CLOUD_OCI_STACK_MONITORING_ANOMALY_DATA_POINT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-BB83C870-D097-4648-BBE8-BCBD6F66B813)
- [DBMS_CLOUD_OCI_STACK_MONITORING_ANOMALY_METRIC_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-68986950-796F-4AE8-BA58-D046B1C99E33)
- [DBMS_CLOUD_OCI_STACK_MONITORING_ASSOCIATE_MONITORED_RESOURCES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-95C7E07E-3E67-49CB-8A6C-7E73139904C8)
- [DBMS_CLOUD_OCI_STACK_MONITORING_ASSOCIATED_MONITORED_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-872B7921-9B8D-46D8-924B-3A2D653283A2)
- [DBMS_CLOUD_OCI_STACK_MONITORING_ASSOCIATED_MONITORED_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-1C8C551C-5566-4822-8CB3-126B54A7A1C6)
- [DBMS_CLOUD_OCI_STACK_MONITORING_ASSOCIATED_RESOURCES_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-A5A0E1C1-E31E-4321-B73F-700C07F9A658)
- [DBMS_CLOUD_OCI_STACK_MONITORING_ASSOCIATED_RESOURCES_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-F29D5FF8-96AD-4ED6-85B0-40EC53248C56)
- [DBMS_CLOUD_OCI_STACK_MONITORING_ASSOCIATED_RESOURCES_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-9937349D-9E13-4B77-B942-781028049326)
- [DBMS_CLOUD_OCI_STACK_MONITORING_ASSOCIATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-5CDE0ECC-8547-4857-9A8F-74ECA16DD485)
- [DBMS_CLOUD_OCI_STACK_MONITORING_ASSOCIATION_RESOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-FA4EF98C-F2C0-4850-8A97-A3EEFDA89F93)
- [DBMS_CLOUD_OCI_STACK_MONITORING_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-CA58B3C1-6503-457E-85AA-70FA4D7A5851)
- [DBMS_CLOUD_OCI_STACK_MONITORING_AUTO_PROMOTE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-CC584E6C-6669-4435-8951-A328A4827CA8)
- [DBMS_CLOUD_OCI_STACK_MONITORING_CONFIG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-137CB674-1768-4EA0-AF48-8A616DB89BC5)
- [DBMS_CLOUD_OCI_STACK_MONITORING_AUTO_PROMOTE_CONFIG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-D4223FFA-298D-4268-AB37-24B45EAEC937)
- [DBMS_CLOUD_OCI_STACK_MONITORING_BASELINEABLE_METRIC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-612CFC32-A9BF-41B6-9428-3B3CE50C2A6B)
- [DBMS_CLOUD_OCI_STACK_MONITORING_BASELINEABLE_METRIC_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-DEB91D47-AB2B-4908-8FDC-6269B47F7F08)
- [DBMS_CLOUD_OCI_STACK_MONITORING_BASELINEABLE_METRIC_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-3E0ED9EB-3AE1-45DC-976F-CEC6F03DCF6F)
- [DBMS_CLOUD_OCI_STACK_MONITORING_BASELINEABLE_METRIC_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-762D8197-54DF-4CAC-B53E-6DFF326FDB03)
- [DBMS_CLOUD_OCI_STACK_MONITORING_CHANGE_CONFIG_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-A716561F-B68F-4E45-BDA1-60BC725E9878)
- [DBMS_CLOUD_OCI_STACK_MONITORING_CHANGE_METRIC_EXTENSION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-F69642AB-6EE7-4648-A1BE-8E675765C172)
- [DBMS_CLOUD_OCI_STACK_MONITORING_CHANGE_MONITORED_RESOURCE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-87EDF69D-7DD6-45EB-A9DA-D59083966CF4)
- [DBMS_CLOUD_OCI_STACK_MONITORING_CHANGE_MONITORED_RESOURCE_TASK_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-7FC2FAFD-E1F8-4441-B7EE-27A2449806DF)
- [DBMS_CLOUD_OCI_STACK_MONITORING_CONFIG_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-8D892CD9-ABB7-4700-95E8-61ED3EE7B5AE)
- [DBMS_CLOUD_OCI_STACK_MONITORING_CONFIG_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-279B461B-461D-48AD-B942-50B439152D36)
- [DBMS_CLOUD_OCI_STACK_MONITORING_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-97C570F0-8BF2-494A-90D2-7F4B2FF6E4D9)
- [DBMS_CLOUD_OCI_STACK_MONITORING_CREATE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-B1C7B396-6350-493E-B96C-1435DEE600D9)
- [DBMS_CLOUD_OCI_STACK_MONITORING_CREATE_AUTO_PROMOTE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-A6D7138D-B1F9-4B64-84BA-2F92FA7894CB)
- [DBMS_CLOUD_OCI_STACK_MONITORING_CREATE_BASELINEABLE_METRIC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-783111D0-CFFB-4E9C-A553-C83DE94EC8CD)
- [DBMS_CLOUD_OCI_STACK_MONITORING_PROPERTY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-FA0BC3A6-C6B0-4D87-AE19-91FFF3731A85)
- [DBMS_CLOUD_OCI_STACK_MONITORING_CREDENTIAL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-84B346F7-8587-43AA-8D38-556D5A03FEAB)
- [DBMS_CLOUD_OCI_STACK_MONITORING_CREDENTIAL_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-DF7AF30B-98D5-4A5F-ABEA-BDF3F9D0424C)
- [DBMS_CLOUD_OCI_STACK_MONITORING_CREDENTIAL_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-14E52A31-A2EF-43AB-9AC4-8ABD66E7973D)
- [DBMS_CLOUD_OCI_STACK_MONITORING_DISCOVERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-81DD5D1B-EFB7-47B8-B417-7EAD48EFFBBD)
- [DBMS_CLOUD_OCI_STACK_MONITORING_CREATE_DISCOVERY_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-17115424-E564-45DC-8B74-019AF47AD444)
- [DBMS_CLOUD_OCI_STACK_MONITORING_CREATE_LICENSE_AUTO_ASSIGN_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-C92B1E80-6527-455A-A376-259DA037301F)
- [DBMS_CLOUD_OCI_STACK_MONITORING_CREATE_LICENSE_ENTERPRISE_EXTENSIBILITY_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-DEE6241D-247B-4DEF-B1DB-E89CB542E933)
- [DBMS_CLOUD_OCI_STACK_MONITORING_METRIC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-53BE8F84-4A02-40CF-A471-6D23C0E28DD5)
- [DBMS_CLOUD_OCI_STACK_MONITORING_METRIC_EXTENSION_QUERY_PROPERTIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-560C2B71-DEA7-417E-8046-48B8521304EA)
- [DBMS_CLOUD_OCI_STACK_MONITORING_METRIC_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-B8F6F1E4-7D29-49F9-8214-FB7AE9345A09)
- [DBMS_CLOUD_OCI_STACK_MONITORING_CREATE_METRIC_EXTENSION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-89E72995-D4D4-406E-9C68-2B7998FDC6FF)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_PROPERTY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-4E721E11-CDEE-42DB-A83C-2CC922A0E93E)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_CREDENTIAL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-15DAB96B-46A5-468D-AD64-22EB66BB2BB3)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_ALIAS_SOURCE_CREDENTIAL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-47694CBB-87D1-436F-8305-8AA9B165F0A4)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_ALIAS_CREDENTIAL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-A310D160-009F-4848-B202-F7AB2082C6ED)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_PROPERTY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-59D4B953-B57C-4DF9-99D2-596785400945)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_CREDENTIAL_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-2926CFCE-CB9E-4490-B1F5-BBC3839DF0BC)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_ALIAS_CREDENTIAL_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-57748C78-624A-46C9-80C7-3ECB16B22A36)
- [DBMS_CLOUD_OCI_STACK_MONITORING_CREATE_MONITORED_RESOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-41BA9E84-4C02-42D9-9AAB-CE5C20AB582D)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_TASK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-2C703456-E0D3-4D12-87C2-BD1DCADD24D0)
- [DBMS_CLOUD_OCI_STACK_MONITORING_CREATE_MONITORED_RESOURCE_TASK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-C492F2AC-3ECE-4B69-AC40-E88D8F68BCF9)
- [DBMS_CLOUD_OCI_STACK_MONITORING_RESOURCE_TYPE_METADATA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-A9F88F9B-B907-45F5-A54D-488C8CBF047E)
- [DBMS_CLOUD_OCI_STACK_MONITORING_CREATE_MONITORED_RESOURCE_TYPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-72388BAB-B5AA-4712-8CB4-8541B91A1B7C)
- [DBMS_CLOUD_OCI_STACK_MONITORING_CREDENTIAL_PROPERTY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-1D1646B5-8D58-4123-8105-607195644EF7)
- [DBMS_CLOUD_OCI_STACK_MONITORING_DATA_POINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-D59D907F-8CC9-45D9-9A2A-8EE95A7E611D)
- [DBMS_CLOUD_OCI_STACK_MONITORING_DISABLE_METRIC_EXTENSION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-E8221AC0-7AE7-4DE2-80F2-CE1A7321BDF0)
- [DBMS_CLOUD_OCI_STACK_MONITORING_DISASSOCIATE_MONITORED_RESOURCES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-5788E365-A2E9-4808-BDE4-5EEA39C105AB)
- [DBMS_CLOUD_OCI_STACK_MONITORING_DISCOVERY_JOB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-8910A2A0-F7B6-40B3-9157-9A085434B573)
- [DBMS_CLOUD_OCI_STACK_MONITORING_DISCOVERY_JOB_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-D24AECC4-BE66-4780-BE47-FAF5C93DC277)
- [DBMS_CLOUD_OCI_STACK_MONITORING_DISCOVERY_JOB_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-A02118AA-F524-467E-9C8C-AD03DA856398)
- [DBMS_CLOUD_OCI_STACK_MONITORING_DISCOVERY_JOB_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-334B00A8-9E66-443A-94F8-637A7ACBD6F4)
- [DBMS_CLOUD_OCI_STACK_MONITORING_DISCOVERY_JOB_LOG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-59520F1C-87F1-42AB-993E-DFA7A7B4B688)
- [DBMS_CLOUD_OCI_STACK_MONITORING_DISCOVERY_JOB_LOG_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-D6A5A89B-D0CA-48B4-AD2F-3F9E3F16C92A)
- [DBMS_CLOUD_OCI_STACK_MONITORING_DISCOVERY_JOB_LOG_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-3C9954A7-BCD2-4B2C-877B-26DCF590DC71)
- [DBMS_CLOUD_OCI_STACK_MONITORING_ENABLE_METRIC_EXTENSION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-9C0C7F3B-7657-405F-8F64-3A109FC91F16)
- [DBMS_CLOUD_OCI_STACK_MONITORING_ENABLED_RESOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-18F47370-EC7D-4D37-9CBD-F7FE4931660B)
- [DBMS_CLOUD_OCI_STACK_MONITORING_CREDENTIAL_PROPERTY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-931D752D-7B3F-499D-8C7C-BB25C55C01E9)
- [DBMS_CLOUD_OCI_STACK_MONITORING_ENCRYPTED_CREDENTIALS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-92D3DE15-EF47-49C2-B1E7-CA61B25D61D6)
- [DBMS_CLOUD_OCI_STACK_MONITORING_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-A3F56A97-2259-4F29-AF01-CDCAB7956DE7)
- [DBMS_CLOUD_OCI_STACK_MONITORING_DATA_POINT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-C537374F-3372-4C93-B965-B818DA99B6D2)
- [DBMS_CLOUD_OCI_STACK_MONITORING_METRIC_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-22ACA1CC-5A5C-43C5-AA32-BF477D71B168)
- [DBMS_CLOUD_OCI_STACK_MONITORING_METRIC_DATA_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-31AC2656-3AD6-4FC6-AF38-91264905CFEE)
- [DBMS_CLOUD_OCI_STACK_MONITORING_EVALUATE_BASELINEABLE_METRIC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-7DBB5FB5-76E3-42DC-AE4A-1062AB57498D)
- [DBMS_CLOUD_OCI_STACK_MONITORING_ANOMALY_METRIC_DATA_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-450D6469-E97B-4E55-BF29-0E419AB69831)
- [DBMS_CLOUD_OCI_STACK_MONITORING_EVALUATE_BASELINEABLE_METRIC_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-048540FB-B998-41EB-B031-08DB1FA4B098)
- [DBMS_CLOUD_OCI_STACK_MONITORING_IMPORT_OCI_TELEMETRY_RESOURCES_TASK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-C2CD0289-D095-4D86-BBBF-F69B3399B22B)
- [DBMS_CLOUD_OCI_STACK_MONITORING_JMX_QUERY_PROPERTIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-124F9AFD-4426-414E-9996-1F688BC1D627)
- [DBMS_CLOUD_OCI_STACK_MONITORING_METRIC_EXTENSION_UPDATE_QUERY_PROPERTIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-E9DAB403-2C86-4000-82EF-2FCDA3985176)
- [DBMS_CLOUD_OCI_STACK_MONITORING_JMX_UPDATE_QUERY_PROPERTIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-3B5C554F-B532-422A-AE4C-FE2ECC70D0CC)
- [DBMS_CLOUD_OCI_STACK_MONITORING_LICENSE_AUTO_ASSIGN_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-D2A89075-EDD1-4ACF-B438-03DE2771F830)
- [DBMS_CLOUD_OCI_STACK_MONITORING_LICENSE_AUTO_ASSIGN_CONFIG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-3C68E094-1CC9-47AF-ADCC-5B3037068336)
- [DBMS_CLOUD_OCI_STACK_MONITORING_LICENSE_ENTERPRISE_EXTENSIBILITY_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-DE0FF777-6DFD-4B4D-8EED-EAFA64F25A0C)
- [DBMS_CLOUD_OCI_STACK_MONITORING_LICENSE_ENTERPRISE_EXTENSIBILITY_CONFIG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-F3E18EC1-81DD-4D56-82CF-596C4D7D4840)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MANAGE_LICENSE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-5A17BBB1-42A7-4AF1-A0CA-EE94CC2BBD28)
- [DBMS_CLOUD_OCI_STACK_MONITORING_ENABLED_RESOURCE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-28AFD5C1-2C2C-462F-8D85-6CD37A88CDFA)
- [DBMS_CLOUD_OCI_STACK_MONITORING_METRIC_EXTENSION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-487CC8CB-4061-414C-A14A-5C93D7446066)
- [DBMS_CLOUD_OCI_STACK_MONITORING_METRIC_EXTENSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-F25B514F-9DD4-4C87-B24A-B71F1BF38C42)
- [DBMS_CLOUD_OCI_STACK_MONITORING_METRIC_EXTENSION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-C785AB91-F477-479F-8C51-D16E735CB9C6)
- [DBMS_CLOUD_OCI_STACK_MONITORING_METRIC_EXTENSION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-B77670EE-06B5-4F70-B071-287D75BC6EE4)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-7808C30B-6D28-4A38-859E-B711D46AB9B8)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_ASSOCIATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-6F760A32-E660-428F-95F6-424A6CF7E237)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_ASSOCIATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-308CB0F0-09E9-4B69-AD7B-76637745DC8B)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_ASSOCIATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-7C64ABDB-6014-42ED-9844-E4339268ED94)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_ASSOCIATIONS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-F11512BD-8EEB-487D-B77B-8A716D23388E)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-357895E4-619B-4DC1-BA4E-DA494FDB3CF1)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-CDB1503E-ADF2-41E3-A5FB-620F37A3D4CD)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-1A0D7919-6EE0-40F2-A6EA-9CA3A4520F21)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_MEMBER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-364A1244-3CCD-4AEE-AFF0-739A9A8400B3)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_MEMBER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-33B888BB-B318-4F44-9F97-5F5B743EF900)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_MEMBERS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-A11D9015-C8C9-4FC6-B06C-2B4CE4B36744)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-3F3A7800-1D33-475A-8120-EAA59948E567)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_TASK_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-DC13014B-39CC-4F00-8033-93AA52B46C1F)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_TASK_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-E47E6957-79CA-48AA-B347-37F8B64C51FC)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_TASKS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-A7A14526-E2B9-4B5E-BDB6-ED512C586C92)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-EA86ED3A-C7B8-46CC-9046-5954A0566BF3)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_TYPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-99D8C77E-581D-41F3-96DF-87E95BB41430)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_TYPE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-199A2BF1-8CCC-4EAE-A9C0-67EB5572CA60)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCE_TYPES_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-0A7565B5-4242-4446-A8E2-A69D4D7EB701)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCES_COUNT_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-B547A566-F0B4-4408-A49E-B582FB6059FA)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCES_COUNT_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-E5A7F184-5F62-46F2-9BB3-4CDA5C16AC3D)
- [DBMS_CLOUD_OCI_STACK_MONITORING_MONITORED_RESOURCES_COUNT_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-83BCC7B3-0368-41C5-81FC-7BF54D29EEAE)
- [DBMS_CLOUD_OCI_STACK_MONITORING_SCRIPT_FILE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-597C35C0-9754-401A-97ED-1962E91366AD)
- [DBMS_CLOUD_OCI_STACK_MONITORING_OS_COMMAND_QUERY_PROPERTIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-3907023C-D95E-4CF2-A818-9FA6B23B8FC5)
- [DBMS_CLOUD_OCI_STACK_MONITORING_OS_COMMAND_UPDATE_QUERY_PROPERTIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-59DBBB95-9A83-4437-A916-95098F1C85B9)
- [DBMS_CLOUD_OCI_STACK_MONITORING_PLAIN_TEXT_CREDENTIALS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-00BA5BDD-2BBC-4E4F-9442-57BCF2A9EAFF)
- [DBMS_CLOUD_OCI_STACK_MONITORING_PRE_EXISTING_CREDENTIALS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-3953A30E-4BC3-4304-AC18-415E29B6890A)
- [DBMS_CLOUD_OCI_STACK_MONITORING_SEARCH_ASSOCIATED_RESOURCES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-07F669BC-8363-443C-B1F6-C7ED28C3F3C2)
- [DBMS_CLOUD_OCI_STACK_MONITORING_SEARCH_MONITORED_RESOURCE_ASSOCIATIONS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-92E6E8C3-35DB-48C3-95E3-F7EB3A014386)
- [DBMS_CLOUD_OCI_STACK_MONITORING_SEARCH_MONITORED_RESOURCE_MEMBERS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-24480CB4-805A-4C4F-ABA0-4C9B341A1A47)
- [DBMS_CLOUD_OCI_STACK_MONITORING_SEARCH_MONITORED_RESOURCES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-246B2C6F-A0B9-41F0-B0D5-99E3CECFAA17)
- [DBMS_CLOUD_OCI_STACK_MONITORING_SQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-8C042D57-4FDA-4939-A0B0-0597FE33E8AE)
- [DBMS_CLOUD_OCI_STACK_MONITORING_SQL_IN_PARAM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-927B0597-4BA3-4E07-A432-93BD3FFE83CD)
- [DBMS_CLOUD_OCI_STACK_MONITORING_SQL_OUT_PARAM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-A39E9463-D5A0-4A8C-B0A0-7AB83AB47FED)
- [DBMS_CLOUD_OCI_STACK_MONITORING_SQL_IN_PARAM_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-8AEA647E-C847-4726-BB21-41DAC4DD5D8B)
- [DBMS_CLOUD_OCI_STACK_MONITORING_SQL_QUERY_PROPERTIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-5C065C2F-A621-45DE-8346-DCA96784B512)
- [DBMS_CLOUD_OCI_STACK_MONITORING_SQL_UPDATE_QUERY_PROPERTIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-ADD94DCD-F8E2-444F-BDC6-D8E5F7FCE11C)
- [DBMS_CLOUD_OCI_STACK_MONITORING_UNIQUE_PROPERTY_SET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-883FCA63-B47B-4F1E-9574-471476ECB862)
- [DBMS_CLOUD_OCI_STACK_MONITORING_UNIQUE_PROPERTY_SET_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-3F6DF3A0-DD8C-496C-AD14-58F01EBFC588)
- [DBMS_CLOUD_OCI_STACK_MONITORING_SYSTEM_FORMAT_RESOURCE_TYPE_METADATA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-822EB670-B43F-474E-AE28-A4C7B372998D)
- [DBMS_CLOUD_OCI_STACK_MONITORING_TEST_METRIC_EXTENSION_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-951D6BB8-66A0-469E-B2DD-72036D9B3507)
- [DBMS_CLOUD_OCI_STACK_MONITORING_TEST_METRIC_EXTENSION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-76F0E207-AA7C-4296-8FD4-BFB7BF16C03F)
- [DBMS_CLOUD_OCI_STACK_MONITORING_UPDATE_AND_PROPAGATE_TAGS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-616E2B45-D9EE-478A-A42C-F2AD937AD334)
- [DBMS_CLOUD_OCI_STACK_MONITORING_UPDATE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-4E6DDE20-2B37-4AF7-B8A4-4BD2FC3DE3B9)
- [DBMS_CLOUD_OCI_STACK_MONITORING_UPDATE_AUTO_PROMOTE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-9D7734D3-76F1-40AB-9A78-B4C0EFA4FD0D)
- [DBMS_CLOUD_OCI_STACK_MONITORING_UPDATE_BASELINEABLE_METRIC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-9E1D0C1B-2013-4C59-A74E-12EB099763E5)
- [DBMS_CLOUD_OCI_STACK_MONITORING_UPDATE_LICENSE_AUTO_ASSIGN_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-06185DEB-D4B1-4087-A618-5CF34A12EFCF)
- [DBMS_CLOUD_OCI_STACK_MONITORING_UPDATE_LICENSE_ENTERPRISE_EXTENSIBILITY_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-129A9D82-6604-48F2-A5D3-F8A47024164D)
- [DBMS_CLOUD_OCI_STACK_MONITORING_UPDATE_METRIC_EXTENSION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-B97D0A02-0E35-4ECD-9472-4C14151B5BE1)
- [DBMS_CLOUD_OCI_STACK_MONITORING_UPDATE_MONITORED_RESOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-2FA8D98A-F65B-4823-857D-1D0349F237B7)
- [DBMS_CLOUD_OCI_STACK_MONITORING_UPDATE_MONITORED_RESOURCE_TASK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-52618C10-FEB9-4384-8A5B-B89F2941421D)
- [DBMS_CLOUD_OCI_STACK_MONITORING_UPDATE_MONITORED_RESOURCE_TYPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-62F66C31-AF5F-4807-B3A4-204B0196DC92)
- [DBMS_CLOUD_OCI_STACK_MONITORING_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-CEFE4CF6-E939-4049-BF8E-BDEE210758B9)
- [DBMS_CLOUD_OCI_STACK_MONITORING_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-FE229B98-74DF-44FF-BA59-9F60943A06A7)
- [DBMS_CLOUD_OCI_STACK_MONITORING_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-8BC29B7B-EC30-43DB-A571-17B1EE12FEA2)
- [DBMS_CLOUD_OCI_STACK_MONITORING_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-676A108B-5037-4067-9FA4-EC3B7091AA00)
- [DBMS_CLOUD_OCI_STACK_MONITORING_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-D479BE0E-B5FB-4139-ABE7-8F23B891ACFE)
- [DBMS_CLOUD_OCI_STACK_MONITORING_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-7DEBF13D-771B-41CB-A23D-A12B3F2450EB)
- [DBMS_CLOUD_OCI_STACK_MONITORING_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-728C60E4-BDA0-47AD-95B0-B1FCCFBE7426)
- [DBMS_CLOUD_OCI_STACK_MONITORING_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-A7E1D55E-BA7E-4819-8FF0-C0EDC9161000)
- [DBMS_CLOUD_OCI_STACK_MONITORING_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-56331F00-9542-425B-AAA0-ACC007768245)
- [DBMS_CLOUD_OCI_STACK_MONITORING_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-B98A0A3B-2A55-44F8-ABE1-0525431B8C4D)
- [DBMS_CLOUD_OCI_STACK_MONITORING_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-AD5913E5-CB5F-4388-A64C-B11F834F8E99)
- [DBMS_CLOUD_OCI_STACK_MONITORING_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/stack_monitoring_t.html#ADSDK-GUID-ACDFB11A-30E3-4D8F-988D-7F26A859E2CC)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
