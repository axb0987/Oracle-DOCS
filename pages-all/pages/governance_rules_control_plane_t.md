# Governance Rules CP Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html
- Fetched: 2026-09-05 19:16 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#dcoc-content-body)

## Governance Rules CP Common Types

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_TEMPLATE_T Type

Template object for the governance rule. It could be of type QUOTA, TAG or REGION_RESTRICTION.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS. Example: `QUOTA`

Allowed values are: 'QUOTA', 'TAG', 'ALLOWED_REGIONS'

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_ALLOWED_REGIONS_TEMPLATE_T Type

Template for governance rules of type allowed regions (ALLOWED_REGIONS).

Syntax
```

```

`dbms_cloud_oci_governance_rules_control_plane_allowed_regions_template_t`is a subtype of the`dbms_cloud_oci_governance_rules_control_plane_template_t`type.

Fields

Field Description

`display_name`

(required) Display name of the allowed region resource.

`description`

(optional) Description of the allowed region resource.

`regions`

(required) List of allowed regions.

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_ASSOCIATION_T Type

Association represents the basis on which the governance rule will be applied to the opted-in child tenancies.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of Association, can be one of TENANCY, ALL or TAG. We support only TENANCY for now. Example: `TENANCY`

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_BASE_TAG_DEFINITION_VALIDATOR_T Type

Validates a definedTag value. Each validator performs validation steps in addition to the standard validation for definedTag values. For more information, see[Limits on Tags](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm#limits). If you define a validator after a value has been set for a defined tag, then any updates that attempt to change the value must pass the additional validation defined by the current rule. Previously set values (even those that would fail the current validation) are not updated. You can still update other attributes to resources that contain a non-valid defined tag. To clear the validator call UpdateTag with[DefaultTagDefinitionValidator](https://docs.oracle.com/iaas/api/#/en/identity/latest/datatypes/DefaultTagDefinitionValidator).

Syntax
```

```

Fields

Field Description

`validator_type`

(required) Specifies the type of validation: a static value (no validation) or a list.

Allowed values are: 'ENUM', 'DEFAULT'

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_CREATE_GOVERNANCE_RULE_DETAILS_T Type

Request object for CreateGovernanceRule operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the root compartment containing the governance rule.

`display_name`

(required) Display name of the governance rule.

`description`

(optional) Description of the governance rule.

`l_type`

(required) Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS. Example: `QUOTA`

Allowed values are: 'QUOTA', 'TAG', 'ALLOWED_REGIONS'

`creation_option`

(required) The type of option used to create the governance rule, could be one of TEMPLATE or CLONE. Example: `TEMPLATE`

Allowed values are: 'TEMPLATE', 'CLONE'

`template`

(required)

`related_resource_id`

(optional) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the resource, which was used as a template to create this governance rule.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_CREATE_INCLUSION_CRITERION_DETAILS_T Type

Request object for Createinclusion criterion operation.

Syntax
```

```

Fields

Field Description

`governance_rule_id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the governance rule. Every inclusion criterion is associated with a governance rule.

`l_type`

(required) Type of inclusion criterion - TENANCY, ALL or TAG. We support TENANCY and ALL for now.

`association`

(optional)

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_DEFAULT_TAG_DEFINITION_VALIDATOR_T Type

Use this validator to clear any existing validator on the tag key definition with the UpdateTag operation. Using this `validatorType` is the same as not setting any value on the validator field. The resultant value for `validatorType` returned in the response body is `null`.

Syntax
```

```

`dbms_cloud_oci_governance_rules_control_plane_default_tag_definition_validator_t`is a subtype of the`dbms_cloud_oci_governance_rules_control_plane_base_tag_definition_validator_t`type.

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_ENFORCED_GOVERNANCE_RULE_T Type

Represents the governance rule shown to the child which is a subset of governance rule resource in parent tenancy.

Syntax
```

```

Fields

Field Description

`id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the enforced governance rule.

`compartment_id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the child's root compartment to which the governance rule is attached.

`governance_rule_display_name`

(required) Display name of the governance rule.

`l_type`

(required) Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS. Example: `QUOTA`

Allowed values are: 'QUOTA', 'TAG', 'ALLOWED_REGIONS'

`template`

(required)

`lifecycle_state`

(required) The current state of the governance rule.

Allowed values are: 'ACTIVE', 'DELETED'

`time_created`

(required) Date and time the governance rule was created. An RFC3339 formatted datetime string. Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(required) Date and time the governance rule was updated. An RFC3339 formatted datetime string. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_ENFORCED_GOVERNANCE_RULE_SUMMARY_T Type

A summary of the enforced governance rule.

Syntax
```

```

Fields

Field Description

`id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the enforced governance rule.

`compartment_id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the child's root compartment to which the governance rule is attached.

`governance_rule_display_name`

(required) Display name of the governance rule.

`l_type`

(required) Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS. Example: `QUOTA`

Allowed values are: 'QUOTA', 'TAG', 'ALLOWED_REGIONS'

`lifecycle_state`

(required) The current state of the governance rule.

Allowed values are: 'ACTIVE', 'DELETED'

`time_created`

(required) Date and time the governance rule was created. An RFC3339 formatted datetime string. Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(required) Date and time the governance rule was updated. An RFC3339 formatted datetime string. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_ENFORCED_GOVERNANCE_RULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_governance_rules_control_plane_enforced_governance_rule_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_ENFORCED_GOVERNANCE_RULE_COLLECTION_T Type

Results of an enforced governance rule search. Contains EnforcedGovernanceRuleSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of EnforcedGovernanceRuleSummary objects.

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_ENUM_TAG_DEFINITION_VALIDATOR_T Type

Used to validate the value set for a defined tag and contains the list of allowable `values`. You must specify at least one valid value in the `values` array. You can't have blank or or empty strings (`\"\"`). Duplicate values are not allowed.

Syntax
```

```

`dbms_cloud_oci_governance_rules_control_plane_enum_tag_definition_validator_t`is a subtype of the`dbms_cloud_oci_governance_rules_control_plane_base_tag_definition_validator_t`type.

Fields

Field Description

`l_values`

(optional) The list of allowed values for a definedTag value.

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_ERROR_T Type

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

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_GOVERNANCE_RULE_T Type

Represents a rule in parent tenancy which governs resources in child tenancies.

Syntax
```

```

Fields

Field Description

`id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the governance rule.

`compartment_id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the root compartment containing the governance rule.

`display_name`

(required) Display name of the governance rule.

`description`

(optional) Description of the governance rule.

`l_type`

(required) Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS. Example: `QUOTA`

Allowed values are: 'QUOTA', 'TAG', 'ALLOWED_REGIONS'

`creation_option`

(required) The type of option used to create the governance rule, could be one of TEMPLATE or CLONE. Example: `TEMPLATE`

Allowed values are: 'TEMPLATE', 'CLONE'

`template`

(required)

`related_resource_id`

(optional) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the resource, which was used as a template to create this governance rule.

`time_created`

(required) Date and time the governance rule was created. An RFC3339 formatted datetime string. Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(required) Date and time the governance rule was updated. An RFC3339 formatted datetime string. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state of the governance rule.

Allowed values are: 'ACTIVE', 'DELETED'

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_GOVERNANCE_RULE_SUMMARY_T Type

A summary of the governance rule.

Syntax
```

```

Fields

Field Description

`id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the governance rule.

`compartment_id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the root compartment containing the governance rule.

`display_name`

(required) Display name of the governance rule.

`l_type`

(required) Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS. Example: `QUOTA`

Allowed values are: 'QUOTA', 'TAG', 'ALLOWED_REGIONS'

`creation_option`

(required) The type of option used to create the governance rule, could be one of TEMPLATE or CLONE. Example: `TEMPLATE`

Allowed values are: 'TEMPLATE', 'CLONE'

`time_created`

(required) Date and time the governance rule was created. An RFC3339 formatted datetime string. Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(required) Date and time the governance rule was updated. An RFC3339 formatted datetime string. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state of the governance rule.

Allowed values are: 'ACTIVE', 'DELETED'

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_GOVERNANCE_RULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_governance_rules_control_plane_governance_rule_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_GOVERNANCE_RULE_COLLECTION_T Type

Results of a governance rule search. Contains GovernanceRuleSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of GovernanceRuleSummary objects.

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_INCLUSION_CRITERION_T Type

Represents the criterion for the inclusion of the child tenancies under a governance rule. This can be either TENANCY or TAG.

Syntax
```

```

Fields

Field Description

`id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the inclusion criterion.

`governance_rule_id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the governance rule. Every inclusion criterion is associated with a governance rule.

`l_type`

(required) Type of inclusion criterion - TENANCY, ALL or TAG. We support TENANCY and ALL for now.

Allowed values are: 'TENANCY', 'ALL'

`association`

(optional)

`lifecycle_state`

(required) The current state of the inclusion criterion.

Allowed values are: 'ACTIVE', 'DELETED'

`time_created`

(required) Date and time the inclusion criterion was created. An RFC3339 formatted datetime string. Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(required) Date and time the inclusion criterion was updated. An RFC3339 formatted datetime string. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_INCLUSION_CRITERION_SUMMARY_T Type

Summary of the inclusion criterion.

Syntax
```

```

Fields

Field Description

`id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the inclusion criterion.

`governance_rule_id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the governance rule. Every inclusion criterion is associated with a governance rule.

`l_type`

(required) Type of inclusion criterion - TENANCY, ALL or TAG. We support TENANCY and ALL for now.

`association`

(optional)

`lifecycle_state`

(required) The current state of the inclusion criterion.

`time_created`

(required) Date and time the inclusion criterion was created. An RFC3339 formatted datetime string. Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(required) Date and time the inclusion criterion was updated. An RFC3339 formatted datetime string. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_INCLUSION_CRITERION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_governance_rules_control_plane_inclusion_criterion_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_INCLUSION_CRITERION_COLLECTION_T Type

Results of a inclusion criterion search. Contains inclusion criterion summary items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of inclusionCriteria.

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_QUOTA_TEMPLATE_T Type

Quota template for governance rule.

Syntax
```

```

`dbms_cloud_oci_governance_rules_control_plane_quota_template_t`is a subtype of the`dbms_cloud_oci_governance_rules_control_plane_template_t`type.

Fields

Field Description

`display_name`

(required) Display name of the quota resource.

`description`

(optional) Description of the quota resource.

`statements`

(required) List of quota statements.

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_TAG_T Type

Details of the tag that is being created.

Syntax
```

```

Fields

Field Description

`name`

(required) The name you assign to the tag during creation. This is the tag key definition. The name must be unique within the tag namespace and cannot be changed.

`description`

(optional) The description assigned to the tag during creation.

`is_cost_tracking`

(optional) Indicates whether the tag is enabled for cost tracking.

`validator`

(optional)

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_TAG_DEFAULT_T Type

Tag defaults let you specify a default tag (tagnamespace.tag=\"value\") to apply to all resource types in a specified compartment. The tag default is applied at the time the resource is created. Resources that exist in the compartment before you create the tag default are not tagged.

Syntax
```

```

Fields

Field Description

`tag_name`

(required) The name of the tag. The tag default will always assign a default value for this tag name.

`value`

(required) The default value for the tag name. This will be applied to all new resources created in the compartment.

`is_required`

(required) If you specify that a value is required, a value is set during resource creation (either by the user creating the resource or another tag default). If no value is set, resource creation is blocked. * If the `isRequired` flag is set to \"true\", the value is set during resource creation. * If the `isRequired` flag is set to \"false\", the value you enter is set during resource creation. Example: `false`

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_TAG_TBL Type

Nested table type of dbms_cloud_oci_governance_rules_control_plane_tag_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_TAG_DEFAULT_TBL Type

Nested table type of dbms_cloud_oci_governance_rules_control_plane_tag_default_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_TAG_TEMPLATE_T Type

Template for governance rules of type tag.

Syntax
```

```

`dbms_cloud_oci_governance_rules_control_plane_tag_template_t`is a subtype of the`dbms_cloud_oci_governance_rules_control_plane_template_t`type.

Fields

Field Description

`name`

(required) The name of the tag namespace. It must be unique across all tag namespaces in the tenancy and cannot be changed.

`description`

(optional) Description of the tag namespace.

`tags`

(optional) Represents an array of tags for tag namespace.

`tag_defaults`

(optional)

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_TENANCY_ASSOCIATION_T Type

Tenancy association represents the tenancy id to which the governance rule will be applied.

Syntax
```

```

`dbms_cloud_oci_governance_rules_control_plane_tenancy_association_t`is a subtype of the`dbms_cloud_oci_governance_rules_control_plane_association_t`type.

Fields

Field Description

`tenancy_id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the tenancy to which the governance rule will be applied as part of this tenancy inclusion criterion.

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_TENANCY_ATTACHMENT_T Type

Tenancy attachment associates a tenancy to a governance rule via an inclusion criterion.

Syntax
```

```

Fields

Field Description

`id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the tenancy attachment.

`compartment_id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the root compartment containing the tenancy attachment.

`governance_rule_id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the governance rule. Every tenancy attachment is associated with a governance rule.

`tenancy_id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the tenancy to which the governance rule is attached.

`lifecycle_state`

(required) The current state of the tenancy attachment.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'NEEDS_ATTENTION', 'DELETING', 'DELETED'

`time_created`

(required) Date and time the tenancy attachment was created. An RFC3339 formatted datetime string. Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(required) Date and time the tenancy attachment was updated. An RFC3339 formatted datetime string. Example: `2016-08-25T21:10:29.600Z`

`time_last_attempted`

(optional) Date and time the tenancy attachment was last attempted. An RFC3339 formatted datetime string. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_TENANCY_ATTACHMENT_SUMMARY_T Type

Summary of the tenancy attachment.

Syntax
```

```

Fields

Field Description

`id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the tenancy attachment.

`compartment_id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the root compartment containing the tenancy attachment.

`governance_rule_id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the governance rule. Every tenancy attachment is associated with a governance rule.

`tenancy_id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the tenancy to which the governance rule is attached.

`lifecycle_state`

(required) The current state of the tenancy attachment.

`time_created`

(required) Date and time the tenancy attachment was created. An RFC3339 formatted datetime string. Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(required) Date and time the tenancy attachment was updated. An RFC3339 formatted datetime string. Example: `2016-08-25T21:10:29.600Z`

`time_last_attempted`

(optional) Date and time the tenancy attachment was last attempted. An RFC3339 formatted datetime string. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_TENANCY_ATTACHMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_governance_rules_control_plane_tenancy_attachment_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_TENANCY_ATTACHMENT_COLLECTION_T Type

Results of a tenancy attachment search. Contains tenancy attachment summary items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of tenancy attachments.

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_UPDATE_GOVERNANCE_RULE_DETAILS_T Type

Request object for UpdateGovernanceRule operation.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Display name of the governance rule.

`description`

(optional) Description of the governance rule.

`template`

(optional)

`related_resource_id`

(optional) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the resource, which was used as a template to create this governance rule.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_WORK_REQUEST_RESOURCE_T Type

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

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_governance_rules_control_plane_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_WORK_REQUEST_T Type

A description of workrequest status

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_GOVERNANCE_RULE', 'UPDATE_GOVERNANCE_RULE', 'DELETE_GOVERNANCE_RULE', 'RETRY_GOVERNANCE_RULE', 'CREATE_INCLUSION_CRITERIA', 'DELETE_INCLUSION_CRITERIA', 'RETRY_TENANCY_ATTACHMENT', 'APPLY_TENANCY_ATTACHMENT', 'CREATE_ENFORCED_QUOTA_GOVERNANCE_RULE', 'CREATE_ENFORCED_TAG_GOVERNANCE_RULE', 'UPDATE_ENFORCED_QUOTA_GOVERNANCE_RULE', 'UPDATE_ENFORCED_TAG_GOVERNANCE_RULE', 'DELETE_ENFORCED_QUOTA_GOVERNANCE_RULE', 'DELETE_ENFORCED_TAG_GOVERNANCE_RULE', 'TENANT_MANAGER_OPT_IN_EVENT_HANDLER', 'TENANT_MANAGER_OPT_OUT_EVENT_HANDLER'

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

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_WORK_REQUEST_ERROR_T Type

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

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_governance_rules_control_plane_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestError objects.

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_WORK_REQUEST_LOG_ENTRY_T Type

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

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_governance_rules_control_plane_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a workRequestLog search. Contains both workRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestLogEntries.

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_GOVERNANCE_RULE', 'UPDATE_GOVERNANCE_RULE', 'DELETE_GOVERNANCE_RULE', 'RETRY_GOVERNANCE_RULE', 'CREATE_INCLUSION_CRITERIA', 'DELETE_INCLUSION_CRITERIA', 'RETRY_TENANCY_ATTACHMENT', 'APPLY_TENANCY_ATTACHMENT', 'CREATE_ENFORCED_QUOTA_GOVERNANCE_RULE', 'CREATE_ENFORCED_TAG_GOVERNANCE_RULE', 'UPDATE_ENFORCED_QUOTA_GOVERNANCE_RULE', 'UPDATE_ENFORCED_TAG_GOVERNANCE_RULE', 'DELETE_ENFORCED_QUOTA_GOVERNANCE_RULE', 'DELETE_ENFORCED_TAG_GOVERNANCE_RULE', 'TENANT_MANAGER_OPT_IN_EVENT_HANDLER', 'TENANT_MANAGER_OPT_OUT_EVENT_HANDLER'

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

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_governance_rules_control_plane_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestSummary objects.

- [Governance Rules CP Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-CD643A86-4ADB-43FD-9715-C0C7EF258218)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-BE3D235C-585D-464C-925F-630A3FF82420)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_TEMPLATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-4DC03993-1105-455B-BA00-6F5AA0F0BEF9)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_ALLOWED_REGIONS_TEMPLATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-F00D331D-F0E0-41B8-A188-DA5FECBE25DD)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_ASSOCIATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-B551120A-C760-44A4-BC6B-203C8ECA7701)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_BASE_TAG_DEFINITION_VALIDATOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-751C2B82-0A9C-4419-83A6-FA945174191F)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_CREATE_GOVERNANCE_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-9AA501BC-1679-4507-83B7-DC79BA13A257)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_CREATE_INCLUSION_CRITERION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-7808948D-ED49-4E05-859D-99E492BBADCB)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_DEFAULT_TAG_DEFINITION_VALIDATOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-0525AB9C-B8C6-4D71-B1FE-B4E08FD9D69D)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_ENFORCED_GOVERNANCE_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-2F2DD3DF-CB68-49FD-925C-1FF244741983)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_ENFORCED_GOVERNANCE_RULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-A81B9C14-3196-4014-AF1E-D8F5C97000ED)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_ENFORCED_GOVERNANCE_RULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-02433891-FF09-406C-8C06-C3921D53EE22)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_ENFORCED_GOVERNANCE_RULE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-E992109D-C029-411F-96F4-12FE6DF6EABD)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_ENUM_TAG_DEFINITION_VALIDATOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-811C673B-5332-4F52-AFDE-66299B625E29)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-1BCB4D0D-B2CF-45C9-BF28-E5154D67FFC5)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_GOVERNANCE_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-457DE28C-625B-4B45-B1A8-CD8732039E5D)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_GOVERNANCE_RULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-D10A2D9D-D809-4866-91B0-A947430EC746)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_GOVERNANCE_RULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-1AD3FF45-79B5-4607-9F03-39318621DCBE)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_GOVERNANCE_RULE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-75FC3FB9-3938-49E8-B16E-3E71EC2EEBC5)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_INCLUSION_CRITERION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-4D1A38A4-A64C-40E3-8CD7-06AC33FFD97E)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_INCLUSION_CRITERION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-B9755040-C501-409D-8B41-026DF658C4ED)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_INCLUSION_CRITERION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-88BC8A2B-4886-476E-BDDA-FEA7A5169B88)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_INCLUSION_CRITERION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-01E3A88C-BFAE-47B8-B194-027D65117E64)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_QUOTA_TEMPLATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-5FF0433A-D606-44E5-91A1-A9F44B6A68E3)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_TAG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-B789ECB1-4B17-485F-8CB5-FEF1FBA4AC91)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_TAG_DEFAULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-2D17013A-97C0-4509-B8BA-755AE408C57F)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_TAG_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-A0BC1B21-C111-485E-AB9B-63295595ED0B)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_TAG_DEFAULT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-C0DAD72C-624A-48D3-9FC1-9BF4FA0A9984)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_TAG_TEMPLATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-2B2B1362-8D4E-4DB2-9C69-DE807EA85A1D)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_TENANCY_ASSOCIATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-3E051556-4B2D-44EC-9680-D653B31AAF86)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_TENANCY_ATTACHMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-AF8F7E0F-B3FA-4581-8A10-CF0817652CFD)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_TENANCY_ATTACHMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-C39CDA6E-0CCE-4578-A626-D11DC1F33473)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_TENANCY_ATTACHMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-EE6718A6-5CA0-493A-9702-2F090FF040F7)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_TENANCY_ATTACHMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-60DECCE4-67FF-4A20-B84B-20507F6F0D6E)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_UPDATE_GOVERNANCE_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-EE4381A8-AB14-4671-A131-D44B32C2A00F)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-F983B15B-D10A-40A4-AC23-86A10166DDA3)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-DD24EF57-4846-4CE3-8900-33518D8625A3)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-DDD3999E-494E-4C18-AD6A-4C8CB0348325)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-02C9F6A3-D1FD-4BC9-90DE-118162E35EDB)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-E0BFFEF3-4D29-4FBD-953F-3CB38492F210)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-629022F8-3624-448B-B075-6F1385922B3D)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-34E53DB2-3E7A-498E-8573-D8A0A0A7E4BD)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-96A19364-0B81-4C30-A0F1-A81DF6F81CD0)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-6A52A310-3D21-4792-9810-1BF345693C98)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-ADA3EB51-2F13-40F4-8AEC-276D5EC0B190)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-5A63E1F8-BE41-43C2-905A-AD2C88855450)
- [DBMS_CLOUD_OCI_GOVERNANCE_RULES_CONTROL_PLANE_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/governance_rules_control_plane_t.html#ADSDK-GUID-BC42DD5D-08D7-418C-9483-8FD636575EFB)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
