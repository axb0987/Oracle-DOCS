# Dashboard Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dbs_dashboard.html
- Fetched: 2026-09-05 19:06 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dbs_dashboard.html#dcoc-content-body)

## Dashboard Functions

Package: DBMS_CLOUD_OCI_DBS_DASHBOARD

### CHANGE_DASHBOARD_GROUP Function

Moves a Dashboard resource from one dashboardGroup identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`dashboard_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dashboard.

`change_dashboard_group_details`

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

### CREATE_DASHBOARD Function

Creates a new dashboard in the dashboard group's compartment using the details provided in request body. **Caution:** Resources for the Dashboard service are created in the tenacy's home region. Although it is possible to create dashboard resource in regions other than the home region, you won't be able to view those resources in the Console. Therefore, creating resources outside of the home region is not recommended.

Syntax
```

```

Parameters

Parameter Description

`create_dashboard_details`

(required) Details about the dashboard being created.

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

### DELETE_DASHBOARD Function

Deletes the specified dashboard. Uses the dashboard's OCID to determine which dashboard to delete.

Syntax
```

```

Parameters

Parameter Description

`dashboard_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dashboard.

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

### GET_DASHBOARD Function

Gets the specified dashboard's information. Uses the dashboard's OCID to determine which dashboard to retrieve.

Syntax
```

```

Parameters

Parameter Description

`dashboard_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dashboard.

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

### LIST_DASHBOARDS Function

Returns a list of dashboards with a specific dashboard group ID.

Syntax
```

```

Parameters

Parameter Description

`dashboard_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dashboard group that the dashboard belongs to.

`lifecycle_state`

(optional) A filter that returns dashboard resources that match the lifecycle state specified.

`display_name`

(optional) A case-sensitive filter that returns resources that match the entire display name specified.

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dashboard.

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

### UPDATE_DASHBOARD Function

Updates the specified dashboard. Uses the dashboard's OCID to determine which dashboard to update.

Syntax
```

```

Parameters

Parameter Description

`dashboard_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dashboard.

`update_dashboard_details`

(required) The dashboard details to be updated.

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

- [Dashboard Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dbs_dashboard.html#ADSDK-GUID-F1F3CB07-387C-4BF9-BBF8-FC8A6E62B471)
- [CHANGE_DASHBOARD_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dbs_dashboard.html#ADSDK-GUID-842BB00A-E7F0-4DCE-8ADB-0D29CD55D65E)
- [CREATE_DASHBOARD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dbs_dashboard.html#ADSDK-GUID-C37466AA-0457-42B2-BFD0-4A47500477A2)
- [DELETE_DASHBOARD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dbs_dashboard.html#ADSDK-GUID-35730011-711F-4E09-A13D-5CB8ECDF58FD)
- [GET_DASHBOARD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dbs_dashboard.html#ADSDK-GUID-D00FD370-1954-4466-ADC7-9967F447903C)
- [LIST_DASHBOARDS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dbs_dashboard.html#ADSDK-GUID-60E3C062-75F1-41D5-BE8E-82FC4FDA953D)
- [UPDATE_DASHBOARD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dbs_dashboard.html#ADSDK-GUID-D72ACA4B-5C09-46EB-BCF6-6F6EFFCC2BC2)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
