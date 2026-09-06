# Operator Access Control Operator Actions Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_operator_actions.html
- Fetched: 2026-09-05 19:10 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_operator_actions.html#dcoc-content-body)

## Operator Access Control Operator Actions Functions

Package: DBMS_CLOUD_OCI_OAC_OPERATOR_ACTIONS

### GET_OPERATOR_ACTION Function

Gets the operator action associated with the specified operator action ID.

Syntax
```

```

Parameters

Parameter Description

`operator_action_id`

(required) Unique Oracle supplied identifier associated with the operator action.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operator-access-control.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_OPERATOR_ACTIONS Function

Lists all the OperatorActions available in the system.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`name`

(optional) A filter to return only resources that match the entire display name given.

`resource_type`

(optional) A filter to return only lists of resources that match the entire given service type.

`lifecycle_state`

(optional) A filter to return only resources whose lifecycleState matches the given OperatorAction lifecycleState.

Allowed values are: 'ACTIVE', 'INACTIVE'

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

- [Operator Access Control Operator Actions Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_operator_actions.html#ADSDK-GUID-9938F900-5259-4ED0-9540-F08A171417D3)
- [GET_OPERATOR_ACTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_operator_actions.html#ADSDK-GUID-678A783A-45B1-4CCF-BCFA-50DBAE3F60A9)
- [LIST_OPERATOR_ACTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_operator_actions.html#ADSDK-GUID-D95FC8C8-D671-43EF-B06F-B2393E67692F)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
