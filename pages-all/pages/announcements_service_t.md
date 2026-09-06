# Announcements Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html
- Fetched: 2026-09-05 19:00 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#dcoc-content-body)

## Announcements Common Types

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_PROPERTY_T Type

A generic property that might be associated with the affected resource.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the property.

`value`

(required) The value of the property.

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_PROPERTY_TBL Type

Nested table type of dbms_cloud_oci_announcements_service_property_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_AFFECTED_RESOURCE_T Type

The resource affected by the event described in the announcement.

Syntax
```

```

Fields

Field Description

`resource_id`

(required) The OCID of the affected resource.

`resource_name`

(required) The friendly name of the resource.

`l_region`

(required) The region where the affected resource exists.

`additional_properties`

(optional) Additional properties associated with the resource.

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_BASE_ANNOUNCEMENT_T Type

Incident information that forms the basis of an announcement. Avoid entering confidential information.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the announcement.

`l_type`

(required) The entity type, which is either an announcement or the summary representation of an announcement.

`reference_ticket_number`

(required) The reference Jira ticket number.

`summary`

(required) A summary of the issue. A summary might appear in the console banner view of the announcement or in an email subject line. Avoid entering confidential information.

`time_one_title`

(optional) The label associated with an initial time value. Example: `Time Started`

`time_one_type`

(optional) The type of a time associated with an initial time value. If the `timeOneTitle` attribute is present, then the `timeOneTitle` attribute contains a label of `timeOneType` in English. Example: `START_TIME`

Allowed values are: 'ACTION_REQUIRED_BY', 'NEW_START_TIME', 'ORIGINAL_END_TIME', 'REPORT_DATE', 'START_TIME', 'TIME_DETECTED'

`time_one_value`

(optional) The actual value of the first time value for the event. Typically, this denotes the time an event started, but the meaning can vary, depending on the announcement type. The `timeOneType` attribute describes the meaning.

`time_two_title`

(optional) The label associated with a second time value. Example: `Time Ended`

`time_two_type`

(optional) The type of a time associated with second time value. If the `timeTwoTitle` attribute is present, then the `timeTwoTitle` attribute contains a label of `timeTwoType` in English. Example: `END_TIME`

Allowed values are: 'END_TIME', 'NEW_END_TIME', 'ESTIMATED_END_TIME'

`time_two_value`

(optional) The actual value of the second time value. Typically, this denotes the time an event ended, but the meaning can vary, depending on the announcement type. The `timeTwoType` attribute describes the meaning.

`services`

(required) Impacted Oracle Cloud Infrastructure services.

`affected_regions`

(required) Impacted regions.

`announcement_type`

(required) The type of announcement. An announcement's type signals its severity.

Allowed values are: 'ACTION_RECOMMENDED', 'ACTION_REQUIRED', 'EMERGENCY_CHANGE', 'EMERGENCY_MAINTENANCE', 'EMERGENCY_MAINTENANCE_COMPLETE', 'EMERGENCY_MAINTENANCE_EXTENDED', 'EMERGENCY_MAINTENANCE_RESCHEDULED', 'INFORMATION', 'PLANNED_CHANGE', 'PLANNED_CHANGE_COMPLETE', 'PLANNED_CHANGE_EXTENDED', 'PLANNED_CHANGE_RESCHEDULED', 'PRODUCTION_EVENT_NOTIFICATION', 'SCHEDULED_MAINTENANCE'

`lifecycle_state`

(required) The current lifecycle state of the announcement.

Allowed values are: 'ACTIVE', 'INACTIVE'

`is_banner`

(required) Whether the announcement is displayed as a banner in the console.

`time_created`

(optional) The date and time the announcement was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-01-01T17:43:01.389+0000`

`time_updated`

(optional) The date and time the announcement was last updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-01-01T17:43:01.389+0000`

`environment_name`

(optional) The name of the environment that this announcement pertains to.

`platform_type`

(optional) The platform type that this announcement pertains to.

Allowed values are: 'IAAS', 'SAAS'

`chain_id`

(optional) The sequence of connected announcements, or announcement chain, that this announcement belongs to. Related announcements share the same chain ID.

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_AFFECTED_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_announcements_service_affected_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ANNOUNCEMENT_T Type

A message about an impactful operational event.

Syntax
```

```

`dbms_cloud_oci_announcements_service_announcement_t`is a subtype of the`dbms_cloud_oci_announcements_service_base_announcement_t`type.

Fields

Field Description

`description`

(optional) A detailed explanation of the event, expressed by using Markdown language. Avoid entering confidential information.

`additional_information`

(optional) Additional information about the event, expressed by using Markdown language and included in the details view of an announcement. Additional information might include remediation steps or answers to frequently asked questions. Avoid entering confidential information.

`affected_resources`

(optional) The list of resources, if any, affected by the event described in the announcement.

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_FILTER_T Type

Criteria that the Announcements service uses to match announcements so it can provide only desired announcements to subscribers.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of filter. You cannot combine the RESOURCE_ID filter with any other type of filter within a given filter group. For filter types that support multiple values, specify the values individually.

Allowed values are: 'COMPARTMENT_ID', 'PLATFORM_TYPE', 'REGION', 'SERVICE', 'RESOURCE_ID', 'ANNOUNCEMENT_TYPE'

`value`

(required) The value of the filter.

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_FILTER_TBL Type

Nested table type of dbms_cloud_oci_announcements_service_filter_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_FILTER_GROUP_T Type

A group of filters to match announcements against.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the group. The name must be unique and it cannot be changed. Avoid entering confidential information.

`filters`

(required) A list of filters against which the Announcements service matches announcements. You cannot combine the RESOURCE_ID filter with any other type of filter within a given filter group. For filter types that support multiple values, specify the values individually.

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ANNOUNCEMENT_SUBSCRIPTION_T Type

A subscription with the Announcements service to receive selected announcements in the format and delivery mechanisms supported by a corresponding topic endpoint configured in the Oracle Cloud Infrastructure Notifications service.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the announcement subscription.

`display_name`

(required) A user-friendly name for the announcement subscription. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) A description of the announcement subscription. Avoid entering confidential information.

`compartment_id`

(required) The OCID of the compartment that contains the announcement subscription.

`time_created`

(required) The date and time that the announcement subscription was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.

`time_updated`

(optional) The date and time that the announcement subscription was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.

`lifecycle_state`

(required) The current lifecycle state of the announcement subscription.

Allowed values are: 'ACTIVE', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current lifecycle state in more detail. For example, details might provide required or recommended actions for a resource in a Failed state.

`ons_topic_id`

(required) The OCID of the Notifications service topic that is the target for publishing announcements that match the configured announcement subscription.

`filter_groups`

(optional) A list of filter groups for the announcement subscription. A filter group is a combination of multiple filters applied to announcements for matching purposes.

`preferred_language`

(optional) (For announcement subscriptions with SaaS configured as the platform type or Oracle Fusion Applications as the service, or both, only) The language in which the user prefers to receive emailed announcements. Specify the preference with a value that uses the x-obmcs-human-language format. For example fr-FR.

`preferred_time_zone`

(optional) The time zone in which the user prefers to receive announcements. Specify the preference with a value that uses the IANA Time Zone Database format (x-obmcs-time-zone). For example - America/Los_Angeles

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ANNOUNCEMENT_SUBSCRIPTION_SUMMARY_T Type

A summary representation of an announcement subscription.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the announcement subscription.

`display_name`

(required) A user-friendly name for the announcement subscription. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(required) The OCID of the compartment that contains the announcement subscription.

`time_created`

(required) The date and time that the announcement subscription was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.

`time_updated`

(optional) The date and time that the announcement subscription was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.

`lifecycle_state`

(required) The current lifecycle state of the announcement subscription.

`lifecycle_details`

(optional) A message describing the current lifecycle state in more detail. For example, details might provide required or recommended actions for a resource in a Failed state.

`ons_topic_id`

(required) The OCID of the Notifications service topic that is the target for publishing announcements that match the configured announcement subscription.

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ANNOUNCEMENT_SUBSCRIPTION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_announcements_service_announcement_subscription_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ANNOUNCEMENT_SUBSCRIPTION_COLLECTION_T Type

The results of a search for announcement subscriptions. This object contains both announcement subscription summary objects and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of announcement subscriptions.

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ANNOUNCEMENT_SUMMARY_T Type

A summary representation of an announcement.

Syntax
```

```

`dbms_cloud_oci_announcements_service_announcement_summary_t`is a subtype of the`dbms_cloud_oci_announcements_service_base_announcement_t`type.

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ANNOUNCEMENT_USER_STATUS_DETAILS_T Type

An announcement's status regarding whether it has been acknowledged by a user.

Syntax
```

```

Fields

Field Description

`user_status_announcement_id`

(required) The OCID of the announcement that this status is associated with.

`user_id`

(required) The OCID of the user that this status is associated with.

`time_acknowledged`

(optional) The date and time the announcement was acknowledged, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-01-01T17:43:01.389+0000`

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ANNOUNCEMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_announcements_service_announcement_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ANNOUNCEMENT_USER_STATUS_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_announcements_service_announcement_user_status_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ANNOUNCEMENTS_COLLECTION_T Type

A list of announcements that match filter criteria, if any. Results contain both the announcements and the user-specific status of the announcements.

Syntax
```

```

Fields

Field Description

`items`

(optional) A collection of announcements.

`user_statuses`

(optional) The user-specific status for found announcements.

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_BASE_ANNOUNCEMENTS_PREFERENCES_T Type

The object that contains the announcement email preferences configured for the tenancy (root compartment).

Syntax
```

```

Fields

Field Description

`l_type`

(required) The entity type, which specifies either an object or a summary object for announcement email preferences.

`compartment_id`

(optional) The OCID of the compartment for which the email preferences apply. Because announcements are specific to a tenancy, specify the tenancy by providing the root compartment OCID.

`id`

(optional) The ID of the preferences.

`is_unsubscribed`

(optional) A Boolean value to indicate whether the specified compartment chooses to not to receive informational announcements by email. (Manage preferences for receiving announcements by email by specifying the `preferenceType` attribute instead.)

`time_created`

(optional) When the preferences were set initially.

`time_updated`

(optional) When the preferences were last updated.

`preference_type`

(optional) The string representing the user's preference regarding receiving announcements by email.

`preferred_time_zone`

(optional) The time zone in which the user prefers to receive announcements. Specify the preference with a value that uses the IANA Time Zone Database format (x-obmcs-time-zone). For example - America/Los_Angeles

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ANNOUNCEMENTS_PREFERENCES_T Type

The object for announcement email preferences.

Syntax
```

```

`dbms_cloud_oci_announcements_service_announcements_preferences_t`is a subtype of the`dbms_cloud_oci_announcements_service_base_announcements_preferences_t`type.

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ANNOUNCEMENTS_PREFERENCES_SUMMARY_T Type

The summary object for announcement email preferences.

Syntax
```

```

`dbms_cloud_oci_announcements_service_announcements_preferences_summary_t`is a subtype of the`dbms_cloud_oci_announcements_service_base_announcements_preferences_t`type.

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_BASE_CREATE_ANNOUNCEMENTS_PREFERENCES_DETAILS_T Type

The model for the parameters of announcement email preferences configured for the tenancy (root compartment).

Syntax
```

```

Fields

Field Description

`l_type`

(required) The entity type, which specifies a model that either creates new announcement email preferences or updates existing preferences.

`is_unsubscribed`

(optional) A Boolean value to indicate whether the specified compartment chooses to not to receive informational announcements by email. (Manage preferences for receiving announcements by email by specifying the `preferenceType` attribute instead.)

`compartment_id`

(optional) The OCID of the compartment for which you want to manage announcement email preferences. (Specify the tenancy by providing the root compartment OCID.)

`preference_type`

(required) The string representing the user's preference, whether to opt in to only required announcements, to opt in to all announcements, including informational announcements, or to opt out of all announcements.

Allowed values are: 'OPT_IN_TENANT_ANNOUNCEMENTS', 'OPT_IN_TENANT_AND_INFORMATIONAL_ANNOUNCEMENTS', 'OPT_OUT_ALL_ANNOUNCEMENTS'

`preferred_time_zone`

(optional) The time zone in which the user prefers to receive announcements. Specify the preference with a value that uses the IANA Time Zone Database format (x-obmcs-time-zone). For example - America/Los_Angeles

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_CHANGE_ANNOUNCEMENT_SUBSCRIPTION_COMPARTMENT_DETAILS_T Type

The details of the request to change the compartment of the announcement subscription.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which you want to move the announcement subscription.

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_FILTER_GROUP_DETAILS_T Type

The details of a group of filters to match announcements against. A filter group combines one or more individual filters.

Syntax
```

```

Fields

Field Description

`filters`

(required) A list of filters against which the Announcements service matches announcements. You cannot combine the RESOURCE_ID filter with any other type of filter within a given filter group. For filter types that support multiple values, specify the values individually.

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_CREATE_ANNOUNCEMENT_SUBSCRIPTION_DETAILS_T Type

The details for creating a new announcement subscription.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly name for the announcement subscription. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) A description of the announcement subscription. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create the announcement subscription.

`ons_topic_id`

(required) The OCID of the Notifications service topic that is the target for publishing announcements that match the configured announcement subscription. The caller of the operation needs the ONS_TOPIC_PUBLISH permission for the targeted Notifications service topic. For more information about Notifications permissions, see[Details for Notifications](https://docs.oracle.com/iaas/Content/Identity/policyreference/notificationpolicyreference.htm).

`filter_groups`

(optional) A list of filter groups for the announcement subscription. A filter group combines one or more filters that the Announcements service applies to announcements for matching purposes.

`preferred_language`

(optional) (For announcement subscriptions with SaaS configured as the platform type or Oracle Fusion Applications as the service, or both, only) The language in which the user prefers to receive emailed announcements. Specify the preference with a value that uses the x-obmcs-human-language format. For example fr-FR.

`preferred_time_zone`

(optional) The time zone in which the user prefers to receive announcements. Specify the preference with a value that uses the IANA Time Zone Database format (x-obmcs-time-zone). For example - America/Los_Angeles

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_CREATE_ANNOUNCEMENTS_PREFERENCES_DETAILS_T Type

The object used to create announcement email preferences.

Syntax
```

```

`dbms_cloud_oci_announcements_service_create_announcements_preferences_details_t`is a subtype of the`dbms_cloud_oci_announcements_service_base_create_announcements_preferences_details_t`type.

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_CREATE_FILTER_GROUP_DETAILS_T Type

The details for creating a new filter group for an announcement subscription.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the filter group. The name must be unique and it cannot be changed. Avoid entering confidential information.

`filters`

(required) A list of filters against which the Announcements service will match announcements. You cannot have more than one of any given filter type within a filter group.

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ERROR_T Type

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

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_UPDATE_ANNOUNCEMENT_SUBSCRIPTION_DETAILS_T Type

The details for updating an announcement subscription.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name for the announcement subscription. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) A description of the announcement subscription. Avoid entering confidential information.

`ons_topic_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Notifications service topic that is the target for publishing announcements that match the configured announcement subscription. The caller of the operation needs the ONS_TOPIC_PUBLISH permission for the targeted Notifications service topic. For more information about Notifications permissions, see[Details for Notifications](https://docs.oracle.com/iaas/Content/Identity/policyreference/notificationpolicyreference.htm).

`preferred_language`

(optional) (For announcement subscriptions with SaaS configured as the platform type or Oracle Fusion Applications as the service, or both, only) The language in which the user prefers to receive emailed announcements. Specify the preference with a value that uses the x-obmcs-human-language format. For example fr-FR.

`preferred_time_zone`

(optional) The time zone in which the user prefers to receive announcements. Specify the preference with a value that uses the IANA Time Zone Database format (x-obmcs-time-zone). For example - America/Los_Angeles

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_UPDATE_ANNOUNCEMENTS_PREFERENCES_DETAILS_T Type

The object used to update announcement email preferences.

Syntax
```

```

`dbms_cloud_oci_announcements_service_update_announcements_preferences_details_t`is a subtype of the`dbms_cloud_oci_announcements_service_base_create_announcements_preferences_details_t`type.

### DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_UPDATE_FILTER_GROUP_DETAILS_T Type

The details for updating a filter group in an announcement subscription.

Syntax
```

```

Fields

Field Description

`filters`

(required) A list of filters against which the Announcements service will match announcements. You cannot combine the RESOURCE_ID filter with any other type of filter within a given filter group. For filter types that support multiple values, specify the values individually.

- [Announcements Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-D601F099-F2BA-4BCC-A91C-9D67DAE64D0C)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-834AE18C-5DCC-4195-BC05-0603445F45A4)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_PROPERTY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-949E12B8-3675-4C6B-80DA-CC14F3AB206A)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_PROPERTY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-BA4C54E9-E1B0-44A6-9D6E-8BAB36AD3775)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_AFFECTED_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-34A44622-DFC7-4998-9EA8-08F55ED4BDA6)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_BASE_ANNOUNCEMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-0DFE6613-5536-412C-92CA-592AE67C3104)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_AFFECTED_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-14AC7115-C5ED-4D43-83DA-E2DC344BC661)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ANNOUNCEMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-315AF4F5-1BE2-4D83-ACA3-77676D2C608D)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-A21706B5-D74A-4460-A51A-BF0C79CEF96C)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_FILTER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-C7EB190C-FC75-4FF5-B45C-2AC23A506F16)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_FILTER_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-66D2EAE5-4F60-40FF-8CF7-B1217D237E34)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ANNOUNCEMENT_SUBSCRIPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-D2C3D1D4-4E28-4F94-9216-08CA9E955FE2)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ANNOUNCEMENT_SUBSCRIPTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-01AAA940-5299-414F-A96B-6C6C55B5525B)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ANNOUNCEMENT_SUBSCRIPTION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-B234B49D-D7A5-4092-9ABF-0D77FB2DFFF5)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ANNOUNCEMENT_SUBSCRIPTION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-29B605F9-7C73-4809-8698-3938D38BC83D)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ANNOUNCEMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-2489A8B7-A56C-4BF3-BB84-281FACF5654D)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ANNOUNCEMENT_USER_STATUS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-01EC0ABF-D1D0-4890-A71B-BF2EE2B4F558)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ANNOUNCEMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-1C245BFF-02E7-4627-BB34-B45D63702361)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ANNOUNCEMENT_USER_STATUS_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-65648F89-CE64-487B-8FDF-D76AB29A3044)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ANNOUNCEMENTS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-D0E92109-C9F2-4B19-AC34-018B4F74D188)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_BASE_ANNOUNCEMENTS_PREFERENCES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-2974C5E5-E20F-43F7-A6C7-18A16D9FDAC0)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ANNOUNCEMENTS_PREFERENCES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-B143848D-64D4-4AE8-A7AF-48384A52098E)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ANNOUNCEMENTS_PREFERENCES_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-0FE72D8A-0B39-4FB4-AB0B-A094BB06428B)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_BASE_CREATE_ANNOUNCEMENTS_PREFERENCES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-B7F94DC1-5D1C-48A0-A565-43277DEE3BAC)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_CHANGE_ANNOUNCEMENT_SUBSCRIPTION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-376CDF82-AC91-4740-B1AE-1558965B4902)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_FILTER_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-5D392458-4A63-4970-AD8C-A39FD86C0BDF)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_CREATE_ANNOUNCEMENT_SUBSCRIPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-00BE817B-2597-46A6-AD8C-A31A139D6DBA)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_CREATE_ANNOUNCEMENTS_PREFERENCES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-45EDD93F-1711-458B-A4B0-4D6C7E50410E)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_CREATE_FILTER_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-7B8F5B91-562D-48C8-AB3A-F26D64CD92A4)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-0A514CBB-660C-4FBB-9166-19351BEE9D21)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_UPDATE_ANNOUNCEMENT_SUBSCRIPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-F56CFE8A-1510-4083-BD0C-071C6229CA1B)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_UPDATE_ANNOUNCEMENTS_PREFERENCES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-B249246C-1D96-4C36-81F6-DEEC7CE187C8)
- [DBMS_CLOUD_OCI_ANNOUNCEMENTS_SERVICE_UPDATE_FILTER_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/announcements_service_t.html#ADSDK-GUID-0300EB83-B9B7-4BA1-BD98-CE3618B5D854)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
