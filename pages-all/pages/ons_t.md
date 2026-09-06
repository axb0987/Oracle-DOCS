# Notifications Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ons_t.html
- Fetched: 2026-09-05 19:18 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ons_t.html#dcoc-content-body)

## Notifications Common Types

### DBMS_CLOUD_OCI_ONS_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_ONS_BACKOFF_RETRY_POLICY_T Type

The backoff retry portion of the subscription delivery policy. For information about retry durations for subscriptions, see[How Notifications Works](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#how).

Syntax
```

```

Fields

Field Description

`max_retry_duration`

(required) The maximum retry duration in milliseconds. Default value is `7200000` (2 hours).

`policy_type`

(required) The type of delivery policy.

Allowed values are: 'EXPONENTIAL'

### DBMS_CLOUD_OCI_ONS_CHANGE_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the specified topic or subscription to.

### DBMS_CLOUD_OCI_ONS_CONFIRMATION_RESULT_T Type

The confirmation details for the specified subscription.

Syntax
```

```

Fields

Field Description

`topic_name`

(required) The name of the subscribed topic.

`topic_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the topic associated with the specified subscription.

`endpoint`

(required) A locator that corresponds to the subscription protocol. For example, an email address for a subscription that uses the `EMAIL` protocol, or a URL for a subscription that uses an HTTP-based protocol.

`unsubscribe_url`

(required) The URL for unsubscribing from the topic.

`message`

(required) A human-readable string indicating the status of the subscription confirmation.

`subscription_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subscription specified in the request.

### DBMS_CLOUD_OCI_ONS_CREATE_SUBSCRIPTION_DETAILS_T Type

The configuration details for creating the subscription.

Syntax
```

```

Fields

Field Description

`topic_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the topic for the subscription.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment for the subscription.

`protocol`

(required) The protocol used for the subscription. Allowed values: * `CUSTOM_HTTPS` * `EMAIL` * `HTTPS` (deprecated; for PagerDuty endpoints, use `PAGERDUTY`) * `ORACLE_FUNCTIONS` * `PAGERDUTY` * `SLACK` * `SMS` .

`endpoint`

(required) A locator that corresponds to the subscription protocol. For example, an email address for a subscription that uses the `EMAIL` protocol, or a URL for a subscription that uses an HTTP-based protocol. HTTP-based protocols use URL endpoints that begin with \"http:\" or \"https:\". A URL cannot exceed 512 characters. Avoid entering confidential information.

`metadata`

(optional) Metadata for the subscription.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_ONS_CREATE_TOPIC_DETAILS_T Type

The configuration details for creating the topic.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the topic being created. The topic name must be unique across the tenancy. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to create the topic in.

`description`

(optional) The description of the topic being created. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_ONS_DELIVERY_POLICY_T Type

The subscription delivery policy.

Syntax
```

```

Fields

Field Description

`backoff_retry_policy`

(optional)

### DBMS_CLOUD_OCI_ONS_ERROR_T Type

An error has occurred.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_ONS_MESSAGE_DETAILS_T Type

The content of the message to be published.

Syntax
```

```

Fields

Field Description

`title`

(optional) The title of the message to be published. Avoid entering confidential information.

`body`

(required) The body of the message to be published. Avoid entering confidential information.

### DBMS_CLOUD_OCI_ONS_NOTIFICATION_TOPIC_T Type

The properties that define a topic. For general information about topics, see[Notifications Overview](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the topic.

`topic_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the topic.

`short_topic_id`

(optional) A unique short topic Id. This is used only for SMS subscriptions.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment for the topic.

`lifecycle_state`

(required) The lifecycle state of the topic.

Allowed values are: 'ACTIVE', 'DELETING', 'CREATING'

`description`

(optional) The description of the topic.

`time_created`

(required) The time the topic was created.

`etag`

(optional) For optimistic concurrency control. See `if-match`.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`api_endpoint`

(required) The endpoint for managing subscriptions or publishing messages to the topic.

### DBMS_CLOUD_OCI_ONS_NOTIFICATION_TOPIC_SUMMARY_T Type

A summary of the properties that define a topic.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the topic.

`topic_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the topic.

`short_topic_id`

(optional) A unique short topic Id. This is used only for SMS subscriptions.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment for the topic.

`lifecycle_state`

(required) The lifecycle state of the topic.

Allowed values are: 'ACTIVE', 'DELETING', 'CREATING'

`description`

(optional) The description of the topic.

`time_created`

(required) The time the topic was created.

`etag`

(optional) For optimistic concurrency control. See `if-match`.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`api_endpoint`

(required) The endpoint for managing subscriptions or publishing messages to the topic.

### DBMS_CLOUD_OCI_ONS_PUBLISH_RESULT_T Type

The response to a PublishMessage call.

Syntax
```

```

Fields

Field Description

`message_id`

(required) The UUID of the message.

`time_stamp`

(optional) The time that the service received the message.

### DBMS_CLOUD_OCI_ONS_SUBSCRIPTION_T Type

The subscription's configuration. For general information about subscriptions, see[Notifications Overview](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subscription.

`topic_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated topic.

`protocol`

(required) The protocol used for the subscription. Allowed values: * `CUSTOM_HTTPS` * `EMAIL` * `HTTPS` (deprecated; for PagerDuty endpoints, use `PAGERDUTY`) * `ORACLE_FUNCTIONS` * `PAGERDUTY` * `SLACK` * `SMS` .

`endpoint`

(required) A locator that corresponds to the subscription protocol. For example, an email address for a subscription that uses the `EMAIL` protocol, or a URL for a subscription that uses an HTTP-based protocol.

`lifecycle_state`

(required) The lifecycle state of the subscription. The status of a new subscription is PENDING; when confirmed, the subscription status changes to ACTIVE.

Allowed values are: 'PENDING', 'ACTIVE', 'DELETED'

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment for the subscription.

`created_time`

(optional) The time when this suscription was created.

`deliver_policy`

(optional) The delivery policy of the subscription. Stored as a JSON string.

`etag`

(optional) For optimistic concurrency control. See `if-match`.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_ONS_SUBSCRIPTION_SUMMARY_T Type

The subscription's configuration summary.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subscription.

`topic_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated topic.

`protocol`

(required) The protocol used for the subscription. Allowed values: * `CUSTOM_HTTPS` * `EMAIL` * `HTTPS` (deprecated; for PagerDuty endpoints, use `PAGERDUTY`) * `ORACLE_FUNCTIONS` * `PAGERDUTY` * `SLACK` * `SMS` .

`endpoint`

(required) A locator that corresponds to the subscription protocol. For example, an email address for a subscription that uses the `EMAIL` protocol, or a URL for a subscription that uses an HTTP-based protocol.

`lifecycle_state`

(required) The lifecycle state of the subscription. The status of a new subscription is PENDING; when confirmed, the subscription status changes to ACTIVE.

Allowed values are: 'PENDING', 'ACTIVE', 'DELETED'

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment for the subscription.

`created_time`

(optional) The time when this suscription was created.

`delivery_policy`

(optional)

`etag`

(optional) For optimistic concurrency control. See `if-match`.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_ONS_TOPIC_ATTRIBUTES_DETAILS_T Type

The configuration details for updating the topic.

Syntax
```

```

Fields

Field Description

`description`

(required) The description of the topic. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_ONS_UPDATE_SUBSCRIPTION_DETAILS_T Type

The configuration details for updating the subscription.

Syntax
```

```

Fields

Field Description

`delivery_policy`

(optional) The delivery policy of the subscription. Stored as a JSON string.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

- [Notifications Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ons_t.html#ADSDK-GUID-193637CE-97EC-4389-A2F9-8F7F92D93A44)
- [DBMS_CLOUD_OCI_ONS_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ons_t.html#ADSDK-GUID-06212F1C-5B26-4CCD-868B-69230D279B22)
- [DBMS_CLOUD_OCI_ONS_BACKOFF_RETRY_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ons_t.html#ADSDK-GUID-1F3F4980-A63E-4274-ADBF-04B554552FF1)
- [DBMS_CLOUD_OCI_ONS_CHANGE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ons_t.html#ADSDK-GUID-F70CB874-1B4B-4D92-AF93-DB50ED7F9701)
- [DBMS_CLOUD_OCI_ONS_CONFIRMATION_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ons_t.html#ADSDK-GUID-F47E97A6-97C5-45B0-AE30-3743A7FF9DAC)
- [DBMS_CLOUD_OCI_ONS_CREATE_SUBSCRIPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ons_t.html#ADSDK-GUID-6989E1B1-A7C7-46C1-A0B9-87B2BE21ECA5)
- [DBMS_CLOUD_OCI_ONS_CREATE_TOPIC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ons_t.html#ADSDK-GUID-EB870C12-5F18-44A3-A73D-B7B56423B237)
- [DBMS_CLOUD_OCI_ONS_DELIVERY_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ons_t.html#ADSDK-GUID-DAC1E837-E077-4C5E-878E-8F8F030DCF4E)
- [DBMS_CLOUD_OCI_ONS_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ons_t.html#ADSDK-GUID-88BC0F57-117F-409A-953E-CC9031EB5F31)
- [DBMS_CLOUD_OCI_ONS_MESSAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ons_t.html#ADSDK-GUID-FBEA3BAE-7725-4088-B625-F428EDE8D96D)
- [DBMS_CLOUD_OCI_ONS_NOTIFICATION_TOPIC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ons_t.html#ADSDK-GUID-88687A2B-6B27-4AFC-977D-AF7D42A52B4D)
- [DBMS_CLOUD_OCI_ONS_NOTIFICATION_TOPIC_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ons_t.html#ADSDK-GUID-3B861E6F-14E2-41F0-935F-8D0FF4E7962B)
- [DBMS_CLOUD_OCI_ONS_PUBLISH_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ons_t.html#ADSDK-GUID-1F893AE0-DC9A-4ECD-9782-5B8D6DFFB569)
- [DBMS_CLOUD_OCI_ONS_SUBSCRIPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ons_t.html#ADSDK-GUID-647C53A4-5659-4460-8B37-3B4704698B5F)
- [DBMS_CLOUD_OCI_ONS_SUBSCRIPTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ons_t.html#ADSDK-GUID-18631993-4386-4DB7-B371-E8558E08D123)
- [DBMS_CLOUD_OCI_ONS_TOPIC_ATTRIBUTES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ons_t.html#ADSDK-GUID-C267E6EC-C28D-473E-87E1-1169C12FA1E4)
- [DBMS_CLOUD_OCI_ONS_UPDATE_SUBSCRIPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ons_t.html#ADSDK-GUID-94BF953B-4531-4A77-8B17-F1F92C5968EE)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
