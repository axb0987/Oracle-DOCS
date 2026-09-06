# Streaming Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html
- Fetched: 2026-09-05 19:20 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#dcoc-content-body)

## Streaming Common Types

### DBMS_CLOUD_OCI_STREAMING_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_STREAMING_CHANGE_CONNECT_HARNESS_COMPARTMENT_DETAILS_T Type

Detailed representation of a change connect harness compartment operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_STREAMING_CHANGE_STREAM_COMPARTMENT_DETAILS_T Type

Detailed representation of a change stream compartment operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_STREAMING_CHANGE_STREAM_POOL_COMPARTMENT_DETAILS_T Type

Detailed representation of a change stream pool compartment operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_STREAMING_CONNECT_HARNESS_T Type

Detailed representation of a connect harness.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the connect harness. Avoid entering confidential information. Example: `JDBCConnector`

`id`

(required) The OCID of the connect harness.

`compartment_id`

(required) The OCID of the compartment that contains the connect harness.

`lifecycle_state`

(required) The current state of the connect harness.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'UPDATING'

`lifecycle_state_details`

(optional) Any additional details about the current state of the connect harness.

`time_created`

(required) The date and time the connect harness was created, expressed in in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2018-04-20T00:00:07.405Z`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. Exists for cross-compatibility only. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}'

### DBMS_CLOUD_OCI_STREAMING_CONNECT_HARNESS_SUMMARY_T Type

Summary representation of a ConnectHarness.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the connect harness. Example: `TelemetryEvents`

`id`

(required) The OCID of the connect harness.

`compartment_id`

(required) The OCID of the compartment that contains the connect harness.

`lifecycle_state`

(required) The current state of the connect harness.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'UPDATING'

`time_created`

(required) The date and time the connect harness was created, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2018-04-20T00:00:07.405Z`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair that is applied with no predefined name, type, or namespace. Exists for cross-compatibility only. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_STREAMING_CREATE_CONNECT_HARNESS_DETAILS_T Type

Object used to create a connect harness.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the connect harness. Avoid entering confidential information. Example: `JDBCConnector`

`compartment_id`

(required) The OCID of the compartment that contains the connect harness.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair that is applied with no predefined name, type, or namespace. Exists for cross-compatibility only. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_STREAMING_CREATE_CURSOR_DETAILS_T Type

Object used to create a cursor to consume messages in a stream.

Syntax
```

```

Fields

Field Description

`partition`

(required) The partition to get messages from.

`l_type`

(required) The type of cursor, which determines the starting point from which the stream will be consumed: - `AFTER_OFFSET:` The partition position immediately following the offset you specify. (Offsets are assigned when you successfully append a message to a partition in a stream.) - `AT_OFFSET:` The exact partition position indicated by the offset you specify. - `AT_TIME:` A specific point in time. - `LATEST:` The most recent message in the partition that was added after the cursor was created. - `TRIM_HORIZON:` The oldest message in the partition that is within the retention period window.

Allowed values are: 'AFTER_OFFSET', 'AT_OFFSET', 'AT_TIME', 'LATEST', 'TRIM_HORIZON'

`offset`

(optional) The offset to consume from if the cursor type is `AT_OFFSET` or `AFTER_OFFSET`.

`time`

(optional) The time to consume from if the cursor type is `AT_TIME`, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format.

### DBMS_CLOUD_OCI_STREAMING_CREATE_GROUP_CURSOR_DETAILS_T Type

Object used to create a group cursor.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of the cursor. This value is only used when the group is created.

Allowed values are: 'AT_TIME', 'LATEST', 'TRIM_HORIZON'

`time`

(optional) The time to consume from if type is AT_TIME.

`group_name`

(required) Name of the consumer group.

`instance_name`

(optional) A unique identifier for the instance joining the consumer group. If an instanceName is not provided, a UUID will be generated and used.

`timeout_in_ms`

(optional) The amount of a consumer instance inactivity time, before partition reservations are released.

`commit_on_get`

(optional) When using consumer-groups, the default commit-on-get behaviour can be overriden by setting this value to false. If disabled, a consumer must manually commit their cursors.

### DBMS_CLOUD_OCI_STREAMING_CREATE_STREAM_DETAILS_T Type

Object used to create a stream.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the stream. Avoid entering confidential information. Example: `TelemetryEvents`

`partitions`

(required) The number of partitions in the stream.

`compartment_id`

(optional) The OCID of the compartment that contains the stream.

`stream_pool_id`

(optional) The OCID of the stream pool that contains the stream.

`retention_in_hours`

(optional) The retention period of the stream, in hours. Accepted values are between 24 and 168 (7 days). If not specified, the stream will have a retention period of 24 hours.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair that is applied with no predefined name, type, or namespace. Exists for cross-compatibility only. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_STREAMING_KAFKA_SETTINGS_T Type

Settings for the Kafka compatibility layer.

Syntax
```

```

Fields

Field Description

`bootstrap_servers`

(optional) Bootstrap servers.

`auto_create_topics_enable`

(optional) Enable auto creation of topic on the server.

`log_retention_hours`

(optional) The number of hours to keep a log file before deleting it (in hours).

`num_partitions`

(optional) The default number of log partitions per topic.

### DBMS_CLOUD_OCI_STREAMING_CUSTOM_ENCRYPTION_KEY_DETAILS_T Type

The OCID of the custom encryption key to be used or deleted if currently being used.

Syntax
```

```

Fields

Field Description

`kms_key_id`

(required) Custom Encryption Key (Master Key) ocid.

### DBMS_CLOUD_OCI_STREAMING_PRIVATE_ENDPOINT_DETAILS_T Type

Optional parameters if a private stream pool is requested.

Syntax
```

```

Fields

Field Description

`subnet_id`

(optional) If specified, the stream pool will be private and only accessible from inside that subnet. Producing-to and consuming-from a stream inside a private stream pool can also only be done from inside the subnet. That value cannot be changed.

`private_endpoint_ip`

(optional) The optional private IP you want to be associated with your private stream pool. That parameter can only be specified when the subnetId parameter is set. It cannot be changed. The private IP needs to be part of the CIDR range of the specified subnetId or the creation will fail. If not specified a random IP inside the subnet will be chosen. After the stream pool is created, a custom FQDN, pointing to this private IP, is created. The FQDN is then used to access the service instead of the private IP.

`nsg_ids`

(optional) The optional list of network security groups to be used with the private endpoint of the stream pool. That value cannot be changed.

### DBMS_CLOUD_OCI_STREAMING_CREATE_STREAM_POOL_DETAILS_T Type

Object used to create a stream pool.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment that contains the stream.

`name`

(required) The name of the stream pool. Avoid entering confidential information. Example: `MyStreamPool`

`kafka_settings`

(optional)

`custom_encryption_key_details`

(optional)

`private_endpoint_details`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair that is applied with no predefined name, type, or namespace. Exists for cross-compatibility only. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_STREAMING_CURSOR_T Type

A cursor that indicates the position in the stream from which you want to begin consuming messages and which is required by the`GET_MESSAGES`Function operation.

Syntax
```

```

Fields

Field Description

`value`

(required) The cursor to pass to the `GetMessages` operation.

### DBMS_CLOUD_OCI_STREAMING_CUSTOM_ENCRYPTION_KEY_T Type

Custom Encryption Key which will be used for encryption by all the streams in the pool.

Syntax
```

```

Fields

Field Description

`kms_key_id`

(optional) Custom Encryption Key (Master Key) ocid.

`key_state`

(optional) Life cycle State of the custom key

Allowed values are: 'ACTIVE', 'CREATING', 'DELETING', 'NONE', 'FAILED', 'UPDATING'

### DBMS_CLOUD_OCI_STREAMING_ERROR_T Type

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

### DBMS_CLOUD_OCI_STREAMING_PARTITION_RESERVATION_T Type

Represents the state of a single partition reservation.

Syntax
```

```

Fields

Field Description

`partition`

(optional) The partition for which the reservation applies.

`committed_offset`

(optional) The latest offset which has been committed for this partition.

`reserved_instance`

(optional) The consumer instance which currently has the partition reserved.

`time_reserved_until`

(optional) A timestamp when the current reservation expires.

### DBMS_CLOUD_OCI_STREAMING_PARTITION_RESERVATION_TBL Type

Nested table type of dbms_cloud_oci_streaming_partition_reservation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STREAMING_GROUP_T Type

Represents the current state of a consumer group, including partition reservations and committed offsets.

Syntax
```

```

Fields

Field Description

`stream_id`

(required) The streamId for which the group exists.

`group_name`

(required) The name of the consumer group.

`reservations`

(optional) An array of the partition reservations of a group.

### DBMS_CLOUD_OCI_STREAMING_MESSAGE_T Type

A message in a stream.

Syntax
```

```

Fields

Field Description

`stream`

(required) The name of the stream that the message belongs to.

`partition`

(required) The ID of the partition where the message is stored.

`key`

(required) The key associated with the message, expressed as a byte array.

`value`

(required) The value associated with the message, expressed as a byte array.

`offset`

(required) The offset of the message, which uniquely identifies it within the partition.

`l_timestamp`

(required) The timestamp indicating when the server appended the message to the stream.

### DBMS_CLOUD_OCI_STREAMING_PRIVATE_ENDPOINT_SETTINGS_T Type

Optional settings if the stream pool is private.

Syntax
```

```

Fields

Field Description

`subnet_id`

(optional) The subnet id from which the private stream pool can be accessed. Trying to access the streams from another network location will result in an error.

`private_endpoint_ip`

(optional) The private IP associated with the stream pool in the associated subnetId. The stream pool's FQDN resolves to that IP and should be used - instead of the private IP - in order to not trigger any TLS issues.

`nsg_ids`

(optional) The optional list of network security groups that are associated with the private endpoint of the stream pool.

### DBMS_CLOUD_OCI_STREAMING_PUT_MESSAGES_DETAILS_ENTRY_T Type

Object that represents a message to emit to a stream.

Syntax
```

```

Fields

Field Description

`key`

(optional) The key of the message, expressed as a byte array up to 256 bytes in size. Messages with the same key are stored in the same partition.

`value`

(required) The message, expressed as a byte array up to 1 MiB in size.

### DBMS_CLOUD_OCI_STREAMING_PUT_MESSAGES_DETAILS_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_streaming_put_messages_details_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STREAMING_PUT_MESSAGES_DETAILS_T Type

Object that represents an array of messages to emit to a stream.

Syntax
```

```

Fields

Field Description

`messages`

(required) The array of messages to put into a stream.

### DBMS_CLOUD_OCI_STREAMING_PUT_MESSAGES_RESULT_ENTRY_T Type

Represents the result of a`PUT_MESSAGES`Function request, whether it was successful or not. If a message was successfully appended to the stream, the entry includes the `offset`, `partition`, and `timestamp`. If the message failed to be appended to the stream, the entry includes the `error` and `errorMessage`.

Syntax
```

```

Fields

Field Description

`partition`

(optional) The ID of the partition where the message was stored.

`offset`

(optional) The offset of the message in the partition.

`l_timestamp`

(optional) The timestamp indicating when the server appended the message to the stream.

`error`

(optional) The error code, in case the message was not successfully appended to the stream.

`error_message`

(optional) A human-readable error message associated with the error code.

### DBMS_CLOUD_OCI_STREAMING_PUT_MESSAGES_RESULT_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_streaming_put_messages_result_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_STREAMING_PUT_MESSAGES_RESULT_T Type

The response to a`PUT_MESSAGES`Function request. It indicates the number of failed messages as well as an array of results for successful and failed messages.

Syntax
```

```

Fields

Field Description

`failures`

(required) The number of messages that failed to be added to the stream.

`entries`

(required) An array of items representing the result of each message. The order is guaranteed to be the same as in the `PutMessagesDetails` object. If a message was successfully appended to the stream, the entry includes the `offset`, `partition`, and `timestamp`. If a message failed to be appended to the stream, the entry includes the `error` and `errorMessage`.

### DBMS_CLOUD_OCI_STREAMING_STREAM_T Type

Detailed representation of a stream, including all its partitions.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the stream. Avoid entering confidential information. Example: `TelemetryEvents`

`id`

(required) The OCID of the stream.

`partitions`

(required) The number of partitions in the stream.

`retention_in_hours`

(required) The retention period of the stream, in hours. This property is read-only.

`compartment_id`

(required) The OCID of the stream.

`stream_pool_id`

(required) The OCID of the stream pool that contains the stream.

`lifecycle_state`

(required) The current state of the stream.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'UPDATING'

`lifecycle_state_details`

(optional) Any additional details about the current state of the stream.

`time_created`

(required) The date and time the stream was created, expressed in in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2018-04-20T00:00:07.405Z`

`messages_endpoint`

(required) The endpoint to use when creating the StreamClient to consume or publish messages in the stream. If the associated stream pool is private, the endpoint is also private and can only be accessed from inside the stream pool's associated subnet.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. Exists for cross-compatibility only. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}'

### DBMS_CLOUD_OCI_STREAMING_STREAM_POOL_T Type

The details of a stream pool.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the stream pool.

`compartment_id`

(required) Compartment OCID that the pool belongs to.

`name`

(required) The name of the stream pool.

`lifecycle_state`

(required) The current state of the stream pool.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'UPDATING'

`lifecycle_state_details`

(optional) Any additional details about the current state of the stream.

`time_created`

(required) The date and time the stream pool was created, expressed in in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2018-04-20T00:00:07.405Z`

`kafka_settings`

(required)

`custom_encryption_key`

(required)

`is_private`

(optional) True if the stream pool is private, false otherwise. If the stream pool is private, the streams inside the stream pool can only be accessed from inside the associated subnetId.

`endpoint_fqdn`

(optional) The FQDN used to access the streams inside the stream pool (same FQDN as the messagesEndpoint attribute of a`STREAM`Type object). If the stream pool is private, the FQDN is customized and can only be accessed from inside the associated subnetId, otherwise the FQDN is publicly resolvable. Depending on which protocol you attempt to use, you need to either prepend https or append the Kafka port.

`private_endpoint_settings`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. Exists for cross-compatibility only. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}'

### DBMS_CLOUD_OCI_STREAMING_STREAM_POOL_SUMMARY_T Type

The summary representation of a stream pool.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the stream pool.

`compartment_id`

(required) Compartment OCID that the pool belongs to.

`name`

(required) The name of the stream pool.

`lifecycle_state`

(required) The current state of the stream pool.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'UPDATING'

`time_created`

(required) The date and time the stream pool was created, expressed in in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2018-04-20T00:00:07.405Z`

`is_private`

(optional) True if the stream pool is private, false otherwise. The associated endpoint and subnetId of a private stream pool can be retrieved through the`GET_STREAM_POOL`Function API.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair that is applied with no predefined name, type, or namespace. Exists for cross-compatibility only. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_STREAMING_STREAM_SUMMARY_T Type

Summary representation of a stream.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the stream. Example: `TelemetryEvents`

`id`

(required) The OCID of the stream.

`partitions`

(required) The number of partitions in the stream.

`compartment_id`

(required) The OCID of the compartment that contains the stream.

`stream_pool_id`

(required) The OCID of the stream pool that contains the stream.

`lifecycle_state`

(required) The current state of the stream.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'UPDATING'

`time_created`

(required) The date and time the stream was created, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2018-04-20T00:00:07.405Z`

`messages_endpoint`

(required) The endpoint to use when creating the StreamClient to consume or publish messages in the stream. If the associated stream pool is private, the endpoint is also private and can only be accessed from inside the stream pool's associated subnet.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair that is applied with no predefined name, type, or namespace. Exists for cross-compatibility only. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_STREAMING_UPDATE_CONNECT_HARNESS_DETAILS_T Type

Object used to update a connect harness.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair that is applied with no predefined name, type, or namespace. Exists for cross-compatibility only. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_STREAMING_UPDATE_GROUP_DETAILS_T Type

Request body for operationally managing a group.

Syntax
```

```

Fields

Field Description

`l_type`

(optional) The type of the cursor.

Allowed values are: 'AT_TIME', 'LATEST', 'TRIM_HORIZON'

`time`

(optional) The time to consume from if type is AT_TIME.

### DBMS_CLOUD_OCI_STREAMING_UPDATE_STREAM_DETAILS_T Type

Object used to update a stream.

Syntax
```

```

Fields

Field Description

`stream_pool_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the stream pool where the stream should be moved.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair that is applied with no predefined name, type, or namespace. Exists for cross-compatibility only. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_STREAMING_UPDATE_STREAM_POOL_DETAILS_T Type

Object used to update the stream pool's details.

Syntax
```

```

Fields

Field Description

`name`

(optional)

`kafka_settings`

(optional)

`custom_encryption_key_details`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair that is applied with no predefined name, type, or namespace. Exists for cross-compatibility only. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

- [Streaming Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-64E57827-7776-426D-8ED9-835CCE37D54C)
- [DBMS_CLOUD_OCI_STREAMING_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-503C7DB0-FF79-42B9-8B2D-9E06828EC18F)
- [DBMS_CLOUD_OCI_STREAMING_CHANGE_CONNECT_HARNESS_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-0CB9530B-F07F-4850-B505-2A18EBDE3C09)
- [DBMS_CLOUD_OCI_STREAMING_CHANGE_STREAM_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-DA10F5FE-3946-470E-B6E9-501049DEF8DA)
- [DBMS_CLOUD_OCI_STREAMING_CHANGE_STREAM_POOL_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-AC2F42CF-36D7-402F-A748-F1A60CD842E8)
- [DBMS_CLOUD_OCI_STREAMING_CONNECT_HARNESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-13099604-E71C-4112-B921-0E1231357E06)
- [DBMS_CLOUD_OCI_STREAMING_CONNECT_HARNESS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-AEA29AE3-48FB-41BF-88FC-B7FAC95865DA)
- [DBMS_CLOUD_OCI_STREAMING_CREATE_CONNECT_HARNESS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-06E1823E-BCF0-415B-AA02-3E1863E2197F)
- [DBMS_CLOUD_OCI_STREAMING_CREATE_CURSOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-466D6D01-ED2B-49BE-8517-8921D0438292)
- [DBMS_CLOUD_OCI_STREAMING_CREATE_GROUP_CURSOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-AA22A69E-07E5-4A09-A21C-876C4EF93491)
- [DBMS_CLOUD_OCI_STREAMING_CREATE_STREAM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-951DDD95-E99E-4E2F-93DC-CCFF834E78AB)
- [DBMS_CLOUD_OCI_STREAMING_KAFKA_SETTINGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-891E15F4-4552-4D1A-BF01-FF1D5006C9D5)
- [DBMS_CLOUD_OCI_STREAMING_CUSTOM_ENCRYPTION_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-9BD6A434-80AA-4A69-9C86-0B252E5AB065)
- [DBMS_CLOUD_OCI_STREAMING_PRIVATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-EF096514-CF19-42D5-9086-2DF65CF57516)
- [DBMS_CLOUD_OCI_STREAMING_CREATE_STREAM_POOL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-B980CC5E-A4BD-4D0A-83B9-79AD793C4816)
- [DBMS_CLOUD_OCI_STREAMING_CURSOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-128AF5FA-D565-4D6B-BD7B-D949755276A4)
- [DBMS_CLOUD_OCI_STREAMING_CUSTOM_ENCRYPTION_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-61D0DC5D-0C34-485B-8647-4E8CA78B94FB)
- [DBMS_CLOUD_OCI_STREAMING_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-BBB02CC2-73AB-456A-8CD2-479810560953)
- [DBMS_CLOUD_OCI_STREAMING_PARTITION_RESERVATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-6E7100D7-49E8-4781-843D-7D93CA759A9F)
- [DBMS_CLOUD_OCI_STREAMING_PARTITION_RESERVATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-8E3A3465-61F5-4588-8A02-969361641692)
- [DBMS_CLOUD_OCI_STREAMING_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-CC743D45-B890-4683-A99F-820045915114)
- [DBMS_CLOUD_OCI_STREAMING_MESSAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-4FD2AFE2-94C3-4830-AE27-178FEAB65478)
- [DBMS_CLOUD_OCI_STREAMING_PRIVATE_ENDPOINT_SETTINGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-2BA2AFE1-5BF0-48DD-B9AA-B2E95EF518C3)
- [DBMS_CLOUD_OCI_STREAMING_PUT_MESSAGES_DETAILS_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-ED4DC500-04F8-46B4-95FF-3BBF7CEDD88F)
- [DBMS_CLOUD_OCI_STREAMING_PUT_MESSAGES_DETAILS_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-9A4851DE-2264-40F0-8E4E-509B75A0CD19)
- [DBMS_CLOUD_OCI_STREAMING_PUT_MESSAGES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-0EFAABA5-8705-440C-B875-088E41E15BFE)
- [DBMS_CLOUD_OCI_STREAMING_PUT_MESSAGES_RESULT_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-15592CFA-5884-4FE4-A600-E62FB9EEEFD6)
- [DBMS_CLOUD_OCI_STREAMING_PUT_MESSAGES_RESULT_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-20B8C0B3-D579-449E-89D1-F2AE7BA379F2)
- [DBMS_CLOUD_OCI_STREAMING_PUT_MESSAGES_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-C3AC1FCC-2C9C-49A2-83F0-DDE98C921ECD)
- [DBMS_CLOUD_OCI_STREAMING_STREAM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-CC97F1B5-1D68-4A51-9D9B-6CC6E3C09F96)
- [DBMS_CLOUD_OCI_STREAMING_STREAM_POOL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-3D972CE8-980F-4CBB-9EC8-677A763AB6C9)
- [DBMS_CLOUD_OCI_STREAMING_STREAM_POOL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-235DDE78-5601-4CBC-AF56-8E2AF8860B34)
- [DBMS_CLOUD_OCI_STREAMING_STREAM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-FE4124CF-65EB-4334-A1D4-E1699E912374)
- [DBMS_CLOUD_OCI_STREAMING_UPDATE_CONNECT_HARNESS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-271AACF5-CF83-4376-86DE-10F09DB18477)
- [DBMS_CLOUD_OCI_STREAMING_UPDATE_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-B84B4A35-E139-4542-A884-060A0593D779)
- [DBMS_CLOUD_OCI_STREAMING_UPDATE_STREAM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-31C990C0-8270-4418-BC33-3497070D2196)
- [DBMS_CLOUD_OCI_STREAMING_UPDATE_STREAM_POOL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/streaming_t.html#ADSDK-GUID-27CC1DA8-EBCF-4FB7-B6D4-A07DDA8A489F)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
