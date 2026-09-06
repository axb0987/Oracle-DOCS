# Management Dashboard Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_md_dashx_apis.html
- Fetched: 2026-09-05 19:09 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_md_dashx_apis.html#dcoc-content-body)

## Management Dashboard Functions

Package: DBMS_CLOUD_OCI_MD_DASHX_APIS

### CHANGE_MANAGEMENT_DASHBOARDS_COMPARTMENT Function

Moves the dashboard from the existing compartment to a new compartment.

Syntax
```

```

Parameters

Parameter Description

`management_dashboard_id`

(required) A unique dashboard identifier.

`change_management_dashboards_compartment_details`

(required) ID of the dashboard that is being moved.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managementdashboard.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_MANAGEMENT_SAVED_SEARCHES_COMPARTMENT Function

Moves the saved search from the existing compartment to a new compartment.

Syntax
```

```

Parameters

Parameter Description

`management_saved_search_id`

(required) A unique saved search identifier.

`change_management_saved_searches_compartment_details`

(required) ID of the saved search that is being moved.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managementdashboard.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MANAGEMENT_DASHBOARD Function

Creates a new dashboard. Limit for number of saved searches in a dashboard is 20. Here's an example of how you can use CLI to create a dashboard. For information on the details that must be passed to CREATE, you can use the GET API to obtain the Create.json file: `oci management-dashboard dashboard get --management-dashboard-id \"ocid1.managementdashboard.oc1..dashboardId1\" --query data &gt; Create.json.` You can then modify the Create.json file by removing the `id` attribute and making other required changes, and use the `oci management-dashboard dashboard create` command.

Syntax
```

```

Parameters

Parameter Description

`create_management_dashboard_details`

(required) JSON metadata for creating a new dashboard.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managementdashboard.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MANAGEMENT_SAVED_SEARCH Function

Creates a new saved search. Here's an example of how you can use CLI to create a saved search. For information on the details that must be passed to CREATE, you can use the GET API to obtain the Create.json file: `oci management-dashboard saved-search get --management-saved-search-id ocid1.managementsavedsearch.oc1..savedsearchId1 --query data &gt; Create.json`. You can then modify the Create.json file by removing the `id` attribute and making other required changes, and use the `oci management-dashboard saved-search create` command.

Syntax
```

```

Parameters

Parameter Description

`create_management_saved_search_details`

(required) JSON metadata for the saved search.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managementdashboard.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MANAGEMENT_DASHBOARD Function

Deletes a Dashboard by ID.

Syntax
```

```

Parameters

Parameter Description

`management_dashboard_id`

(required) A unique dashboard identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managementdashboard.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MANAGEMENT_SAVED_SEARCH Function

Deletes a saved search by ID.

Syntax
```

```

Parameters

Parameter Description

`management_saved_search_id`

(required) A unique saved search identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managementdashboard.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### EXPORT_DASHBOARD Function

Exports an array of dashboards and their saved searches. Export is designed to work with importDashboard. Here's an example of how you can use CLI to export a dashboard: `$oci management-dashboard dashboard export --query data --export-dashboard-id \"{\\\"dashboardIds\\\":[\\\"ocid1.managementdashboard.oc1..dashboardId1\\\"]}\" &gt; dashboards.json`

Syntax
```

```

Parameters

Parameter Description

`export_dashboard_id`

(required) List of dashboardIds in plain text. The syntax is '{\"dashboardIds\":[\"dashboardId1\", \"dashboardId2\", ...]}'. Escaping is needed when using in OCI CLI. For example, \"{\\\"dashboardIds\\\":[\\\"ocid1.managementdashboard.oc1..dashboardId1\\\"]}\" .

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managementdashboard.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MANAGEMENT_DASHBOARD Function

Gets a dashboard and its saved searches by ID. Deleted or unauthorized saved searches are marked by tile's state property.

Syntax
```

```

Parameters

Parameter Description

`management_dashboard_id`

(required) A unique dashboard identifier.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managementdashboard.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MANAGEMENT_SAVED_SEARCH Function

Gets a saved search by ID.

Syntax
```

```

Parameters

Parameter Description

`management_saved_search_id`

(required) A unique saved search identifier.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managementdashboard.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### IMPORT_DASHBOARD Function

Imports an array of dashboards and their saved searches. Here's an example of how you can use CLI to import a dashboard. For information on the details that must be passed to IMPORT, you can use the EXPORT API to obtain the Import.json file: `oci management-dashboard dashboard export --query data --export-dashboard-id \"{\\\"dashboardIds\\\":[\\\"ocid1.managementdashboard.oc1..dashboardId1\\\"]}\" &gt; Import.json`. Note that import API updates the resource if it already exists, and creates a new resource if it does not exist. To import to a different compartment, edit and change the compartmentId to the desired compartment OCID. Here's an example of how you can use CLI to import: `oci management-dashboard dashboard import --from-json file://Import.json`

Syntax
```

```

Parameters

Parameter Description

`management_dashboard_import_details`

(required) JSON metadata for importing dashboards and their saved searches.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managementdashboard.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MANAGEMENT_DASHBOARDS Function

Gets the list of dashboards in a compartment with pagination. Returned properties are the summary.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page on which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managementdashboard.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MANAGEMENT_SAVED_SEARCHES Function

Gets the list of saved searches in a compartment with pagination. Returned properties are the summary.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page on which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managementdashboard.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MANAGEMENT_DASHBOARD Function

Updates an existing dashboard identified by ID path parameter. CompartmentId can be modified only by the changeCompartment API. Limit for number of saved searches in a dashboard is 20.

Syntax
```

```

Parameters

Parameter Description

`management_dashboard_id`

(required) A unique dashboard identifier.

`update_management_dashboard_details`

(required) JSON metadata for changed dashboard properties.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managementdashboard.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MANAGEMENT_SAVED_SEARCH Function

Updates an existing saved search identified by ID path parameter. CompartmentId can be modified only by the changeCompartment API.

Syntax
```

```

Parameters

Parameter Description

`management_saved_search_id`

(required) A unique saved search identifier.

`update_management_saved_search_details`

(required) JSON metadata for changed saved search properties.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://managementdashboard.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Management Dashboard Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_md_dashx_apis.html#ADSDK-GUID-9E6AACF0-097A-412C-A88E-53B7943A83D6)
- [CHANGE_MANAGEMENT_DASHBOARDS_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_md_dashx_apis.html#ADSDK-GUID-C1CA0081-4281-4B01-AFAA-5CA2F39F7535)
- [CHANGE_MANAGEMENT_SAVED_SEARCHES_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_md_dashx_apis.html#ADSDK-GUID-14B09EB0-5194-4A8A-9661-4B2F63EEAD6D)
- [CREATE_MANAGEMENT_DASHBOARD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_md_dashx_apis.html#ADSDK-GUID-F14F5ECA-398F-40B0-9966-4B10E2DA54C5)
- [CREATE_MANAGEMENT_SAVED_SEARCH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_md_dashx_apis.html#ADSDK-GUID-0A574958-3AC1-4D82-8447-12C66D0488E8)
- [DELETE_MANAGEMENT_DASHBOARD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_md_dashx_apis.html#ADSDK-GUID-6F7A96D4-F83A-496A-BB41-BC5A13D7D9D8)
- [DELETE_MANAGEMENT_SAVED_SEARCH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_md_dashx_apis.html#ADSDK-GUID-E52C906E-9F0D-43A7-8A52-FCC8264B786E)
- [EXPORT_DASHBOARD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_md_dashx_apis.html#ADSDK-GUID-B80822AD-5791-4F89-8C34-B1C7C4A5A12F)
- [GET_MANAGEMENT_DASHBOARD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_md_dashx_apis.html#ADSDK-GUID-D759EF83-3B54-4259-B81A-0E0DC7137C9B)
- [GET_MANAGEMENT_SAVED_SEARCH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_md_dashx_apis.html#ADSDK-GUID-3D9BD69E-42DF-4A29-9D31-9178AFD597CD)
- [IMPORT_DASHBOARD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_md_dashx_apis.html#ADSDK-GUID-9431A88D-49D2-4966-9C8B-17745434E9CD)
- [LIST_MANAGEMENT_DASHBOARDS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_md_dashx_apis.html#ADSDK-GUID-8D2B6B59-48EE-4EE3-BA0F-78B07A41AF0B)
- [LIST_MANAGEMENT_SAVED_SEARCHES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_md_dashx_apis.html#ADSDK-GUID-CD447439-5632-4A99-AABE-3CF4D57AAD48)
- [UPDATE_MANAGEMENT_DASHBOARD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_md_dashx_apis.html#ADSDK-GUID-02C2C0F5-2C4F-4946-A71E-C1911A22284E)
- [UPDATE_MANAGEMENT_SAVED_SEARCH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_md_dashx_apis.html#ADSDK-GUID-C3A08878-BA70-4E30-A09D-0C090DAF3BC1)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
