# Operator Access Control Operator Control Assignment Funtions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_operator_control_assignment.html
- Fetched: 2026-09-05 19:10 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_operator_control_assignment.html#dcoc-content-body)

## Operator Access Control Operator Control Assignment Funtions

Package: DBMS_CLOUD_OCI_OAC_OPERATOR_CONTROL_ASSIGNMENT

### CHANGE_OPERATOR_CONTROL_ASSIGNMENT_COMPARTMENT Function

Changes the compartment of the specified Operator Control assignment ID.

Syntax
```

```

Parameters

Parameter Description

`operator_control_assignment_id`

(required) unique OperatorControl identifier

`change_operator_control_assignment_compartment_details`

(required) Changes the compartment for the given operator control assignment.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operator-access-control.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_OPERATOR_CONTROL_ASSIGNMENT Function

Creates an Operator Control Assignment resource. In effect, this brings the target resource under the governance of the Operator Control for specified time duration.

Syntax
```

```

Parameters

Parameter Description

`create_operator_control_assignment_details`

(required) Details of the Operator Control Assignment.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operator-access-control.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_OPERATOR_CONTROL_ASSIGNMENT Function

Deletes the specified Operator Control Assignment. This has the effect of unassigning the specific Operator Control from the target resource.

Syntax
```

```

Parameters

Parameter Description

`operator_control_assignment_id`

(required) unique OperatorControl identifier

`description`

(optional) reason for detachment of OperatorAssignment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operator-access-control.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_OPERATOR_CONTROL_ASSIGNMENT Function

Gets the details of an Operator Control Assignment of the specified ID.

Syntax
```

```

Parameters

Parameter Description

`operator_control_assignment_id`

(required) unique OperatorControl identifier

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operator-access-control.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_OPERATOR_CONTROL_ASSIGNMENTS Function

Lists all Operator Control Assignments.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`operator_control_name`

(optional) A filter to return OperatorControl that match the given operatorControlName.

`resource_name`

(optional) A filter to return only resources that match the given ResourceName.

`resource_type`

(optional) A filter to return only lists of resources that match the entire given service type.

`lifecycle_state`

(optional) A filter to return only resources whose lifecycleState matches the given OperatorControlAssignment lifecycleState.

Allowed values are: 'CREATED', 'APPLIED', 'APPLYFAILED', 'UPDATING', 'UPDATEFAILED', 'DELETING', 'DELETED', 'DELETIONFAILED'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operator-access-control.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_OPERATOR_CONTROL_ASSIGNMENT Function

Modifies the existing Operator Control assignment of the specified Operator Control assignment ID. Modifying the assignment does not change the Operator Control assignment ID.

Syntax
```

```

Parameters

Parameter Description

`operator_control_assignment_id`

(required) unique OperatorControl identifier

`update_operator_control_assignment_details`

(required) Details for the new operator control assignment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operator-access-control.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Operator Access Control Operator Control Assignment Funtions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_operator_control_assignment.html#ADSDK-GUID-2DC25D5D-3320-47A8-AFD8-83A12B503734)
- [CHANGE_OPERATOR_CONTROL_ASSIGNMENT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_operator_control_assignment.html#ADSDK-GUID-526B722E-162C-415F-94FC-394635A0BFD0)
- [CREATE_OPERATOR_CONTROL_ASSIGNMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_operator_control_assignment.html#ADSDK-GUID-421E8F4A-5340-4673-AAB5-47E77EF1CD07)
- [DELETE_OPERATOR_CONTROL_ASSIGNMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_operator_control_assignment.html#ADSDK-GUID-4035904F-CA33-4896-B95B-3FB47AC6459B)
- [GET_OPERATOR_CONTROL_ASSIGNMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_operator_control_assignment.html#ADSDK-GUID-17C79C75-F5E2-4856-8F63-53951A523735)
- [LIST_OPERATOR_CONTROL_ASSIGNMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_operator_control_assignment.html#ADSDK-GUID-CE0A8AB2-F1E9-4A69-B72E-B628151EAC3D)
- [UPDATE_OPERATOR_CONTROL_ASSIGNMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_operator_control_assignment.html#ADSDK-GUID-F0A066AC-307D-4ED7-8356-865C1BC4A766)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
