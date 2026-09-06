# Application Migration Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_am_application_migration.html
- Fetched: 2026-09-05 19:04 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_am_application_migration.html#dcoc-content-body)

## Application Migration Functions

Package: DBMS_CLOUD_OCI_AM_APPLICATION_MIGRATION

### CANCEL_WORK_REQUEST Function

Cancels the specified work request. When you cancel a work request, it causes the in-progress task to be canceled. For example, if the create migration work request is in the accepted or in progress state for a long time, you can cancel the work request. When you cancel a work request, the state of the work request changes to cancelling, and then to the cancelled state.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://applicationmigration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_MIGRATION_COMPARTMENT Function

Moves the specified migration into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`migration_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the migration.

`change_migration_compartment_details`

(required) The updated compartment details

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of retrying the same action. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://applicationmigration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_SOURCE_COMPARTMENT Function

Moves the specified source into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`source_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source.

`change_source_compartment_details`

(required) The updated compartment details

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of retrying the same action. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://applicationmigration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MIGRATION Function

Creates a migration. A migration represents the end-to-end workflow of moving an application from a source environment to Oracle Cloud Infrastructure. Each migration moves a single application to Oracle Cloud Infrastructure. For more information, see[Manage Migrations](https://docs.oracle.com/iaas/application-migration/manage_migrations.htm). When you create a migration, provide the required information to let Application Migration access the source environment. Application Migration uses this information to access the application in the source environment and discover application artifacts. All Oracle Cloud Infrastructure resources, including migrations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. For more information, see Resource Identifiers. After you send your request, a migration is created in the compartment that contains the source. The new migration's lifecycle state will temporarily be &lt;code&gt;CREATING&lt;/code&gt; and the state of the migration will be &lt;code&gt;DISCOVERING_APPLICATION&lt;/code&gt;. During this phase, Application Migration sets the template for the &lt;code&gt;serviceConfig&lt;/code&gt; and &lt;code&gt;applicationConfig&lt;/code&gt; fields of the migration. When this operation is complete, the state of the migration changes to &lt;code&gt;MISSING_CONFIG_VALUES&lt;/code&gt;. Next, you'll need to update the migration to provide configuration values. Before updating the migration, ensure that its state has changed to &lt;code&gt;MISSING_CONFIG_VALUES&lt;/code&gt;. To track the progress of this operation, you can monitor the status of the Create Migration and Discover Application work requests by using the &lt;code&gt;`GET_WORK_REQUEST`Function&lt;/code&gt; REST API operation on the work request or by viewing the status of the work request in the console.

Syntax
```

```

Parameters

Parameter Description

`create_migration_details`

(required) The properties for creating a migration.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of retrying the same action. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://applicationmigration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SOURCE Function

Creates a source in the specified compartment. In Application Migration, a source refers to the environment from which the application is being migrated. For more information, see[Manage Sources](https://docs.oracle.com/iaas/application-migration/manage_sources.htm). All Oracle Cloud Infrastructure resources, including sources, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. After you send your request, a source is created in the specified compartment. The new source's lifecycle state will temporarily be &lt;code&gt;CREATING&lt;/code&gt;. Application Migration connects to the source environment with the authentication credentials that you have provided. If the connection is established, the status of the source changes to &lt;code&gt;ACTIVE&lt;/code&gt; and Application Migration fetches the list of applications that are available for migration in the source environment. To track the progress of the operation, you can monitor the status of the Create Source work request by using the &lt;code&gt;`GET_WORK_REQUEST`Function&lt;/code&gt; REST API operation on the work request or by viewing the status of the work request in the console. Ensure that the state of the source has changed to &lt;code&gt;ACTIVE&lt;/code&gt;, before you retrieve the list of applications from the source environment using the &lt;code&gt;`LIST_SOURCE_APPLICATIONS`Function&lt;/code&gt; REST API call.

Syntax
```

```

Parameters

Parameter Description

`create_source_details`

(required) The properties for creating a source.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of retrying the same action. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://applicationmigration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MIGRATION Function

Deletes the specified migration. If you have migrated the application or for any other reason if you no longer require a migration, then you can delete the relevant migration. You can delete a migration, irrespective of its state. If any work request is being processed for the migration that you want to delete, then the associated work requests are cancelled and then the migration is deleted.

Syntax
```

```

Parameters

Parameter Description

`migration_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the migration.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://applicationmigration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SOURCE Function

Deletes the specified source. Before deleting a source, you must delete all the migrations associated with the source. If you have migrated all the required applications in a source or for any other reason you no longer require a source, then you can delete the relevant source.

Syntax
```

```

Parameters

Parameter Description

`source_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://applicationmigration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MIGRATION Function

Retrieves details of the specified migration.

Syntax
```

```

Parameters

Parameter Description

`migration_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the migration.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://applicationmigration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SOURCE Function

Retrieves details of the specified source. Specify the OCID of the source for which you want to retrieve details.

Syntax
```

```

Parameters

Parameter Description

`source_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://applicationmigration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://applicationmigration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MIGRATIONS Function

Retrieves details of all the migrations that are available in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a compartment. Retrieves details of objects in the specified compartment.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)on which to query for a migration.

`limit`

(optional) The number of items returned in a paginated `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field on which to sort. By default, `TIMECREATED` is ordered descending. By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`display_name`

(optional) Display name on which to query.

`lifecycle_state`

(optional) This field is not supported. Do not use.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'SUCCEEDED', 'DELETING', 'DELETED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://applicationmigration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SOURCE_APPLICATIONS Function

Retrieves details of all the applications associated with the specified source. This list is generated dynamically by interrogating the source and the list changes as applications are started or stopped in the source environment.

Syntax
```

```

Parameters

Parameter Description

`source_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a compartment. Retrieves details of objects in the specified compartment.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) The number of items returned in a paginated `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field on which to sort. By default, `TIMECREATED` is ordered descending. By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`display_name`

(optional) Resource name on which to query.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://applicationmigration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SOURCES Function

Retrieves details of all the sources that are available in the specified compartment and match the specified query criteria. If you don't specify any query criteria, then details of all the sources are displayed. To filter the retrieved results, you can pass one or more of the following query parameters, by appending them to the URI as shown in the following example.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a compartment. Retrieves details of objects in the specified compartment.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)on which to query for a source.

`limit`

(optional) The number of items returned in a paginated `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field on which to sort. By default, `TIMECREATED` is ordered descending. By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`display_name`

(optional) Display name on which to query.

`lifecycle_state`

(optional) Retrieves details of sources in the specified lifecycle state.

Allowed values are: 'CREATING', 'DELETING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://applicationmigration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Retrieves details of the errors encountered while executing an operation that is tracked by the specified work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`limit`

(optional) The number of items returned in a paginated `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://applicationmigration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Retrieves logs for the specified work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`limit`

(optional) The number of items returned in a paginated `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order, either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://applicationmigration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

Retrieves details of all the work requests and match the specified query criteria. To filter the retrieved results, you can pass one or more of the following query parameters, by appending them to the URI as shown in the following example.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a compartment. Retrieves details of objects in the specified compartment.

`resource_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for a resource. Retrieves details of the specified resource.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) The number of items returned in a paginated `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://applicationmigration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### MIGRATE_APPLICATION Function

Starts migrating the specified application to Oracle Cloud Infrastructure. Before sending this request, ensure that you have provided configuration details to update the migration and the state of the migration is &lt;code&gt;READY&lt;/code&gt;. After you send this request, the migration's state will temporarily be &lt;code&gt;MIGRATING&lt;/code&gt;. To track the progress of the operation, you can monitor the status of the Migrate Application work request by using the &lt;code&gt;`GET_WORK_REQUEST`Function&lt;/code&gt; REST API operation on the work request or by viewing the status of the work request in the console. When this work request is processed successfully, Application Migration creates the required resources in the target environment and the state of the migration changes to &lt;code&gt;MIGRATION_SUCCEEDED&lt;/code&gt;.

Syntax
```

```

Parameters

Parameter Description

`migration_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the migration.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of retrying the same action. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://applicationmigration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MIGRATION Function

Updates the configuration details for the specified migration. When you create a migration, Application Migration sets the template for the &lt;code&gt;serviceConfig&lt;/code&gt; and &lt;code&gt;applicationConfig&lt;/code&gt; attributes of the migration. When you update the migration, you must provide values for these fields to specify configuration information for the application in the target environment. Before updating the migration, complete the following tasks: &lt;ol&gt; &lt;li&gt;Identify the migration that you want to update and ensure that the migration is in the &lt;code&gt;MISSING_CONFIG_VALUES&lt;/code&gt; state.&lt;/li&gt; &lt;li&gt;Get details of the migration using the &lt;code&gt;GetMigration&lt;/code&gt; command. This returns the template for the &lt;code&gt;serviceConfig&lt;/code&gt; and &lt;code&gt;applicationConfig&lt;/code&gt; attributes of the migration.&lt;/li&gt; &lt;li&gt;You must fill out the required details for the &lt;code&gt;serviceConfig&lt;/code&gt; and &lt;code&gt;applicationConfig&lt;/code&gt; attributes. The &lt;code&gt;isRequired&lt;/code&gt; attribute of a configuration property indicates whether it is mandatory to provide a value.&lt;/li&gt; &lt;li&gt;You can provide values for the optional configuration properties or you can delete the optional properties for which you do not provide values. Note that you cannot add any property that is not present in the template.&lt;/li&gt; &lt;/ol&gt; To update the migration, pass the configuration values in the request body. The information that you must provide depends on the type of application that you are migrating. For reference information about configuration fields, see[Provide Configuration Information](https://docs.oracle.com/iaas/application-migration/manage_migrations.htm#provide_configuration_details). To track the progress of the operation, you can monitor the status of the Update Migration work request by using the &lt;code&gt;`GET_WORK_REQUEST`Function&lt;/code&gt; REST API operation on the work request or by viewing the status of the work request in the console. When the migration has been updated, the state of the migration changes to &lt;code&gt;READY&lt;/code&gt;. After updating the migration, you can start the migration whenever you are ready.

Syntax
```

```

Parameters

Parameter Description

`migration_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the migration.

`update_migration_details`

(required) Updated configuration for the migration.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of retrying the same action. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected.

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://applicationmigration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SOURCE Function

You can update the authorization details to access the source environment from which you want to migrate applications to Oracle Cloud Infrastructure. You can also update the description and tags of a source. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Parameters

Parameter Description

`source_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source.

`update_source_details`

(required) Updated configuration for the source.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://applicationmigration.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Application Migration Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_am_application_migration.html#ADSDK-GUID-6563FF72-D95C-4E6B-8D90-0214F700368A)
- [CANCEL_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_am_application_migration.html#ADSDK-GUID-80CBEAE7-089B-47C3-95E7-97ED0EBDF6BA)
- [CHANGE_MIGRATION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_am_application_migration.html#ADSDK-GUID-B8143F26-3F71-4F9C-BB6F-C63C7601D46F)
- [CHANGE_SOURCE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_am_application_migration.html#ADSDK-GUID-4B45192B-E15C-4C3A-AEA9-217C3E80F47B)
- [CREATE_MIGRATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_am_application_migration.html#ADSDK-GUID-69838432-5631-4862-9935-6C85FDAA7101)
- [CREATE_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_am_application_migration.html#ADSDK-GUID-83DC04B4-FA90-4BE7-AAA7-7C7A45BF2A03)
- [DELETE_MIGRATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_am_application_migration.html#ADSDK-GUID-9656712F-DC95-41F9-BEF5-D7C54B2DCE62)
- [DELETE_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_am_application_migration.html#ADSDK-GUID-852D3F3A-1D58-43A4-AF31-477979389284)
- [GET_MIGRATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_am_application_migration.html#ADSDK-GUID-17CAFABE-B8F0-4B2B-99E3-FFB407BBC5DB)
- [GET_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_am_application_migration.html#ADSDK-GUID-CAF62E2A-F382-485A-A05D-64005C53FA60)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_am_application_migration.html#ADSDK-GUID-7D9E00A2-2125-46C5-9214-72AC5D9A31E8)
- [LIST_MIGRATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_am_application_migration.html#ADSDK-GUID-3F6CBB18-89AC-4AE9-97C0-B12C8453720B)
- [LIST_SOURCE_APPLICATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_am_application_migration.html#ADSDK-GUID-5A70E59B-5402-406F-9A76-32841710C19A)
- [LIST_SOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_am_application_migration.html#ADSDK-GUID-ECD3049C-C4CA-493B-A3C6-C2AAEFFA492D)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_am_application_migration.html#ADSDK-GUID-22BE16F6-148A-4379-94BB-E14BCB556F6D)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_am_application_migration.html#ADSDK-GUID-9F5A147C-1F8C-4C97-BC1D-0C9E145D5DEA)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_am_application_migration.html#ADSDK-GUID-A7421A95-D3C6-4B2B-96C1-E64DF1C57834)
- [MIGRATE_APPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_am_application_migration.html#ADSDK-GUID-8DB1C5D4-8794-4AEF-8C13-A1FBB37A4D53)
- [UPDATE_MIGRATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_am_application_migration.html#ADSDK-GUID-F179B3F4-C60A-4BA6-8745-35BD527B2903)
- [UPDATE_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_am_application_migration.html#ADSDK-GUID-CC124E43-76CF-419F-9A26-82F03326FB91)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
