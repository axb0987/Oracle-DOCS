# Service Connector Hub Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_sch_service_connector.html
- Fetched: 2026-09-05 19:14 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_sch_service_connector.html#dcoc-content-body)

## Service Connector Hub Functions

Package: DBMS_CLOUD_OCI_SCH_SERVICE_CONNECTOR

### ACTIVATE_SERVICE_CONNECTOR Function

Activates the specified service connector. After you send your request, the service connector's state is temporarily UPDATING. When the state changes to ACTIVE, data begins transferring from the source service to the target service. For instructions on activating service connectors, see[To activate a service connector](https://docs.oracle.com/iaas/Content/service-connector-hub/managingconnectors.htm#activate).

Syntax
```

```

Parameters

Parameter Description

`service_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the service connector.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-connector-hub.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_SERVICE_CONNECTOR_COMPARTMENT Function

Moves a service connector into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes). When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`service_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the service connector.

`change_service_connector_compartment_details`

(required) The configuration details for moving a service connector to a different compartment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-connector-hub.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SERVICE_CONNECTOR Function

Creates a new service connector in the specified compartment. A service connector is a logically defined flow for moving data from a source service to a destination service in Oracle Cloud Infrastructure. For instructions, see[To create a service connector](https://docs.oracle.com/iaas/Content/service-connector-hub/managingconnectors.htm#create). For general information about service connectors, see[Service Connector Hub Overview](https://docs.oracle.com/iaas/Content/service-connector-hub/overview.htm). For purposes of access control, you must provide the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want the service connector to reside. Notice that the service connector doesn't have to be in the same compartment as the source or target services. For information about access control and compartments, see[Overview of the IAM Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). After you send your request, the new service connector's state is temporarily CREATING. When the state changes to ACTIVE, data begins transferring from the source service to the target service. For instructions on deactivating and activating service connectors, see[To activate or deactivate a service connector](https://docs.oracle.com/iaas/Content/service-connector-hub/overview.htm).

Syntax
```

```

Parameters

Parameter Description

`create_service_connector_details`

(required) Configuration details for the new service connector.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-connector-hub.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DEACTIVATE_SERVICE_CONNECTOR Function

Deactivates the specified service connector. After you send your request, the service connector's state is temporarily UPDATING and any data transfer stops. The state then changes to INACTIVE. For instructions on deactivating service connectors, see[To deactivate a service connector](https://docs.oracle.com/iaas/Content/service-connector-hub/managingconnectors.htm#deactivate).

Syntax
```

```

Parameters

Parameter Description

`service_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the service connector.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-connector-hub.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SERVICE_CONNECTOR Function

Deletes the specified service connector. After you send your request, the service connector's state is temporarily DELETING and any data transfer stops. The state then changes to DELETED.

Syntax
```

```

Parameters

Parameter Description

`service_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the service connector.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-connector-hub.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SERVICE_CONNECTOR Function

Gets the specified service connector's configuration information.

Syntax
```

```

Parameters

Parameter Description

`service_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the service connector.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-connector-hub.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets the details of the specified work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-connector-hub.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SERVICE_CONNECTORS Function

Lists service connectors in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment for this request.

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state. Example: `ACTIVE`

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`display_name`

(optional) A filter to return only resources that match the given display name exactly. Example: `example_service_connector`

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the opc-next-page response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for `timeCreated` is descending. Default order for `displayName` is ascending. If no value is specified `timeCreated` is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-connector-hub.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Lists work request errors for the specified work request. Results are paginated.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) For list pagination. The value of the opc-next-page response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-connector-hub.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Lists logs for the specified work request. Results are paginated.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) For list pagination. The value of the opc-next-page response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-connector-hub.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

Lists the work requests in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment for this request.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) For list pagination. The value of the opc-next-page response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-connector-hub.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SERVICE_CONNECTOR Function

Updates the configuration information for the specified service connector. After you send your request, the service connector's state is temporarily UPDATING and any data transfer pauses. The state then changes back to its original value: if ACTIVE, then data transfer resumes.

Syntax
```

```

Parameters

Parameter Description

`service_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the service connector.

`update_service_connector_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-connector-hub.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Service Connector Hub Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_sch_service_connector.html#ADSDK-GUID-0B306310-C3B5-4D0E-BC4E-BD56D7B68C4D)
- [ACTIVATE_SERVICE_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_sch_service_connector.html#ADSDK-GUID-850141F4-6086-4E76-8BF7-D608935B695A)
- [CHANGE_SERVICE_CONNECTOR_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_sch_service_connector.html#ADSDK-GUID-257CF161-1BA0-44C0-99FE-98591D435DF5)
- [CREATE_SERVICE_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_sch_service_connector.html#ADSDK-GUID-0E240668-AA57-4E3C-A72F-9D24575B2681)
- [DEACTIVATE_SERVICE_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_sch_service_connector.html#ADSDK-GUID-C8EFB574-2F25-4946-8578-E9F9F45797DD)
- [DELETE_SERVICE_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_sch_service_connector.html#ADSDK-GUID-5AB820D5-5A5B-4612-BF4D-C0946430E2E1)
- [GET_SERVICE_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_sch_service_connector.html#ADSDK-GUID-8F0B5827-2C4E-4032-B7C1-6327330889EE)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_sch_service_connector.html#ADSDK-GUID-D7C4E925-15A4-4D5C-BAA9-54CCCF67A641)
- [LIST_SERVICE_CONNECTORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_sch_service_connector.html#ADSDK-GUID-B742E78E-6DC1-47D5-BB7F-C9CFDF67F451)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_sch_service_connector.html#ADSDK-GUID-A9DB8A3C-E215-4634-8E54-A45431F80A3C)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_sch_service_connector.html#ADSDK-GUID-292777E5-A407-4887-8A43-ECBE4F83859D)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_sch_service_connector.html#ADSDK-GUID-AE5DA257-0396-42F8-9926-479CFA8E4EAB)
- [UPDATE_SERVICE_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_sch_service_connector.html#ADSDK-GUID-D4651BBE-DB2F-43EE-99DE-3E2B8E3892FE)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
