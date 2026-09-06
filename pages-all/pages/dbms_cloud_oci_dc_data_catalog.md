# Data Catalog Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html
- Fetched: 2026-09-05 19:06 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#dcoc-content-body)

## Data Catalog Functions

Package: DBMS_CLOUD_OCI_DC_DATA_CATALOG

### ADD_CATALOG_LOCK Function

Adds a lock to a Catalog resource.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`add_resource_lock_details`

(required) AddResourceLockDetails body parameter

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_CATALOG_PRIVATE_ENDPOINT_LOCK Function

Adds a lock to a CatalogPrivateEndpoint resource.

Syntax
```

```

Parameters

Parameter Description

`catalog_private_endpoint_id`

(required) Unique private reverse connection identifier.

`add_resource_lock_details`

(required) AddResourceLockDetails body parameter

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_DATA_SELECTOR_PATTERNS Function

Add data selector pattern to the data asset.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`data_selector_pattern_details`

(required) The information used to add the patterns for deriving logical entities.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_METASTORE_LOCK Function

Adds a lock to a Metastore resource.

Syntax
```

```

Parameters

Parameter Description

`metastore_id`

(required) The metastore's OCID.

`add_resource_lock_details`

(required) AddResourceLockDetails body parameter

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ASSOCIATE_CUSTOM_PROPERTY Function

Associate the custom property for the given type

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`type_key`

(required) Unique type key.

`associate_custom_property_details`

(required) The information used to associate the custom property for the type.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ASYNCHRONOUS_EXPORT_GLOSSARY Function

Exports the contents of a glossary in Excel format. Returns details about the job which actually performs the export.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`glossary_key`

(required) Unique glossary key.

`asynchronous_export_glossary_details`

(required) Details needed by the glossary export request.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ATTACH_CATALOG_PRIVATE_ENDPOINT Function

Attaches a private reverse connection endpoint resource to a data catalog resource. When provided, 'If-Match' is checked against 'ETag' values of the resource.

Syntax
```

```

Parameters

Parameter Description

`attach_catalog_private_endpoint_details`

(required) Details for private reverse connection endpoint to be used for attachment.

`catalog_id`

(required) Unique catalog identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_CATALOG_COMPARTMENT Function

Moves a resource into a different compartment. When provided, 'If-Match' is checked against 'ETag' values of the resource.

Syntax
```

```

Parameters

Parameter Description

`change_catalog_compartment_details`

(required) Details for the target compartment.

`catalog_id`

(required) Unique catalog identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_CATALOG_PRIVATE_ENDPOINT_COMPARTMENT Function

Moves a resource into a different compartment. When provided, 'If-Match' is checked against 'ETag' values of the resource.

Syntax
```

```

Parameters

Parameter Description

`change_catalog_private_endpoint_compartment_details`

(required) Details for the target compartment.

`catalog_private_endpoint_id`

(required) Unique private reverse connection identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_METASTORE_COMPARTMENT Function

Moves a resource into a different compartment. When provided, 'If-Match' is checked against 'ETag' values of the resource.

Syntax
```

```

Parameters

Parameter Description

`change_metastore_compartment_details`

(required) Information about a change in metastore compartment.

`metastore_id`

(required) The metastore's OCID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ATTRIBUTE Function

Creates a new entity attribute.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`entity_key`

(required) Unique entity key.

`create_attribute_details`

(required) The information used to create an entity attribute.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ATTRIBUTE_TAG Function

Creates a new entity attribute tag.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`entity_key`

(required) Unique entity key.

`attribute_key`

(required) Unique attribute key.

`create_attribute_tag_details`

(required) The information used to create an entity attribute tag.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CATALOG Function

Creates a new data catalog instance that includes a console and an API URL for managing metadata operations. For more information, please see the documentation.

Syntax
```

```

Parameters

Parameter Description

`create_catalog_details`

(required) Details for the new data catalog.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CATALOG_PRIVATE_ENDPOINT Function

Create a new private reverse connection endpoint.

Syntax
```

```

Parameters

Parameter Description

`create_catalog_private_endpoint_details`

(required) The information used to create the private reverse connection.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CONNECTION Function

Creates a new connection.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`create_connection_details`

(required) The information used to create the connection.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CUSTOM_PROPERTY Function

Create a new Custom Property

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`namespace_id`

(required) Unique namespace identifier.

`create_custom_property_details`

(required) The information used to create the Custom Property.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DATA_ASSET Function

Create a new data asset.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`create_data_asset_details`

(required) The information used to create the data asset.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DATA_ASSET_TAG Function

Creates a new data asset tag.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`create_data_asset_tag_details`

(required) The information used to create the data asset tag.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ENTITY Function

Creates a new data entity.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`create_entity_details`

(required) The information used to create the data entity.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ENTITY_TAG Function

Creates a new entity tag.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`entity_key`

(required) Unique entity key.

`create_entity_tag_details`

(required) The information used to create the entity tag.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_FOLDER Function

Creates a new folder.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`create_folder_details`

(required) The information used to create the folder.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_FOLDER_TAG Function

Creates a new folder tag.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`folder_key`

(required) Unique folder key.

`create_folder_tag_details`

(required) The information used to create the folder tag.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_GLOSSARY Function

Creates a new glossary.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`create_glossary_details`

(required) The information used to create the glossary.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_JOB Function

Creates a new job.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`create_job_details`

(required) The information used to create the job.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_JOB_DEFINITION Function

Creates a new job definition.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`create_job_definition_details`

(required) The information used to create the job definition.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_JOB_EXECUTION Function

Creates a new job execution.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`job_key`

(required) Unique job key.

`create_job_execution_details`

(required) The information used to create the job execution.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_METASTORE Function

Creates a new metastore.

Syntax
```

```

Parameters

Parameter Description

`create_metastore_details`

(required) Information about a new metastore to be created.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_NAMESPACE Function

Create a new Namespace to be used by a custom property

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`create_namespace_details`

(required) The information used to create the Namespace.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PATTERN Function

Create a new pattern.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`create_pattern_details`

(required) The information used to create the pattern.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_TERM Function

Create a new term within a glossary.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`glossary_key`

(required) Unique glossary key.

`create_term_details`

(required) The information used to create the term.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_TERM_RELATIONSHIP Function

Creates a new term relationship for this term within a glossary.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`glossary_key`

(required) Unique glossary key.

`term_key`

(required) Unique glossary term key.

`create_term_relationship_details`

(required) The information used to create the term relationship.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ATTRIBUTE Function

Deletes a specific entity attribute.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`entity_key`

(required) Unique entity key.

`attribute_key`

(required) Unique attribute key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ATTRIBUTE_TAG Function

Deletes a specific entity attribute tag.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`entity_key`

(required) Unique entity key.

`attribute_key`

(required) Unique attribute key.

`tag_key`

(required) Unique tag key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CATALOG Function

Deletes a data catalog resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CATALOG_PRIVATE_ENDPOINT Function

Deletes a private reverse connection endpoint by identifier.

Syntax
```

```

Parameters

Parameter Description

`catalog_private_endpoint_id`

(required) Unique private reverse connection identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CONNECTION Function

Deletes a specific connection of a data asset.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`connection_key`

(required) Unique connection key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CUSTOM_PROPERTY Function

Deletes a specific custom property identified by it's key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`namespace_id`

(required) Unique namespace identifier.

`custom_property_key`

(required) Unique Custom Property key

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DATA_ASSET Function

Deletes a specific data asset identified by it's key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DATA_ASSET_TAG Function

Deletes a specific data asset tag.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`tag_key`

(required) Unique tag key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ENTITY Function

Deletes a specific data entity.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`entity_key`

(required) Unique entity key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ENTITY_TAG Function

Deletes a specific entity tag.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`entity_key`

(required) Unique entity key.

`tag_key`

(required) Unique tag key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_FOLDER Function

Deletes a specific folder of a data asset identified by it's key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`folder_key`

(required) Unique folder key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_FOLDER_TAG Function

Deletes a specific folder tag.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`folder_key`

(required) Unique folder key.

`tag_key`

(required) Unique tag key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_GLOSSARY Function

Deletes a specific glossary identified by it's key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`glossary_key`

(required) Unique glossary key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_JOB Function

Deletes a specific job identified by it's key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`job_key`

(required) Unique job key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_JOB_DEFINITION Function

Deletes a specific job definition identified by it's key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`job_definition_key`

(required) Unique job definition key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_METASTORE Function

Deletes a metastore resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`metastore_id`

(required) The metastore's OCID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_NAMESPACE Function

Deletes a specific Namespace identified by it's key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`namespace_id`

(required) Unique namespace identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PATTERN Function

Deletes a specific pattern identified by it's key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`pattern_key`

(required) Unique pattern key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_TERM Function

Deletes a specific glossary term.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`glossary_key`

(required) Unique glossary key.

`term_key`

(required) Unique glossary term key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_TERM_RELATIONSHIP Function

Deletes a specific glossary term relationship.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`glossary_key`

(required) Unique glossary key.

`term_key`

(required) Unique glossary term key.

`term_relationship_key`

(required) Unique glossary term relationship key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DETACH_CATALOG_PRIVATE_ENDPOINT Function

Detaches a private reverse connection endpoint resource to a data catalog resource. When provided, 'If-Match' is checked against 'ETag' values of the resource.

Syntax
```

```

Parameters

Parameter Description

`detach_catalog_private_endpoint_details`

(required) Details for private reverse connection endpoint to be used for attachment

`catalog_id`

(required) Unique catalog identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISASSOCIATE_CUSTOM_PROPERTY Function

Remove the custom property for the given type

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`type_key`

(required) Unique type key.

`disassociate_custom_property_details`

(required) The information used to remove the custom properties.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### EXPAND_TREE_FOR_GLOSSARY Function

Returns the fully expanded tree hierarchy of parent and child terms in this glossary.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`glossary_key`

(required) Unique glossary key.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### EXPORT_GLOSSARY Function

Export the glossary and the terms and return the exported glossary as csv or json.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`glossary_key`

(required) Unique glossary key.

`is_relationship_exported`

(optional) Specify if the relationship metadata is exported for the glossary.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### FETCH_ENTITY_LINEAGE Function

Returns lineage for a given entity object.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`entity_key`

(required) Unique entity key.

`fetch_entity_lineage_details`

(required) The information needed to obtain desired lineage.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ATTRIBUTE Function

Gets a specific entity attribute by key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`entity_key`

(required) Unique entity key.

`attribute_key`

(required) Unique attribute key.

`is_include_object_relationships`

(optional) Indicates whether the list of objects and their relationships to this object will be provided in the response.

`fields`

(optional) Specifies the fields to return in an entity attribute response.

Allowed values are: 'key', 'displayName', 'description', 'entityKey', 'lifecycleState', 'timeCreated', 'timeUpdated', 'createdById', 'updatedById', 'externalDataType', 'externalKey', 'isIncrementalData', 'isNullable', 'length', 'position', 'precision', 'scale', 'timeExternal', 'uri', 'properties', 'path', 'minCollectionCount', 'maxCollectionCount', 'datatypeEntityKey', 'externalDatatypeEntityKey', 'parentAttributeKey', 'externalParentAttributeKey', 'typeKey'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ATTRIBUTE_TAG Function

Gets a specific entity attribute tag by key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`entity_key`

(required) Unique entity key.

`attribute_key`

(required) Unique attribute key.

`tag_key`

(required) Unique tag key.

`fields`

(optional) Specifies the fields to return in an entity attribute tag response.

Allowed values are: 'key', 'name', 'termKey', 'termPath', 'termDescription', 'lifecycleState', 'timeCreated', 'createdById', 'uri', 'attributeKey'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CATALOG Function

Gets a data catalog by identifier.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CATALOG_PRIVATE_ENDPOINT Function

Gets a specific private reverse connection by identifier.

Syntax
```

```

Parameters

Parameter Description

`catalog_private_endpoint_id`

(required) Unique private reverse connection identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CONNECTION Function

Gets a specific data asset connection by key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`connection_key`

(required) Unique connection key.

`fields`

(optional) Specifies the fields to return in a connection response.

Allowed values are: 'key', 'displayName', 'description', 'dataAssetKey', 'typeKey', 'timeCreated', 'timeUpdated', 'createdById', 'updatedById', 'properties', 'externalKey', 'timeStatusUpdated', 'lifecycleState', 'isDefault', 'uri'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CUSTOM_PROPERTY Function

Gets a specific custom property for the given key within a data catalog.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`namespace_id`

(required) Unique namespace identifier.

`custom_property_key`

(required) Unique Custom Property key

`fields`

(optional) Specifies the fields to return in a custom property response.

Allowed values are: 'key', 'displayName', 'description', 'dataType', 'namespaceName', 'lifecycleState', 'timeCreated', 'timeUpdated', 'createdById', 'updatedById', 'properties'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATA_ASSET Function

Gets a specific data asset for the given key within a data catalog.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`fields`

(optional) Specifies the fields to return in a data asset response.

Allowed values are: 'key', 'displayName', 'description', 'catalogId', 'externalKey', 'typeKey', 'lifecycleState', 'timeCreated', 'timeUpdated', 'createdById', 'updatedById', 'uri', 'properties'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATA_ASSET_TAG Function

Gets a specific data asset tag by key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`tag_key`

(required) Unique tag key.

`fields`

(optional) Specifies the fields to return in a data asset tag response.

Allowed values are: 'key', 'name', 'termKey', 'termPath', 'termDescription', 'lifecycleState', 'timeCreated', 'createdById', 'uri', 'dataAssetKey'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ENTITY Function

Gets a specific data entity by key for a data asset.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`entity_key`

(required) Unique entity key.

`is_include_object_relationships`

(optional) Indicates whether the list of objects and their relationships to this object will be provided in the response.

`fields`

(optional) Specifies the fields to return in an entity response.

Allowed values are: 'key', 'displayName', 'description', 'dataAssetKey', 'timeCreated', 'timeUpdated', 'createdById', 'updatedById', 'lifecycleState', 'externalKey', 'timeExternal', 'timeStatusUpdated', 'isLogical', 'isPartition', 'folderKey', 'folderName', 'typeKey', 'path', 'harvestStatus', 'lastJobKey', 'uri', 'properties'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ENTITY_TAG Function

Gets a specific entity tag by key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`entity_key`

(required) Unique entity key.

`tag_key`

(required) Unique tag key.

`fields`

(optional) Specifies the fields to return in an entity tag response.

Allowed values are: 'key', 'name', 'termKey', 'termPath', 'termDescription', 'lifecycleState', 'timeCreated', 'createdById', 'uri', 'entityKey'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FOLDER Function

Gets a specific data asset folder by key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`folder_key`

(required) Unique folder key.

`is_include_object_relationships`

(optional) Indicates whether the list of objects and their relationships to this object will be provided in the response.

`fields`

(optional) Specifies the fields to return in a folder response.

Allowed values are: 'key', 'displayName', 'description', 'parentFolderKey', 'path', 'dataAssetKey', 'properties', 'externalKey', 'timeCreated', 'timeUpdated', 'createdById', 'updatedById', 'timeExternal', 'lifecycleState', 'harvestStatus', 'lastJobKey', 'uri'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FOLDER_TAG Function

Gets a specific folder tag by key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`folder_key`

(required) Unique folder key.

`tag_key`

(required) Unique tag key.

`fields`

(optional) Specifies the fields to return in a folder tag response.

Allowed values are: 'key', 'name', 'termKey', 'termPath', 'termDescription', 'lifecycleState', 'timeCreated', 'createdById', 'uri', 'folderKey'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_GLOSSARY Function

Gets a specific glossary by key within a data catalog.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`glossary_key`

(required) Unique glossary key.

`fields`

(optional) Specifies the fields to return in a glossary response.

Allowed values are: 'key', 'displayName', 'description', 'catalogId', 'lifecycleState', 'timeCreated', 'timeUpdated', 'createdById', 'updatedById', 'owner', 'workflowStatus', 'uri'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JOB Function

Gets a specific job by key within a data catalog.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`job_key`

(required) Unique job key.

`fields`

(optional) Specifies the fields to return in a job response.

Allowed values are: 'key', 'displayName', 'description', 'catalogId', 'lifecycleState', 'timeCreated', 'timeUpdated', 'jobType', 'scheduleCronExpression', 'timeScheduleBegin', 'timeScheduleEnd', 'scheduleType', 'connectionKey', 'jobDefinitionKey', 'internalVersion', 'executionCount', 'timeOfLatestExecution', 'executions', 'createdById', 'updatedById', 'uri', 'jobDefinitionName', 'errorCode', 'errorMessage'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JOB_DEFINITION Function

Gets a specific job definition by key within a data catalog.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`job_definition_key`

(required) Unique job definition key.

`fields`

(optional) Specifies the fields to return in a job definition response.

Allowed values are: 'key', 'displayName', 'description', 'catalogId', 'jobType', 'isIncremental', 'dataAssetKey', 'connectionKey', 'internalVersion', 'lifecycleState', 'timeCreated', 'timeUpdated', 'createdById', 'updatedById', 'uri', 'isSampleDataExtracted', 'sampleDataSizeInMBs', 'timeLatestExecutionStarted', 'timeLatestExecutionEnded', 'jobExecutionState', 'scheduleType', 'properties'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JOB_EXECUTION Function

Gets a specific job execution by key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`job_key`

(required) Unique job key.

`job_execution_key`

(required) The key of the job execution.

`fields`

(optional) Specifies the fields to return in a job execution response.

Allowed values are: 'key', 'jobKey', 'jobType', 'subType', 'parentKey', 'scheduleInstanceKey', 'lifecycleState', 'timeCreated', 'timeStarted', 'timeEnded', 'errorCode', 'errorMessage', 'processKey', 'externalUrl', 'eventKey', 'dataEntityKey', 'createdById', 'updatedById', 'properties', 'uri'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JOB_LOG Function

Gets a specific job log by key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`job_key`

(required) Unique job key.

`job_execution_key`

(required) The key of the job execution.

`job_log_key`

(required) Unique job log key.

`fields`

(optional) Specifies the fields to return in a job log response.

Allowed values are: 'key', 'jobExecutionKey', 'createdById', 'updatedById', 'timeUpdated', 'timeCreated', 'severity', 'logMessage', 'uri'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JOB_METRICS Function

Gets a specific job metric by key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`job_key`

(required) Unique job key.

`job_execution_key`

(required) The key of the job execution.

`job_metrics_key`

(required) Unique job metrics key.

`fields`

(optional) Specifies the fields to return in a job metric response.

Allowed values are: 'key', 'description', 'displayName', 'timeInserted', 'category', 'subCategory', 'unit', 'value', 'batchKey', 'jobExecutionKey', 'createdById', 'updatedById', 'timeUpdated', 'timeCreated', 'uri'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_METASTORE Function

Gets a metastore by identifier.

Syntax
```

```

Parameters

Parameter Description

`metastore_id`

(required) The metastore's OCID.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_NAMESPACE Function

Gets a specific namespace for the given key within a data catalog.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`namespace_id`

(required) Unique namespace identifier.

`fields`

(optional) Specifies the fields to return in a namespace response.

Allowed values are: 'key', 'displayName', 'description', 'lifecycleState', 'timeCreated', 'timeUpdated', 'createdById', 'updatedById', 'properties'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PATTERN Function

Gets a specific pattern for the given key within a data catalog.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`pattern_key`

(required) Unique pattern key.

`fields`

(optional) Specifies the fields to return in a pattern response.

Allowed values are: 'key', 'displayName', 'description', 'catalogId', 'expression', 'lifecycleState', 'timeCreated', 'timeUpdated', 'createdById', 'updatedById', 'properties'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TERM Function

Gets a specific glossary term by key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`glossary_key`

(required) Unique glossary key.

`term_key`

(required) Unique glossary term key.

`fields`

(optional) Specifies the fields to return in a term response.

Allowed values are: 'key', 'displayName', 'description', 'glossaryKey', 'parentTermKey', 'isAllowedToHaveChildTerms', 'path', 'lifecycleState', 'timeCreated', 'timeUpdated', 'createdById', 'updatedById', 'owner', 'workflowStatus', 'uri', 'relatedTerms', 'associatedObjectCount', 'associatedObjects'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TERM_RELATIONSHIP Function

Gets a specific glossary term relationship by key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`glossary_key`

(required) Unique glossary key.

`term_key`

(required) Unique glossary term key.

`term_relationship_key`

(required) Unique glossary term relationship key.

`fields`

(optional) Specifies the fields to return in a term relationship response.

Allowed values are: 'key', 'displayName', 'description', 'relatedTermKey', 'relatedTermDisplayName', 'parentTermKey', 'parentTermDisplayName', 'lifecycleState', 'timeCreated', 'uri'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TYPE Function

Gets a specific type by key within a data catalog.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`type_key`

(required) Unique type key.

`fields`

(optional) Specifies the fields to return in a type response.

Allowed values are: 'key', 'description', 'name', 'catalogId', 'properties', 'isInternal', 'isTag', 'isApproved', 'typeCategory', 'externalTypeName', 'lifecycleState', 'uri'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets the status of the work request with the given OCID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### IMPORT_CONNECTION Function

Import new connection for this data asset.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`import_connection_details`

(required) The information used to create the connections through import.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### IMPORT_DATA_ASSET Function

Import technical objects to a Data Asset

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`import_data_asset_details`

(required) The file contents to be imported.

`import_type`

(required) Type of import.

Allowed values are: 'CUSTOM_PROPERTY_VALUES', 'ALL'

`is_missing_value_ignored`

(optional) Specify whether to ignore the missing values in the import file.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### IMPORT_GLOSSARY Function

Import the glossary and the terms from csv or json files and return the imported glossary resource.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`glossary_key`

(required) Unique glossary key.

`import_glossary_details`

(required) The file contents to import the glossary.

`is_relationship_imported`

(optional) Specify if the relationship metadata is imported for the glossary.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AGGREGATED_PHYSICAL_ENTITIES Function

List the physical entities aggregated by this logical entity.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`entity_key`

(required) Unique entity key.

`fields`

(optional) Specifies the fields to return in an entity response.

Allowed values are: 'key', 'displayName', 'description', 'dataAssetKey', 'timeCreated', 'timeUpdated', 'createdById', 'updatedById', 'lifecycleState', 'externalKey', 'timeExternal', 'timeStatusUpdated', 'isLogical', 'isPartition', 'folderKey', 'folderName', 'typeKey', 'path', 'harvestStatus', 'lastJobKey', 'uri', 'properties'

`display_name_contains`

(optional) A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\" or has the pattern \"Cu\" anywhere in between.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`is_include_properties`

(optional) Indicates whether the properties map will be provided in the response.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ATTRIBUTE_TAGS Function

Returns a list of all tags for an entity attribute.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`entity_key`

(required) Unique entity key.

`attribute_key`

(required) Unique attribute key.

`name`

(optional) Immutable resource name.

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`term_key`

(optional) Unique key of the related term.

`term_path`

(optional) Path of the related term.

`time_created`

(optional) Time that the resource was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the resource.

`fields`

(optional) Specifies the fields to return in an entity attribute tag summary response.

Allowed values are: 'key', 'name', 'termKey', 'termPath', 'termDescription', 'lifecycleState', 'timeCreated', 'uri', 'glossaryKey', 'attributeKey'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ATTRIBUTES Function

Returns a list of all attributes of an data entity.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`entity_key`

(required) Unique entity key.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`business_name`

(optional) A filter to return only resources that match the entire business name given. The match is not case sensitive.

`display_or_business_name_contains`

(optional) A filter to return only resources that match display name or business name pattern given. The match is not case sensitive. For Example : /folders?displayOrBusinessNameContains=Cu.* The above would match all folders with display name or business name that starts with \"Cu\" or has the pattern \"Cu\" anywhere in between.

`display_name_contains`

(optional) A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\" or has the pattern \"Cu\" anywhere in between.

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`time_created`

(optional) Time that the resource was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_updated`

(optional) Time that the resource was updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the resource.

`updated_by_id`

(optional) OCID of the user who updated the resource.

`external_key`

(optional) Unique external identifier of this resource in the external source system.

`time_external`

(optional) Last modified timestamp of this object in the external system.

`external_type_name`

(optional) Data type as defined in an external system.

`is_incremental_data`

(optional) Identifies whether this attribute can be used as a watermark to extract incremental data.

`is_nullable`

(optional) Identifies whether this attribute can be assigned null value.

`length`

(optional) Max allowed length of the attribute value.

`position`

(optional) Position of the attribute in the record definition.

`precision`

(optional) Precision of the attribute value usually applies to float data type.

`scale`

(optional) Scale of the attribute value usually applies to float data type.

`fields`

(optional) Specifies the fields to return in an entity attribute summary response.

Allowed values are: 'key', 'displayName', 'description', 'entityKey', 'lifecycleState', 'timeCreated', 'externalDataType', 'externalKey', 'length', 'precision', 'scale', 'isNullable', 'uri', 'path', 'minCollectionCount', 'maxCollectionCount', 'datatypeEntityKey', 'externalDatatypeEntityKey', 'parentAttributeKey', 'externalParentAttributeKey', 'position', 'typeKey'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. DISPLAYORBUSINESSNAME considers businessName of a given object if set, else its displayName is used. Default sort order for TIMECREATED is descending and default sort order for DISPLAYNAME, POSITION and DISPLAYORBUSINESSNAME is ascending. If no order is specified, POSITION is the default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME', 'POSITION', 'DISPLAYORBUSINESSNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CATALOG_PRIVATE_ENDPOINTS Function

Returns a list of all the catalog private endpoints in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment where you want to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CATALOGS Function

Returns a list of all the data catalogs in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment where you want to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CONNECTIONS Function

Returns a list of all Connections for a data asset.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`display_name_contains`

(optional) A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\" or has the pattern \"Cu\" anywhere in between.

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`time_created`

(optional) Time that the resource was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_updated`

(optional) Time that the resource was updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the resource.

`updated_by_id`

(optional) OCID of the user who updated the resource.

`external_key`

(optional) Unique external identifier of this resource in the external source system.

`time_status_updated`

(optional) Time that the resource's status was last updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`is_default`

(optional) Indicates whether this connection is the default connection.

`fields`

(optional) Specifies the fields to return in a connection summary response.

Allowed values are: 'key', 'displayName', 'description', 'dataAssetKey', 'typeKey', 'timeCreated', 'externalKey', 'lifecycleState', 'isDefault', 'uri'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CUSTOM_PROPERTIES Function

Returns a list of custom properties within a data catalog.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`namespace_id`

(required) Unique namespace identifier.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`display_name_contains`

(optional) A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\" or has the pattern \"Cu\" anywhere in between.

`data_types`

(optional) Return the custom properties which has specified data types

Allowed values are: 'TEXT', 'RICH_TEXT', 'BOOLEAN', 'NUMBER', 'DATE'

`type_name`

(optional) A filter to return only resources that match the entire type name given. The match is not case sensitive

Allowed values are: 'DATA_ASSET', 'AUTONOMOUS_DATA_WAREHOUSE', 'HIVE', 'KAFKA', 'MYSQL', 'ORACLE_OBJECT_STORAGE', 'AUTONOMOUS_TRANSACTION_PROCESSING', 'ORACLE', 'POSTGRESQL', 'MICROSOFT_AZURE_SQL_DATABASE', 'MICROSOFT_SQL_SERVER', 'IBM_DB2', 'DATA_ENTITY', 'LOGICAL_ENTITY', 'TABLE', 'VIEW', 'ATTRIBUTE', 'FOLDER', 'ORACLE_ANALYTICS_SUBJECT_AREA_COLUMN', 'ORACLE_ANALYTICS_LOGICAL_COLUMN', 'ORACLE_ANALYTICS_PHYSICAL_COLUMN', 'ORACLE_ANALYTICS_ANALYSIS_COLUMN', 'ORACLE_ANALYTICS_SERVER', 'ORACLE_ANALYTICS_CLOUD', 'ORACLE_ANALYTICS_SUBJECT_AREA', 'ORACLE_ANALYTICS_DASHBOARD', 'ORACLE_ANALYTICS_BUSINESS_MODEL', 'ORACLE_ANALYTICS_PHYSICAL_DATABASE', 'ORACLE_ANALYTICS_PHYSICAL_SCHEMA', 'ORACLE_ANALYTICS_PRESENTATION_TABLE', 'ORACLE_ANALYTICS_LOGICAL_TABLE', 'ORACLE_ANALYTICS_PHYSICAL_TABLE', 'ORACLE_ANALYTICS_ANALYSIS', 'DATABASE_SCHEMA', 'TOPIC', 'CONNECTION', 'GLOSSARY', 'TERM', 'CATEGORY', 'FILE', 'BUCKET', 'MESSAGE', 'UNRECOGNIZED_FILE'

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`time_created`

(optional) Time that the resource was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_updated`

(optional) Time that the resource was updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the resource.

`updated_by_id`

(optional) OCID of the user who updated the resource.

`fields`

(optional) Specifies the fields to return in a custom property summary response.

Allowed values are: 'key', 'displayName', 'description', 'dataType', 'namespaceName', 'lifecycleState', 'timeCreated'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for USAGECOUNT and DISPLAYNAME is Ascending

Allowed values are: 'DISPLAYNAME', 'USAGECOUNT'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATA_ASSET_TAGS Function

Returns a list of all tags for a data asset.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`name`

(optional) Immutable resource name.

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`term_key`

(optional) Unique key of the related term.

`term_path`

(optional) Path of the related term.

`time_created`

(optional) Time that the resource was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the resource.

`fields`

(optional) Specifies the fields to return in a data asset tag summary response.

Allowed values are: 'key', 'name', 'termKey', 'termPath', 'termDescription', 'lifecycleState', 'timeCreated', 'uri', 'glossaryKey', 'dataAssetKey'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATA_ASSETS Function

Returns a list of data assets within a data catalog.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`display_name_contains`

(optional) A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\" or has the pattern \"Cu\" anywhere in between.

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`time_created`

(optional) Time that the resource was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_updated`

(optional) Time that the resource was updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the resource.

`updated_by_id`

(optional) OCID of the user who updated the resource.

`external_key`

(optional) Unique external identifier of this resource in the external source system.

`type_key`

(optional) The key of the object type.

`fields`

(optional) Specifies the fields to return in a data asset summary response.

Allowed values are: 'key', 'displayName', 'description', 'catalogId', 'externalKey', 'typeKey', 'lifecycleState', 'timeCreated', 'uri'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DERIVED_LOGICAL_ENTITIES Function

List logical entities derived from this pattern.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`pattern_key`

(required) Unique pattern key.

`display_name_contains`

(optional) A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\" or has the pattern \"Cu\" anywhere in between.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ENTITIES Function

Returns a list of all entities of a data asset.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`business_name`

(optional) A filter to return only resources that match the entire business name given. The match is not case sensitive.

`display_or_business_name_contains`

(optional) A filter to return only resources that match display name or business name pattern given. The match is not case sensitive. For Example : /folders?displayOrBusinessNameContains=Cu.* The above would match all folders with display name or business name that starts with \"Cu\" or has the pattern \"Cu\" anywhere in between.

`type_key`

(optional) The key of the object type.

`display_name_contains`

(optional) A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\" or has the pattern \"Cu\" anywhere in between.

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`time_created`

(optional) Time that the resource was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_updated`

(optional) Time that the resource was updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the resource.

`updated_by_id`

(optional) OCID of the user who updated the resource.

`external_key`

(optional) Unique external identifier of this resource in the external source system.

`pattern_key`

(optional) Unique pattern key.

`time_external`

(optional) Last modified timestamp of this object in the external system.

`time_status_updated`

(optional) Time that the resource's status was last updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`is_logical`

(optional) Identifies if the object is a physical object (materialized) or virtual/logical object defined on other objects.

`is_partition`

(optional) Identifies if an object is a sub object (partition) of a physical or materialized parent object.

`folder_key`

(optional) Key of the associated folder.

`path`

(optional) Full path of the resource for resources that support paths.

`harvest_status`

(optional) Harvest status of the harvestable resource as updated by the harvest process.

Allowed values are: 'COMPLETE', 'ERROR', 'IN_PROGRESS', 'DEFERRED'

`last_job_key`

(optional) Key of the last harvest process to update this resource.

`fields`

(optional) Specifies the fields to return in an entity summary response.

Allowed values are: 'key', 'displayName', 'description', 'dataAssetKey', 'timeCreated', 'timeUpdated', 'updatedById', 'lifecycleState', 'folderKey', 'folderName', 'externalKey', 'path', 'uri'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. DISPLAYORBUSINESSNAME considers businessName of a given object if set, else its displayName is used. Default sort order for TIMECREATED is descending and default sort order for DISPLAYNAME and DISPLAYORBUSINESSNAME is ascending. If no order is specified, TIMECREATED is the default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME', 'DISPLAYORBUSINESSNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ENTITY_TAGS Function

Returns a list of all tags for a data entity.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`entity_key`

(required) Unique entity key.

`name`

(optional) Immutable resource name.

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`term_key`

(optional) Unique key of the related term.

`term_path`

(optional) Path of the related term.

`time_created`

(optional) Time that the resource was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the resource.

`fields`

(optional) Specifies the fields to return in an entity tag summary response.

Allowed values are: 'key', 'name', 'termKey', 'termPath', 'termDescription', 'lifecycleState', 'timeCreated', 'uri', 'glossaryKey', 'entityKey'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FOLDER_TAGS Function

Returns a list of all tags for a folder.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`folder_key`

(required) Unique folder key.

`name`

(optional) Immutable resource name.

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`term_key`

(optional) Unique key of the related term.

`term_path`

(optional) Path of the related term.

`time_created`

(optional) Time that the resource was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the resource.

`fields`

(optional) Specifies the fields to return in a folder tag summary response.

Allowed values are: 'key', 'name', 'termKey', 'termPath', 'termDescription', 'lifecycleState', 'timeCreated', 'uri', 'glossaryKey', 'folderKey'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FOLDERS Function

Returns a list of all folders.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`business_name`

(optional) A filter to return only resources that match the entire business name given. The match is not case sensitive.

`display_or_business_name_contains`

(optional) A filter to return only resources that match display name or business name pattern given. The match is not case sensitive. For Example : /folders?displayOrBusinessNameContains=Cu.* The above would match all folders with display name or business name that starts with \"Cu\" or has the pattern \"Cu\" anywhere in between.

`display_name_contains`

(optional) A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\" or has the pattern \"Cu\" anywhere in between.

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`parent_folder_key`

(optional) Unique folder key.

`path`

(optional) Full path of the resource for resources that support paths.

`external_key`

(optional) Unique external identifier of this resource in the external source system.

`time_created`

(optional) Time that the resource was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_updated`

(optional) Time that the resource was updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the resource.

`updated_by_id`

(optional) OCID of the user who updated the resource.

`harvest_status`

(optional) Harvest status of the harvestable resource as updated by the harvest process.

Allowed values are: 'COMPLETE', 'ERROR', 'IN_PROGRESS', 'DEFERRED'

`last_job_key`

(optional) Key of the last harvest process to update this resource.

`fields`

(optional) Specifies the fields to return in a folder summary response.

Allowed values are: 'key', 'displayName', 'description', 'parentFolderKey', 'path', 'dataAssetKey', 'externalKey', 'timeExternal', 'timeCreated', 'lifecycleState', 'uri'

`type_key`

(optional) The key of the object type.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. DISPLAYORBUSINESSNAME considers businessName of a given object if set, else its displayName is used. Default sort order for TIMECREATED is descending and default sort order for DISPLAYNAME and DISPLAYORBUSINESSNAME is ascending. If no order is specified, TIMECREATED is the default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME', 'DISPLAYORBUSINESSNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_GLOSSARIES Function

Returns a list of all glossaries within a data catalog.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`display_name_contains`

(optional) A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\" or has the pattern \"Cu\" anywhere in between.

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`time_created`

(optional) Time that the resource was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_updated`

(optional) Time that the resource was updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the resource.

`updated_by_id`

(optional) OCID of the user who updated the resource.

`fields`

(optional) Specifies the fields to return in a glossary summary response.

Allowed values are: 'key', 'displayName', 'description', 'catalogId', 'lifecycleState', 'timeCreated', 'uri', 'workflowStatus'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_JOB_DEFINITIONS Function

Returns a list of job definitions within a data catalog.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`display_name_contains`

(optional) A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\" or has the pattern \"Cu\" anywhere in between.

`job_execution_state`

(optional) Job execution state.

Allowed values are: 'CREATED', 'IN_PROGRESS', 'INACTIVE', 'FAILED', 'SUCCEEDED', 'CANCELED', 'SUCCEEDED_WITH_WARNINGS'

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`job_type`

(optional) Job type.

Allowed values are: 'HARVEST', 'PROFILING', 'SAMPLING', 'PREVIEW', 'IMPORT', 'EXPORT', 'IMPORT_GLOSSARY', 'EXPORT_GLOSSARY', 'INTERNAL', 'PURGE', 'IMMEDIATE', 'SCHEDULED', 'IMMEDIATE_EXECUTION', 'SCHEDULED_EXECUTION', 'SCHEDULED_EXECUTION_INSTANCE', 'ASYNC_DELETE', 'IMPORT_DATA_ASSET', 'CREATE_SCAN_PROXY', 'ASYNC_EXPORT_GLOSSARY'

`is_incremental`

(optional) Whether job definition is an incremental harvest (true) or a full harvest (false).

`data_asset_key`

(optional) Unique data asset key.

`glossary_key`

(optional) Unique glossary key.

`connection_key`

(optional) Unique connection key.

`time_created`

(optional) Time that the resource was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_updated`

(optional) Time that the resource was updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the resource.

`updated_by_id`

(optional) OCID of the user who updated the resource.

`sample_data_size_in_m_bs`

(optional) The sample data size in MB, specified as number of rows, for a metadata harvest.

`fields`

(optional) Specifies the fields to return in a job definition summary response.

Allowed values are: 'key', 'displayName', 'description', 'catalogId', 'jobType', 'connectionKey', 'lifecycleState', 'timeCreated', 'isSampleDataExtracted', 'uri', 'timeLatestExecutionStarted', 'timeLatestExecutionEnded', 'jobExecutionState', 'scheduleType'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. Default order for TIMELATESTEXECUTIONSTARTED is descending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME', 'TIMELATESTEXECUTIONSTARTED'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_JOB_EXECUTIONS Function

Returns a list of job executions for a job.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`job_key`

(required) Unique job key.

`lifecycle_state`

(optional) Job execution lifecycle state.

Allowed values are: 'CREATED', 'IN_PROGRESS', 'INACTIVE', 'FAILED', 'SUCCEEDED', 'CANCELED', 'SUCCEEDED_WITH_WARNINGS'

`time_created`

(optional) Time that the resource was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_updated`

(optional) Time that the resource was updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the resource.

`updated_by_id`

(optional) OCID of the user who updated the resource.

`job_type`

(optional) Job type.

Allowed values are: 'HARVEST', 'PROFILING', 'SAMPLING', 'PREVIEW', 'IMPORT', 'EXPORT', 'IMPORT_GLOSSARY', 'EXPORT_GLOSSARY', 'INTERNAL', 'PURGE', 'IMMEDIATE', 'SCHEDULED', 'IMMEDIATE_EXECUTION', 'SCHEDULED_EXECUTION', 'SCHEDULED_EXECUTION_INSTANCE', 'ASYNC_DELETE', 'IMPORT_DATA_ASSET', 'CREATE_SCAN_PROXY', 'ASYNC_EXPORT_GLOSSARY'

`sub_type`

(optional) Sub-type of this job execution.

`parent_key`

(optional) The unique key of the parent execution or null if this job execution has no parent.

`time_start`

(optional) Time that the job execution was started or in the case of a future time, the time when the job will start. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_end`

(optional) Time that the job execution ended or null if the job is still running or hasn't run yet. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`error_code`

(optional) Error code returned from the job execution or null if job is still running or didn't return an error.

`error_message`

(optional) Error message returned from the job execution or null if job is still running or didn't return an error.

`process_key`

(optional) Process identifier related to the job execution.

`external_url`

(optional) The a URL of the job for accessing this resource and its status.

`event_key`

(optional) Event that triggered the execution of this job or null.

`data_entity_key`

(optional) Unique entity key.

`fields`

(optional) Specifies the fields to return in a job execution summary response.

Allowed values are: 'key', 'jobKey', 'jobType', 'parentKey', 'scheduleInstanceKey', 'lifecycleState', 'timeCreated', 'timeStarted', 'timeEnded', 'uri'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided; the default is descending. Use sortOrder query param to specify order.

Allowed values are: 'TIMECREATED'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_JOB_LOGS Function

Returns a list of job logs.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`job_key`

(required) Unique job key.

`job_execution_key`

(required) The key of the job execution.

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`severity`

(optional) Severity level for this Log.

`time_created`

(optional) Time that the resource was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_updated`

(optional) Time that the resource was updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the resource.

`updated_by_id`

(optional) OCID of the user who updated the resource.

`fields`

(optional) Specifies the fields to return in a job log summary response.

Allowed values are: 'key', 'jobExecutionKey', 'severity', 'timeCreated', 'logMessage', 'uri'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_JOB_METRICS Function

Returns a list of job metrics.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`job_key`

(required) Unique job key.

`job_execution_key`

(required) The key of the job execution.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`display_name_contains`

(optional) A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\" or has the pattern \"Cu\" anywhere in between.

`category`

(optional) Category of this metric.

`sub_category`

(optional) Sub category of this metric under the category. Used for aggregating values. May be null.

`unit`

(optional) Unit of this metric.

`value`

(optional) Value of this metric.

`batch_key`

(optional) Batch key for grouping, may be null.

`time_created`

(optional) Time that the resource was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_updated`

(optional) Time that the resource was updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_inserted`

(optional) The time the metric was logged or captured in the system where the job executed. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the resource.

`updated_by_id`

(optional) OCID of the user who updated the resource.

`fields`

(optional) Specifies the fields to return in a job metric summary response.

Allowed values are: 'key', 'description', 'displayName', 'timeInserted', 'category', 'subCategory', 'unit', 'value', 'batchKey', 'jobExecutionKey', 'timeCreated', 'uri'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_JOBS Function

Returns a list of jobs within a data catalog.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`display_name_contains`

(optional) A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\" or has the pattern \"Cu\" anywhere in between.

`lifecycle_state`

(optional) Job lifecycle state.

Allowed values are: 'ACTIVE', 'INACTIVE', 'EXPIRED'

`time_created`

(optional) Time that the resource was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_updated`

(optional) Time that the resource was updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the resource.

`updated_by_id`

(optional) OCID of the user who updated the resource.

`job_type`

(optional) Job type.

Allowed values are: 'HARVEST', 'PROFILING', 'SAMPLING', 'PREVIEW', 'IMPORT', 'EXPORT', 'IMPORT_GLOSSARY', 'EXPORT_GLOSSARY', 'INTERNAL', 'PURGE', 'IMMEDIATE', 'SCHEDULED', 'IMMEDIATE_EXECUTION', 'SCHEDULED_EXECUTION', 'SCHEDULED_EXECUTION_INSTANCE', 'ASYNC_DELETE', 'IMPORT_DATA_ASSET', 'CREATE_SCAN_PROXY', 'ASYNC_EXPORT_GLOSSARY'

`job_definition_key`

(optional) Unique job definition key.

`data_asset_key`

(optional) Unique data asset key.

`glossary_key`

(optional) Unique glossary key.

`schedule_cron_expression`

(optional) Interval on which the job will be run. Value is specified as a cron-supported time specification \"nickname\". The following subset of those is supported: @monthly, @weekly, @daily, @hourly. For metastore sync, an additional option @default is supported, which will schedule jobs at a more granular frequency.

`time_schedule_begin`

(optional) Date that the schedule should be operational. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_schedule_end`

(optional) Date that the schedule should end from being operational. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`schedule_type`

(optional) Type of the job schedule.

Allowed values are: 'SCHEDULED', 'IMMEDIATE'

`connection_key`

(optional) Unique connection key.

`fields`

(optional) Specifies the fields to return in a job summary response.

Allowed values are: 'key', 'displayName', 'description', 'catalogId', 'jobDefinitionKey', 'lifecycleState', 'timeCreated', 'timeUpdated', 'createdById', 'updatedById', 'jobType', 'scheduleCronExpression', 'timeScheduleBegin', 'scheduleType', 'executionCount', 'timeOfLatestExecution', 'executions', 'uri', 'jobDefinitionName', 'errorCode', 'errorMessage'

`execution_count`

(optional) The total number of executions for this job schedule.

`time_of_latest_execution`

(optional) The date and time the most recent execution for this job ,in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_METASTORES Function

Returns a list of all metastores in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment where you want to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_NAMESPACES Function

Returns a list of namespaces within a data catalog.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`display_name_contains`

(optional) A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\" or has the pattern \"Cu\" anywhere in between.

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`time_created`

(optional) Time that the resource was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_updated`

(optional) Time that the resource was updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the resource.

`updated_by_id`

(optional) OCID of the user who updated the resource.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`fields`

(optional) Specifies the fields to return in a namespace summary response.

Allowed values are: 'key', 'displayName', 'description', 'lifecycleState', 'timeCreated'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PATTERNS Function

Returns a list of patterns within a data catalog.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`display_name_contains`

(optional) A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\" or has the pattern \"Cu\" anywhere in between.

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`time_created`

(optional) Time that the resource was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_updated`

(optional) Time that the resource was updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the resource.

`updated_by_id`

(optional) OCID of the user who updated the resource.

`fields`

(optional) Specifies the fields to return in a pattern summary response.

Allowed values are: 'key', 'displayName', 'description', 'catalogId', 'expression', 'lifecycleState', 'timeCreated'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RULES Function

Returns a list of all rules of a data entity.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`entity_key`

(required) Unique entity key.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`display_name_contains`

(optional) A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\" or has the pattern \"Cu\" anywhere in between.

`rule_type`

(optional) Rule type used to filter the response to a list rules call.

Allowed values are: 'PRIMARYKEY', 'FOREIGNKEY', 'UNIQUEKEY'

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`origin_type`

(optional) Rule origin type used to filter the response to a list rules call.

Allowed values are: 'SOURCE', 'USER', 'PROFILING'

`external_key`

(optional) Unique external identifier of this resource in the external source system.

`time_created`

(optional) Time that the resource was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_updated`

(optional) Time that the resource was updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the resource.

`updated_by_id`

(optional) OCID of the user who updated the resource.

`fields`

(optional) Specifies the fields to return in a rule summary response.

Allowed values are: 'key', 'displayName', 'ruleType', 'externalKey', 'referencedFolderKey', 'referencedFolderName', 'referencedEntityKey', 'referencedEntityName', 'referencedRuleKey', 'referencedRuleName', 'originType', 'lifecycleState', 'timeCreated', 'uri'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TAGS Function

Returns a list of all user created tags in the system.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`display_name_contains`

(optional) A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\" or has the pattern \"Cu\" anywhere in between.

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`fields`

(optional) Specifies the fields to return in a term summary response.

Allowed values are: 'key', 'displayName', 'description', 'glossaryKey', 'parentTermKey', 'isAllowedToHaveChildTerms', 'path', 'lifecycleState', 'timeCreated', 'workflowStatus', 'associatedObjectCount', 'uri'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TERM_RELATIONSHIPS Function

Returns a list of all term relationships within a glossary.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`glossary_key`

(required) Unique glossary key.

`term_key`

(required) Unique glossary term key.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`display_name_contains`

(optional) A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\" or has the pattern \"Cu\" anywhere in between.

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`fields`

(optional) Specifies the fields to return in a term relationship summary response.

Allowed values are: 'key', 'displayName', 'description', 'relatedTermKey', 'relatedTermDisplayName', 'parentTermKey', 'parentTermDisplayName', 'lifecycleState', 'timeCreated', 'uri'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TERMS Function

Returns a list of all terms within a glossary.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`glossary_key`

(required) Unique glossary key.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`display_name_contains`

(optional) A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\" or has the pattern \"Cu\" anywhere in between.

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`parent_term_key`

(optional) Unique key of the parent term.

`is_allowed_to_have_child_terms`

(optional) Indicates whether a term may contain child terms.

`workflow_status`

(optional) Status of the approval workflow for this business term in the glossary.

Allowed values are: 'NEW', 'APPROVED', 'UNDER_REVIEW', 'ESCALATED'

`path`

(optional) Full path of the resource for resources that support paths.

`fields`

(optional) Specifies the fields to return in a term summary response.

Allowed values are: 'key', 'displayName', 'description', 'glossaryKey', 'parentTermKey', 'isAllowedToHaveChildTerms', 'path', 'lifecycleState', 'timeCreated', 'workflowStatus', 'associatedObjectCount', 'uri'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TYPES Function

Returns a list of all types within a data catalog.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`name`

(optional) Immutable resource name.

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`is_internal`

(optional) Indicates whether the type is internal, making it unavailable for use by metadata elements.

`is_tag`

(optional) Indicates whether the type can be used for tagging metadata elements.

`is_approved`

(optional) Indicates whether the type is approved for use as a classifying object.

`external_type_name`

(optional) Data type as defined in an external system.

`type_category`

(optional) Indicates the category of this type . For example, data assets or connections.

`fields`

(optional) Specifies the fields to return in a type summary response.

Allowed values are: 'key', 'description', 'name', 'catalogId', 'lifecycleState', 'typeCategory', 'uri'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Returns a (paginated) list of errors for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMESTAMP is descending. Default order for CODE and MESSAGE is ascending. If no value is specified TIMESTAMP is default.

Allowed values are: 'CODE', 'TIMESTAMP'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Returns a (paginated) list of logs for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMESTAMP is descending. Default order for MESSAGE is ascending. If no value is specified TIMESTAMP is default.

Allowed values are: 'MESSAGE', 'TIMESTAMP'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The OCID of the compartment where you want to list resources.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### OBJECT_STATS Function

Returns stats on objects by type in the repository.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PARSE_CONNECTION Function

Parse data asset references through connections from this data asset.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`parse_connection_details`

(required) The information used to parse the connections from payload or connection detail.

`connection_key`

(optional) Unique connection key.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PROCESS_RECOMMENDATION Function

Act on a recommendation. A recommendation can be accepted or rejected. For example, if a recommendation of type LINK_GLOSSARY_TERM is accepted, the system will link the source object (e.g. an attribute) to a target glossary term.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`process_recommendation_details`

(required) Recommendation to be processed.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RECOMMENDATIONS Function

Returns a list of recommendations for the given object and recommendation type. By default, it will return inferred recommendations for review. The optional query param 'RecommendationStatus' can be set, to return only recommendations having that status.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`recommendation_type`

(required) A filter used to return only recommendations of the specified type.

Allowed values are: 'LINK_GLOSSARY_TERM'

`source_object_key`

(required) A filter used to provide the unique identifier of the source object, for which a list of recommendations will be returned for review.

`source_object_type`

(required) A filter used to provide the type of the source object, for which a list of recommendations will be returned for review.

Allowed values are: 'DATA_ENTITY', 'ATTRIBUTE', 'TERM', 'CATEGORY'

`recommendation_status`

(optional) A filter used to return only recommendations having the requested status.

Allowed values are: 'ACCEPTED', 'REJECTED', 'INFERRED'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_CATALOG_LOCK Function

Removes a lock from a Catalog resource.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`remove_resource_lock_details`

(required) RemoveResourceLockDetails body parameter

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_CATALOG_PRIVATE_ENDPOINT_LOCK Function

Removes a lock from a CatalogPrivateEndpoint resource.

Syntax
```

```

Parameters

Parameter Description

`catalog_private_endpoint_id`

(required) Unique private reverse connection identifier.

`remove_resource_lock_details`

(required) RemoveResourceLockDetails body parameter

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_DATA_SELECTOR_PATTERNS Function

Remove data selector pattern from the data asset.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`data_selector_pattern_details`

(required) The information used to remove the data selector patterns.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_METASTORE_LOCK Function

Removes a lock from a Metastore resource.

Syntax
```

```

Parameters

Parameter Description

`metastore_id`

(required) The metastore's OCID.

`remove_resource_lock_details`

(required) RemoveResourceLockDetails body parameter

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SEARCH_CRITERIA Function

Returns a list of search results within a data catalog.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`search_criteria_details`

(optional) The information used to create an extended search results.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`name`

(optional) Immutable resource name.

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`timeout`

(optional) A search timeout string (for example, timeout=4000ms), bounding the search request to be executed within the specified time value and bail with the hits accumulated up to that point when expired. Defaults to no timeout.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUGGEST_MATCHES Function

Returns a list of potential string matches for a given input string.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`input_text`

(required) Text input string used for computing potential matching suggestions.

`timeout`

(optional) A search timeout string (for example, timeout=4000ms), bounding the search request to be executed within the specified time value and bail with the hits accumulated up to that point when expired. Defaults to no timeout.

`limit`

(optional) Limit for the list of potential matches returned from the Suggest API. If not specified, will default to 10.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SYNCHRONOUS_EXPORT_DATA_ASSET Function

Export technical objects from a Data Asset

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`synchronous_export_data_asset_details`

(required) The details of what needs to be exported.

`export_type`

(required) Type of export.

Allowed values are: 'CUSTOM_PROPERTY_VALUES', 'ALL'

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### TEST_CONNECTION Function

Test the connection by connecting to the data asset using credentials in the metadata.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`connection_key`

(required) Unique connection key.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ATTRIBUTE Function

Updates a specific data asset attribute.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`entity_key`

(required) Unique entity key.

`attribute_key`

(required) Unique attribute key.

`update_attribute_details`

(required) The information to be updated in the attribute.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CATALOG Function

Updates the data catalog.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`update_catalog_details`

(required) The data catalog information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CATALOG_PRIVATE_ENDPOINT Function

Updates the private reverse connection endpoint.

Syntax
```

```

Parameters

Parameter Description

`catalog_private_endpoint_id`

(required) Unique private reverse connection identifier.

`update_catalog_private_endpoint_details`

(required) The information to be updated in private reverse connection

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CONNECTION Function

Updates a specific connection of a data asset.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`connection_key`

(required) Unique connection key.

`update_connection_details`

(required) The information to be updated in the connection.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CUSTOM_PROPERTY Function

Updates a specific custom property identified by the given key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`namespace_id`

(required) Unique namespace identifier.

`custom_property_key`

(required) Unique Custom Property key

`update_custom_property_details`

(required) The information to be updated in the custom property.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DATA_ASSET Function

Updates a specific data asset identified by the given key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`update_data_asset_details`

(required) The information to be updated in the data asset.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ENTITY Function

Updates a specific data entity.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`entity_key`

(required) Unique entity key.

`update_entity_details`

(required) The information to be updated in the data entity.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_FOLDER Function

Updates a specific folder of a data asset.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`folder_key`

(required) Unique folder key.

`update_folder_details`

(required) The information to be updated in the folder.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_GLOSSARY Function

Updates a specific glossary identified by the given key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`glossary_key`

(required) Unique glossary key.

`update_glossary_details`

(required) The information to be updated in the glossary.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_JOB Function

Updates a specific job identified by the given key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`job_key`

(required) Unique job key.

`update_job_details`

(required) The information to be updated in the job.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_JOB_DEFINITION Function

Update a specific job definition identified by the given key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`job_definition_key`

(required) Unique job definition key.

`update_job_definition_details`

(required) The information to be updated in the job definition.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_METASTORE Function

Updates a metastore resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`metastore_id`

(required) The metastore's OCID.

`update_metastore_details`

(required) The metastore information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_NAMESPACE Function

Updates a specific namespace identified by the given key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`namespace_id`

(required) Unique namespace identifier.

`update_namespace_details`

(required) The information to be updated in the namespace.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PATTERN Function

Updates a specific pattern identified by the given key.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`pattern_key`

(required) Unique pattern key.

`update_pattern_details`

(required) The information to be updated in the pattern.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TERM Function

Updates a specific glossary term.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`glossary_key`

(required) Unique glossary key.

`term_key`

(required) Unique glossary term key.

`update_term_details`

(required) The information to be updated in the term.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TERM_RELATIONSHIP Function

Updates a specific glossary term relationship.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`glossary_key`

(required) Unique glossary key.

`term_key`

(required) Unique glossary term key.

`term_relationship_key`

(required) Unique glossary term relationship key.

`update_term_relationship_details`

(required) The information to be updated in the term relationship.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPLOAD_CREDENTIALS Function

Upload connection credentails and metadata for this connection.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`connection_key`

(required) Unique connection key.

`upload_credentials_details`

(required) The information used to upload the credentials file and metadata for updating this connection.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### USERS Function

Returns active users in the system.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### VALIDATE_CONNECTION Function

Validate connection by connecting to the data asset using credentials in metadata.

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`data_asset_key`

(required) Unique data asset key.

`validate_connection_details`

(required) The information used to validate the connections.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### VALIDATE_PATTERN Function

Validate pattern by deriving file groups representing logical entities using the expression

Syntax
```

```

Parameters

Parameter Description

`catalog_id`

(required) Unique catalog identifier.

`pattern_key`

(required) Unique pattern key.

`validate_pattern_details`

(required) The information used to validate the pattern.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datacatalog.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Data Catalog Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-4FF5EEC7-8695-4EA8-910F-082287352652)
- [ADD_CATALOG_LOCK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-5AD43C35-71F0-4CC4-A5CF-46F474E18A40)
- [ADD_CATALOG_PRIVATE_ENDPOINT_LOCK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-D0FC274A-50C5-4D33-BD08-A6427F1428C1)
- [ADD_DATA_SELECTOR_PATTERNS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-C3FE9ED7-9D79-46F3-9FA9-D13BB4F1A030)
- [ADD_METASTORE_LOCK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-F95988CA-C5F2-4F2D-976F-D382789CB346)
- [ASSOCIATE_CUSTOM_PROPERTY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-13436745-2AFC-4FD2-996D-3D8B8786EBB4)
- [ASYNCHRONOUS_EXPORT_GLOSSARY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-DF16C86E-80BC-46D9-990B-925612E87A29)
- [ATTACH_CATALOG_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-1A08AC7F-6202-49E3-B72C-7244922CA3CD)
- [CHANGE_CATALOG_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-CE15C3D0-0A5B-4628-A356-0F91C2397B40)
- [CHANGE_CATALOG_PRIVATE_ENDPOINT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-05BF3F96-8748-418B-B817-5E3AB0A4FD38)
- [CHANGE_METASTORE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-24426E39-401C-4506-A3A8-143C8B96C637)
- [CREATE_ATTRIBUTE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-BFB7F286-BDBB-4954-8D72-B6CA04145167)
- [CREATE_ATTRIBUTE_TAG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-4245F92E-D8D1-4A37-B48B-C6ED9E86C8C0)
- [CREATE_CATALOG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-0860BFE0-B4AE-4F2D-B671-B7C4654F9B0D)
- [CREATE_CATALOG_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-47AF9573-A3B2-44CE-A90E-5490ABF37D2B)
- [CREATE_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-10637FE3-6AE7-4B76-A1F2-D1DABB1EC41D)
- [CREATE_CUSTOM_PROPERTY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-612AA272-05B8-4847-A49C-B81B1A79170E)
- [CREATE_DATA_ASSET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-99C8C839-3C48-4AC2-BB27-813CB0E71978)
- [CREATE_DATA_ASSET_TAG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-F879172E-107F-44A4-B856-98474F15A5CC)
- [CREATE_ENTITY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-88D3A59D-506F-401B-97D3-0B2C7F26BA75)
- [CREATE_ENTITY_TAG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-6A8485A5-2750-4E23-910F-9444756DEA69)
- [CREATE_FOLDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-00726DA6-94C6-42A7-99F7-CC7451BF9DE6)
- [CREATE_FOLDER_TAG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-D89FC56F-ECAD-4EA8-A302-DDA650E95935)
- [CREATE_GLOSSARY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-C73E1707-29DC-4BD8-9164-5DA90D1DCE21)
- [CREATE_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-DAF3BFB6-A297-4726-ACB7-9915726DFC90)
- [CREATE_JOB_DEFINITION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-C90DA271-C32E-4B5B-A987-F60C94006C75)
- [CREATE_JOB_EXECUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-178D962E-42C9-4A4D-9466-0059ABF406E6)
- [CREATE_METASTORE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-367C34FD-9E51-4B01-B0DA-1287E69E8BC8)
- [CREATE_NAMESPACE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-1E564576-4005-40C8-A711-742B0E2FB37F)
- [CREATE_PATTERN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-B7626E50-D669-47B1-AE34-CB208D2A2050)
- [CREATE_TERM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-FC813ACA-9D65-4EAB-8B6A-FCD84177DA8E)
- [CREATE_TERM_RELATIONSHIP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-039073C3-E4C2-4C60-B989-CCC9B10382E7)
- [DELETE_ATTRIBUTE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-8DDABADE-7837-4A6E-8CCF-3768EAFA8BAC)
- [DELETE_ATTRIBUTE_TAG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-28717C0E-829D-48FA-8082-8200F67A4746)
- [DELETE_CATALOG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-6480F9AD-D471-4E76-B0E4-97E2EFE00B1C)
- [DELETE_CATALOG_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-6F03E77B-4E47-480C-9E86-6D5413DE6069)
- [DELETE_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-541C54D7-7565-4F0B-8F38-7BA1E32834E6)
- [DELETE_CUSTOM_PROPERTY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-F5ABB00E-8976-43EE-96A1-E8769DAF66FF)
- [DELETE_DATA_ASSET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-BA210A3F-672E-4491-BE03-48AF62D69DA1)
- [DELETE_DATA_ASSET_TAG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-D5BED015-2FE5-4929-AA22-889690F474A1)
- [DELETE_ENTITY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-55AAE0AA-DFE4-445D-A38B-C5ADD46F270B)
- [DELETE_ENTITY_TAG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-F4F5925E-43FE-44BA-8C45-7DDFC08F0547)
- [DELETE_FOLDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-E87D724B-945B-46D6-8E33-65D1C324F049)
- [DELETE_FOLDER_TAG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-9DB1F84E-971B-4A28-AD5D-C86D27A586FA)
- [DELETE_GLOSSARY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-5B180962-72EC-4FF3-B652-086000D85150)
- [DELETE_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-6D1A801A-6C73-438A-B470-EAA52CF02979)
- [DELETE_JOB_DEFINITION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-13DAEF05-4BD4-4ADD-9DFF-18D8BD21C19E)
- [DELETE_METASTORE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-E96A914B-A33A-4E3A-89EE-750F7C8F9C29)
- [DELETE_NAMESPACE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-1265C67E-F1FB-4E14-96A5-68387354E3AB)
- [DELETE_PATTERN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-3D67A99A-28E5-447B-9B18-FBF4DA57ACC9)
- [DELETE_TERM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-D6E2AE0A-F6A8-4E5C-9F87-BCF69F782C89)
- [DELETE_TERM_RELATIONSHIP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-AA8B32B5-453F-421D-89AB-052E73D403D8)
- [DETACH_CATALOG_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-8CA7C686-8025-4AE1-AEDA-1000447FCBF7)
- [DISASSOCIATE_CUSTOM_PROPERTY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-CD481B91-134A-4FE3-98FF-308231DE77A2)
- [EXPAND_TREE_FOR_GLOSSARY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-A68C79B2-0FA4-4D85-942A-A6B03C2BD4A5)
- [EXPORT_GLOSSARY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-5189814C-BB71-40C0-92DD-4C20245CE5F4)
- [FETCH_ENTITY_LINEAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-4F683E4E-94AA-4073-91AB-FF8D105E8EE4)
- [GET_ATTRIBUTE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-5D118C30-DC07-4CD5-99F9-8DBCAABB36AF)
- [GET_ATTRIBUTE_TAG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-BC5D0F58-2B80-4ED7-B151-18BC289B7D99)
- [GET_CATALOG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-FBC31E14-68ED-4F8A-BAA8-FA02A9B29C71)
- [GET_CATALOG_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-0BC1216C-A9F1-4BA7-9154-E12080666B77)
- [GET_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-20ED9CA4-F438-4C38-9A5E-650AC3F33E0E)
- [GET_CUSTOM_PROPERTY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-0F764338-DBA5-4789-8453-B70CF01BA51D)
- [GET_DATA_ASSET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-637F87E7-5708-4714-898B-6B606C1E8A4D)
- [GET_DATA_ASSET_TAG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-DB70AC71-6E4D-4BCD-8E33-A1332B3842B9)
- [GET_ENTITY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-EC111B4A-1FDA-4548-82E5-EDA2E0E179EF)
- [GET_ENTITY_TAG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-F715BF48-D58C-4D83-9001-294CD5186441)
- [GET_FOLDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-E8236DA9-4807-4EEC-B21F-34515659A498)
- [GET_FOLDER_TAG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-486F6B05-CE81-4FA1-84D4-BA839C25AFF9)
- [GET_GLOSSARY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-12B71559-CBA2-4D04-B144-F3BE4D9691FF)
- [GET_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-2B1F4D32-5605-41A2-8D28-A24D91D21159)
- [GET_JOB_DEFINITION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-C51BC604-56D9-405A-8202-0E7D39C70303)
- [GET_JOB_EXECUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-BC6CC2F4-59DF-4645-9315-EEF49D6B2D57)
- [GET_JOB_LOG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-045F521A-FF74-4BEE-AA90-8D8EECEDE3AF)
- [GET_JOB_METRICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-7546FB69-6D06-4EC5-AC33-B938ACAF3ED1)
- [GET_METASTORE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-AB458707-3121-4A03-B625-19A37E9127A1)
- [GET_NAMESPACE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-8D916AB5-E45C-453E-8836-B6AEB78FAD98)
- [GET_PATTERN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-A90A63BE-CD99-4FFC-B5AC-A61D7085B2C6)
- [GET_TERM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-97CDDC28-12A2-4F56-9A52-0AFE1AB04E9C)
- [GET_TERM_RELATIONSHIP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-55F63986-911E-4E19-8C88-8CF40D9A8F7F)
- [GET_TYPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-CC341B66-812D-49D7-BD53-C71D12B22A53)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-A7A8E388-2419-4AEA-A5E4-E58CBB014114)
- [IMPORT_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-24CFE408-0B01-4EAD-ACEC-9072AB20431E)
- [IMPORT_DATA_ASSET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-9EC1EC90-942F-49C5-8E2D-FDC971E2A95C)
- [IMPORT_GLOSSARY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-0C81DBA0-5D3F-474E-8D93-7C3CECAE5552)
- [LIST_AGGREGATED_PHYSICAL_ENTITIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-6BB15855-0CB9-46E5-A27F-C58C939BF992)
- [LIST_ATTRIBUTE_TAGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-C71D8BF3-88BF-4487-85AC-3E4A3A6D3820)
- [LIST_ATTRIBUTES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-C7E8281C-8FE5-45DF-AEEA-D7C38253ADC1)
- [LIST_CATALOG_PRIVATE_ENDPOINTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-26A5B6C5-93D5-4D33-852C-37687894E1D1)
- [LIST_CATALOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-B1765DD5-0514-4130-B998-CC5BF7F6851A)
- [LIST_CONNECTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-23E00328-B58C-47E7-873C-77EE42EB6F21)
- [LIST_CUSTOM_PROPERTIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-B34D4073-630D-498F-AA51-C77E8B10E414)
- [LIST_DATA_ASSET_TAGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-3C901391-8062-4723-A75B-F602F49F7CB3)
- [LIST_DATA_ASSETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-CAD467BC-1395-4006-8C3A-C448A468742E)
- [LIST_DERIVED_LOGICAL_ENTITIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-E1B43492-738F-4FD7-8D88-D44EAAC9EE4D)
- [LIST_ENTITIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-71795343-9BA4-45EF-A079-D5A0EBD6D9DA)
- [LIST_ENTITY_TAGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-0AC6AC15-70F8-4719-B4B5-74041F75779E)
- [LIST_FOLDER_TAGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-7AB69F1D-ED8E-43C3-BB7D-E23B3195934C)
- [LIST_FOLDERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-3E982480-214D-4EA7-A55C-DC442977E1AE)
- [LIST_GLOSSARIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-8C279614-435F-4C08-AE9C-81B05325F8E8)
- [LIST_JOB_DEFINITIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-2776C8F0-3C83-4D57-AA2E-10B5EC440FB0)
- [LIST_JOB_EXECUTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-45E53BA8-386B-4C70-8AC9-A4669DF4F30F)
- [LIST_JOB_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-E72BADBF-FE55-4E73-A7F0-5724F110D940)
- [LIST_JOB_METRICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-88E3A316-F289-4082-AB33-F58CFFD14795)
- [LIST_JOBS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-6C6B4C83-9021-4CDD-9E17-E5A21D27B0F7)
- [LIST_METASTORES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-FA0A046B-913F-403D-8389-7BF7204A6F96)
- [LIST_NAMESPACES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-3467B029-8155-45C3-B2AD-9EE7BE3820FE)
- [LIST_PATTERNS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-46BB6676-54FA-4032-A840-8D24CD90085A)
- [LIST_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-1A6F0BF3-D391-4C47-B3A1-D178878CFE93)
- [LIST_TAGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-426BDB41-2C75-4D3B-8E5F-D725D6CBE171)
- [LIST_TERM_RELATIONSHIPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-3FFDD1A5-6CC2-4876-98D6-AD50FB11A0A7)
- [LIST_TERMS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-221B2FBF-B6AA-4D7F-8960-B9E135AC0C8B)
- [LIST_TYPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-659F7EE8-827E-4593-8784-B22FB932B3AD)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-8387C7FE-D9D0-4CCA-B128-CDD3F892DBFD)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-2BCEC673-15F6-4EB0-A97E-3FBFC106D19D)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-1AD145C2-0BE3-44F0-8E16-90EDFE9471D7)
- [OBJECT_STATS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-ADE42C7B-00E5-4B88-9B88-BAAC969B52C2)
- [PARSE_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-F7FC4F2C-F516-4DC6-850E-5457DD6D61AF)
- [PROCESS_RECOMMENDATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-67017AE6-8F91-463A-BBE9-FEA9DFF755F6)
- [RECOMMENDATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-A80FBDE0-C776-42D0-BC33-72CF28E9B8AE)
- [REMOVE_CATALOG_LOCK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-AB430313-9AB3-4514-BBDE-3D19005C7338)
- [REMOVE_CATALOG_PRIVATE_ENDPOINT_LOCK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-103B6BE0-EDB7-4B0A-8487-D7A08E2D5170)
- [REMOVE_DATA_SELECTOR_PATTERNS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-56BA7B75-3B59-4562-862E-9403B11B825A)
- [REMOVE_METASTORE_LOCK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-0598007D-A895-436D-A43B-CB8985929DDA)
- [SEARCH_CRITERIA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-87D78A37-57EC-4158-8BA4-A140794C0BBF)
- [SUGGEST_MATCHES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-8AC5CAE1-2886-4BAB-842E-A46343765CFB)
- [SYNCHRONOUS_EXPORT_DATA_ASSET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-2B22F569-64AE-4275-B02D-5948009F84A1)
- [TEST_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-D1DDC44F-6677-4F54-A66E-1702AAC000DA)
- [UPDATE_ATTRIBUTE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-9105FC5A-F2A4-435B-9810-E29B8056C29E)
- [UPDATE_CATALOG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-269A2472-3810-48CF-80FE-8EF87ED07613)
- [UPDATE_CATALOG_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-17F83BA0-0962-4201-8344-EEB0CF282A14)
- [UPDATE_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-8F863718-DA2B-40D0-BAA6-5EA50D930E4F)
- [UPDATE_CUSTOM_PROPERTY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-22400D85-57B6-4BA1-AACA-728C19E81BD3)
- [UPDATE_DATA_ASSET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-3462E530-B408-48C3-9043-09164B4C62D8)
- [UPDATE_ENTITY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-8AA7823D-DC6A-454E-AC63-F5B52FEFDD33)
- [UPDATE_FOLDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-57B3DBF7-D3F7-4F1F-8199-B6E62F31DFC4)
- [UPDATE_GLOSSARY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-9E1159D6-07CD-48F9-9E0F-1F2C4A1714E2)
- [UPDATE_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-2B77D9A7-CA6D-4F25-821A-0516A3D9895E)
- [UPDATE_JOB_DEFINITION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-BD780C78-76D6-4BB7-92DF-745B2AEFFAD5)
- [UPDATE_METASTORE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-ECA05D4A-8FB3-4461-9230-AE6BE758004A)
- [UPDATE_NAMESPACE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-E5E67ACC-666A-4007-9B39-007E0621A0C7)
- [UPDATE_PATTERN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-B39D7C62-EB5A-4F5A-8859-C326887A15AC)
- [UPDATE_TERM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-F6862D5B-ACFF-47F7-9B76-EC8938D92E36)
- [UPDATE_TERM_RELATIONSHIP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-8D6A0386-D2D2-40E4-AB10-106852366B57)
- [UPLOAD_CREDENTIALS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-55BAFBB2-FA71-4EDE-B0DC-C99482C2A3BE)
- [USERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-E0BA330F-A931-4C97-9094-B12E9642EA45)
- [VALIDATE_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-54C47138-7483-42CD-A4DE-2E766CF7B162)
- [VALIDATE_PATTERN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dc_data_catalog.html#ADSDK-GUID-86980D20-5E6A-48F6-B684-470C8082C592)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
