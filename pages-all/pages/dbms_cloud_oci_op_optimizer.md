# Optimizer Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html
- Fetched: 2026-09-05 19:12 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#dcoc-content-body)

## Optimizer Functions

Package: DBMS_CLOUD_OCI_OP_OPTIMIZER

### BULK_APPLY_RECOMMENDATIONS Function

Applies the specified recommendations to the resources.

Syntax
```

```

Parameters

Parameter Description

`recommendation_id`

(required) The unique OCID associated with the recommendation.

`bulk_apply_recommendations_details`

(required) Details about bulk recommendation actions.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PROFILE Function

Creates a new profile.

Syntax
```

```

Parameters

Parameter Description

`create_profile_details`

(required) Details for creating the profile.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PROFILE Function

Deletes the specified profile. Uses the profile's OCID to determine which profile to delete.

Syntax
```

```

Parameters

Parameter Description

`profile_id`

(required) The unique OCID of the profile.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### FILTER_RESOURCE_ACTIONS Function

Queries the Cloud Advisor resource actions that are supported.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`compartment_id_in_subtree`

(required) When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`. Can only be set to true when performing ListCompartments on the tenancy (root compartment).

`query_details`

(required) The request parameters that describe the query criteria.

`recommendation_id`

(optional) The unique OCID associated with the recommendation.

`recommendation_name`

(optional) Optional. A filter that returns results that match the recommendation name specified.

`child_tenancy_ids`

(optional) A list of child tenancies for which the respective data will be returned. Please note that the parent tenancy id can also be included in this list. For example, if there is a parent P with two children A and B, to return results of only parent P and child A, this list should be populated with tenancy id of parent P and child A. If this list contains a tenancy id that isn't part of the organization of parent P, the request will fail. That is, let's say there is an organization with parent P with children A and B, and also one other tenant T that isn't part of the organization. If T is included in the list of childTenancyIds, the request will fail. It is important to note that if you are setting the includeOrganization parameter value as true and also populating the childTenancyIds parameter with a list of child tenancies, the request will fail. The childTenancyIds and includeOrganization should be used exclusively. When using this parameter, please make sure to set the compartmentId with the parent tenancy ID.

`include_organization`

(optional) When set to true, the data for all child tenancies including the parent is returned. That is, if there is an organization with parent P and children A and B, to return the data for the parent P, child A and child B, this parameter value should be set to true. Please note that this parameter shouldn't be used along with childTenancyIds parameter. If you would like to get results specifically for parent P and only child A, use the childTenancyIds parameter and populate the list with tenancy id of P and A. When using this parameter, please make sure to set the compartmentId with the parent tenancy ID.

`include_resource_metadata`

(optional) Supplement additional resource information in extended metadata response.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CATEGORY Function

Gets the category that corresponds to the specified OCID.

Syntax
```

```

Parameters

Parameter Description

`category_id`

(required) The unique OCID associated with the category.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ENROLLMENT_STATUS Function

Gets the Cloud Advisor enrollment status.

Syntax
```

```

Parameters

Parameter Description

`enrollment_status_id`

(required) The unique OCID associated with the enrollment status.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PROFILE Function

Gets the specified profile's information. Uses the profile's OCID to determine which profile to retrieve.

Syntax
```

```

Parameters

Parameter Description

`profile_id`

(required) The unique OCID of the profile.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_RECOMMENDATION Function

Gets the recommendation for the specified OCID.

Syntax
```

```

Parameters

Parameter Description

`recommendation_id`

(required) The unique OCID associated with the recommendation.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_RESOURCE_ACTION Function

Gets the resource action that corresponds to the specified OCID.

Syntax
```

```

Parameters

Parameter Description

`resource_action_id`

(required) The unique OCID associated with the resource action.

`include_resource_metadata`

(optional) Supplement additional resource information in extended metadata response.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets the status of the work request associated with the specified ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the work request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CATEGORIES Function

Lists the supported Cloud Advisor categories.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`compartment_id_in_subtree`

(required) When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`. Can only be set to true when performing ListCompartments on the tenancy (root compartment).

`child_tenancy_ids`

(optional) A list of child tenancies for which the respective data will be returned. Please note that the parent tenancy id can also be included in this list. For example, if there is a parent P with two children A and B, to return results of only parent P and child A, this list should be populated with tenancy id of parent P and child A. If this list contains a tenancy id that isn't part of the organization of parent P, the request will fail. That is, let's say there is an organization with parent P with children A and B, and also one other tenant T that isn't part of the organization. If T is included in the list of childTenancyIds, the request will fail. It is important to note that if you are setting the includeOrganization parameter value as true and also populating the childTenancyIds parameter with a list of child tenancies, the request will fail. The childTenancyIds and includeOrganization should be used exclusively. When using this parameter, please make sure to set the compartmentId with the parent tenancy ID.

`include_organization`

(optional) When set to true, the data for all child tenancies including the parent is returned. That is, if there is an organization with parent P and children A and B, to return the data for the parent P, child A and child B, this parameter value should be set to true. Please note that this parameter shouldn't be used along with childTenancyIds parameter. If you would like to get results specifically for parent P and only child A, use the childTenancyIds parameter and populate the list with tenancy id of P and A. When using this parameter, please make sure to set the compartmentId with the parent tenancy ID.

`name`

(optional) Optional. A filter that returns results that match the name specified.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.

Allowed values are: 'NAME', 'TIMECREATED'

`lifecycle_state`

(optional) A filter that returns results that match the lifecycle state specified.

Allowed values are: 'ACTIVE', 'FAILED', 'INACTIVE', 'ATTACHING', 'DETACHING', 'DELETING', 'DELETED', 'UPDATING', 'CREATING'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ENROLLMENT_STATUSES Function

Lists the Cloud Advisor enrollment statuses.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.

Allowed values are: 'NAME', 'TIMECREATED'

`lifecycle_state`

(optional) A filter that returns results that match the lifecycle state specified.

Allowed values are: 'ACTIVE', 'FAILED', 'INACTIVE', 'ATTACHING', 'DETACHING', 'DELETING', 'DELETED', 'UPDATING', 'CREATING'

`status`

(optional) A filter that returns results that match the Cloud Advisor enrollment status specified.

Allowed values are: 'ACTIVE', 'INACTIVE'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_HISTORIES Function

Lists changes to the recommendations based on user activity. For example, lists when recommendations have been implemented, dismissed, postponed, or reactivated.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`compartment_id_in_subtree`

(required) When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`. Can only be set to true when performing ListCompartments on the tenancy (root compartment).

`name`

(optional) Optional. A filter that returns results that match the name specified.

`recommendation_name`

(optional) Optional. A filter that returns results that match the recommendation name specified.

`recommendation_id`

(optional) The unique OCID associated with the recommendation.

`resource_type`

(optional) Optional. A filter that returns results that match the resource type specified.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.

Allowed values are: 'NAME', 'TIMECREATED'

`lifecycle_state`

(optional) A filter that returns results that match the lifecycle state specified.

Allowed values are: 'ACTIVE', 'FAILED', 'INACTIVE', 'ATTACHING', 'DETACHING', 'DELETING', 'DELETED', 'UPDATING', 'CREATING'

`status`

(optional) A filter that returns recommendations that match the status specified.

Allowed values are: 'PENDING', 'DISMISSED', 'POSTPONED', 'IMPLEMENTED'

`include_resource_metadata`

(optional) Supplement additional resource information in extended metadata response.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PROFILE_LEVELS Function

Lists the existing profile levels.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`compartment_id_in_subtree`

(required) When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`. Can only be set to true when performing ListCompartments on the tenancy (root compartment).

`name`

(optional) Optional. A filter that returns results that match the name specified.

`recommendation_name`

(optional) Optional. A filter that returns results that match the recommendation name specified.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.

Allowed values are: 'NAME', 'TIMECREATED'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PROFILES Function

Lists the existing profiles.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`name`

(optional) Optional. A filter that returns results that match the name specified.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.

Allowed values are: 'NAME', 'TIMECREATED'

`lifecycle_state`

(optional) A filter that returns results that match the lifecycle state specified.

Allowed values are: 'ACTIVE', 'FAILED', 'INACTIVE', 'ATTACHING', 'DETACHING', 'DELETING', 'DELETED', 'UPDATING', 'CREATING'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RECOMMENDATION_STRATEGIES Function

Lists the existing strategies.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`compartment_id_in_subtree`

(required) When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`. Can only be set to true when performing ListCompartments on the tenancy (root compartment).

`name`

(optional) Optional. A filter that returns results that match the name specified.

`recommendation_name`

(optional) Optional. A filter that returns results that match the recommendation name specified.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.

Allowed values are: 'NAME', 'TIMECREATED'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RECOMMENDATIONS Function

Lists the Cloud Advisor recommendations that are currently supported.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`compartment_id_in_subtree`

(required) When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`. Can only be set to true when performing ListCompartments on the tenancy (root compartment).

`category_id`

(optional) The unique OCID associated with the category.

`category_name`

(optional) Optional. A filter that returns results that match the category name specified.

`child_tenancy_ids`

(optional) A list of child tenancies for which the respective data will be returned. Please note that the parent tenancy id can also be included in this list. For example, if there is a parent P with two children A and B, to return results of only parent P and child A, this list should be populated with tenancy id of parent P and child A. If this list contains a tenancy id that isn't part of the organization of parent P, the request will fail. That is, let's say there is an organization with parent P with children A and B, and also one other tenant T that isn't part of the organization. If T is included in the list of childTenancyIds, the request will fail. It is important to note that if you are setting the includeOrganization parameter value as true and also populating the childTenancyIds parameter with a list of child tenancies, the request will fail. The childTenancyIds and includeOrganization should be used exclusively. When using this parameter, please make sure to set the compartmentId with the parent tenancy ID.

`include_organization`

(optional) When set to true, the data for all child tenancies including the parent is returned. That is, if there is an organization with parent P and children A and B, to return the data for the parent P, child A and child B, this parameter value should be set to true. Please note that this parameter shouldn't be used along with childTenancyIds parameter. If you would like to get results specifically for parent P and only child A, use the childTenancyIds parameter and populate the list with tenancy id of P and A. When using this parameter, please make sure to set the compartmentId with the parent tenancy ID.

`name`

(optional) Optional. A filter that returns results that match the name specified.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.

Allowed values are: 'NAME', 'TIMECREATED'

`lifecycle_state`

(optional) A filter that returns results that match the lifecycle state specified.

Allowed values are: 'ACTIVE', 'FAILED', 'INACTIVE', 'ATTACHING', 'DETACHING', 'DELETING', 'DELETED', 'UPDATING', 'CREATING'

`status`

(optional) A filter that returns recommendations that match the status specified.

Allowed values are: 'PENDING', 'DISMISSED', 'POSTPONED', 'IMPLEMENTED'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RESOURCE_ACTION_QUERYABLE_FIELDS Function

Lists the fields that are indexed for querying and their associated value types.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`compartment_id_in_subtree`

(required) When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`. Can only be set to true when performing ListCompartments on the tenancy (root compartment).

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RESOURCE_ACTIONS Function

Lists the Cloud Advisor resource actions that are supported.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`compartment_id_in_subtree`

(required) When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`. Can only be set to true when performing ListCompartments on the tenancy (root compartment).

`recommendation_id`

(optional) The unique OCID associated with the recommendation.

`recommendation_name`

(optional) Optional. A filter that returns results that match the recommendation name specified.

`child_tenancy_ids`

(optional) A list of child tenancies for which the respective data will be returned. Please note that the parent tenancy id can also be included in this list. For example, if there is a parent P with two children A and B, to return results of only parent P and child A, this list should be populated with tenancy id of parent P and child A. If this list contains a tenancy id that isn't part of the organization of parent P, the request will fail. That is, let's say there is an organization with parent P with children A and B, and also one other tenant T that isn't part of the organization. If T is included in the list of childTenancyIds, the request will fail. It is important to note that if you are setting the includeOrganization parameter value as true and also populating the childTenancyIds parameter with a list of child tenancies, the request will fail. The childTenancyIds and includeOrganization should be used exclusively. When using this parameter, please make sure to set the compartmentId with the parent tenancy ID.

`include_organization`

(optional) When set to true, the data for all child tenancies including the parent is returned. That is, if there is an organization with parent P and children A and B, to return the data for the parent P, child A and child B, this parameter value should be set to true. Please note that this parameter shouldn't be used along with childTenancyIds parameter. If you would like to get results specifically for parent P and only child A, use the childTenancyIds parameter and populate the list with tenancy id of P and A. When using this parameter, please make sure to set the compartmentId with the parent tenancy ID.

`name`

(optional) Optional. A filter that returns results that match the name specified.

`resource_type`

(optional) Optional. A filter that returns results that match the resource type specified.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.

Allowed values are: 'NAME', 'TIMECREATED'

`lifecycle_state`

(optional) A filter that returns results that match the lifecycle state specified.

Allowed values are: 'ACTIVE', 'FAILED', 'INACTIVE', 'ATTACHING', 'DETACHING', 'DELETING', 'DELETED', 'UPDATING', 'CREATING'

`status`

(optional) A filter that returns recommendations that match the status specified.

Allowed values are: 'PENDING', 'DISMISSED', 'POSTPONED', 'IMPLEMENTED'

`include_resource_metadata`

(optional) Supplement additional resource information in extended metadata response.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Lists errors associated with the specified work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the work request.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Lists the logs associated with the specified work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the work request.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

Lists the work requests in the tenancy. The tenancy is the root compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ENROLLMENT_STATUS Function

Updates the enrollment status of the tenancy.

Syntax
```

```

Parameters

Parameter Description

`enrollment_status_id`

(required) The unique OCID associated with the enrollment status.

`update_enrollment_status_details`

(required) The request object for updating the enrollment status.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PROFILE Function

Updates the specified profile. Uses the profile's OCID to determine which profile to update.

Syntax
```

```

Parameters

Parameter Description

`profile_id`

(required) The unique OCID of the profile.

`update_profile_details`

(required) The profile information to use for the update.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_RECOMMENDATION Function

Updates the recommendation that corresponds to the specified OCID. Use this operation to implement the following actions: * Postpone recommendation * Dismiss recommendation * Reactivate recommendation

Syntax
```

```

Parameters

Parameter Description

`recommendation_id`

(required) The unique OCID associated with the recommendation.

`update_recommendation_details`

(required) The request object for updating the recommendation details.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_RESOURCE_ACTION Function

Updates the resource action that corresponds to the specified OCID. Use this operation to implement the following actions: * Postpone resource action * Ignore resource action * Reactivate resource action

Syntax
```

```

Parameters

Parameter Description

`resource_action_id`

(required) The unique OCID associated with the resource action.

`update_resource_action_details`

(required) The resource action information to be updated.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://optimizer.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Optimizer Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-48081BC3-D2B1-4782-B022-52A4A5E2BC96)
- [BULK_APPLY_RECOMMENDATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-9E81F079-7DF0-4CDD-9561-546CDBAE53E8)
- [CREATE_PROFILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-8080BCD1-BD12-40F2-AB9A-2042F30E61B0)
- [DELETE_PROFILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-525440A1-8B80-459E-9ED7-33F1A6459618)
- [FILTER_RESOURCE_ACTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-5D4DC7C8-0666-4424-8EB8-4EF4A3C0E2CC)
- [GET_CATEGORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-BE6B8C28-04E2-467C-B662-DBDA70AC307A)
- [GET_ENROLLMENT_STATUS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-CDB70AC0-414B-46AF-877E-6688B4DAE292)
- [GET_PROFILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-D370FAB0-EB1F-4382-9FE4-2A5B8388C65D)
- [GET_RECOMMENDATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-ECBA5ED4-85F9-4198-B813-19E6367B9FF5)
- [GET_RESOURCE_ACTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-C3F5AC5A-9307-4174-B987-F42B1088756A)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-570C4CA0-5B3A-4A0D-B111-570A06493ED2)
- [LIST_CATEGORIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-F54E56D6-F32A-42EF-829A-EEE785D9FBCA)
- [LIST_ENROLLMENT_STATUSES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-BE0EED8C-741E-4581-834A-E3E1F521DC22)
- [LIST_HISTORIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-5C736BFB-5302-4B70-961B-B249E815C8D3)
- [LIST_PROFILE_LEVELS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-34BADDE3-0F25-47C1-8B54-47CD32935A09)
- [LIST_PROFILES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-F5A9D1C9-AE0F-4FF8-A4A6-E4DCB966AB2A)
- [LIST_RECOMMENDATION_STRATEGIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-02844BF0-A4DD-419F-9375-F97110463014)
- [LIST_RECOMMENDATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-F6158873-058B-4105-AA18-96919812A45E)
- [LIST_RESOURCE_ACTION_QUERYABLE_FIELDS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-4F9D6F92-D00B-499D-A7CB-6A2C63A841F7)
- [LIST_RESOURCE_ACTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-E8A0AB69-34C6-4B7E-A8FA-7CADD30AE08B)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-B69D7D0F-29D0-49E2-9F3C-31D65986653B)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-79CD95C0-8C8E-49DE-91D1-91B111ED4928)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-72F9C0B4-7328-443F-B5AC-0E2F86BE2CBF)
- [UPDATE_ENROLLMENT_STATUS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-02669FD0-6EB1-4FDB-B69A-2447F6280FC8)
- [UPDATE_PROFILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-8248ECEE-A55C-4010-B32A-B6B6E2E1CD40)
- [UPDATE_RECOMMENDATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-59A1931C-AC01-4408-971F-9B5E873B91FD)
- [UPDATE_RESOURCE_ACTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_op_optimizer.html#ADSDK-GUID-382DE688-3BC8-4EE6-8266-445D0B9BC74D)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
