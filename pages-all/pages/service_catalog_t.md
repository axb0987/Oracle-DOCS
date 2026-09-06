# Service Catalog Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html
- Fetched: 2026-09-05 19:20 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#dcoc-content-body)

## Service Catalog Common Types

### DBMS_CLOUD_OCI_SERVICE_CATALOG_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_CATALOG_PUBLISHER_SUMMARY_T Type

Summary details about the publisher of the resource.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier for the publisher.

`display_name`

(required) The name of the publisher.

### DBMS_CLOUD_OCI_SERVICE_CATALOG_UPLOAD_DATA_T Type

The model for uploaded binary data, like logos and images.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The name used to refer to the uploaded data.

`content_url`

(optional) The content URL of the uploaded data.

`mime_type`

(optional) The MIME type of the uploaded data.

### DBMS_CLOUD_OCI_SERVICE_CATALOG_APPLICATION_SUMMARY_T Type

The model for summary of an application in service catalog.

Syntax
```

```

Fields

Field Description

`entity_id`

(required) Identifier of the application from a service catalog.

`entity_type`

(required) The type of an application in the service catalog.

`display_name`

(required) The name that service catalog should use to display this application.

`is_featured`

(optional) Indicates whether the application is featured.

`publisher`

(optional)

`short_description`

(optional) A short description of the application.

`logo`

(optional)

`pricing_type`

(optional) Summary of the pricing types available across all packages in the application.

Allowed values are: 'FREE', 'BYOL', 'PAYGO'

`package_type`

(optional) The type of the packages withing the application.

Allowed values are: 'STACK'

### DBMS_CLOUD_OCI_SERVICE_CATALOG_APPLICATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_service_catalog_application_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_CATALOG_APPLICATION_COLLECTION_T Type

Collection of applications in a given service catalog or a tenancy.

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of service catalog applications.

### DBMS_CLOUD_OCI_SERVICE_CATALOG_CREATE_SERVICE_CATALOG_ASSOCIATION_DETAILS_T Type

The model to create a single association between a service catalog and a resource.

Syntax
```

```

Fields

Field Description

`service_catalog_id`

(required) Identifier of the service catalog.

`entity_id`

(required) Identifier of the entity being associated with service catalog.

`entity_type`

(optional) The type of the entity that is associated with the service catalog.

### DBMS_CLOUD_OCI_SERVICE_CATALOG_CREATE_SERVICE_CATALOG_ASSOCIATION_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_service_catalog_create_service_catalog_association_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_CATALOG_BULK_REPLACE_SERVICE_CATALOG_ASSOCIATIONS_DETAILS_T Type

The model to replace service catalog associations in bulk.

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of CreateServiceCatalogAssociationDetails for bulk operation.

### DBMS_CLOUD_OCI_SERVICE_CATALOG_CHANGE_PRIVATE_APPLICATION_COMPARTMENT_DETAILS_T Type

All the parameters required to make the move.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to move the private application.

### DBMS_CLOUD_OCI_SERVICE_CATALOG_CHANGE_SERVICE_CATALOG_COMPARTMENT_DETAILS_T Type

The model for the parameters needed move a service catalog from one compartment to another.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to move the service catalog.

### DBMS_CLOUD_OCI_SERVICE_CATALOG_CREATE_PRIVATE_APPLICATION_PACKAGE_T Type

A base object for creating a private application package.

Syntax
```

```

Fields

Field Description

`package_type`

(required) The package's type.

Allowed values are: 'STACK'

`version`

(required) The package version.

### DBMS_CLOUD_OCI_SERVICE_CATALOG_CREATE_PRIVATE_APPLICATION_DETAILS_T Type

The model for the parameters needed to create a private application.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create the private application.

`display_name`

(required) The name of the private application.

`short_description`

(required) A short description of the private application.

`long_description`

(optional) A long description of the private application.

`logo_file_base64_encoded`

(optional) Base64-encoded logo to use as the private application icon. Template icon file requirements: PNG format, 50 KB maximum, 130 x 130 pixels.

`package_details`

(required)

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_SERVICE_CATALOG_CREATE_PRIVATE_APPLICATION_STACK_PACKAGE_T Type

An object for creating a private application stack package.

Syntax
```

```

`dbms_cloud_oci_service_catalog_create_private_application_stack_package_t`is a subtype of the`dbms_cloud_oci_service_catalog_create_private_application_package_t`type.

Fields

Field Description

`zip_file_base64_encoded`

(optional) Base-64 payload of the Terraform zip package.

### DBMS_CLOUD_OCI_SERVICE_CATALOG_CREATE_SERVICE_CATALOG_DETAILS_T Type

The model for parameter needed to create service catalog.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The unique identifier for the compartment where the service catalog will be created.

`display_name`

(required) The display name of the service catalog.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_SERVICE_CATALOG_ERROR_ENTITY_T Type

The model for the error entity.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_SERVICE_CATALOG_PRIVATE_APPLICATION_T Type

Full details of an application or a solution, which lives inside the tenancy and may be included into service catalogs.

Syntax
```

```

Fields

Field Description

`lifecycle_state`

(required) The lifecycle state of the private application.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED'

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where the private application resides.

`id`

(required) The unique identifier for the private application in Marketplace.

`display_name`

(required) The name of the private application.

`short_description`

(optional) A short description of the private application.

`long_description`

(optional) A long description of the private application.

`logo`

(optional)

`package_type`

(required) Type of packages within this private application.

Allowed values are: 'STACK'

`time_created`

(required) The date and time the private application was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2021-05-26T21:10:29.600Z`

`time_updated`

(optional) The date and time the private application was last modified, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2021-12-10T05:10:29.721Z`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_SERVICE_CATALOG_PRIVATE_APPLICATION_SUMMARY_T Type

Brief data about an application or a solution, which lives inside the tenancy and may be included into service catalogs.

Syntax
```

```

Fields

Field Description

`lifecycle_state`

(required) The lifecycle state of the private application.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where the private application resides.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private application.

`display_name`

(required) The name of the private application.

`short_description`

(optional) A short description of the private application.

`logo`

(optional)

`package_type`

(required) Type of the packages, which are hosted by the private application.

Allowed values are: 'STACK'

`time_created`

(required) The date and time the private application was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2021-05-27T21:10:29.600Z`

### DBMS_CLOUD_OCI_SERVICE_CATALOG_PRIVATE_APPLICATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_service_catalog_private_application_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_CATALOG_PRIVATE_APPLICATION_COLLECTION_T Type

Collection of private applications.

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of items.

### DBMS_CLOUD_OCI_SERVICE_CATALOG_PRIVATE_APPLICATION_PACKAGE_T Type

A base object for all types of private application packages.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private application package.

`private_application_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private application where the package is hosted.

`display_name`

(optional) The display name of the package.

`version`

(required) The package version.

`package_type`

(required) The specified package's type.

Allowed values are: 'STACK'

`time_created`

(required) The date and time the private application package was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2021-05-27T21:10:29.600Z`

### DBMS_CLOUD_OCI_SERVICE_CATALOG_PRIVATE_APPLICATION_PACKAGE_SUMMARY_T Type

The model for a summary of a private application package.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private application package.

`private_application_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private application where the package is hosted.

`display_name`

(optional) The display name of the specified package.

`version`

(required) The version of the specified package.

`package_type`

(required) The type of the package.

Allowed values are: 'STACK'

`time_created`

(required) The date and time the private application package was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2021-05-27T21:10:29.600Z`

### DBMS_CLOUD_OCI_SERVICE_CATALOG_PRIVATE_APPLICATION_PACKAGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_service_catalog_private_application_package_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_CATALOG_PRIVATE_APPLICATION_PACKAGE_COLLECTION_T Type

Collection of Private Application Package summary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of items.

### DBMS_CLOUD_OCI_SERVICE_CATALOG_PRIVATE_APPLICATION_STACK_PACKAGE_T Type

A stack package for private applications.

Syntax
```

```

`dbms_cloud_oci_service_catalog_private_application_stack_package_t`is a subtype of the`dbms_cloud_oci_service_catalog_private_application_package_t`type.

Fields

Field Description

`content_url`

(optional) The content URL of the terraform configuration.

`mime_type`

(optional) The MIME type of the terraform configuration.

### DBMS_CLOUD_OCI_SERVICE_CATALOG_SERVICE_CATALOG_T Type

The model for an Oracle Cloud Infrastructure Service Catalog.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier for the Service catalog.

`compartment_id`

(required) The Compartment id where the service catalog exists

`display_name`

(required) The name of the service catalog.

`lifecycle_state`

(required) The lifecycle state of the service catalog.

Allowed values are: 'ACTIVE', 'DELETED'

`time_created`

(required) The date and time the service catalog was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2021-05-26T21:10:29.600Z`

`time_updated`

(optional) The date and time the service catalog was last modified, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2021-12-10T05:10:29.721Z`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_SERVICE_CATALOG_SERVICE_CATALOG_ASSOCIATION_T Type

The detailed model for service catalog association.

Syntax
```

```

Fields

Field Description

`id`

(required) Identifier of the association.

`service_catalog_id`

(required) Identifier of the service catalog.

`entity_id`

(required) Identifier of the entity being associated with service catalog.

`entity_type`

(optional) The type of the entity that is associated with the service catalog.

`time_created`

(required) Timestamp of when the resource was associated with service catalog.

### DBMS_CLOUD_OCI_SERVICE_CATALOG_SERVICE_CATALOG_ASSOCIATION_SUMMARY_T Type

The model for a summary of a service catalog association.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier of the service catalog association.

`service_catalog_id`

(required) The unique identifier of the service catalog.

`entity_id`

(required) The unique identifier of the resource being associated to service catalog.

`entity_type`

(optional) The type of the entity that is associated with the service catalog.

`time_created`

(required) Timestamp of when the resource was associated with service catalog.

### DBMS_CLOUD_OCI_SERVICE_CATALOG_SERVICE_CATALOG_ASSOCIATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_service_catalog_service_catalog_association_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_CATALOG_SERVICE_CATALOG_ASSOCIATION_COLLECTION_T Type

Collection of service catalog associations.

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of service catalog and the resources associated with it.

### DBMS_CLOUD_OCI_SERVICE_CATALOG_SERVICE_CATALOG_SUMMARY_T Type

The model for a summary of an Oracle Cloud Infrastructure service catalog.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier for the Service catalog.

`lifecycle_state`

(required) The lifecycle state of the service catalog.

`compartment_id`

(required) The Compartment id where the service catalog exists.

`display_name`

(required) The name of the service catalog.

`time_created`

(required) The date and time this service catalog was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2021-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_SERVICE_CATALOG_SERVICE_CATALOG_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_service_catalog_service_catalog_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_CATALOG_SERVICE_CATALOG_COLLECTION_T Type

Collection of Service Catalog Summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of catalog summaries.

### DBMS_CLOUD_OCI_SERVICE_CATALOG_UPDATE_PRIVATE_APPLICATION_DETAILS_T Type

The model for the parameters needed to update a private application.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The name of the private application.

`short_description`

(optional) A short description of the private application.

`long_description`

(optional) A long description of the private application.

`logo_file_base64_encoded`

(optional) Base64-encoded logo to use as the private application icon. Template icon file requirements: PNG format, 50 KB maximum, 130 x 130 pixels.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_SERVICE_CATALOG_UPDATE_SERVICE_CATALOG_DETAILS_T Type

The model for the parameters needed to update a service catalog.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A display name of the service catalog.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_SERVICE_CATALOG_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource at which point it will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'FAILED'

`entity_id`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata

### DBMS_CLOUD_OCI_SERVICE_CATALOG_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_service_catalog_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_CATALOG_WORK_REQUEST_T Type

A description of workrequest status

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_PRIVATE_APPLICATION', 'UPDATE_PRIVATE_APPLICATION', 'DELETE_PRIVATE_APPLICATION', 'MOVE_PRIVATE_APPLICATION'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'FAILED', 'SUCCEEDED'

`id`

(required) The id of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_SERVICE_CATALOG_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed on (https://docs.cloud.oracle.com/Content/API/References/apierrors.htm)

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) The time the error occured. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_SERVICE_CATALOG_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_service_catalog_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_CATALOG_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestError objects.

### DBMS_CLOUD_OCI_SERVICE_CATALOG_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written. An RFC3339 formatted datetime string

### DBMS_CLOUD_OCI_SERVICE_CATALOG_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_service_catalog_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_CATALOG_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a workRequestLog search. Contains both workRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestLogEntries.

### DBMS_CLOUD_OCI_SERVICE_CATALOG_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_PRIVATE_APPLICATION', 'UPDATE_PRIVATE_APPLICATION', 'DELETE_PRIVATE_APPLICATION', 'MOVE_PRIVATE_APPLICATION'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'FAILED', 'SUCCEEDED'

`id`

(required) The id of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_SERVICE_CATALOG_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_service_catalog_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_CATALOG_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestSummary objects.

- [Service Catalog Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-3EC447A4-60E7-43F1-8078-C3E1D1ABB071)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-8488BD8C-6A43-4719-AF80-956C41DDC6F6)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_PUBLISHER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-6D1ABFF2-D70A-4932-A63F-C8E0385060ED)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_UPLOAD_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-20AD9524-CE2F-420F-9ED1-91C80E0D9918)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_APPLICATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-4D0653E5-8FAA-455F-A122-3C2D6507DBD3)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_APPLICATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-2BAE1ABA-E485-408A-BC73-C1C1C96C2743)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_APPLICATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-034BF91E-730A-4F80-82C0-AD9E6C486F36)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_CREATE_SERVICE_CATALOG_ASSOCIATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-A190FD77-CA52-464D-B100-5A0F897FB4CC)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_CREATE_SERVICE_CATALOG_ASSOCIATION_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-5E25493C-8EF8-4CED-ABD6-1CAF3F3E034F)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_BULK_REPLACE_SERVICE_CATALOG_ASSOCIATIONS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-41EAF51D-603F-44DE-8DB1-DF38A439B063)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_CHANGE_PRIVATE_APPLICATION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-F0817719-E53D-4EE7-BF6C-B32882B83AD3)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_CHANGE_SERVICE_CATALOG_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-C7385D0D-D77E-4790-BB22-49858942920B)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_CREATE_PRIVATE_APPLICATION_PACKAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-079C2859-25CE-40A3-A8EC-D9CC5C2E1975)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_CREATE_PRIVATE_APPLICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-420A2F8A-7553-4DA5-98C6-3FFDA1B8EEA7)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_CREATE_PRIVATE_APPLICATION_STACK_PACKAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-66293403-3C9E-4476-97CB-D5FECCE602AD)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_CREATE_SERVICE_CATALOG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-CA63E5D0-805E-4D0A-87C2-15BE908A3735)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_ERROR_ENTITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-19F11A19-8AFA-40D4-8115-80933F0FFD41)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_PRIVATE_APPLICATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-3FCCFB62-3008-4FF1-A04D-91E475AFE977)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_PRIVATE_APPLICATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-4313CA9D-A857-4630-82F7-091B2254AFA3)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_PRIVATE_APPLICATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-0B02DC7C-F72A-49C0-B16F-3A3662FB7498)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_PRIVATE_APPLICATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-D4E66867-C445-40B0-8B13-366DB5FD3CAC)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_PRIVATE_APPLICATION_PACKAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-692578F7-2018-420A-AB45-E57F4DB0F099)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_PRIVATE_APPLICATION_PACKAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-E6933F38-7172-4F4B-8AA2-8DFC28E97AFF)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_PRIVATE_APPLICATION_PACKAGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-44C3E4A9-74F8-4C45-A506-1F39F912E497)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_PRIVATE_APPLICATION_PACKAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-D9E2B3C2-550D-41C4-8101-0A9698464BEF)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_PRIVATE_APPLICATION_STACK_PACKAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-64772482-5DB4-486F-B878-F4C12898199D)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_SERVICE_CATALOG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-AD2A12E5-BC12-48FE-A5AB-AB778FA76CD8)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_SERVICE_CATALOG_ASSOCIATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-A6B0F5E5-39E1-4AD5-9354-0308B3FBD078)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_SERVICE_CATALOG_ASSOCIATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-B3B09B79-FCEB-4DA6-A373-DD88144523FC)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_SERVICE_CATALOG_ASSOCIATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-85D014EB-EBE2-490C-8782-0C560B1ED137)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_SERVICE_CATALOG_ASSOCIATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-E4A0C424-2E4F-4226-9D7D-E4382644ADF3)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_SERVICE_CATALOG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-26531AFB-E6CA-47C8-B86A-2BA4E50362AB)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_SERVICE_CATALOG_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-40583AD0-06E0-4458-968A-8847BD3BB8F3)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_SERVICE_CATALOG_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-0D0B627B-1B25-46AF-970E-D18B5ADF6809)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_UPDATE_PRIVATE_APPLICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-53A4782F-5B9F-4B10-896E-661465C5F38C)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_UPDATE_SERVICE_CATALOG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-992D2B8B-43B9-4496-A62A-A1D050893D43)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-D7F8ECC0-684A-49E8-B19C-4AFEBE9BCE25)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-730865C0-3864-4240-BB7B-F35BB8B2D781)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-F87FA84D-603A-4DBE-A8F5-9B7B9E7CE5AB)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-471CA753-17DE-4026-A766-4F619C3F3508)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-E9AE631B-3EB8-44EF-A3D5-96A0928E7C3D)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-D1A82405-28C9-4F21-9E1D-6D4E9521293D)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-A5ED047B-9F36-4A21-A50E-CBDCF1969999)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-8A037C90-8F25-4594-BCA5-463B043B7382)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-02E015B3-7489-4A91-A00E-46631FDFB476)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-F96CF030-4F2D-4514-9D4E-A5BE0F514C86)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-3D153856-0AEC-4F67-A6A0-422A1DE5845D)
- [DBMS_CLOUD_OCI_SERVICE_CATALOG_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_catalog_t.html#ADSDK-GUID-3528A08C-159A-4023-AF62-5735F9D54E47)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
