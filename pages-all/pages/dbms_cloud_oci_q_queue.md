# Queue Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_q_queue.html
- Fetched: 2026-09-05 19:13 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_q_queue.html#dcoc-content-body)

## Queue Functions

Package: DBMS_CLOUD_OCI_Q_QUEUE

### DELETE_MESSAGE Function

Deletes the message represented by the receipt from the queue. You must use the[messages endpoint](https://docs.oracle.com/iaas/Content/queue/messages.htm#messages__messages-endpoint)to delete messages. The messages endpoint may be different for different queues. Use`GET_QUEUE`Function to find the queue's `messagesEndpoint`.

Syntax
```

```

Parameters

Parameter Description

`queue_id`

(required) The unique queue identifier.

`message_receipt`

(required) The receipt of the message retrieved from a GetMessages call.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://messaging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MESSAGES Function

Deletes multiple messages from the queue. You must use the[messages endpoint](https://docs.oracle.com/iaas/Content/queue/messages.htm#messages__messages-endpoint)to delete messages. The messages endpoint may be different for different queues. Use`GET_QUEUE`Function to find the queue's `messagesEndpoint`.

Syntax
```

```

Parameters

Parameter Description

`queue_id`

(required) The unique queue identifier.

`delete_messages_details`

(required) Details for the messages to delete.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://messaging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MESSAGES Function

Consumes messages from the queue. You must use the[messages endpoint](https://docs.oracle.com/iaas/Content/queue/messages.htm#messages__messages-endpoint)to consume messages. The messages endpoint may be different for different queues. Use`GET_QUEUE`Function to find the queue's `messagesEndpoint`. GetMessages accepts optional channelFilter query parameter that can filter source channels of the messages. When channelFilter is present, service will return available messages from the channel which ID exactly matched the filter. When filter is not specified, messages will be returned from a random non-empty channel within a queue.

Syntax
```

```

Parameters

Parameter Description

`queue_id`

(required) The unique queue identifier.

`visibility_in_seconds`

(optional) If the `visibilityInSeconds` parameter is set, messages will be hidden for `visibilityInSeconds` seconds and won't be consumable by other consumers during that time. If it isn't set it defaults to the value set at the queue level. Using a `visibilityInSeconds` value of 0 effectively acts as a peek functionality. Messages retrieved that way aren't meant to be deleted because they will most likely be delivered to another consumer as their visibility won't change, but will still increase the delivery count by one.

`timeout_in_seconds`

(optional) If the `timeoutInSeconds parameter` isn't set or it is set to a value greater than 0, the request is using the long-polling mode and will only return when a message is available for consumption (it does not wait for limit messages but still only returns at-most limit messages) or after `timeoutInSeconds` seconds (in which case it will return an empty response), whichever comes first. If the parameter is set to 0, the request is using the short-polling mode and immediately returns whether messages have been retrieved or not. In same rare-cases a long-polling request could be interrupted (returned with empty response) before the end of the timeout.

`limit`

(optional) The limit parameter controls how many messages is returned at-most.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`channel_filter`

(optional) Optional parameter to filter the channels.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://messaging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_STATS Function

Gets the statistics for the queue and its dead letter queue. You must use the[messages endpoint](https://docs.oracle.com/iaas/Content/queue/messages.htm#messages__messages-endpoint)to get a queue's statistics. The messages endpoint may be different for different queues. Use`GET_QUEUE`Function to find the queue's `messagesEndpoint`.

Syntax
```

```

Parameters

Parameter Description

`queue_id`

(required) The unique queue identifier.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`channel_id`

(optional) Id to specify channel.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://messaging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CHANNELS Function

Gets the list of IDs of non-empty channels. It will return an approximate list of IDs of non-empty channels. That information is based on the queue level statistics. API supports optional channelFilter parameter which will filter the returned results according to the specified filter. List of channel IDs is approximate, because statistics is refreshed once per-second, and that list represents a snapshot of the past information. API is paginated.

Syntax
```

```

Parameters

Parameter Description

`queue_id`

(required) The unique queue identifier.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the opc-next-page response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`channel_filter`

(optional) Optional parameter to filter the channels.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://messaging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PUT_MESSAGES Function

Puts messages into the queue. You must use the[messages endpoint](https://docs.oracle.com/iaas/Content/queue/messages.htm#messages__messages-endpoint)to produce messages. The messages endpoint may be different for different queues. Use`GET_QUEUE`Function to find the queue's `messagesEndpoint`.

Syntax
```

```

Parameters

Parameter Description

`queue_id`

(required) The unique queue identifier.

`put_messages_details`

(required) Details for the messages to publish.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://messaging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MESSAGE Function

Updates the visibility of the message represented by the receipt. You must use the[messages endpoint](https://docs.oracle.com/iaas/Content/queue/messages.htm#messages__messages-endpoint)to update messages. The messages endpoint may be different for different queues. Use`GET_QUEUE`Function to find the queue's `messagesEndpoint`.

Syntax
```

```

Parameters

Parameter Description

`queue_id`

(required) The unique queue identifier.

`message_receipt`

(required) The receipt of the message retrieved from a GetMessages call.

`update_message_details`

(required) Details for the message to update.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://messaging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MESSAGES Function

Updates multiple messages in the queue. You must use the[messages endpoint](https://docs.oracle.com/iaas/Content/queue/messages.htm#messages__messages-endpoint)to update messages. The messages endpoint may be different for different queues. Use`GET_QUEUE`Function to find the queue's `messagesEndpoint`.

Syntax
```

```

Parameters

Parameter Description

`queue_id`

(required) The unique queue identifier.

`update_messages_details`

(required) Details for the messages to update.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://messaging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Queue Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_q_queue.html#ADSDK-GUID-63A4BB1D-2A4F-49F3-8C18-FC0252749148)
- [DELETE_MESSAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_q_queue.html#ADSDK-GUID-853616EE-612D-4272-AD9D-C651153DCA41)
- [DELETE_MESSAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_q_queue.html#ADSDK-GUID-AECAAD80-CF47-4457-8B42-9D89C8E39320)
- [GET_MESSAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_q_queue.html#ADSDK-GUID-7D2DFEBB-33E0-4393-AA28-7B4D3E44A7B6)
- [GET_STATS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_q_queue.html#ADSDK-GUID-F81079EC-DE79-4477-A58F-B323CA928BEE)
- [LIST_CHANNELS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_q_queue.html#ADSDK-GUID-94681811-BD7B-4525-BFA3-09F7AEDC7ADE)
- [PUT_MESSAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_q_queue.html#ADSDK-GUID-28DF7691-4908-4BA4-A089-E07B6ED09C0C)
- [UPDATE_MESSAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_q_queue.html#ADSDK-GUID-73C26CE4-3E9D-406B-BDB2-04A3A138B1F7)
- [UPDATE_MESSAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_q_queue.html#ADSDK-GUID-EA9A29AF-8BE5-4B59-9025-D92D40636D1A)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
