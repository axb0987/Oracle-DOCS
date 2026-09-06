# Compute Cloud at Customer Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ccac_compute_cloud_at_customer.html
- Fetched: 2026-09-05 19:05 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ccac_compute_cloud_at_customer.html#dcoc-content-body)

## Compute Cloud at Customer Functions

Package: DBMS_CLOUD_OCI_CCAC_COMPUTE_CLOUD_AT_CUSTOMER

### CHANGE_CCC_INFRASTRUCTURE_COMPARTMENT Function

Moves a Compute Cloud@Customer infrastructure resource from one compartment to another.

Syntax
```

```

Parameters

Parameter Description

`ccc_infrastructure_id`

(required) An[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for a Compute Cloud@Customer Infrastructure.

`change_ccc_infrastructure_compartment_details`

(required) Details about the compartment change operation including the destination compartment specified by the resource[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ccc.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_CCC_UPGRADE_SCHEDULE_COMPARTMENT Function

Moves a Compute Cloud@Customer upgrade schedule from one compartment to another using the specified[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`ccc_upgrade_schedule_id`

(required) Compute Cloud@Customer upgrade schedule[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`change_ccc_upgrade_schedule_compartment_details`

(required) Details about the compartment change operation including the destination compartment specified by the resource[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ccc.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CCC_INFRASTRUCTURE Function

Creates a Compute Cloud@Customer infrastructure. Once created, Oracle Services must connect the rack in the data center to this Oracle Cloud Infrastructure resource.

Syntax
```

```

Parameters

Parameter Description

`create_ccc_infrastructure_details`

(required) Details for the new CccInfrastructure.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ccc.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CCC_UPGRADE_SCHEDULE Function

Creates a new Compute Cloud@Customer upgrade schedule.

Syntax
```

```

Parameters

Parameter Description

`create_ccc_upgrade_schedule_details`

(required) Details for the new CCC Upgrade Schedule.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ccc.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CCC_INFRASTRUCTURE Function

Deletes a Compute Cloud@Customer infrastructure resource specified by the resource[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`ccc_infrastructure_id`

(required) An[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for a Compute Cloud@Customer Infrastructure.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ccc.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CCC_UPGRADE_SCHEDULE Function

Deletes a Compute Cloud@Customer upgrade schedule by the specified[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`ccc_upgrade_schedule_id`

(required) Compute Cloud@Customer upgrade schedule[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ccc.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CCC_INFRASTRUCTURE Function

Gets a Compute Cloud@Customer infrastructure using the infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`ccc_infrastructure_id`

(required) An[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for a Compute Cloud@Customer Infrastructure.

`opc_request_id`

(optional) The client request[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ccc.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CCC_UPGRADE_SCHEDULE Function

Gets a Compute Cloud@Customer upgrade schedule by the specified[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`ccc_upgrade_schedule_id`

(required) Compute Cloud@Customer upgrade schedule[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) The client request[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ccc.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CCC_INFRASTRUCTURES Function

Returns a list of Compute Cloud@Customer infrastructures.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which to list resources.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and sub-compartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`lifecycle_state`

(optional) A filter used to return only resources that match the given lifecycleState.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`display_name_contains`

(optional) A filter to return only resources whose display name contains the substring.

`ccc_infrastructure_id`

(optional) An[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for a Compute Cloud@Customer Infrastructure.

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

(optional) The client request[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ccc.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CCC_UPGRADE_SCHEDULES Function

Returns a list of Compute Cloud@Customer upgrade schedules.

Syntax
```

```

Parameters

Parameter Description

`ccc_upgrade_schedule_id`

(optional) Compute Cloud@Customer upgrade schedule[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which to list resources.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and sub-compartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`lifecycle_state`

(optional) A filter to return resources only when their lifecycleState matches the given lifecycleState.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`display_name_contains`

(optional) A filter to return only resources whose display name contains the substring.

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

(optional) The client request[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ccc.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CCC_INFRASTRUCTURE Function

Updates Compute Cloud@Customer infrastructure resource.

Syntax
```

```

Parameters

Parameter Description

`ccc_infrastructure_id`

(required) An[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for a Compute Cloud@Customer Infrastructure.

`update_ccc_infrastructure_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ccc.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CCC_UPGRADE_SCHEDULE Function

Updates the Compute Cloud@Customer upgrade schedule.

Syntax
```

```

Parameters

Parameter Description

`ccc_upgrade_schedule_id`

(required) Compute Cloud@Customer upgrade schedule[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_ccc_upgrade_schedule_details`

(required) The information to be updated in the Compute Cloud@Customer upgrade schedule.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ccc.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Compute Cloud at Customer Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ccac_compute_cloud_at_customer.html#ADSDK-GUID-44A529D4-44F1-428A-9618-5D8FB8525EF6)
- [CHANGE_CCC_INFRASTRUCTURE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ccac_compute_cloud_at_customer.html#ADSDK-GUID-3A6BC0A0-884B-4D34-A88F-BFAEB9310D88)
- [CHANGE_CCC_UPGRADE_SCHEDULE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ccac_compute_cloud_at_customer.html#ADSDK-GUID-E544A467-2DDB-4C24-8B29-ED9C6D8A77A2)
- [CREATE_CCC_INFRASTRUCTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ccac_compute_cloud_at_customer.html#ADSDK-GUID-12D87951-B61F-45DC-AD43-5962CDD6D9D3)
- [CREATE_CCC_UPGRADE_SCHEDULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ccac_compute_cloud_at_customer.html#ADSDK-GUID-A58E345E-7D83-44F7-A1C9-F568EAAB7510)
- [DELETE_CCC_INFRASTRUCTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ccac_compute_cloud_at_customer.html#ADSDK-GUID-03256EE9-6581-49B9-AFC3-7F27FD48CFB6)
- [DELETE_CCC_UPGRADE_SCHEDULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ccac_compute_cloud_at_customer.html#ADSDK-GUID-1AA561B3-9970-4A9E-B260-498C4D17FB1E)
- [GET_CCC_INFRASTRUCTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ccac_compute_cloud_at_customer.html#ADSDK-GUID-B590E837-3C10-42CE-9FA9-1AC0BA31E9D8)
- [GET_CCC_UPGRADE_SCHEDULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ccac_compute_cloud_at_customer.html#ADSDK-GUID-B9691BDE-3961-484E-AD40-C008605A2AFB)
- [LIST_CCC_INFRASTRUCTURES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ccac_compute_cloud_at_customer.html#ADSDK-GUID-1B985F3D-E625-4A37-941C-D60C9E651763)
- [LIST_CCC_UPGRADE_SCHEDULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ccac_compute_cloud_at_customer.html#ADSDK-GUID-B4C875DB-3165-46EB-B9D9-5E500679A1C7)
- [UPDATE_CCC_INFRASTRUCTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ccac_compute_cloud_at_customer.html#ADSDK-GUID-9804F35C-7691-4257-8849-DA7C34302434)
- [UPDATE_CCC_UPGRADE_SCHEDULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ccac_compute_cloud_at_customer.html#ADSDK-GUID-F6B27A7E-2F8E-45EF-8C66-C99AC4A461F8)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
