# Cloud Guard Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html
- Fetched: 2026-09-05 19:02 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#dcoc-content-body)

## Cloud Guard Common Types

### DBMS_CLOUD_OCI_CLOUD_GUARD_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_CONTINUOUS_QUERY_START_POLICY_T Type

Continuous query start policy object

Syntax
```

```

Fields

Field Description

`start_policy_type`

(required) policy used for deciding the query start time

Allowed values are: 'NO_DELAY_START_POLICY', 'ABSOLUTE_TIME_START_POLICY'

### DBMS_CLOUD_OCI_CLOUD_GUARD_ABSOLUTE_TIME_START_POLICY_T Type

Policy that defines the exact start time.

Syntax
```

```

`dbms_cloud_oci_cloud_guard_absolute_time_start_policy_t`is a subtype of the`dbms_cloud_oci_cloud_guard_continuous_query_start_policy_t`type.

Fields

Field Description

`query_start_time`

(optional) Time when the query can start, if not specified it can start immediately.

### DBMS_CLOUD_OCI_CLOUD_GUARD_POLITICAL_LOCATION_T Type

Political location of a problem

Syntax
```

```

Fields

Field Description

`city`

(required) City

`state`

(required) State

`country`

(required) Country

### DBMS_CLOUD_OCI_CLOUD_GUARD_GEOGRAPHICAL_LOCATION_T Type

Geographical Location of a problem

Syntax
```

```

Fields

Field Description

`latitude`

(required) Latitude

`longitude`

(required) Longitude

### DBMS_CLOUD_OCI_CLOUD_GUARD_ACTIVITY_PROBLEM_AGGREGATION_T Type

Provides the dimensions and their corresponding count.

Syntax
```

```

Fields

Field Description

`dimensions_map`

(required) The key-value pairs of dimensions and their names.

`political_location`

(required)

`geographical_location`

(required)

`l_count`

(required) The number of occurences with given dimension/s

### DBMS_CLOUD_OCI_CLOUD_GUARD_ACTIVITY_PROBLEM_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_activity_problem_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_ACTIVITY_PROBLEM_AGGREGATION_COLLECTION_T Type

Activity Problem Aggregation Collection.

Syntax
```

```

Fields

Field Description

`items`

(required) The items consists of all the ActivityProblemAggregation objects.

### DBMS_CLOUD_OCI_CLOUD_GUARD_ADD_COMPARTMENT_DETAILS_T Type

An existing compartment to add to a security zone

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to be added to the security zone.

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_SELECTED_T Type

Target Selection eg select ALL or select on basis of TargetResourceTypes or TargetIds.

Syntax
```

```

Fields

Field Description

`kind`

(required) Target selection.

Allowed values are: 'ALL', 'TARGETTYPES', 'TARGETIDS'

### DBMS_CLOUD_OCI_CLOUD_GUARD_ALL_TARGETS_SELECTED_T Type

All Targets selected.

Syntax
```

```

`dbms_cloud_oci_cloud_guard_all_targets_selected_t`is a subtype of the`dbms_cloud_oci_cloud_guard_target_selected_t`type.

### DBMS_CLOUD_OCI_CLOUD_GUARD_ATTACH_TARGET_DETECTOR_RECIPE_DETAILS_T Type

The information required to create TargetDetectorRecipe

Syntax
```

```

Fields

Field Description

`detector_recipe_id`

(required) DetectorRecipe Identifier

### DBMS_CLOUD_OCI_CLOUD_GUARD_ATTACH_TARGET_RESPONDER_RECIPE_DETAILS_T Type

The information required to create TargetResponderRecipe

Syntax
```

```

Fields

Field Description

`responder_recipe_id`

(required) ResponderRecipe Identifier

### DBMS_CLOUD_OCI_CLOUD_GUARD_CANDIDATE_RESPONDER_RULE_T Type

Candidate Responder Rule list in Detector rule

Syntax
```

```

Fields

Field Description

`id`

(optional) The unique identifier of the Responder rule

`display_name`

(optional) The display name of the Responder rule

`is_preferred`

(optional) Preferred state

### DBMS_CLOUD_OCI_CLOUD_GUARD_CHANGE_DATA_SOURCE_COMPARTMENT_DETAILS_T Type

Changing compartmentId for DataSource

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment into which the DataSource should be moved

### DBMS_CLOUD_OCI_CLOUD_GUARD_CHANGE_DETECTOR_RECIPE_COMPARTMENT_DETAILS_T Type

Changing compartmentId for DetectorRecipe

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment into which the DetectorRecipe should be moved

### DBMS_CLOUD_OCI_CLOUD_GUARD_CHANGE_MANAGED_LIST_COMPARTMENT_DETAILS_T Type

Changing compartmentId for ManagedList

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment into which the ManagedList should be moved

### DBMS_CLOUD_OCI_CLOUD_GUARD_CHANGE_RESPONDER_RECIPE_COMPARTMENT_DETAILS_T Type

Changing compartmentId for ResponderRecipe

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment into which the ResponderRecipe should be moved

### DBMS_CLOUD_OCI_CLOUD_GUARD_CHANGE_SECURITY_POLICY_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_CLOUD_GUARD_CHANGE_SECURITY_RECIPE_COMPARTMENT_DETAILS_T Type

The compartment for the security zone recipe

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_CLOUD_GUARD_CHANGE_SECURITY_ZONE_COMPARTMENT_DETAILS_T Type

The compartment for the security zone

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_CLOUD_GUARD_CONDITION_T Type

Base condition object

Syntax
```

```

Fields

Field Description

`kind`

(required) Type of condition object

Allowed values are: 'COMPOSITE', 'SIMPLE'

### DBMS_CLOUD_OCI_CLOUD_GUARD_COMPOSITE_CONDITION_T Type

Composite Condition object with nested Condition

Syntax
```

```

`dbms_cloud_oci_cloud_guard_composite_condition_t`is a subtype of the`dbms_cloud_oci_cloud_guard_condition_t`type.

Fields

Field Description

`left_operand`

(optional)

`composite_operator`

(optional)

Allowed values are: 'AND', 'OR'

`right_operand`

(optional)

### DBMS_CLOUD_OCI_CLOUD_GUARD_CONDITION_GROUP_T Type

Condition configured on a target

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) compartment associated with condition

`condition`

(required)

### DBMS_CLOUD_OCI_CLOUD_GUARD_CONDITION_OPERATOR_T Type

Conditions related to the parameter data type

Syntax
```

```

Fields

Field Description

`name`

(required) operator name

Allowed values are: 'AND', 'OR', 'IN', 'NOT_IN', 'EQUALS', 'NOT_EQUALS', 'LESS_THAN', 'GREATER_THAN', 'RANGE'

`display_name`

(required) display name of the operator

### DBMS_CLOUD_OCI_CLOUD_GUARD_CONDITION_OPERATOR_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_condition_operator_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_OPERATOR_SUMMARY_T Type

Summary of Operator

Syntax
```

```

Fields

Field Description

`name`

(required) name of the operand

`display_name`

(required) display name of the operand

`datatype`

(required) data type of operand

`managed_listtype`

(required) operand list type

`filter_type`

(required) Filter type can be config filter or condition filter

Allowed values are: 'CONDITION', 'CONFIG'

`operators`

(required) List of parameters

`multi_list_types`

(optional) configuration value type list for multilist data type

### DBMS_CLOUD_OCI_CLOUD_GUARD_OPERATOR_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_operator_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_RULE_SUMMARY_T Type

Summary of rules

Syntax
```

```

Fields

Field Description

`id`

(required) id of the rule

`description`

(required) description of the rule

`parameters`

(required) List of parameters applicable for rule

### DBMS_CLOUD_OCI_CLOUD_GUARD_RULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_rule_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_TYPE_SUMMARY_T Type

Summary of ResourceType

Syntax
```

```

Fields

Field Description

`name`

(required) name of the resource

`display_name`

(required) display name of the resource

`rules`

(optional) List of rules

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_TYPE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_resource_type_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_SERVICE_TYPE_SUMMARY_T Type

Summary of Service type

Syntax
```

```

Fields

Field Description

`name`

(required) name of the service type

`resource_types`

(required) List of Resource

### DBMS_CLOUD_OCI_CLOUD_GUARD_SERVICE_TYPE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_service_type_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_CONDITION_METADATA_TYPE_T Type

condition type provided by cloud guard

Syntax
```

```

Fields

Field Description

`name`

(required) Name used to identify

`service_types`

(required) collection of Service type

### DBMS_CLOUD_OCI_CLOUD_GUARD_CONDITION_METADATA_TYPE_SUMMARY_T Type

condition type provided by cloud guard

Syntax
```

```

Fields

Field Description

`id`

(required) Name used to identify

`description`

(required) Display name of the condition type

`lifecycle_state`

(optional) The current state of the resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

### DBMS_CLOUD_OCI_CLOUD_GUARD_CONDITION_METADATA_TYPE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_condition_metadata_type_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_CONDITION_METADATA_TYPE_COLLECTION_T Type

condition type provided by cloud guard

Syntax
```

```

Fields

Field Description

`items`

(required) collection of condition types

### DBMS_CLOUD_OCI_CLOUD_GUARD_CONFIG_VALUE_T Type

configuration item for multi list data type

Syntax
```

```

Fields

Field Description

`list_type`

(required) configuration list item type, either CUSTOM or MANAGED

Allowed values are: 'MANAGED', 'CUSTOM'

`managed_list_type`

(required) type of the managed list

`value`

(required) configuration value

### DBMS_CLOUD_OCI_CLOUD_GUARD_CONFIGURATION_T Type

Cloud Guard configuration details of a tenancy.

Syntax
```

```

Fields

Field Description

`reporting_region`

(required) The reporting region value

`status`

(optional) Status of Cloud Guard Tenant

Allowed values are: 'ENABLED', 'DISABLED'

`self_manage_resources`

(optional) Identifies if Oracle managed resources were created by customers

### DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_DATA_MASK_RULE_DETAILS_T Type

The information about new Data Mask Rule.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Data mask rule name. Avoid entering confidential information.

`compartment_id`

(required) Compartment Identifier where the resource is created

`description`

(optional) The data mask rule description. Avoid entering confidential information.

`iam_group_id`

(required) IAM Group id associated with the data mask rule

`target_selected`

(required)

`data_mask_categories`

(required) Data Mask Categories

Allowed values are: 'ACTOR', 'PII', 'PHI', 'FINANCIAL', 'LOCATION', 'CUSTOM'

`data_mask_rule_status`

(optional) The status of the dataMaskRule.

Allowed values are: 'ENABLED', 'DISABLED'

`lifecycle_state`

(optional) The current state of the DataMaskRule.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_SOURCE_DETAILS_T Type

Details specific to the data source type.

Syntax
```

```

Fields

Field Description

`data_source_feed_provider`

(required) Possible type of dataSourceFeed Provider(LoggingQuery)

Allowed values are: 'LOGGINGQUERY'

### DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_DATA_SOURCE_DETAILS_T Type

Creation of Data Source.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Data Source display name.

`compartment_id`

(required) CompartmentId of Data Source.

`data_source_feed_provider`

(required) Possible type of dataSourceFeed Provider(LoggingQuery)

Allowed values are: 'LOGGINGQUERY'

`data_source_details`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_CONFIG_VALUE_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_config_value_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_CONFIGURATION_T Type

A single configuration applied to a detector

Syntax
```

```

Fields

Field Description

`config_key`

(required) Unique name of the configuration

`name`

(required) configuration name

`value`

(optional) configuration value

`data_type`

(optional) configuration data type

`l_values`

(optional) List of configuration values

### DBMS_CLOUD_OCI_CLOUD_GUARD_ENTITIES_MAPPING_T Type

Data Source Entities mappings

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The display name of entity

`query_field`

(required) The entity value mapped to a data source query

`entity_type`

(optional) Possible type of entity

Allowed values are: 'EXTERNAL_IP', 'INTERNAL_IP', 'TEXT', 'JSON_LIST'

### DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_CONFIGURATION_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_detector_configuration_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_ENTITIES_MAPPING_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_entities_mapping_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_DETECTOR_RULE_DETAILS_T Type

Details of a Detector Rule to be overriden in Detector Recipe

Syntax
```

```

Fields

Field Description

`is_enabled`

(required) Enables the control

`risk_level`

(optional) The Risk Level

Allowed values are: 'CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'MINOR'

`configurations`

(optional) Configuration details

`condition`

(optional)

`labels`

(optional) user defined labels for a detector rule

`description`

(optional) Description for DetectorRecipeDetectorRule.

`recommendation`

(optional) Recommendation for DetectorRecipeDetectorRule

`data_source_id`

(optional) The id of the attached DataSource.

`entities_mappings`

(optional) Data Source entities mapping for a Detector Rule

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_DETECTOR_RECIPE_DETECTOR_RULE_T Type

The details to be updated in DetectorRule

Syntax
```

```

Fields

Field Description

`detector_rule_id`

(required) DetectorRecipeRule Identifier

`details`

(required)

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_DETECTOR_RECIPE_DETECTOR_RULE_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_update_detector_recipe_detector_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_DETECTOR_RECIPE_DETAILS_T Type

Create of Detector recipe.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Detector recipe display name. Avoid entering confidential information.

`description`

(optional) Detector recipe description. Avoid entering confidential information.

`detector`

(optional) detector for the rule

Allowed values are: 'IAAS_ACTIVITY_DETECTOR', 'IAAS_CONFIGURATION_DETECTOR', 'IAAS_THREAT_DETECTOR', 'IAAS_LOG_INSIGHT_DETECTOR'

`source_detector_recipe_id`

(optional) The id of the source detector recipe.

`compartment_id`

(required) Compartment Identifier

`detector_rules`

(optional) Detector Rules to override from source detector recipe

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_DETECTOR_RULE_DETAILS_T Type

Details of a Detector Rule to be created in Detector Recipe

Syntax
```

```

Fields

Field Description

`source_detector_rule_id`

(optional) Id of source detector rule

`name`

(required) Name of the detector rule

`description`

(optional) Description of the detector rule

`is_enabled`

(optional) Identifies state for detector rule

`risk_level`

(optional) The Risk Level

Allowed values are: 'CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'MINOR'

`configurations`

(optional) Configuration details

`condition`

(optional)

`labels`

(optional) user defined labels for a detector rule

`recommendation`

(optional) Recommendations of the detector rule

`data_source_id`

(optional) ocid of the data source which needs to attached

`entities_mappings`

(optional) Data Source entities mapping for a Detector Rule

### DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_DETECTOR_RECIPE_DETECTOR_RULE_DETAILS_T Type

Create detector rule in a detector recipe

Syntax
```

```

Fields

Field Description

`details`

(optional)

### DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_MANAGED_LIST_DETAILS_T Type

Create ManagedList

Syntax
```

```

Fields

Field Description

`display_name`

(required) Managed list display name. Avoid entering confidential information.

`compartment_id`

(required) Compartment Identifier

`source_managed_list_id`

(optional) OCID of the Source ManagedList

`description`

(optional) Managed list description. Avoid entering confidential information.

`list_type`

(optional) type of the list

Allowed values are: 'CIDR_BLOCK', 'USERS', 'GROUPS', 'IPV4ADDRESS', 'IPV6ADDRESS', 'RESOURCE_OCID', 'REGION', 'COUNTRY', 'STATE', 'CITY', 'TAGS', 'GENERIC'

`list_items`

(optional) List of ManagedListItem

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_RESPONDER_RULE_DETAILS_T Type

Details of UpdateResponderRuleDetails.

Syntax
```

```

Fields

Field Description

`is_enabled`

(required) Identifies state for ResponderRule

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_RESPONDER_RECIPE_RESPONDER_RULE_T Type

The details to be updated in ResponderRule

Syntax
```

```

Fields

Field Description

`responder_rule_id`

(required) ResponderRecipeRule Identifier

`details`

(required)

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_RESPONDER_RECIPE_RESPONDER_RULE_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_update_responder_recipe_responder_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_RESPONDER_RECIPE_DETAILS_T Type

Details of ResponderRecipe.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Responder recipe display name. Avoid entering confidential information.

`description`

(optional) Responder recipe description. Avoid entering confidential information.

`source_responder_recipe_id`

(required) The id of the source responder recipe.

`compartment_id`

(required) Compartment Identifier

`responder_rules`

(optional) Responder Rules to override from source responder recipe

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_SECURITY_POLICY_DETAILS_T Type

The information about new SecurityPolicy.

Syntax
```

```

Fields

Field Description

`friendly_name`

(optional) SecurityPolicy friendly name

`display_name`

(required) SecurityPolicy Identifier

`description`

(optional) Security policy description

`category`

(optional) The category of security policy.

`services`

(optional) The list of services for policy.

`compartment_id`

(required) Compartment Identifier

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_SECURITY_RECIPE_DETAILS_T Type

Details about a new security zone recipe

Syntax
```

```

Fields

Field Description

`display_name`

(required) The recipe's name

`description`

(optional) The recipe's description

`security_policies`

(required) The list of `SecurityPolicy` ids to include in the recipe

`compartment_id`

(required) The compartment in which to create the recipe

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_SECURITY_ZONE_DETAILS_T Type

Details for a new security zone

Syntax
```

```

Fields

Field Description

`display_name`

(required) The security zone's name

`description`

(optional) The security zone's description

`security_zone_recipe_id`

(required) The OCID of the recipe (`SecurityRecipe`) for the security zone

`compartment_id`

(required) The OCID of the compartment for the security zone

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_CONDITION_GROUP_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_condition_group_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_DETECTOR_RULE_DETAILS_T Type

Overriden settings of a Detector Rule applied on target

Syntax
```

```

Fields

Field Description

`condition_groups`

(optional) Condition group corresponding to each compartment

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_RECIPE_DETECTOR_RULE_DETAILS_T Type

The details to be updated in TargetDetectorRecipeDetectorRule

Syntax
```

```

Fields

Field Description

`detector_rule_id`

(required) Identifier for DetectorRule.

`details`

(required)

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_RECIPE_DETECTOR_RULE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_update_target_recipe_detector_rule_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_TARGET_DETECTOR_RECIPE_DETAILS_T Type

The information required to create TargetDetectorRecipe

Syntax
```

```

Fields

Field Description

`detector_recipe_id`

(required) Identifier for DetectorRecipe.

`detector_rules`

(optional) Overrides to be applied to Detector Rule associated with the target

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_CONFIGURATION_T Type

A single configuration applied to a responder

Syntax
```

```

Fields

Field Description

`config_key`

(required) Unique name of the configuration

`name`

(required) configuration name

`value`

(required) configuration value

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_CONFIGURATION_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_responder_configuration_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_RESPONDER_RULE_DETAILS_T Type

Details of ResponderRule.

Syntax
```

```

Fields

Field Description

`condition`

(optional)

`configurations`

(optional) Configurations associated with the ResponderRule

`l_mode`

(optional) Execution Mode for ResponderRule

Allowed values are: 'AUTOACTION', 'USERACTION'

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_RECIPE_RESPONDER_RULE_DETAILS_T Type

The details to be updated in TargetResponderRecipeResponderRule

Syntax
```

```

Fields

Field Description

`responder_rule_id`

(required) Identifier for ResponderRule.

`details`

(required)

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_RECIPE_RESPONDER_RULE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_update_target_recipe_responder_rule_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_TARGET_RESPONDER_RECIPE_DETAILS_T Type

The information required to create TargetResponderRecipe

Syntax
```

```

Fields

Field Description

`responder_recipe_id`

(required) Identifier for ResponderRecipe.

`responder_rules`

(optional) Override responder rules associated with reponder recipe in a target.

### DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_TARGET_DETECTOR_RECIPE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_create_target_detector_recipe_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_TARGET_RESPONDER_RECIPE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_create_target_responder_recipe_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_TARGET_DETAILS_T Type

The information about new Target.

Syntax
```

```

Fields

Field Description

`display_name`

(required) DetectorTemplate identifier. Avoid entering confidential information.

`compartment_id`

(required) Compartment Identifier where the resource is created

`description`

(optional) The target description. Avoid entering confidential information.

`target_resource_type`

(required) possible type of targets(COMPARTMENT/FACLOUD)

Allowed values are: 'COMPARTMENT', 'ERPCLOUD', 'HCMCLOUD', 'SECURITY_ZONE'

`target_resource_id`

(required) Resource ID which the target uses to monitor

`target_detector_recipes`

(optional) List of detector recipes to associate with target

`target_responder_recipes`

(optional) List of responder recipes to associate with target

`lifecycle_state`

(optional) The current state of the DetectorRule.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_MASK_RULE_T Type

Description of DataMaskRule.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`display_name`

(optional) Data Mask Rule Identifier, can be renamed.

`compartment_id`

(required) Compartment Identifier where the resource is created.

`description`

(optional) The data mask rule description.

`iam_group_id`

(required) IAM Group id associated with the data mask rule

`target_selected`

(required)

`data_mask_categories`

(optional) Data Mask Categories

Allowed values are: 'ACTOR', 'PII', 'PHI', 'FINANCIAL', 'LOCATION', 'CUSTOM'

`time_created`

(optional) The date and time the target was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the target was updated. Format defined by RFC3339.

`data_mask_rule_status`

(optional) The status of the dataMaskRule.

Allowed values are: 'ENABLED', 'DISABLED'

`lifecycle_state`

(optional) The current state of the DataMaskRule.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecyle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_MASK_RULE_SUMMARY_T Type

Summary of DataMaskRule.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`display_name`

(optional) Data Mask Rule Name.

`compartment_id`

(required) Compartment Identifier where the resource is created

`description`

(optional) The data mask rule description.

`iam_group_id`

(required) IAM Group id associated with the data mask rule

`target_selected`

(required)

`data_mask_categories`

(optional) Data Mask Categories

Allowed values are: 'ACTOR', 'PII', 'PHI', 'FINANCIAL', 'LOCATION', 'CUSTOM'

`time_created`

(optional) The date and time the target was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the target was updated. Format defined by RFC3339.

`data_mask_rule_status`

(optional) The status of the dataMaskRule.

Allowed values are: 'ENABLED', 'DISABLED'

`lifecycle_state`

(optional) The current state of the DataMaskRule.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecyle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_MASK_RULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_data_mask_rule_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_MASK_RULE_COLLECTION_T Type

Collection of Data Mask Rule

Syntax
```

```

Fields

Field Description

`items`

(required) List of Data Mask Rule Summary

### DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_SOURCE_MAPPING_INFO_T Type

Detail of resources which are mapped to DataSource.

Syntax
```

```

Fields

Field Description

`detector_recipe_id`

(required) Id of the attached detectorRecipeId to the Data Source.

`detector_rule_id`

(required) Id of the attached detectorRuleId to the Data Source.

### DBMS_CLOUD_OCI_CLOUD_GUARD_REGION_STATUS_DETAIL_T Type

Status of Region query replication.

Syntax
```

```

Fields

Field Description

`l_region`

(required) Data Source replication region.

`status`

(required) Data Source replication region status.

Allowed values are: 'PROVISIONING', 'FAILED', 'SUCCEEDED'

### DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_SOURCE_MAPPING_INFO_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_data_source_mapping_info_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_REGION_STATUS_DETAIL_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_region_status_detail_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_SOURCE_T Type

Details of Data source

Syntax
```

```

Fields

Field Description

`id`

(required) Ocid for Data source

`display_name`

(required) DisplayName of Data source.

`data_source_feed_provider`

(required) Possible type of dataSourceFeed Provider(LoggingQuery)

Allowed values are: 'LOGGINGQUERY'

`compartment_id`

(required) CompartmentId of Data source.

`data_source_details`

(optional)

`time_created`

(optional) The date and time the Data source was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the Data source was updated. Format defined by RFC3339.

`status`

(optional) Status of data Source

Allowed values are: 'ENABLED', 'DISABLED'

`data_source_detector_mapping_info`

(optional) Information about the detector recipe and rule attached

`region_status_detail`

(optional) Information about the region and status of query replication

`lifecycle_state`

(optional) The current state of the resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_SOURCE_SUMMARY_DETAILS_T Type

Summary specific to the data source type.

Syntax
```

```

Fields

Field Description

`data_source_feed_provider`

(required) Possible type of dataSourceFeed Provider(LoggingQuery)

Allowed values are: 'LOGGINGQUERY'

### DBMS_CLOUD_OCI_CLOUD_GUARD_LOGGING_QUERY_DETAILS_T Type

Additional details specific to the data source type (Sighting/Insight).

Syntax
```

```

Fields

Field Description

`logging_query_type`

(required) Logging query type for data source (Sighting/Insight)

Allowed values are: 'INSIGHT'

### DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_SOURCE_SUMMARY_T Type

Summary of Data Source

Syntax
```

```

Fields

Field Description

`id`

(required) Ocid for Data Source

`display_name`

(required) DisplayName of Data Source

`data_source_feed_provider`

(required) Possible type of dataSourceFeed Provider(LoggingQuery)

Allowed values are: 'LOGGINGQUERY'

`compartment_id`

(required) CompartmentId of Data Source.

`data_source_summary_details`

(optional)

`time_created`

(optional) The date and time the data source was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the data source was updated. Format defined by RFC3339.

`status`

(optional) Status of data Source

Allowed values are: 'ENABLED', 'DISABLED'

`logging_query_details`

(optional)

`lifecycle_state`

(optional) The current state of the resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, this can be used to provide actionable information for a zone in the `Failed` state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_SOURCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_data_source_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_SOURCE_COLLECTION_T Type

Summary of the DataSource.

Syntax
```

```

Fields

Field Description

`items`

(required) List of DataSourceSummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_SOURCE_EVENT_INFO_T Type

Event info of a data source.

Syntax
```

```

Fields

Field Description

`data_source_feed_provider`

(required) Possible type of dataSourceFeed Provider(LoggingQuery)

Allowed values are: 'LOGGINGQUERY'

### DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_SOURCE_EVENT_SUMMARY_T Type

The information about Event details of DataSource.

Syntax
```

```

Fields

Field Description

`l_region`

(required) Data source event region

`event_date`

(required) Data source event date time

`data_source_id`

(required) Attached data Source

`time_created`

(required) Data source event created time

`status`

(optional) Current data source event info status

Allowed values are: 'SUCCESS', 'FAILURE'

`comments`

(optional) Data source event comments

`event_info`

(required)

### DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_SOURCE_EVENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_data_source_event_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_SOURCE_EVENT_COLLECTION_T Type

The collection of datasource events.

Syntax
```

```

Fields

Field Description

`items`

(required) List of event related to a DataSource

### DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_T Type

A single Detector

Syntax
```

```

Fields

Field Description

`id`

(required) detector key

`description`

(required) detector description

`lifecycle_state`

(optional) The current state of the resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

### DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_SUMMARY_T Type

Summary of the Detector.

Syntax
```

```

Fields

Field Description

`id`

(required) detector Identifier

`description`

(optional) detector description

`lifecycle_state`

(optional) The current state of the resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

### DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_detector_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_COLLECTION_T Type

Summary of the Detector.

Syntax
```

```

Fields

Field Description

`items`

(required) List of DetectorSummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_SIGHTING_TYPE_T Type

Specific behavior that can trigger a Sighting

Syntax
```

```

Fields

Field Description

`id`

(optional) The unique identifier of sighting type

`display_name`

(optional) Name of the sighting type

`description`

(optional) Description of the sighting type

`mitre_link`

(optional) Link of the sighting type

`tactic`

(optional) Mitre Att&amp;ck tactic

`techniques`

(optional) List of Mitre Att&amp;ck Techniques

### DBMS_CLOUD_OCI_CLOUD_GUARD_SIGHTING_TYPE_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_sighting_type_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_DETAILS_T Type

Details of a Detector Rule

Syntax
```

```

Fields

Field Description

`is_enabled`

(required) Enables the control

`risk_level`

(optional) The Risk Level

Allowed values are: 'CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'MINOR'

`configurations`

(optional) Configuration details

`condition`

(optional)

`labels`

(optional) user defined labels for a detector rule

`is_configuration_allowed`

(optional) configuration allowed or not

`problem_threshold`

(optional) Cutover point for an elevated resource Risk Score to create a Problem

`target_types`

(optional) List of target types for which the detector rule is applicable

`sighting_types`

(optional) List of sighting types

### DBMS_CLOUD_OCI_CLOUD_GUARD_CANDIDATE_RESPONDER_RULE_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_candidate_responder_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RECIPE_DETECTOR_RULE_T Type

Detector Recipe Rule

Syntax
```

```

Fields

Field Description

`detector_rule_id`

(required) The unique identifier of the detector rule.

`display_name`

(optional) Display name for DetectorRecipeDetectorRule.

`description`

(optional) Description for DetectorRecipeDetectorRule.

`recommendation`

(optional) Recommendation for DetectorRecipeDetectorRule

`detector`

(required) detector for the rule

Allowed values are: 'IAAS_ACTIVITY_DETECTOR', 'IAAS_CONFIGURATION_DETECTOR', 'IAAS_THREAT_DETECTOR', 'IAAS_LOG_INSIGHT_DETECTOR'

`service_type`

(required) service type of the configuration to which the rule is applied

`resource_type`

(required) resource type of the configuration to which the rule is applied

`details`

(optional)

`managed_list_types`

(optional) List of cloudguard managed list types related to this rule

Allowed values are: 'CIDR_BLOCK', 'USERS', 'GROUPS', 'IPV4ADDRESS', 'IPV6ADDRESS', 'RESOURCE_OCID', 'REGION', 'COUNTRY', 'STATE', 'CITY', 'TAGS', 'GENERIC'

`candidate_responder_rules`

(optional) List of CandidateResponderRule related to this rule

`time_created`

(optional) The date and time the detector recipe rule was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the detector recipe rule was updated. Format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the DetectorRule.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`data_source_id`

(optional) The id of the attached DataSource.

`entities_mappings`

(optional) Data Source entities mapping for a Detector Rule

### DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RECIPE_DETECTOR_RULE_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_detector_recipe_detector_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RECIPE_T Type

Details of Detector recipe

Syntax
```

```

Fields

Field Description

`id`

(required) Ocid for detector recipe

`display_name`

(required) DisplayName of detector recipe.

`description`

(optional) Detector recipe description.

`compartment_id`

(required) compartmentId of detector recipe

`source_detector_recipe_id`

(required) Recipe Ocid of the Source Recipe to be cloned

`owner`

(required) Owner of detector recipe

Allowed values are: 'CUSTOMER', 'ORACLE'

`detector`

(required) Type of detector

Allowed values are: 'IAAS_ACTIVITY_DETECTOR', 'IAAS_CONFIGURATION_DETECTOR', 'IAAS_THREAT_DETECTOR', 'IAAS_LOG_INSIGHT_DETECTOR'

`detector_rules`

(optional) List of detector rules for the detector type for recipe - user input

`effective_detector_rules`

(optional) List of effective detector rules for the detector type for recipe after applying defaults

`time_created`

(optional) The date and time the detector recipe was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the detector recipe was updated. Format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`source_data_retention`

(optional) The number of days for which source data is retained

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`target_ids`

(optional) The recipe attached to targets

### DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RECIPE_SUMMARY_T Type

Summary of Detector recipe

Syntax
```

```

Fields

Field Description

`id`

(required) Ocid for detector recipe

`display_name`

(required) DisplayName of detector recipe

`description`

(optional) Detector recipe description

`compartment_id`

(required) compartmentId of detector recipe

`source_detector_recipe_id`

(optional) Recipe Ocid of the Source Recipe to be cloned

`owner`

(required) Owner of detector recipe

Allowed values are: 'CUSTOMER', 'ORACLE'

`detector`

(required) Type of detector

Allowed values are: 'IAAS_ACTIVITY_DETECTOR', 'IAAS_CONFIGURATION_DETECTOR', 'IAAS_THREAT_DETECTOR', 'IAAS_LOG_INSIGHT_DETECTOR'

`detector_rules`

(optional) List of detetor rules for the detector type

`time_created`

(optional) The date and time the detector recipe was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the detector recipe was updated. Format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`source_data_retention`

(optional) The number of days for which source data is retained

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RECIPE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_detector_recipe_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RECIPE_COLLECTION_T Type

Summary of the DetectorRecipe.

Syntax
```

```

Fields

Field Description

`items`

(required) List of DetectorRecipeSummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RECIPE_DETECTOR_RULE_SUMMARY_T Type

Summary of the Detector Recipe Rule.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier of the detector rule

`display_name`

(optional) DetectorTemplate Identifier, can be renamed

`description`

(optional) DetectorTemplate Identifier, can be renamed

`recommendation`

(optional) Recommendation for DetectorRecipeDetectorRule

`detector`

(required) possible type of detectors

Allowed values are: 'IAAS_ACTIVITY_DETECTOR', 'IAAS_CONFIGURATION_DETECTOR', 'IAAS_THREAT_DETECTOR', 'IAAS_LOG_INSIGHT_DETECTOR'

`service_type`

(optional) service type of the configuration to which the rule is applied

`resource_type`

(optional) resource type of the configuration to which the rule is applied

`managed_list_types`

(optional) List of cloudguard managed list types related to this rule

Allowed values are: 'CIDR_BLOCK', 'USERS', 'GROUPS', 'IPV4ADDRESS', 'IPV6ADDRESS', 'RESOURCE_OCID', 'REGION', 'COUNTRY', 'STATE', 'CITY', 'TAGS', 'GENERIC'

`candidate_responder_rules`

(optional) List of CandidateResponderRule related to this rule

`detector_details`

(optional)

`time_created`

(optional) The date and time the detector recipe rule was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the detector recipe rule was updated. Format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the detector recipe rule

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`data_source_id`

(optional) The id of the attached DataSource.

`entities_mappings`

(optional) Data Source entities mapping for a Detector Rule

### DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RECIPE_DETECTOR_RULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_detector_recipe_detector_rule_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RECIPE_DETECTOR_RULE_COLLECTION_T Type

Summary of the DetectorRule.

Syntax
```

```

Fields

Field Description

`items`

(required) List of DetectorRecipeDetectorRuleSummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RULE_T Type

Detector

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier of the detector rule.

`display_name`

(optional) Display name for DetectorRule.

`description`

(optional) Description for DetectorRule.

`recommendation`

(optional) recommendation for DetectorRule

`detector`

(required) detector for the rule

Allowed values are: 'IAAS_ACTIVITY_DETECTOR', 'IAAS_CONFIGURATION_DETECTOR', 'IAAS_THREAT_DETECTOR', 'IAAS_LOG_INSIGHT_DETECTOR'

`service_type`

(required) service type of the configuration to which the rule is applied

`resource_type`

(required) resource type of the configuration to which the rule is applied

`detector_details`

(optional)

`managed_list_types`

(optional) List of cloudguard managed list types related to this rule

Allowed values are: 'CIDR_BLOCK', 'USERS', 'GROUPS', 'IPV4ADDRESS', 'IPV6ADDRESS', 'RESOURCE_OCID', 'REGION', 'COUNTRY', 'STATE', 'CITY', 'TAGS', 'GENERIC'

`candidate_responder_rules`

(optional) List of CandidateResponderRule related to this rule

`time_created`

(optional) The date and time the detector rule was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the detector rule was updated. Format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the DetectorRule.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RULE_SUMMARY_T Type

Summary of the Detector Rules.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier of the detector rule

`display_name`

(optional) DetectorTemplate Identifier, can be renamed

`description`

(optional) Description for detector rule

`recommendation`

(optional) Recommendation for detector rule

`detector`

(required) possible type of detectors

Allowed values are: 'IAAS_ACTIVITY_DETECTOR', 'IAAS_CONFIGURATION_DETECTOR', 'IAAS_THREAT_DETECTOR', 'IAAS_LOG_INSIGHT_DETECTOR'

`service_type`

(optional) service type of the configuration to which the rule is applied

`resource_type`

(optional) resource type of the configuration to which the rule is applied

`managed_list_types`

(optional) List of cloudguard managed list types related to this rule

Allowed values are: 'CIDR_BLOCK', 'USERS', 'GROUPS', 'IPV4ADDRESS', 'IPV6ADDRESS', 'RESOURCE_OCID', 'REGION', 'COUNTRY', 'STATE', 'CITY', 'TAGS', 'GENERIC'

`candidate_responder_rules`

(optional) List of CandidateResponderRule related to this rule

`detector_details`

(optional)

`time_created`

(optional) The date and time the detector rule was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the detector rule was updated. Format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the detector rule

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_detector_rule_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RULE_COLLECTION_T Type

Summary of the DetectorRule.

Syntax
```

```

Fields

Field Description

`items`

(required) List of DetectorRuleSummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_ENTITY_DETAILS_T Type

Entities Details for a data source

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The display name of entity

`value`

(optional) The entity value

`l_type`

(optional) Type of entity

### DBMS_CLOUD_OCI_CLOUD_GUARD_ERROR_T Type

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

### DBMS_CLOUD_OCI_CLOUD_GUARD_EXECUTE_RESPONDER_EXECUTION_DETAILS_T Type

The details for Responder Configuration

Syntax
```

```

Fields

Field Description

`configurations`

(optional) ResponderRule configurations

### DBMS_CLOUD_OCI_CLOUD_GUARD_IMPACTED_RESOURCE_SUMMARY_T Type

Impacted Resource summary Definition.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier for finding event

`resource_id`

(required) Unique id of the Impacted Resource

`problem_id`

(required) Problem Id to which the Impacted Resource is associated

`compartment_id`

(required) Compartment Id where the resource is created

`sighting_type`

(optional) Identifier for the sighting type

`sighting_type_display_name`

(optional) Name of the sighting type

`resource_name`

(required) Name of the Impacted Resource

`resource_type`

(required) Type of the Impacted Resource

`l_region`

(required) Region where the resource is created

`time_identified`

(required) Time when the problem was identified

### DBMS_CLOUD_OCI_CLOUD_GUARD_IMPACTED_RESOURCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_impacted_resource_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_IMPACTED_RESOURCE_COLLECTION_T Type

Provides the summary of impacted resources

Syntax
```

```

Fields

Field Description

`items`

(required) List of ImpactedResourceSummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_INSIGHT_TYPE_LOGGING_QUERY_DETAILS_T Type

Additional details specific to insight type DataSource.

Syntax
```

```

`dbms_cloud_oci_cloud_guard_insight_type_logging_query_details_t`is a subtype of the`dbms_cloud_oci_cloud_guard_logging_query_details_t`type.

Fields

Field Description

`key_entities_count`

(optional) The key entities count used for data source query

### DBMS_CLOUD_OCI_CLOUD_GUARD_LOGGING_EVENT_INFO_T Type

The information about new Logging event detail of DataSource.

Syntax
```

```

`dbms_cloud_oci_cloud_guard_logging_event_info_t`is a subtype of the`dbms_cloud_oci_cloud_guard_data_source_event_info_t`type.

Fields

Field Description

`observed_value`

(optional)

`trigger_value`

(optional)

`operator`

(optional)

`log_result`

(optional)

### DBMS_CLOUD_OCI_CLOUD_GUARD_LOGGING_QUERY_DATA_SOURCE_DETAILS_T Type

The information about new Logging Query of type DataSource.

Syntax
```

```

`dbms_cloud_oci_cloud_guard_logging_query_data_source_details_t`is a subtype of the`dbms_cloud_oci_cloud_guard_data_source_details_t`type.

Fields

Field Description

`regions`

(optional) Logging Query regions

`query`

(optional) The continuous query expression that is run periodically.

`interval_in_minutes`

(optional) Interval in minutes that query is run periodically.

`threshold`

(optional) The integer value that must be exceeded, fall below or equal to (depending on the operator), the query result to trigger an event.

`query_start_time`

(optional)

`operator`

(optional) Operator used in Data Soruce

Allowed values are: 'EQUAL', 'GREATER', 'GREATERTHANEQUALTO', 'LESS', 'LESSTHANEQUALTO'

`logging_query_type`

(optional) Logging query type for data source (Sighting/Insight)

Allowed values are: 'INSIGHT'

`additional_entities_count`

(optional) The additional entities count used for data source query.

`logging_query_details`

(optional)

### DBMS_CLOUD_OCI_CLOUD_GUARD_LOGGING_QUERY_DATA_SOURCE_SUMMARY_DETAILS_T Type

The information about new Logging Query of type DataSourceSummary.

Syntax
```

```

`dbms_cloud_oci_cloud_guard_logging_query_data_source_summary_details_t`is a subtype of the`dbms_cloud_oci_cloud_guard_data_source_summary_details_t`type.

Fields

Field Description

`regions`

(optional) DataSource customer specified regions

`data_source_detector_mapping_info`

(optional) DataSource mapping with detectorRecipe and detectorRule

`region_status_detail`

(optional) DataSource query metadata replication region and status.

### DBMS_CLOUD_OCI_CLOUD_GUARD_MANAGED_LIST_T Type

A cloud guard list containing one or more items of a list type

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`display_name`

(required) ManagedList display name.

`description`

(optional) ManagedList description.

`compartment_id`

(required) Compartment Identifier where the resource is created

`source_managed_list_id`

(optional) OCID of the Source ManagedList

`list_type`

(required) type of the list

Allowed values are: 'CIDR_BLOCK', 'USERS', 'GROUPS', 'IPV4ADDRESS', 'IPV6ADDRESS', 'RESOURCE_OCID', 'REGION', 'COUNTRY', 'STATE', 'CITY', 'TAGS', 'GENERIC'

`list_items`

(optional) List of ManagedListItem

`feed_provider`

(optional) provider of the feed

Allowed values are: 'CUSTOMER', 'ORACLE'

`is_editable`

(optional) If this list is editable or not

`time_created`

(optional) The date and time the managed list was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the managed list was updated. Format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecyle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_MANAGED_LIST_SUMMARY_T Type

Summary of ManagedList

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`display_name`

(required) ManagedList display name

`description`

(optional) ManagedList description

`compartment_id`

(required) Compartment Identifier where the resource is created

`source_managed_list_id`

(optional) OCID of the Source ManagedList

`list_type`

(required) type of the list

Allowed values are: 'CIDR_BLOCK', 'USERS', 'GROUPS', 'IPV4ADDRESS', 'IPV6ADDRESS', 'RESOURCE_OCID', 'REGION', 'COUNTRY', 'STATE', 'CITY', 'TAGS', 'GENERIC'

`feed_provider`

(required) provider of the feed

Allowed values are: 'CUSTOMER', 'ORACLE'

`is_editable`

(optional) If this list is editable or not

`list_items`

(required) List of ManagedListItem

`time_created`

(optional) The date and time the managed list was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the managed list was updated. Format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecyle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_MANAGED_LIST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_managed_list_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_MANAGED_LIST_COLLECTION_T Type

Summary of the ManagedList.

Syntax
```

```

Fields

Field Description

`items`

(required) List of ManagedListSummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_MANAGED_LIST_TYPE_SUMMARY_T Type

Summary of the ManagedListType.

Syntax
```

```

Fields

Field Description

`id`

(required) ManagedListType Identifier

`description`

(optional) ManagedListType description

`lifecycle_state`

(optional) The current state of the resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

### DBMS_CLOUD_OCI_CLOUD_GUARD_MANAGED_LIST_TYPE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_managed_list_type_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_MANAGED_LIST_TYPE_COLLECTION_T Type

Summary of the ManagedListType.

Syntax
```

```

Fields

Field Description

`items`

(required) List of ManagedListTypeSummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_NO_DELAY_START_POLICY_T Type

Continuous query start policy that starts the query immediately.

Syntax
```

```

`dbms_cloud_oci_cloud_guard_no_delay_start_policy_t`is a subtype of the`dbms_cloud_oci_cloud_guard_continuous_query_start_policy_t`type.

### DBMS_CLOUD_OCI_CLOUD_GUARD_POLICY_SUMMARY_T Type

Global policy statement

Syntax
```

```

Fields

Field Description

`policy`

(required) Global policy statement

### DBMS_CLOUD_OCI_CLOUD_GUARD_POLICY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_policy_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_POLICY_COLLECTION_T Type

Collection of policy statements required by cloud guard

Syntax
```

```

Fields

Field Description

`items`

(required) List of global policy statements

### DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_T Type

Problem Definition.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`compartment_id`

(required) Compartment Identifier where the resource is created

`detector_rule_id`

(optional) Identifier of the rule

`l_region`

(optional) DEPRECATED

`regions`

(optional) Regions where the problem is found

`risk_level`

(optional) The Risk Level

Allowed values are: 'CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'MINOR'

`risk_score`

(optional) Risk Score for the problem

`peak_risk_score_date`

(optional) The date and time for the peak risk score that is observed. Format defined by RFC3339.

`peak_risk_score`

(optional) Peak risk score for the problem

`auto_resolve_date`

(optional) The date and time when the problem will be auto resolved. Format defined by RFC3339.

`peak_risk_score_lookup_period_in_days`

(optional) Number of days for which peak score is calculated for the problem

`resource_id`

(optional) Identifier of the Resource

`resource_name`

(optional) DisplayName of the Resource

`resource_type`

(optional) Type of the Resource

`labels`

(optional) user defined labels on the problem

`time_last_detected`

(optional) The date and time the problem was last detected. Format defined by RFC3339.

`time_first_detected`

(optional) The date and time the problem was first detected. Format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the Problem.

Allowed values are: 'ACTIVE', 'INACTIVE'

`lifecycle_detail`

(optional) The lifecycleDetail will give more detail on the substate of the lifecycleState.

Allowed values are: 'OPEN', 'RESOLVED', 'DISMISSED', 'DELETED'

`detector_id`

(optional) Id of the detector associated with the Problem.

Allowed values are: 'IAAS_ACTIVITY_DETECTOR', 'IAAS_CONFIGURATION_DETECTOR', 'IAAS_THREAT_DETECTOR', 'IAAS_LOG_INSIGHT_DETECTOR'

`target_id`

(optional) targetId of the problem

`additional_details`

(optional) The additional details of the Problem

`description`

(optional) Description of the problem

`recommendation`

(optional) Recommendation for the problem

`l_comment`

(optional) User Comments

`impacted_resource_id`

(optional) Identifier of the impacted Resource

`impacted_resource_name`

(optional) DisplayName of the impacted Resource

`impacted_resource_type`

(optional) Type of the impacted Resource

### DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_AGGREGATION_T Type

Provides the dimensions and their corresponding count value.

Syntax
```

```

Fields

Field Description

`dimensions_map`

(required) The key-value pairs of dimensions and their names.

`l_count`

(required) The number of occurences with given dimension/s

### DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_problem_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_AGGREGATION_COLLECTION_T Type

Problem Analytics data.

Syntax
```

```

Fields

Field Description

`items`

(required) The items consist of all the ProblemAggregation objects.

### DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_SUMMARY_T Type

Summary of the Problem.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`compartment_id`

(required) Compartment Identifier where the resource is created

`detector_rule_id`

(optional) Identifier of the rule

`risk_level`

(optional) The Risk Level

Allowed values are: 'CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'MINOR'

`risk_score`

(optional) Risk Score for the problem

`resource_id`

(optional) Identifier of the Resource

`resource_name`

(optional) DisplayName of the Resource

`resource_type`

(optional) Type of the Resource

`labels`

(optional) user defined labels on the problem

`time_first_detected`

(optional) The date and time the problem was first detected. Format defined by RFC3339.

`time_last_detected`

(optional) The date and time the problem was last detected. Format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the Problem.

Allowed values are: 'ACTIVE', 'INACTIVE'

`lifecycle_detail`

(optional) The lifecycleDetail will give more detail on the substate of the lifecycleState.

Allowed values are: 'OPEN', 'RESOLVED', 'DISMISSED', 'DELETED'

`detector_id`

(optional) Id of detector associated with the Problem.

Allowed values are: 'IAAS_ACTIVITY_DETECTOR', 'IAAS_CONFIGURATION_DETECTOR', 'IAAS_THREAT_DETECTOR', 'IAAS_LOG_INSIGHT_DETECTOR'

`l_region`

(optional) DEPRECATED

`regions`

(optional) Regions where the problem is found

`target_id`

(optional) targetId associated with the problem.

### DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_problem_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_COLLECTION_T Type

Collection of Problem

Syntax
```

```

Fields

Field Description

`items`

(required) List of ProblemSummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_ENDPOINT_SUMMARY_T Type

Problem endpoints summary.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier for problem endpoint.

`sighting_id`

(required) Unique id for sighting associated with the endpoint.

`problem_id`

(required) Unique id for cloudguard problem

`sighting_type`

(required) Identifier for the sighting type

`sighting_type_display_name`

(required) Display Name of the sighting type

`ip_address`

(required) IP Address of the Endpoint

`ip_address_type`

(required) IP Address type of the Endpoint

`ip_classification_type`

(optional) IP Address classification type of the endpoint

`country`

(optional) Country of the endpoint

`latitude`

(optional) Latitude of the endpoint

`longitude`

(optional) Longitude of the endpoint

`asn_number`

(optional) ASN number of the endpoint

`regions`

(optional) Regions where activities were performed from this IP

`services`

(optional) Services where activities were performed from this IP

`time_last_detected`

(required) Time when activities were last detected

### DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_ENDPOINT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_problem_endpoint_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_ENDPOINT_COLLECTION_T Type

Provides the list of problem endpoints

Syntax
```

```

Fields

Field Description

`items`

(required) List of problem endpoints

### DBMS_CLOUD_OCI_CLOUD_GUARD_ENTITY_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_entity_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_ENTITY_SUMMARY_T Type

The information about problem entities details of DataSource for a CloudGuard Problem.

Syntax
```

```

Fields

Field Description

`regions`

(required) Data source problem entities region

`time_first_detected`

(required) Data source problem entities first detected time

`problem_id`

(required) Attached problem id

`time_last_detected`

(required) Data source problem entities last detected time

`result_url`

(optional) Log result query url for a data source query

`entity_details`

(optional) List of event related to a DataSource

### DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_ENTITY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_problem_entity_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_ENTITY_COLLECTION_T Type

The collection of problem entities detail related to a data source.

Syntax
```

```

Fields

Field Description

`items`

(required) List of problem entities summaries related to a data source.

### DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_HISTORY_SUMMARY_T Type

Problem History Definition.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier for the history record

`problem_id`

(required) problemId for which history is associated to.

`actor_type`

(required) Actor type who performed the operation

Allowed values are: 'CLOUD_GUARD_SERVICE', 'CORRELATION', 'RESPONDER', 'USER'

`actor_name`

(required) Resource Name who performed activity

`explanation`

(required) Activity explanation details

`lifecycle_detail`

(required) Problem Lifecycle Detail Status

Allowed values are: 'OPEN', 'RESOLVED', 'DISMISSED', 'DELETED'

`event_status`

(optional) Event status

Allowed values are: 'REOPEN', 'OPEN', 'UPDATE', 'RESOLVE', 'DISMISS', 'DELETE'

`time_created`

(required) Type of the Entity

`delta`

(required) Impacted Resource Names in a comma-separated string.

`l_comment`

(optional) User Defined Comments

### DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_HISTORY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_problem_history_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_HISTORY_COLLECTION_T Type

Collection of Problem History

Syntax
```

```

Fields

Field Description

`items`

(required) List of ProblemHistorySummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_TREND_AGGREGATION_T Type

Provides the dimensions and their corresponding time and count.

Syntax
```

```

Fields

Field Description

`dimensions_map`

(required) The key-value pairs of dimensions and their names.

`start_timestamp`

(required) Start Time in epoch seconds

`duration_in_seconds`

(required) Duration

`l_count`

(required) The number of occurences with for the corresponding time range and dimensions.

### DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_TREND_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_problem_trend_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_TREND_AGGREGATION_COLLECTION_T Type

Problem Trend Aggregation Collection.

Syntax
```

```

Fields

Field Description

`items`

(required) The items consist of all the ProblemTrendAggregation objects.

### DBMS_CLOUD_OCI_CLOUD_GUARD_RECOMMENDATION_SUMMARY_T Type

Recommendation Definition.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier for Recommendation

`l_type`

(optional) Recommendation type

Allowed values are: 'DETECTOR_PROBLEMS', 'RESOLVED_PROBLEMS'

`tenant_id`

(optional) Tenant Identifier

`compartment_id`

(required) Compartment Identifier

`target_id`

(required) targetId associated with the problem

`details`

(required) Recommendation details

`risk_level`

(optional) The Risk Level

Allowed values are: 'CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'MINOR'

`problem_count`

(required) Count number of the problem

`lifecycle_state`

(required) The current state of the Recommendation.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_detail`

(required) The lifecycleDetail will give more detail on the substate of the lifecycleState.

Allowed values are: 'OPEN', 'RESOLVED', 'DISMISSED'

`time_created`

(optional) problem creating time

`time_updated`

(optional) problem updating time

`name`

(required) recommendation string showing on UX

`description`

(required) description of the recommendation

### DBMS_CLOUD_OCI_CLOUD_GUARD_RECOMMENDATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_recommendation_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_RECOMMENDATION_SUMMARY_COLLECTION_T Type

Collection of the RecommendationSummary

Syntax
```

```

Fields

Field Description

`items`

(required) List of Recommendation

### DBMS_CLOUD_OCI_CLOUD_GUARD_REMOVE_COMPARTMENT_DETAILS_T Type

An existing compartment to remove from a security zone

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to be removed from SecurityZone.

### DBMS_CLOUD_OCI_CLOUD_GUARD_REQUEST_SUMMARIZED_TREND_RESOURCE_RISK_SCORES_DETAILS_T Type

ResourceRiskScores filter.

Syntax
```

```

Fields

Field Description

`filter`

(required) The filter type.

Allowed values are: 'PROBLEM_ID', 'RESOURCE_PROFILE_ID'

`filter_id`

(required) Id to be passed in to filter the risk scores.

### DBMS_CLOUD_OCI_CLOUD_GUARD_TACTIC_SUMMARY_T Type

Tactic summary.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier for the tactic.

`display_name`

(required) Display name of the tactic

### DBMS_CLOUD_OCI_CLOUD_GUARD_TACTIC_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_tactic_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_T Type

Resource profile details

Syntax
```

```

Fields

Field Description

`sightings_count`

(optional) Number of sightings associated with this resource profile

`id`

(required) Unique identifier for resource profile

`resource_id`

(required) Unique identifier for resource profile

`display_name`

(required) Resource name for resource profile

`l_type`

(required) Resource type for resource profile

`problem_ids`

(optional) List of Problems associated with the resource profile.

`compartment_id`

(required) Compartment Id for resource profile

`target_id`

(optional) Target Id for resource profile

`risk_score`

(required) Risk Score for the resource profile

`risk_level`

(optional) Risk Level associated with resource profile

Allowed values are: 'CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'MINOR'

`peak_risk_score`

(optional) Peak Risk Score for the resource profile

`time_peak_score`

(optional) The date and time for peak risk score. Format defined by RFC3339.

`time_first_detected`

(required) The date and time the resource profile was first detected. Format defined by RFC3339.

`time_last_detected`

(required) The date and time the resource profile was last detected. Format defined by RFC3339.

`tactics`

(required) List of tactic summary associated with the resource profile.

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_SUMMARY_T Type

Resource profile summary.

Syntax
```

```

Fields

Field Description

`sightings_count`

(optional) Number of sightings associated with this resource profile

`id`

(required) Unique identifier for resource profile

`resource_id`

(required) Unique identifier for resource profile

`display_name`

(required) Resource name for resource profile

`l_type`

(required) Resource type for resource profile

`risk_score`

(required) Risk Score for the resource profile

`tactics`

(required) List of tactic summary associated with the resource profile.

`time_first_detected`

(required) The date and time the resource profile was first detected. Format defined by RFC3339.

`time_last_detected`

(required) The date and time the resource profile was last detected. Format defined by RFC3339.

`problems_count`

(optional) Number of problems associated with this resource profile

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_resource_profile_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_COLLECTION_T Type

Collection of resource profile summary.

Syntax
```

```

Fields

Field Description

`items`

(required) List of resource profiles

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_ENDPOINT_SUMMARY_T Type

Resource Profile Endpoints summary.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier for sighting endpoints

`resource_profile_id`

(required) Resource profile Id associated with the imacted resource

`problem_id`

(optional) Problem Id for sighting endpoints

`sighting_type`

(required) Identifier for the sighting type

`sighting_type_display_name`

(required) Name of the sighting type

`ip_address`

(required) IP Address

`ip_address_type`

(required) IP Address type

`ip_classification_type`

(optional) IP Address classification type

`country`

(optional) Country

`latitude`

(optional) Latitude

`longitude`

(optional) Longitude

`asn_number`

(optional) ASN number

`regions`

(optional) Regions where activities were performed from this IP

`services`

(optional) Services where activities were performed from this IP

`time_last_detected`

(required) Time when activities were created

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_ENDPOINT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_resource_profile_endpoint_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_ENDPOINT_COLLECTION_T Type

Collection of Resource Profile endpoint summaries

Syntax
```

```

Fields

Field Description

`items`

(required) List of ResourceProfileEndpointSummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_IMPACTED_RESOURCE_SUMMARY_T Type

Resource Profile impacted resource summary.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier for impacted resource

`resource_profile_id`

(required) Resource profile Id associated with the imacted resource

`problem_id`

(optional) Problem Id for impacted resource

`compartment_id`

(required) Compartment Id for impacted resource

`resource_id`

(required) Impacted resource Id

`resource_name`

(required) Resource name

`resource_type`

(required) Resource type

`sighting_type`

(required) Identifier for the sighting type

`sighting_type_display_name`

(required) Name of the sighting type

`l_region`

(required) Region for impacted resource

`time_identified`

(required) Time when the impacted resource is identified for given resource profile.

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_IMPACTED_RESOURCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_resource_profile_impacted_resource_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_IMPACTED_RESOURCE_COLLECTION_T Type

Collection of resource profile impacted resource summaries

Syntax
```

```

Fields

Field Description

`items`

(required) List of ResourceProfileImpactedResourceSummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_RISK_SCORE_AGGREGATION_T Type

Risk score of a resource.

Syntax
```

```

Fields

Field Description

`tactics`

(required) Tactics used for evaluating the risk scrore

`score_timestamp`

(required) The date and time for which the score is calculated. Format defined by RFC3339.

`risk_score`

(required) Risk Score

`risk_level`

(required) The Risk Level

Allowed values are: 'CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'MINOR'

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_RISK_SCORE_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_resource_risk_score_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_RISK_SCORE_AGGREGATION_SUMMARY_T Type

Resource profile risk score trend-line

Syntax
```

```

Fields

Field Description

`resource_profile_id`

(required) OCID for the resource profile

`resource_profile_display_name`

(required) Display name for the resource profile

`risk_threshold`

(optional) Risk threshold

`items`

(required) List of ResourceRiskScoreAggregation

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_RISK_SCORE_AGGREGATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_resource_profile_risk_score_aggregation_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_RISK_SCORE_AGGREGATION_SUMMARY_COLLECTION_T Type

Collection of resource profile risk score trends.

Syntax
```

```

Fields

Field Description

`items`

(required) List of ResourceProfileRiskScoreAggregationSummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_RISK_SCORE_AGGREGATION_COLLECTION_T Type

Collection of Resource risk scores

Syntax
```

```

Fields

Field Description

`filter_type`

(required) Type of filter. Valid Values - problem_id and resource_id

`filter_id`

(required) Id value on which risk scores are filtered

`risk_threshold`

(optional) Risk Score

`items`

(required) List of ResourceRiskScoreAggregation

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_TYPE_COLLECTION_T Type

resource type provided by cloud guard

Syntax
```

```

Fields

Field Description

`items`

(required) collection of resource types

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_ACTIVITY_SUMMARY_T Type

Responder Activity summary Definition.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique id for Responder activity.

`problem_id`

(required) problemId for which Responder activity is associated to.

`responder_rule_id`

(required) Id of the responder rule for the problem

`responder_type`

(required) responder rule type for performing the operation

Allowed values are: 'REMEDIATION', 'NOTIFICATION'

`responder_rule_name`

(required) responder rule name

`responder_activity_type`

(required) Responder activity types

Allowed values are: 'STARTED', 'COMPLETED'

`responder_execution_status`

(required) the responder execution status

Allowed values are: 'STARTED', 'AWAITING_CONFIRMATION', 'AWAITING_INPUT', 'SUCCEEDED', 'FAILED', 'SKIPPED', 'ALL'

`time_created`

(required) responder activity starting time

`message`

(required) additional message related to this operation

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_ACTIVITY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_responder_activity_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_ACTIVITY_COLLECTION_T Type

Provides the summary of responder activities and their corresponding count value.

Syntax
```

```

Fields

Field Description

`items`

(required) List of ResponderActivitySummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RULE_EXECUTION_DETAILS_T Type

Details of ResponderRuleExecution. A Responder Rule Execution is the entity that captures the execution of a Responder Rule for a given Problem.

Syntax
```

```

Fields

Field Description

`condition`

(optional)

`configurations`

(optional) ResponderRule configurations

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_EXECUTION_T Type

Responder Execution Object.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier of the responder execution

`responder_rule_id`

(required) Responder Rule id for the responder execution

`responder_rule_type`

(required) Rule Type for the responder execution

Allowed values are: 'REMEDIATION', 'NOTIFICATION'

`responder_rule_name`

(required) Rule name for the responder execution

`problem_id`

(required) Problem id associated with the responder execution

`l_region`

(required) region where the problem is found

`target_id`

(required) targetId of the problem for the responder execution

`compartment_id`

(required) compartment id of the responder execution for the problem

`resource_type`

(required) resource type of the problem for the responder execution

`resource_name`

(required) resource name of the problem for the responder execution. TODO-DOC link to resource definition doc

`time_created`

(required) The date and time the responder execution was created. Format defined by RFC3339.

`time_completed`

(optional) The date and time the responder execution was updated. Format defined by RFC3339.

`responder_execution_status`

(required) current execution status of the responder

Allowed values are: 'STARTED', 'AWAITING_CONFIRMATION', 'AWAITING_INPUT', 'SUCCEEDED', 'FAILED', 'SKIPPED', 'ALL'

`responder_execution_mode`

(required) execution mode of the responder

Allowed values are: 'MANUAL', 'AUTOMATED', 'ALL'

`message`

(optional) Message about the responder execution.

`responder_rule_execution_details`

(optional)

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_EXECUTION_AGGREGATION_T Type

Provides the dimensions and their corresponding count value.

Syntax
```

```

Fields

Field Description

`dimensions_map`

(required) The key-value pairs of dimensions and their names. The key corresponds to the Analytic Dimension(s) chosen, and the value corresponds to the value of the dimension from the data. E.g. if the Analytic Dimension chosen is \"RISK_LEVEL\", then the value will be like \"CRITICAL\". If the Analytic Dimensions chosen are \"RISK_LEVEL\" and \"RESOURCE_TYPE\", then the map will have two key-value pairs of form {\"RISK_LEVEL\" &amp;#58; \"CRITICAL, \"RESOURCE_TYPE\" &amp;#58; \"LOAD_BALANCER\"}

`l_count`

(required) The number of occurences with given dimension(s)

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_EXECUTION_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_responder_execution_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_EXECUTION_AGGREGATION_COLLECTION_T Type

Collection of ResponderExecutionAggregation objects

Syntax
```

```

Fields

Field Description

`items`

(required) The items consist of all the ResponderExecutionAggregation objects.

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_EXECUTION_SUMMARY_T Type

Summary of the Responder Execution.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier of the responder execution

`responder_rule_id`

(required) Responder Rule id for the responder execution

`responder_rule_type`

(required) Rule Type for the responder execution

Allowed values are: 'REMEDIATION', 'NOTIFICATION'

`responder_rule_name`

(required) Rule name for the responder execution

`problem_id`

(required) Problem id associated with the responder execution

`problem_name`

(required) Problem name associated with the responder execution

`l_region`

(required) Region where the problem is found

`target_id`

(required) Target Id of the problem for the responder execution

`compartment_id`

(required) compartment id of the problem for the responder execution

`resource_type`

(required) resource type of the problem for the responder execution

`resource_name`

(required) resource name of the problem for the responder execution. TODO-DOC link to resource definition doc

`time_created`

(required) The date and time the responder execution was created. Format defined by RFC3339.

`time_completed`

(optional) The date and time the responder execution was updated. Format defined by RFC3339.

`responder_execution_status`

(required) current execution status of the responder

Allowed values are: 'STARTED', 'AWAITING_CONFIRMATION', 'AWAITING_INPUT', 'SUCCEEDED', 'FAILED', 'SKIPPED', 'ALL'

`responder_execution_mode`

(required) possible type of responder execution modes

Allowed values are: 'MANUAL', 'AUTOMATED', 'ALL'

`message`

(optional) Message about the responder execution.

`responder_rule_execution_details`

(optional)

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_EXECUTION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_responder_execution_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_EXECUTION_COLLECTION_T Type

Provides the summary of responder executions and their corresponding count value.

Syntax
```

```

Fields

Field Description

`items`

(required) List of ResponderExecutionSummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_EXECUTION_TREND_AGGREGATION_T Type

Provides the timestamps and their corresponding number of remediations.

Syntax
```

```

Fields

Field Description

`dimensions_map`

(required) The key-value pairs of dimensions and their names.

`start_timestamp`

(required) Start Time in epoch seconds

`duration_in_seconds`

(required) Duration

`l_count`

(required) The number of remediations for a given time.

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_EXECUTION_TREND_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_responder_execution_trend_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_EXECUTION_TREND_AGGREGATION_COLLECTION_T Type

Responder Execution Trend Collection

Syntax
```

```

Fields

Field Description

`items`

(required) The items consist of all the ResponderExecutionTrendAggregation objects.

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RULE_DETAILS_T Type

Details of ResponderRule.

Syntax
```

```

Fields

Field Description

`condition`

(optional)

`configurations`

(optional) ResponderRule configurations

`is_enabled`

(required) Identifies state for ResponderRule

`l_mode`

(optional) Execution Mode for ResponderRule

Allowed values are: 'AUTOACTION', 'USERACTION'

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RECIPE_RESPONDER_RULE_T Type

Details of ResponderRule.

Syntax
```

```

Fields

Field Description

`responder_rule_id`

(required) Identifier for ResponderRule.

`display_name`

(optional) ResponderRule display name.

`description`

(optional) ResponderRule description.

`l_type`

(optional) Type of Responder

Allowed values are: 'REMEDIATION', 'NOTIFICATION'

`policies`

(optional) List of Policy

`supported_modes`

(optional) Supported Execution Modes

Allowed values are: 'AUTOACTION', 'USERACTION'

`details`

(optional)

`compartment_id`

(required) Compartment Identifier

`time_created`

(optional) The date and time the responder recipe rule was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the responder recipe rule was updated. Format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the ResponderRule.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RECIPE_RESPONDER_RULE_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_responder_recipe_responder_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RECIPE_T Type

Details of ResponderRecipe.

Syntax
```

```

Fields

Field Description

`id`

(required) Identifier for ResponderRecipe.

`display_name`

(optional) ResponderRecipe display name.

`description`

(optional) ResponderRecipe description.

`owner`

(optional) Owner of ResponderRecipe

Allowed values are: 'CUSTOMER', 'ORACLE'

`responder_rules`

(optional) List of responder rules associated with the recipe

`effective_responder_rules`

(optional) List of responder rules associated with the recipe

`source_responder_recipe_id`

(optional) The id of the source responder recipe.

`compartment_id`

(required) Compartment Identifier

`time_created`

(optional) The date and time the responder recipe was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the responder recipe was updated. Format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the Example.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RECIPE_SUMMARY_T Type

Summary of the ResponderRecipe.

Syntax
```

```

Fields

Field Description

`id`

(required) Identifier for ResponderRecipe.

`display_name`

(optional) ResponderRecipe display name.

`description`

(optional) ResponderRecipe description.

`owner`

(optional) Owner of ResponderRecipe

Allowed values are: 'CUSTOMER', 'ORACLE'

`responder_rules`

(optional) List of responder rules associated with the recipe

`source_responder_recipe_id`

(optional) The id of the source responder recipe.

`compartment_id`

(required) Compartment Identifier

`time_created`

(optional) The date and time the responder recipe was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the responder recipe was updated. Format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the Example.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RECIPE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_responder_recipe_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RECIPE_COLLECTION_T Type

Summary of the ResponderRecipe.

Syntax
```

```

Fields

Field Description

`items`

(required) List of ResponderRecipeSummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RECIPE_RESPONDER_RULE_SUMMARY_T Type

Details of ResponderRule.

Syntax
```

```

Fields

Field Description

`id`

(required) Identifier for ResponderRule.

`display_name`

(optional) ResponderRule Display Name

`description`

(optional) ResponderRule Description

`l_type`

(optional) Type of Responder

Allowed values are: 'REMEDIATION', 'NOTIFICATION'

`policies`

(optional) List of Policy

`supported_modes`

(optional) Supported Execution Modes

Allowed values are: 'AUTOACTION', 'USERACTION'

`details`

(optional)

`compartment_id`

(required) Compartment Identifier

`time_created`

(optional) The date and time the responder recipe rule was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the responder recipe rule was updated. Format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the ResponderRule.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RECIPE_RESPONDER_RULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_responder_recipe_responder_rule_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RECIPE_RESPONDER_RULE_COLLECTION_T Type

Summary of the ResponderRule within ResponderRecipe.

Syntax
```

```

Fields

Field Description

`items`

(required) List of ResponderRecipeResponderRuleSummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RULE_T Type

Definition of ResponderRule.

Syntax
```

```

Fields

Field Description

`id`

(required) Identifier for ResponderRule.

`display_name`

(required) ResponderRule Display Name

`description`

(required) ResponderRule Description

`l_type`

(required) Type of Responder

Allowed values are: 'REMEDIATION', 'NOTIFICATION'

`policies`

(optional) List of Policy

`supported_modes`

(optional) Supported Execution Modes

Allowed values are: 'AUTOACTION', 'USERACTION'

`details`

(optional)

`time_created`

(optional) The date and time the responder rule was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the responder rule was updated. Format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the ResponderRule.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RULE_SUMMARY_T Type

Summary of the ResponderRule.

Syntax
```

```

Fields

Field Description

`id`

(required) Identifier for ResponderRule.

`display_name`

(required) ResponderRule Display Name

`description`

(required) ResponderRule Description

`l_type`

(required) Type of Responder

Allowed values are: 'REMEDIATION', 'NOTIFICATION'

`policies`

(optional) List of Policy

`supported_modes`

(optional) Supported Execution Modes

Allowed values are: 'AUTOACTION', 'USERACTION'

`details`

(optional)

`time_created`

(optional) The date and time the responder rule was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the responder rule was updated. Format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the ResponderRule.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_responder_rule_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RULE_COLLECTION_T Type

Summary of the ResponderRule.

Syntax
```

```

Fields

Field Description

`items`

(required) List of ResponderRuleSummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_RISK_SCORE_AGGREGATION_T Type

Provides the dimensions and their corresponding risk score.

Syntax
```

```

Fields

Field Description

`dimensions_map`

(required) The key-value pairs of dimensions and their names.

`risk_score`

(required) The risk score with given dimensions

### DBMS_CLOUD_OCI_CLOUD_GUARD_RISK_SCORE_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_risk_score_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_RISK_SCORE_AGGREGATION_COLLECTION_T Type

Risk Score Aggregation Collection.

Syntax
```

```

Fields

Field Description

`items`

(required) The items consist of all the RiskScoreAggregation objects.

### DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_POLICY_T Type

A security policy defines a security requirement for resources in a security zone. If a security zone enables a policy (using a recipe), then any action that attempts to violate that policy is denied.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`friendly_name`

(optional) A shorter version of the security policy's name

`display_name`

(optional) The security policy's full name

`description`

(optional) The security policy's description

`compartment_id`

(required) The id of the security policy's compartment

`owner`

(required) The owner of the security policy

Allowed values are: 'CUSTOMER', 'ORACLE'

`category`

(optional) The category of security policy

`services`

(optional) The list of services that the security policy protects

`time_created`

(optional) The time the security policy was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the security policy was last updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the security policy

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, this can be used to provide actionable information for a resource in a `Failed` state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_POLICY_SUMMARY_T Type

Summary information for a security zone policy. A security policy defines a security requirement for resources in a security zone. If a security zone enables a policy (using a recipe), then any action that attempts to violate that policy is denied.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`friendly_name`

(optional) A shorter version of the security policy's name

`display_name`

(optional) The security policy's full name

`description`

(optional) The security policy's description

`compartment_id`

(required) The id of the security policy's compartment

`owner`

(required) The owner of the security policy

Allowed values are: 'CUSTOMER', 'ORACLE'

`category`

(optional) The category of security policy

`services`

(optional) The list of services that the security policy protects

`time_created`

(optional) The time the security policy was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the security policy was last updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the security policy

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, this can be used to provide actionable information for a policy in the `Failed` state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_POLICY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_security_policy_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_POLICY_COLLECTION_T Type

Results of a security policy search. Contains `SecurityPolicySummary` items.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of security policy summaries

### DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_RECIPE_T Type

A security zone recipe is a collection of security zone policies. Oracle Cloud Infrastructure enforces these policies on security zones that use the recipe.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`display_name`

(optional) The recipe's name

`description`

(optional) The recipe's description

`compartment_id`

(required) The id of the compartment that contains the recipe

`owner`

(required) The owner of the recipe

Allowed values are: 'CUSTOMER', 'ORACLE'

`security_policies`

(required) The list of `SecurityPolicy` ids that are included in the recipe

`time_created`

(optional) The time the recipe was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the recipe was last updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the recipe

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, this can be used to provide actionable information for a recipe in the `Failed` state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_RECIPE_SUMMARY_T Type

Summary information for a security zone recipe. A security zone recipe is a collection of security zone policies. Oracle Cloud Infrastructure enforces these policies on security zones that use the recipe.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`display_name`

(optional) The recipe's name

`description`

(optional) The recipe's description

`compartment_id`

(required) The id of the compartment that contains the recipe

`owner`

(required) The owner of the recipe

Allowed values are: 'CUSTOMER', 'ORACLE'

`security_policies`

(required) The list of `SecurityPolicy` ids that are included in the recipe

`time_created`

(optional) The time the recipe was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the recipe was last updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the recipe

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, this can be used to provide actionable information for a recipe in the `Failed` state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_RECIPE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_security_recipe_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_RECIPE_COLLECTION_T Type

Results of a security zone recipe search. Contains `SecurityRecipeSummary` items.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of security zone recipe summaries

### DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_SCORE_AGGREGATION_T Type

Provides the dimensions and their corresponding count value.

Syntax
```

```

Fields

Field Description

`dimensions_map`

(required) The key-value pairs of dimensions and their names.

`security_rating`

(required) The security rating with given dimension/s

Allowed values are: 'EXCELLENT', 'GOOD', 'FAIR', 'POOR', 'NA'

`security_score`

(required) The security score with given dimension/s

### DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_SCORE_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_security_score_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_SCORE_AGGREGATION_COLLECTION_T Type

Security Score Aggregation Collection.

Syntax
```

```

Fields

Field Description

`items`

(required) The items consist of all the SecurityScoreAggregation objects.

### DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_SCORE_TREND_AGGREGATION_T Type

Provides the dimensions and their corresponding time and security score.

Syntax
```

```

Fields

Field Description

`dimensions_map`

(required) The key-value pairs of dimensions and their names.

`start_timestamp`

(required) Start Time in epoch seconds

`duration_in_seconds`

(required) Duration

`security_rating`

(required) The security rating with given dimensions and time range

Allowed values are: 'EXCELLENT', 'GOOD', 'FAIR', 'POOR', 'NA'

`security_score`

(required) The security score with given dimensions and time range

### DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_SCORE_TREND_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_security_score_trend_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_SCORE_TREND_AGGREGATION_COLLECTION_T Type

Security Score Trend Aggregation Collection.

Syntax
```

```

Fields

Field Description

`items`

(required) The items consist of all the SecurityScoreTrendAggregation objects.

### DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_ZONE_T Type

A security zone is associated with a security zone recipe and enforces all security zone policies in the recipe. Any actions in the zone's compartment (and any subcompartments in the zone) that violate a policy are denied.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`display_name`

(optional) The security zone's name

`description`

(optional) The security zone's description

`compartment_id`

(required) The OCID of the compartment for the security zone

`security_zone_recipe_id`

(required) The OCID of the recipe (`SecurityRecipe`) for the security zone

`security_zone_target_id`

(optional) The OCID of the target associated with the security zone

`inherited_by_compartments`

(optional) List of inherited compartments

`time_created`

(optional) The time the security zone was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the security zone was last updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the security zone

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, this can be used to provide actionable information for a zone in the `Failed` state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_ZONE_SUMMARY_T Type

Summary information for a security zone. A security zone is associated with a security zone recipe and enforces all security zone policies in the recipe. Any actions in the zone's compartment (and any subcompartments in the zone) that violate a policy are denied.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`display_name`

(optional) The security zone's name

`description`

(optional) The security zone's description

`compartment_id`

(required) The OCID of the compartment for the security zone

`security_zone_recipe_id`

(required) The OCID of the recipe (`SecurityRecipe`) for the security zone

`time_created`

(optional) The time the security zone was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the security zone was last updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the security zone

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, this can be used to provide actionable information for a zone in the `Failed` state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_ZONE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_security_zone_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_ZONE_COLLECTION_T Type

Results of a security zone search. Contains `SecurityZoneSummary` items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of security zone summaries

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_DETAILS_T Type

Details specific to the target type.

Syntax
```

```

Fields

Field Description

`target_resource_type`

(required) Possible type of targets.

Allowed values are: 'COMPARTMENT', 'ERPCLOUD', 'HCMCLOUD', 'SECURITY_ZONE'

### DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_RECIPE_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_security_recipe_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_ZONE_TARGET_DETAILS_T Type

Details about Security Zone Target.

Syntax
```

```

`dbms_cloud_oci_cloud_guard_security_zone_target_details_t`is a subtype of the`dbms_cloud_oci_cloud_guard_target_details_t`type.

Fields

Field Description

`security_zone_id`

(optional) The OCID of the security zone to associate this compartment with.

`security_zone_display_name`

(optional) The name of the security zone to associate this compartment with.

`target_security_zone_recipes`

(optional) The list of security zone recipes to associate this compartment with.

### DBMS_CLOUD_OCI_CLOUD_GUARD_SIGHTING_T Type

Sighting details.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier for sighting event

`description`

(required) Description of the sighting event

`problem_id`

(optional) Problem Id to which the Sighting is associated

`compartment_id`

(required) Compartment Id where the resource is created

`actor_principal_id`

(optional) Unique identifier for principal actor

`actor_principal_name`

(optional) Name of the principal actor

`actor_principal_type`

(optional) Type of the principal actor

`classification_status`

(required) ClassificationStatus of the sighting event

Allowed values are: 'FALSE_NEGATIVE', 'TRUE_NEGATIVE', 'FALSE_POSITIVE', 'TRUE_POSITIVE', 'NOT_CLASSIFIED'

`sighting_type`

(required) Identifier for the sighting type

`sighting_type_display_name`

(required) Display name of the sighting type

`tactic_name`

(required) Name of the Mitre att&amp;ck tactic

`technique_name`

(required) Name of the Mitre att&amp;ck technique

`sighting_score`

(required) Score for the sighting

`severity`

(required) Severity of the sighting

Allowed values are: 'CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'MINOR'

`confidence`

(required) Confidence of the sighting

Allowed values are: 'CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'MINOR'

`time_first_detected`

(required) The date and time the sighting was first detected. Format defined by RFC3339.

`time_last_detected`

(required) The date and time the sighting was last detected. Format defined by RFC3339.

`regions`

(required) regions involved in the sighting

`additional_details`

(optional) The additional details of the Sighting

### DBMS_CLOUD_OCI_CLOUD_GUARD_SIGHTING_SUMMARY_T Type

Sighting summary Definition.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier for finding event

`compartment_id`

(required) Compartment Id where the resource is created

`problem_id`

(optional) Problem Id to which the Sighting is associated

`actor_principal_id`

(optional) Unique identifier for principal actor

`actor_principal_name`

(optional) Name of the principal actor

`actor_principal_type`

(optional) Type of the principal actor

`detector_rule_id`

(required) Unique identifier of the rule

`classification_status`

(required) ClassificationStatus of the sighting event

Allowed values are: 'FALSE_NEGATIVE', 'TRUE_NEGATIVE', 'FALSE_POSITIVE', 'TRUE_POSITIVE', 'NOT_CLASSIFIED'

`sighting_type`

(required) Identifier for the sighting type

`sighting_type_display_name`

(required) Name of the sighting type

`tactic_name`

(required) Name of the Mitre att&amp;ck tactic

`technique_name`

(required) Name of the Mitre att&amp;ck technique

`sighting_score`

(required) Score for the sighting

`severity`

(required) Severity of the sighting

Allowed values are: 'CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'MINOR'

`confidence`

(required) Confidence of the sighting

Allowed values are: 'CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'MINOR'

`time_first_detected`

(required) The date and time the sighting was first detected. Format defined by RFC3339.

`time_last_detected`

(required) The date and time the sighting was last detected. Format defined by RFC3339.

`regions`

(required) Regions involved in the sighting

### DBMS_CLOUD_OCI_CLOUD_GUARD_SIGHTING_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_sighting_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_SIGHTING_COLLECTION_T Type

Provides the summary of sighting

Syntax
```

```

Fields

Field Description

`items`

(required) List of SightingSummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_SIGHTING_ENDPOINT_SUMMARY_T Type

Sighting Endpoints summary.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier for sighting endpoints

`sighting_id`

(required) Sighitng Id for sighting endpoints

`problem_id`

(optional) Problem Id for sighting endpoints

`ip_address`

(required) IP Address

`ip_address_type`

(required) IP Address type

`ip_classification_type`

(optional) IP Address classification type

`country`

(optional) Country

`latitude`

(optional) Latitude

`longitude`

(optional) Longitude

`asn_number`

(optional) ASN number

`regions`

(optional) Regions where activities were performed from this IP

`services`

(optional) Services where activities were performed from this IP

`time_last_detected`

(required) Time when activities were created

### DBMS_CLOUD_OCI_CLOUD_GUARD_SIGHTING_ENDPOINT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_sighting_endpoint_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_SIGHTING_ENDPOINT_COLLECTION_T Type

Provides the summary of sighting endpoints

Syntax
```

```

Fields

Field Description

`items`

(required) List of SightingEndpointSummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_SIGHTING_IMPACTED_RESOURCE_SUMMARY_T Type

Sighting Impacted Resource summary.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier for impacted resource

`resource_id`

(required) Impacted resource Id

`sighting_id`

(required) Sighting Id

`problem_id`

(optional) Problem Id for impacted resource

`compartment_id`

(required) Compartment Id for impacted resource

`resource_name`

(required) Resource name

`resource_type`

(required) Resource type

`l_region`

(required) Region for impacted resource

`time_identified`

(required) Time when the impacted resource is identified for given sighting.

### DBMS_CLOUD_OCI_CLOUD_GUARD_SIGHTING_IMPACTED_RESOURCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_sighting_impacted_resource_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_SIGHTING_IMPACTED_RESOURCE_COLLECTION_T Type

Provides the summary of sighting impacted resource

Syntax
```

```

Fields

Field Description

`items`

(required) List of SightingImpactedResourceSummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_SIMPLE_CONDITION_T Type

Simple Condition object.

Syntax
```

```

`dbms_cloud_oci_cloud_guard_simple_condition_t`is a subtype of the`dbms_cloud_oci_cloud_guard_condition_t`type.

Fields

Field Description

`parameter`

(optional) parameter Key

`operator`

(optional) type of operator

Allowed values are: 'IN', 'NOT_IN', 'EQUALS', 'NOT_EQUALS'

`value`

(optional) type of operator

`value_type`

(optional) type of value

Allowed values are: 'MANAGED', 'CUSTOM'

### DBMS_CLOUD_OCI_CLOUD_GUARD_SKIP_BULK_RESPONDER_EXECUTION_DETAILS_T Type

List of responder execution ids to skip the execution

Syntax
```

```

Fields

Field Description

`responder_execution_ids`

(required) List of responder execution ids to skip the execution

### DBMS_CLOUD_OCI_CLOUD_GUARD_TACTIC_COLLECTION_T Type

Collection of tactic summaries in Cloud Guard

Syntax
```

```

Fields

Field Description

`items`

(required) List of tactic summary.

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_DETECTOR_DETAILS_T Type

Overriden settings of a Detector Rule applied on target

Syntax
```

```

Fields

Field Description

`is_enabled`

(required) Enables the control

`risk_level`

(optional) The Risk Level

Allowed values are: 'CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'MINOR'

`configurations`

(optional) Configuration details

`condition_groups`

(optional) Condition group corresponding to each compartment

`labels`

(optional) user defined labels for a detector rule

`is_configuration_allowed`

(optional) configuration allowed or not

`problem_threshold`

(optional) Cutover point for an elevated resource Risk Score to create a Problem

`target_types`

(optional) List of target types for which the detector rule is applicable

`sighting_types`

(optional) List of sighting types

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_DETECTOR_RECIPE_DETECTOR_RULE_T Type

Detector Recipe Rule

Syntax
```

```

Fields

Field Description

`detector_rule_id`

(required) The unique identifier of the detector rule.

`display_name`

(optional) Display name for TargetDetectorRecipeDetectorRule. information.

`description`

(optional) Description for TargetDetectorRecipeDetectorRule. information.

`recommendation`

(optional) Recommendation for TargetDetectorRecipeDetectorRule

`detector`

(required) detector for the rule

Allowed values are: 'IAAS_ACTIVITY_DETECTOR', 'IAAS_CONFIGURATION_DETECTOR', 'IAAS_THREAT_DETECTOR', 'IAAS_LOG_INSIGHT_DETECTOR'

`service_type`

(required) service type of the configuration to which the rule is applied

`resource_type`

(required) resource type of the configuration to which the rule is applied

`details`

(optional)

`managed_list_types`

(optional) List of cloudguard managed list types related to this rule

Allowed values are: 'CIDR_BLOCK', 'USERS', 'GROUPS', 'IPV4ADDRESS', 'IPV6ADDRESS', 'RESOURCE_OCID', 'REGION', 'COUNTRY', 'STATE', 'CITY', 'TAGS', 'GENERIC'

`time_created`

(optional) The date and time the target detector recipe rule was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the target detector recipe rule was updated. Format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the DetectorRule.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`data_source_id`

(optional) The id of the attached DataSource.

`entities_mappings`

(optional) Data Source entities mapping for a Detector Rule

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_DETECTOR_RECIPE_DETECTOR_RULE_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_target_detector_recipe_detector_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_DETECTOR_RECIPE_T Type

Target Detector recipe

Syntax
```

```

Fields

Field Description

`id`

(required) Ocid for detector recipe

`display_name`

(required) Display name of detector recipe.

`description`

(optional) Detector recipe description.

`compartment_id`

(required) compartmentId of detector recipe

`detector_recipe_id`

(required) Unique identifier for Detector Recipe of which this is an extension

`owner`

(required) Owner of detector recipe

Allowed values are: 'CUSTOMER', 'ORACLE'

`detector`

(required) Type of detector

Allowed values are: 'IAAS_ACTIVITY_DETECTOR', 'IAAS_CONFIGURATION_DETECTOR', 'IAAS_THREAT_DETECTOR', 'IAAS_LOG_INSIGHT_DETECTOR'

`detector_rules`

(optional) List of detector rules for the detector type for recipe - user input

`effective_detector_rules`

(optional) List of effective detector rules for the detector type for recipe after applying defaults

`time_created`

(optional) The date and time the target detector recipe was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the target detector recipe was updated. Format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`source_data_retention`

(optional) The number of days for which source data is retained

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_RESPONDER_RECIPE_RESPONDER_RULE_T Type

Details of ResponderRule.

Syntax
```

```

Fields

Field Description

`responder_rule_id`

(required) Unique ResponderRule identifier.

`display_name`

(optional) ResponderRule display name.

`description`

(optional) ResponderRule description.

`l_type`

(optional) Type of Responder

Allowed values are: 'REMEDIATION', 'NOTIFICATION'

`policies`

(optional) List of Policy

`supported_modes`

(optional) Supported Execution Modes

Allowed values are: 'AUTOACTION', 'USERACTION'

`details`

(optional)

`compartment_id`

(required) Compartment Identifier

`time_created`

(optional) The date and time the target responder recipe rule was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the target responder recipe rule was updated. Format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the ResponderRule.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_RESPONDER_RECIPE_RESPONDER_RULE_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_target_responder_recipe_responder_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_RESPONDER_RECIPE_T Type

Details of Target ResponderRecipe

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier of TargetResponderRecipe that can't be changed after creation.

`responder_recipe_id`

(required) Unique identifier for Responder Recipe of which this is an extension.

`compartment_id`

(required) Compartment Identifier

`display_name`

(required) ResponderRecipe display name.

`description`

(required) ResponderRecipe description.

`owner`

(required) Owner of ResponderRecipe

Allowed values are: 'CUSTOMER', 'ORACLE'

`time_created`

(optional) The date and time the target responder recipe rule was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the target responder recipe rule was updated. Format defined by RFC3339.

`responder_rules`

(optional) List of responder rules associated with the recipe - user input

`effective_responder_rules`

(optional) List of responder rules associated with the recipe after applying all defaults

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_DETECTOR_RECIPE_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_target_detector_recipe_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_RESPONDER_RECIPE_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_target_responder_recipe_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_T Type

Description of Target.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(optional) Target display name, can be renamed.

`compartment_id`

(required) Compartment Identifier where the resource is created

`description`

(optional) The target description.

`target_resource_type`

(required) possible type of targets

Allowed values are: 'COMPARTMENT', 'ERPCLOUD', 'HCMCLOUD', 'SECURITY_ZONE'

`target_resource_id`

(required) Resource ID which the target uses to monitor

`recipe_count`

(required) Total number of recipes attached to target

`target_detector_recipes`

(optional) List of detector recipes associated with target

`target_responder_recipes`

(optional) List of responder recipes associated with target

`target_details`

(optional)

`inherited_by_compartments`

(optional) List of inherited compartments

`time_created`

(optional) The date and time the target was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the target was updated. Format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the Target.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecyle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_SUMMARY_T Type

Summary of the Target.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`display_name`

(optional) DetectorTemplate Identifier, can be renamed

`compartment_id`

(required) Compartment Identifier where the resource is created

`target_resource_type`

(required) possible type of targets(compartment/HCMCloud/ERPCloud)

Allowed values are: 'COMPARTMENT', 'ERPCLOUD', 'HCMCLOUD', 'SECURITY_ZONE'

`target_resource_id`

(required) Resource ID which the target uses to monitor

`recipe_count`

(required) Total number of recipes attached to target

`time_created`

(optional) The date and time the target was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the target was updated. Format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecyle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_target_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_COLLECTION_T Type

Collection of Target

Syntax
```

```

Fields

Field Description

`items`

(required) List of TargetSummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_DETECTOR_RECIPE_SUMMARY_T Type

Summary of DetectorRecipe

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`compartment_id`

(required) Compartment Identifier

`display_name`

(required) DetectorRecipe Identifier Name

`description`

(required) DetectorRecipe Description

`owner`

(required) Owner of DetectorRecipe

Allowed values are: 'CUSTOMER', 'ORACLE'

`detector_recipe_id`

(required) Unique identifier for Detector Recipe of which this is an extension

`detector`

(optional) Type of detector

Allowed values are: 'IAAS_ACTIVITY_DETECTOR', 'IAAS_CONFIGURATION_DETECTOR', 'IAAS_THREAT_DETECTOR', 'IAAS_LOG_INSIGHT_DETECTOR'

`lifecycle_state`

(optional) The current state of the resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(optional) The date and time the target detector recipe was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the target detector recipe was updated. Format defined by RFC3339.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`source_data_retention`

(optional) The number of days for which source data is retained

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_DETECTOR_RECIPE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_target_detector_recipe_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_DETECTOR_RECIPE_COLLECTION_T Type

Summary of the Target DetectorRecipe.

Syntax
```

```

Fields

Field Description

`items`

(required) List of TargetDetectorRecipeSummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_DETECTOR_RECIPE_DETECTOR_RULE_SUMMARY_T Type

Summary of the Detector Recipe Rule.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier of the detector rule

`display_name`

(optional) DetectorTemplate Identifier, can be renamed

`description`

(optional) DetectorTemplate Identifier, can be renamed

`recommendation`

(optional) Recommendation for TargetDetectorRecipeDetectorRule

`detector`

(required) possible type of detectors

Allowed values are: 'IAAS_ACTIVITY_DETECTOR', 'IAAS_CONFIGURATION_DETECTOR', 'IAAS_THREAT_DETECTOR', 'IAAS_LOG_INSIGHT_DETECTOR'

`service_type`

(optional) service type of the configuration to which the rule is applied

`resource_type`

(optional) resource type of the configuration to which the rule is applied

`managed_list_types`

(optional) List of cloudguard managed list types related to this rule

Allowed values are: 'CIDR_BLOCK', 'USERS', 'GROUPS', 'IPV4ADDRESS', 'IPV6ADDRESS', 'RESOURCE_OCID', 'REGION', 'COUNTRY', 'STATE', 'CITY', 'TAGS', 'GENERIC'

`detector_details`

(optional)

`time_created`

(optional) The date and time the target detector recipe rule was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the target detector recipe rule was updated. Format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the target detector recipe rule

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`data_source_id`

(optional) The id of the attached DataSource.

`entities_mappings`

(optional) Data Source entities mapping for a Detector Rule

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_DETECTOR_RECIPE_DETECTOR_RULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_target_detector_recipe_detector_rule_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_DETECTOR_RECIPE_DETECTOR_RULE_COLLECTION_T Type

Summary of the DetectorRule within Target.

Syntax
```

```

Fields

Field Description

`items`

(required) List of TargetDetectorRecipeDetectorRuleSummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_IDS_SELECTED_T Type

Target selection on basis of TargetIds.

Syntax
```

```

`dbms_cloud_oci_cloud_guard_target_ids_selected_t`is a subtype of the`dbms_cloud_oci_cloud_guard_target_selected_t`type.

Fields

Field Description

`l_values`

(optional) Ids of Target

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_RESOURCE_TYPES_SELECTED_T Type

Target selection on basis of TargetResourceTypes.

Syntax
```

```

`dbms_cloud_oci_cloud_guard_target_resource_types_selected_t`is a subtype of the`dbms_cloud_oci_cloud_guard_target_selected_t`type.

Fields

Field Description

`l_values`

(optional) Types of Targets

Allowed values are: 'COMPARTMENT', 'ERPCLOUD', 'HCMCLOUD', 'SECURITY_ZONE'

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_RESPONDER_RECIPE_SUMMARY_T Type

Summary of ResponderRecipe

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`compartment_id`

(required) Compartment Identifier

`responder_recipe_id`

(required) Unique identifier for Responder Recipe of which this is an extension

`display_name`

(required) ResponderRecipe Identifier Name

`description`

(required) ResponderRecipe Description

`owner`

(required) Owner of ResponderRecipe

Allowed values are: 'CUSTOMER', 'ORACLE'

`time_created`

(optional) The date and time the target responder recipe was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the target responder recipe was updated. Format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the Example.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_RESPONDER_RECIPE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_target_responder_recipe_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_RESPONDER_RECIPE_COLLECTION_T Type

Collection of TargetResponderRecipe

Syntax
```

```

Fields

Field Description

`items`

(required) List of TargetResponderRecipeSummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_RESPONDER_RECIPE_RESPONDER_RULE_SUMMARY_T Type

Summary of ResponderRule.

Syntax
```

```

Fields

Field Description

`id`

(required) Identifier for ResponderRule.

`display_name`

(optional) ResponderRule Display Name

`description`

(optional) ResponderRule Description

`l_type`

(optional) Type of Responder

Allowed values are: 'REMEDIATION', 'NOTIFICATION'

`policies`

(optional) List of Policy

`supported_modes`

(optional) Supported Execution Modes

Allowed values are: 'AUTOACTION', 'USERACTION'

`details`

(optional)

`compartment_id`

(required) Compartment Identifier

`time_created`

(optional) The date and time the target responder recipe rule was created. Format defined by RFC3339.

`time_updated`

(optional) The date and time the target responder recipe rule was updated. Format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the ResponderRule.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_RESPONDER_RECIPE_RESPONDER_RULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_target_responder_recipe_responder_rule_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_RESPONDER_RECIPE_RESPONDER_RULE_COLLECTION_T Type

Summary of the ResponderRule within Target.

Syntax
```

```

Fields

Field Description

`items`

(required) List of TargetResponderRecipeResponderRuleSummary

### DBMS_CLOUD_OCI_CLOUD_GUARD_TECHNIQUE_SUMMARY_T Type

Technique summary.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier for the technique.

`display_name`

(required) Display name of the technique

### DBMS_CLOUD_OCI_CLOUD_GUARD_TECHNIQUE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_technique_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_TECHNIQUE_COLLECTION_T Type

Collection of technique summaries in Cloud Guard

Syntax
```

```

Fields

Field Description

`items`

(required) List of technique summary.

### DBMS_CLOUD_OCI_CLOUD_GUARD_TRIGGER_RESPONDER_DETAILS_T Type

The Responder details to be pushed to responder

Syntax
```

```

Fields

Field Description

`responder_rule_id`

(required) ResponderRule ID

`configurations`

(optional) ResponderRule configurations

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_BULK_PROBLEM_STATUS_DETAILS_T Type

List of problem ids to be passed in to update the Problem status.

Syntax
```

```

Fields

Field Description

`status`

(required) Action taken by user

Allowed values are: 'OPEN', 'RESOLVED', 'DISMISSED', 'DELETED'

`problem_ids`

(required) List of ProblemIds to be passed in to update the Problem status.

`l_comment`

(optional) User defined comment to be passed in to update the problem.

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_CONFIGURATION_DETAILS_T Type

Update cloud guard configuration details for a tenancy.

Syntax
```

```

Fields

Field Description

`reporting_region`

(required) The reporting region value

`status`

(required) Status of Cloud Guard Tenant

Allowed values are: 'ENABLED', 'DISABLED'

`self_manage_resources`

(optional) Identifies if Oracle managed resources will be created by customers. If no value is specified false is the default.

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_DATA_MASK_RULE_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Data mask rule Name. Avoid entering confidential information.

`compartment_id`

(optional) Compartment Identifier where the resource is created

`iam_group_id`

(optional) IAM Group id associated with the data mask rule

`target_selected`

(optional)

`data_mask_categories`

(optional) Data Mask Categories

Allowed values are: 'ACTOR', 'PII', 'PHI', 'FINANCIAL', 'LOCATION', 'CUSTOM'

`data_mask_rule_status`

(optional) The status of the dataMaskRule.

Allowed values are: 'ENABLED', 'DISABLED'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_DATA_SOURCE_DETAILS_T Type

Update of Data Source

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Data Source display name.

`status`

(optional) Status of DataSource.

Allowed values are: 'ENABLED', 'DISABLED'

`data_source_details`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_DETECTOR_RECIPE_DETAILS_T Type

Update of detector recipe

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Display name of detector recipe. Avoid entering confidential information.

`description`

(optional) Detector recipe description. Avoid entering confidential information.

`detector_rules`

(optional) Detector Rules to update

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_DETECTOR_RECIPE_DETECTOR_RULE_DETAILS_T Type

Update of detector rule of a detector recipe

Syntax
```

```

Fields

Field Description

`details`

(optional)

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_MANAGED_LIST_DETAILS_T Type

Update ManagedList

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Managed list display name. Avoid entering confidential information.

`description`

(optional) Managed list description. Avoid entering confidential information.

`list_items`

(optional) List of ManagedListItem

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_PROBLEM_STATUS_DETAILS_T Type

The additional details for the problem

Syntax
```

```

Fields

Field Description

`status`

(required) Action taken by user

Allowed values are: 'OPEN', 'RESOLVED', 'DISMISSED', 'DELETED'

`l_comment`

(optional) User Comments

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_RESPONDER_RECIPE_DETAILS_T Type

The details to be updated in ResponderRecipe

Syntax
```

```

Fields

Field Description

`display_name`

(required) Responder recipe identifier. Avoid entering confidential information.

`description`

(optional) Responder recipe description. Avoid entering confidential information.

`responder_rules`

(optional) Responder Rules to Update

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_RESPONDER_RECIPE_RESPONDER_RULE_DETAILS_T Type

The details to be updated in ResponderRule

Syntax
```

```

Fields

Field Description

`details`

(required)

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_SECURITY_POLICY_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(required) SecurityPolicy Identifier

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_SECURITY_RECIPE_DETAILS_T Type

Information to update in an existing security zone recipe

Syntax
```

```

Fields

Field Description

`display_name`

(required) The recipe's name

`description`

(optional) The recipe's description

`security_policies`

(optional) The list of `SecurityPolicy` ids to include in the recipe

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_SECURITY_ZONE_DETAILS_T Type

Information to update in an existing security zone

Syntax
```

```

Fields

Field Description

`display_name`

(required) The security zone's name

`description`

(optional) The security zone's description

`security_zone_recipe_id`

(optional) The OCID of the recipe (`SecurityRecipe`) for the security zone

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_DETECTOR_RECIPE_T Type

The information to be updated in attached Target DetectorRecipe

Syntax
```

```

Fields

Field Description

`target_detector_recipe_id`

(required) Identifier for DetectorRecipe.

`detector_rules`

(required) Updates to be applied to Detector Rule associated with the target

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_RESPONDER_RECIPE_T Type

The information to be updated in attached Target ResponderRecipe

Syntax
```

```

Fields

Field Description

`target_responder_recipe_id`

(required) Identifier for ResponderRecipe.

`responder_rules`

(required) Update responder rules associated with reponder recipe in a target.

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_DETECTOR_RECIPE_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_update_target_detector_recipe_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_RESPONDER_RECIPE_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_update_target_responder_recipe_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Display name of a target. Avoid entering confidential information.

`lifecycle_state`

(optional) The current state of the Target.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`target_detector_recipes`

(optional) The details of target detector recipes to be updated.

`target_responder_recipes`

(optional) The details of target responder recipes to be updated.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}` Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_DETECTOR_RECIPE_DETAILS_T Type

The information to be updated in DetectorRecipe

Syntax
```

```

Fields

Field Description

`detector_recipe_id`

(optional) Detector recipe identifier associated with the target

`is_validation_only_query`

(optional) When enabled, validation is performed for attaching the detector recipe.

`detector_rules`

(optional) Update detector rules associated with detector recipe in a target.

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_DETECTOR_RECIPE_DETECTOR_RULE_DETAILS_T Type

The details to be updated in DetectorRule

Syntax
```

```

Fields

Field Description

`details`

(required)

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_RESPONDER_RECIPE_DETAILS_T Type

The information to be updated in ResponderRecipe.

Syntax
```

```

Fields

Field Description

`responder_rules`

(required) Update responder rules associated with responder recipe in a target.

### DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_RESPONDER_RECIPE_RESPONDER_RULE_DETAILS_T Type

The details to be updated in ResponderRule

Syntax
```

```

Fields

Field Description

`details`

(required)

### DBMS_CLOUD_OCI_CLOUD_GUARD_WORK_REQUEST_RESOURCE_T Type

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

`metadata`

(optional) Additional information that helps to explain the resource.

### DBMS_CLOUD_OCI_CLOUD_GUARD_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_WORK_REQUEST_T Type

A description of workrequest status

Syntax
```

```

Fields

Field Description

`id`

(required) The id of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

`operation_type`

(required) Operation type of the work request.

Allowed values are: 'CREATE', 'UPDATE', 'DELETE', 'MOVE'

`status`

(required) Operation status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created

`time_started`

(optional) The date and time the request was started

`time_finished`

(optional) The date and time the object was finished

### DBMS_CLOUD_OCI_CLOUD_GUARD_WORK_REQUEST_ERROR_T Type

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

(required) The time the error occured.

### DBMS_CLOUD_OCI_CLOUD_GUARD_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestError objects.

### DBMS_CLOUD_OCI_CLOUD_GUARD_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written.

### DBMS_CLOUD_OCI_CLOUD_GUARD_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a workRequestLog search. Contains both workRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestLogEntries.

### DBMS_CLOUD_OCI_CLOUD_GUARD_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE', 'UPDATE', 'DELETE', 'MOVE'

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

(required) The date and time the request was created

`time_started`

(optional) The date and time the request was started

`time_finished`

(optional) The date and time the object was finished

### DBMS_CLOUD_OCI_CLOUD_GUARD_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_guard_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_GUARD_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestSummary objects.

- [Cloud Guard Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-586E4EB4-3437-4A1C-A0BE-852C658A9C16)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-105163D7-F599-4D6A-971A-1C3B7BE05A7A)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CONTINUOUS_QUERY_START_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-C2513459-26C1-4E41-8539-5E489A6698CD)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_ABSOLUTE_TIME_START_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-BADB5411-40F4-435F-A78A-6D74C2EDB1D6)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_POLITICAL_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-9613BD49-7926-4CE9-A9E6-4E995C4C51CE)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_GEOGRAPHICAL_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-4A1F9B96-A23F-4A6B-B11F-E9CCA661CAED)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_ACTIVITY_PROBLEM_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-0EAF9731-CC14-4317-A60F-59C6B5E69B7B)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_ACTIVITY_PROBLEM_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-E3C338E8-7476-4477-AD63-3CE7BEFAF013)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_ACTIVITY_PROBLEM_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-1DD207D3-2785-4A8F-9C4D-B67E370734D2)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_ADD_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-36A6AF20-2359-44ED-8EF8-626BD7DCB2F5)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_SELECTED_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-C3F3EB66-1E1F-48CB-B33B-20DF368BD626)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_ALL_TARGETS_SELECTED_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-711219A2-677B-4A70-B45B-A70991C9229D)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_ATTACH_TARGET_DETECTOR_RECIPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-F8C0E18B-D8EB-4FA8-A47D-4AA40B51E632)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_ATTACH_TARGET_RESPONDER_RECIPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-E8211618-AD2B-4E3C-A473-17DF5196B800)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CANDIDATE_RESPONDER_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-50E1E3F1-888A-47DD-A2F5-2F4BA372B340)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CHANGE_DATA_SOURCE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-D4B78845-752B-474C-A913-2A0C8DB1F1B5)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CHANGE_DETECTOR_RECIPE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-16D9DF7C-F49E-4F13-B094-671F7DB15E36)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CHANGE_MANAGED_LIST_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-37EAEA15-2F56-4326-BD87-F19DE0EBE1EB)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CHANGE_RESPONDER_RECIPE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-9E66176B-D241-431B-A3D1-8C0626A87894)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CHANGE_SECURITY_POLICY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-D016D41A-53F3-4291-BA48-AB60796B8BEF)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CHANGE_SECURITY_RECIPE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-BD351C98-7DE9-4437-AAFA-E8022507FC3E)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CHANGE_SECURITY_ZONE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-1AE76DD6-705D-4CD0-8F15-2063CC41FC59)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CONDITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-27D25D84-047B-408C-A934-2878C8EE3DEE)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_COMPOSITE_CONDITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-648B9DB6-BBA6-43EB-B604-FBA1792D0DBF)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CONDITION_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-363E0322-591B-488E-8A1F-3368D25A0634)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CONDITION_OPERATOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-F865E7EB-57C7-4C63-9DA8-A0E679A14844)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CONDITION_OPERATOR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-EEB3CADB-5778-4753-9F5D-4CF1427240F0)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_OPERATOR_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-D038030D-D47E-4D83-8605-E7210F3C280B)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_OPERATOR_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-BC1B4D25-ED0D-4B83-A7B9-77D055B2C1BD)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-42786857-16E9-414A-BB98-1E6BAC8416CE)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-E5536781-49F5-4218-978C-A8578463EB3C)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_TYPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-A6774E96-A1BA-46B9-B865-EAB8B6955A62)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_TYPE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-161BDDEF-3465-4670-B392-4D9B7F277AAF)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SERVICE_TYPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-95A7D520-EA0F-4F6C-8AF5-8902DCEC8785)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SERVICE_TYPE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-84FDF177-716E-4BF0-BB49-C97E83A43FA6)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CONDITION_METADATA_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-9F9CFBF8-5290-4FED-A82E-93F02FA0C36F)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CONDITION_METADATA_TYPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-85F83073-D665-4375-A4AD-790CAC80CF2B)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CONDITION_METADATA_TYPE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-4BA6FB64-63CD-4E08-ADE6-769214572BD0)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CONDITION_METADATA_TYPE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-14F683D6-4BF0-4948-8E10-87D52BF0E5F7)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CONFIG_VALUE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-962A7372-E299-4CB5-BC43-82193E1506C4)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-4B8924D2-36D0-4ADA-8F6D-86878B4CEBB0)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_DATA_MASK_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-D9CA04C0-2098-4A1D-B966-AE10BE3218DD)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-DB85F3AD-BA40-4418-877B-180533DBEAF6)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_DATA_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-DC883128-5E9D-4548-A6F6-F61448152E2A)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CONFIG_VALUE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-7CBDA6F2-E248-4C72-B621-629BC7873A1D)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-A5523508-2DAE-4269-8D3D-59DB39F78050)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_ENTITIES_MAPPING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-51D62F9B-459A-4A82-A1D9-963D330B2D0A)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_CONFIGURATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-68F49ACD-9FE9-435A-AB2D-CC951AA65C38)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_ENTITIES_MAPPING_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-C96F37D6-849C-4B13-9398-F9E504263942)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_DETECTOR_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-D3A619BE-10F5-4E14-9718-03A7590D3831)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_DETECTOR_RECIPE_DETECTOR_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-B28D0573-6BBC-48E2-8B94-3013608450D7)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_DETECTOR_RECIPE_DETECTOR_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-F728232E-E9D5-4F74-9139-8B90C91DC2A5)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_DETECTOR_RECIPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-3B04DEE0-4190-4D81-AFB8-48791EB6457D)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_DETECTOR_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-3CA62275-70B3-4809-96F4-CD220F732CBB)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_DETECTOR_RECIPE_DETECTOR_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-593A72CA-BBEC-4F1C-8265-17DFC70436EB)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_MANAGED_LIST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-0779F4DB-3B6D-4C9C-97E7-0B396F46D563)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_RESPONDER_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-362060A7-26B1-4171-ADE5-D83EFCEC95C2)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_RESPONDER_RECIPE_RESPONDER_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-23DC0AE8-AF03-40C5-A7BD-CF4D7B148A66)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_RESPONDER_RECIPE_RESPONDER_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-2B2355CD-1A3A-4821-9C91-B280FB47725B)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_RESPONDER_RECIPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-0F6C3EA5-6521-4D8B-95F4-F80E2BB77EFE)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_SECURITY_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-202BF413-C76E-4378-B4B3-D2285E997D78)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_SECURITY_RECIPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-51F84DD4-A6D6-48D4-8955-EEAAFBF02C5D)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_SECURITY_ZONE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-B6FAED77-E9D9-48B2-8176-03B039B9929E)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CONDITION_GROUP_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-951B981F-0F70-4889-8F21-A03178AC091F)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_DETECTOR_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-0527E0AB-F079-4A37-B112-6A48EA3C0851)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_RECIPE_DETECTOR_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-816B54CF-A0CC-4C82-B4AE-5FA3AFD98531)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_RECIPE_DETECTOR_RULE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-D10B0991-86C2-47A5-B2F3-988439B40D38)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_TARGET_DETECTOR_RECIPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-1E8A143B-D6EF-4D37-8178-BC15D47DFB4A)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-8C8F52B3-6188-438F-88C3-DF8847A3AF4A)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_CONFIGURATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-C79B594E-DEF6-4F8F-808B-2CC0A19374EE)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_RESPONDER_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-278DFF0C-E84C-4CD8-B346-E463317105FF)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_RECIPE_RESPONDER_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-9AB2312B-F925-4C28-B5E8-D4E359ABC6F6)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_RECIPE_RESPONDER_RULE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-5843C953-49ED-4CD2-AA05-68615E79F610)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_TARGET_RESPONDER_RECIPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-EF16C5AB-C2B0-4402-A117-0444EF48B4AB)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_TARGET_DETECTOR_RECIPE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-9BBDB3D9-AF2A-47B8-8C90-1AB6670C3747)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_TARGET_RESPONDER_RECIPE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-C4CAB0CD-35E0-44CD-82D7-31B5D066294A)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CREATE_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-6C678932-B726-4FB4-BDD7-84C56BAC78B4)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_MASK_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-E4D94923-89D7-44B4-9BDC-3B863F900F8B)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_MASK_RULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-1737645B-0A4C-40C7-8DD0-C2F6FDB42B75)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_MASK_RULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-C2551E37-5F1A-4522-BB4C-3282F0563D2D)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_MASK_RULE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-B025A4FB-9335-45D1-827E-EBBA5DAD76D8)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_SOURCE_MAPPING_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-2A69B06C-7099-4BC2-A0E2-8195601F830E)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_REGION_STATUS_DETAIL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-5970CB97-A7CC-44FF-8B6C-AF32BAC3161B)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_SOURCE_MAPPING_INFO_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-78656089-B0B4-448B-9369-A3E953409B37)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_REGION_STATUS_DETAIL_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-A35E777C-D287-4276-B556-6BD837ADBFF3)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-8C3389BF-43D2-4D3A-BE6F-A14475FF1622)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_SOURCE_SUMMARY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-CB2D1128-5F20-4C6C-9F3D-2D320BA5AD15)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_LOGGING_QUERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-7A3AA91B-5A40-47BB-8B09-A4FE62010AEC)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_SOURCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-424DE16F-01BF-42F8-B1BE-A41C1D0365D3)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_SOURCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-596E20AE-CBF6-4143-AB8B-A2A457D4D7F8)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_SOURCE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-27AAC780-3F68-4609-ACB9-614C57DC941D)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_SOURCE_EVENT_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-333371D8-B462-4640-A860-06A47CCE2705)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_SOURCE_EVENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-4B65AE55-D7B8-4A5C-A227-5684FC84EB65)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_SOURCE_EVENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-E2254CF8-0DC9-4CCD-ABCF-539C3457CB50)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DATA_SOURCE_EVENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-BED0D920-CC09-46BE-BE99-F5E3CA0B0807)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-8ED6F48C-311E-4B7C-AB94-1E4CB0EB8965)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-C5C51103-69EC-4AAE-97D9-E92EBE18139E)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-DAE85A85-32C4-498C-ADE2-56D9A0CBACD7)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-1873FE86-03E1-4486-B424-12F84D9E46EB)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SIGHTING_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-B58D6F2E-C935-4FCC-9564-41726934C0AA)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SIGHTING_TYPE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-F142A43F-50A8-484E-BDE8-7A2CD0612FAE)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-5F9DC91A-5E99-4FA2-82BE-13A94B240C20)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_CANDIDATE_RESPONDER_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-5D5A93F5-1DE7-45F1-BB8E-94DCD322F8D6)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RECIPE_DETECTOR_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-B9426A92-E1FE-419A-9780-C3B8E3A108BE)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RECIPE_DETECTOR_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-671B906D-FF6B-493A-8D1F-551ED2D6B7FB)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RECIPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-79DFB803-D40E-48B8-B7B6-069EA64A8A9A)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RECIPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-01DC74E0-27C5-4C43-8B6C-399B25700DBB)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RECIPE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-CFAF3B01-0A4F-4AA2-8885-5889B3E23BD4)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RECIPE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-340D9516-E5C7-4B9D-8060-47A72DD59BA5)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RECIPE_DETECTOR_RULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-9F8CFCA1-82C3-4739-B524-EBF5E279B502)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RECIPE_DETECTOR_RULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-0B99BC2E-8343-49D8-B403-EFFD9BDD0D79)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RECIPE_DETECTOR_RULE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-B8ED034B-786B-4B0D-8C7F-30C728FA2157)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-30458CDA-58CC-489D-84FF-B28C5F518C17)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-F2099462-0A3A-43A9-951B-B0C2B05CEC9F)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-E444BA93-8796-48F6-9F9F-09D0BF29E330)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_DETECTOR_RULE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-BD50AF68-481F-4E70-8998-0A3AACA9E411)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_ENTITY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-39EBCBCE-7EFB-44F4-B5F5-5D70F4E6E789)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-7BDD8C47-C559-44F3-AB52-65CF1EA2AD21)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_EXECUTE_RESPONDER_EXECUTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-ACEF7698-4BBC-4278-A5AB-540ED3C1CB35)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_IMPACTED_RESOURCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-FC4AF71D-A9E8-453F-B198-D3598C04C001)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_IMPACTED_RESOURCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-9B21105B-BFBE-4D02-999F-E4CB8639274C)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_IMPACTED_RESOURCE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-A954B32A-BB88-4717-A4BB-9BB188A75727)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_INSIGHT_TYPE_LOGGING_QUERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-73D9B4BD-56B3-4C57-8C78-C048B4AD6888)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_LOGGING_EVENT_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-7FD62685-8A65-4912-8A98-6F3BAE46745A)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_LOGGING_QUERY_DATA_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-DB339115-F4D3-41ED-8160-B6C86B89E464)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_LOGGING_QUERY_DATA_SOURCE_SUMMARY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-163936F7-9BA4-4011-930D-FF624865D2D6)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_MANAGED_LIST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-D7893D9C-E558-49B7-9521-3129BFC88071)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_MANAGED_LIST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-CC835DB7-E94A-4DE4-AC90-807F813FB41B)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_MANAGED_LIST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-2B7D96CD-EA02-4C22-B536-3B386BEA206B)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_MANAGED_LIST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-04BE4B0F-74D8-427F-994C-4750F86F8935)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_MANAGED_LIST_TYPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-266A9BEA-C917-41CF-AE7A-64BD0FB8FA21)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_MANAGED_LIST_TYPE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-0AC36836-500E-4423-9EF8-42CAE3F97E0F)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_MANAGED_LIST_TYPE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-6830C562-AF38-491C-8A71-900DE5EA924A)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_NO_DELAY_START_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-FF030261-2788-4F18-A116-B11BA2E44CEE)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_POLICY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-7DF85A3B-072C-45E8-82DA-DD8295AB661E)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_POLICY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-25FEEE58-3C84-4653-94AA-4920B9FBC2A8)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_POLICY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-CE9EA82E-8901-4A2C-9E3D-870C60D262F6)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-F4368F73-6352-4EEB-AEF9-03B27E3D5041)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-11B4E276-3375-4598-BD0D-3D26F702AEF1)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-A8FA1C06-9CAD-4018-8F60-765C4E001B87)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-65206652-CA6F-4D58-BF21-06B6C9EDCDC1)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-8E4CD5D0-AC6C-4121-89DE-9F955ABF3F81)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-0FAFC9F3-9CFD-468F-B176-4626D85BCD5E)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-646C83BD-FE56-41F9-9316-84A612FD2E21)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_ENDPOINT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-28954B96-B465-4712-B36F-75DD07804E86)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_ENDPOINT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-5E6E3D98-DE71-431B-977C-C2D2F04AB29D)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_ENDPOINT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-71DF7118-D7D5-45B3-BB27-72E3EB56E90D)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_ENTITY_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-FD4EA10A-6809-47F6-8D16-C89AD52A6579)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_ENTITY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-3D5C9043-60A1-476D-A3E5-85176D29D3FD)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_ENTITY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-BD45A45F-01FD-4AFD-B03D-EE7B9339CBDF)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_ENTITY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-D96C388C-8130-4E2B-8CA6-4A7E0BCB6E50)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_HISTORY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-D65549BE-CE18-4B78-9C70-6C6585A29D3E)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_HISTORY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-87DB4625-A4E3-4E46-A3B4-F373AAED34B1)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_HISTORY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-5C7C2536-3AB6-42AC-B5F2-CC5A01553D33)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_TREND_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-06DA7900-2CF4-4091-A218-EA0BD07A1496)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_TREND_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-23B30163-6C70-46E1-BD4D-B7D59D3596D3)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_PROBLEM_TREND_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-E8FB1CC6-5FBF-413F-B25D-23A083B1B260)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RECOMMENDATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-7688D619-EC12-46F4-8429-EF539A1E7777)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RECOMMENDATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-0672AE6B-C655-47E8-8CB9-8F7E0D062740)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RECOMMENDATION_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-248C49E9-C1F6-4149-AE07-CA00A4B7819D)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_REMOVE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-AAC93785-9B4F-4719-A975-FE3332697754)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_REQUEST_SUMMARIZED_TREND_RESOURCE_RISK_SCORES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-AC16E851-6DD4-453A-9871-B38B27DB3314)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TACTIC_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-255A9D84-CCDF-4F53-91B8-15EABD5AFE00)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TACTIC_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-E2507939-F751-4A8C-B5C3-A0835E4398F7)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-7A4B0F30-AD39-434F-938F-467F2F0B25EC)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-4D052588-2F4A-469E-8531-FE4294D4B758)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-191E0D65-23A1-48FD-BACC-AD06B13A65FD)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-33090AC3-7D85-444F-A231-C4E936E66279)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_ENDPOINT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-EEF61332-B371-4687-B4A6-02299C1251C4)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_ENDPOINT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-DD1BACB6-8132-4A30-BA08-9BFCAFE66DB7)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_ENDPOINT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-9E79CB51-1EA0-41AF-BA2B-8949223DF854)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_IMPACTED_RESOURCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-BF1A25CA-D9F0-439D-9B23-B2F8A62D5E02)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_IMPACTED_RESOURCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-A4ED4827-FD82-4851-9946-B8D918159FBD)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_IMPACTED_RESOURCE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-BB93F204-A87D-48CE-B5C8-FE5752725274)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_RISK_SCORE_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-A87B351C-40D8-4B02-8D53-1F0C6F947F02)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_RISK_SCORE_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-5524E5F9-CEAF-462F-AFE3-C807ED3A499A)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_RISK_SCORE_AGGREGATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-84465D4B-76C4-4E22-9F89-6DDE59AB01A7)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_RISK_SCORE_AGGREGATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-969422B9-9F59-4887-9F06-BA74111A3194)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_PROFILE_RISK_SCORE_AGGREGATION_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-83F06763-8164-4998-9D82-5017DADDBD23)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_RISK_SCORE_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-0FC215AE-610C-42A2-93D1-A7D17D5DEFCB)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESOURCE_TYPE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-CD262BFB-D4FD-4D43-90CE-3DB45CFC9C95)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_ACTIVITY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-07CC4718-4F97-47D6-BC7C-45E231506C9F)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_ACTIVITY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-A11FA5DF-66FE-4EC1-879D-FC65B2D30123)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_ACTIVITY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-D47EC499-0376-4C6E-A117-BF6E9C3BA422)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RULE_EXECUTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-D2FEE2CB-F316-402A-ACCC-28B63F7491BC)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_EXECUTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-51654F86-EEF0-4A9B-A644-73C96300DD7C)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_EXECUTION_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-16B5E7A9-1980-4EE0-815F-955D82F873AE)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_EXECUTION_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-F9A2BEDF-6308-43F5-88C8-9A177E4661CE)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_EXECUTION_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-68255CF8-6796-4E1F-9A65-31087710F6DE)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_EXECUTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-CADB8550-E120-405F-B672-8CC68D99D4E0)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_EXECUTION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-FE6272C1-B434-4572-AF83-F4BEDF6C9729)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_EXECUTION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-521CCD5E-F45C-44C5-8FC8-323DA76800C8)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_EXECUTION_TREND_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-53E5D4DA-D73D-4D93-A026-63136D826A79)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_EXECUTION_TREND_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-BDE9ADC1-C926-4025-AE5D-3EAE899930FC)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_EXECUTION_TREND_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-64A6C7E0-299F-4A7F-8046-57F35DB81B01)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-F83B1561-CC88-4383-93A4-025347448821)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RECIPE_RESPONDER_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-2542725C-8429-465C-9521-49DC1A7C4B09)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RECIPE_RESPONDER_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-08518000-23D9-4F49-956F-E945FC0500DD)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RECIPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-188AB7F9-5008-4C85-A068-DC43D428EAAE)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RECIPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-33B2823E-E6F0-476B-9463-67D20FAB9DDB)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RECIPE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-4582EEE4-2DC9-4B26-AA75-069F0C9E040A)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RECIPE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-941B0161-7300-4521-8D93-75CCCBE6C9A4)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RECIPE_RESPONDER_RULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-F7B89AA3-B304-4A71-B270-BDC9C3A99CDC)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RECIPE_RESPONDER_RULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-B7BCE310-ADD2-4310-8DAB-4C33CCF61DAE)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RECIPE_RESPONDER_RULE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-0F4EFF02-D10E-41E6-9835-4734DB0C6277)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-5C91F0BC-86A7-4167-BA75-C1EEDC079BD8)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-3F3114C1-3823-4C00-B3D9-135D49F10329)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-A163A791-ADEC-4D75-B1FF-C0EDECB916F8)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RESPONDER_RULE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-57078336-C889-459E-9582-F658B2FE300E)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RISK_SCORE_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-9F59B4A6-41D8-4AA5-9754-5EE4AA8293A6)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RISK_SCORE_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-B24E08F9-5F3E-48BA-9E82-0DC666F4D5AC)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_RISK_SCORE_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-15937DD6-4101-40EC-A73A-CE7943D6ED3B)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-549B56D1-FCC7-4E37-83A4-956622C58E50)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_POLICY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-BEEA41A4-E4D0-4AFF-AE2A-9B779BE96693)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_POLICY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-0C5FFA02-5098-480C-BDE8-BE2D41076C83)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_POLICY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-7291E15C-E9E5-406F-B38C-F14D5EA6A160)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_RECIPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-E02485F4-79B5-4C77-B536-C69C3232A144)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_RECIPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-CDCA09F6-EDD4-446E-9BDA-8C5E4B71760A)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_RECIPE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-A28FF7CA-CD92-4152-B1C9-398EDA1FF217)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_RECIPE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-A51F28DD-8725-4C04-8DD6-725314A841FA)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_SCORE_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-A7E2F2E5-25BA-457A-923A-CDDA68F6EEF3)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_SCORE_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-473DD067-FE61-4F7D-B1F9-39D758496C0A)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_SCORE_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-0C0D4D71-5053-4709-A01B-45F3B6B6590E)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_SCORE_TREND_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-BEA2CAE8-144D-475B-8664-F955E9A5619F)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_SCORE_TREND_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-B449E1B5-3821-4BC7-855F-07436720FBB8)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_SCORE_TREND_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-4F4BB334-D257-4305-B67A-76E944E42819)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_ZONE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-F0324C7B-2A60-40DB-BC69-CDE1E05E4E05)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_ZONE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-8C84A20D-0D10-4AFC-A070-D0E1A5727AFE)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_ZONE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-7A2E7B84-1168-4197-9FEF-DA75D75F77A1)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_ZONE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-1E991D93-AEAA-4E32-BCEF-388C91C0E0FB)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-8A1E3205-E481-4FBE-BD39-5E18ABA9988A)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_RECIPE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-9732C00E-7523-4E03-83A4-DD613B43B86E)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SECURITY_ZONE_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-7649BEE1-890A-4EB0-BA19-089307EF2D5F)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SIGHTING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-60F2728F-136E-49C7-AF5C-67167335D212)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SIGHTING_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-812EDEC3-EF3B-4ACF-AFDB-F935709C9109)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SIGHTING_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-308065E5-0BA6-4F64-9CC6-45DDD877FEC8)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SIGHTING_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-8EA84619-9ABB-4EC5-9E37-787D8FF5D7AE)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SIGHTING_ENDPOINT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-A16C630A-3991-4D94-93B2-00042261D144)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SIGHTING_ENDPOINT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-4C28455D-DC37-431F-9675-FC356CD35530)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SIGHTING_ENDPOINT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-2490BA52-9CAF-42A4-852B-0E72F3821260)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SIGHTING_IMPACTED_RESOURCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-84DCA370-BA5E-4861-ACBA-4CD632C4EA6D)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SIGHTING_IMPACTED_RESOURCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-DE55E569-79E5-4459-AE7B-79EBB09BE7D6)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SIGHTING_IMPACTED_RESOURCE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-2A6BCFC3-7AEC-4489-97C8-6161D4CFA272)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SIMPLE_CONDITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-45A42E30-0180-4D33-A81C-3451E5FFFCAF)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_SKIP_BULK_RESPONDER_EXECUTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-172FC3A5-7048-4BEB-B90A-9046FF802870)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TACTIC_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-B98232BF-60DD-493C-8953-D44A21AD6A85)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_DETECTOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-64D97694-D072-4713-A68D-A4ACAC72CE9E)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_DETECTOR_RECIPE_DETECTOR_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-415A9955-CD81-410C-AEEB-C0D9CD08E36D)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_DETECTOR_RECIPE_DETECTOR_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-D9F7A67F-4735-4645-AC6D-DAA174953E30)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_DETECTOR_RECIPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-D2E2063C-C87D-47A6-9725-6ABE1F7A7A1C)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_RESPONDER_RECIPE_RESPONDER_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-7FD0582B-F50B-4D12-A639-7B187CC380DE)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_RESPONDER_RECIPE_RESPONDER_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-5BCDB577-DE56-4EF9-BF01-B9B74DAF0C98)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_RESPONDER_RECIPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-0478A2C9-1D6B-4782-B92A-6F881C929575)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_DETECTOR_RECIPE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-004EEA8F-08E3-4A05-9E03-EA1126412DBB)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_RESPONDER_RECIPE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-338E1F21-3C39-44C8-83BD-64B2A0438B49)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-3184038B-D269-427C-B456-07419C58D073)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-4BDAEC4F-2918-41C7-B54E-21684D86C414)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-FAC7BC34-642E-4586-A853-63E9762090B2)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-DB5CBC47-E03C-4CEF-9F8E-D3A8492D2C26)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_DETECTOR_RECIPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-751D6AA4-56A2-411B-AA37-CB7B710B01E8)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_DETECTOR_RECIPE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-4E1F7BD3-50F1-4975-AEEA-C379327DD983)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_DETECTOR_RECIPE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-A716ADA2-9B6B-4B54-A081-EA37751DE8B9)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_DETECTOR_RECIPE_DETECTOR_RULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-E35525DB-63B8-45CD-A99A-D59FBA5E05EF)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_DETECTOR_RECIPE_DETECTOR_RULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-7353AEC3-E6C1-4658-BCC9-D784F818E56C)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_DETECTOR_RECIPE_DETECTOR_RULE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-CF1A6698-6B23-45C4-9768-45987367EDF4)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_IDS_SELECTED_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-13347239-655A-4867-BA4E-8D9EB8675115)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_RESOURCE_TYPES_SELECTED_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-04FAF53C-D955-41CD-BF02-4D7E35536AE7)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_RESPONDER_RECIPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-75BDDB1E-D22F-469C-8950-224314E57148)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_RESPONDER_RECIPE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-5D592A6C-7563-4FC5-BBEE-F7792D8FADCF)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_RESPONDER_RECIPE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-FCCA637F-E60A-41E6-A48A-2E7214204620)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_RESPONDER_RECIPE_RESPONDER_RULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-2F03E55C-9E47-45E0-B0CD-6EC1CB229243)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_RESPONDER_RECIPE_RESPONDER_RULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-5FE757ED-724B-4E26-B234-2C6B5310ABDC)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TARGET_RESPONDER_RECIPE_RESPONDER_RULE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-6DA04A64-52B9-481C-8E84-F6A2354439ED)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TECHNIQUE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-BB77F87F-CB2D-4654-B453-1DAA199756E4)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TECHNIQUE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-5EBAE812-CCB2-4627-8AD4-ABF69C41103F)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TECHNIQUE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-4F6BDDA5-2F4C-4E4A-B710-FB9957E84F5A)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_TRIGGER_RESPONDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-B4E38E6B-64AB-47A3-8D38-EA47FE272BFD)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_BULK_PROBLEM_STATUS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-3D5DB580-9132-4162-B5D3-FF85485CB336)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-CE81FB7E-3C09-41B2-BF30-1D6BBF8D518C)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_DATA_MASK_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-16656F6F-197D-445C-A9DE-3B99A561C29C)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_DATA_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-DF153694-84AF-4B55-86D3-3BBA5B842BED)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_DETECTOR_RECIPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-4C92F393-09E0-435C-853E-602B936F1C8A)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_DETECTOR_RECIPE_DETECTOR_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-FA7C6DD7-39BB-4FB2-80C1-269CD40D65F6)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_MANAGED_LIST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-43E1FF4F-FBB2-478C-83B4-8713216717AC)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_PROBLEM_STATUS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-465D1C60-75BD-40F3-A2DA-15CE4B22033E)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_RESPONDER_RECIPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-E2179A90-0E5D-429F-8013-2FEED13BD1B6)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_RESPONDER_RECIPE_RESPONDER_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-C0824AF1-DC2A-4C0E-A74D-0CB1B054D1ED)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_SECURITY_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-8DEDF9EF-3BCD-4DFB-9426-75E973EF0727)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_SECURITY_RECIPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-7B9282A9-37CD-40AF-92E7-A9626437F702)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_SECURITY_ZONE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-8CE1C71D-CAB1-42FC-B86C-4615E4FEC5C1)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_DETECTOR_RECIPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-36FF66FF-83BD-4C3E-921C-2B5DDBA810E1)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_RESPONDER_RECIPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-31ACB4DA-C820-4C0E-81B6-002125C73D25)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_DETECTOR_RECIPE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-840F4CB0-5E4C-4DD3-973C-A1B30C56F069)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_RESPONDER_RECIPE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-80FD8433-9C60-4A95-B56B-B4DC55F115C7)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-CA5A17A5-64D9-4A13-87C7-01017D307260)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_DETECTOR_RECIPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-71CCFFF3-9F73-4475-80C4-91D3D84BFF76)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_DETECTOR_RECIPE_DETECTOR_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-D86E9358-F06D-4BAC-9FB2-F87BFA81F931)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_RESPONDER_RECIPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-AC27EFEF-6420-46D6-ABD6-0B2D79D3D6A4)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_UPDATE_TARGET_RESPONDER_RECIPE_RESPONDER_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-7A83978B-92CC-48FE-89E9-0A3E62121F43)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-1DA11555-50D8-4A46-B5AB-5E88C62E973E)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-A306CC4F-D15C-4E2B-A120-05DC21BDA718)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-A695B36A-DA0E-4D84-A7C2-B360FD928C2A)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-BDA0A9DF-7DCD-4CFA-9BA5-7F451E05E82F)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-CAA6419C-BC64-4C4F-9CCD-2F8FE8B27627)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-BB027AB0-D0FC-4B64-8305-D7DDE5174678)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-749EAC38-0215-499D-9C79-CF6110F3D566)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-E45AAD99-B0D8-41F8-ACFF-DA2FB2E7EEED)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-E1931330-8D87-4163-B53E-2C476BEA167F)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-CF72EA55-1C7E-4D9F-94C0-076A1B38221F)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-ACFAAFC9-D535-4448-B5FF-81B8AA6C878A)
- [DBMS_CLOUD_OCI_CLOUD_GUARD_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_guard_t.html#ADSDK-GUID-34142464-EBD0-41EF-AB0E-023744EE0A5D)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
