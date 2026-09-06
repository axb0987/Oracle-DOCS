# OS Management Event Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_event.html
- Fetched: 2026-09-05 19:11 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_event.html#dcoc-content-body)

## OS Management Event Functions

Package: DBMS_CLOUD_OCI_OM_EVENT

### DELETE_EVENT_CONTENT Function

Delete an event content ZIP archive from the service

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) Instance Oracle Cloud identifier (ocid)

`event_id`

(required) Unique Event identifier (OCID)

`compartment_id`

(required) The ID of the compartment in which to list resources.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EVENT Function

Gets an Event by identifier

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) Instance Oracle Cloud identifier (ocid)

`event_id`

(required) Unique Event identifier (OCID)

`compartment_id`

(required) The ID of the compartment in which to list resources.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EVENT_CONTENT Function

Get additional data about a event as a ZIP archive. The archive content depends on the event eventType.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) Instance Oracle Cloud identifier (ocid)

`event_id`

(required) Unique Event identifier (OCID)

`compartment_id`

(required) The ID of the compartment in which to list resources.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EVENT_REPORT Function

Get summary information about events on this instance.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) Instance Oracle Cloud identifier (ocid)

`compartment_id`

(required) The ID of the compartment in which to list resources.

`latest_timestamp_less_than`

(optional) filter event occurrence. Selecting only those last occurred before given date in ISO 8601 format Example: 2017-07-14T02:40:00.000Z

`latest_timestamp_greater_than_or_equal_to`

(optional) filter event occurrence. Selecting only those last occurred on or after given date in ISO 8601 format Example: 2017-07-14T02:40:00.000Z

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EVENTS Function

Returns a list of Events.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) Instance Oracle Cloud identifier (ocid)

`compartment_id`

(required) The ID of the compartment in which to list resources.

`event_id`

(optional) Unique event identifier (OCID)

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing.

`event_type`

(optional) A filter to return only event of given type.

Allowed values are: 'KERNEL_OOPS', 'KERNEL_CRASH', 'CRASH', 'EXPLOIT_ATTEMPT', 'COMPLIANCE', 'TUNING_SUGGESTION', 'TUNING_APPLIED', 'SECURITY', 'ERROR', 'WARNING'

`latest_timestamp_less_than`

(optional) filter event occurrence. Selecting only those last occurred before given date in ISO 8601 format Example: 2017-07-14T02:40:00.000Z

`latest_timestamp_greater_than_or_equal_to`

(optional) filter event occurrence. Selecting only those last occurred on or after given date in ISO 8601 format Example: 2017-07-14T02:40:00.000Z

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RELATED_EVENTS Function

Returns a list of related events. For now pagination is not implemented.

Syntax
```

```

Parameters

Parameter Description

`event_fingerprint`

(required) Event fingerprint identifier

`compartment_id`

(required) The ID of the compartment in which to list resources.

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for id is descending.

Allowed values are: 'instanceId', 'id', 'eventFingerprint'

`latest_timestamp_less_than`

(optional) filter event occurrence. Selecting only those last occurred before given date in ISO 8601 format Example: 2017-07-14T02:40:00.000Z

`latest_timestamp_greater_than_or_equal_to`

(optional) filter event occurrence. Selecting only those last occurred on or after given date in ISO 8601 format Example: 2017-07-14T02:40:00.000Z

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_EVENT Function

Updates an existing event associated to a managed instance

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) Instance Oracle Cloud identifier (ocid)

`event_id`

(required) Unique Event identifier (OCID)

`compartment_id`

(required) The ID of the compartment in which to list resources.

`update_event_details`

(required) Details about the event to update

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPLOAD_EVENT_CONTENT Function

Upload the event content as a ZIP archive from the managed instance to the service

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) Instance Oracle Cloud identifier (ocid)

`event_id`

(required) Unique Event identifier (OCID)

`compartment_id`

(required) The ID of the compartment in which to list resources.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osms.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [OS Management Event Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_event.html#ADSDK-GUID-D1363B9C-C867-4F53-BA53-F19092BE5DD2)
- [DELETE_EVENT_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_event.html#ADSDK-GUID-22F6740F-7CF1-46D5-A70F-4FA6932D39A3)
- [GET_EVENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_event.html#ADSDK-GUID-30BA55E7-6C1D-43CE-8937-4A3D3AA5A2BB)
- [GET_EVENT_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_event.html#ADSDK-GUID-74B04EAF-B2B5-4396-B194-4020FC8B8973)
- [GET_EVENT_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_event.html#ADSDK-GUID-1DC4ED7E-DFF1-4D6E-891F-3A736848F891)
- [LIST_EVENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_event.html#ADSDK-GUID-7EC45EC4-4B5D-4D0B-AC38-3290C2E3CCF8)
- [LIST_RELATED_EVENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_event.html#ADSDK-GUID-B35774F3-8122-432B-A52A-F26565F9C0B2)
- [UPDATE_EVENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_event.html#ADSDK-GUID-D28B6998-EA5E-4C6E-952C-F12BF45E6B65)
- [UPLOAD_EVENT_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_om_event.html#ADSDK-GUID-23F1A1EC-13EC-4E7C-84B5-86269ECC79DF)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
