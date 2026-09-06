# Governance Rules CP Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_grcp_governance_rule.html
- Fetched: 2026-09-05 19:08 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_grcp_governance_rule.html#dcoc-content-body)

## Governance Rules CP Functions

Package: DBMS_CLOUD_OCI_GRCP_GOVERNANCE_RULE

### CREATE_GOVERNANCE_RULE Function

Create governance rule in the root compartment only. Either relatedResourceId or template must be supplied.

Syntax
```

```

Parameters

Parameter Description

`create_governance_rule_details`

(required) Details to create a new governance rule.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://governance-rules.organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_INCLUSION_CRITERION Function

Create inclusion criterion of type tenancy or tag for the governance rule.

Syntax
```

```

Parameters

Parameter Description

`create_inclusion_criterion_details`

(required) Details to create a new inclusion criterion.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://governance-rules.organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_GOVERNANCE_RULE Function

Delete the specified governance rule.

Syntax
```

```

Parameters

Parameter Description

`governance_rule_id`

(required) Unique governance rule identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://governance-rules.organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_INCLUSION_CRITERION Function

Delete the specified inclusion criterion.

Syntax
```

```

Parameters

Parameter Description

`inclusion_criterion_id`

(required) Unique inclusion criterion identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://governance-rules.organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ENFORCED_GOVERNANCE_RULE Function

Get the specified enforced governance rule's information.

Syntax
```

```

Parameters

Parameter Description

`enforced_governance_rule_id`

(required) Unique enforced governance rule identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://governance-rules.organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_GOVERNANCE_RULE Function

Get the specified governance rule's information.

Syntax
```

```

Parameters

Parameter Description

`governance_rule_id`

(required) Unique governance rule identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://governance-rules.organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_INCLUSION_CRITERION Function

Get the specified inclusion criterion's information.

Syntax
```

```

Parameters

Parameter Description

`inclusion_criterion_id`

(required) Unique inclusion criterion identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://governance-rules.organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TENANCY_ATTACHMENT Function

Get the specified tenancy attachment's information.

Syntax
```

```

Parameters

Parameter Description

`tenancy_attachment_id`

(required) Unique tenancy attachment identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://governance-rules.organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ENFORCED_GOVERNANCE_RULES Function

List enforced governance rules. Either compartment id or enforced governance rule id must be supplied. An optional governance rule type or a display name can also be supplied.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The ID of the compartment in which to list resources.

`enforced_governance_rule_id`

(optional) Unique enforced governance rule identifier.

`governance_rule_type`

(optional) A filter to return only resources that match the type given.

Allowed values are: 'QUOTA', 'TAG', 'ALLOWED_REGIONS'

`display_name`

(optional) A filter to return only resources that match the entire name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://governance-rules.organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_GOVERNANCE_RULES Function

List governance rules. Either compartment id or governance rule id must be supplied. An optional lifecycle state, display name or a governance rule type can also be supplied.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The ID of the compartment in which to list resources.

`governance_rule_id`

(optional) Unique governance rule identifier.

`lifecycle_state`

(optional) A filter to return only resources whose lifecycle state matches the given lifecycle state.

Allowed values are: 'ACTIVE', 'DELETED'

`display_name`

(optional) A filter to return only resources that match the entire name given.

`governance_rule_type`

(optional) A filter to return only resources that match the type given.

Allowed values are: 'QUOTA', 'TAG', 'ALLOWED_REGIONS'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://governance-rules.organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_INCLUSION_CRITERIA Function

List inclusion criteria associated with a governance rule. Governance rule id must be supplied. An optional inclusion criterion id or a lifecycle state can also be supplied.

Syntax
```

```

Parameters

Parameter Description

`governance_rule_id`

(required) Unique governance rule identifier.

`inclusion_criterion_id`

(optional) Unique inclusion criterion identifier.

`lifecycle_state`

(optional) A filter to return only resources when their lifecycle state matches the given lifecycle state.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://governance-rules.organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TENANCY_ATTACHMENTS Function

List tenancy attachments. Either compartment id, governance rule id or tenancy attachment id must be supplied. An optional lifecycle state or a child tenancy id can also be supplied.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The ID of the compartment in which to list resources.

`tenancy_attachment_id`

(optional) Unique tenancy attachment identifier.

`governance_rule_id`

(optional) Unique governance rule identifier.

`lifecycle_state`

(optional) A filter to return only resources when their lifecycle state matches the given lifecycle state.

`child_tenancy_id`

(optional) A filter to return only governance rules that match the given tenancy id.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://governance-rules.organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RETRY_GOVERNANCE_RULE Function

Retry the creation of the specified governance rule. Used by the tenancy admins when all the workflow retries have exhausted. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`governance_rule_id`

(required) Unique governance rule identifier.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://governance-rules.organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RETRY_TENANCY_ATTACHMENT Function

Retry governance rule application for the specified tenancy attachment id. Used by the tenancy admins when all the workflow retries have exhausted.

Syntax
```

```

Parameters

Parameter Description

`tenancy_attachment_id`

(required) Unique tenancy attachment identifier.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://governance-rules.organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_GOVERNANCE_RULE Function

Update the specified governance rule.

Syntax
```

```

Parameters

Parameter Description

`governance_rule_id`

(required) Unique governance rule identifier.

`update_governance_rule_details`

(required) Details to update the governance rule.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://governance-rules.organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Governance Rules CP Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_grcp_governance_rule.html#ADSDK-GUID-1B2A881E-706C-4D6A-B465-AFEC52C082D0)
- [CREATE_GOVERNANCE_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_grcp_governance_rule.html#ADSDK-GUID-D154556C-7780-450A-989A-10DFE0EE1F6C)
- [CREATE_INCLUSION_CRITERION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_grcp_governance_rule.html#ADSDK-GUID-08C14126-644C-41A3-8296-563785078ECC)
- [DELETE_GOVERNANCE_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_grcp_governance_rule.html#ADSDK-GUID-BA53D908-829C-4865-82B0-E8F3BFFB37B9)
- [DELETE_INCLUSION_CRITERION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_grcp_governance_rule.html#ADSDK-GUID-ED084DA7-E8F6-4EB5-B533-DCCB57A90CC8)
- [GET_ENFORCED_GOVERNANCE_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_grcp_governance_rule.html#ADSDK-GUID-7264DF52-D404-411F-B6B1-5FF6E4606BA8)
- [GET_GOVERNANCE_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_grcp_governance_rule.html#ADSDK-GUID-EBCA0EF1-DF58-498A-8984-4789D9B10A3F)
- [GET_INCLUSION_CRITERION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_grcp_governance_rule.html#ADSDK-GUID-5575463D-3BD5-4F6D-812F-727115DA7D40)
- [GET_TENANCY_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_grcp_governance_rule.html#ADSDK-GUID-6A4F80AF-9E6D-4B00-9B82-DE9E466E7B06)
- [LIST_ENFORCED_GOVERNANCE_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_grcp_governance_rule.html#ADSDK-GUID-500989F3-5D47-46BE-AD3A-7F7905BB3B9E)
- [LIST_GOVERNANCE_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_grcp_governance_rule.html#ADSDK-GUID-78473FCA-A11D-4C1F-8851-9A89DB6D3BC2)
- [LIST_INCLUSION_CRITERIA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_grcp_governance_rule.html#ADSDK-GUID-BD06FC56-57D1-44CF-84AE-5C30486D0E54)
- [LIST_TENANCY_ATTACHMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_grcp_governance_rule.html#ADSDK-GUID-CDCAF3AD-625F-45E3-9D91-1834CEFB61E2)
- [RETRY_GOVERNANCE_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_grcp_governance_rule.html#ADSDK-GUID-B8EA2953-911E-43B7-9949-D774E87EA66A)
- [RETRY_TENANCY_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_grcp_governance_rule.html#ADSDK-GUID-49BC6006-3AC3-4896-B9BC-2B685847B640)
- [UPDATE_GOVERNANCE_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_grcp_governance_rule.html#ADSDK-GUID-FD0BD1B0-51FF-422B-9C79-677D666920B2)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
