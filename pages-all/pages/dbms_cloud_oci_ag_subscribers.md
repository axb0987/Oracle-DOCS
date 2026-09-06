# API Gateway Subscribers Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_subscribers.html
- Fetched: 2026-09-05 19:03 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_subscribers.html#dcoc-content-body)

## API Gateway Subscribers Functions

Package: DBMS_CLOUD_OCI_AG_SUBSCRIBERS

### CHANGE_SUBSCRIBER_COMPARTMENT Function

Changes the subscriber compartment.

Syntax
```

```

Parameters

Parameter Description

`subscriber_id`

(required) The ocid of the subscriber.

`change_subscriber_compartment_details`

(required) Details of the target compartment.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request id for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apigateway.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SUBSCRIBER Function

Creates a new subscriber.

Syntax
```

```

Parameters

Parameter Description

`create_subscriber_details`

(required) Details for the new subscriber.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request id for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apigateway.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SUBSCRIBER Function

Deletes the subscriber with the given identifier.

Syntax
```

```

Parameters

Parameter Description

`subscriber_id`

(required) The ocid of the subscriber.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request id for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apigateway.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SUBSCRIBER Function

Gets a subscriber by identifier.

Syntax
```

```

Parameters

Parameter Description

`subscriber_id`

(required) The ocid of the subscriber.

`opc_request_id`

(optional) The client request id for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apigateway.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SUBSCRIBERS Function

Returns a list of subscribers.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ocid of the compartment in which to list resources.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state. Example: `ACTIVE`

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'. The default order depends on the sortBy value.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for `timeCreated` is descending. Default order for `displayName` is ascending. The `displayName` sort order is case sensitive.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request id for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apigateway.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SUBSCRIBER Function

Updates the subscriber with the given identifier.

Syntax
```

```

Parameters

Parameter Description

`subscriber_id`

(required) The ocid of the subscriber.

`update_subscriber_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request id for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apigateway.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [API Gateway Subscribers Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_subscribers.html#ADSDK-GUID-77590E6E-DD6F-429E-AAB3-6E24982539D0)
- [CHANGE_SUBSCRIBER_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_subscribers.html#ADSDK-GUID-8BD5EC91-DC17-4C42-B165-32F78C552FDB)
- [CREATE_SUBSCRIBER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_subscribers.html#ADSDK-GUID-64393811-A373-4F2D-8542-09E498302D7D)
- [DELETE_SUBSCRIBER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_subscribers.html#ADSDK-GUID-00BFCC67-F4CF-440C-9FE7-03A38F3A9A3D)
- [GET_SUBSCRIBER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_subscribers.html#ADSDK-GUID-BE8E0AF3-F8DA-47CD-B6A9-7D7531D34DBC)
- [LIST_SUBSCRIBERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_subscribers.html#ADSDK-GUID-95903B07-3BC1-4089-A8F0-A61B6634A78B)
- [UPDATE_SUBSCRIBER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_subscribers.html#ADSDK-GUID-853CCBF7-35BB-4C34-9C90-86620F4C5056)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
