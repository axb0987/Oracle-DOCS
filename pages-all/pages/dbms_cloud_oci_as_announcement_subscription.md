# Announcements Subscription Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcement_subscription.html
- Fetched: 2026-09-05 19:04 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcement_subscription.html#dcoc-content-body)

## Announcements Subscription Functions

Package: DBMS_CLOUD_OCI_AS_ANNOUNCEMENT_SUBSCRIPTION

### CHANGE_ANNOUNCEMENT_SUBSCRIPTION_COMPARTMENT Function

Moves the specified announcement subscription from one compartment to another compartment. When provided, If-Match is checked against ETag values of the resource. This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`announcement_subscription_id`

(required) The OCID of the announcement subscription.

`change_announcement_subscription_compartment_details`

(required) The compartment information to update.

`if_match`

(optional) The locking version, used for optimistic concurrency control.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the complete request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://announcements.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ANNOUNCEMENT_SUBSCRIPTION Function

Creates a new announcement subscription. This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`create_announcement_subscription_details`

(required) Details of the new announcement subscription.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the complete request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://announcements.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_FILTER_GROUP Function

Creates a new filter group in the specified announcement subscription. This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`announcement_subscription_id`

(required) The OCID of the announcement subscription.

`create_filter_group_details`

(required) Details of the new filter group.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the complete request ID.

`if_match`

(optional) The locking version, used for optimistic concurrency control.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://announcements.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ANNOUNCEMENT_SUBSCRIPTION Function

Deletes the specified announcement subscription. This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`announcement_subscription_id`

(required) The OCID of the announcement subscription.

`if_match`

(optional) The locking version, used for optimistic concurrency control.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the complete request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://announcements.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_FILTER_GROUP Function

Deletes a filter group in the specified announcement subscription. This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`announcement_subscription_id`

(required) The OCID of the announcement subscription.

`filter_group_name`

(required) The name of the filter group.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the complete request ID.

`if_match`

(optional) The locking version, used for optimistic concurrency control.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://announcements.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ANNOUNCEMENT_SUBSCRIPTION Function

Gets the specified announcement subscription. This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`announcement_subscription_id`

(required) The OCID of the announcement subscription.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the complete request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://announcements.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ANNOUNCEMENT_SUBSCRIPTIONS Function

Gets a list of all announcement subscriptions in the specified compartment. This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`lifecycle_state`

(optional) A filter to return only announcement subscriptions that match the given lifecycle state.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`id`

(optional) The OCID of the announcement subscription.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`sort_order`

(optional) The sort order to use, whether ascending ('ASC') or descending ('DESC').

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The criteria to sort by. You can specify only one sort order. The default sort order for the creation date of resources is descending. The default sort order for display names is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the complete request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://announcements.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ANNOUNCEMENT_SUBSCRIPTION Function

Updates the specified announcement subscription. This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`announcement_subscription_id`

(required) The OCID of the announcement subscription.

`update_announcement_subscription_details`

(required) The subscription information to update.

`if_match`

(optional) The locking version, used for optimistic concurrency control.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the complete request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://announcements.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_FILTER_GROUP Function

Updates a filter group in the specified announcement subscription. This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`announcement_subscription_id`

(required) The OCID of the announcement subscription.

`filter_group_name`

(required) The name of the filter group.

`update_filter_group_details`

(required) The filter group information to update.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the complete request ID.

`if_match`

(optional) The locking version, used for optimistic concurrency control.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://announcements.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Announcements Subscription Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcement_subscription.html#ADSDK-GUID-90A1F8F0-CB58-4CB3-83B6-6835B3501E9F)
- [CHANGE_ANNOUNCEMENT_SUBSCRIPTION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcement_subscription.html#ADSDK-GUID-0B203F97-018F-45B3-A11A-10440F4F6E46)
- [CREATE_ANNOUNCEMENT_SUBSCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcement_subscription.html#ADSDK-GUID-A1439EF4-28D9-4417-98BC-D66E53CDA3F4)
- [CREATE_FILTER_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcement_subscription.html#ADSDK-GUID-BBDA0AE3-39CB-40E3-BB0A-1CC336B0E1A2)
- [DELETE_ANNOUNCEMENT_SUBSCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcement_subscription.html#ADSDK-GUID-07F7291D-EAD5-400D-BF35-336BC31E7F0D)
- [DELETE_FILTER_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcement_subscription.html#ADSDK-GUID-24E28572-611D-4FE3-8BD2-3630C830182C)
- [GET_ANNOUNCEMENT_SUBSCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcement_subscription.html#ADSDK-GUID-A2EBD332-87A5-4826-B3A4-04C9205CEEA7)
- [LIST_ANNOUNCEMENT_SUBSCRIPTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcement_subscription.html#ADSDK-GUID-4136E732-9D8B-43A4-AD25-C5F7874B0561)
- [UPDATE_ANNOUNCEMENT_SUBSCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcement_subscription.html#ADSDK-GUID-14F429E8-272C-487D-B91E-45BEB35ED91F)
- [UPDATE_FILTER_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcement_subscription.html#ADSDK-GUID-F2D7493A-6869-48C9-A3AC-F529195D99F1)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
