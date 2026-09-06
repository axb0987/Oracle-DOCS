# Dashboard Group Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dbs_dashboard_group.html
- Fetched: 2026-09-05 19:06 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dbs_dashboard_group.html#dcoc-content-body)

## Dashboard Group Functions

Package: DBMS_CLOUD_OCI_DBS_DASHBOARD_GROUP

### CHANGE_DASHBOARD_GROUP_COMPARTMENT Function

Moves a DashboardGroup resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`dashboard_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dashboard group.

`change_dashboard_group_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dashboard.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DASHBOARD_GROUP Function

Creates a new dashboard group using the details provided in request body. **Caution:** Resources for the Dashboard service are created in the tenacy's home region. Although it is possible to create dashboard group resource in regions other than the home region, you won't be able to view those resources in the Console. Therefore, creating resources outside of the home region is not recommended.

Syntax
```

```

Parameters

Parameter Description

`create_dashboard_group_details`

(required) Details about the dashboard group being created.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_cross_region`

(optional) To identify if the call is cross-regional. In CRUD calls for a resource, to identify that the call originates from different region, set the `CrossRegionIdentifierHeader` parameter to a region name (ex - `US-ASHBURN-1`) The call will be served from a Replicated bucket. For same-region calls, the value is unassigned.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dashboard.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DASHBOARD_GROUP Function

Deletes the specified dashboard group. Uses the dashboard group's OCID to determine which dashboard group to delete.

Syntax
```

```

Parameters

Parameter Description

`dashboard_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dashboard group.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_cross_region`

(optional) To identify if the call is cross-regional. In CRUD calls for a resource, to identify that the call originates from different region, set the `CrossRegionIdentifierHeader` parameter to a region name (ex - `US-ASHBURN-1`) The call will be served from a Replicated bucket. For same-region calls, the value is unassigned.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dashboard.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DASHBOARD_GROUP Function

Gets the specified dashboard group's information. Uses the dashboard group's OCID to determine which dashboard to retrieve.

Syntax
```

```

Parameters

Parameter Description

`dashboard_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dashboard group.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_cross_region`

(optional) To identify if the call is cross-regional. In CRUD calls for a resource, to identify that the call originates from different region, set the `CrossRegionIdentifierHeader` parameter to a region name (ex - `US-ASHBURN-1`) The call will be served from a Replicated bucket. For same-region calls, the value is unassigned.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dashboard.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DASHBOARD_GROUPS Function

Returns a list of dashboard groups with a specific compartment ID.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which to list resources.

`lifecycle_state`

(optional) A filter that returns dashboard groups that match the lifecycle state specified.

`display_name`

(optional) A case-sensitive filter that returns resources that match the entire display name specified.

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dashboard group.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This value is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_cross_region`

(optional) To identify if the call is cross-regional. In CRUD calls for a resource, to identify that the call originates from different region, set the `CrossRegionIdentifierHeader` parameter to a region name (ex - `US-ASHBURN-1`) The call will be served from a Replicated bucket. For same-region calls, the value is unassigned.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dashboard.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DASHBOARD_GROUP Function

Updates the specified dashboard group. Uses the dashboard group's OCID to determine which dashboard group to update.

Syntax
```

```

Parameters

Parameter Description

`dashboard_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dashboard group.

`update_dashboard_group_details`

(required) The dashboard group details to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_cross_region`

(optional) To identify if the call is cross-regional. In CRUD calls for a resource, to identify that the call originates from different region, set the `CrossRegionIdentifierHeader` parameter to a region name (ex - `US-ASHBURN-1`) The call will be served from a Replicated bucket. For same-region calls, the value is unassigned.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dashboard.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Dashboard Group Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dbs_dashboard_group.html#ADSDK-GUID-B8CDD49E-523D-48E3-8440-82A1BA3BDF40)
- [CHANGE_DASHBOARD_GROUP_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dbs_dashboard_group.html#ADSDK-GUID-4462C777-9FE3-4260-8E88-FB5E5505D4D7)
- [CREATE_DASHBOARD_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dbs_dashboard_group.html#ADSDK-GUID-5382FDEB-E26F-46B2-A004-7A60EB2E05BD)
- [DELETE_DASHBOARD_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dbs_dashboard_group.html#ADSDK-GUID-B321E237-5361-4683-831E-9BE0D03CFF10)
- [GET_DASHBOARD_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dbs_dashboard_group.html#ADSDK-GUID-255D99E2-5289-4D37-97A1-0CBA06A73F44)
- [LIST_DASHBOARD_GROUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dbs_dashboard_group.html#ADSDK-GUID-0F4D35CE-3127-4DFD-9A01-A7F54B70A7CB)
- [UPDATE_DASHBOARD_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dbs_dashboard_group.html#ADSDK-GUID-1763ADB5-37C3-4F8D-829A-04CD747B5084)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
