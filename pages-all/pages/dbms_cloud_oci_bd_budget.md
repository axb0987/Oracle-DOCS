# Budget Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bd_budget.html
- Fetched: 2026-09-05 19:04 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bd_budget.html#dcoc-content-body)

## Budget Functions

Package: DBMS_CLOUD_OCI_BD_BUDGET

### CREATE_ALERT_RULE Function

Creates a new Alert Rule.

Syntax
```

```

Parameters

Parameter Description

`budget_id`

(required) The unique budget OCID.

`create_alert_rule_details`

(required) Details for the new Alert Rule.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usage.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_BUDGET Function

Creates a new budget.

Syntax
```

```

Parameters

Parameter Description

`create_budget_details`

(required) Details for the new budget.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usage.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ALERT_RULE Function

Deletes a specified Alert Rule resource.

Syntax
```

```

Parameters

Parameter Description

`budget_id`

(required) The unique budget OCID.

`alert_rule_id`

(required) The unique Alert Rule OCID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usage.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_BUDGET Function

Deletes a specified budget resource.

Syntax
```

```

Parameters

Parameter Description

`budget_id`

(required) The unique budget OCID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usage.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ALERT_RULE Function

Gets an Alert Rule for a specified budget.

Syntax
```

```

Parameters

Parameter Description

`budget_id`

(required) The unique budget OCID.

`alert_rule_id`

(required) The unique Alert Rule OCID.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usage.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BUDGET Function

Gets a budget by the identifier.

Syntax
```

```

Parameters

Parameter Description

`budget_id`

(required) The unique budget OCID.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usage.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ALERT_RULES Function

Returns a list of Alert Rules for a specified budget.

Syntax
```

```

Parameters

Parameter Description

`budget_id`

(required) The unique budget OCID.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. If not specified, the default is timeCreated. The default sort order for timeCreated is DESC. The default sort order for displayName is ASC in alphanumeric order.

Allowed values are: 'timeCreated', 'displayName'

`lifecycle_state`

(optional) The current state of the resource to filter by.

Allowed values are: 'ACTIVE', 'INACTIVE'

`display_name`

(optional) A user-friendly name. This does not have to be unique, and it's changeable. Example: `My new resource`

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usage.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BUDGETS Function

Gets a list of budgets in a compartment. By default, ListBudgets returns budgets of the 'COMPARTMENT' target type, and the budget records with only one target compartment OCID. To list all budgets, set the targetType query parameter to ALL (for example: 'targetType=ALL'). Clients should ignore new targetTypes, or upgrade to the latest version of the client SDK to handle new targetTypes.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. If not specified, the default is timeCreated. The default sort order for timeCreated is DESC. The default sort order for displayName is ASC in alphanumeric order.

Allowed values are: 'timeCreated', 'displayName'

`lifecycle_state`

(optional) The current state of the resource to filter by.

Allowed values are: 'ACTIVE', 'INACTIVE'

`display_name`

(optional) A user-friendly name. This does not have to be unique, and it's changeable. Example: `My new resource`

`target_type`

(optional) The type of target to filter by: * ALL - List all budgets * COMPARTMENT - List all budgets with targetType == \"COMPARTMENT\" * TAG - List all budgets with targetType == \"TAG\"

Allowed values are: 'ALL', 'COMPARTMENT', 'TAG'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usage.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ALERT_RULE Function

Update an Alert Rule for the budget identified by the OCID.

Syntax
```

```

Parameters

Parameter Description

`budget_id`

(required) The unique budget OCID.

`alert_rule_id`

(required) The unique Alert Rule OCID.

`update_alert_rule_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usage.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_BUDGET Function

Update a budget identified by the OCID.

Syntax
```

```

Parameters

Parameter Description

`budget_id`

(required) The unique budget OCID.

`update_budget_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usage.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Budget Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bd_budget.html#ADSDK-GUID-3BE0917D-CD31-4A3A-AE9C-EB2BAE2585CA)
- [CREATE_ALERT_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bd_budget.html#ADSDK-GUID-C1A61EFD-01B7-4974-8C69-4F513353DDCE)
- [CREATE_BUDGET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bd_budget.html#ADSDK-GUID-04FEE033-C02A-4808-A60E-4F53E81DD2BD)
- [DELETE_ALERT_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bd_budget.html#ADSDK-GUID-A0AFFD5F-57BE-4C5F-8410-BED73C3FBFCE)
- [DELETE_BUDGET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bd_budget.html#ADSDK-GUID-2CCFE73F-DCE9-4AB1-A2CA-8EC1AA917E9B)
- [GET_ALERT_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bd_budget.html#ADSDK-GUID-8E9FB355-115A-4006-BE76-9CE2411B26A6)
- [GET_BUDGET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bd_budget.html#ADSDK-GUID-3F8405C3-AADF-416C-B963-0AABA7A2BD5E)
- [LIST_ALERT_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bd_budget.html#ADSDK-GUID-6EAB74BE-A450-47BB-BC52-BFA599E29213)
- [LIST_BUDGETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bd_budget.html#ADSDK-GUID-FD243851-0A07-47AC-80F0-A18C9E77E494)
- [UPDATE_ALERT_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bd_budget.html#ADSDK-GUID-F9214363-6FF9-4656-8BBF-A319DD479083)
- [UPDATE_BUDGET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_bd_budget.html#ADSDK-GUID-96F7D7D7-4A26-4C77-A7F0-1D956291550A)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
