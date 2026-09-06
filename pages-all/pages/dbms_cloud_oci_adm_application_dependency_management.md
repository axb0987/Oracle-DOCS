# ADM Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html
- Fetched: 2026-09-05 19:03 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#dcoc-content-body)

## ADM Functions

Package: DBMS_CLOUD_OCI_ADM_APPLICATION_DEPENDENCY_MANAGEMENT

### ACTIVATE_REMEDIATION_RECIPE Function

Activates the specified Remediation Recipe.

Syntax
```

```

Parameters

Parameter Description

`remediation_recipe_id`

(required) The Oracle Cloud Identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of a Remediation Recipe, as a URL path parameter.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CANCEL_REMEDIATION_RUN Function

Cancels the specified remediation run.

Syntax
```

```

Parameters

Parameter Description

`remediation_run_id`

(required) Unique Remediation Run identifier path parameter.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CANCEL_WORK_REQUEST Function

Cancel work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The Oracle Cloud Identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the asynchronous request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_KNOWLEDGE_BASE_COMPARTMENT Function

Moves a Knowledge Base from one compartment to another.

Syntax
```

```

Parameters

Parameter Description

`knowledge_base_id`

(required) The Oracle Cloud Identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of a Knowledge Base, as a URL path parameter.

`change_knowledge_base_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_REMEDIATION_RECIPE_COMPARTMENT Function

Moves a Remediation Recipe from one compartment to another.

Syntax
```

```

Parameters

Parameter Description

`remediation_recipe_id`

(required) The Oracle Cloud Identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of a Remediation Recipe, as a URL path parameter.

`change_remediation_recipe_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_REMEDIATION_RUN_COMPARTMENT Function

Moves a remediation run from one compartment to another.

Syntax
```

```

Parameters

Parameter Description

`remediation_run_id`

(required) Unique Remediation Run identifier path parameter.

`change_remediation_run_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_VULNERABILITY_AUDIT_COMPARTMENT Function

Moves a Vulnerability Audit from one compartment to another.

Syntax
```

```

Parameters

Parameter Description

`vulnerability_audit_id`

(required) Unique Vulnerability Audit identifier path parameter.

`change_vulnerability_audit_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_KNOWLEDGE_BASE Function

Creates a new Knowledge Base.

Syntax
```

```

Parameters

Parameter Description

`create_knowledge_base_details`

(required) The details to create a new Knowledge Base.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_REMEDIATION_RECIPE Function

Creates a new Remediation Recipe.

Syntax
```

```

Parameters

Parameter Description

`create_remediation_recipe_details`

(required) The details to create a new Remediation Recipe.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_REMEDIATION_RUN Function

Creates a new remediation run.

Syntax
```

```

Parameters

Parameter Description

`create_remediation_run_details`

(required) The details used to create a new remediation run.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_VULNERABILITY_AUDIT Function

Creates a new Vulnerability Audit by providing a tree of Application Dependencies.

Syntax
```

```

Parameters

Parameter Description

`create_vulnerability_audit_details`

(required) The details to create a new Vulnerability Audit.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DEACTIVATE_REMEDIATION_RECIPE Function

Deactivates the specified Remediation Recipe.

Syntax
```

```

Parameters

Parameter Description

`remediation_recipe_id`

(required) The Oracle Cloud Identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of a Remediation Recipe, as a URL path parameter.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_KNOWLEDGE_BASE Function

Deletes the specified Knowledge Base.

Syntax
```

```

Parameters

Parameter Description

`knowledge_base_id`

(required) The Oracle Cloud Identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of a Knowledge Base, as a URL path parameter.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_REMEDIATION_RECIPE Function

Deletes the specified Remediation Recipe.

Syntax
```

```

Parameters

Parameter Description

`remediation_recipe_id`

(required) The Oracle Cloud Identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of a Remediation Recipe, as a URL path parameter.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_REMEDIATION_RUN Function

Deletes the specified remediation run.

Syntax
```

```

Parameters

Parameter Description

`remediation_run_id`

(required) Unique Remediation Run identifier path parameter.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_VULNERABILITY_AUDIT Function

Deletes the specified Vulnerability Audit.

Syntax
```

```

Parameters

Parameter Description

`vulnerability_audit_id`

(required) Unique Vulnerability Audit identifier path parameter.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_KNOWLEDGE_BASE Function

Returns the details of the specified Knowledge Base.

Syntax
```

```

Parameters

Parameter Description

`knowledge_base_id`

(required) The Oracle Cloud Identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of a Knowledge Base, as a URL path parameter.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_REMEDIATION_RECIPE Function

Returns the details of the specified RemediationRecipe.

Syntax
```

```

Parameters

Parameter Description

`remediation_recipe_id`

(required) The Oracle Cloud Identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of a Remediation Recipe, as a URL path parameter.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_REMEDIATION_RUN Function

Returns the details of the specified remediation run.

Syntax
```

```

Parameters

Parameter Description

`remediation_run_id`

(required) Unique Remediation Run identifier path parameter.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_STAGE Function

Returns the details of the specified Remediation Run Stage.

Syntax
```

```

Parameters

Parameter Description

`remediation_run_id`

(required) Unique Remediation Run identifier path parameter.

`stage_type`

(required) The type of Remediation Run Stage, as a URL path parameter.

Allowed values are: 'DETECT', 'RECOMMEND', 'VERIFY', 'APPLY'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VULNERABILITY_AUDIT Function

Returns the details of the specified Vulnerability Audit.

Syntax
```

```

Parameters

Parameter Description

`vulnerability_audit_id`

(required) Unique Vulnerability Audit identifier path parameter.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets the status of the work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The Oracle Cloud Identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_APPLICATION_DEPENDENCY_RECOMMENDATIONS Function

Returns a list of application dependency with their associated recommendations.

Syntax
```

```

Parameters

Parameter Description

`remediation_run_id`

(required) Unique Remediation Run identifier path parameter.

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`gav`

(optional) A filter to return only resources that match the entire GAV (Group Artifact Version) identifier given.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. If sort order is dfs, the nodes are returned by going through the application dependency tree in a depth-first manner. Children are sorted based on their GAV property alphabetically (either ascending or descending, depending on the order parameter). Default order is ascending. If sort order is bfs, the nodes are returned by going through the application dependency tree in a breadth-first manner. Children are sorted based on their GAV property alphabetically (either ascending or descending, depending on the order parameter). Default order is ascending. Default order for gav is ascending where ascending corresponds to alphanumerical order. Default order for nodeId is ascending where ascending corresponds to alphanumerical order. Sorting by DFS or BFS cannot be used in conjunction with the following query parameters: \"gav\", \"cvssV2GreaterThanOrEqual\", \"cvssV3GreaterThanOrEqual\" and \"vulnerabilityId\".

Allowed values are: 'gav', 'nodeId', 'dfs', 'bfs'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_APPLICATION_DEPENDENCY_VULNERABILITIES Function

Returns a list of Application Dependencies with their associated vulnerabilities.

Syntax
```

```

Parameters

Parameter Description

`vulnerability_audit_id`

(required) Unique Vulnerability Audit identifier path parameter.

`vulnerability_id`

(optional) A filter to return only Vulnerability Audits that match the specified id.

`cvss_v3_greater_than_or_equal`

(optional) A filter that returns only Vulnerability Audits that have a Common Vulnerability Scoring System Version 3 (CVSS V3) greater or equal than the specified value.

`cvss_v2_greater_than_or_equal`

(optional) A filter that returns only Vulnerability Audits that have a Common Vulnerability Scoring System Version 2 (CVSS V2) greater or equal than the specified value.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. If sort order is dfs, the nodes are returned by going through the application dependency tree in a depth-first manner. Children are sorted based on their GAV property alphabetically (either ascending or descending, depending on the order parameter). Default order is ascending. If sort order is bfs, the nodes are returned by going through the application dependency tree in a breadth-first manner. Children are sorted based on their GAV property alphabetically (either ascending or descending, depending on the order parameter). Default order is ascending. Default order for gav is ascending where ascending corresponds to alphanumerical order. Default order for nodeId is ascending where ascending corresponds to alphanumerical order. Sorting by DFS or BFS cannot be used in conjunction with the following query parameters: \"gav\", \"cvssV2GreaterThanOrEqual\", \"cvssV3GreaterThanOrEqual\" and \"vulnerabilityId\".

Allowed values are: 'gav', 'nodeId', 'dfs', 'bfs'

`root_node_id`

(optional) A filter to override the top level root identifier with the new given value. The application dependency tree will only be traversed from the given node. Query parameters \"cvssV2GreaterThanOrEqual\", \"cvssV3GreaterThanOrEqual\", \"gav\" and \"vulnerabilityId\" cannot be used in conjunction with this parameter.

`depth`

(optional) A filter to limit depth of the application dependencies tree traversal. Additionally query parameters such as \"cvssV2GreaterThanOrEqual\", \"cvssV3GreaterThanOrEqual\", \"gav\" and \"vulnerabilityId\" can't be used in conjunction with this latter.

`gav`

(optional) A filter to return only resources that match the entire GAV (Group Artifact Version) identifier given.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_KNOWLEDGE_BASES Function

Returns a list of KnowledgeBases based on the specified query parameters. At least id or compartmentId query parameter must be provided.

Syntax
```

```

Parameters

Parameter Description

`id`

(optional) A filter to return only resources that match the specified identifier. Required only if the compartmentId query parameter is not specified.

`sort_by`

(optional) The field used to sort Knowledge Bases. Only one sort order is allowed. Default order for _displayName_ is **ascending alphabetical order**. Default order for _lifecyleState_ is the following sequence: **CREATING, ACTIVE, UPDATING, FAILED, DELETING, and DELETED**.Default order for _timeCreated_ is **descending**. Default order for _timeUpdated_ is **descending**.

Allowed values are: 'DISPLAY_NAME', 'LIFECYCLE_STATE', 'TIME_CREATED', 'TIME_UPDATED'

`lifecycle_state`

(optional) A filter to return only Knowledge Bases that match the specified lifecycleState.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`compartment_id`

(optional) A filter to return only resources that belong to the specified compartment identifier. Required only if the id query param is not specified.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_REMEDIATION_RECIPES Function

Returns a list of Remediation Recipes based on the specified query parameters. The query parameters `compartmentId` or `id` must be provided.

Syntax
```

```

Parameters

Parameter Description

`id`

(optional) A filter to return only resources that match the specified identifier. Required only if the compartmentId query parameter is not specified.

`sort_by`

(optional) The field used to sort Remediation Recipes. Only one sort order is allowed. Default order for _displayName_ is **ascending alphabetical order**. Default order for _lifecyleState_ is the following sequence: **CREATING, ACTIVE, UPDATING, INACTIVE, FAILED, DELETING, and DELETED**. Default order for _timeCreated_ is **descending**. Default order for _timeUpdated_ is **descending**. Default order for _type_ is the following sequence: **ADM**.

Allowed values are: 'DISPLAY_NAME', 'LIFECYCLE_STATE', 'TIME_CREATED', 'TIME_UPDATED', 'TYPE'

`lifecycle_state`

(optional) A filter to return only Remediation Recipes that match the specified lifecycleState.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`compartment_id`

(optional) A filter to return only resources that belong to the specified compartment identifier. Required only if the id query param is not specified.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_REMEDIATION_RUNS Function

Returns a list of remediation runs contained by a compartment. The query parameter `compartmentId` is required unless the query parameter `id` is specified.

Syntax
```

```

Parameters

Parameter Description

`id`

(optional) A filter to return only resources that match the specified identifier. Required only if the compartmentId query parameter is not specified.

`remediation_recipe_id`

(optional) A filter to return only resources that match the specified Remediation Recipe identifier.

`lifecycle_state`

(optional) A filter to return only Remediation Runs that match the specified lifecycleState.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field used to sort Remediation Runs. Only one sort order is allowed. Default order for _timeCreated_ is **descending**. Default order for _timeFinished_ is **descending**. Default order for _timeStarted_ is **descending**. Default order for _displayName_ is **ascending alphabetical order**. Default order for _lifecycleState_ is the following sequence: **CREATING, ACTIVE, UPDATING, DELETING, DELETED, and FAILED**. Default order for currentStageType is the following sequence: **DETECT, RECOMMEND, VERIFY, and APPLY**.

Allowed values are: 'timeCreated', 'timeFinished', 'timeStarted', 'displayName', 'lifecycleState', 'currentStageType'

`compartment_id`

(optional) A filter to return only resources that belong to the specified compartment identifier. Required only if the id query param is not specified.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_STAGES Function

Returns a list of Remediation Run Stages based on the specified query parameters and Remediation Run identifier.

Syntax
```

```

Parameters

Parameter Description

`remediation_run_id`

(required) Unique Remediation Run identifier path parameter.

`l_type`

(optional) A filter to return only Stages that match the specified type.

Allowed values are: 'DETECT', 'RECOMMEND', 'VERIFY', 'APPLY'

`status`

(optional) A filter to return only Stages that match the specified status.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`opc_request_id`

(optional) The client request ID for tracing.

`sort_by`

(optional) The field used to sort Stages. Only one sort order is allowed. Default order for status is the following sequence: **CREATED, IN_PROGRESS, SUCCEEDED, FAILED, CANCELING, and CANCELED**. Default order for _timeCreated_ is **descending**. Default order for _timeFinished_ is **descending**. Default order for _timeStarted_ is **descending**. Default order for _type_ is the following sequence: **DETECT, RECOMMEND, VERIFY, and APPLY**.

Allowed values are: 'status', 'timeCreated', 'timeFinished', 'timeStarted', 'type'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VULNERABILITY_AUDITS Function

Returns a list of Vulnerability Audits based on the specified query parameters. At least one of id, compartmentId query parameter must be provided.

Syntax
```

```

Parameters

Parameter Description

`id`

(optional) A filter to return only resources that match the specified identifier. Required only if the compartmentId query parameter is not specified.

`compartment_id`

(optional) A filter to return only resources that belong to the specified compartment identifier. Required only if the id query param is not specified.

`knowledge_base_id`

(optional) A filter to return only Vulnerability Audits that were created against the specified knowledge base.

`is_success`

(optional) A filter to return only successful or failed Vulnerability Audits.

`lifecycle_state`

(optional) A filter to return only Vulnerability Audits that match the specified lifecycleState.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`opc_request_id`

(optional) The client request ID for tracing.

`sort_by`

(optional) The field used to sort Vulnerability Audits. Only one sort order is allowed. Default order for _maxObservedCvssV2Score_ is **ascending**. Default order for _maxObservedCvssV3Score_ is **ascending**. Default order for _maxObservedCvssV2ScoreWithIgnored_ is **ascending**. Default order for _maxObservedCvssV3ScoreWithIgnored_ is **ascending**. Default order for _timeCreated_ is **descending**. Default order for _vulnerableArtifactsCount_ is **ascending**. Default order for _vulnerableArtifactsCountWithIgnored_ is **ascending**.

Allowed values are: 'maxObservedCvssV2Score', 'maxObservedCvssV3Score', 'timeCreated', 'vulnerableArtifactsCount', 'maxObservedCvssV2ScoreWithIgnored', 'maxObservedCvssV3ScoreWithIgnored', 'vulnerableArtifactsCountWithIgnored'

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Return a (paginated) list of errors for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The Oracle Cloud Identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field used to sort WorkRequests. Only one sort order is allowed. Default order for _timeAccepted_ is **descending**.

Allowed values are: 'timeAccepted'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Return a (paginated) list of logs for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The Oracle Cloud Identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field used to sort WorkRequests. Only one sort order is allowed. Default order for _timeAccepted_ is **descending**.

Allowed values are: 'timeAccepted'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

Lists the work requests in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) A filter to return only resources that belong to the specified compartment identifier. Required only if the id query param is not specified.

`work_request_id`

(optional) The identifier of the asynchronous work request.

`status`

(optional) A filter to return only resources that match the specified OperationStatus.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`resource_id`

(optional) The Oracle Cloud Identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the resource affected by the work request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field used to sort WorkRequests. Only one sort order is allowed. Default order for _timeAccepted_ is **descending**.

Allowed values are: 'timeAccepted'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_KNOWLEDGE_BASE Function

Updates one or more attributes of the specified Knowledge Base.

Syntax
```

```

Parameters

Parameter Description

`knowledge_base_id`

(required) The Oracle Cloud Identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of a Knowledge Base, as a URL path parameter.

`update_knowledge_base_details`

(required) The details to update a Knowledge Base.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_REMEDIATION_RECIPE Function

Updates one or more attributes of the specified Remediation Recipe.

Syntax
```

```

Parameters

Parameter Description

`remediation_recipe_id`

(required) The Oracle Cloud Identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of a Remediation Recipe, as a URL path parameter.

`update_remediation_recipe_details`

(required) The details to update a Remediation Recipe.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_REMEDIATION_RUN Function

Updates by identifier one or more attributes of the specified remediation run.

Syntax
```

```

Parameters

Parameter Description

`remediation_run_id`

(required) Unique Remediation Run identifier path parameter.

`update_remediation_run_details`

(required) The details used to update a remediation run.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_VULNERABILITY_AUDIT Function

Updates one or more attributes of the specified Vulnerability Audit.

Syntax
```

```

Parameters

Parameter Description

`vulnerability_audit_id`

(required) Unique Vulnerability Audit identifier path parameter.

`update_vulnerability_audit_details`

(required) The details to update a Vulnerability Audit.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://adm.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [ADM Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-5BCFE4C6-C80F-47BA-84C2-5BBE16C11FA4)
- [ACTIVATE_REMEDIATION_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-828A920E-7654-447E-BF9B-FBC3311378CB)
- [CANCEL_REMEDIATION_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-93EF9044-36FF-4E69-8DA0-379D98EE6746)
- [CANCEL_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-6306F1EC-75BE-444D-87C6-DB359A4CE8F6)
- [CHANGE_KNOWLEDGE_BASE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-5E3BCEE9-3041-446B-BF77-2DB3AA1D97AD)
- [CHANGE_REMEDIATION_RECIPE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-2CF67A0A-B70F-4DD8-8C34-79FA7F6DC98D)
- [CHANGE_REMEDIATION_RUN_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-3DDE1E78-6958-49D8-9430-BF1AE517FAD8)
- [CHANGE_VULNERABILITY_AUDIT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-D4CE6352-A520-4EEC-9CEF-164EAA87F465)
- [CREATE_KNOWLEDGE_BASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-5FD2C32D-4947-4022-8D0E-6F50873C64A4)
- [CREATE_REMEDIATION_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-3A92B9AC-6946-44A8-91C9-129035C57E0A)
- [CREATE_REMEDIATION_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-881D40F7-FAFC-47F9-8677-5F81B0FE67FF)
- [CREATE_VULNERABILITY_AUDIT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-E095FD85-73A3-46DF-B72D-C98579A8E99F)
- [DEACTIVATE_REMEDIATION_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-1621F0D9-C2B9-4FA9-9E8D-ADBCCD817497)
- [DELETE_KNOWLEDGE_BASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-BEB696A9-F740-4F8A-82C8-311F5D76D7C4)
- [DELETE_REMEDIATION_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-3F7C3B11-1FEC-493D-BC1F-80A601597CA8)
- [DELETE_REMEDIATION_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-77200FB6-ED0A-4821-8ACE-5CC1B09320B5)
- [DELETE_VULNERABILITY_AUDIT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-6387958F-1FF6-41AB-B2C6-10359CA2F25A)
- [GET_KNOWLEDGE_BASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-A023F1E9-78DB-44F8-A5AE-D7E6E431E645)
- [GET_REMEDIATION_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-0FF6C513-5738-452F-BF2D-C2D069A86B24)
- [GET_REMEDIATION_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-3853C7A0-2DB4-45FB-BA00-E21A358798EF)
- [GET_STAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-B873355E-F21F-4F61-B37D-A5688DD9D8A8)
- [GET_VULNERABILITY_AUDIT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-3E17DE2C-A9ED-4412-909A-89A46FC90D4A)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-FC6D2E7F-CD4B-4519-86D2-B8096682FAA6)
- [LIST_APPLICATION_DEPENDENCY_RECOMMENDATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-5B691E59-0B6A-485F-AC76-4C969848621D)
- [LIST_APPLICATION_DEPENDENCY_VULNERABILITIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-FA0D4CBE-4EB4-4F36-AB9B-2AB31EAD5FAE)
- [LIST_KNOWLEDGE_BASES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-D8A8C2D9-CD0E-494B-A073-1B2A5B9EA8A7)
- [LIST_REMEDIATION_RECIPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-4DF49F00-B2D9-4EF7-8BA0-59433A806C5F)
- [LIST_REMEDIATION_RUNS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-B35F2DAC-D6FB-4C8B-B503-C0DC8CD42B52)
- [LIST_STAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-03B8D8C7-CEEC-4548-9AAB-065CD27853D3)
- [LIST_VULNERABILITY_AUDITS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-A1F16682-5C03-4915-968D-F5694B1AB674)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-ABB32135-3093-4681-B037-82420771F1A9)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-E173AD4A-763C-41DC-8E24-CFD044879716)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-8CFF0C20-3A04-46FA-B434-167266DBE2A1)
- [UPDATE_KNOWLEDGE_BASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-A05BC955-68AF-4936-B451-BBFB9B4CA9EB)
- [UPDATE_REMEDIATION_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-AA5BB0F9-9B76-495A-9077-F2BB1D654BA8)
- [UPDATE_REMEDIATION_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-3DF17DB4-922D-40A8-88A1-18600ADBC3DB)
- [UPDATE_VULNERABILITY_AUDIT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_adm_application_dependency_management.html#ADSDK-GUID-ABB5593C-BBB5-4481-8ED7-3D18DD023A73)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
