# API Gateway Usage Plans Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_usage_plans.html
- Fetched: 2026-09-05 19:03 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_usage_plans.html#dcoc-content-body)

## API Gateway Usage Plans Functions

Package: DBMS_CLOUD_OCI_AG_USAGE_PLANS

### CHANGE_USAGE_PLAN_COMPARTMENT Function

Changes the usage plan compartment.

Syntax
```

```

Parameters

Parameter Description

`usage_plan_id`

(required) The ocid of the usage plan.

`change_usage_plan_compartment_details`

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

### CREATE_USAGE_PLAN Function

Creates a new usage plan.

Syntax
```

```

Parameters

Parameter Description

`create_usage_plan_details`

(required) Details for the new usage plan.

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

### DELETE_USAGE_PLAN Function

Deletes the usage plan with the given identifier.

Syntax
```

```

Parameters

Parameter Description

`usage_plan_id`

(required) The ocid of the usage plan.

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

### GET_USAGE_PLAN Function

Gets a usage plan by identifier.

Syntax
```

```

Parameters

Parameter Description

`usage_plan_id`

(required) The ocid of the usage plan.

`opc_request_id`

(optional) The client request id for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apigateway.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_USAGE_PLANS Function

Returns a list of usage plans.

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

### UPDATE_USAGE_PLAN Function

Updates the usage plan with the given identifier.

Syntax
```

```

Parameters

Parameter Description

`usage_plan_id`

(required) The ocid of the usage plan.

`update_usage_plan_details`

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

- [API Gateway Usage Plans Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_usage_plans.html#ADSDK-GUID-9E5C0EF7-59D2-46D4-BD28-E33B4A6D04D0)
- [CHANGE_USAGE_PLAN_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_usage_plans.html#ADSDK-GUID-33C43520-F2C4-4256-88E5-B790AB0EDE1E)
- [CREATE_USAGE_PLAN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_usage_plans.html#ADSDK-GUID-42DF2B17-E742-41BE-A9E1-6BA2A2D800D4)
- [DELETE_USAGE_PLAN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_usage_plans.html#ADSDK-GUID-1A7FE41F-1DE4-4B3A-9E1A-85854DEEA783)
- [GET_USAGE_PLAN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_usage_plans.html#ADSDK-GUID-7DC9325F-4425-4D59-9017-90DF37E55F0E)
- [LIST_USAGE_PLANS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_usage_plans.html#ADSDK-GUID-83568A33-385E-4DC3-899C-B9FF82DF36A0)
- [UPDATE_USAGE_PLAN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_usage_plans.html#ADSDK-GUID-AB43ECBA-083C-4FF6-A601-2DD4CC90D16D)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
