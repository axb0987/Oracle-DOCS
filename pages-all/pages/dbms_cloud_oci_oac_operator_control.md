# Operator Access Control Operator Control Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_operator_control.html
- Fetched: 2026-09-05 19:10 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_operator_control.html#dcoc-content-body)

## Operator Access Control Operator Control Functions

Package: DBMS_CLOUD_OCI_OAC_OPERATOR_CONTROL

### CHANGE_OPERATOR_CONTROL_COMPARTMENT Function

Moves the Operator Control resource into a different compartment. When provided, 'If-Match' is checked against 'ETag' values of the resource.

Syntax
```

```

Parameters

Parameter Description

`operator_control_id`

(required) unique OperatorControl identifier

`change_operator_control_compartment_details`

(required) Moves the Operator Control resource into a different compartment.

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

### CREATE_OPERATOR_CONTROL Function

Creates an Operator Control.

Syntax
```

```

Parameters

Parameter Description

`create_operator_control_details`

(required) Details for the new Operator Control.

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

### DELETE_OPERATOR_CONTROL Function

Deletes an Operator Control. You cannot delete an Operator Control if it is assigned to govern any target resource currently or in the future. In that case, first, delete all of the current and future assignments before deleting the Operator Control. An Operator Control that was previously assigned to a target resource is marked as DELETED following a successful deletion. However, it is not completely deleted from the system. This is to ensure auditing information for the accesses done under the Operator Control is preserved for future needs. The system purges the deleted Operator Control only when all of the audit data associated with the Operator Control are also deleted. Therefore, you cannot reuse the name of the deleted Operator Control until the system purges the Operator Control.

Syntax
```

```

Parameters

Parameter Description

`operator_control_id`

(required) unique OperatorControl identifier

`description`

(optional) reason for deletion of OperatorControl.

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

### GET_OPERATOR_CONTROL Function

Gets the Operator Control associated with the specified Operator Control ID.

Syntax
```

```

Parameters

Parameter Description

`operator_control_id`

(required) unique OperatorControl identifier

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operator-access-control.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_OPERATOR_CONTROLS Function

Lists the operator controls in the compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`lifecycle_state`

(optional) A filter to return only resources whose lifecycleState matches the given OperatorControl lifecycleState.

Allowed values are: 'CREATED', 'ASSIGNED', 'UNASSIGNED', 'DELETED'

`display_name`

(optional) A filter to return OperatorControl that match the entire display name given.

`resource_type`

(optional) A filter to return only lists of resources that match the entire given service type.

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

### UPDATE_OPERATOR_CONTROL Function

Modifies the existing OperatorControl for a given operator control id except the operator control id.

Syntax
```

```

Parameters

Parameter Description

`operator_control_id`

(required) unique OperatorControl identifier

`update_operator_control_details`

(required) Details for the new OperatorControl.

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

- [Operator Access Control Operator Control Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_operator_control.html#ADSDK-GUID-356E57F1-E861-494B-A1B2-02DD50A14D3A)
- [CHANGE_OPERATOR_CONTROL_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_operator_control.html#ADSDK-GUID-84BA189C-1463-4CEA-A26F-704E586D1C61)
- [CREATE_OPERATOR_CONTROL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_operator_control.html#ADSDK-GUID-F47D9CD2-0FBC-47D1-9CB7-E82B15D52AD8)
- [DELETE_OPERATOR_CONTROL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_operator_control.html#ADSDK-GUID-C1E9AA2D-877F-4F8F-BBCC-4D66B4CE24F3)
- [GET_OPERATOR_CONTROL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_operator_control.html#ADSDK-GUID-1C84F084-4AEB-43B3-9CF9-A86CE562BBBB)
- [LIST_OPERATOR_CONTROLS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_operator_control.html#ADSDK-GUID-42CC8AAB-3DBA-4533-AF8D-E9FE337D7D4D)
- [UPDATE_OPERATOR_CONTROL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_operator_control.html#ADSDK-GUID-D535DE97-5C5B-4822-B8E7-49DC79C4A87F)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
