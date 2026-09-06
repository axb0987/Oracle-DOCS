# Budget Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/budget_t.html
- Fetched: 2026-09-05 19:01 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/budget_t.html#dcoc-content-body)

## Budget Common Types

### DBMS_CLOUD_OCI_BUDGET_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_BUDGET_ALERT_RULE_T Type

The alert rule.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the alert rule.

`budget_id`

(required) The OCID of the budget.

`display_name`

(required) The name of the alert rule. Avoid entering confidential information.

`l_type`

(required) The type of the alert. Valid values are ACTUAL (the alert triggers based on actual usage), or FORECAST (the alert triggers based on predicted usage).

Allowed values are: 'ACTUAL', 'FORECAST'

`threshold`

(required) The threshold for triggering the alert. If the thresholdType is PERCENTAGE, the maximum value is 10000.

`threshold_type`

(required) The type of threshold.

Allowed values are: 'PERCENTAGE', 'ABSOLUTE'

`lifecycle_state`

(required) The current state of the alert rule.

Allowed values are: 'ACTIVE', 'INACTIVE'

`message`

(optional) Custom message sent when an alert is triggered.

`description`

(optional) The description of the alert rule.

`version`

(optional) The version of the alert rule. Starts from 1 and increments by 1.

`recipients`

(required) The delimited list of email addresses to receive the alert when it triggers. Delimiter characters can be a comma, space, TAB, or semicolon.

`time_created`

(required) The time the budget was created.

`time_updated`

(required) The time the budget was updated.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_BUDGET_ALERT_RULE_SUMMARY_T Type

The alert rule.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the alert rule.

`budget_id`

(required) The OCID of the budget.

`display_name`

(required) The name of the alert rule. Avoid entering confidential information.

`l_type`

(required) ACTUAL means the alert triggers based on actual usage. FORECAST means the alert triggers based on predicted usage.

Allowed values are: 'ACTUAL', 'FORECAST'

`threshold`

(required) The threshold for triggering the alert. If the thresholdType is PERCENTAGE, the maximum value is 10000.

`threshold_type`

(required) The type of threshold.

Allowed values are: 'PERCENTAGE', 'ABSOLUTE'

`lifecycle_state`

(required) The current state of the alert rule.

Allowed values are: 'ACTIVE', 'INACTIVE'

`message`

(optional) The custom message that will be sent when the alert is triggered.

`description`

(optional) The description of the alert rule.

`version`

(optional) The version of the alert rule. Starts from 1 and increments by 1.

`recipients`

(required) The audience that receives the alert when it triggers.

`time_created`

(required) The time when the budget was created.

`time_updated`

(required) The time when the budget was updated.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_BUDGET_BUDGET_T Type

A budget.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the budget.

`compartment_id`

(required) The OCID of the compartment.

`target_compartment_id`

(optional) This is DEPRECATED. For backwards compatability, the property is populated when the targetType is \"COMPARTMENT\", and targets contain the specific target compartment OCID. For all other scenarios, this property will be left empty.

`display_name`

(required) The display name of the budget. Avoid entering confidential information.

`description`

(optional) The description of the budget.

`amount`

(required) The amount of the budget expressed in the currency of the customer's rate card.

`reset_period`

(required) The reset period for the budget.

Allowed values are: 'MONTHLY'

`budget_processing_period_start_offset`

(optional) The number of days offset from the first day of the month, at which the budget processing period starts. In months that have fewer days than this value, processing will begin on the last day of that month. For example, for a value of 12, processing starts every month on the 12th at midnight.

`processing_period_type`

(optional) The budget processing period type. Valid values are INVOICE, MONTH, and SINGLE_USE.

Allowed values are: 'INVOICE', 'MONTH', 'SINGLE_USE'

`start_date`

(optional) The date when the one-time budget begins. For example, `2023-03-23`. The date-time format conforms to RFC 3339, and will be truncated to the starting point of the date provided after being converted to UTC time.

`end_date`

(optional) The time when the one-time budget concludes. For example, `2023-03-23`. The date-time format conforms to RFC 3339, and will be truncated to the starting point of the date provided after being converted to UTC time.

`target_type`

(optional) The type of target on which the budget is applied.

Allowed values are: 'COMPARTMENT', 'TAG'

`targets`

(optional) The list of targets on which the budget is applied. If the targetType is \"COMPARTMENT\", the targets contain the list of compartment OCIDs. If the targetType is \"TAG\", the targets contain the list of cost tracking tag identifiers in the form of \"{tagNamespace}.{tagKey}.{tagValue}\".

`lifecycle_state`

(required) The current state of the budget.

Allowed values are: 'ACTIVE', 'INACTIVE'

`alert_rule_count`

(required) The total number of alert rules in the budget.

`version`

(optional) The version of the budget. Starts from 1 and increments by 1.

`actual_spend`

(optional) The actual spend in currency for the current budget cycle.

`forecasted_spend`

(optional) The forecasted spend in currency by the end of the current budget cycle.

`time_spend_computed`

(optional) The time that the budget spend was last computed.

`time_created`

(required) The time that the budget was created.

`time_updated`

(required) The time that the budget was updated.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_BUDGET_BUDGET_SUMMARY_T Type

A budget.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the budget.

`compartment_id`

(required) The OCID of the compartment.

`target_compartment_id`

(optional) This is DEPRECATED. For backwards compatability, the property is populated when the targetType is \"COMPARTMENT\", and the targets contain the specific target compartment OCID. For all other scenarios, this property is left empty.

`display_name`

(required) The display name of the budget. Avoid entering confidential information.

`description`

(optional) The description of the budget.

`amount`

(required) The amount of the budget, expressed in the currency of the customer's rate card.

`reset_period`

(required) The reset period for the budget.

Allowed values are: 'MONTHLY'

`budget_processing_period_start_offset`

(optional) The number of days offset from the first day of the month, at which the budget processing period starts. In months that have fewer days than this value, processing will begin on the last day of that month. For example, for a value of 12, processing starts every month on the 12th at midnight.

`processing_period_type`

(optional) The type of the budget processing period. Valid values are INVOICE, MONTH, and SINGLE_USE.

Allowed values are: 'INVOICE', 'MONTH', 'SINGLE_USE'

`start_date`

(optional) The date when the one-time budget begins. For example, `2023-03-23`. The date-time format conforms to RFC 3339, and will be truncated to the starting point of the date provided after being converted to UTC time.

`end_date`

(optional) The time when the one-time budget concludes. For example, - `2023-03-23`. The date-time format conforms to RFC 3339, and will be truncated to the starting point of the date provided after being converted to UTC time.

`target_type`

(optional) The type of target on which the budget is applied.

Allowed values are: 'COMPARTMENT', 'TAG'

`targets`

(optional) The list of targets on which the budget is applied. If the targetType is \"COMPARTMENT\", the targets contain the list of compartment OCIDs. If the targetType is \"TAG\", the targets contain the list of cost tracking tag identifiers in the form of \"{tagNamespace}.{tagKey}.{tagValue}\".

`lifecycle_state`

(required) The current state of the budget.

Allowed values are: 'ACTIVE', 'INACTIVE'

`alert_rule_count`

(required) The total number of alert rules in the budget.

`version`

(optional) The version of the budget. Starts from 1 and increments by 1.

`actual_spend`

(optional) The actual spend in currency for the current budget cycle.

`forecasted_spend`

(optional) The forecasted spend in currency by the end of the current budget cycle.

`time_spend_computed`

(optional) The time the budget spend was last computed.

`time_created`

(required) The time the budget was created.

`time_updated`

(required) The time the budget was updated.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_BUDGET_CREATE_ALERT_RULE_DETAILS_T Type

The create alert rule details. This is a batch-create.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The name of the alert rule. Avoid entering confidential information.

`description`

(optional) The description of the alert rule.

`l_type`

(required) The type of the alert. Valid values are ACTUAL (the alert triggers based on actual usage), or FORECAST (the alert triggers based on predicted usage).

Allowed values are: 'ACTUAL', 'FORECAST'

`threshold`

(required) The threshold for triggering the alert, expressed as a whole number or decimal value. If the thresholdType is ABSOLUTE, the threshold can have at most 12 digits before the decimal point, and up to two digits after the decimal point. If the thresholdType is PERCENTAGE, the maximum value is 10000 and can have up to two digits after the decimal point.

`threshold_type`

(required) The type of threshold.

Allowed values are: 'PERCENTAGE', 'ABSOLUTE'

`recipients`

(optional) The audience that receives the alert when it triggers. An empty string is interpreted as null.

`message`

(optional) The message to be sent to the recipients when the alert rule is triggered.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_BUDGET_CREATE_BUDGET_DETAILS_T Type

The create budget details. Clients should use 'targetType' and 'targets' to specify the target type and list of targets on which the budget is applied. For backwards compatibility, 'targetCompartmentId' is still supported for all existing clients. This is considered deprecated, however, and all clients are upgraded to use 'targetType' and 'targets'. Specifying both 'targetCompartmentId' and 'targets' causes a Bad Request.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment.

`target_compartment_id`

(optional) This is DEPRECATED. Set the target compartment ID in targets instead.

`display_name`

(optional) The displayName of the budget. Avoid entering confidential information.

`description`

(optional) The description of the budget.

`amount`

(required) The amount of the budget expressed as a whole number in the currency of the customer's rate card.

`reset_period`

(required) The reset period for the budget.

Allowed values are: 'MONTHLY'

`budget_processing_period_start_offset`

(optional) The number of days offset from the first day of the month, at which the budget processing period starts. In months that have fewer days than this value, processing will begin on the last day of that month. For example, for a value of 12, processing starts every month on the 12th at midnight.

`processing_period_type`

(optional) The type of the budget processing period. Valid values are INVOICE, MONTH, and SINGLE_USE.

Allowed values are: 'INVOICE', 'MONTH', 'SINGLE_USE'

`start_date`

(optional) The date when the one-time budget begins. For example, `2023-03-23`. The date-time format conforms to RFC 3339, and will be truncated to the starting point of the date provided after being converted to UTC time.

`end_date`

(optional) The date when the one-time budget concludes. For example, `2023-03-23`. The date-time format conforms to RFC 3339, and will be truncated to the starting point of the date provided after being converted to UTC time.

`target_type`

(optional) The type of target on which the budget is applied.

Allowed values are: 'COMPARTMENT', 'TAG'

`targets`

(optional) The list of targets on which the budget is applied. If targetType is \"COMPARTMENT\", the targets contain the list of compartment OCIDs. If targetType is \"TAG\", the targets contain the list of cost tracking tag identifiers in the form of \"{tagNamespace}.{tagKey}.{tagValue}\". Curerntly, the array should contain exactly one item.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_BUDGET_ERROR_T Type

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

### DBMS_CLOUD_OCI_BUDGET_UPDATE_ALERT_RULE_DETAILS_T Type

The update alert rule details.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The name of the alert rule. Avoid entering confidential information.

`l_type`

(optional) The type of the alert. Valid values are ACTUAL (the alert triggers based on actual usage), or FORECAST (the alert triggers based on predicted usage).

Allowed values are: 'ACTUAL', 'FORECAST'

`threshold`

(optional) The threshold for triggering the alert, expressed as a whole number or decimal value. If the thresholdType is ABSOLUTE, the threshold can have at most 12 digits before the decimal point, and up to two digits after the decimal point. If the thresholdType is PERCENTAGE, the maximum value is 10000 and can have up to two digits after the decimal point.

`threshold_type`

(optional) The type of threshold.

Allowed values are: 'PERCENTAGE', 'ABSOLUTE'

`recipients`

(optional) The audience that receives the alert when it triggers. If you need to clear out this value, pass in an empty string instead of a null value.

`description`

(optional) The description of the alert rule.

`message`

(optional) The message to be delivered to the recipients when an alert is triggered.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_BUDGET_UPDATE_BUDGET_DETAILS_T Type

The update budget details.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The displayName of the budget. Avoid entering confidential information.

`description`

(optional) The description of the budget.

`amount`

(optional) The amount of the budget expressed as a whole number in the currency of the customer's rate card.

`budget_processing_period_start_offset`

(optional) The number of days offset from the first day of the month, at which the budget processing period starts. In months that have fewer days than this value, processing will begin on the last day of that month. For example, for a value of 12, processing starts every month on the 12th at midnight.

`processing_period_type`

(optional) The type of the budget processing period. Valid values are INVOICE, MONTH, and SINGLE_USE.

Allowed values are: 'INVOICE', 'MONTH', 'SINGLE_USE'

`start_date`

(optional) The date when the one-time budget begins. For example, `2023-03-23`. The date-time format conforms to RFC 3339, and will be truncated to the starting point of the date provided after being converted to UTC time.

`end_date`

(optional) The time when the one-time budget concludes. For example, `2023-03-23`. The date-time format conforms to RFC 3339, and will be truncated to the starting point of the date provided after being converted to UTC time.

`reset_period`

(optional) The reset period for the budget.

Allowed values are: 'MONTHLY'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

- [Budget Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/budget_t.html#ADSDK-GUID-71E2BBEC-906A-4EC5-9D0F-7F07704A9351)
- [DBMS_CLOUD_OCI_BUDGET_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/budget_t.html#ADSDK-GUID-1DA84D29-48AB-4059-B8B8-E0589335552C)
- [DBMS_CLOUD_OCI_BUDGET_ALERT_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/budget_t.html#ADSDK-GUID-61BD6A27-7B33-47A3-852C-D84C11890B65)
- [DBMS_CLOUD_OCI_BUDGET_ALERT_RULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/budget_t.html#ADSDK-GUID-CB38B529-3ABE-49EC-89AB-136720257BD1)
- [DBMS_CLOUD_OCI_BUDGET_BUDGET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/budget_t.html#ADSDK-GUID-5C4F56EE-4FA6-4F8A-9075-DA013841B301)
- [DBMS_CLOUD_OCI_BUDGET_BUDGET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/budget_t.html#ADSDK-GUID-275C2984-EF50-4A7E-AC65-77F18706059E)
- [DBMS_CLOUD_OCI_BUDGET_CREATE_ALERT_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/budget_t.html#ADSDK-GUID-0FE1C87A-247B-4EAB-AB18-D8A9CA5C242C)
- [DBMS_CLOUD_OCI_BUDGET_CREATE_BUDGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/budget_t.html#ADSDK-GUID-AB04E998-1F41-46FF-B33B-C6E6EBB3C735)
- [DBMS_CLOUD_OCI_BUDGET_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/budget_t.html#ADSDK-GUID-3873A75D-0C2E-455B-8D27-ED3606DD0F2B)
- [DBMS_CLOUD_OCI_BUDGET_UPDATE_ALERT_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/budget_t.html#ADSDK-GUID-FD30B568-982C-4D56-9BFD-75F42A16F40C)
- [DBMS_CLOUD_OCI_BUDGET_UPDATE_BUDGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/budget_t.html#ADSDK-GUID-1D73BE69-D5C3-4197-8745-C5103DC19155)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
