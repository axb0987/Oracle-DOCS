# Access Governance CP Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_agc_access_governance_cp.html
- Fetched: 2026-09-05 19:03 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_agc_access_governance_cp.html#dcoc-content-body)

## Access Governance CP Functions

Package: DBMS_CLOUD_OCI_AGC_ACCESS_GOVERNANCE_CP

### CHANGE_GOVERNANCE_INSTANCE_COMPARTMENT Function

Moves a GovernanceInstance resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`governance_instance_id`

(required) The OCID of the GovernanceInstance

`change_governance_instance_compartment_details`

(required) The details to change the compartment of a GovernanceInstance.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cp-prod.access-governance.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_GOVERNANCE_INSTANCE Function

Creates a new GovernanceInstance.

Syntax
```

```

Parameters

Parameter Description

`create_governance_instance_details`

(required) The details of a new GovernanceInstance.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cp-prod.access-governance.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_GOVERNANCE_INSTANCE Function

Deletes an existing GovernanceInstance.

Syntax
```

```

Parameters

Parameter Description

`governance_instance_id`

(required) The OCID of the GovernanceInstance

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cp-prod.access-governance.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_GOVERNANCE_INSTANCE Function

Gets a GovernanceInstance by OCID.

Syntax
```

```

Parameters

Parameter Description

`governance_instance_id`

(required) The OCID of the GovernanceInstance

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cp-prod.access-governance.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_GOVERNANCE_INSTANCE_CONFIGURATION Function

Gets the tenancy-wide configuration for GovernanceInstances

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment in which resources are listed.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cp-prod.access-governance.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_GOVERNANCE_INSTANCES Function

Returns a list of Governance Instances.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment in which resources are listed.

`lifecycle_state`

(optional) The lifecycle state to filter on.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`id`

(optional) The OCID of the GovernanceInstance

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending.

Allowed values are: 'timeCreated', 'displayName', 'timeUpdated', 'lifecycleState'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cp-prod.access-governance.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_GOVERNANCE_INSTANCE Function

Updates the GovernanceInstance.

Syntax
```

```

Parameters

Parameter Description

`update_governance_instance_details`

(required) The details of the GovernanceInstance to be updated.

`governance_instance_id`

(required) The OCID of the GovernanceInstance

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cp-prod.access-governance.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_GOVERNANCE_INSTANCE_CONFIGURATION Function

Updates the tenancy-wide configuration for GovernanceInstances

Syntax
```

```

Parameters

Parameter Description

`update_governance_instance_configuration_details`

(required) The details of the tenancy-wide configuration to be updated.

`compartment_id`

(required) The OCID of the compartment in which resources are listed.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cp-prod.access-governance.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Access Governance CP Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_agc_access_governance_cp.html#ADSDK-GUID-5B7D4433-9094-4219-A1CB-CF03990FFD85)
- [CHANGE_GOVERNANCE_INSTANCE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_agc_access_governance_cp.html#ADSDK-GUID-0010F44D-2FC5-4C44-B591-12E7A9F4BD18)
- [CREATE_GOVERNANCE_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_agc_access_governance_cp.html#ADSDK-GUID-24A4B828-4185-475C-A2C1-BE8EDEF25302)
- [DELETE_GOVERNANCE_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_agc_access_governance_cp.html#ADSDK-GUID-88E3A243-C560-4C53-9863-A90369E14383)
- [GET_GOVERNANCE_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_agc_access_governance_cp.html#ADSDK-GUID-6704BB86-4903-4BB1-8AA9-DB20EA626183)
- [GET_GOVERNANCE_INSTANCE_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_agc_access_governance_cp.html#ADSDK-GUID-3FDFC1CE-2E97-41E6-AA42-2B981A2F1B53)
- [LIST_GOVERNANCE_INSTANCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_agc_access_governance_cp.html#ADSDK-GUID-8E5E0663-292D-4646-B616-982EC7CAAE7B)
- [UPDATE_GOVERNANCE_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_agc_access_governance_cp.html#ADSDK-GUID-F99D0E4C-F92E-472D-89DD-DC727608EEA4)
- [UPDATE_GOVERNANCE_INSTANCE_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_agc_access_governance_cp.html#ADSDK-GUID-6474AFB0-3EC8-46C9-A143-B0EA919200B2)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
