# Notifications Data Plane Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ons_notification_data_plane.html
- Fetched: 2026-09-05 19:12 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ons_notification_data_plane.html#dcoc-content-body)

## Notifications Data Plane Functions

Package: DBMS_CLOUD_OCI_ONS_NOTIFICATION_DATA_PLANE

### CHANGE_SUBSCRIPTION_COMPARTMENT Function

Moves a subscription into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes). Transactions Per Minute (TPM) per-tenancy limit for this operation: 60.

Syntax
```

```

Parameters

Parameter Description

`subscription_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subscription to move.

`change_subscription_compartment_details`

(required) The configuration details for the move operation.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before that due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) Used for optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://notification.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SUBSCRIPTION Function

Creates a subscription for the specified topic and sends a subscription confirmation URL to the endpoint. The subscription remains in \"Pending\" status until it has been confirmed. Transactions Per Minute (TPM) per-tenancy limit for this operation: 60.

Syntax
```

```

Parameters

Parameter Description

`create_subscription_details`

(required) The subscription to create.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before that due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://notification.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SUBSCRIPTION Function

Deletes the specified subscription. Transactions Per Minute (TPM) per-tenancy limit for this operation: 60.

Syntax
```

```

Parameters

Parameter Description

`subscription_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subscription to delete.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) Used for optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://notification.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CONFIRM_SUBSCRIPTION Function

Gets the confirmation details for the specified subscription. Transactions Per Minute (TPM) per-tenancy limit for this operation: 60.

Syntax
```

```

Parameters

Parameter Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subscription to get the confirmation details for.

`token`

(required) The subscription confirmation token.

`protocol`

(required) The protocol used for the subscription. Allowed values: * `CUSTOM_HTTPS` * `EMAIL` * `HTTPS` (deprecated; for PagerDuty endpoints, use `PAGERDUTY`) * `ORACLE_FUNCTIONS` * `PAGERDUTY` * `SLACK` * `SMS` .

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://notification.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SUBSCRIPTION Function

Gets the specified subscription's configuration information. Transactions Per Minute (TPM) per-tenancy limit for this operation: 60.

Syntax
```

```

Parameters

Parameter Description

`subscription_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subscription to retrieve.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://notification.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_UNSUBSCRIPTION Function

Unsubscribes the subscription from the topic. Transactions Per Minute (TPM) per-tenancy limit for this operation: 60.

Syntax
```

```

Parameters

Parameter Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subscription to unsubscribe from.

`token`

(required) The subscription confirmation token.

`protocol`

(required) The protocol used for the subscription. Allowed values: * `CUSTOM_HTTPS` * `EMAIL` * `HTTPS` (deprecated; for PagerDuty endpoints, use `PAGERDUTY`) * `ORACLE_FUNCTIONS` * `PAGERDUTY` * `SLACK` * `SMS` .

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://notification.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SUBSCRIPTIONS Function

Lists the subscriptions in the specified compartment or topic. Transactions Per Minute (TPM) per-tenancy limit for this operation: 60.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`topic_id`

(optional) Return all subscriptions that are subscribed to the given topic OCID. Either this query parameter or the compartmentId query parameter must be set.

`page`

(optional) For list pagination. The value of the opc-next-page response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://notification.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PUBLISH_MESSAGE Function

Publishes a message to the specified topic. The topic endpoint is required for this operation. To get the topic endpoint, use`GET_TOPIC`Function and review the `apiEndpoint` value in the response (`NOTIFICATION_TOPIC`Type). Limits information follows. Message size limit per request: 64KB. Message delivery rate limit per endpoint: 60 messages per minute for HTTP-based protocols, 10 messages per minute for the `EMAIL` protocol. HTTP-based protocols use URL endpoints that begin with \"http:\" or \"https:\". Transactions Per Minute (TPM) per-tenancy limit for this operation: 60 per topic. (This TPM limit represents messages per minute.) For more information about publishing messages, see[Publishing Messages](https://docs.oracle.com/iaas/Content/Notification/Tasks/publishingmessages.htm). For steps to request a limit increase, see[Requesting a Service Limit Increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#three).

Syntax
```

```

Parameters

Parameter Description

`topic_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the topic.

`message_details`

(required) The message to publish.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`message_type`

(optional) **Deprecated.** Support for JSON is deprecated. You can send a JSON payload even when transmitting the payload as a raw string. Configure your receiving system to read the raw payload as JSON format. Type of message body in the request. For `messageType` of JSON, a default key-value pair is required. Example: `{\"default\": \"Alarm breached\", \"Email\": \"Alarm breached: &lt;url&gt;\"}.`

Allowed values are: 'JSON', 'RAW_TEXT'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://notification.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RESEND_SUBSCRIPTION_CONFIRMATION Function

Resends the confirmation details for the specified subscription. Transactions Per Minute (TPM) per-tenancy limit for this operation: 60.

Syntax
```

```

Parameters

Parameter Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subscription to resend the confirmation for.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://notification.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SUBSCRIPTION Function

Updates the specified subscription's configuration. Transactions Per Minute (TPM) per-tenancy limit for this operation: 60.

Syntax
```

```

Parameters

Parameter Description

`subscription_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subscription to update.

`update_subscription_details`

(required) The configuration details for updating the subscription.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) Used for optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://notification.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Notifications Data Plane Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ons_notification_data_plane.html#ADSDK-GUID-CE239787-C2A1-40F8-A021-5EF21F7D27C3)
- [CHANGE_SUBSCRIPTION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ons_notification_data_plane.html#ADSDK-GUID-BB3E3827-CBE0-47FB-8C3F-57FBAAE05A33)
- [CREATE_SUBSCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ons_notification_data_plane.html#ADSDK-GUID-66A9CE7F-A2AC-4D90-8FAB-467064C7A5E8)
- [DELETE_SUBSCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ons_notification_data_plane.html#ADSDK-GUID-27012B60-6423-48C0-B489-2015F2010A0D)
- [GET_CONFIRM_SUBSCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ons_notification_data_plane.html#ADSDK-GUID-96BE0669-021A-4F2F-9658-D46C4FFCAA65)
- [GET_SUBSCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ons_notification_data_plane.html#ADSDK-GUID-3FDFE704-AAB0-426C-93DD-DDF18BB0ABAF)
- [GET_UNSUBSCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ons_notification_data_plane.html#ADSDK-GUID-08A038F9-A593-46B3-815C-0241BBEB753A)
- [LIST_SUBSCRIPTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ons_notification_data_plane.html#ADSDK-GUID-62EE828F-18D0-4807-9A86-4D26BC47B49A)
- [PUBLISH_MESSAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ons_notification_data_plane.html#ADSDK-GUID-B92E0FDF-7451-4141-BC47-30769643ECB2)
- [RESEND_SUBSCRIPTION_CONFIRMATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ons_notification_data_plane.html#ADSDK-GUID-24E5174C-7EF9-4808-83F4-97FB883456DC)
- [UPDATE_SUBSCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ons_notification_data_plane.html#ADSDK-GUID-FD142C79-0DD2-4AA7-8B59-6FDC7856E11E)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
