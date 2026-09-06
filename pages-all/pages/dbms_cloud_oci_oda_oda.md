# ODA Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_oda.html
- Fetched: 2026-09-05 19:11 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_oda.html#dcoc-content-body)

## ODA Functions

Package: DBMS_CLOUD_OCI_ODA_ODA

### CHANGE_ODA_INSTANCE_COMPARTMENT Function

Moves an Digital Assistant instance into a different compartment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`change_oda_instance_compartment_details`

(required) The compartment to which the Digital Assistant instance should be moved.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that you can retry the request if there's a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but they can become invalid before then if there are conflicting operations. For example, if an instance was deleted and purged from the system, then the service might reject a retry of the original creation request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ODA_INSTANCE Function

Starts an asynchronous job to create a Digital Assistant instance. To monitor the status of the job, take the `opc-work-request-id` response header value and use it to call `GET /workRequests/{workRequestId}`.

Syntax
```

```

Parameters

Parameter Description

`create_oda_instance_details`

(required) Details for the new Digital Assistant instance.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that you can retry the request if there's a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but they can become invalid before then if there are conflicting operations. For example, if an instance was deleted and purged from the system, then the service might reject a retry of the original creation request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ODA_INSTANCE_ATTACHMENT Function

Starts an asynchronous job to create a Digital Assistant instance attachment. To monitor the status of the job, take the `opc-work-request-id` response header value and use it to call `GET /workRequests/{workRequestId}`.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`create_oda_instance_attachment_details`

(required) Details for the new Digital Assistant instance attachment.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that you can retry the request if there's a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but they can become invalid before then if there are conflicting operations. For example, if an instance was deleted and purged from the system, then the service might reject a retry of the original creation request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ODA_INSTANCE Function

Starts an asynchronous job to delete the specified Digital Assistant instance. To monitor the status of the job, take the `opc-work-request-id` response header value and use it to call `GET /workRequests/{workRequestId}`.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`retention_time`

(optional) Retain the ODA instance being deleted for the given number of days before hard-delete/purge.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ODA_INSTANCE_ATTACHMENT Function

Starts an asynchronous job to delete the specified Digital Assistant instance attachment.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`attachment_id`

(required) Unique Digital Assistant instance attachment identifier.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ODA_INSTANCE Function

Gets the specified Digital Assistant instance.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ODA_INSTANCE_ATTACHMENT Function

Gets an ODA instance attachment by identifier

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`attachment_id`

(required) Unique Digital Assistant instance attachment identifier.

`include_owner_metadata`

(optional) Whether to send attachment owner info during get/list call.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets information about the work request with the specified ID, including its status. You can use this operation to monitor the status of jobs that you requested to create, delete, and update instances.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The identifier of the asynchronous work request.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ODA_INSTANCE_ATTACHMENTS Function

Returns a list of ODA instance attachments

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`include_owner_metadata`

(optional) Whether to send attachment owner info during get/list call.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The page at which to start retrieving results. You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter. Example: `MToxMA==`

`lifecycle_state`

(optional) List only the ODA instance attachments that are in this lifecycle state.

Allowed values are: 'ATTACHING', 'ACTIVE', 'DETACHING', 'INACTIVE', 'FAILED'

`sort_order`

(optional) Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Sort on this field. You can specify one sort order only. The default sort field is `TIMECREATED`. The default sort order for `TIMECREATED` is descending.

Allowed values are: 'TIMECREATED'

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ODA_INSTANCES Function

Returns a page of Digital Assistant instances that belong to the specified compartment. If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) List the Digital Assistant instances that belong to this compartment.

`display_name`

(optional) List only the information for the Digital Assistant instance with this user-friendly name. These names don't have to be unique and may change. Example: `My new resource`

`lifecycle_state`

(optional) List only the Digital Assistant instances that are in this lifecycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The page at which to start retrieving results. You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter. Example: `MToxMA==`

`sort_order`

(optional) Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Sort on this field. You can specify one sort order only. The default sort field is `TIMECREATED`. The default sort order for `TIMECREATED` is descending, and the default sort order for `DISPLAYNAME` is ascending.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Returns a page of errors for the specified work request. If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The identifier of the asynchronous work request.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`page`

(optional) The page at which to start retrieving results. You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter. Example: `MToxMA==`

`limit`

(optional) The maximum number of items to return per page.

`sort_by`

(optional) The field to sort by. You can specify only one sort order. If no value is specified, then the default is `TIMESTAMP`. The default sort order for both `TIMESTAMP` and `CODE` is ascending.

Allowed values are: 'CODE', 'TIMESTAMP'

`sort_order`

(optional) Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Returns a page of of log messages for a given work request. If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The identifier of the asynchronous work request.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`page`

(optional) The page at which to start retrieving results. You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter. Example: `MToxMA==`

`limit`

(optional) The maximum number of items to return per page.

`sort_by`

(optional) The field to sort by. You can specify only one sort order. If no value is specified, then the default is `TIMESTAMP`. The default sort order for both `TIMESTAMP` and `MESSAGE` is ascending.

Allowed values are: 'MESSAGE', 'TIMESTAMP'

`sort_order`

(optional) Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

Returns a page of work requests for the specified compartment. If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) List the Digital Assistant instances that belong to this compartment.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`oda_instance_id`

(optional) List only the information for this Digital Assistant instance.

`resource_id`

(optional) List only the information for this resource.

`page`

(optional) The page at which to start retrieving results. You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter. Example: `MToxMA==`

`limit`

(optional) The maximum number of items to return per page.

`sort_by`

(optional) The field to sort by. You can specify only one sort order. If no value is specified, then the default is `TIME_ACCEPTED`. The default sort order for the time fields is descending. The default order for `DISPLAYNAME` and `STATUS` is ascending.default: TIME_ACCEPTED

Allowed values are: 'OPERATION_TYPE', 'STATUS', 'TIME_ACCEPTED', 'TIME_STARTED', 'TIME_FINISHED'

`sort_order`

(optional) Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### START_ODA_INSTANCE Function

Starts an inactive Digital Assistant instance. Once active, the instance will be accessible and metering of requests will be started again.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that you can retry the request if there's a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but they can become invalid before then if there are conflicting operations. For example, if an instance was deleted and purged from the system, then the service might reject a retry of the original creation request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### STOP_ODA_INSTANCE Function

Stops an active Digital Assistant instance. Once inactive, the instance will not be accessible and metering of requests will be stopped until the instance is started again. Data associated with the instance is not affected.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that you can retry the request if there's a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but they can become invalid before then if there are conflicting operations. For example, if an instance was deleted and purged from the system, then the service might reject a retry of the original creation request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ODA_INSTANCE Function

Updates the specified Digital Assistant instance with the information in the request body.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`update_oda_instance_details`

(required) The information to update.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ODA_INSTANCE_ATTACHMENT Function

Updates the ODA instance attachment

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`attachment_id`

(required) Unique Digital Assistant instance attachment identifier.

`update_oda_instance_attachment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [ODA Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_oda.html#ADSDK-GUID-C7B4D4FA-4934-47EF-AA33-63F53001B767)
- [CHANGE_ODA_INSTANCE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_oda.html#ADSDK-GUID-F1976E0C-8A2A-448D-9AEF-75BC192EA485)
- [CREATE_ODA_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_oda.html#ADSDK-GUID-A7E0B800-421B-41BA-B3CA-2A4A650A1BF0)
- [CREATE_ODA_INSTANCE_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_oda.html#ADSDK-GUID-F96CE1AF-3764-4D57-8D77-1639AE65F179)
- [DELETE_ODA_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_oda.html#ADSDK-GUID-7D94E5EC-B140-4948-838E-022521D90FDF)
- [DELETE_ODA_INSTANCE_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_oda.html#ADSDK-GUID-F31B9D95-C794-4CF7-9CD4-8238EC6DD691)
- [GET_ODA_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_oda.html#ADSDK-GUID-86F55CD2-297B-480E-99D0-C67F739B14C7)
- [GET_ODA_INSTANCE_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_oda.html#ADSDK-GUID-F26C3F3B-68FD-4857-9A9E-5E2599826C2C)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_oda.html#ADSDK-GUID-2E45A578-FFEA-4160-B6FF-30504CB672BD)
- [LIST_ODA_INSTANCE_ATTACHMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_oda.html#ADSDK-GUID-AB77B471-50D5-4390-9895-FBF79F6317D9)
- [LIST_ODA_INSTANCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_oda.html#ADSDK-GUID-946F287C-C0A9-4A16-89FF-199E2ADFF95D)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_oda.html#ADSDK-GUID-55835BED-B8B6-4C57-9921-3C7CF35CCC16)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_oda.html#ADSDK-GUID-EF36D31C-7A0D-4A9D-BA4A-1801D4E0D199)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_oda.html#ADSDK-GUID-D4C94EC1-5B1E-4943-833E-BFBBBE27F91C)
- [START_ODA_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_oda.html#ADSDK-GUID-3BA0CD14-80AA-45A2-A91B-F8B28FE1D0B1)
- [STOP_ODA_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_oda.html#ADSDK-GUID-37EFBF4C-49AB-4ABA-B9EB-8B0EC3ECF0A3)
- [UPDATE_ODA_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_oda.html#ADSDK-GUID-2628522E-0665-481A-9CFE-077A2057A8A2)
- [UPDATE_ODA_INSTANCE_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_oda.html#ADSDK-GUID-9D33B82A-2C6F-4A49-881A-E184FFC4672A)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
