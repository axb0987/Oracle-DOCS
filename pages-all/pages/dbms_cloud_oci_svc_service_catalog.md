# Service Catalog Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html
- Fetched: 2026-09-05 19:14 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#dcoc-content-body)

## Service Catalog Functions

Package: DBMS_CLOUD_OCI_SVC_SERVICE_CATALOG

### BULK_REPLACE_SERVICE_CATALOG_ASSOCIATIONS Function

Replace all associations of a given service catalog in one bulk transaction.

Syntax
```

```

Parameters

Parameter Description

`service_catalog_id`

(required) The unique identifier for the service catalog.

`bulk_replace_service_catalog_associations_details`

(required) Details of the service catalog update operation.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_PRIVATE_APPLICATION_COMPARTMENT Function

Moves the specified private application from one compartment to another.

Syntax
```

```

Parameters

Parameter Description

`private_application_id`

(required) The unique identifier for the private application.

`change_private_application_compartment_details`

(required) The details of the request to change the compartment of a given private application.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_SERVICE_CATALOG_COMPARTMENT Function

Moves the specified service catalog from one compartment to another.

Syntax
```

```

Parameters

Parameter Description

`service_catalog_id`

(required) The unique identifier for the service catalog.

`change_service_catalog_compartment_details`

(required) The details of the request to change the compartment of a given service catalog.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PRIVATE_APPLICATION Function

Creates a private application along with a single package to be hosted.

Syntax
```

```

Parameters

Parameter Description

`create_private_application_details`

(required) Private application creation details.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SERVICE_CATALOG Function

Creates a brand new service catalog in a given compartment.

Syntax
```

```

Parameters

Parameter Description

`create_service_catalog_details`

(required) The details for creating a service catalog.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SERVICE_CATALOG_ASSOCIATION Function

Creates an association between service catalog and a resource.

Syntax
```

```

Parameters

Parameter Description

`create_service_catalog_association_details`

(required) The details for creating the association between resource and service catalog.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PRIVATE_APPLICATION Function

Deletes an existing private application.

Syntax
```

```

Parameters

Parameter Description

`private_application_id`

(required) The unique identifier for the private application.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SERVICE_CATALOG Function

Deletes the specified service catalog from the compartment.

Syntax
```

```

Parameters

Parameter Description

`service_catalog_id`

(required) The unique identifier for the service catalog.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SERVICE_CATALOG_ASSOCIATION Function

Removes an association between service catalog and a resource.

Syntax
```

```

Parameters

Parameter Description

`service_catalog_association_id`

(required) The unique identifier of the service catalog association.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PRIVATE_APPLICATION Function

Gets the details of the specified private application.

Syntax
```

```

Parameters

Parameter Description

`private_application_id`

(required) The unique identifier for the private application.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PRIVATE_APPLICATION_ACTION_DOWNLOAD_LOGO Function

Downloads the binary payload of the logo image of the private application.

Syntax
```

```

Parameters

Parameter Description

`private_application_id`

(required) The unique identifier for the private application.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PRIVATE_APPLICATION_PACKAGE Function

Gets the details of a specific package within a given private application.

Syntax
```

```

Parameters

Parameter Description

`private_application_package_id`

(required) The unique identifier for the private application package.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PRIVATE_APPLICATION_PACKAGE_ACTION_DOWNLOAD_CONFIG Function

Downloads the configuration that was used to create the private application package.

Syntax
```

```

Parameters

Parameter Description

`private_application_package_id`

(required) The unique identifier for the private application package.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SERVICE_CATALOG Function

Gets detailed information about the service catalog including name, compartmentId

Syntax
```

```

Parameters

Parameter Description

`service_catalog_id`

(required) The unique identifier for the service catalog.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SERVICE_CATALOG_ASSOCIATION Function

Gets detailed information about specific service catalog association.

Syntax
```

```

Parameters

Parameter Description

`service_catalog_association_id`

(required) The unique identifier of the service catalog association.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets the status of the work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_APPLICATIONS Function

Lists all the applications in a service catalog or a tenancy. If no parameter is specified, all catalogs from all compartments in the tenancy will be scanned for any type of content.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The unique identifier for the compartment.

`service_catalog_id`

(optional) The unique identifier for the service catalog.

`entity_type`

(optional) The type of the application in the service catalog.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`display_name`

(optional) Exact match name filter.

`entity_id`

(optional) The unique identifier of the entity associated with service catalog.

`publisher_id`

(optional) Limit results to just this publisher.

`package_type`

(optional) Name of the package type. If multiple package types are provided, then any resource with one or more matching package types will be returned.

Allowed values are: 'STACK'

`pricing`

(optional) Name of the pricing type. If multiple pricing types are provided, then any resource with one or more matching pricing models will be returned.

Allowed values are: 'FREE', 'BYOL', 'PAYGO'

`is_featured`

(optional) Indicates whether to show only featured resources. If this is set to `false` or is omitted, then all resources will be returned.

`sort_order`

(optional) The sort order to apply, either `ASC` or `DESC`. Default is `ASC`.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PRIVATE_APPLICATION_PACKAGES Function

Lists the packages in the specified private application.

Syntax
```

```

Parameters

Parameter Description

`private_application_id`

(required) The unique identifier for the private application.

`private_application_package_id`

(optional) The unique identifier for the private application package.

`package_type`

(optional) Name of the package type. If multiple package types are provided, then any resource with one or more matching package types will be returned.

Allowed values are: 'STACK'

`limit`

(optional) How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`sort_by`

(optional) The field to use to sort listed results. You can only specify one field to sort by. `TIMECREATED` displays results in descending order by default. You can change your preference by specifying a different sort order.

Allowed values are: 'TIMECREATED', 'VERSION'

`sort_order`

(optional) The sort order to apply, either `ASC` or `DESC`. Default is `ASC`.

Allowed values are: 'ASC', 'DESC'

`display_name`

(optional) Exact match name filter.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PRIVATE_APPLICATIONS Function

Lists all the private applications in a given compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The unique identifier for the compartment.

`private_application_id`

(optional) The unique identifier for the private application.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`sort_by`

(optional) The field to use to sort listed results. You can only specify one field to sort by. Default is `TIMECREATED`.

Allowed values are: 'TIMECREATED', 'LIFECYCLESTATE'

`sort_order`

(optional) The sort order to apply, either `ASC` or `DESC`. Default is `ASC`.

Allowed values are: 'ASC', 'DESC'

`display_name`

(optional) Exact match name filter.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SERVICE_CATALOG_ASSOCIATIONS Function

Lists all the resource associations for a specific service catalog.

Syntax
```

```

Parameters

Parameter Description

`service_catalog_association_id`

(optional) The unique identifier for the service catalog association.

`service_catalog_id`

(optional) The unique identifier for the service catalog.

`entity_id`

(optional) The unique identifier of the entity associated with service catalog.

`entity_type`

(optional) The type of the application in the service catalog.

`limit`

(optional) How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`sort_order`

(optional) The sort order to apply, either `ASC` or `DESC`. Default is `ASC`.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Default is `TIMECREATED`

Allowed values are: 'TIMECREATED'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SERVICE_CATALOGS Function

Lists all the service catalogs in the given compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The unique identifier for the compartment.

`service_catalog_id`

(optional) The unique identifier for the service catalog.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`sort_by`

(optional) Default is `TIMECREATED`

Allowed values are: 'TIMECREATED'

`sort_order`

(optional) The sort order to apply, either `ASC` or `DESC`. Default is `ASC`.

Allowed values are: 'ASC', 'DESC'

`display_name`

(optional) Exact match name filter.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Return a (paginated) list of errors for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`sort_order`

(optional) The sort order to apply, either `ASC` or `DESC`. Default is `ASC`.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Return a (paginated) list of logs for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`sort_order`

(optional) The sort order to apply, either `ASC` or `DESC`. Default is `ASC`.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

Lists the work requests in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The unique identifier for the compartment.

`work_request_id`

(optional) The ID of the asynchronous work request.

`status`

(optional) A filter to return only resources their lifecycleState matches the given OperationStatus.

Allowed values are: 'ACCEPTED', 'FAILED', 'SUCCEEDED'

`resource_id`

(optional) The ID of the resource affected by the work request

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

`sort_order`

(optional) The sort order to apply, either `ASC` or `DESC`. Default is `ASC`.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PRIVATE_APPLICATION Function

Updates the details of an existing private application.

Syntax
```

```

Parameters

Parameter Description

`private_application_id`

(required) The unique identifier for the private application.

`update_private_application_details`

(required) The details for updating the private application.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SERVICE_CATALOG Function

Updates the details of a previously created service catalog.

Syntax
```

```

Parameters

Parameter Description

`service_catalog_id`

(required) The unique identifier for the service catalog.

`update_service_catalog_details`

(required) Details to update for a service catalog.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://service-catalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Service Catalog Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-783848BC-729A-430B-8D55-EF89D341E9DF)
- [BULK_REPLACE_SERVICE_CATALOG_ASSOCIATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-C2A0B292-EE99-450B-A5F6-B3FFFFB67C05)
- [CHANGE_PRIVATE_APPLICATION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-E93A368E-DB77-4F68-BCFA-24F473B6ABF1)
- [CHANGE_SERVICE_CATALOG_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-C26A70F3-AAE8-47C4-9739-B4869F48FCB5)
- [CREATE_PRIVATE_APPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-37CDED92-5929-4D8C-8FC7-59B8F94E7EEF)
- [CREATE_SERVICE_CATALOG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-F3BCBEE9-7690-4D0D-B698-6B2DC25FAB98)
- [CREATE_SERVICE_CATALOG_ASSOCIATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-B1DED312-1B69-4FDB-B5BF-FC62AB95F1ED)
- [DELETE_PRIVATE_APPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-614B9F36-090C-4571-BDC1-3475BFE91650)
- [DELETE_SERVICE_CATALOG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-7937C89A-CEA0-46EE-A962-1989F6439F40)
- [DELETE_SERVICE_CATALOG_ASSOCIATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-AE4E3014-102C-434E-A1AE-F4A1FA02CCD8)
- [GET_PRIVATE_APPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-32964EDE-1D34-4287-9EF8-237C876D4A1A)
- [GET_PRIVATE_APPLICATION_ACTION_DOWNLOAD_LOGO Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-EEC2F703-5731-4C55-B34F-4CEBBF811712)
- [GET_PRIVATE_APPLICATION_PACKAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-4A2BE19F-4E48-43CE-BE0E-F5E25394D708)
- [GET_PRIVATE_APPLICATION_PACKAGE_ACTION_DOWNLOAD_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-1B25DF63-980D-46B5-B95E-7A9899E4FCC1)
- [GET_SERVICE_CATALOG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-5BFD1CC0-C48E-4069-BC91-7BD3BA7B3C82)
- [GET_SERVICE_CATALOG_ASSOCIATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-30B88514-45D3-4D8A-90B4-35C265B06931)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-B4C84B8F-2C74-40FF-8676-59510D27DEDF)
- [LIST_APPLICATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-C2CD633E-1436-4814-ABB0-91F0C09FD70A)
- [LIST_PRIVATE_APPLICATION_PACKAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-EC27C7F3-3DFD-4FA2-8769-99EEC73FAB73)
- [LIST_PRIVATE_APPLICATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-69DC66E2-9C8D-4418-8D7E-0CBB3BB1439F)
- [LIST_SERVICE_CATALOG_ASSOCIATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-877EDD7D-9CD1-458A-9753-916CBCF6D8F2)
- [LIST_SERVICE_CATALOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-8AA383BA-52B7-4285-B1DA-75A322B1C31B)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-6B8604FD-0770-4465-9347-B85636413C16)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-0FF4D61B-AC3D-4197-AF01-F3596DD4E3F1)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-5E82EF2A-DB60-4A80-85E2-0DD784223E89)
- [UPDATE_PRIVATE_APPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-C5E74E6E-D1CE-4D27-AB5F-51C7996CFDD1)
- [UPDATE_SERVICE_CATALOG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svc_service_catalog.html#ADSDK-GUID-FFDD8EF2-E9D2-45EE-978D-4BD6BE7EB1D6)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
