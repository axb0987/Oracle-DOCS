# Streaming Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream.html
- Fetched: 2026-09-05 19:14 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream.html#dcoc-content-body)

## Streaming Functions

Package: DBMS_CLOUD_OCI_ST_STREAM

### CONSUMER_COMMIT Function

Provides a mechanism to manually commit offsets, if not using commit-on-get consumer semantics. This commits offsets assicated with the provided cursor, extends the timeout on each of the affected partitions, and returns an updated cursor.

Syntax
```

```

Parameters

Parameter Description

`stream_id`

(required) The OCID of the stream.

`l_cursor`

(required) The group-cursor representing the offsets of the group. This cursor is retrieved from the CreateGroupCursor API call.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CONSUMER_HEARTBEAT Function

Allows long-running processes to extend the timeout on partitions reserved by a consumer instance.

Syntax
```

```

Parameters

Parameter Description

`stream_id`

(required) The OCID of the stream.

`l_cursor`

(required) The group-cursor representing the offsets of the group. This cursor is retrieved from the CreateGroupCursor API call.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CURSOR Function

Creates a cursor. Cursors are used to consume a stream, starting from a specific point in the partition and going forward from there. You can create a cursor based on an offset, a time, the trim horizon, or the most recent message in the stream. As the oldest message inside the retention period boundary, using the trim horizon effectively lets you consume all messages in the stream. A cursor based on the most recent message allows consumption of only messages that are added to the stream after you create the cursor. Cursors expire five minutes after you receive them from the service.

Syntax
```

```

Parameters

Parameter Description

`stream_id`

(required) The OCID of the stream.

`create_cursor_details`

(required) The information used to create the cursor.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_GROUP_CURSOR Function

Creates a group-cursor.

Syntax
```

```

Parameters

Parameter Description

`stream_id`

(required) The OCID of the stream.

`create_group_cursor_details`

(required) The information used to create the cursor.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_GROUP Function

Returns the current state of a consumer group.

Syntax
```

```

Parameters

Parameter Description

`stream_id`

(required) The OCID of the stream.

`group_name`

(required) The name of the consumer group.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MESSAGES Function

Returns messages from the specified stream using the specified cursor as the starting point for consumption. By default, the number of messages returned is undefined, but the service returns as many as possible. To get messages, you must first obtain a cursor using the`CREATE_CURSOR`Function operation. In the response, retrieve the value of the 'opc-next-cursor' header to pass as a parameter to get the next batch of messages in the stream.

Syntax
```

```

Parameters

Parameter Description

`stream_id`

(required) The OCID of the stream.

`l_cursor`

(required) The cursor used to consume the stream.

`limit`

(optional) The maximum number of messages to return. You can specify any value up to 10000. By default, the service returns as many messages as possible. Consider your average message size to help avoid exceeding throughput on the stream.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PUT_MESSAGES Function

Emits messages to a stream. There's no limit to the number of messages in a request, but the total size of a message or request must be 1 MiB or less. The service calculates the partition ID from the message key and stores messages that share a key on the same partition. If a message does not contain a key or if the key is null, the service generates a message key for you. The partition ID cannot be passed as a parameter.

Syntax
```

```

Parameters

Parameter Description

`stream_id`

(required) The OCID of the stream.

`put_messages_details`

(required) Array of messages to put into the stream.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_GROUP Function

Forcefully changes the current location of a group as a whole; reseting processing location of all consumers to a particular location in the stream.

Syntax
```

```

Parameters

Parameter Description

`stream_id`

(required) The OCID of the stream.

`group_name`

(required) The name of the consumer group.

`update_group_details`

(required) The information used to modify the group.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://streaming.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Streaming Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream.html#ADSDK-GUID-B4E25334-D470-4A90-88EA-E9B30FB12DB9)
- [CONSUMER_COMMIT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream.html#ADSDK-GUID-D571B524-F588-4266-A6A1-B9CA984D281C)
- [CONSUMER_HEARTBEAT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream.html#ADSDK-GUID-893DCBBD-BA27-45F7-B533-32D9071415E4)
- [CREATE_CURSOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream.html#ADSDK-GUID-F1170695-DC9F-4E99-8FBF-820008D2EC16)
- [CREATE_GROUP_CURSOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream.html#ADSDK-GUID-5576954F-3896-4B2D-9015-ED985EB61498)
- [GET_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream.html#ADSDK-GUID-D4A2A4AB-2C27-449C-85AB-66B07E8F57F5)
- [GET_MESSAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream.html#ADSDK-GUID-27A9C287-086E-4487-A2C3-606E0B5B0BB4)
- [PUT_MESSAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream.html#ADSDK-GUID-F5AD3333-42A4-4DDF-B25B-CD85CE2266DF)
- [UPDATE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_st_stream.html#ADSDK-GUID-B77326F8-FE0F-400C-84E2-0DA9556AD096)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
