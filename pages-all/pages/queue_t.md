# Queue Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html
- Fetched: 2026-09-05 19:19 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#dcoc-content-body)

## Queue Common Types

### DBMS_CLOUD_OCI_QUEUE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_QUEUE_CHANGE_QUEUE_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_QUEUE_CHANNEL_COLLECTION_T Type

List of IDs of non-empty channels.

Syntax
```

```

Fields

Field Description

`items`

(required) The approximate list of IDs of non-empty channels.

### DBMS_CLOUD_OCI_QUEUE_CREATE_QUEUE_DETAILS_T Type

The information about a new queue.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The user-friendly name of the queue.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the queue.

`retention_in_seconds`

(optional) The retention period of messages in the queue, in seconds.

`visibility_in_seconds`

(optional) The default visibility timeout of the messages consumed from the queue, in seconds.

`timeout_in_seconds`

(optional) The default polling timeout of the messages in the queue, in seconds.

`channel_consumption_limit`

(optional) The percentage of allocated queue resources that can be consumed by a single channel. For example, if a queue has a storage limit of 2Gb, and a single channel consumption limit is 0.1 (10%), that means data size of a single channel can't exceed 200Mb. Consumption limit of 100% (default) means that a single channel can consume up-to all allocated queue's resources.

`dead_letter_queue_delivery_count`

(optional) The number of times a message can be delivered to a consumer before being moved to the dead letter queue. A value of 0 indicates that the DLQ is not used.

`custom_encryption_key_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the custom encryption key to be used to encrypt messages content.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_QUEUE_DELETE_MESSAGES_DETAILS_ENTRY_T Type

Object that represents a message to delete from a queue.

Syntax
```

```

Fields

Field Description

`receipt`

(required) The receipt of the message to delete.

### DBMS_CLOUD_OCI_QUEUE_DELETE_MESSAGES_DETAILS_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_queue_delete_messages_details_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_QUEUE_DELETE_MESSAGES_DETAILS_T Type

The details of a DeleteMessages request.

Syntax
```

```

Fields

Field Description

`entries`

(required) The array of messages to delete from a queue.

### DBMS_CLOUD_OCI_QUEUE_DELETE_MESSAGES_RESULT_ENTRY_T Type

Represents the result of a DeleteMessages request, whether it was successful or not. If a message was successfully deleted from the queue, the entry does not contain any fields. If a message failed to be deleted from the queue, the entry includes the `errorCode` and `errorMessage` fields.

Syntax
```

```

Fields

Field Description

`error_code`

(optional) The error code, in case the message was not successfully deleted from the queue.

`error_message`

(optional) A human-readable error message associated with the error code.

### DBMS_CLOUD_OCI_QUEUE_DELETE_MESSAGES_RESULT_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_queue_delete_messages_result_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_QUEUE_DELETE_MESSAGES_RESULT_T Type

The response to a DeleteMessages request. It indicates the number of server and client failures as well as an array of entries for successful and failed actions.

Syntax
```

```

Fields

Field Description

`server_failures`

(required) The number of messages that failed to be deleted from the queue because of a server failure.

`client_failures`

(required) The number of messages that failed to be deleted from the queue because of a client failure such as an invalid receipt.

`entries`

(required) An array of items representing the result of each action. The order is guaranteed to be the same as in the `DeleteMessagesDetails` object. If a message was successfully deleted from the queue, the entry does not contain any fields. If a message failed to be deleted from the queue, the entry includes the `errorCode` and `errorMessage` fields.

### DBMS_CLOUD_OCI_QUEUE_ERROR_T Type

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

### DBMS_CLOUD_OCI_QUEUE_MESSAGE_METADATA_T Type

Object that represents metadata for message.

Syntax
```

```

Fields

Field Description

`channel_id`

(required) The channel ID which specifies the channel to publish or retrieve messages.

`custom_properties`

(optional) Additional message properties

### DBMS_CLOUD_OCI_QUEUE_GET_MESSAGE_T Type

A message consumed from a queue.

Syntax
```

```

Fields

Field Description

`id`

(required) The ID of the message. This ID is only used for tracing and debugging purposes and isn't used as a parameter in any request.

`content`

(required) The content of the message.

`receipt`

(required) A receipt is a base64urlencode opaque token, uniquely representing a message. The receipt can be used to delete a message or update its visibility.

`delivery_count`

(required) The number of times that the message has been delivered to a consumer.

`visible_after`

(required) The time after which the message will be visible to other consumers, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2018-04-20T00:00:07.405Z`

`expire_after`

(required) The time after which the message will be automatically deleted, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2018-04-20T00:00:07.405Z`

`metadata`

(optional)

### DBMS_CLOUD_OCI_QUEUE_GET_MESSAGE_TBL Type

Nested table type of dbms_cloud_oci_queue_get_message_t.

Syntax
```

```

### DBMS_CLOUD_OCI_QUEUE_GET_MESSAGES_T Type

A list of messages from a queue.

Syntax
```

```

Fields

Field Description

`messages`

(required) List of messages from a queue.

### DBMS_CLOUD_OCI_QUEUE_PURGE_QUEUE_DETAILS_T Type

Purge parameters.

Syntax
```

```

Fields

Field Description

`purge_type`

(required) Type of the purge to perform: - NORMAL - purge only the normal queue - DLQ - purge only the dead letter queue - BOTH - purge both the normal queue and the dead letter queue

Allowed values are: 'NORMAL', 'DLQ', 'BOTH'

`channel_ids`

(optional) Optional parameter to specify the destination of purge operation. If the channel ID is specified, the purge operation will delete all the messages in the specific channels. If the channel ID is not specified, the purge operation will delete all the messages in the queue and in the child channels.

### DBMS_CLOUD_OCI_QUEUE_PUT_MESSAGE_T Type

A message that has been published to a queue.

Syntax
```

```

Fields

Field Description

`id`

(required) The ID of the message.

`expire_after`

(optional) The time after which the message will be automatically deleted, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2018-04-20T00:00:07.405Z`

### DBMS_CLOUD_OCI_QUEUE_PUT_MESSAGE_TBL Type

Nested table type of dbms_cloud_oci_queue_put_message_t.

Syntax
```

```

### DBMS_CLOUD_OCI_QUEUE_PUT_MESSAGES_T Type

A list of the messages published to a queue.

Syntax
```

```

Fields

Field Description

`messages`

(required) The messages that have been published to a queue.

### DBMS_CLOUD_OCI_QUEUE_PUT_MESSAGES_DETAILS_ENTRY_T Type

Object that represents a message to publish into a queue.

Syntax
```

```

Fields

Field Description

`content`

(required) The content of the message

`metadata`

(optional)

### DBMS_CLOUD_OCI_QUEUE_PUT_MESSAGES_DETAILS_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_queue_put_messages_details_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_QUEUE_PUT_MESSAGES_DETAILS_T Type

The details of a PutMessages request.

Syntax
```

```

Fields

Field Description

`messages`

(required) The array of messages to put into a queue.

### DBMS_CLOUD_OCI_QUEUE_QUEUE_T Type

A detailed representation of a queue and its configuration.

Syntax
```

```

Fields

Field Description

`id`

(required) A unique identifier for the queue that is immutable on creation.

`display_name`

(optional) A user-friendly name for the queue. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the queue.

`time_created`

(required) The time that the queue was created, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2018-04-20T00:00:07.405Z`

`time_updated`

(required) The time that the queue was updated, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2018-04-20T00:00:07.405Z`

`lifecycle_state`

(required) The current state of the queue.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) Any additional details about the current state of the queue.

`messages_endpoint`

(required) The endpoint to use to consume or publish messages in the queue.

`retention_in_seconds`

(required) The retention period of the messages in the queue, in seconds.

`visibility_in_seconds`

(required) The default visibility timeout of the messages consumed from the queue, in seconds.

`timeout_in_seconds`

(required) The default polling timeout of the messages in the queue, in seconds.

`dead_letter_queue_delivery_count`

(required) The number of times a message can be delivered to a consumer before being moved to the dead letter queue. A value of 0 indicates that the DLQ is not used.

`custom_encryption_key_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the custom encryption key to be used to encrypt messages content.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`channel_consumption_limit`

(optional) The percentage of allocated queue resources that can be consumed by a single channel. For example, if a queue has a storage limit of 2Gb, and a single channel consumption limit is 0.1 (10%), that means data size of a single channel can't exceed 200Mb. Consumption limit of 100% (default) means that a single channel can consume up-to all allocated queue's resources.

### DBMS_CLOUD_OCI_QUEUE_QUEUE_SUMMARY_T Type

Summary of the queue.

Syntax
```

```

Fields

Field Description

`id`

(required) A unique identifier for the queue that is immutable on creation.

`display_name`

(optional) A user-friendly name for the queue. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the queue.

`time_created`

(required) The time that the queue was created, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2018-04-20T00:00:07.405Z`

`time_updated`

(required) The time that the queue was updated, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2018-04-20T00:00:07.405Z`

`lifecycle_state`

(required) The current state of the queue.

`lifecycle_details`

(optional) Any additional details about the current state of the queue.

`messages_endpoint`

(required) The endpoint to use to consume or publish messages in the queue.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_QUEUE_QUEUE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_queue_queue_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_QUEUE_QUEUE_COLLECTION_T Type

Results of a queue search. Contains both QueueSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of queues.

### DBMS_CLOUD_OCI_QUEUE_STATS_T Type

The stats for a queue or a dead letter queue.

Syntax
```

```

Fields

Field Description

`visible_messages`

(required) The approximate number of visible messages (available for delivery) currently in the queue.

`in_flight_messages`

(required) The approximate number of messages delivered to a consumer but not yet deleted and so unavailable for re-delivery.

`size_in_bytes`

(required) The approximate size of the queue in bytes. Sum of the size of visible and in-flight messages.

### DBMS_CLOUD_OCI_QUEUE_QUEUE_STATS_T Type

The stats for a queue and its dead letter queue. If channelId is specified in request field, it will return channel specific stats response.

Syntax
```

```

Fields

Field Description

`queue`

(required)

`dlq`

(required)

`channel_id`

(optional) If channelId is presented in GetStats call, the channel id will be returned in the GetStats response.

### DBMS_CLOUD_OCI_QUEUE_UPDATE_MESSAGE_DETAILS_T Type

Updates the visibility of a message

Syntax
```

```

Fields

Field Description

`visibility_in_seconds`

(required) The new visibility of the message relative to the current time (as-per the clock of the server receiving the request).

### DBMS_CLOUD_OCI_QUEUE_UPDATE_MESSAGES_DETAILS_ENTRY_T Type

Object that represents a message to update in a queue.

Syntax
```

```

Fields

Field Description

`receipt`

(required) The receipt of the message to update.

`visibility_in_seconds`

(required) The new visibility of the message relative to the current time (as-per the clock of the server receiving the request).

### DBMS_CLOUD_OCI_QUEUE_UPDATE_MESSAGES_DETAILS_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_queue_update_messages_details_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_QUEUE_UPDATE_MESSAGES_DETAILS_T Type

The details of an UpdateMessages request.

Syntax
```

```

Fields

Field Description

`entries`

(required) The array of messages to update in a queue.

### DBMS_CLOUD_OCI_QUEUE_UPDATE_MESSAGES_RESULT_ENTRY_T Type

Represents the result of a UpdateMessages request, whether it was successful or not. If a message was successfully updated in the queue, the entry includes the `id` and `visibleAfter` fields. If a message failed to be updated in the queue, the entry includes the `errorCode` and `errorMessage` fields.

Syntax
```

```

Fields

Field Description

`id`

(optional) The ID of the message that's been updated.

`visible_after`

(optional) The time after which the message will be visible to other consumers, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2018-04-20T00:00:07.405Z`

`error_code`

(optional) The error code, in case the message was not successfully updated in the queue.

`error_message`

(optional) A human-readable error message associated with the error code.

### DBMS_CLOUD_OCI_QUEUE_UPDATE_MESSAGES_RESULT_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_queue_update_messages_result_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_QUEUE_UPDATE_MESSAGES_RESULT_T Type

The response to a UpdateMessages request. It indicates the number of server and client failures as well as an array of entries for successful and failed actions.

Syntax
```

```

Fields

Field Description

`server_failures`

(required) The number of messages that failed to be updated in the queue because of a server failure.

`client_failures`

(required) The number of messages that failed to be updated in the queue because of a client failure such as an invalid receipt or invalid `visibilityInSeconds`.

`entries`

(required) An array of items representing the result of each action. The order is guaranteed to be the same as in the `UpdateMessagesDetails` object. If a message was successfully updated in the queue, the entry includes the `id` and `visibleAfter` fields. If a message failed to be updated in the queue, the entry includes the `errorCode` and `errorMessage` fields.

### DBMS_CLOUD_OCI_QUEUE_UPDATE_QUEUE_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the queue.

`visibility_in_seconds`

(optional) The default visibility timeout of the messages consumed from the queue, in seconds.

`timeout_in_seconds`

(optional) The default polling timeout of the messages in the queue, in seconds.

`channel_consumption_limit`

(optional) The percentage of allocated queue resources that can be consumed by a single channel. For example, if a queue has a storage limit of 2Gb, and a single channel consumption limit is 0.1 (10%), that means data size of a single channel can't exceed 200Mb. Consumption limit of 100% (default) means that a single channel can consume up-to all allocated queue's resources.

`dead_letter_queue_delivery_count`

(optional) The number of times a message can be delivered to a consumer before being moved to the dead letter queue. A value of 0 indicates that the DLQ is not used. Changing that value to a lower threshold does not retroactively move in-flight messages in the dead letter queue.

`custom_encryption_key_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the custom encryption key to be used to encrypt messages content. A string with a length of 0 means the custom key should be removed from queue.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_QUEUE_UPDATED_MESSAGE_T Type

An updated message with the new visibility.

Syntax
```

```

Fields

Field Description

`id`

(required) The ID of the message that's been updated.

`visible_after`

(required) The time after which the message will be visible to other consumers, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2018-04-20T00:00:07.405Z`

### DBMS_CLOUD_OCI_QUEUE_WORK_REQUEST_RESOURCE_T Type

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

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata

### DBMS_CLOUD_OCI_QUEUE_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_queue_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_QUEUE_WORK_REQUEST_T Type

A description of workrequest status

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_QUEUE', 'UPDATE_QUEUE', 'DELETE_QUEUE', 'MOVE_QUEUE', 'PURGE_QUEUE'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The id of the work request.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

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

### DBMS_CLOUD_OCI_QUEUE_WORK_REQUEST_ERROR_T Type

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

(required) The time the error occured. An[RFC 3339](https://tools.ietf.org/rfc/rfc3339)formatted datetime string.

### DBMS_CLOUD_OCI_QUEUE_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_queue_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_QUEUE_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestError objects.

### DBMS_CLOUD_OCI_QUEUE_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written. An[RFC 3339](https://tools.ietf.org/rfc/rfc3339)formatted datetime string

### DBMS_CLOUD_OCI_QUEUE_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_queue_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_QUEUE_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a workRequestLog search. Contains both workRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestLogEntries.

### DBMS_CLOUD_OCI_QUEUE_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_QUEUE', 'UPDATE_QUEUE', 'DELETE_QUEUE', 'MOVE_QUEUE', 'PURGE_QUEUE'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The ID of the work request.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

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

### DBMS_CLOUD_OCI_QUEUE_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_queue_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_QUEUE_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestSummary objects.

- [Queue Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-9E15470A-7EDD-4E38-81B3-329E16E1C893)
- [DBMS_CLOUD_OCI_QUEUE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-3D3716C3-44A8-4C2E-BA80-DBFC51E10D31)
- [DBMS_CLOUD_OCI_QUEUE_CHANGE_QUEUE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-7FBE3D1B-C819-4852-8A68-88FAECAFC146)
- [DBMS_CLOUD_OCI_QUEUE_CHANNEL_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-2F04B333-6779-4F97-A4F1-F3D0B76000BE)
- [DBMS_CLOUD_OCI_QUEUE_CREATE_QUEUE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-01CA62AA-9C7A-479C-A7AD-1E38540127AB)
- [DBMS_CLOUD_OCI_QUEUE_DELETE_MESSAGES_DETAILS_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-DE126D62-8A93-4702-AD6D-EC8DC8FFA297)
- [DBMS_CLOUD_OCI_QUEUE_DELETE_MESSAGES_DETAILS_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-526144A6-391B-4EB8-B47F-F8DE75438C0B)
- [DBMS_CLOUD_OCI_QUEUE_DELETE_MESSAGES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-32913A37-BAA6-4E77-82BA-0F379B3916D8)
- [DBMS_CLOUD_OCI_QUEUE_DELETE_MESSAGES_RESULT_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-4DE4DE60-F11A-45EC-AFC3-A0DED00D63C7)
- [DBMS_CLOUD_OCI_QUEUE_DELETE_MESSAGES_RESULT_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-8CCA7416-C95B-4C7A-BE57-F7C39519973F)
- [DBMS_CLOUD_OCI_QUEUE_DELETE_MESSAGES_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-A085A600-4218-44B6-B5BE-5A30DA84FCBB)
- [DBMS_CLOUD_OCI_QUEUE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-5E4B4647-7935-4D78-BC4A-B22C58298FBF)
- [DBMS_CLOUD_OCI_QUEUE_MESSAGE_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-8924DE94-8856-4A08-A777-331423EC4A7A)
- [DBMS_CLOUD_OCI_QUEUE_GET_MESSAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-B663A689-A4C6-458D-984D-A0E7F6130685)
- [DBMS_CLOUD_OCI_QUEUE_GET_MESSAGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-05ADE652-F45F-4D3A-92DF-27C8AA303B64)
- [DBMS_CLOUD_OCI_QUEUE_GET_MESSAGES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-EE5047D5-0997-4DBC-A515-8D28A64BF7B4)
- [DBMS_CLOUD_OCI_QUEUE_PURGE_QUEUE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-69936514-3221-4B7D-801D-1A9DBD977BBF)
- [DBMS_CLOUD_OCI_QUEUE_PUT_MESSAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-9B06BBC2-4B66-4D21-B89D-9253683E56ED)
- [DBMS_CLOUD_OCI_QUEUE_PUT_MESSAGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-F8FAB51E-4C29-4BA8-B17F-33916EE91F2A)
- [DBMS_CLOUD_OCI_QUEUE_PUT_MESSAGES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-32BFE40F-4A96-40BF-8B80-FA1C6BFD4D14)
- [DBMS_CLOUD_OCI_QUEUE_PUT_MESSAGES_DETAILS_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-75337439-FA66-48F3-BCCC-8BAF9E1CD764)
- [DBMS_CLOUD_OCI_QUEUE_PUT_MESSAGES_DETAILS_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-339A3381-21BD-4FA0-9604-5399136A022F)
- [DBMS_CLOUD_OCI_QUEUE_PUT_MESSAGES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-55CA926A-3C80-4DAF-90FC-8EB5E6019CD1)
- [DBMS_CLOUD_OCI_QUEUE_QUEUE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-61B69288-7CEE-4FF0-BB29-8D5D097433A4)
- [DBMS_CLOUD_OCI_QUEUE_QUEUE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-A9592A45-CF10-4B59-98B1-9500C8D5A835)
- [DBMS_CLOUD_OCI_QUEUE_QUEUE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-6EAA4D3A-4BC1-4A2C-952C-F40280912B59)
- [DBMS_CLOUD_OCI_QUEUE_QUEUE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-AE96CD14-0ED0-4905-8A9A-C61227D82E5B)
- [DBMS_CLOUD_OCI_QUEUE_STATS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-997C8ECF-913D-4780-9BBD-3B88D126965C)
- [DBMS_CLOUD_OCI_QUEUE_QUEUE_STATS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-A111F391-DE5B-4020-9B69-5F4CBA7275FD)
- [DBMS_CLOUD_OCI_QUEUE_UPDATE_MESSAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-D9A55FB5-429F-40CE-8FF4-F8E0B72E1A6A)
- [DBMS_CLOUD_OCI_QUEUE_UPDATE_MESSAGES_DETAILS_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-448D42A0-38C2-405C-AC11-4E48EF5AC07E)
- [DBMS_CLOUD_OCI_QUEUE_UPDATE_MESSAGES_DETAILS_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-4536C8D0-65C2-47E0-A499-FC12115A47D3)
- [DBMS_CLOUD_OCI_QUEUE_UPDATE_MESSAGES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-464BD7C6-7E40-4087-9E72-646B369611C6)
- [DBMS_CLOUD_OCI_QUEUE_UPDATE_MESSAGES_RESULT_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-0890191B-B960-46FE-BF6D-E21C77E5FCEF)
- [DBMS_CLOUD_OCI_QUEUE_UPDATE_MESSAGES_RESULT_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-C11A7AE5-2C24-4867-B40B-2659308C71D8)
- [DBMS_CLOUD_OCI_QUEUE_UPDATE_MESSAGES_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-6F78D480-7044-49D2-8B6E-B85EACCF0D3B)
- [DBMS_CLOUD_OCI_QUEUE_UPDATE_QUEUE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-44596DEC-CA7A-4782-BA02-4ECECD078EB3)
- [DBMS_CLOUD_OCI_QUEUE_UPDATED_MESSAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-043BBD3E-7A9B-444E-9D4E-24FF287F811B)
- [DBMS_CLOUD_OCI_QUEUE_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-65AD6DB7-F089-4150-A71C-39356B3BF62B)
- [DBMS_CLOUD_OCI_QUEUE_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-C49A2A05-45DF-47F9-A907-8CE435291A23)
- [DBMS_CLOUD_OCI_QUEUE_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-45671358-7294-4AEB-948A-A8E1EC4F8530)
- [DBMS_CLOUD_OCI_QUEUE_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-30478DD5-B19C-44A8-B71F-49F6AE27B5C7)
- [DBMS_CLOUD_OCI_QUEUE_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-7DFAE60C-E223-41E8-A970-9968A51787D9)
- [DBMS_CLOUD_OCI_QUEUE_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-01DACEC9-12C6-47CA-9712-AD0AE870B339)
- [DBMS_CLOUD_OCI_QUEUE_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-EE8B96B8-F9D8-4A1E-B07C-0F9AE236C0F2)
- [DBMS_CLOUD_OCI_QUEUE_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-051AF746-4743-4940-B359-B6D3F371244A)
- [DBMS_CLOUD_OCI_QUEUE_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-EAD1FB19-9E6D-4E10-B06D-A400D2614EB8)
- [DBMS_CLOUD_OCI_QUEUE_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-565740C2-8C4B-4D81-8260-4DC545EF6BFD)
- [DBMS_CLOUD_OCI_QUEUE_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-93463102-1BA7-4C3F-B1D4-C935A8353788)
- [DBMS_CLOUD_OCI_QUEUE_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/queue_t.html#ADSDK-GUID-E19543D9-0673-4E8F-A9E0-8058F9ED7EB8)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
