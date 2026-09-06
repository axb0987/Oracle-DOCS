# Tenant Manager Control Plane Subscription Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_subscription.html
- Fetched: 2026-09-05 19:15 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_subscription.html#dcoc-content-body)

## Tenant Manager Control Plane Subscription Functions

Package: DBMS_CLOUD_OCI_TMCP_SUBSCRIPTION

### CREATE_SUBSCRIPTION_MAPPING Function

Assign the tenancy record identified by the compartment ID to the given subscription ID.

Syntax
```

```

Parameters

Parameter Description

`create_subscription_mapping_details`

(required) Compartment ID and Subscription ID details to create a subscription mapping.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request, so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request will be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SUBSCRIPTION_MAPPING Function

Delete the subscription mapping details by subscription mapping ID.

Syntax
```

```

Parameters

Parameter Description

`subscription_mapping_id`

(required) OCID of the subscription mapping ID.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ASSIGNED_SUBSCRIPTION Function

Get the assigned subscription details by assigned subscription ID.

Syntax
```

```

Parameters

Parameter Description

`assigned_subscription_id`

(required) OCID of the assigned Oracle Cloud Subscription.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SUBSCRIPTION Function

Gets the subscription details by subscription ID.

Syntax
```

```

Parameters

Parameter Description

`subscription_id`

(required) OCID of the subscription.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SUBSCRIPTION_MAPPING Function

Get the subscription mapping details by subscription mapping ID.

Syntax
```

```

Parameters

Parameter Description

`subscription_mapping_id`

(required) OCID of the subscriptionMappingId.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ASSIGNED_SUBSCRIPTION_LINE_ITEMS Function

List line item summaries that a assigned subscription owns.

Syntax
```

```

Parameters

Parameter Description

`assigned_subscription_id`

(required) OCID of the assigned Oracle Cloud Subscription.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use, whether 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. * The default order for timeCreated is descending. * The default order for displayName is ascending. * If no value is specified, timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ASSIGNED_SUBSCRIPTIONS Function

Lists subscriptions that are consumed by the compartment. Only the root compartment is allowed.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`subscription_id`

(optional) The ID of the subscription to which the tenancy is associated.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use, whether 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. * The default order for timeCreated is descending. * The default order for displayName is ascending. * If no value is specified, timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`entity_version`

(optional) The version of the subscription entity.

Allowed values are: 'V1', 'V2'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AVAILABLE_REGIONS Function

List the available regions based on subscription ID.

Syntax
```

```

Parameters

Parameter Description

`subscription_id`

(required) OCID of the subscription.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SUBSCRIPTION_LINE_ITEMS Function

Lists the line items in a subscription.

Syntax
```

```

Parameters

Parameter Description

`subscription_id`

(required) OCID of the subscription.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use, whether 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. * The default order for timeCreated is descending. * The default order for displayName is ascending. * If no value is specified, timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SUBSCRIPTION_MAPPINGS Function

Lists the subscription mappings for all the subscriptions owned by a given compartmentId. Only the root compartment is allowed.

Syntax
```

```

Parameters

Parameter Description

`subscription_id`

(required) OCID of the subscription.

`subscription_mapping_id`

(optional) A unique ID for subscription and tenancy mapping.

`compartment_id`

(optional) The ID of the compartment in which to list resources.

`lifecycle_state`

(optional) The lifecycle state of the resource.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use, whether 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. * The default order for timeCreated is descending. * The default order for displayName is ascending. * If no value is specified, timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SUBSCRIPTIONS Function

List the subscriptions that a compartment owns. Only the root compartment is allowed.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The ID of the compartment in which to list resources.

`subscription_id`

(optional) The ID of the subscription to which the tenancy is associated.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use, whether 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. * The default order for timeCreated is descending. * The default order for displayName is ascending. * If no value is specified, timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`entity_version`

(optional) The version of the subscription entity.

Allowed values are: 'V1', 'V2'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Tenant Manager Control Plane Subscription Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_subscription.html#ADSDK-GUID-5691172A-C3D4-436C-9C5B-1B6E78101A51)
- [CREATE_SUBSCRIPTION_MAPPING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_subscription.html#ADSDK-GUID-7B1F571E-FDAB-4D54-88CE-587A4DAB52DF)
- [DELETE_SUBSCRIPTION_MAPPING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_subscription.html#ADSDK-GUID-1DE48847-9058-46F8-B75B-DBE8C4BC68AD)
- [GET_ASSIGNED_SUBSCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_subscription.html#ADSDK-GUID-57EE4E79-3E51-4D8C-B335-65FC0438DCC3)
- [GET_SUBSCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_subscription.html#ADSDK-GUID-7DA9CB4C-52AF-4564-A27E-7177973F30F9)
- [GET_SUBSCRIPTION_MAPPING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_subscription.html#ADSDK-GUID-B031A3BF-B343-4DB9-8C46-839E3C6D235D)
- [LIST_ASSIGNED_SUBSCRIPTION_LINE_ITEMS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_subscription.html#ADSDK-GUID-05814C49-7E1D-493E-8FA9-FDF6639BF00D)
- [LIST_ASSIGNED_SUBSCRIPTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_subscription.html#ADSDK-GUID-367FADA9-58D5-4372-9F65-F55D95977ECB)
- [LIST_AVAILABLE_REGIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_subscription.html#ADSDK-GUID-9CE838A7-B479-411C-A3B5-E7041D3616D4)
- [LIST_SUBSCRIPTION_LINE_ITEMS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_subscription.html#ADSDK-GUID-B2DA206B-7247-45F5-BE53-796954DD39DF)
- [LIST_SUBSCRIPTION_MAPPINGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_subscription.html#ADSDK-GUID-68019433-2300-4941-8029-D162B3B0B79C)
- [LIST_SUBSCRIPTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_subscription.html#ADSDK-GUID-F2BACC33-0600-4432-9F92-5B364320F989)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
