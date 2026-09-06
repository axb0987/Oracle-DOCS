# Optimizer Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html
- Fetched: 2026-09-05 19:19 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#dcoc-content-body)

## Optimizer Common Types

### DBMS_CLOUD_OCI_OPTIMIZER_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_ACTION_T Type

Details about the recommended action.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The status of the resource action.

Allowed values are: 'KB_ARTICLE'

`description`

(required) Text describing the recommended action.

`url`

(required) The URL path to documentation that explains how to perform the action.

### DBMS_CLOUD_OCI_OPTIMIZER_BULK_APPLY_RESOURCE_ACTION_T Type

The resource action that a recommendation will be applied to.

Syntax
```

```

Fields

Field Description

`resource_action_id`

(required) The unique OCIDs of the resource actions that recommendations are applied to.

`status`

(optional) The current status of the recommendation.

Allowed values are: 'PENDING', 'DISMISSED', 'POSTPONED', 'IMPLEMENTED'

`time_status_end`

(optional) The date and time the current status will change. The format is defined by RFC3339. For example, \"The current `postponed` status of the resource action will end and change to `pending` on this date and time.\"

`parameters`

(optional) Additional parameter key-value pairs defining the resource action. For example: `{\"timeAmount\": 15, \"timeUnit\": \"seconds\"}`

`strategy_name`

(optional) The name of the strategy.

### DBMS_CLOUD_OCI_OPTIMIZER_BULK_APPLY_RESOURCE_ACTION_TBL Type

Nested table type of dbms_cloud_oci_optimizer_bulk_apply_resource_action_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_BULK_APPLY_RECOMMENDATIONS_DETAILS_T Type

Details about bulk recommendation actions.

Syntax
```

```

Fields

Field Description

`resource_action_ids`

(optional) The unique OCIDs of the resource actions that recommendations are applied to. This field is deprecated.

`actions`

(optional) The unique resource actions that recommendations are applied to.

`status`

(required) The current status of the recommendation.

Allowed values are: 'PENDING', 'DISMISSED', 'POSTPONED', 'IMPLEMENTED'

`time_status_end`

(optional) The date and time the current status will change. The format is defined by RFC3339. For example, \"The current `postponed` status of the resource action will end and change to `pending` on this date and time.\"

### DBMS_CLOUD_OCI_OPTIMIZER_RECOMMENDATION_COUNT_T Type

The count of recommendations in a category, grouped by importance.

Syntax
```

```

Fields

Field Description

`importance`

(required) The level of importance assigned to the recommendation.

Allowed values are: 'CRITICAL', 'HIGH', 'MODERATE', 'LOW', 'MINOR'

`l_count`

(required) The count of recommendations.

### DBMS_CLOUD_OCI_OPTIMIZER_RESOURCE_COUNT_T Type

The count of resources in a category, grouped by status.

Syntax
```

```

Fields

Field Description

`status`

(required) The recommendation status of the resource.

Allowed values are: 'PENDING', 'DISMISSED', 'POSTPONED', 'IMPLEMENTED'

`l_count`

(required) The count of resources.

### DBMS_CLOUD_OCI_OPTIMIZER_RECOMMENDATION_COUNT_TBL Type

Nested table type of dbms_cloud_oci_optimizer_recommendation_count_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_RESOURCE_COUNT_TBL Type

Nested table type of dbms_cloud_oci_optimizer_resource_count_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_CATEGORY_T Type

The metadata associated with the category.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique OCID of the category.

`compartment_id`

(required) The OCID of the tenancy. The tenancy is the root compartment.

`compartment_name`

(required) The name associated with the compartment.

`name`

(required) The name assigned to the category.

`description`

(required) Text describing the category.

`recommendation_counts`

(required) An array of `RecommendationCount` objects grouped by the level of importance assigned to the recommendation.

`resource_counts`

(required) An array of `ResourceCount` objects grouped by the status of the recommendation.

`lifecycle_state`

(required) The category's current state.

Allowed values are: 'ACTIVE', 'FAILED', 'INACTIVE', 'ATTACHING', 'DETACHING', 'DELETING', 'DELETED', 'UPDATING', 'CREATING'

`estimated_cost_saving`

(required) The estimated cost savings, in dollars, for the category.

`time_created`

(required) The date and time the category details were created, in the format defined by RFC3339.

`time_updated`

(required) The date and time the category details were last updated, in the format defined by RFC3339.

`extended_metadata`

(optional) Additional metadata key/value pairs for the category. For example: `{\"EstimatedSaving\": \"200\"}`

### DBMS_CLOUD_OCI_OPTIMIZER_CATEGORY_SUMMARY_T Type

The metadata associated with the category summary.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique OCID of the category.

`compartment_id`

(required) The OCID of the tenancy. The tenancy is the root compartment.

`compartment_name`

(required) The name associated with the compartment.

`name`

(required) The name assigned to the category.

`description`

(required) Text describing the category.

`recommendation_counts`

(required) An array of `RecommendationCount` objects grouped by the level of importance assigned to each recommendation.

`resource_counts`

(required) An array of `ResourceCount` objects grouped by the status of each recommendation.

`lifecycle_state`

(required) The category's current state.

Allowed values are: 'ACTIVE', 'FAILED', 'INACTIVE', 'ATTACHING', 'DETACHING', 'DELETING', 'DELETED', 'UPDATING', 'CREATING'

`estimated_cost_saving`

(required) The estimated cost savings, in dollars, for the category.

`time_created`

(required) The date and time the category details were created, in the format defined by RFC3339.

`time_updated`

(required) The date and time the category details were last updated, in the format defined by RFC3339.

`extended_metadata`

(optional) Additional metadata key/value pairs for the category summary. For example: `{\"EstimatedSaving\": \"200\"}`

### DBMS_CLOUD_OCI_OPTIMIZER_CATEGORY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_optimizer_category_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_CATEGORY_COLLECTION_T Type

A list of categories that match filter criteria, if any. Results contain `CategorySummary` objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A collection of category summaries.

### DBMS_CLOUD_OCI_OPTIMIZER_LEVEL_CONFIGURATION_T Type

Details about the configuration level for the recommendation.

Syntax
```

```

Fields

Field Description

`recommendation_id`

(optional) The unique OCID of the recommendation.

`l_level`

(optional) The pre-defined profile level.

### DBMS_CLOUD_OCI_OPTIMIZER_LEVEL_CONFIGURATION_TBL Type

Nested table type of dbms_cloud_oci_optimizer_level_configuration_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_LEVELS_CONFIGURATION_T Type

A list of configuration levels for each recommendation.

Syntax
```

```

Fields

Field Description

`items`

(optional) The array of configuration levels.

### DBMS_CLOUD_OCI_OPTIMIZER_TARGET_COMPARTMENTS_T Type

Optional. The compartments specified in the profile override for a recommendation.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of OCIDs attached to the compartments specified in the current profile override.

### DBMS_CLOUD_OCI_OPTIMIZER_TARGET_TAG_T Type

A tag key definition used in the current profile override, including the tag namespace, tag key, tag value type, and tag values. Only defined tags are supported. For more information about tagging, see[Tagging Overview](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm)

Syntax
```

```

Fields

Field Description

`tag_namespace_name`

(required) The name of the tag namespace.

`tag_definition_name`

(required) The name you use to refer to the tag, also known as the tag key.

`tag_value_type`

(required) Specifies which tag value types in the `tagValues` field result in overrides of the recommendation criteria. When the value for this field is `ANY`, the `tagValues` field should be empty, which enforces overrides to the recommendation for resources with any tag values attached to them. When the value for this field value is `VALUE`, the `tagValues` field must include a specific value or list of values. Overrides to the recommendation criteria only occur for resources that match the values in the `tagValues` fields.

Allowed values are: 'VALUE', 'ANY'

`tag_values`

(optional) The list of tag values. The tag value is the value that the user applying the tag adds to the tag key.

### DBMS_CLOUD_OCI_OPTIMIZER_TARGET_TAG_TBL Type

Nested table type of dbms_cloud_oci_optimizer_target_tag_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_TARGET_TAGS_T Type

Optional. The tags specified in the profile override for a recommendation.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of tags specified in the current profile override.

### DBMS_CLOUD_OCI_OPTIMIZER_CREATE_PROFILE_DETAILS_T Type

Details for creating a profile.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the tenancy. The tenancy is the root compartment.

`name`

(required) The name assigned to the profile. Avoid entering confidential information.

`description`

(required) Text describing the profile. Avoid entering confidential information.

`aggregation_interval_in_days`

(optional) The time period over which to collect data for the recommendations, measured in number of days.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair applied without any predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{ \"orcl-cloud\": { \"free-tier-retained\": \"true\" } }`

`levels_configuration`

(required)

`target_compartments`

(optional)

`target_tags`

(optional)

### DBMS_CLOUD_OCI_OPTIMIZER_ENROLLMENT_STATUS_T Type

The metadata associated with the enrollment status.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the enrollment status.

`compartment_id`

(required) The OCID of the compartment.

`lifecycle_state`

(required) The enrollment status' current state.

Allowed values are: 'ACTIVE', 'FAILED', 'INACTIVE', 'ATTACHING', 'DETACHING', 'DELETING', 'DELETED', 'UPDATING', 'CREATING'

`status`

(required) The current Cloud Advisor enrollment status.

Allowed values are: 'ACTIVE', 'INACTIVE'

`status_reason`

(optional) The reason for the enrollment status of the tenancy.

`time_created`

(optional) The date and time the enrollment status was created, in the format defined by RFC3339.

`time_updated`

(optional) The date and time the enrollment status was last updated, in the format defined by RFC3339.

### DBMS_CLOUD_OCI_OPTIMIZER_ENROLLMENT_STATUS_SUMMARY_T Type

The metadata associated with the enrollment status summary.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the enrollment status.

`compartment_id`

(required) The OCID of the compartment.

`lifecycle_state`

(required) The enrollment status' current state.

Allowed values are: 'ACTIVE', 'FAILED', 'INACTIVE', 'ATTACHING', 'DETACHING', 'DELETING', 'DELETED', 'UPDATING', 'CREATING'

`status`

(required) The current Cloud Advisor enrollment status.

Allowed values are: 'ACTIVE', 'INACTIVE'

`status_reason`

(optional) The reason for the enrollment status of the tenancy.

`time_created`

(optional) The date and time the enrollment status was created, in the format defined by RFC3339.

`time_updated`

(optional) The date and time the enrollment status was last updated, in the format defined by RFC3339.

### DBMS_CLOUD_OCI_OPTIMIZER_ENROLLMENT_STATUS_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_optimizer_enrollment_status_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_ENROLLMENT_STATUS_COLLECTION_T Type

A list of enrollment statuses that match filter criteria, if any. Results contain `EnrollmentStatusSummary` objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A collection of enrollment status summaries.

### DBMS_CLOUD_OCI_OPTIMIZER_ERROR_T Type

The representation of an error.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_OPTIMIZER_EVALUATED_METRIC_T Type

One of the metrics that will be evaluated by profiles using this profile level.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the metric (e.g., `CpuUtilization`).

`statistic`

(required) The name of the statistic (e.g., `p95`).

`threshold`

(required) The threshold that must be crossed for the recommendation to appear.

`target`

(optional) Optional. The metric value that the recommendation will target.

### DBMS_CLOUD_OCI_OPTIMIZER_HISTORY_SUMMARY_T Type

The metadata associated with the recommendation history and its related resources.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique OCID associated with the recommendation history.

`name`

(required) The name assigned to the resource.

`resource_type`

(required) The kind of resource.

`category_id`

(required) The unique OCID associated with the category.

`recommendation_id`

(required) The unique OCID associated with the recommendation.

`recommendation_name`

(required) The name assigned to the recommendation.

`resource_id`

(required) The unique OCID associated with the resource.

`resource_action_id`

(required) The unique OCID associated with the resource action.

`action`

(required)

`compartment_id`

(required) The OCID of the compartment.

`compartment_name`

(required) The name assigned to the compartment.

`lifecycle_state`

(required) The recommendation history's current state.

Allowed values are: 'ACTIVE', 'FAILED', 'INACTIVE', 'ATTACHING', 'DETACHING', 'DELETING', 'DELETED', 'UPDATING', 'CREATING'

`estimated_cost_saving`

(required) The estimated cost savings, in dollars, for the resource action.

`status`

(required) The current status of the resource action.

Allowed values are: 'PENDING', 'DISMISSED', 'POSTPONED', 'IMPLEMENTED'

`metadata`

(optional) Custom metadata key/value pairs for the resource action. **Metadata Example** \"metadata\" : { \"cpuRecommendedShape\": \"VM.Standard1.1\", \"computeMemoryUtilization\": \"26.05734124418388\", \"currentShape\": \"VM.Standard1.2\", \"instanceRecommendedShape\": \"VM.Standard1.1\", \"computeCpuUtilization\": \"7.930035319720132\", \"memoryRecommendedShape\": \"None\" }

`extended_metadata`

(optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the `metadata` object. They are distinguished from `metadata` fields in that these can be nested JSON objects (whereas `metadata` fields are string/string maps only). For example: `{\"CurrentShape\": {\"name\":\"VM.Standard2.16\"}, \"RecommendedShape\": {\"name\":\"VM.Standard2.8\"}}`

`time_created`

(optional) The date and time the recommendation history was created, in the format defined by RFC3339.

### DBMS_CLOUD_OCI_OPTIMIZER_HISTORY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_optimizer_history_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_HISTORY_COLLECTION_T Type

A list containing the recommendation history items that match filter criteria, if any. Results contain `HistorySummary` objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A collection of history summaries.

### DBMS_CLOUD_OCI_OPTIMIZER_PROFILE_T Type

The metadata associated with the profile.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique OCID of the profile.

`compartment_id`

(required) The OCID of the tenancy. The tenancy is the root compartment.

`name`

(required) The name assigned to the profile. Avoid entering confidential information.

`description`

(required) Text describing the profile. Avoid entering confidential information.

`aggregation_interval_in_days`

(optional) The time period over which to collect data for the recommendations, measured in number of days.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair applied without any predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{ \"orcl-cloud\": { \"free-tier-retained\": \"true\" } }`

`levels_configuration`

(optional)

`target_compartments`

(optional)

`target_tags`

(optional)

`lifecycle_state`

(required) The profile's current state.

Allowed values are: 'ACTIVE', 'FAILED', 'INACTIVE', 'ATTACHING', 'DETACHING', 'DELETING', 'DELETED', 'UPDATING', 'CREATING'

`time_created`

(required) The date and time the profile was created, in the format defined by RFC3339.

`time_updated`

(required) The date and time the profile was last updated, in the format defined by RFC3339.

### DBMS_CLOUD_OCI_OPTIMIZER_PROFILE_SUMMARY_T Type

The metadata associated with the profile summary.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique OCID of the profile.

`compartment_id`

(required) The OCID of the tenancy. The tenancy is the root compartment.

`name`

(required) The name assigned to the profile.

`description`

(required) Text describing the profile.

`aggregation_interval_in_days`

(optional) The time period over which to collect data for the recommendations, measured in number of days.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair applied without any predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{ \"orcl-cloud\": { \"free-tier-retained\": \"true\" } }`

`lifecycle_state`

(required) The profile's current state.

Allowed values are: 'ACTIVE', 'FAILED', 'INACTIVE', 'ATTACHING', 'DETACHING', 'DELETING', 'DELETED', 'UPDATING', 'CREATING'

`levels_configuration`

(optional)

`target_compartments`

(optional)

`target_tags`

(optional)

`time_created`

(required) The date and time the profile was created, in the format defined by RFC3339.

`time_updated`

(required) The date and time the profile was last updated, in the format defined by RFC3339.

### DBMS_CLOUD_OCI_OPTIMIZER_PROFILE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_optimizer_profile_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_PROFILE_COLLECTION_T Type

A list of profiles that match filter criteria, if any. Results contain `ProfileSummary` objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A collection of profile summaries.

### DBMS_CLOUD_OCI_OPTIMIZER_EVALUATED_METRIC_TBL Type

Nested table type of dbms_cloud_oci_optimizer_evaluated_metric_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_NUMBER_TBL Type

Nested table type of number.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_PROFILE_LEVEL_SUMMARY_T Type

The metadata associated with the profile level summary.

Syntax
```

```

Fields

Field Description

`name`

(required) A unique name for the profile level.

`recommendation_name`

(required) The name of the recommendation this profile level applies to.

`metrics`

(required) The metrics that will be evaluated by profiles using this profile level.

`default_interval`

(required) The default aggregation interval (in days) for profiles using this profile level.

`valid_intervals`

(required) An array of aggregation intervals (in days) allowed for profiles using this profile level.

`time_created`

(required) The date and time the category details were created, in the format defined by RFC3339.

`time_updated`

(required) The date and time the category details were last updated, in the format defined by RFC3339.

### DBMS_CLOUD_OCI_OPTIMIZER_PROFILE_LEVEL_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_optimizer_profile_level_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_PROFILE_LEVEL_COLLECTION_T Type

A list of profile levels that match the filter criteria, if any. The result contains `ProfileLevelSummary` objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A collection of profile levels.

### DBMS_CLOUD_OCI_OPTIMIZER_QUERY_DETAILS_T Type

The request object for querying the resource action details.

Syntax
```

```

Fields

Field Description

`query`

(optional) The query describing which resources to search for. For more information, see[Query Language Syntax](https://docs.oracle.com/iaas/Content/CloudAdvisor/Reference/query-syntax.htm).

### DBMS_CLOUD_OCI_OPTIMIZER_QUERYABLE_FIELD_SUMMARY_ABS_T

An individual field that can be used as part of a query filter.

Syntax
```

```

Fields

Field Description

`field_type`

(required) The type of the field, which dictates the semantics and query constraints that you can use when searching or querying.

Allowed values are: 'STRING', 'INTEGER', 'BOOLEAN', 'DATE_TIME', 'OBJECT'

`field_name`

(required) The name of the field to use when constructing the query. Field names are present for all types except `OBJECT`.

### DBMS_CLOUD_OCI_OPTIMIZER_QUERYABLE_FIELD_SUMMARY_ABS_TBL Type

Nested table type of dbms_cloud_oci_optimizer_queryable_field_summary_abs_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_QUERYABLE_FIELD_SUMMARY_T Type

An individual field that can be used as part of a query filter.

Syntax
```

```

Fields

Field Description

`object_properties`

(optional) If the field type is `OBJECT`, this property lists the individual properties of the object that can be queried.

### DBMS_CLOUD_OCI_OPTIMIZER_QUERYABLE_FIELD_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_optimizer_queryable_field_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_QUERYABLE_FIELD_COLLECTION_T Type

List of the fields that are indexed for querying and their associated value types. Results contain `QueryableFieldSummary` objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A collection of queryable field summaries.

### DBMS_CLOUD_OCI_OPTIMIZER_SUPPORTED_LEVEL_T Type

A system defined profile level supported by the recommendation.

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of the profile level.

### DBMS_CLOUD_OCI_OPTIMIZER_SUPPORTED_LEVEL_TBL Type

Nested table type of dbms_cloud_oci_optimizer_supported_level_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_SUPPORTED_LEVELS_T Type

Optional. The profile levels supported by a recommendation. For example, profile level values could be `Low`, `Medium`, and `High`. Not all recommendations support this field.

Syntax
```

```

Fields

Field Description

`items`

(optional) The list of supported levels.

### DBMS_CLOUD_OCI_OPTIMIZER_RECOMMENDATION_T Type

The metadata associated with the recommendation.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique OCID associated with the recommendation.

`compartment_id`

(required) The OCID of the tenancy. The tenancy is the root compartment.

`category_id`

(required) The unique OCID associated with the category.

`name`

(required) The name assigned to the recommendation.

`description`

(required) Text describing the recommendation.

`importance`

(required) The level of importance assigned to the recommendation.

Allowed values are: 'CRITICAL', 'HIGH', 'MODERATE', 'LOW', 'MINOR'

`resource_counts`

(required) An array of `ResourceCount` objects grouped by the status of the resource actions.

`lifecycle_state`

(required) The recommendation's current state.

Allowed values are: 'ACTIVE', 'FAILED', 'INACTIVE', 'ATTACHING', 'DETACHING', 'DELETING', 'DELETED', 'UPDATING', 'CREATING'

`estimated_cost_saving`

(required) The estimated cost savings, in dollars, for the recommendation.

`status`

(required) The current status of the recommendation.

Allowed values are: 'PENDING', 'DISMISSED', 'POSTPONED', 'IMPLEMENTED'

`time_status_begin`

(required) The date and time that the recommendation entered its current status. The format is defined by RFC3339. For example, \"The status of the recommendation changed from `pending` to `current(ignored)` on this date and time.\"

`time_status_end`

(optional) The date and time the current status will change. The format is defined by RFC3339. For example, \"The current `postponed` status of the recommendation will end and change to `pending` on this date and time.\"

`time_created`

(optional) The date and time the recommendation details were created, in the format defined by RFC3339.

`time_updated`

(optional) The date and time the recommendation details were last updated, in the format defined by RFC3339.

`supported_levels`

(optional)

`extended_metadata`

(optional) Additional metadata key/value pairs for the recommendation. For example: `{\"EstimatedSaving\": \"200\"}`

### DBMS_CLOUD_OCI_OPTIMIZER_RECOMMENDATION_SUMMARY_T Type

The metadata associated with the recommendation summary.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique OCID associated with the recommendation.

`compartment_id`

(required) The OCID of the tenancy. The tenancy is the root compartment.

`category_id`

(required) The unique OCID associated with the category.

`name`

(required) The name assigned to the recommendation.

`description`

(required) Text describing the recommendation.

`importance`

(required) The level of importance assigned to the recommendation.

Allowed values are: 'CRITICAL', 'HIGH', 'MODERATE', 'LOW', 'MINOR'

`resource_counts`

(required) An array of `ResourceCount` objects grouped by the status of the resource actions.

`lifecycle_state`

(required) The recommendation's current state.

Allowed values are: 'ACTIVE', 'FAILED', 'INACTIVE', 'ATTACHING', 'DETACHING', 'DELETING', 'DELETED', 'UPDATING', 'CREATING'

`estimated_cost_saving`

(required) The estimated cost savings, in dollars, for the recommendation.

`status`

(required) The current status of the recommendation.

Allowed values are: 'PENDING', 'DISMISSED', 'POSTPONED', 'IMPLEMENTED'

`time_status_begin`

(required) The date and time that the recommendation entered its current status. The format is defined by RFC3339. For example, \"The status of the recommendation changed from `pending` to `current(ignored)` on this date and time.\"

`time_status_end`

(optional) The date and time the current status will change. The format is defined by RFC3339. For example, \"The current `postponed` status of the recommendation will end and change to `pending` on this date and time.\"

`time_created`

(optional) The date and time the recommendation details were created, in the format defined by RFC3339.

`time_updated`

(optional) The date and time the recommendation details were last updated, in the format defined by RFC3339.

`supported_levels`

(optional)

`extended_metadata`

(optional) Additional metadata key/value pairs for the recommendation summary. For example: `{\"EstimatedSaving\": \"200\"}`

### DBMS_CLOUD_OCI_OPTIMIZER_RECOMMENDATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_optimizer_recommendation_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_RECOMMENDATION_COLLECTION_T Type

A list of recommendations that match filter criteria, if any. Results contain `RecommendationSummary` objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A collection of recommendations.

### DBMS_CLOUD_OCI_OPTIMIZER_JSON_ELEMENT_T_TBL Type

Nested table type of json_element_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_STRATEGY_PARAMETER_T Type

The metadata associated with the strategy parameter.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the strategy parameter.

`l_type`

(required) The type of strategy parameter.

Allowed values are: 'STRING', 'BOOLEAN', 'NUMBER', 'DATETIME'

`description`

(required) Text describing the strategy parameter.

`is_required`

(required) Whether this parameter is required.

`default_value`

(optional) A default value used for the strategy parameter.

`possible_values`

(optional) The list of possible values used for these strategy parameters.

### DBMS_CLOUD_OCI_OPTIMIZER_STRATEGY_PARAMETER_TBL Type

Nested table type of dbms_cloud_oci_optimizer_strategy_parameter_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_STRATEGY_T Type

The metadata associated with the strategy. The strategy is the method used to apply the recommendation.

Syntax
```

```

Fields

Field Description

`strategy_name`

(required) The name of the strategy.

`is_default`

(required) Whether this is the default recommendation strategy.

`parameters_definition`

(optional) The list of strategies for the parameters.

### DBMS_CLOUD_OCI_OPTIMIZER_STRATEGY_TBL Type

Nested table type of dbms_cloud_oci_optimizer_strategy_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_RECOMMENDATION_STRATEGY_SUMMARY_T Type

The metadata associated with the recommendation strategy.

Syntax
```

```

Fields

Field Description

`name`

(required) The display name of the recommendation.

`strategies`

(required) The list of strategies used.

### DBMS_CLOUD_OCI_OPTIMIZER_RECOMMENDATION_STRATEGY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_optimizer_recommendation_strategy_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_RECOMMENDATION_STRATEGY_COLLECTION_T Type

A list of strategies that match filter criteria, if any. Results contain `RecommendationStrategySummary` objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A collection of recommendation strategy summaries.

### DBMS_CLOUD_OCI_OPTIMIZER_RESOURCE_ACTION_T Type

The metadata associated with the resource action.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique OCID associated with the resource action.

`category_id`

(required) The unique OCID associated with the category.

`recommendation_id`

(required) The unique OCID associated with the recommendation.

`resource_id`

(required) The unique OCID associated with the resource.

`name`

(required) The name assigned to the resource.

`resource_type`

(required) The kind of resource.

`compartment_id`

(required) The OCID of the compartment.

`compartment_name`

(required) The name associated with the compartment.

`action`

(required)

`lifecycle_state`

(required) The resource action's current state.

Allowed values are: 'ACTIVE', 'FAILED', 'INACTIVE', 'ATTACHING', 'DETACHING', 'DELETING', 'DELETED', 'UPDATING', 'CREATING'

`estimated_cost_saving`

(required) The estimated cost savings, in dollars, for the resource action.

`status`

(required) The current status of the resource action.

Allowed values are: 'PENDING', 'DISMISSED', 'POSTPONED', 'IMPLEMENTED'

`time_status_begin`

(required) The date and time that the resource action entered its current status. The format is defined by RFC3339. For example, \"The status of the resource action changed from `pending` to `current(ignored)` on this date and time.\"

`time_status_end`

(optional) The date and time the current status will change. The format is defined by RFC3339. For example, \"The current `postponed` status of the resource action will end and change to `pending` on this date and time.\"

`metadata`

(optional) Custom metadata key/value pairs for the resource action. **Metadata Example** \"metadata\" : { \"cpuRecommendedShape\": \"VM.Standard1.1\", \"computeMemoryUtilization\": \"26.05734124418388\", \"currentShape\": \"VM.Standard1.2\", \"instanceRecommendedShape\": \"VM.Standard1.1\", \"computeCpuUtilization\": \"7.930035319720132\", \"memoryRecommendedShape\": \"None\" }

`extended_metadata`

(optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the `metadata` object. They are distinguished from `metadata` fields in that these can be nested JSON objects (whereas `metadata` fields are string/string maps only). For example: `{\"CurrentShape\": {\"name\":\"VM.Standard2.16\"}, \"RecommendedShape\": {\"name\":\"VM.Standard2.8\"}}`

`time_created`

(optional) The date and time the resource action details were created, in the format defined by RFC3339.

`time_updated`

(optional) The date and time the resource action details were last updated, in the format defined by RFC3339.

### DBMS_CLOUD_OCI_OPTIMIZER_RESOURCE_ACTION_SUMMARY_T Type

The metadata associated with the resource action summary.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique OCID associated with the resource action.

`category_id`

(required) The unique OCID associated with the category.

`recommendation_id`

(required) The unique OCID associated with the recommendation.

`resource_id`

(required) The unique OCID associated with the resource.

`name`

(required) The name assigned to the resource.

`resource_type`

(required) The kind of resource.

`compartment_id`

(required) The OCID of the compartment.

`compartment_name`

(required) The name associated with the compartment.

`action`

(required)

`lifecycle_state`

(required) The resource action's current state.

Allowed values are: 'ACTIVE', 'FAILED', 'INACTIVE', 'ATTACHING', 'DETACHING', 'DELETING', 'DELETED', 'UPDATING', 'CREATING'

`estimated_cost_saving`

(required) The estimated cost savings, in dollars, for the resource action.

`status`

(required) The current status of the resource action.

Allowed values are: 'PENDING', 'DISMISSED', 'POSTPONED', 'IMPLEMENTED'

`time_status_begin`

(required) The date and time that the resource action entered its current status. The format is defined by RFC3339. For example, \"The status of the resource action changed from `pending` to `current(ignored)` on this date and time.\"

`time_status_end`

(optional) The date and time the current status will change. The format is defined by RFC3339. For example, \"The current `postponed` status of the resource action will end and change to `pending` on this date and time.\"

`metadata`

(optional) Custom metadata key/value pairs for the resource action. **Metadata Example** \"metadata\" : { \"cpuRecommendedShape\": \"VM.Standard1.1\", \"computeMemoryUtilization\": \"26.05734124418388\", \"currentShape\": \"VM.Standard1.2\", \"instanceRecommendedShape\": \"VM.Standard1.1\", \"computeCpuUtilization\": \"7.930035319720132\", \"memoryRecommendedShape\": \"None\" }

`extended_metadata`

(optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the `metadata` object. They are distinguished from `metadata` fields in that these can be nested JSON objects (whereas `metadata` fields are string/string maps only). For example: `{\"CurrentShape\": {\"name\":\"VM.Standard2.16\"}, \"RecommendedShape\": {\"name\":\"VM.Standard2.8\"}}`

`time_created`

(optional) The date and time the resource action details were created, in the format defined by RFC3339.

`time_updated`

(optional) The date and time the resource action details were last updated, in the format defined by RFC3339.

### DBMS_CLOUD_OCI_OPTIMIZER_RESOURCE_ACTION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_optimizer_resource_action_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_RESOURCE_ACTION_COLLECTION_T Type

A list of resource actions that match filter criteria, if any. Results contain `ResourceActionSummary` objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A collection of resource actions.

### DBMS_CLOUD_OCI_OPTIMIZER_UPDATE_ENROLLMENT_STATUS_DETAILS_T Type

The request object for updating the enrollment status details.

Syntax
```

```

Fields

Field Description

`status`

(required) The Cloud Advisor enrollment status.

Allowed values are: 'ACTIVE', 'INACTIVE'

### DBMS_CLOUD_OCI_OPTIMIZER_UPDATE_PROFILE_DETAILS_T Type

Details for updating a profile.

Syntax
```

```

Fields

Field Description

`description`

(optional) Text describing the profile. Avoid entering confidential information.

`aggregation_interval_in_days`

(optional) The time period over which to collect data for the recommendations, measured in number of days.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair applied without any predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{ \"orcl-cloud\": { \"free-tier-retained\": \"true\" } }`

`levels_configuration`

(optional)

`target_compartments`

(optional)

`target_tags`

(optional)

`name`

(optional) The name assigned to the profile. Avoid entering confidential information.

### DBMS_CLOUD_OCI_OPTIMIZER_UPDATE_RECOMMENDATION_DETAILS_T Type

The request object for updating the recommendation details.

Syntax
```

```

Fields

Field Description

`status`

(required) The status of the recommendation.

Allowed values are: 'PENDING', 'DISMISSED', 'POSTPONED', 'IMPLEMENTED'

`time_status_end`

(optional) The date and time the current status will change. The format is defined by RFC3339. For example, \"The current `postponed` status of the recommendation will end and change to `pending` on this date and time.\"

### DBMS_CLOUD_OCI_OPTIMIZER_UPDATE_RESOURCE_ACTION_DETAILS_T Type

The request object for updating the resource action details.

Syntax
```

```

Fields

Field Description

`status`

(required) The status of the resource action.

Allowed values are: 'PENDING', 'DISMISSED', 'POSTPONED', 'IMPLEMENTED'

`time_status_end`

(optional) The date and time the current status will change. The format is defined by RFC3339. For example, \"The current `postponed` status of the resource action will end and change to `pending` on this date and time.\"

### DBMS_CLOUD_OCI_OPTIMIZER_WORK_REQUEST_RESOURCE_T Type

Details about the resource entity.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way in which this resource was affected by the work tracked by the work request. A resource being created, updated, or deleted remains in the `IN_PROGRESS` state until work is complete for that resource. At that point, the resource transitions to the `CREATED`, `UPDATED`, or `DELETED` state.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED'

`identifier`

(required) The resource identifier the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata

`metadata`

(optional) Additional information about the resource.

### DBMS_CLOUD_OCI_OPTIMIZER_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_optimizer_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_WORK_REQUEST_T Type

The asynchronous API request does not take effect immediately. This request spawns an asynchronous workflow to fulfill the request. WorkRequest objects provide visibility for in-progress workflows.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) An enum-like description of the type of work the work request is doing.

Allowed values are: 'BULK_APPLY_RECOMMENDATIONS'

`status`

(required) The current status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The OCID of the work request.

`compartment_id`

(required) The OCID of the compartment that contains the work request.

`resources`

(required) The resources this work request affects.

`percent_complete`

(required) How much progress the operation has made.

`time_accepted`

(required) Date and time the work was accepted, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_started`

(optional) Date and time the work started, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_finished`

(optional) Date and time the work completed, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_OPTIMIZER_WORK_REQUEST_TBL Type

Nested table type of dbms_cloud_oci_optimizer_work_request_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_WORK_REQUEST_COLLECTION_T Type

A list of work requests that match filter criteria, if any. Results contain `WorkRequest` objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A collection of work requests.

### DBMS_CLOUD_OCI_OPTIMIZER_WORK_REQUEST_ERROR_T Type

Details about errors encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occurred.

`message`

(required) A human-readable error string.

`l_timestamp`

(required) Date and time the error happened, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_OPTIMIZER_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_optimizer_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_WORK_REQUEST_ERROR_COLLECTION_T Type

A list of work request errors that match filter criteria, if any. Results contain `WorkRequestError` objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A collection of work request errors.

### DBMS_CLOUD_OCI_OPTIMIZER_WORK_REQUEST_LOG_ENTRY_T Type

Details about the log entity.

Syntax
```

```

Fields

Field Description

`message`

(required) A human-readable error string.

`l_timestamp`

(required) Date and time the log was written, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_OPTIMIZER_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_optimizer_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPTIMIZER_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

A list of work request logs that match filter criteria, if any. Results contain `WorkRequestLogEntry` objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A collection of work request log entries.

- [Optimizer Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-5A857A0A-4C52-43BA-A3F2-AE606614B5CF)
- [DBMS_CLOUD_OCI_OPTIMIZER_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-4ACD26EE-1491-4D16-92B8-4FF8124F4AD6)
- [DBMS_CLOUD_OCI_OPTIMIZER_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-5CDAE783-2911-4FF5-9116-5BE5AC9E2C5D)
- [DBMS_CLOUD_OCI_OPTIMIZER_BULK_APPLY_RESOURCE_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-D2DB3E2A-DE01-4561-A9E2-02DC5420EF22)
- [DBMS_CLOUD_OCI_OPTIMIZER_BULK_APPLY_RESOURCE_ACTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-2838868F-FB78-47D5-AD10-1DC4A4274773)
- [DBMS_CLOUD_OCI_OPTIMIZER_BULK_APPLY_RECOMMENDATIONS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-A7A4A1E2-AC63-429B-8BAA-E2C5BD8972F9)
- [DBMS_CLOUD_OCI_OPTIMIZER_RECOMMENDATION_COUNT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-AA95BBD9-5209-400E-8DD0-42BD1F15163D)
- [DBMS_CLOUD_OCI_OPTIMIZER_RESOURCE_COUNT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-E613DAA5-7F07-46BD-BD7F-918B12FCC35D)
- [DBMS_CLOUD_OCI_OPTIMIZER_RECOMMENDATION_COUNT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-2162C293-867B-489F-927B-A215C83A69AC)
- [DBMS_CLOUD_OCI_OPTIMIZER_RESOURCE_COUNT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-4A2381D6-530B-4365-88A3-10ECCB5EFC4E)
- [DBMS_CLOUD_OCI_OPTIMIZER_CATEGORY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-87163EA4-0B93-483A-A474-60D4E645F8E0)
- [DBMS_CLOUD_OCI_OPTIMIZER_CATEGORY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-F67AC66B-0C1F-4BF8-A02A-26CF2EF490B5)
- [DBMS_CLOUD_OCI_OPTIMIZER_CATEGORY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-D08AA4AD-6D9E-48BE-AB6F-8B59C7B534CC)
- [DBMS_CLOUD_OCI_OPTIMIZER_CATEGORY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-A4BE9F55-0627-4819-A342-FDC37C72BFA2)
- [DBMS_CLOUD_OCI_OPTIMIZER_LEVEL_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-1CA818CA-26D8-432E-AFAD-FF150344F1E7)
- [DBMS_CLOUD_OCI_OPTIMIZER_LEVEL_CONFIGURATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-EF1A13E6-F33A-490D-A6E0-DAC762522D59)
- [DBMS_CLOUD_OCI_OPTIMIZER_LEVELS_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-37C2DF0D-63BE-4146-8EC4-9571AFD6DEFB)
- [DBMS_CLOUD_OCI_OPTIMIZER_TARGET_COMPARTMENTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-5101A7DC-E162-4F7B-AA36-29DF3C3D3C90)
- [DBMS_CLOUD_OCI_OPTIMIZER_TARGET_TAG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-A14F1B2D-CC74-41C1-B259-196E5F7819CD)
- [DBMS_CLOUD_OCI_OPTIMIZER_TARGET_TAG_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-03B33920-58DD-42CA-BBAC-A5E7B51B02CB)
- [DBMS_CLOUD_OCI_OPTIMIZER_TARGET_TAGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-D76B8033-507E-4F8E-A9F4-45C130145CA0)
- [DBMS_CLOUD_OCI_OPTIMIZER_CREATE_PROFILE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-9BD4737A-8F31-49B9-8EFD-00471E29544D)
- [DBMS_CLOUD_OCI_OPTIMIZER_ENROLLMENT_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-614CB8D7-0571-46EF-B3B6-F9DD0A14E474)
- [DBMS_CLOUD_OCI_OPTIMIZER_ENROLLMENT_STATUS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-43FFA2B0-BBB2-4918-B019-5C0C6C0A8193)
- [DBMS_CLOUD_OCI_OPTIMIZER_ENROLLMENT_STATUS_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-6A5A27C2-FDC0-4EDF-BE42-8428DA214463)
- [DBMS_CLOUD_OCI_OPTIMIZER_ENROLLMENT_STATUS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-BE2ECFC1-D2BC-4DF6-A45B-C3CB1A677AA3)
- [DBMS_CLOUD_OCI_OPTIMIZER_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-B65B4CBE-0408-42B1-9422-77F02DEF5055)
- [DBMS_CLOUD_OCI_OPTIMIZER_EVALUATED_METRIC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-8E4B1B12-693F-47C6-85D0-E60046799112)
- [DBMS_CLOUD_OCI_OPTIMIZER_HISTORY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-3BD7BCD6-9FE7-41B6-91DB-AF4E8469483C)
- [DBMS_CLOUD_OCI_OPTIMIZER_HISTORY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-77DF7745-9A72-4867-900A-9A5D4F441465)
- [DBMS_CLOUD_OCI_OPTIMIZER_HISTORY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-1CA8EA80-8C41-454A-957E-17FDD986B666)
- [DBMS_CLOUD_OCI_OPTIMIZER_PROFILE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-BD82EC8B-48ED-4C26-AF99-A7B9280D896A)
- [DBMS_CLOUD_OCI_OPTIMIZER_PROFILE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-86A33F95-C3D0-431A-A4DA-D802E96E96BF)
- [DBMS_CLOUD_OCI_OPTIMIZER_PROFILE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-8B8A3CCD-F3FA-4B3A-B018-B0C415E8CD43)
- [DBMS_CLOUD_OCI_OPTIMIZER_PROFILE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-C9944B17-6D64-4C7E-89CF-C236086D2612)
- [DBMS_CLOUD_OCI_OPTIMIZER_EVALUATED_METRIC_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-56E70547-A815-4D92-939C-0B3F7A9455BD)
- [DBMS_CLOUD_OCI_OPTIMIZER_NUMBER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-3F499976-5588-49A9-8639-71B7A564744D)
- [DBMS_CLOUD_OCI_OPTIMIZER_PROFILE_LEVEL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-06E28510-9EFB-4530-BB23-D009DE159E29)
- [DBMS_CLOUD_OCI_OPTIMIZER_PROFILE_LEVEL_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-CA0CCDD9-1DEA-4B25-AE1C-6826CF9A8B46)
- [DBMS_CLOUD_OCI_OPTIMIZER_PROFILE_LEVEL_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-12B8212B-13F8-440D-BA94-D5F26485AA99)
- [DBMS_CLOUD_OCI_OPTIMIZER_QUERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-2298F452-AB09-40E4-9E35-C8067BE14625)
- [DBMS_CLOUD_OCI_OPTIMIZER_QUERYABLE_FIELD_SUMMARY_ABS_T](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-EE8DAD07-03FF-4D84-86A2-26AB6209C3A8)
- [DBMS_CLOUD_OCI_OPTIMIZER_QUERYABLE_FIELD_SUMMARY_ABS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-E6CB25E8-4572-4A21-9C11-29E66D60FFF5)
- [DBMS_CLOUD_OCI_OPTIMIZER_QUERYABLE_FIELD_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-92AB59DE-0EC6-4C25-9045-37A453005126)
- [DBMS_CLOUD_OCI_OPTIMIZER_QUERYABLE_FIELD_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-029E6FFA-67E5-44D0-9AA6-76EACC7FF500)
- [DBMS_CLOUD_OCI_OPTIMIZER_QUERYABLE_FIELD_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-D9971F91-9BD5-472B-A39E-3980DD4AFA87)
- [DBMS_CLOUD_OCI_OPTIMIZER_SUPPORTED_LEVEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-7707167B-DADE-41DD-96B8-5F36E8357859)
- [DBMS_CLOUD_OCI_OPTIMIZER_SUPPORTED_LEVEL_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-95E9A4DB-87A8-4055-927C-891C5961EF10)
- [DBMS_CLOUD_OCI_OPTIMIZER_SUPPORTED_LEVELS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-53E73A12-0F39-47EC-992A-60E2F92FF2AD)
- [DBMS_CLOUD_OCI_OPTIMIZER_RECOMMENDATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-5A832C7D-10CB-4D36-ABE6-109E9A4A2153)
- [DBMS_CLOUD_OCI_OPTIMIZER_RECOMMENDATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-3F7912A9-F9CE-4A64-A310-DCE111319EC0)
- [DBMS_CLOUD_OCI_OPTIMIZER_RECOMMENDATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-FDC2E63F-44A4-4E4E-AE7C-E15CD33EE728)
- [DBMS_CLOUD_OCI_OPTIMIZER_RECOMMENDATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-1A457087-0D47-40CA-AD21-82676524686A)
- [DBMS_CLOUD_OCI_OPTIMIZER_JSON_ELEMENT_T_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-F50CF093-D2F2-4BAA-8972-D5C5AE8D6976)
- [DBMS_CLOUD_OCI_OPTIMIZER_STRATEGY_PARAMETER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-76A061F2-4C5E-4E04-8BBA-43092CB29359)
- [DBMS_CLOUD_OCI_OPTIMIZER_STRATEGY_PARAMETER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-9CEC20D4-864E-4B99-9A56-9B68DC175D11)
- [DBMS_CLOUD_OCI_OPTIMIZER_STRATEGY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-3AE0931C-6BB3-4CD4-8C2B-1E8DF328EBFC)
- [DBMS_CLOUD_OCI_OPTIMIZER_STRATEGY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-A8CE8928-4396-4C58-ABA7-366B1E85B029)
- [DBMS_CLOUD_OCI_OPTIMIZER_RECOMMENDATION_STRATEGY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-7BF3A8A3-1880-4333-ADC1-6440F00F80F2)
- [DBMS_CLOUD_OCI_OPTIMIZER_RECOMMENDATION_STRATEGY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-95504AAB-FE5A-4E46-A29C-E5AC182EB459)
- [DBMS_CLOUD_OCI_OPTIMIZER_RECOMMENDATION_STRATEGY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-D93C7284-4032-4002-81B0-69F5255D173A)
- [DBMS_CLOUD_OCI_OPTIMIZER_RESOURCE_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-F5C3E5A8-6588-4368-946A-C44BFE1EFB49)
- [DBMS_CLOUD_OCI_OPTIMIZER_RESOURCE_ACTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-4F0BBC21-1E2F-47CC-AEFE-46AAFE5E776E)
- [DBMS_CLOUD_OCI_OPTIMIZER_RESOURCE_ACTION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-330A2785-C2C2-45A6-B934-398E4C3E045E)
- [DBMS_CLOUD_OCI_OPTIMIZER_RESOURCE_ACTION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-C941B288-C3A4-43F7-BC61-94D6C7424F6E)
- [DBMS_CLOUD_OCI_OPTIMIZER_UPDATE_ENROLLMENT_STATUS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-71686768-7494-4CBF-AF77-C1F6129364A5)
- [DBMS_CLOUD_OCI_OPTIMIZER_UPDATE_PROFILE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-295D99DA-98D4-48CA-B890-08EB7655A983)
- [DBMS_CLOUD_OCI_OPTIMIZER_UPDATE_RECOMMENDATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-273169D6-7DCB-448F-A49B-7F4D7A7200C1)
- [DBMS_CLOUD_OCI_OPTIMIZER_UPDATE_RESOURCE_ACTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-384174D7-7D74-4778-8EE0-BF245918D887)
- [DBMS_CLOUD_OCI_OPTIMIZER_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-D1DE07AF-61AC-4671-91D8-C2456C04E408)
- [DBMS_CLOUD_OCI_OPTIMIZER_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-A14A583F-F7B6-47DE-B999-246736BECE74)
- [DBMS_CLOUD_OCI_OPTIMIZER_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-11E112BB-E1B5-4E70-AAD8-F17EB043983E)
- [DBMS_CLOUD_OCI_OPTIMIZER_WORK_REQUEST_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-0F8DFC54-FA3C-44A7-881D-8EF4C6DCB52E)
- [DBMS_CLOUD_OCI_OPTIMIZER_WORK_REQUEST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-125B0EDF-400F-4BC6-BA63-F83B93431AA7)
- [DBMS_CLOUD_OCI_OPTIMIZER_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-8D9394C2-3549-4D0F-A973-D8EC9FA08AEA)
- [DBMS_CLOUD_OCI_OPTIMIZER_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-5963DF8A-FC02-4466-8DED-DAF2A483AB66)
- [DBMS_CLOUD_OCI_OPTIMIZER_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-A38DE58F-72AE-47A5-BDA1-359DA5D45D18)
- [DBMS_CLOUD_OCI_OPTIMIZER_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-0A7BDA79-4963-42D9-BEB2-C66560777D5C)
- [DBMS_CLOUD_OCI_OPTIMIZER_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-28A2A288-385D-4138-91C4-AD7D01142EC5)
- [DBMS_CLOUD_OCI_OPTIMIZER_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/optimizer_t.html#ADSDK-GUID-8852EDA3-3AB0-4FE6-82B8-7EE6FAAACC4D)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
