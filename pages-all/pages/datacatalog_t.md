# Data Catalog Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html
- Fetched: 2026-09-05 19:02 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#dcoc-content-body)

## Data Catalog Common Types

### DBMS_CLOUD_OCI_DATACATALOG_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_ADD_RESOURCE_LOCK_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the lock.

Allowed values are: 'FULL', 'DELETE'

`related_resource_id`

(optional) The id of the resource that is locking this resource. Indicates that deleting this resource will remove the lock.

`message`

(optional) A message added by the creator of the lock. This is typically used to give an indication of why the resource is locked.

`time_created`

(optional) When the lock was created.

### DBMS_CLOUD_OCI_DATACATALOG_OBJECT_STORAGE_OBJECT_REFERENCE_T Type

A reference to an Object Storage object.

Syntax
```

```

Fields

Field Description

`namespace_name`

(required) Object Storage namespace.

`bucket_name`

(required) Object Storage bucket name.

`object_name`

(required) Object Storage object name.

### DBMS_CLOUD_OCI_DATACATALOG_ASYNCHRONOUS_EXPORT_GLOSSARY_DETAILS_T Type

Details needed by the glossary export request.

Syntax
```

```

Fields

Field Description

`object_storage_target`

(optional)

### DBMS_CLOUD_OCI_DATACATALOG_ASYNCHRONOUS_EXPORT_GLOSSARY_RESULT_T Type

Details about the job which performs an export.

Syntax
```

```

Fields

Field Description

`job_definition_name`

(optional) Display name of the export job.

`job_definition_key`

(optional) Unique key of the export job definition.

`job_key`

(optional) Unique key of the export job.

`job_execution_key`

(optional) Unique key of the job execution.

`source_key`

(optional) Unique key of the object being exported.

### DBMS_CLOUD_OCI_DATACATALOG_ASYNCHRONOUS_EXPORT_REQUEST_DETAILS_T Type

Details for an export request.

Syntax
```

```

Fields

Field Description

`object_storage_target`

(optional)

### DBMS_CLOUD_OCI_DATACATALOG_ASYNCHRONOUS_EXPORT_RESULT_T Type

Details about the job which performs an export.

Syntax
```

```

Fields

Field Description

`job_definition_name`

(optional) Display name of the export job.

`job_definition_key`

(optional) Unique key of the export job definition.

`job_key`

(optional) Unique key of the export job.

`job_execution_key`

(optional) Unique key of the job execution.

`source_key`

(optional) Unique key of the object being exported.

### DBMS_CLOUD_OCI_DATACATALOG_ATTACH_CATALOG_PRIVATE_ENDPOINT_DETAILS_T Type

Information about the attaching the private endpoint resource to a catalog

Syntax
```

```

Fields

Field Description

`catalog_private_endpoint_id`

(required) The identifier of the private endpoint to be attached to the catalog resource.

### DBMS_CLOUD_OCI_DATACATALOG_OBJECT_RELATIONSHIP_T Type

Details regarding a specific object and its relationship to the referencing object.

Syntax
```

```

Fields

Field Description

`relationship_type`

(optional) Type of relationship with the referencing object.

`key`

(optional) Unique id of the object.

`name`

(optional) Name of the object.

`type_name`

(optional) Type name of the object. Type names can be found via the '/types' endpoint.

`type_key`

(optional) Type key of the object. Type keys can be found via the '/types' endpoint.

`time_created`

(optional) The date and time the relationship was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`time_updated`

(optional) The last time a change was made to this reference. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`path`

(optional) Full path of the object.

`parent_key`

(optional) Key of the parent object for the resource.

`parent_path`

(optional) Full path of the parent object.

### DBMS_CLOUD_OCI_DATACATALOG_CUSTOM_PROPERTY_GET_USAGE_T Type

Details of a single custom property

Syntax
```

```

Fields

Field Description

`key`

(optional) Unique Identifier of the attribute which is ID

`display_name`

(optional) Display name of the custom property

`description`

(optional) Description of the custom property

`value`

(optional) The custom property value

`data_type`

(optional) The data type of the custom property

Allowed values are: 'TEXT', 'RICH_TEXT', 'BOOLEAN', 'NUMBER', 'DATE'

`namespace_name`

(optional) Namespace name of the custom property

`namespace_key`

(optional) Unique namespace key that is immutable

`is_multi_valued`

(optional) If this field allows multiple values to be set

`is_hidden`

(optional) If this field is a hidden field

`is_editable`

(optional) If this field is a editable field

`is_shown_in_list`

(optional) If this field is displayed in a list view of applicable objects.

`is_event_enabled`

(optional) If an OCI Event will be emitted when the custom property is modified.

`is_list_type`

(optional) Is this property allowed to have list of values

`allowed_values`

(optional) Allowed values for the custom property if any

### DBMS_CLOUD_OCI_DATACATALOG_OBJECT_RELATIONSHIP_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_object_relationship_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_CUSTOM_PROPERTY_GET_USAGE_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_custom_property_get_usage_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_ATTRIBUTE_T Type

Details of an entity attribute. An attribute of a data entity describing an item of data, with a name and data type. Synonymous with 'column' in a database.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique attribute key that is immutable.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`business_name`

(optional) Optional user friendly business name of the attribute. If set, this supplements the harvested display name of the object.

`description`

(optional) Detailed description of the attribute.

`entity_key`

(optional) The unique key of the parent entity.

`lifecycle_state`

(optional) State of the attribute.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`lifecycle_details`

(optional) A message describing the current state in more detail. An object not in ACTIVE state may have functional limitations, see service documentation for details.

`time_created`

(optional) The date and time the attribute was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`time_updated`

(optional) The last time that any change was made to the attribute. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created this attribute in the data catalog.

`updated_by_id`

(optional) OCID of the user who modified this attribute in the data catalog.

`external_data_type`

(optional) Data type of the attribute as defined in the external system. Type mapping across systems can be achieved through term associations across domains in the ontology. The attribute can also be tagged to the datatype in the domain ontology to resolve any ambiguity arising from type name similarity that can occur with user defined types.

`external_key`

(optional) Unique external key of this attribute in the external source system.

`is_incremental_data`

(optional) Property that identifies if this attribute can be used as a watermark to extract incremental data.

`is_nullable`

(optional) Property that identifies if this attribute can be assigned null values.

`type_key`

(optional) The type of the attribute. Type keys can be found via the '/types' endpoint.

`min_collection_count`

(optional) The minimum count for the number of instances of a given type stored in this collection type attribute,applicable if this attribute is a complex type.

`max_collection_count`

(optional) The maximum count for the number of instances of a given type stored in this collection type attribute,applicable if this attribute is a complex type. For type specifications in systems that specify only \"capacity\" without upper or lower bound , this property can also be used to just mean \"capacity\". Some examples are Varray size in Oracle , Occurs Clause in Cobol , capacity in XmlSchemaObjectCollection , maxOccurs in Xml , maxItems in Json

`datatype_entity_key`

(optional) Entity key that represents the datatype of this attribute , applicable if this attribute is a complex type.

`external_datatype_entity_key`

(optional) External entity key that represents the datatype of this attribute , applicable if this attribute is a complex type.

`parent_attribute_key`

(optional) Attribute key that represents the parent attribute of this attribute , applicable if the parent attribute is of complex datatype.

`external_parent_attribute_key`

(optional) External attribute key that represents the parent attribute of this attribute , applicable if the parent attribute is of complex type.

`length`

(optional) Max allowed length of the attribute value.

`position`

(optional) Position of the attribute in the record definition.

`precision`

(optional) Precision of the attribute value usually applies to float data type.

`scale`

(optional) Scale of the attribute value usually applies to float data type.

`time_external`

(optional) Last modified timestamp of this object in the external system.

`time_harvested`

(optional) The date and time the attribute was harvested, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`object_relationships`

(optional) List of objects and their relationships to this attribute.

`is_derived_attribute`

(optional) Whether a column is derived or not.

`uri`

(optional) URI to the attribute instance in the API.

`path`

(optional) Full path of the attribute.

`custom_property_members`

(optional) The list of customized properties along with the values for this object

`properties`

(optional) A map of maps that contains the properties which are specific to the attribute type. Each attribute type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most attributes have required properties within the \"default\" category. Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`

`associated_rule_types`

(optional) Rule types associated with attribute.

Allowed values are: 'PRIMARYKEY', 'FOREIGNKEY', 'UNIQUEKEY'

### DBMS_CLOUD_OCI_DATACATALOG_ATTRIBUTE_SUMMARY_T Type

Summary of an entity attribute.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique attribute key that is immutable.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`business_name`

(optional) Optional user friendly business name of the attribute. If set, this supplements the harvested display name of the object.

`description`

(optional) Detailed description of the attribute.

`entity_key`

(optional) The unique key of the parent entity.

`external_key`

(optional) Unique external key of this attribute in the external source system.

`length`

(optional) Max allowed length of the attribute value.

`position`

(optional) Position of the attribute in the record definition.

`precision`

(optional) Precision of the attribute value usually applies to float data type.

`scale`

(optional) Scale of the attribute value usually applies to float data type.

`is_nullable`

(optional) Property that identifies if this attribute can be assigned null values.

`uri`

(optional) URI to the attribute instance in the API.

`lifecycle_state`

(optional) State of the attribute.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`lifecycle_details`

(optional) A message describing the current state in more detail. An object not in ACTIVE state may have functional limitations, see service documentation for details.

`time_created`

(optional) The date and time the attribute was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`external_data_type`

(optional) Data type of the attribute as defined in the external source system.

`type_key`

(optional) The type of the attribute. Type keys can be found via the '/types' endpoint.

`min_collection_count`

(optional) The minimum count for the number of instances of a given type stored in this collection type attribute,applicable if this attribute is a complex type.

`max_collection_count`

(optional) The maximum count for the number of instances of a given type stored in this collection type attribute,applicable if this attribute is a complex type. For type specifications in systems that specify only \"capacity\" without upper or lower bound , this property can also be used to just mean \"capacity\". Some examples are Varray size in Oracle , Occurs Clause in Cobol , capacity in XmlSchemaObjectCollection , maxOccurs in Xml , maxItems in Json

`datatype_entity_key`

(optional) Entity key that represents the datatype of this attribute , applicable if this attribute is a complex type.

`external_datatype_entity_key`

(optional) External entity key that represents the datatype of this attribute , applicable if this attribute is a complex type.

`parent_attribute_key`

(optional) Attribute key that represents the parent attribute of this attribute , applicable if the parent attribute is of complex datatype.

`external_parent_attribute_key`

(optional) External attribute key that represents the parent attribute of this attribute , applicable if the parent attribute is of complex type.

`path`

(optional) Full path of the attribute.

`custom_property_members`

(optional) The list of customized properties along with the values for this object

`associated_rule_types`

(optional) Rule types associated with attribute.

Allowed values are: 'PRIMARYKEY', 'FOREIGNKEY', 'UNIQUEKEY'

`is_derived_attribute`

(optional) Whether a column is derived or not.

`time_updated`

(optional) The last time that any change was made to the attribute. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`properties`

(optional) A map of maps that contains the properties which are specific to the attribute type. Each attribute type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most attributes have required properties within the \"default\" category. Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_ATTRIBUTE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_attribute_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_ATTRIBUTE_COLLECTION_T Type

Results of an attributes listing. Attributes describe an item of data with name and datatype.

Syntax
```

```

Fields

Field Description

`l_count`

(optional) Total number of items returned.

`items`

(required) Collection of attributes.

### DBMS_CLOUD_OCI_DATACATALOG_ATTRIBUTE_TAG_T Type

Represents an association of an entity attribute to a term.

Syntax
```

```

Fields

Field Description

`attribute_key`

(optional) The unique key of the parent attribute.

`key`

(required) Unique tag key that is immutable.

`name`

(optional) Name of the tag which matches the term name.

`term_key`

(optional) Unique key of the related term.

`term_path`

(optional) Path of the related term.

`term_description`

(optional) Description of the related term.

`lifecycle_state`

(optional) The current state of the tag.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`time_created`

(optional) The date and time the tag was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`created_by_id`

(optional) OCID of the user who created the tag.

`uri`

(optional) URI to the tag instance in the API.

### DBMS_CLOUD_OCI_DATACATALOG_ATTRIBUTE_TAG_SUMMARY_T Type

Summary of an entity attribute tag.

Syntax
```

```

Fields

Field Description

`attribute_key`

(optional) The unique key of the parent attribute.

`key`

(required) Unique tag key that is immutable.

`time_created`

(optional) The date and time the tag was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`name`

(optional) Name of the tag that matches the term name.

`uri`

(optional) URI to the tag instance in the API.

`term_key`

(optional) Unique key of the related term.

`term_path`

(optional) Path of the related term.

`term_description`

(optional) Description of the related term.

`glossary_key`

(optional) Unique id of the parent glossary of the term.

`lifecycle_state`

(optional) State of the Tag.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

### DBMS_CLOUD_OCI_DATACATALOG_ATTRIBUTE_TAG_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_attribute_tag_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_ATTRIBUTE_TAG_COLLECTION_T Type

Results of an attribute tags listing. Attribnute tags allow association of business terms with attributes.

Syntax
```

```

Fields

Field Description

`l_count`

(optional) Total number of items returned.

`items`

(required) Collection of attribute tags.

### DBMS_CLOUD_OCI_DATACATALOG_BASE_PERMISSIONS_SUMMARY_T Type

Permissions object sent as part of the response.

Syntax
```

```

Fields

Field Description

`user_permissions`

(optional) An array of permissions.

### DBMS_CLOUD_OCI_DATACATALOG_BASE_TAG_T Type

Represents the association of an object to a term. Tags are immutable.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique tag key that is immutable.

`name`

(optional) Name of the tag which matches the term name.

`term_key`

(optional) Unique key of the related term.

`term_path`

(optional) Path of the related term.

`term_description`

(optional) Description of the related term.

`lifecycle_state`

(optional) The current state of the tag.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`time_created`

(optional) The date and time the tag was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`created_by_id`

(optional) OCID of the user who created the tag.

`uri`

(optional) URI to the tag instance in the API.

### DBMS_CLOUD_OCI_DATACATALOG_BASE_TAG_SUMMARY_T Type

Represents the association of an object to a term.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique tag key that is immutable.

`time_created`

(optional) The date and time the tag was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`name`

(optional) Name of the tag that matches the term name.

`uri`

(optional) URI to the tag instance in the API.

`term_key`

(optional) Unique key of the related term.

`term_path`

(optional) Path of the related term.

`term_description`

(optional) Description of the related term.

`glossary_key`

(optional) Unique id of the parent glossary of the term.

`lifecycle_state`

(optional) State of the Tag.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

### DBMS_CLOUD_OCI_DATACATALOG_RESOURCE_LOCK_T Type

Resource locks are used to prevent certain APIs from being called for the resource. A full lock prevents both updating the resource and deleting the resource. A delete lock prevents deleting the resource.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the lock.

Allowed values are: 'FULL', 'DELETE'

`related_resource_id`

(optional) The id of the resource that is locking this resource. Indicates that deleting this resource will remove the lock.

`message`

(optional) A message added by the creator of the lock. This is typically used to give an indication of why the resource is locked.

`time_created`

(optional) When the lock was created.

### DBMS_CLOUD_OCI_DATACATALOG_RESOURCE_LOCK_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_resource_lock_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_CATALOG_T Type

A data catalog enables you to collect, organize, find, access, understand, enrich, and activate technical, business, and operational metadata.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID of the data catalog instance.

`display_name`

(optional) Data catalog identifier, which can be renamed.

`compartment_id`

(required) Compartment identifier.

`time_created`

(optional) The time the data catalog was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_updated`

(optional) The time the data catalog was updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`service_api_url`

(optional) The REST front endpoint URL to the data catalog instance.

`service_console_url`

(optional) The console front endpoint URL to the data catalog instance.

`number_of_objects`

(optional) The number of data objects added to the data catalog. Please see the data catalog documentation for further information on how this is calculated.

`lifecycle_state`

(optional) The current state of the data catalog resource.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`lifecycle_details`

(optional) An message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in 'Failed' state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`attached_catalog_private_endpoints`

(optional) The list of private reverse connection endpoints attached to the catalog

`locks`

(optional) Locks associated with this resource.

### DBMS_CLOUD_OCI_DATACATALOG_CATALOG_PERMISSIONS_SUMMARY_T Type

General permissions object.

Syntax
```

```

Fields

Field Description

`catalog_id`

(optional) The data catalog's OCID.

`user_permissions`

(optional) An array of permissions.

### DBMS_CLOUD_OCI_DATACATALOG_CATALOG_PRIVATE_ENDPOINT_T Type

A private network reverse connection creates a connection from service to customer subnet over a private network.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable

`compartment_id`

(required) Compartment Identifier.

`subnet_id`

(required) Subnet Identifier

`display_name`

(optional) Private Reverse Connection Endpoint display name

`dns_zones`

(required) List of DNS zones to be used by the data assets to be harvested. Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com

`time_created`

(optional) The time the private endpoint was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_updated`

(optional) The time the private endpoint was updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`lifecycle_state`

(optional) The current state of the private endpoint resource.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in 'Failed' state.

`attached_catalogs`

(optional) The list of catalogs using the private reverse connection endpoint

`locks`

(optional) Locks associated with this resource.

### DBMS_CLOUD_OCI_DATACATALOG_CATALOG_PRIVATE_ENDPOINT_SUMMARY_T Type

A private network reverse connection creates a connection from service to customer subnet over a private network.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable

`subnet_id`

(required) Subnet Identifier

`dns_zones`

(required) List of DNS zones to be used by the data assets to be harvested. Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com

`compartment_id`

(required) Identifier of the compartment this private endpoint belongs to

`time_created`

(optional) The time the private endpoint was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_updated`

(optional) The time the private endpoint was updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`display_name`

(optional) Mutable name of the Private Reverse Connection Endpoint

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in 'Failed' state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`lifecycle_state`

(optional) The current state of the private endpoint resource.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`attached_catalogs`

(optional) The list of catalogs using the private reverse connection endpoint

`locks`

(optional) Locks associated with this resource.

### DBMS_CLOUD_OCI_DATACATALOG_CATALOG_SUMMARY_T Type

Summary of the data catalog.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(optional) Data catalog identifier, that can be renamed.

`compartment_id`

(required) Compartment identifier.

`time_created`

(optional) The time the data catalog was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_updated`

(optional) The time the data catalog was updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`number_of_objects`

(optional) The number of high level objects added to the data catalog.

`lifecycle_state`

(optional) The current state of the data catalog resource.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`lifecycle_details`

(optional) An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in 'Failed' state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`attached_catalog_private_endpoints`

(optional) The list of private reverse connection endpoints attached to the catalog

`locks`

(optional) Locks associated with this resource.

### DBMS_CLOUD_OCI_DATACATALOG_CHANGE_CATALOG_COMPARTMENT_DETAILS_T Type

Information about the change compartment

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The identifier of the compartment where the resource should be moved.

### DBMS_CLOUD_OCI_DATACATALOG_CHANGE_CATALOG_PRIVATE_ENDPOINT_COMPARTMENT_DETAILS_T Type

Information about the change compartment for the private endpoint resource

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The identifier of the compartment where the resource should be moved.

### DBMS_CLOUD_OCI_DATACATALOG_CHANGE_METASTORE_COMPARTMENT_DETAILS_T Type

Information about a change in metastore compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) OCID of the compartment to which the metastore should be moved.

### DBMS_CLOUD_OCI_DATACATALOG_CONNECTION_T Type

Detailed representation of a connection to a data asset, minus any sensitive properties.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique connection key that is immutable.

`description`

(optional) A description of the connection.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`time_created`

(optional) The date and time the connection was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`time_updated`

(optional) The last time that any change was made to the connection. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the connection.

`updated_by_id`

(optional) OCID of the user who modified the connection.

`custom_property_members`

(optional) The list of customized properties along with the values for this object

`properties`

(optional) A map of maps that contains the properties which are specific to the connection type. Each connection type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most connections have required properties within the \"default\" category. Example: `{\"properties\": { \"default\": { \"username\": \"user1\"}}}`

`external_key`

(optional) Unique external key of this object from the source system.

`time_status_updated`

(optional) Time that the connections status was last updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`lifecycle_state`

(optional) The current state of the connection.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`is_default`

(optional) Indicates whether this connection is the default connection.

`data_asset_key`

(optional) Unique key of the parent data asset.

`type_key`

(optional) The key of the object type. Type key's can be found via the '/types' endpoint.

`uri`

(optional) URI to the connection instance in the API.

### DBMS_CLOUD_OCI_DATACATALOG_CONNECTION_ALIAS_SUMMARY_T Type

Summary representation of database aliases parsed from the file metadata.

Syntax
```

```

Fields

Field Description

`alias_name`

(required) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`alias_details`

(optional) The description about the database alias parsed from the file metadata.

### DBMS_CLOUD_OCI_DATACATALOG_CONNECTION_SUMMARY_T Type

Summary representation of a connection to a data asset.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique connection key that is immutable.

`description`

(optional) A description of the connection.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`data_asset_key`

(optional) The unique key of the parent data asset.

`type_key`

(optional) The key of the object type. Type key's can be found via the '/types' endpoint.

`uri`

(optional) URI to the connection instance in the API.

`external_key`

(optional) Unique external key for this object as defined in the source systems.

`lifecycle_state`

(optional) The current state of the connection.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`is_default`

(optional) Indicates whether this connection is the default connection.

`time_created`

(optional) The date and time the connection was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_DATACATALOG_CONNECTION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_connection_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_CONNECTION_COLLECTION_T Type

Results of a connections listing. Each member of the result is a summary representation of a connection to a data asset.

Syntax
```

```

Fields

Field Description

`l_count`

(optional) Total number of items returned.

`items`

(required) Collection of connection summaries.

### DBMS_CLOUD_OCI_DATACATALOG_CUSTOM_PROPERTY_SET_USAGE_T Type

Details of a single custom property.

Syntax
```

```

Fields

Field Description

`key`

(optional) Unique Identifier of the attribute which is ID

`display_name`

(optional) Name of the custom property

`value`

(optional) The custom property value

`namespace_name`

(optional) Namespace name of the custom property

### DBMS_CLOUD_OCI_DATACATALOG_CUSTOM_PROPERTY_SET_USAGE_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_custom_property_set_usage_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_CREATE_ATTRIBUTE_DETAILS_T Type

Properties used in attribute create operations.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`business_name`

(optional) Optional user friendly business name of the attribute. If set, this supplements the harvested display name of the object.

`description`

(optional) Detailed description of the attribute.

`external_data_type`

(required) Data type of the attribute as defined in the external system.

`is_incremental_data`

(optional) Property that identifies if this attribute can be used as a watermark to extract incremental data.

`is_nullable`

(optional) Property that identifies if this attribute can be assigned null values.

`length`

(optional) Max allowed length of the attribute value.

`position`

(optional) Position of the attribute in the record definition.

`precision`

(optional) Precision of the attribute value usually applies to float data type.

`scale`

(optional) Scale of the attribute value usually applies to float data type.

`time_external`

(required) Last modified timestamp of this object in the external system.

`min_collection_count`

(optional) The minimum count for the number of instances of a given type stored in this collection type attribute,applicable if this attribute is a complex type.

`max_collection_count`

(optional) The maximum count for the number of instances of a given type stored in this collection type attribute,applicable if this attribute is a complex type. For type specifications in systems that specify only \"capacity\" without upper or lower bound , this property can also be used to just mean \"capacity\". Some examples are Varray size in Oracle , Occurs Clause in Cobol , capacity in XmlSchemaObjectCollection , maxOccurs in Xml , maxItems in Json

`external_datatype_entity_key`

(optional) External entity key that represents the datatype of this attribute , applicable if this attribute is a complex type.

`external_parent_attribute_key`

(optional) External attribute key that represents the parent attribute of this attribute , applicable if the parent attribute is of complex type.

`custom_property_members`

(optional) The list of customized properties along with the values for this object

`type_key`

(optional) Type key of the object. Type keys can be found via the '/types' endpoint.

`properties`

(optional) A map of maps that contains the properties which are specific to the attribute type. Each attribute type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most attributes have required properties within the \"default\" category. To determine the set of required and optional properties for an attribute type, a query can be done on '/types?type=attribute' that returns a collection of all attribute types. The appropriate attribute type, which will include definitions of all of it's properties, can be identified from this collection. Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_CREATE_CATALOG_DETAILS_T Type

The information about a new data catalog.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Data catalog identifier.

`compartment_id`

(required) Compartment identifier.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DATACATALOG_CREATE_CATALOG_PRIVATE_ENDPOINT_DETAILS_T Type

Information about the new private endpoint resource

Syntax
```

```

Fields

Field Description

`dns_zones`

(required) List of DNS zones to be used by the data assets to be harvested. Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com

`subnet_id`

(required) The OCID of subnet to which the reverse connection is to be created

`compartment_id`

(required) Compartment identifier.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) Display name of the private endpoint resource being created.

### DBMS_CLOUD_OCI_DATACATALOG_CREATE_CONNECTION_DETAILS_T Type

Properties used in connection create operations.

Syntax
```

```

Fields

Field Description

`description`

(optional) A description of the connection.

`display_name`

(required) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`type_key`

(required) The key of the object type. Type key's can be found via the '/types' endpoint.

`custom_property_members`

(optional) The list of customized properties along with the values for this object

`properties`

(required) A map of maps that contains the properties which are specific to the connection type. Each connection type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most connections have required properties within the \"default\" category. To determine the set of optional and required properties for a connection type, a query can be done on '/types?type=connection' that returns a collection of all connection types. The appropriate connection type, which will include definitions of all of it's properties, can be identified from this collection. Example: `{\"properties\": { \"default\": { \"username\": \"user1\"}}}`

`enc_properties`

(optional) A map of maps that contains the encrypted values for sensitive properties which are specific to the connection type. Each connection type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most connections have required properties within the \"default\" category. To determine the set of optional and required properties for a connection type, a query can be done on '/types?type=connection' that returns a collection of all connection types. The appropriate connection type, which will include definitions of all of it's properties, can be identified from this collection. Example: `{\"encProperties\": { \"default\": { \"password\": \"example-password\"}}}`

`is_default`

(optional) Indicates whether this connection is the default connection. The first connection of a data asset defaults to being the default, subsequent connections default to not being the default. If a default connection already exists, then trying to create a connection as the default will fail. In this case the default connection would need to be updated not to be the default and then the new connection can then be created as the default.

### DBMS_CLOUD_OCI_DATACATALOG_CREATE_CUSTOM_PROPERTY_DETAILS_T Type

Properties used in custom property create operations.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of the custom property.

`data_type`

(optional) The data type of the custom property

Allowed values are: 'TEXT', 'RICH_TEXT', 'BOOLEAN', 'NUMBER', 'DATE'

`is_sortable`

(optional) If this field allows to sort from UI

`is_filterable`

(optional) If this field allows to filter or create facets from UI

`is_multi_valued`

(optional) If this field allows multiple values to be set

`is_hidden`

(optional) If this field is a hidden field

`is_editable`

(optional) If this field is a editable field

`is_shown_in_list`

(optional) If this field is displayed in a list view of applicable objects.

`is_hidden_in_search`

(optional) If this field is allowed to pop in search results

`is_event_enabled`

(optional) If an OCI Event will be emitted when the custom property is modified.

`allowed_values`

(optional) Allowed values for the custom property if any

`properties`

(optional) A map of maps that contains the properties which are specific to the data asset type. Each data asset type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most data assets have required properties within the \"default\" category. To determine the set of optional and required properties for a data asset type, a query can be done on '/types?type=dataAsset' that returns a collection of all data asset types. The appropriate data asset type, which includes definitions of all of it's properties, can be identified from this collection. Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_CREATE_DATA_ASSET_DETAILS_T Type

Properties used in data asset create operations.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of the data asset.

`type_key`

(required) The key of the data asset type. This can be obtained via the '/types' endpoint.

`custom_property_members`

(optional) The list of customized properties along with the values for this object

`properties`

(optional) A map of maps that contains the properties which are specific to the data asset type. Each data asset type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most data assets have required properties within the \"default\" category. To determine the set of optional and required properties for a data asset type, a query can be done on '/types?type=dataAsset' that returns a collection of all data asset types. The appropriate data asset type, which includes definitions of all of it's properties, can be identified from this collection. Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_CREATE_ENTITY_DETAILS_T Type

Properties used in data entity create operations.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`business_name`

(optional) Optional user friendly business name of the data entity. If set, this supplements the harvested display name of the object.

`type_key`

(optional) The type of data entity object. Type key's can be found via the '/types' endpoint.

`description`

(optional) Detailed description of a data entity.

`time_external`

(required) Last modified timestamp of the object in the external system.

`is_logical`

(optional) Property to indicate if the object is a physical materialized object or virtual. For example, View.

`is_partition`

(optional) Property to indicate if the object is a sub object of a parent physical object.

`folder_key`

(optional) Key of the associated folder.

`pattern_key`

(optional) Key of the associated pattern if this is a logical entity.

`realized_expression`

(optional) The expression realized after resolving qualifiers . Used in deriving this logical entity

`harvest_status`

(optional) Status of the object as updated by the harvest process. When an entity object is created , it's harvest status will indicate if the entity's metadata has been fully harvested or not. The harvest process can perform shallow harvesting to allow users to browse the metadata and can on-demand deep harvest on any object This requires a harvest status indicator for catalog objects.

Allowed values are: 'COMPLETE', 'ERROR', 'IN_PROGRESS', 'DEFERRED'

`last_job_key`

(optional) Key of the last harvest process to update this object.

`custom_property_members`

(optional) The list of customized properties along with the values for this object

`properties`

(optional) A map of maps that contains the properties which are specific to the entity type. Each entity type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most entities have required properties within the \"default\" category. To determine the set of required and optional properties for an entity type, a query can be done on '/types?type=dataEntity' that returns a collection of all entity types. The appropriate entity type, which includes definitions of all of it's properties, can be identified from this collection. Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_CREATE_FOLDER_DETAILS_T Type

Properties used in folder create operations.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`business_name`

(optional) Optional user friendly business name of the folder. If set, this supplements the harvested display name of the object.

`description`

(optional) Detailed description of a folder.

`custom_property_members`

(optional) The list of customized properties along with the values for this object

`properties`

(optional) A map of maps that contains the properties which are specific to the folder type. Each folder type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most folders have required properties within the \"default\" category. To determine the set of optional and required properties for a folder type, a query can be done on '/types?type=folder' that returns a collection of all folder types. The appropriate folder type, which includes definitions of all of it's properties, can be identified from this collection. Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`

`parent_folder_key`

(optional) The key of the containing folder or null if there isn't a parent folder.

`time_external`

(required) Last modified timestamp of this object in the external system.

`last_job_key`

(optional) The job key of the harvest process that updated the folder definition from the source system.

`harvest_status`

(optional) Folder harvesting status.

Allowed values are: 'COMPLETE', 'ERROR', 'IN_PROGRESS', 'DEFERRED'

`type_key`

(optional) Type key of the object. Type keys can be found via the '/types' endpoint.

### DBMS_CLOUD_OCI_DATACATALOG_CREATE_GLOSSARY_DETAILS_T Type

Properties used in glossary create operations.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of the glossary.

`workflow_status`

(optional) Status of the approval process workflow for this business glossary.

Allowed values are: 'NEW', 'APPROVED', 'UNDER_REVIEW', 'ESCALATED'

`owner`

(optional) OCID of the user who is the owner of the glossary.

`custom_property_members`

(optional) The list of customized properties along with the values for this object

### DBMS_CLOUD_OCI_DATACATALOG_CREATE_JOB_DEFINITION_DETAILS_T Type

Representation of a job definition Resource. Job definitions define the harvest scope and includes the list of objects to be harvested along with a schedule. The list of objects is usually specified through a combination of object type, regular expressions, or specific names of objects and a sample size for the data harvested.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of the job definition.

`job_type`

(required) Type of the job definition.

Allowed values are: 'HARVEST', 'PROFILING', 'SAMPLING', 'PREVIEW', 'IMPORT', 'EXPORT', 'IMPORT_GLOSSARY', 'EXPORT_GLOSSARY', 'INTERNAL', 'PURGE', 'IMMEDIATE', 'SCHEDULED', 'IMMEDIATE_EXECUTION', 'SCHEDULED_EXECUTION', 'SCHEDULED_EXECUTION_INSTANCE', 'ASYNC_DELETE', 'IMPORT_DATA_ASSET', 'CREATE_SCAN_PROXY', 'ASYNC_EXPORT_GLOSSARY'

`is_incremental`

(optional) Specifies if the job definition is incremental or full.

`data_asset_key`

(optional) The key of the data asset for which the job is defined.

`glossary_key`

(optional) Unique key of the glossary to which this job applies.

`connection_key`

(optional) The key of the connection resource to be used for the job.

`is_sample_data_extracted`

(optional) Specify if sample data to be extracted as part of this harvest.

`sample_data_size_in_m_bs`

(optional) Specify the sample data size in MB, specified as number of rows, for this metadata harvest.

`properties`

(optional) A map of maps that contains the properties which are specific to the job type. Each job type definition may define it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most job definitions have required properties within the \"default\" category. Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_CREATE_JOB_DETAILS_T Type

Properties used to create a job.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of the job.

`schedule_cron_expression`

(optional) Interval on which the job will be run. Value is specified as a cron-supported time specification \"nickname\". The following subset of those is supported: @monthly, @weekly, @daily, @hourly. For metastore sync, an additional option @default is supported, which will schedule jobs at a more granular frequency.

`time_schedule_begin`

(optional) Date that the schedule should be operational. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_schedule_end`

(optional) Date that the schedule should end from being operational. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`connection_key`

(optional) The key of the connection used by the job. This connection will override the default connection specified in the associated job definition. All executions will use this connection.

`job_definition_key`

(required) The unique key of the job definition that defined the scope of this job.

### DBMS_CLOUD_OCI_DATACATALOG_CREATE_JOB_EXECUTION_DETAILS_T Type

Properties for creating a new job execution.

Syntax
```

```

Fields

Field Description

`sub_type`

(optional) Sub-type of this job execution.

`job_type`

(optional) Type of the job execution.

Allowed values are: 'HARVEST', 'PROFILING', 'SAMPLING', 'PREVIEW', 'IMPORT', 'EXPORT', 'IMPORT_GLOSSARY', 'EXPORT_GLOSSARY', 'INTERNAL', 'PURGE', 'IMMEDIATE', 'SCHEDULED', 'IMMEDIATE_EXECUTION', 'SCHEDULED_EXECUTION', 'SCHEDULED_EXECUTION_INSTANCE', 'ASYNC_DELETE', 'IMPORT_DATA_ASSET', 'CREATE_SCAN_PROXY', 'ASYNC_EXPORT_GLOSSARY'

`parent_key`

(optional) The unique key of the parent execution or null if this job execution has no parent.

`time_started`

(optional) Time that job execution started. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_ended`

(optional) Time that the job execution ended or null if it hasn't yet completed. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`lifecycle_state`

(optional) Status of the job execution, such as running, paused, or completed.

Allowed values are: 'CREATED', 'IN_PROGRESS', 'INACTIVE', 'FAILED', 'SUCCEEDED', 'CANCELED', 'SUCCEEDED_WITH_WARNINGS'

`error_code`

(optional) Error code returned from the job execution or null if job is still running or didn't return an error.

`error_message`

(optional) Error message returned from the job execution or null if job is still running or didn't return an error.

`schedule_instance_key`

(optional) The unique key of the triggering external scheduler resource or null if this job execution is not externally triggered.

`process_key`

(optional) Process identifier related to the job execution if the job is an external job.

`external_url`

(optional) If the job is an external process, then a URL of the job for accessing this resource and its status.

`event_key`

(optional) An identifier used for log message correlation.

`data_entity_key`

(optional) The key of the associated data entity resource.

`properties`

(optional) A map of maps that contains the execution context properties which are specific to a job execution. Each job execution may define it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most job executions have required properties within the \"default\" category. Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_CREATE_METASTORE_DETAILS_T Type

Information about a new metastore.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Mutable name of the metastore.

`compartment_id`

(required) OCID of the compartment which holds the metastore.

`default_managed_table_location`

(required) Location under which managed tables will be created by default. This references Object Storage using an HDFS URI format. Example: oci://bucket@namespace/sub-dir/

`default_external_table_location`

(required) Location under which external tables will be created by default. This references Object Storage using an HDFS URI format. Example: oci://bucket@namespace/sub-dir/

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DATACATALOG_CREATE_NAMESPACE_DETAILS_T Type

Properties used in custom property create operations.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of the Namespace.

`is_service_defined`

(optional) If this field is defined by service or by a user

### DBMS_CLOUD_OCI_DATACATALOG_CREATE_PATTERN_DETAILS_T Type

Properties used in pattern create operations.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of the Pattern.

`expression`

(optional) Input string which drives the selection process, allowing for fine-grained control using qualifiers. Refer to the user documentation for details of the format and examples. A pattern cannot include both a prefix and an expression.

`file_path_prefix`

(optional) Input string which drives the selection process. Refer to the user documentation for details of the format and examples. A pattern cannot include both a prefix and an expression.

`check_file_path_list`

(optional) List of file paths against which the pattern can be tried, as a check. This documents, for reference purposes, some example objects a pattern is meant to work with. If isEnableCheckFailureLimit is set to true, this will be run as a validation during the request, such that if the check fails the request fails. If isEnableCheckFailureLimit instead is set to (the default) false, a pattern will still be created or updated even if the check fails, with a lifecycleState of FAILED.

`is_enable_check_failure_limit`

(optional) Indicates whether the pattern check, against the checkFilePathList, will fail the request if the count of UNMATCHED files is above the checkFailureLimit.

`check_failure_limit`

(optional) The maximum number of UNMATCHED files, in checkFilePathList, above which the check fails. Optional, if checkFilePathList is provided - but if isEnableCheckFailureLimit is set to true it is required.

`properties`

(optional) A map of maps that contains the properties which are specific to the pattern type. Each pattern type definition defines it's set of required and optional properties. Example: `{\"properties\": { \"default\": { \"tbd\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_CREATE_TAG_DETAILS_T Type

Properties used in tag create operations.

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of the tag in the case of a free form tag. When linking to a glossary term, this field is not specified.

`term_key`

(optional) Unique key of the related term or null in the case of a free form tag.

### DBMS_CLOUD_OCI_DATACATALOG_CREATE_TERM_DETAILS_T Type

Properties used in term create operations.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly display name. Is changeable. The combination of 'displayName' and 'parentTermKey' must be unique. Avoid entering confidential information.

`description`

(optional) Detailed description of the term.

`is_allowed_to_have_child_terms`

(optional) Indicates whether a term may contain child terms.

`parent_term_key`

(optional) The parent key of the term. In the case of a root-level category only, the term would have no parent and this should be left unset.

`owner`

(optional) OCID of the user who is the owner of this business terminology.

`workflow_status`

(optional) Status of the approval process workflow for this business term in the glossary.

Allowed values are: 'NEW', 'APPROVED', 'UNDER_REVIEW', 'ESCALATED'

`custom_property_members`

(optional) The list of customized properties along with the values for this object

### DBMS_CLOUD_OCI_DATACATALOG_CREATE_TERM_RELATIONSHIP_DETAILS_T Type

Properties used in term relationship create operations.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly display name. Is changeable. The combination of 'displayName' and 'parentTermKey' must be unique. Avoid entering confidential information. This is the same as 'relationshipType' for 'termRelationship'.

`description`

(optional) Detailed description of the term relationship usually defined at the time of creation.

`related_term_key`

(required) Unique id of the related term.

### DBMS_CLOUD_OCI_DATACATALOG_CUSTOM_PROPERTY_TYPE_USAGE_T Type

Object which describes the indivial object stats for every custom property

Syntax
```

```

Fields

Field Description

`type_id`

(optional) Unique type key identifier

`type_name`

(optional) Name of the type associated with

`l_count`

(optional) Number of objects associated with this type

`is_event_enabled`

(optional) If an OCI Event will be emitted when the custom property is modified.

### DBMS_CLOUD_OCI_DATACATALOG_EVENT_CONFIG_T Type

Describes an event configuration, for a given object type and property. Primarily, whether a property change will result in an event being emitted.

Syntax
```

```

Fields

Field Description

`type_id`

(optional) Unique type key identifier.

`type_name`

(optional) Name of the type.

`property_id`

(optional) Unique property key identifier.

`property_name`

(optional) Name of the property.

`event_config_status`

(optional) Status of the configuration.

Allowed values are: 'ENABLED', 'DISABLED'

`time_created`

(optional) The date and time the event was configured, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`time_updated`

(optional) The last time that any change was made to the configuration. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the configuration.

`updated_by_id`

(optional) OCID of the user who last modified the configuration.

### DBMS_CLOUD_OCI_DATACATALOG_CUSTOM_PROPERTY_TYPE_USAGE_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_custom_property_type_usage_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_EVENT_CONFIG_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_event_config_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_CUSTOM_PROPERTY_T Type

Custom Property Definition

Syntax
```

```

Fields

Field Description

`key`

(required) Unique data asset key that is immutable.

`display_name`

(optional) Display name of the custom property

`data_type`

(optional) Data type of the custom property

Allowed values are: 'TEXT', 'RICH_TEXT', 'BOOLEAN', 'NUMBER', 'DATE'

`description`

(optional) Description for the custom property

`namespace_name`

(optional) Namespace name of the custom property

`is_list_type`

(optional) Is this property allowed to have list of values

`is_sortable`

(optional) If this field allows to sort from UI

`is_filterable`

(optional) If this field allows to filter or create facets from UI

`is_multi_valued`

(optional) If this field allows multiple values to be set

`is_hidden`

(optional) If this field is a hidden field

`is_editable`

(optional) If this field is a editable field

`is_shown_in_list`

(optional) If this field is displayed in a list view of applicable objects.

`is_service_defined`

(optional) If this field is defined by service or by a user

`is_hidden_in_search`

(optional) If this field is allowed to pop in search results

`lifecycle_state`

(optional) The current state of the custom property.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`time_created`

(optional) The date and time the custom property was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`time_updated`

(optional) The last time that any change was made to the custom property. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the custom property.

`updated_by_id`

(optional) OCID of the user who last modified the custom property.

`usage_count`

(optional) Total number of first class objects using this custom property

`is_event_enabled`

(optional) If an OCI Event will be emitted when the custom property is modified.

`scope`

(optional) The set of object types to which the custom property applies.

`allowed_values`

(optional) Allowed values for the custom property if any

`events`

(optional) Event configuration for this custom property, against the desired subset of object types to which the property applies.

`properties`

(optional) A map of maps that contains the properties which are specific to the asset type. Each data asset type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most data assets have required properties within the \"default\" category. Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_CUSTOM_PROPERTY_SUMMARY_T Type

Summary of a custom property

Syntax
```

```

Fields

Field Description

`key`

(required) Unique custom property key that is immutable.

`display_name`

(optional) Display name of the custom property

`description`

(optional) Description of the custom property

`data_type`

(optional) Data type of the custom property

Allowed values are: 'TEXT', 'RICH_TEXT', 'BOOLEAN', 'NUMBER', 'DATE'

`namespace_name`

(optional) Namespace name of the custom property

`is_sortable`

(optional) If this field allows to sort from UI

`is_filterable`

(optional) If this field allows to filter or create facets from UI

`is_multi_valued`

(optional) If this field allows multiple values to be set

`is_hidden`

(optional) If this field is a hidden field

`is_editable`

(optional) If this field is a editable field

`is_shown_in_list`

(optional) If this field is displayed in a list view of applicable objects.

`is_service_defined`

(optional) If this field is defined by service or by a user

`is_hidden_in_search`

(optional) If this field is allowed to pop in search results

`time_created`

(optional) The date and time the custom property was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`lifecycle_state`

(optional) The current state of the custom property.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`usage_count`

(optional) Total number of first class objects using this custom property

`scope`

(optional) Type or scope of the custom property belongs to. This will be an array of type id it will be belongs to

`allowed_values`

(optional) Allowed values for the custom property if any

`time_updated`

(optional) The last time that any change was made to the custom property. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the custom property.

`updated_by_id`

(optional) OCID of the user who last modified the custom property.

`is_event_enabled`

(optional) If an OCI Event will be emitted when the custom property is modified.

`events`

(optional) Event configuration for this custom property, against the desired subset of object types to which the property applies.

### DBMS_CLOUD_OCI_DATACATALOG_CUSTOM_PROPERTY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_custom_property_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_CUSTOM_PROPERTY_COLLECTION_T Type

Results of a custom properties listing. A custom property is an user defined attribute tied to the first class object of data catalog

Syntax
```

```

Fields

Field Description

`l_count`

(optional) Total number of items returned.

`items`

(required) Collection of custom property summaries

### DBMS_CLOUD_OCI_DATACATALOG_PATTERN_SUMMARY_T Type

Summary of a pattern. A pattern is a data selector or filter which can provide a singular, logical entity view aggregating multiple physical data artifacts for ease of use.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique pattern key that is immutable.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of the pattern.

`catalog_id`

(optional) The data catalog's OCID.

`time_created`

(optional) The date and time the pattern was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`expression`

(optional) Input string which drives the selection process, allowing for fine-grained control using qualifiers. Refer to the user documentation for details of the format and examples. A pattern cannot include both a prefix and an expression.

`file_path_prefix`

(optional) Input string which drives the selection process. Refer to the user documentation for details of the format and examples. A pattern cannot include both a prefix and an expression.

`lifecycle_state`

(optional) State of the pattern.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

### DBMS_CLOUD_OCI_DATACATALOG_PATTERN_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_pattern_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_DATA_ASSET_T Type

Data asset representation. A physical store, or stream, of data known to the data catalog and containing one or many data entities, possibly in an organized structure of folders. A data asset is often synonymous with a 'System', such as a database, or may be a file container or a message stream.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique data asset key that is immutable.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of the data asset.

`catalog_id`

(optional) The data catalog's OCID.

`external_key`

(optional) External URI that can be used to reference the object. Format will differ based on the type of object.

`type_key`

(optional) The key of the object type. Type key's can be found via the '/types' endpoint.

`lifecycle_state`

(optional) The current state of the data asset.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`lifecycle_details`

(optional) A message describing the current state in more detail. An object not in ACTIVE state may have functional limitations, see service documentation for details.

`time_created`

(optional) The date and time the data asset was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`time_updated`

(optional) The last time that any change was made to the data asset. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_harvested`

(optional) The last time that a harvest was performed on the data asset. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the data asset.

`updated_by_id`

(optional) OCID of the user who last modified the data asset.

`uri`

(optional) URI to the data asset instance in the API.

`custom_property_members`

(optional) The list of customized properties along with the values for this object

`data_selector_patterns`

(optional) The list of data selector patterns used in the harvest for this data asset to derive logical entities.

`properties`

(optional) A map of maps that contains the properties which are specific to the asset type. Each data asset type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most data assets have required properties within the \"default\" category. Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_DATA_ASSET_SUMMARY_T Type

Summary of a data asset. A physical store, or stream, of data known to the data catalog and containing one or many data entities, possibly in an organized structure of folders. A data asset is often synonymous with a 'System', such as a database, or may be a file container or a message stream.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique data asset key that is immutable.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of the data asset.

`catalog_id`

(optional) The data catalog's OCID.

`external_key`

(optional) External URI that can be used to reference the object. Format will differ based on the type of object.

`uri`

(optional) URI to the data asset instance in the API.

`time_created`

(optional) The date and time the data asset was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`type_key`

(optional) The key of the object type. Type keys's can be found via the '/types' endpoint.

`lifecycle_state`

(optional) State of the data asset.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`lifecycle_details`

(optional) A message describing the current state in more detail. An object not in ACTIVE state may have functional limitations, see service documentation for details.

### DBMS_CLOUD_OCI_DATACATALOG_DATA_ASSET_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_data_asset_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_DATA_ASSET_COLLECTION_T Type

Results of a data assets listing. A data asset is often synonymous with a 'System', such as a database, or may be a file container or a message stream.

Syntax
```

```

Fields

Field Description

`l_count`

(optional) Total number of items returned.

`items`

(required) Collection of data asset summaries.

### DBMS_CLOUD_OCI_DATACATALOG_DATA_ASSET_EXPORT_SCOPE_T Type

Scope of asset export, which consists of a container object (bucket, folder, schema, etc) within the asset, and types of child objects contained by that object to be included. objectKey - Key of the container object to be exported. For example, key of schema_1. exportTypeIds - Type key(s) of objects within the container object to be exported. For example, type key of table or view.

Syntax
```

```

Fields

Field Description

`object_key`

(optional) Unique key of the object selected for export.

`export_type_ids`

(optional) Array of type keys selected for export.

### DBMS_CLOUD_OCI_DATACATALOG_DATA_ASSET_PERMISSIONS_SUMMARY_T Type

Permissions object for data assets.

Syntax
```

```

Fields

Field Description

`data_asset_key`

(optional) The unique key of the parent data asset.

`user_permissions`

(optional) An array of permissions.

### DBMS_CLOUD_OCI_DATACATALOG_DATA_ASSET_TAG_T Type

Represents an association of a data asset to a term.

Syntax
```

```

Fields

Field Description

`data_asset_key`

(optional) The unique key of the parent data asset.

`key`

(required) Unique tag key that is immutable.

`name`

(optional) Name of the tag which matches the term name.

`term_key`

(optional) Unique key of the related term.

`term_path`

(optional) Path of the related term.

`term_description`

(optional) Description of the related term.

`lifecycle_state`

(optional) The current state of the tag.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`time_created`

(optional) The date and time the tag was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`created_by_id`

(optional) OCID of the user who created the tag.

`uri`

(optional) URI to the tag instance in the API.

### DBMS_CLOUD_OCI_DATACATALOG_DATA_ASSET_TAG_SUMMARY_T Type

Summary of a data asset tag.

Syntax
```

```

Fields

Field Description

`data_asset_key`

(optional) The unique key of the parent data asset.

`key`

(required) Unique tag key that is immutable.

`time_created`

(optional) The date and time the tag was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`name`

(optional) Name of the tag that matches the term name.

`uri`

(optional) URI to the tag instance in the API.

`term_key`

(optional) Unique key of the related term.

`term_path`

(optional) Path of the related term.

`term_description`

(optional) Description of the related term.

`glossary_key`

(optional) Unique id of the parent glossary of the term.

`lifecycle_state`

(optional) State of the Tag.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

### DBMS_CLOUD_OCI_DATACATALOG_DATA_ASSET_TAG_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_data_asset_tag_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_DATA_ASSET_TAG_COLLECTION_T Type

Results of a data asset tag listing. Data asset tags represent an association of a data asset to a term.

Syntax
```

```

Fields

Field Description

`l_count`

(optional) Total number of items returned.

`items`

(required) Collection of data asset tags.

### DBMS_CLOUD_OCI_DATACATALOG_DATA_SELECTOR_PATTERN_DETAILS_T Type

List of pattern Ids. Used in the addition and removal of patterns in data assets.

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of pattern Ids.

### DBMS_CLOUD_OCI_DATACATALOG_DERIVED_LOGICAL_ENTITIES_T Type

Entities derived from the application of a pattern to a list of file paths.

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of the derived logical entity. The group name of the unmatched files will be UNMATCHED

`realized_expression`

(optional) The expression realized after resolving qualifiers . Used in deriving this logical entity

`files_in_logical_grouping`

(optional) The list of file paths that belong to the grouping of logical entity or UNMATCHED for which realizedExpression is a selector.

### DBMS_CLOUD_OCI_DATACATALOG_DETACH_CATALOG_PRIVATE_ENDPOINT_DETAILS_T Type

Information about the detaching the private endpoint resource from a catalog

Syntax
```

```

Fields

Field Description

`catalog_private_endpoint_id`

(required) The identifier of the private endpoint to be detached from catalog resource.

### DBMS_CLOUD_OCI_DATACATALOG_ENTITY_T Type

Data entity details. A representation of data with a set of attributes, normally representing a single business entity. Synonymous with 'table' or 'view' in a database, or a single logical file structure that one or many files may match.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique data entity key that is immutable.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`business_name`

(optional) Optional user friendly business name of the data entity. If set, this supplements the harvested display name of the object.

`description`

(optional) Detailed description of a data entity.

`time_created`

(optional) The date and time the data entity was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`time_updated`

(optional) The last time that any change was made to the data entity. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created this object in the data catalog.

`updated_by_id`

(optional) OCID of the user who updated this object in the data catalog.

`lifecycle_state`

(optional) The current state of the data entity.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`lifecycle_details`

(optional) A message describing the current state in more detail. An object not in ACTIVE state may have functional limitations, see service documentation for details.

`external_key`

(optional) Unique external key of this object in the source system.

`pattern_key`

(optional) Key of the associated pattern if this is a logical entity.

`realized_expression`

(optional) The expression realized after resolving qualifiers . Used in deriving this logical entity

`time_external`

(optional) Last modified timestamp of this object in the external system.

`time_harvested`

(optional) The date and time the entity was harvested, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`object_relationships`

(optional) List of objects and their relationships to this entity.

`time_status_updated`

(optional) Time that the data entities status was last updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`is_logical`

(optional) Property that identifies if the object is a physical object (materialized) or virtual/logical object defined on other objects.

`is_partition`

(optional) Property that identifies if an object is a sub object of a physical or materialized parent object.

`data_asset_key`

(optional) Unique key of the parent data asset.

`folder_key`

(optional) Key of the associated folder.

`folder_name`

(optional) Name of the associated folder. This name is harvested from the source data asset when the parent folder for the entiy is harvested.

`path`

(optional) Full path of the data entity.

`harvest_status`

(optional) Status of the object as updated by the harvest process.

Allowed values are: 'COMPLETE', 'ERROR', 'IN_PROGRESS', 'DEFERRED'

`last_job_key`

(optional) Key of the last harvest process to update this object.

`type_key`

(optional) The type of data entity object. Type key's can be found via the '/types' endpoint.

`uri`

(optional) URI to the data entity instance in the API.

`object_storage_url`

(optional) URL of the data entity in the object store.

`custom_property_members`

(optional) The list of customized properties along with the values for this object

`properties`

(optional) A map of maps that contains the properties which are specific to the entity type. Each entity type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most data entities have required properties within the \"default\" category. Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_ENTITY_SUMMARY_T Type

Summary of an data entity. A representation of data with a set of attributes, normally representing a single business entity. Synonymous with 'table' or 'view' in a database, or a single logical file structure that one or many files may match.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique data entity key that is immutable.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`business_name`

(optional) Optional user friendly business name of the data entity. If set, this supplements the harvested display name of the object.

`description`

(optional) Detailed description of a data entity.

`is_logical`

(optional) Property that identifies if the object is a physical object (materialized) or virtual/logical object defined on other objects.

`is_partition`

(optional) Property that identifies if an object is a sub object of a physical or materialized parent object.

`data_asset_key`

(optional) Unique key of the parent data asset.

`folder_key`

(optional) Key of the associated folder.

`folder_name`

(optional) Name of the associated folder. This name is harvested from the source data asset when the parent folder for the entiy is harvested.

`external_key`

(optional) Unique external key of this object in the source system.

`pattern_key`

(optional) Key of the associated pattern if this is a logical entity.

`type_key`

(optional) The type of data entity object. Type keys can be found via the '/types' endpoint.

`realized_expression`

(optional) The expression realized after resolving qualifiers . Used in deriving this logical entity

`path`

(optional) Full path of the data entity.

`time_created`

(optional) The date and time the data entity was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`time_updated`

(optional) The last time that any change was made to the data entity. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`updated_by_id`

(optional) OCID of the user who updated this object in the data catalog.

`uri`

(optional) URI to the data entity instance in the API.

`object_storage_url`

(optional) URL of the data entity in the object store.

`lifecycle_state`

(optional) State of the data entity.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`lifecycle_details`

(optional) A message describing the current state in more detail. An object not in ACTIVE state may have functional limitations, see service documentation for details.

`properties`

(optional) A map of maps that contains the properties which are specific to the entity type. Each entity type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most data entities have required properties within the \"default\" category. Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_ENTITY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_entity_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_ENTITY_COLLECTION_T Type

Results of a data entities listing. Data entities are representation of a dataset with a set of attributes.

Syntax
```

```

Fields

Field Description

`l_count`

(optional) Total number of items returned.

`items`

(required) Collection of data entities.

### DBMS_CLOUD_OCI_DATACATALOG_LINEAGE_OBJECT_T Type

Object describing an individual element of object lineage.

Syntax
```

```

Fields

Field Description

`object_key`

(optional) Key of the object, such as an entity, about which this lineage applies.

`display_name`

(optional) Display name of the object.

`description`

(optional) Detailed description of the object.

`is_intra_lineage_available`

(optional) Indicates if intra-lineage is available for this given object. If yes, drill-down can be requested for this object.

`parent_key`

(optional) Key of the parent object for this object.

`parent_path`

(optional) Full path of the parent object.

`time_created`

(optional) The time that this object was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_updated`

(optional) The time that this object was updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`type_name`

(optional) Type name of the object. Type keys can be found via the '/types' endpoint.

`type_key`

(optional) Type key of the object. Type keys can be found via the '/types' endpoint.

`properties`

(optional) A map of maps that contains the properties which are specific to the entity type. Each entity type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most data entities have required properties within the \"default\" category. Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_LINEAGE_RELATIONSHIP_T Type

Declares how two elements of object lineage are related.

Syntax
```

```

Fields

Field Description

`from_object_key`

(optional) Object key of source lineage element.

`to_object_key`

(optional) Object key of target lineage element.

`relationship_type`

(optional) Type of the relationship.

### DBMS_CLOUD_OCI_DATACATALOG_LINEAGE_OBJECT_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_lineage_object_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_LINEAGE_RELATIONSHIP_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_lineage_relationship_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_ENTITY_LINEAGE_T Type

Lineage for a data entity.

Syntax
```

```

Fields

Field Description

`l_level`

(required) Object level at which the lineage is returned.

`direction`

(required) Direction of the lineage returned.

Allowed values are: 'UPSTREAM', 'BOTH', 'DOWNSTREAM'

`objects`

(optional) Set of objects that are involved in the lineage.

`relationships`

(optional) Set of relationships between the objects in the 'objects' set.

`annotations`

(optional) A map of maps that contains additional information in explanation of the lineage returned. The map keys are categories of information and the values are maps of annotation names to their corresponding values. Every annotation is contained inside a category. Example: `{\"annotations\": { \"category\": { \"key\": \"value\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_ENTITY_TAG_T Type

Represents an association of an entity to a term.

Syntax
```

```

Fields

Field Description

`entity_key`

(optional) The unique key of the parent entity.

`key`

(required) Unique tag key that is immutable.

`name`

(optional) Name of the tag which matches the term name.

`term_key`

(optional) Unique key of the related term.

`term_path`

(optional) Path of the related term.

`term_description`

(optional) Description of the related term.

`lifecycle_state`

(optional) The current state of the tag.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`time_created`

(optional) The date and time the tag was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`created_by_id`

(optional) OCID of the user who created the tag.

`uri`

(optional) URI to the tag instance in the API.

### DBMS_CLOUD_OCI_DATACATALOG_ENTITY_TAG_SUMMARY_T Type

Summary of an entity tag.

Syntax
```

```

Fields

Field Description

`entity_key`

(optional) The unique key of the parent entity.

`key`

(required) Unique tag key that is immutable.

`time_created`

(optional) The date and time the tag was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`name`

(optional) Name of the tag that matches the term name.

`uri`

(optional) URI to the tag instance in the API.

`term_key`

(optional) Unique key of the related term.

`term_path`

(optional) Path of the related term.

`term_description`

(optional) Description of the related term.

`glossary_key`

(optional) Unique id of the parent glossary of the term.

`lifecycle_state`

(optional) State of the Tag.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

### DBMS_CLOUD_OCI_DATACATALOG_ENTITY_TAG_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_entity_tag_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_ENTITY_TAG_COLLECTION_T Type

Results of an entity tags listing. Entity tags allow assciation of business terms with entities.

Syntax
```

```

Fields

Field Description

`l_count`

(optional) Total number of items returned.

`items`

(required) Collection of entity tags.

### DBMS_CLOUD_OCI_DATACATALOG_ERROR_T Type

Error Information.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_DATACATALOG_DATA_ASSET_EXPORT_SCOPE_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_data_asset_export_scope_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_EXPORT_DATA_ASSET_DETAILS_T Type

The details of what needs to be exported.

Syntax
```

```

Fields

Field Description

`export_scope`

(optional) Array of objects and their child types to be selected for export.

### DBMS_CLOUD_OCI_DATACATALOG_FACETED_SEARCH_AGGREGATION_T Type

Aggregation/facets on properties of data object.

Syntax
```

```

Fields

Field Description

`l_type`

(optional) Name of data object property

`aggregation`

(optional) Count of number of data objects having property.

`data_type`

(optional) Data type of object property.

`property_type`

(optional) Type of property that indicates if it was defined by the user or system. CUSTOM_PROPERTY is defined by the user on a data object. DEFAULT_PROPERTY is defined by the system on a data object.

Allowed values are: 'CUSTOM_PROPERTY', 'DEFAULT_PROPERTY'

### DBMS_CLOUD_OCI_DATACATALOG_FACETED_SEARCH_CUSTOM_PROPERTY_T Type

Details about custom property

Syntax
```

```

Fields

Field Description

`name`

(optional) Name of custom property field

`value`

(optional) Value of the custom property field

`data_type`

(optional) Data type of the custom property field

### DBMS_CLOUD_OCI_DATACATALOG_FACETED_SEARCH_DATE_FILTER_REQUEST_T Type

Object with date filter criteria

Syntax
```

```

Fields

Field Description

`field_name`

(optional) Date field name that needs to be filtered by. Acceptable fields include TimeCreated and TimeUpdated.

`time_after`

(optional) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_before`

(optional) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

### DBMS_CLOUD_OCI_DATACATALOG_FACETED_SEARCH_STRING_FILTER_REQUEST_T Type

Object with string filter criteria

Syntax
```

```

Fields

Field Description

`field`

(optional) String/boolean/numerical field name that needs to be filtered by. Acceptable field names: CatalogType, AttributeType, FolderType, DataAssetType, CreatedBy, UpdatedBy, Term, Tag, DataAssetName, LifeCycleState.

`l_values`

(optional) Array of values that the search results needs to be filtered by. Acceptable values for field 'CatalogType': DataAsset, Folder, DataEntity, Attribute, Term, Category, Glossary, Pattern, Job, Schedule, CustomProperty. For other fields, acceptable values can be derived by inspecting the data object.

### DBMS_CLOUD_OCI_DATACATALOG_FACETED_SEARCH_DATE_FILTER_REQUEST_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_faceted_search_date_filter_request_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_FACETED_SEARCH_STRING_FILTER_REQUEST_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_faceted_search_string_filter_request_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_FACETED_SEARCH_FILTER_REQUEST_T Type

Object with details about filter criteria.

Syntax
```

```

Fields

Field Description

`search_date_filters`

(optional) Object with date filter criteria

`search_string_filters`

(optional) Object with string filter criteria

### DBMS_CLOUD_OCI_DATACATALOG_FACETED_SEARCH_SORT_REQUEST_T Type

Object with sort criteria details

Syntax
```

```

Fields

Field Description

`sort_by`

(optional) Filed name that needs to be sorted by.

`sort_order`

(optional) Sort order for search results.

Allowed values are: 'ASC', 'DESC'

### DBMS_CLOUD_OCI_DATACATALOG_FETCH_ENTITY_LINEAGE_DETAILS_T Type

The information needed to obtain desired lineage.

Syntax
```

```

Fields

Field Description

`l_level`

(optional) Object level at which the lineage is returned.

`direction`

(optional) Direction of the lineage returned.

Allowed values are: 'UPSTREAM', 'BOTH', 'DOWNSTREAM'

`is_intra_lineage`

(optional) Intra-lineages are drill down lineages. This field indicates whether all intra-lineages need to be expanded inline in the lineage returned.

`intra_lineage_object_key`

(optional) Unique object key for which intra-lineage needs to be fetched. Only drill-down lineage corresponding to the object whose object key is passed is returned.

### DBMS_CLOUD_OCI_DATACATALOG_FOLDER_T Type

A generic term used in the data catalog for an external organization concept used for a collection of data entities or processes within a data asset. This term is an internal term which models multiple external types of folder, such as file directories, database schemas, and so on. Some data assets, such as Object Store containers, may contain many levels of folders.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique folder key that is immutable.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`business_name`

(optional) Optional user friendly business name of the folder. If set, this supplements the harvested display name of the object.

`description`

(optional) Detailed description of a folder.

`parent_folder_key`

(optional) The unique key of the containing folder or null if there is no parent folder.

`type_key`

(optional) The type of folder object. Type keys can be found via the '/types' endpoint.

`time_harvested`

(optional) The date and time the folder was harvested, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`object_relationships`

(optional) List of objects and their relationships to this folder.

`path`

(optional) Full path of the folder.

`data_asset_key`

(optional) The key of the associated data asset.

`custom_property_members`

(optional) The list of customized properties along with the values for this object

`properties`

(optional) A map of maps that contains the properties which are specific to the folder type. Each folder type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most folders have required properties within the \"default\" category. Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`

`external_key`

(optional) Unique external key of this object in the source system.

`time_created`

(optional) The date and time the folder was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`time_updated`

(optional) The last time that any change was made to the folder. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the folder.

`updated_by_id`

(optional) OCID of the user who modified the folder.

`time_external`

(optional) Last modified timestamp of this object in the external system.

`lifecycle_state`

(optional) The current state of the folder.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`lifecycle_details`

(optional) A message describing the current state in more detail. An object not in ACTIVE state may have functional limitations, see service documentation for details.

`harvest_status`

(optional) Status of the object as updated by the harvest process.

Allowed values are: 'COMPLETE', 'ERROR', 'IN_PROGRESS', 'DEFERRED'

`last_job_key`

(optional) The key of the last harvest process to update the metadata of this object.

`uri`

(optional) URI to the folder instance in the API.

`object_storage_url`

(optional) URL of the folder in the object store.

### DBMS_CLOUD_OCI_DATACATALOG_FOLDER_SUMMARY_T Type

Summary of a folder. A generic term used in the data catalog for an external organization concept used for a collection of data entities or processes within a data asset. This term is an internal term which models multiple external types of folder, such as file directories, database schemas, and so on. Some data assets, such as Object Store containers, may contain many levels of folders.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique folder key that is immutable.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`business_name`

(optional) Optional user friendly business name of the folder. If set, this supplements the harvested display name of the object.

`description`

(optional) Detailed description of a folder.

`data_asset_key`

(optional) The unique key of the parent data asset.

`parent_folder_key`

(optional) The key of the containing folder or null if there is no parent.

`type_key`

(optional) The type of folder object. Type keys can be found via the '/types' endpoint.

`path`

(optional) Full path of the folder.

`external_key`

(optional) Unique external key of this object from the source systems.

`time_external`

(optional) Last modified timestamp of this object in the external system.

`time_created`

(optional) The date and time the folder was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`time_updated`

(optional) The date and time the folder was last updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: 2019-03-25T21:10:29.600Z

`uri`

(optional) URI of the folder resource within the data catalog API.

`object_storage_url`

(optional) URL of the folder in the object store.

`lifecycle_state`

(optional) State of the folder.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`lifecycle_details`

(optional) A message describing the current state in more detail. An object not in ACTIVE state may have functional limitations, see service documentation for details.

### DBMS_CLOUD_OCI_DATACATALOG_FOLDER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_folder_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_FOLDER_COLLECTION_T Type

Results of a folders listing. Folders are external organization concept that groups data entities.

Syntax
```

```

Fields

Field Description

`l_count`

(optional) Total number of items returned.

`items`

(required) Collection of folders.

### DBMS_CLOUD_OCI_DATACATALOG_FOLDER_TAG_T Type

Represents an association of a folder to a term.

Syntax
```

```

Fields

Field Description

`folder_key`

(optional) The unique key of the folder associated with this tag.

`key`

(required) Unique tag key that is immutable.

`name`

(optional) Name of the tag which matches the term name.

`term_key`

(optional) Unique key of the related term.

`term_path`

(optional) Path of the related term.

`term_description`

(optional) Description of the related term.

`lifecycle_state`

(optional) The current state of the tag.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`time_created`

(optional) The date and time the tag was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`created_by_id`

(optional) OCID of the user who created the tag.

`uri`

(optional) URI to the tag instance in the API.

### DBMS_CLOUD_OCI_DATACATALOG_FOLDER_TAG_SUMMARY_T Type

Summary of a folder tag.

Syntax
```

```

Fields

Field Description

`folder_key`

(optional) The unique key of the parent folder.

`key`

(required) Unique tag key that is immutable.

`time_created`

(optional) The date and time the tag was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`name`

(optional) Name of the tag that matches the term name.

`uri`

(optional) URI to the tag instance in the API.

`term_key`

(optional) Unique key of the related term.

`term_path`

(optional) Path of the related term.

`term_description`

(optional) Description of the related term.

`glossary_key`

(optional) Unique id of the parent glossary of the term.

`lifecycle_state`

(optional) State of the Tag.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

### DBMS_CLOUD_OCI_DATACATALOG_FOLDER_TAG_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_folder_tag_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_FOLDER_TAG_COLLECTION_T Type

Results of a folders tag listing. Folder tags allow association of folder objects to business terms.

Syntax
```

```

Fields

Field Description

`l_count`

(optional) Total number of items returned.

`items`

(required) Collection of folder tags.

### DBMS_CLOUD_OCI_DATACATALOG_GLOSSARY_T Type

Full glossary details. A glossary of business terms, such as 'Customer', 'Account', 'Contact' , 'Address', or 'Product', with definitions, used to provide common meaning across disparate data assets. Business glossaries may be hierarchical where some terms may contain child terms to allow them to be used as 'taxonomies'. By linking data assets, data entities, and attributes to glossaries and glossary terms, the glossary can act as a way of organizing data catalog objects in a hierarchy to make a large number of objects more navigable and easier to consume. Objects in the data aatalog, such as data assets or data entities, may be linked to any level in the glossary, so that the glossary can be used to browse the available data according to the business model of the organization.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique glossary key that is immutable.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of the glossary.

`catalog_id`

(optional) The data catalog's OCID.

`lifecycle_state`

(optional) The current state of the glossary.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`time_created`

(optional) The date and time the glossary was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`time_updated`

(optional) The last time that any change was made to the glossary. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created this metadata element.

`updated_by_id`

(optional) OCID of the user who updated this metadata element.

`owner`

(optional) OCID of the user who is the owner of the glossary.

`workflow_status`

(optional) Status of the approval process workflow for this business glossary.

Allowed values are: 'NEW', 'APPROVED', 'UNDER_REVIEW', 'ESCALATED'

`custom_property_members`

(optional) The list of customized properties along with the values for this object

`import_job_definition_key`

(optional) The unique key of the job definition resource that was used in the Glossary import.

`import_job_key`

(optional) The unique key of the job policy for Glossary import.

`latest_import_job_execution_key`

(optional) The unique key of the parent job execution for which the log resource was created.

`latest_import_job_execution_status`

(optional) Status of the latest glossary import job execution, such as running, paused, or completed. This may include additional information like time import started , import file size and % of completion

`uri`

(optional) URI to the tag instance in the API.

### DBMS_CLOUD_OCI_DATACATALOG_GLOSSARY_SUMMARY_T Type

Summary of a glossary. A glossary of business terms, such as 'Customer', 'Account', 'Contact', 'Address', or 'Product', with definitions, used to provide common meaning across disparate data assets. Business glossaries may be hierarchical where some terms may contain child terms to allow them to be used as 'taxonomies'. By linking data assets, data entities, and attributes to glossaries and glossary terms, the glossary can act as a way of organizing data catalog objects in a hierarchy to make a large number of objects more navigable and easier to consume. Objects in the data catalog, such as data assets or data entities, may be linked to any level in the glossary, so that the glossary can be used to browse the available data according to the business model of the organization.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique glossary key that is immutable.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`catalog_id`

(optional) The data catalog's OCID.

`time_created`

(optional) The date and time the glossary was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`description`

(optional) Detailed description of the glossary.

`uri`

(optional) URI to the glossary instance in the API.

`workflow_status`

(optional) Status of the approval process workflow for this business glossary.

Allowed values are: 'NEW', 'APPROVED', 'UNDER_REVIEW', 'ESCALATED'

`lifecycle_state`

(optional) State of the Glossary.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`import_job_definition_key`

(optional) The unique key of the job definition resource that was used in the Glossary import.

`import_job_key`

(optional) The unique key of the job policy for Glossary import.

`latest_import_job_execution_key`

(optional) The unique key of the parent job execution for which the log resource was created.

`latest_import_job_execution_status`

(optional) Status of the latest glossary import job execution, such as running, paused, or completed. This may include additional information like time import started , import file size and % of completion

### DBMS_CLOUD_OCI_DATACATALOG_GLOSSARY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_glossary_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_GLOSSARY_COLLECTION_T Type

Results of a glossaries listing. Glossary is an organizing concept for business terms to provide a unified semantic model across disparate data assets.

Syntax
```

```

Fields

Field Description

`l_count`

(optional) Total number of items returned.

`items`

(required) Collection of glossaries.

### DBMS_CLOUD_OCI_DATACATALOG_GLOSSARY_PERMISSIONS_SUMMARY_T Type

Permissions object for glosssaries.

Syntax
```

```

Fields

Field Description

`glossary_key`

(optional) The unique key of the parent glossary.

`user_permissions`

(optional) An array of permissions.

### DBMS_CLOUD_OCI_DATACATALOG_GLOSSARY_TREE_ELEMENT_ABS_T

Glossary tree element with child terms.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique term key that is immutable.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of the term.

`glossary_key`

(optional) Unique id of the parent glossary.

`uri`

(optional) URI to the term instance in the API.

`parent_term_key`

(optional) This terms parent term key. Will be null if the term has no parent term.

`is_allowed_to_have_child_terms`

(optional) Indicates whether a term may contain child terms.

`path`

(optional) Absolute path of the term.

`time_created`

(optional) The date and time the term was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`workflow_status`

(optional) Status of the approval process workflow for this business term in the glossary.

Allowed values are: 'NEW', 'APPROVED', 'UNDER_REVIEW', 'ESCALATED'

`associated_object_count`

(optional) The number of objects tagged with this term.

`lifecycle_state`

(optional) State of the term.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

### DBMS_CLOUD_OCI_DATACATALOG_GLOSSARY_TREE_ELEMENT_ABS_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_glossary_tree_element_abs_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_GLOSSARY_TREE_ELEMENT_T Type

Glossary tree element with child terms.

Syntax
```

```

Fields

Field Description

`child_terms`

(optional) An array of child terms.

### DBMS_CLOUD_OCI_DATACATALOG_GLOSSARY_TREE_ELEMENT_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_glossary_tree_element_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_IMPORT_CONNECTION_DETAILS_T Type

Import connection from the connection metadata and oracle wallet file.

Syntax
```

```

Fields

Field Description

`connection_detail`

(optional)

`connection_payload`

(required) The information used to import the connection.

### DBMS_CLOUD_OCI_DATACATALOG_IMPORT_DATA_ASSET_DETAILS_T Type

Specifies the file contents to be imported.

Syntax
```

```

Fields

Field Description

`import_file_contents`

(required) The file contents to be imported. File size not to exceed 10 MB.

### DBMS_CLOUD_OCI_DATACATALOG_IMPORT_DATA_ASSET_JOB_RESULT_T Type

Information about a data asset import operation.

Syntax
```

```

Fields

Field Description

`data_asset_key`

(required) The unique key of the data asset on which import is triggered.

`import_job_definition_key`

(optional) The unique key of the job definition resource that is used for the import.

`import_job_key`

(optional) The unique key of the job policy for the import.

`import_job_execution_key`

(optional) The unique key of the parent job execution for which the log resource is created.

`import_job_execution_status`

(optional) The status of the import job execution.

Allowed values are: 'CREATED', 'IN_PROGRESS', 'INACTIVE', 'FAILED', 'SUCCEEDED', 'CANCELED', 'SUCCEEDED_WITH_WARNINGS'

### DBMS_CLOUD_OCI_DATACATALOG_IMPORT_GLOSSARY_DETAILS_T Type

Import glossary from the contents of the glossary definition file.

Syntax
```

```

Fields

Field Description

`glossary_file_contents`

(optional) The file contents used for the import of glossary.

### DBMS_CLOUD_OCI_DATACATALOG_JOB_T Type

Details of a job. Jobs are scheduled instances of a job definition.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique key of the job resource.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of the job.

`catalog_id`

(optional) The data catalog's OCID.

`lifecycle_state`

(optional) Lifecycle state for job.

Allowed values are: 'ACTIVE', 'INACTIVE', 'EXPIRED'

`time_created`

(optional) The date and time the job was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`time_updated`

(optional) Time that this job was last updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`job_type`

(optional) Type of the job.

Allowed values are: 'HARVEST', 'PROFILING', 'SAMPLING', 'PREVIEW', 'IMPORT', 'EXPORT', 'IMPORT_GLOSSARY', 'EXPORT_GLOSSARY', 'INTERNAL', 'PURGE', 'IMMEDIATE', 'SCHEDULED', 'IMMEDIATE_EXECUTION', 'SCHEDULED_EXECUTION', 'SCHEDULED_EXECUTION_INSTANCE', 'ASYNC_DELETE', 'IMPORT_DATA_ASSET', 'CREATE_SCAN_PROXY', 'ASYNC_EXPORT_GLOSSARY'

`schedule_cron_expression`

(optional) Interval on which the job will be run. Value is specified as a cron-supported time specification \"nickname\". The following subset of those is supported: @monthly, @weekly, @daily, @hourly. For metastore sync, an additional option @default is supported, which will schedule jobs at a more granular frequency.

`time_schedule_begin`

(optional) Date that the schedule should be operational. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_schedule_end`

(optional) Date that the schedule should end from being operational. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`schedule_type`

(optional) Type of job schedule that is inferred from the scheduling properties.

Allowed values are: 'SCHEDULED', 'IMMEDIATE'

`connection_key`

(optional) The key of the connection used by the job. This connection will override the default connection specified in the associated job definition. All executions will use this connection.

`job_definition_key`

(optional) The unique key of the job definition resource that defined the scope of this job.

`internal_version`

(optional) Internal version of the job resource.

`execution_count`

(optional) The total number of executions for this job schedule.

`time_of_latest_execution`

(optional) The date and time of the most recent execution for this Job, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`created_by_id`

(optional) OCID of the user who created this job.

`updated_by_id`

(optional) OCID of the user who updated this job.

`job_definition_name`

(optional) The display name of the job definition resource that defined the scope of this job.

`data_asset_key`

(optional) Unique key of the data asset to which this job applies, if the job involves a data asset.

`glossary_key`

(optional) Unique key of the glossary to which this job applies.

`error_code`

(optional) Error code returned from the latest job execution for this job. Useful when the latest Job execution is in FAILED state.

`error_message`

(optional) Error message returned from the latest job execution for this job. Useful when the latest Job Execution is in a FAILED state.

`uri`

(optional) URI to the job instance in the API.

### DBMS_CLOUD_OCI_DATACATALOG_JOB_EXECUTION_SUMMARY_T Type

A list of job executions. A job execution is a unit of work being executed on behalf of a job.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique key of the job execution resource.

`job_key`

(optional) The unique key of the parent job.

`job_type`

(optional) Type of the job execution.

Allowed values are: 'HARVEST', 'PROFILING', 'SAMPLING', 'PREVIEW', 'IMPORT', 'EXPORT', 'IMPORT_GLOSSARY', 'EXPORT_GLOSSARY', 'INTERNAL', 'PURGE', 'IMMEDIATE', 'SCHEDULED', 'IMMEDIATE_EXECUTION', 'SCHEDULED_EXECUTION', 'SCHEDULED_EXECUTION_INSTANCE', 'ASYNC_DELETE', 'IMPORT_DATA_ASSET', 'CREATE_SCAN_PROXY', 'ASYNC_EXPORT_GLOSSARY'

`parent_key`

(optional) The unique key of the parent execution or null if this job execution has no parent.

`schedule_instance_key`

(optional) The unique key of the triggering external scheduler resource or null if this job execution is not externally triggered.

`lifecycle_state`

(optional) Status of the job execution, such as running, paused, or completed.

Allowed values are: 'CREATED', 'IN_PROGRESS', 'INACTIVE', 'FAILED', 'SUCCEEDED', 'CANCELED', 'SUCCEEDED_WITH_WARNINGS'

`time_created`

(optional) The date and time the job execution was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`time_started`

(optional) Time that job execution started. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_ended`

(optional) Time that the job execution ended or null if it hasn't yet completed. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`uri`

(optional) URI to the job execution instance in the API.

### DBMS_CLOUD_OCI_DATACATALOG_JOB_EXECUTION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_job_execution_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_JOB_SUMMARY_T Type

Details of a job. Jobs are scheduled instances of a job definition.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique key of the job.

`uri`

(optional) URI to the job instance in the API.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`catalog_id`

(optional) The data catalog's OCID.

`job_definition_key`

(optional) The unique key of the job definition resource that defined the scope of this job.

`lifecycle_state`

(optional) Lifecycle state of the job, such as running, paused, or completed.

Allowed values are: 'ACTIVE', 'INACTIVE', 'EXPIRED'

`job_type`

(optional) Type of the job.

Allowed values are: 'HARVEST', 'PROFILING', 'SAMPLING', 'PREVIEW', 'IMPORT', 'EXPORT', 'IMPORT_GLOSSARY', 'EXPORT_GLOSSARY', 'INTERNAL', 'PURGE', 'IMMEDIATE', 'SCHEDULED', 'IMMEDIATE_EXECUTION', 'SCHEDULED_EXECUTION', 'SCHEDULED_EXECUTION_INSTANCE', 'ASYNC_DELETE', 'IMPORT_DATA_ASSET', 'CREATE_SCAN_PROXY', 'ASYNC_EXPORT_GLOSSARY'

`schedule_type`

(optional) Type of job schedule that is inferred from the scheduling properties.

`description`

(optional) Detailed description of the job.

`time_created`

(optional) The date and time the job was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`time_updated`

(optional) Time that this job was last updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created this job.

`updated_by_id`

(optional) OCID of the user who updated this job.

`schedule_cron_expression`

(optional) Interval on which the job will be run. Value is specified as a cron-supported time specification \"nickname\". The following subset of those is supported: @monthly, @weekly, @daily, @hourly. For metastore sync, an additional option @default is supported, which will schedule jobs at a more granular frequency.

`time_schedule_begin`

(optional) Date that the schedule should be operational. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`execution_count`

(optional) The total number of executions for this job schedule.

`time_of_latest_execution`

(optional) The date and time of the most recent execution for this job, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`job_definition_name`

(optional) The display name of the job definition resource that defined the scope of this job.

`data_asset_key`

(optional) Unique key of the data asset to which this job applies, if the job involves a data asset.

`glossary_key`

(optional) Unique key of the glossary to which this job applies.

`error_code`

(optional) Error code returned from the latest job execution for this job. Useful when the latest Job execution is in FAILED state.

`error_message`

(optional) Error message returned from the latest job execution for this job. Useful when the latest Job Execution is in a FAILED state.

`executions`

(optional) Array of the executions summary associated with this job.

### DBMS_CLOUD_OCI_DATACATALOG_JOB_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_job_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_JOB_COLLECTION_T Type

Results of a jobs listing. Jobs are scheduled instances of a job definition.

Syntax
```

```

Fields

Field Description

`l_count`

(optional) Total number of items returned.

`items`

(required) Collection of jobs.

### DBMS_CLOUD_OCI_DATACATALOG_JOB_DEFINITION_T Type

Representation of a job definition resource. Job definitions define the harvest scope and includes the list of objects to be harvested along with a schedule. The list of objects is usually specified through a combination of object type, regular expressions, or specific names of objects and a sample size for the data harvested.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique key of the job definition resource that is immutable.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`catalog_id`

(optional) The data catalog's OCID.

`job_type`

(optional) Type of the job definition.

Allowed values are: 'HARVEST', 'PROFILING', 'SAMPLING', 'PREVIEW', 'IMPORT', 'EXPORT', 'IMPORT_GLOSSARY', 'EXPORT_GLOSSARY', 'INTERNAL', 'PURGE', 'IMMEDIATE', 'SCHEDULED', 'IMMEDIATE_EXECUTION', 'SCHEDULED_EXECUTION', 'SCHEDULED_EXECUTION_INSTANCE', 'ASYNC_DELETE', 'IMPORT_DATA_ASSET', 'CREATE_SCAN_PROXY', 'ASYNC_EXPORT_GLOSSARY'

`is_incremental`

(optional) Specifies if the job definition is incremental or full.

`data_asset_key`

(optional) The key of the data asset for which the job is defined.

`glossary_key`

(optional) Unique key of the glossary to which this job applies.

`description`

(optional) Detailed description of the job definition.

`connection_key`

(optional) The key of the default connection resource to be used for harvest, sampling, profiling jobs. This may be overridden in each job instance.

`internal_version`

(optional) Version of the job definition object. Used internally but can be visible to users.

`lifecycle_state`

(optional) Lifecycle state of the job definition.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`time_created`

(optional) The date and time the job definition was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`time_updated`

(optional) The last time that any change was made to the data asset. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created this job definition.

`updated_by_id`

(optional) OCID of the user who updated this job definition.

`uri`

(optional) URI to the job definition instance in the API.

`is_sample_data_extracted`

(optional) Specify if sample data to be extracted as part of this harvest.

`sample_data_size_in_m_bs`

(optional) Specify the sample data size in MB, specified as number of rows, for this metadata harvest.

`time_latest_execution_started`

(optional) Time that the latest job execution started. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_latest_execution_ended`

(optional) Time that the latest job execution ended or null if it hasn't yet completed. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`job_execution_state`

(optional) Status of the latest job execution, such as running, paused, or completed.

Allowed values are: 'CREATED', 'IN_PROGRESS', 'INACTIVE', 'FAILED', 'SUCCEEDED', 'CANCELED', 'SUCCEEDED_WITH_WARNINGS'

`schedule_type`

(optional) Type of job schedule for the latest job executed.

Allowed values are: 'SCHEDULED', 'IMMEDIATE'

`properties`

(optional) A map of maps that contains the properties which are specific to the job type. Each job type definition may define it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most job definitions have required properties within the \"default\" category. Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_JOB_DEFINITION_SUMMARY_T Type

A list of job definition resources. Job definitions define the harvest scope and includes the list of objects to be harvested along with a schedule. The list of objects is usually specified through a combination of object type, regular expressions, or specific names of objects and a sample size for the data harvested.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique key of the job definition resource that is immutable.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of the job definition.

`catalog_id`

(optional) The data catalog's OCID.

`uri`

(optional) URI to the job definition instance in the API.

`job_type`

(optional) Type of the job definition.

Allowed values are: 'HARVEST', 'PROFILING', 'SAMPLING', 'PREVIEW', 'IMPORT', 'EXPORT', 'IMPORT_GLOSSARY', 'EXPORT_GLOSSARY', 'INTERNAL', 'PURGE', 'IMMEDIATE', 'SCHEDULED', 'IMMEDIATE_EXECUTION', 'SCHEDULED_EXECUTION', 'SCHEDULED_EXECUTION_INSTANCE', 'ASYNC_DELETE', 'IMPORT_DATA_ASSET', 'CREATE_SCAN_PROXY', 'ASYNC_EXPORT_GLOSSARY'

`lifecycle_state`

(optional) Lifecycle state of the job definition.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`is_sample_data_extracted`

(optional) Specify if sample data to be extracted as part of this harvest.

`time_created`

(optional) The date and time the job definition was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`connection_key`

(optional) The key of the connection resource used in harvest, sampling, profiling jobs.

`time_latest_execution_started`

(optional) Time that the latest job execution started. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_latest_execution_ended`

(optional) Time that the latest job execution ended or null if it hasn't yet completed. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`job_execution_state`

(optional) Status of the latest job execution, such as running, paused, or completed.

Allowed values are: 'CREATED', 'IN_PROGRESS', 'INACTIVE', 'FAILED', 'SUCCEEDED', 'CANCELED', 'SUCCEEDED_WITH_WARNINGS'

`schedule_type`

(optional) Type of job schedule for the latest job executed.

Allowed values are: 'SCHEDULED', 'IMMEDIATE'

`data_asset_key`

(optional) Unique key of the data asset to which this job applies, if the job involves a data asset.

`glossary_key`

(optional) Unique key of the glossary to which this job applies, if the job involves a glossary.

### DBMS_CLOUD_OCI_DATACATALOG_JOB_DEFINITION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_job_definition_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_JOB_DEFINITION_COLLECTION_T Type

Results of a job definition listing. Job definitions are resources that describe the scope and type of jobs (eg: harvest, profiling, sampling) that are defined by users in the system.

Syntax
```

```

Fields

Field Description

`l_count`

(optional) Total number of items returned.

`items`

(required) Collection of job definitions.

### DBMS_CLOUD_OCI_DATACATALOG_JOB_DEFINITION_PERMISSIONS_SUMMARY_T Type

Permissions object for job definitions.

Syntax
```

```

Fields

Field Description

`job_definition_key`

(optional) The unique key of the parent job definition.

`user_permissions`

(optional) An array of permissions.

### DBMS_CLOUD_OCI_DATACATALOG_JOB_DEFINITION_SCOPE_T Type

Defines the rules or criteria based on which the scope for job definition is circumscribed.

Syntax
```

```

Fields

Field Description

`folder_name`

(optional) Name of the folder or schema for this metadata harvest.

`entity_name`

(optional) Name of the entity for this metadata harvest.

`folder_name_filter`

(optional) Filter rules with regular expression to specify folder names for this metadata harvest.

`entity_name_filter`

(optional) Filter rules with regular expression to specify entity names for this metadata harvest.

`is_sample_data_extracted`

(optional) Specify if sample data to be extracted as part of this harvest.

`sample_data_size_in_m_bs`

(optional) Specify the sample data size in MB, specified as number of rows, for this metadata harvest.

### DBMS_CLOUD_OCI_DATACATALOG_JOB_EXECUTION_T Type

A job execution is a unit of work being executed on behalf of a job.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique key of the job execution resource.

`job_key`

(optional) The unique key of the parent job.

`job_type`

(optional) Type of the job execution.

Allowed values are: 'HARVEST', 'PROFILING', 'SAMPLING', 'PREVIEW', 'IMPORT', 'EXPORT', 'IMPORT_GLOSSARY', 'EXPORT_GLOSSARY', 'INTERNAL', 'PURGE', 'IMMEDIATE', 'SCHEDULED', 'IMMEDIATE_EXECUTION', 'SCHEDULED_EXECUTION', 'SCHEDULED_EXECUTION_INSTANCE', 'ASYNC_DELETE', 'IMPORT_DATA_ASSET', 'CREATE_SCAN_PROXY', 'ASYNC_EXPORT_GLOSSARY'

`sub_type`

(optional) Sub-type of this job execution.

`parent_key`

(optional) The unique key of the parent execution or null if this job execution has no parent.

`schedule_instance_key`

(optional) The unique key of the triggering external scheduler resource or null if this job execution is not externally triggered.

`lifecycle_state`

(optional) Status of the job execution, such as running, paused, or completed.

Allowed values are: 'CREATED', 'IN_PROGRESS', 'INACTIVE', 'FAILED', 'SUCCEEDED', 'CANCELED', 'SUCCEEDED_WITH_WARNINGS'

`time_created`

(optional) The date and time the job execution was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`time_started`

(optional) Time that job execution started. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_ended`

(optional) Time that the job execution ended or null if it hasn't yet completed. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`error_code`

(optional) Error code returned from the job execution or null if job is still running or didn't return an error.

`error_message`

(optional) Error message returned from the job execution or null if job is still running or didn't return an error.

`process_key`

(optional) Process identifier related to the job execution if the job is an external job.

`external_url`

(optional) If the job is an external process, then a URL of the job for accessing this resource and its status.

`event_key`

(optional) An identifier used for log message correlation.

`data_entity_key`

(optional) The key of the associated data entity resource.

`created_by_id`

(optional) OCID of the user who created the job execution.

`updated_by`

(optional) OCID of the user who updated the job execution.

`uri`

(optional) URI to the job execution instance in the API.

`properties`

(optional) A map of maps that contains the execution context properties which are specific to a job execution. Each job execution may define it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most job executions have required properties within the \"default\" category. Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_JOB_EXECUTION_COLLECTION_T Type

Results of a job executions listing. Job executions are execution instances of a scheduled job.

Syntax
```

```

Fields

Field Description

`l_count`

(optional) Total number of items returned.

`items`

(required) Collection of job executions.

### DBMS_CLOUD_OCI_DATACATALOG_JOB_LOG_T Type

Job log details. A job log is an audit log record inserted during the lifecycle of a job execution instance.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique key of the job log that is immutable.

`job_execution_key`

(optional) The unique key of the parent job execution for which the log resource was created.

`created_by_id`

(optional) OCID of the user who created the log record for this job. Usually the executor of the job instance.

`updated_by_id`

(optional) OCID of the user who created the log record for this job. Usually the executor of the job instance.

`time_updated`

(optional) Job log update time. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_created`

(optional) The date and time the job log was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`severity`

(optional) Severity level for this log.

`log_message`

(optional) Message for this job log.

`uri`

(optional) URI to the job log instance in the API.

### DBMS_CLOUD_OCI_DATACATALOG_JOB_LOG_SUMMARY_T Type

A list of job execution logs. A job log is an audit log record inserted during the lifecycle of a job execution instance. There can be one or more logs for an execution instance.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique key of the job log that is immutable.

`job_execution_key`

(optional) The unique key of the parent job execution for which the log resource was created.

`uri`

(optional) URI to the job log instance in the API.

`time_created`

(optional) The date and time the job log was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`severity`

(optional) Severity level for this log.

`log_message`

(optional) Message for this job log.

### DBMS_CLOUD_OCI_DATACATALOG_JOB_LOG_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_job_log_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_JOB_LOG_COLLECTION_T Type

Results of a job logs Listing. A job log is an audit log record inserted during the lifecycle of a job execution instance.

Syntax
```

```

Fields

Field Description

`l_count`

(optional) Total number of items returned.

`items`

(required) Collection of Job logs.

### DBMS_CLOUD_OCI_DATACATALOG_JOB_METRIC_T Type

A set of metrics are collected periodically to assess the state and performance characteristics of the execution instance of a job. The metrics are grouped based on their category and sub categories and aggregated based on their batch information.

Syntax
```

```

Fields

Field Description

`key`

(required) Key of the job metric that is immutable.

`description`

(optional) Detailed description of the metric.

`job_execution_key`

(optional) The unique key of the parent job execution for which the job metric resource is being created.

`time_inserted`

(optional) The time the metric was logged or captured in the system where the job executed. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`category`

(optional) Category of this metric.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`sub_category`

(optional) Sub category of this metric under the category. Used for aggregating values. May be null.

`unit`

(optional) Unit of this metric.

`value`

(optional) Value of this metric.

`batch_key`

(optional) Batch key for grouping, may be null.

`uri`

(optional) URI to the job metric instance in the API.

`time_created`

(optional) The date and time the job metric was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`time_updated`

(optional) The last time that this metric was updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the metric for this job. Usually the executor of the job instance.

`updated_by_id`

(optional) OCID of the user who created the metric for this job. Usually the executor of the job instance.

### DBMS_CLOUD_OCI_DATACATALOG_JOB_METRIC_SUMMARY_T Type

Job metric summary.

Syntax
```

```

Fields

Field Description

`key`

(required) Key of the job metric that is immutable.

`description`

(optional) Detailed description of the metric.

`job_execution_key`

(optional) The unique key of the parent job execution for which the job metric resource was created.

`uri`

(optional) URI to the job metric instance in the API.

`time_created`

(optional) The date and time the job metric was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`time_inserted`

(optional) The time the metric was logged or captured in the system where the job executed. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`category`

(optional) Category of this metric.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`sub_category`

(optional) Sub category of this metric under the category. Used for aggregating values. May be null.

`unit`

(optional) Unit of this metric.

`value`

(optional) Value of this metric.

`batch_key`

(optional) Batch key for grouping, may be null.

### DBMS_CLOUD_OCI_DATACATALOG_JOB_METRIC_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_job_metric_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_JOB_METRIC_COLLECTION_T Type

Results of a job metrics listing. Job metrics are datum about a job execution in key value pairs.

Syntax
```

```

Fields

Field Description

`l_count`

(optional) Total number of items returned.

`items`

(required) Collection of job metrics.

### DBMS_CLOUD_OCI_DATACATALOG_METASTORE_T Type

A Data Catalog Metastore provides a centralized metastore repository for use by other OCI services.

Syntax
```

```

Fields

Field Description

`id`

(required) The metastore's OCID.

`display_name`

(optional) Mutable name of the metastore.

`compartment_id`

(required) OCID of the compartment which holds the metastore.

`time_created`

(optional) Time at which the metastore was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_updated`

(optional) Time at which the metastore was last modified. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`default_managed_table_location`

(required) Location under which managed tables will be created by default. This references Object Storage using an HDFS URI format. Example: oci://bucket@namespace/sub-dir/

`default_external_table_location`

(required) Location under which external tables will be created by default. This references Object Storage using an HDFS URI format. Example: oci://bucket@namespace/sub-dir/

`lifecycle_state`

(optional) The current state of the metastore.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`locks`

(optional) Locks associated with this resource.

### DBMS_CLOUD_OCI_DATACATALOG_METASTORE_SUMMARY_T Type

Summary of a metastore.

Syntax
```

```

Fields

Field Description

`id`

(required) The metastore's OCID.

`display_name`

(optional) Mutable name of the metastore.

`compartment_id`

(required) OCID of the compartment which holds the metastore.

`time_created`

(optional) Time at which the metastore was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_updated`

(optional) Time at which the metastore was last modified. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`lifecycle_state`

(optional) The current state of the metastore.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`locks`

(optional) Locks associated with this resource.

### DBMS_CLOUD_OCI_DATACATALOG_NAMESPACE_T Type

Namespace Definition

Syntax
```

```

Fields

Field Description

`key`

(required) Unique namespace key that is immutable.

`display_name`

(optional) Name of the Namespace

`description`

(optional) Description for the namespace

`is_service_defined`

(optional) If this field is defined by service or by a user

`lifecycle_state`

(optional) The current state of the namespace.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`time_created`

(optional) The date and time the namespace was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`time_updated`

(optional) The last time that any change was made to the namespace. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the namespace.

`updated_by_id`

(optional) OCID of the user who last modified the namespace.

### DBMS_CLOUD_OCI_DATACATALOG_NAMESPACE_SUMMARY_T Type

Summary of a namespace

Syntax
```

```

Fields

Field Description

`key`

(required) Unique namespace key that is immutable.

`display_name`

(optional) Name of the namespace

`description`

(optional) Detailed description of the namespace.

`is_service_defined`

(optional) If this field is defined by service or by a user

`lifecycle_state`

(optional) The current state of the namespace.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`time_created`

(optional) The date and time the namespace was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_DATACATALOG_NAMESPACE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_namespace_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_NAMESPACE_COLLECTION_T Type

Results of a namespaces listing. A namespace is an unique name tied to the first class object of data catalog which will be used to create a custom property

Syntax
```

```

Fields

Field Description

`l_count`

(optional) Total number of items returned.

`items`

(required) Collection of namespace summaries

### DBMS_CLOUD_OCI_DATACATALOG_OBJECT_LINEAGE_T Type

Lineage for an object.

Syntax
```

```

Fields

Field Description

`l_level`

(required) Object level at which the lineage is returned.

`direction`

(required) Direction of the lineage returned.

Allowed values are: 'UPSTREAM', 'BOTH', 'DOWNSTREAM'

`objects`

(optional) Set of objects that are involved in the lineage.

`relationships`

(optional) Set of relationships between the objects in the 'objects' set.

`annotations`

(optional) A map of maps that contains additional information in explanation of the lineage returned. The map keys are categories of information and the values are maps of annotation names to their corresponding values. Every annotation is contained inside a category. Example: `{\"annotations\": { \"category\": { \"key\": \"value\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_OBJECT_LINEAGE_REQUEST_DETAILS_T Type

Details needed by a lineage fetch request.

Syntax
```

```

Fields

Field Description

`l_level`

(optional) Object level at which the lineage is returned.

`direction`

(optional) Direction of the lineage returned.

Allowed values are: 'UPSTREAM', 'BOTH', 'DOWNSTREAM'

`is_intra_lineage`

(optional) Intra-lineages are drill down lineages. This field indicates whether all intra-lineages need to be expanded inline in the lineage returned.

`intra_lineage_object_key`

(optional) Unique object key for which intra-lineage needs to be fetched. Only drill-down lineage corresponding to the object whose object key is passed is returned.

### DBMS_CLOUD_OCI_DATACATALOG_PARSE_CONNECTION_DETAILS_T Type

Parse connections from the connection metadata and Oracle wallet file. An error will be returned if more than one of connectionPayload, walletSecretId or walletSecretName are present in the request.

Syntax
```

```

Fields

Field Description

`connection_detail`

(optional)

`connection_payload`

(optional) The information used to parse the connection from the wallet file payload.

`wallet_secret_id`

(optional) OCID of the OCI Vault secret holding the Oracle wallet to parse.

`wallet_secret_name`

(optional) Name of the OCI Vault secret holding the Oracle wallet to parse.

### DBMS_CLOUD_OCI_DATACATALOG_PATTERN_T Type

A pattern is a data selector or filter which can provide a singular, logical entity view aggregating multiple physical data artifacts for ease of use.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique pattern key that is immutable.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of the pattern.

`catalog_id`

(optional) The data catalog's OCID.

`lifecycle_state`

(optional) The current state of the pattern.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`time_created`

(optional) The date and time the pattern was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`time_updated`

(optional) The last time that any change was made to the pattern. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the pattern.

`updated_by_id`

(optional) OCID of the user who last modified the pattern.

`expression`

(optional) Input string which drives the selection process, allowing for fine-grained control using qualifiers. Refer to the user documentation for details of the format and examples. A pattern cannot include both a prefix and an expression.

`file_path_prefix`

(optional) Input string which drives the selection process. Refer to the user documentation for details of the format and examples. A pattern cannot include both a prefix and an expression.

`check_file_path_list`

(optional) List of file paths against which the pattern can be tried, as a check. This documents, for reference purposes, some example objects a pattern is meant to work with. If isEnableCheckFailureLimit is set to true, this will be run as a validation during the request, such that if the check fails the request fails. If isEnableCheckFailureLimit instead is set to (the default) false, a pattern will still be created or updated even if the check fails, with a lifecycleState of FAILED.

`is_enable_check_failure_limit`

(optional) Indicates whether the pattern check, against the checkFilePathList, will fail the request if the count of UNMATCHED files is above the checkFailureLimit.

`check_failure_limit`

(optional) The maximum number of UNMATCHED files, in checkFilePathList, above which the check fails. Optional, if checkFilePathList is provided - but if isEnableCheckFailureLimit is set to true it is required.

`properties`

(optional) A map of maps that contains the properties which are specific to the pattern type. Each pattern type definition defines it's set of required and optional properties. Example: `{\"properties\": { \"default\": { \"tbd\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_PATTERN_COLLECTION_T Type

Results of a pattern listing. Patterns are used in entity harvesting.

Syntax
```

```

Fields

Field Description

`l_count`

(optional) Total number of items returned.

`items`

(required) Collection of pattern summaries.

### DBMS_CLOUD_OCI_DATACATALOG_PROCESS_RECOMMENDATION_DETAILS_T Type

Details of recommendation to be processed.

Syntax
```

```

Fields

Field Description

`recommendation_key`

(required) Unique identifier of the recommendation.

`recommendation_status`

(required) The status of a recommendation.

Allowed values are: 'ACCEPTED', 'REJECTED', 'INFERRED'

`properties`

(optional) A map of maps that contains additional properties which are specific to the associated objects. Each associated object defines it's set of required and optional properties. Example: `{ \"DataEntity\": { \"parentId\": \"entityId\" }, \"Term\": { \"parentId\": \"glossaryId\" } }`

### DBMS_CLOUD_OCI_DATACATALOG_PROPERTY_DEFINITION_T Type

Details of a single type property.

Syntax
```

```

Fields

Field Description

`name`

(optional) Name of the property.

`l_type`

(optional) The properties value type.

`is_required`

(optional) Whether instances of the type are required to set this property.

`is_updatable`

(optional) Indicates if this property value can be updated.

### DBMS_CLOUD_OCI_DATACATALOG_RECOMMENDATION_DETAILS_T Type

Details of a recommendation.

Syntax
```

```

Fields

Field Description

`recommendation_key`

(required) Unique identifier of the recommendation.

`recommendation_type`

(required) Type of recommendation.

Allowed values are: 'LINK_GLOSSARY_TERM'

`recommendation_status`

(required) Status of a recommendation.

Allowed values are: 'ACCEPTED', 'REJECTED', 'INFERRED'

`confidence_score`

(optional) Level of confidence, on a scale between 0 and 1, that the recommendation is applicable.

`source_object_key`

(optional) Unique identifier of the source object; the one for which a recommendation is made.

`source_object_name`

(optional) Name of the source object; the one for which a recommendation is made.

`source_object_type`

(optional) Type of the source object; the one for which a recommendation is made.

Allowed values are: 'DATA_ENTITY', 'ATTRIBUTE', 'TERM', 'CATEGORY'

`target_object_key`

(optional) Unique identifier of the target object; the one which has been recommended.

`target_object_name`

(optional) Name of the target object; the one which has been recommended.

`target_object_type`

(optional) Type of the target object; the one which has been recommended.

Allowed values are: 'DATA_ENTITY', 'ATTRIBUTE', 'TERM', 'CATEGORY'

`properties`

(optional) A map of maps that contains additional properties which are specific to the associated objects. Each associated object defines it's set of required and optional properties. Example: `{ \"DataEntity\": { \"parentId\": \"entityId\" }, \"Term\": { \"parentId\": \"glossaryId\" } }`

### DBMS_CLOUD_OCI_DATACATALOG_RECOMMENDATION_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_recommendation_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_RECOMMENDATION_COLLECTION_T Type

Results of a get recommendation.

Syntax
```

```

Fields

Field Description

`l_count`

(optional) Total number of items returned.

`items`

(required) Collection of recommendations.

### DBMS_CLOUD_OCI_DATACATALOG_REMOVE_RESOURCE_LOCK_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the lock.

Allowed values are: 'FULL', 'DELETE'

`related_resource_id`

(optional) The id of the resource that is locking this resource. Indicates that deleting this resource will remove the lock.

`message`

(optional) A message added by the creator of the lock. This is typically used to give an indication of why the resource is locked.

`time_created`

(optional) When the lock was created.

### DBMS_CLOUD_OCI_DATACATALOG_RULE_ATTRIBUTE_T Type

Object that defines a usage of an attribute in the context of a rule. Example: For a UNIQUEKEY rule, declares the attribute in a table whose value must be unique.

Syntax
```

```

Fields

Field Description

`key`

(required) Immutable unique key of the attribute.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`position`

(optional) Position of the attribute in the record definition.

### DBMS_CLOUD_OCI_DATACATALOG_RULE_ATTRIBUTE_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_rule_attribute_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_RULE_SUMMARY_T Type

A list of rule resources. One or more rules can be defined for a data entity. Each rule can be defined on one or more attributes of the data entity.

Syntax
```

```

Fields

Field Description

`key`

(required) Immutable unique key of a rule.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of a rule.

`rule_type`

(optional) Type of a rule.

Allowed values are: 'PRIMARYKEY', 'FOREIGNKEY', 'UNIQUEKEY'

`external_key`

(optional) External URI that can be used to reference the object. Format will differ based on the type of object.

`attributes`

(optional) Attributes associated with a rule. A UNIQUEKEY rule would contain (at least) one attribute, for the local table column(s) on which uniqueness is defined.

`referenced_folder_key`

(optional) Folder key that represents the referenced folder, applicable only when rule type FOREIGNKEY.

`referenced_folder_name`

(optional) Folder name that represents the referenced folder, applicable only when rule type FOREIGNKEY.

`referenced_entity_key`

(optional) Entity key that represents the referenced entity, applicable only when rule type is FOREIGNKEY.

`referenced_entity_name`

(optional) Entity name that represents the referenced entity, applicable only when rule type is FOREIGNKEY.

`referenced_rule_key`

(optional) Rule key that represents the referenced rule, applicable only when rule type is FOREIGNKEY.

`referenced_rule_name`

(optional) Rule name that represents the referenced rule, applicable only when rule type is FOREIGNKEY.

`referenced_attributes`

(optional) Attributes associated with referenced rule, applicable only when rule type is FOREIGNKEY. A FOREIGNKEY rule would contain (at least) one attribute, for the local table column(s), and (at least) one referencedAttribute for referenced table column(s).

`origin_type`

(optional) Origin type of the rule.

Allowed values are: 'SOURCE', 'USER', 'PROFILING'

`uri`

(optional) URI to the rule instance in the API.

`time_created`

(optional) The date and time the rule was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`lifecycle_state`

(optional) State of the rule.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

### DBMS_CLOUD_OCI_DATACATALOG_RULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_rule_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_RULE_COLLECTION_T Type

Results of an rule listing. Rules describe an item of data with name and ruletype.

Syntax
```

```

Fields

Field Description

`l_count`

(optional) Total number of items returned.

`items`

(required) Collection of rules.

### DBMS_CLOUD_OCI_DATACATALOG_FACETED_SEARCH_SORT_REQUEST_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_faceted_search_sort_request_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_SEARCH_CRITERIA_T Type

Search Query object that allows complex search predicates that cannot be expressed through simple query params.

Syntax
```

```

Fields

Field Description

`query`

(optional) Search query dsl that defines the query components including fields and predicates.

`faceted_query`

(optional) Query string that a dataObject is to be searched with. Used in the faceted query request

`dimensions`

(optional) List of properties of dataObjects that needs to aggregated on for facets.

`sort`

(optional) Array of objects having details about sort field and order.

`filters`

(optional)

### DBMS_CLOUD_OCI_DATACATALOG_SEARCH_TAG_SUMMARY_T Type

Represents the association of an object to a term. Returned as part of search result.

Syntax
```

```

Fields

Field Description

`key`

(optional) Unique tag key that is immutable.

`display_name`

(required) Name of the tag that matches the term name.

### DBMS_CLOUD_OCI_DATACATALOG_SEARCH_TERM_SUMMARY_T Type

Summary of a term associated with an object. This is a brief summary returned as part of the search result.

Syntax
```

```

Fields

Field Description

`key`

(optional) Unique term key that is immutable.

`display_name`

(required) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`glossary_key`

(optional) Unique id of the parent glossary.

`glossary_name`

(optional) Name of the parent glossary.

`parent_term_key`

(optional) This terms parent term key. Will be null if the term has no parent term.

`parent_term_name`

(optional) Name of the parent term key. Will be null if the term has no parent term.

### DBMS_CLOUD_OCI_DATACATALOG_SEARCH_TAG_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_search_tag_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_SEARCH_TERM_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_search_term_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_FACETED_SEARCH_CUSTOM_PROPERTY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_faceted_search_custom_property_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_SEARCH_RESULT_T Type

The search result object is the definition of an element that is returned as part of search. It contains basic information about the object such as key, name and description. The search result also contains the list of tags for each object along with other contextual information like the data asset root, folder, or entity parents.

Syntax
```

```

Fields

Field Description

`key`

(optional) Unique key of the object returned as part of the search result.

`name`

(optional) Name of the object.

`description`

(optional) Detailed description of the object.

`time_created`

(optional) The date and time the result object was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`time_updated`

(optional) The date and time the result object was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`tag_summary`

(optional) Array of the tags associated with this object.

`term_summary`

(optional) Array of the terms associated with this object.

`type_name`

(optional) Name of the object type.

`external_type_name`

(optional) Name of the external object type in the host data asset. For example, column, field, table, view, or file.

`external_data_type`

(optional) Data type of the object if the object is an attribute. Null otherwise.

`data_asset_key`

(optional) Unique key of the data asset that is the root parent of this object.

`data_asset_type`

(optional) Type name of the data asset. For example, Oracle, MySQL or Oracle Object Storage.

`data_asset_name`

(optional) Name of the data asset that is the root parent of this object.

`folder_key`

(optional) Unique key of the folder object if this object is a sub folder, entity, or attribute.

`folder_type`

(optional) Type name of the folder. For example, schema, directory, or topic.

`folder_name`

(optional) Name of the parent folder object if this object is a sub folder, entity, or attribute.

`entitykey`

(optional) Unique key of the entity object if this object is an attribute.

`entity_type`

(optional) Type name of the entity. For example, table, view, external table, file, or object.

`entity_name`

(optional) Name of the parent entity object if this object is an attribute.

`glossary_key`

(optional) Unique id of the parent glossary.

`glossary_name`

(optional) Name of the parent glossary if this object is a term.

`parent_term_key`

(optional) This terms parent term key. Will be null if the term has no parent term.

`parent_term_name`

(optional) Name of the parent term. Will be null if the term has no parent term.

`created_by_id`

(optional) OCID of the user who created the resource.

`updated_by_id`

(optional) OCID of the user who updated the resource.

`path`

(optional) Absolute path of this resource, which could be a term, folder, entity etc, usually resolvable to this resource through a namespace hierarchy.

`business_name`

(optional) Optional user friendly business name of the data object. If set, this supplements the harvested display name of the object.

`lifecycle_state`

(optional) The current state of the data object.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`attribute_type`

(optional) Type name of the attribute. For example - complex, primitive, or array.

`expression`

(optional) Expression for logical entities against which names of dataObjects will be matched.

`custom_properties`

(optional) Custom properties defined by users.

`properties`

(optional) A map of maps that contains the properties which are specific to the element type in the search result. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most element types have required properties within the \"default\" category. Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_SEARCH_RESULT_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_search_result_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_FACETED_SEARCH_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_faceted_search_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_SEARCH_RESULT_COLLECTION_T Type

The list of search result items matching the criteria returned from the search operation. Search errors and messages, if any , will be part of the standard error response.

Syntax
```

```

Fields

Field Description

`l_count`

(optional) Total number of items returned.

`items`

(optional) Search result set.

`query`

(optional) String that data objects are to be searched with.

`faceted_search_aggregation`

(optional) Aggregations/facets on properties of data objects.

`sortable_fields`

(optional) A list of fields or properties used in the sorting of a search result.

### DBMS_CLOUD_OCI_DATACATALOG_SUGGEST_LIST_ITEM_T Type

Details of a potential match returned from the suggest operation for the given input text. by the limit parameter.

Syntax
```

```

Fields

Field Description

`suggestion`

(optional) Potential string match. Matching is based on the frequency of usage within the catalog.

`object_count`

(optional) The number of objects which contain this suggestion.

### DBMS_CLOUD_OCI_DATACATALOG_SUGGEST_LIST_ITEM_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_suggest_list_item_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_SUGGEST_RESULTS_T Type

The list of potential matches returned from the suggest operation for the given input text. The size of the list will be determined by the limit parameter.

Syntax
```

```

Fields

Field Description

`total_count`

(required) Total number of items returned.

`search_latency_in_ms`

(optional) Time taken to compute the result, in milliseconds.

`input_text`

(required) Input string for which the potential matches are computed.

`items`

(optional) List of suggestions.

### DBMS_CLOUD_OCI_DATACATALOG_TERM_ASSOCIATED_OBJECT_T Type

Projection of an object that is tagged to a term.

Syntax
```

```

Fields

Field Description

`key`

(required) Immutable key used to uniquely identify the associated object.

`name`

(optional) Name of the associated object.

`uri`

(optional) URI of the associated object within the data catalog API.

### DBMS_CLOUD_OCI_DATACATALOG_TERM_ASSOCIATED_OBJECT_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_term_associated_object_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_TERM_T Type

Full term definition. A defined business term in a business glossary. As well as a term definition, simple format rules for attributes mapping to the term (for example, the expected data type and length restrictions) may be stated at the term level. Nesting of terms to support a hierarchy is supported by default.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique term key that is immutable.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of the term.

`glossary_key`

(optional) Unique id of the parent glossary.

`parent_term_key`

(optional) This terms parent term key. Will be null if the term has no parent term.

`is_allowed_to_have_child_terms`

(optional) Indicates whether a term may contain child terms.

`path`

(optional) Absolute path of the term.

`lifecycle_state`

(optional) The current state of the term.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`time_created`

(optional) The date and time the term was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`time_updated`

(optional) The last time that any change was made to the term. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`created_by_id`

(optional) OCID of the user who created the term.

`updated_by_id`

(optional) OCID of the user who modified the term.

`owner`

(optional) OCID of the user who is the owner of this business terminology.

`workflow_status`

(optional) Status of the approval process workflow for this business term in the glossary.

Allowed values are: 'NEW', 'APPROVED', 'UNDER_REVIEW', 'ESCALATED'

`uri`

(optional) URI to the term instance in the API.

`associated_object_count`

(optional) The number of objects tagged with this term

`associated_objects`

(optional) Array of objects associated to a term.

`custom_property_members`

(optional) The list of customized properties along with the values for this object

### DBMS_CLOUD_OCI_DATACATALOG_TERM_SUMMARY_T Type

Summary of a term. A defined business term in a business glossary. As well as a term definition, simple format rules for attributes mapping to the term (for example, the expected data type and length restrictions) may be stated at the term level.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique term key that is immutable.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of the term.

`glossary_key`

(optional) Unique id of the parent glossary.

`uri`

(optional) URI to the term instance in the API.

`parent_term_key`

(optional) This terms parent term key. Will be null if the term has no parent term.

`is_allowed_to_have_child_terms`

(optional) Indicates whether a term may contain child terms.

`path`

(optional) Absolute path of the term.

`time_created`

(optional) The date and time the term was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`workflow_status`

(optional) Status of the approval process workflow for this business term in the glossary.

Allowed values are: 'NEW', 'APPROVED', 'UNDER_REVIEW', 'ESCALATED'

`associated_object_count`

(optional) The number of objects tagged with this term.

`lifecycle_state`

(optional) State of the term.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

### DBMS_CLOUD_OCI_DATACATALOG_TERM_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_term_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_TERM_COLLECTION_T Type

Results of a terms listing. Terms are defined in business glossary and are used in tagging catalog objects.

Syntax
```

```

Fields

Field Description

`l_count`

(optional) Total number of items returned.

`items`

(required) Collection of terms.

### DBMS_CLOUD_OCI_DATACATALOG_TERM_RELATIONSHIP_T Type

Full term relationship definition. Business term relationship between two terms in a business glossary.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique term relationship key that is immutable.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.This is the same as relationshipType for termRelationship

`description`

(optional) Detailed description of the term relationship usually defined at the time of creation.

`related_term_key`

(optional) Unique id of the related term.

`related_term_display_name`

(optional) Name of the related term.

`related_term_description`

(optional) Description of the related term.

`related_term_path`

(optional) Full path of the related term.

`related_term_glossary_key`

(optional) Glossary key of the related term.

`uri`

(optional) URI to the term relationship instance in the API.

`parent_term_key`

(optional) This relationships parent term key.

`parent_term_display_name`

(optional) Name of the parent term.

`parent_term_description`

(optional) Description of the parent term.

`parent_term_path`

(optional) Full path of the parent term.

`parent_term_glossary_key`

(optional) Glossary key of the parent term.

`time_created`

(optional) The date and time the term relationship was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`lifecycle_state`

(optional) State of the term relationship.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

### DBMS_CLOUD_OCI_DATACATALOG_TERM_RELATIONSHIP_SUMMARY_T Type

Summary of a term relationship. Business term relationship between two terms in a business glossary.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique term relationship key that is immutable.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.This is the same as relationshipType for termRelationship

`description`

(optional) Detailed description of the term relationship usually defined at the time of creation.

`related_term_key`

(optional) Unique id of the related term.

`related_term_display_name`

(optional) Name of the related term.

`related_term_description`

(optional) Description of the related term.

`related_term_path`

(optional) Full path of the related term.

`related_term_glossary_key`

(optional) Glossary key of the related term.

`uri`

(optional) URI to the term relationship instance in the API.

`parent_term_key`

(optional) This relationships parent term key.

`parent_term_display_name`

(optional) Name of the parent term.

`parent_term_description`

(optional) Description of the parent term.

`parent_term_path`

(optional) Full path of the parent term.

`parent_term_glossary_key`

(optional) Glossary key of the parent term.

`time_created`

(optional) The date and time the term relationship was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2019-03-25T21:10:29.600Z`

`lifecycle_state`

(optional) State of the term relationship.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

### DBMS_CLOUD_OCI_DATACATALOG_TERM_RELATIONSHIP_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_term_relationship_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_TERM_RELATIONSHIP_COLLECTION_T Type

Results of a terms relationship listing. Term relationships are associations between two terms in business glossary.

Syntax
```

```

Fields

Field Description

`l_count`

(optional) Total number of items returned.

`items`

(required) Collection of term relationships.

### DBMS_CLOUD_OCI_DATACATALOG_TYPE_T Type

Full data catalog type definition. Fully defines a type of the data catalog. All types are statically defined in the system and are immutable. It isn't possible to create new types or update existing types via the API.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique type key that is immutable.

`name`

(optional) The immutable name of the type.

`description`

(optional) Detailed description of the type.

`catalog_id`

(optional) The data catalog's OCID.

`properties`

(optional) A map of arrays which defines the type specific properties, both required and optional. The map keys are category names and the values are arrays contiaing all property details. Every property is contained inside of a category. Most types have required properties within the \"default\" category. Example: `{ \"properties\": { \"default\": { \"attributes:\": [ { \"name\": \"host\", \"type\": \"string\", \"isRequired\": true, \"isUpdatable\": false }, ... ] } } }`

`lifecycle_state`

(optional) The current state of the type.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`is_internal`

(optional) Indicates whether the type is internal, making it unavailable for use by metadata elements.

`is_tag`

(optional) Indicates whether the type can be used for tagging metadata elements.

`is_approved`

(optional) Indicates whether the type is approved for use as a classifying object.

`type_category`

(optional) Indicates the category this type belongs to. For instance, data assets, connections.

`external_type_name`

(optional) Mapping type equivalence in the external system.

`uri`

(optional) URI to the type instance in the API.

`custom_properties`

(optional) Custom properties associated with this Type.

`parent_type_key`

(optional) Unique key of the parent type.

`parent_type_name`

(optional) Name of the parent type.

### DBMS_CLOUD_OCI_DATACATALOG_TYPE_SUMMARY_T Type

Summary data catalog type information. All types are statically defined in the system and are immutable. It isn't possible to create new types or update existing types via the API.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique type key that is immutable.

`name`

(optional) The immutable name of the type.

`description`

(optional) Detailed description of the type.

`catalog_id`

(optional) The data catalog's OCID.

`type_category`

(optional) Indicates the category this type belongs to. For instance, data assets, connections.

`uri`

(optional) URI to the type instance in the API.

`lifecycle_state`

(optional) State of the folder.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'MOVING'

`parent_type_key`

(optional) Unique key of the parent type.

`parent_type_name`

(optional) Name of the parent type.

### DBMS_CLOUD_OCI_DATACATALOG_TYPE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_type_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_TYPE_COLLECTION_T Type

Results of a types listing. Types define the basic type of catalog objects and are immutable.

Syntax
```

```

Fields

Field Description

`l_count`

(optional) Total number of items returned.

`items`

(required) Collection of types.

### DBMS_CLOUD_OCI_DATACATALOG_TYPE_CUSTOM_PROPERTY_DETAILS_T Type

Array of custom property IDs for which we have to associate the custom property to the type

Syntax
```

```

Fields

Field Description

`custom_property_ids`

(optional) array of custom property Ids

`is_event_enabled`

(optional) If an OCI Event will be emitted when the custom property is modified.

### DBMS_CLOUD_OCI_DATACATALOG_UPDATE_ATTRIBUTE_DETAILS_T Type

Properties used in attribute update operations.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`business_name`

(optional) Optional user friendly business name of the attribute. If set, this supplements the harvested display name of the object.

`description`

(optional) Detailed description of the attribute.

`external_data_type`

(optional) Data type of the attribute as defined in the external system.

`is_incremental_data`

(optional) Property that identifies if this attribute can be used as a watermark to extract incremental data.

`is_nullable`

(optional) Property that identifies if this attribute can be assigned nullable values.

`length`

(optional) Max allowed length of the attribute value.

`position`

(optional) Position of the attribute in the record definition.

`precision`

(optional) Precision of the attribute value usually applies to float data type.

`scale`

(optional) Scale of the attribute value usually applies to float data type.

`time_external`

(optional) Last modified timestamp of this object in the external system.

`min_collection_count`

(optional) The minimum count for the number of instances of a given type stored in this collection type attribute,applicable if this attribute is a complex type.

`max_collection_count`

(optional) The maximum count for the number of instances of a given type stored in this collection type attribute,applicable if this attribute is a complex type. For type specifications in systems that specify only \"capacity\" without upper or lower bound , this property can also be used to just mean \"capacity\". Some examples are Varray size in Oracle , Occurs Clause in Cobol , capacity in XmlSchemaObjectCollection , maxOccurs in Xml , maxItems in Json

`external_datatype_entity_key`

(optional) External entity key that represents the datatype of this attribute , applicable if this attribute is a complex type.

`external_parent_attribute_key`

(optional) External attribute key that represents the parent attribute of this attribute , applicable if the parent attribute is of complex type.

`custom_property_members`

(optional) The list of customized properties along with the values for this object

`properties`

(optional) A map of maps that contains the properties which are specific to the attribute type. Each attribute type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most attributes have required properties within the \"default\" category. To determine the set of required and optional properties for an Attribute type, a query can be done on '/types?type=attribute' which returns a collection of all attribute types. The appropriate attribute type, which will include definitions of all of it's properties, can be identified from this collection. Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_UPDATE_CATALOG_DETAILS_T Type

The information to be updated for catalog resource.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Data catalog identifier.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DATACATALOG_UPDATE_CATALOG_PRIVATE_ENDPOINT_DETAILS_T Type

Information about the modified private endpoint resource

Syntax
```

```

Fields

Field Description

`dns_zones`

(optional) List of DNS zones to be used by the data assets to be harvested. Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) Display name of the private endpoint resource.

### DBMS_CLOUD_OCI_DATACATALOG_UPDATE_CONNECTION_DETAILS_T Type

Properties used in connection update operations.

Syntax
```

```

Fields

Field Description

`description`

(optional) A description of the connection.

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`custom_property_members`

(optional) The list of customized properties along with the values for this object

`properties`

(optional) A map of maps that contains the properties which are specific to the connection type. Each connection type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most connections have required properties within the \"default\" category. To determine the set of optional and required properties for a connection type, a query can be done on '/types?type=connection' that returns a collection of all connection types. The appropriate connection type, which will include definitions of all of it's properties, can be identified from this collection. Example: `{\"properties\": { \"default\": { \"username\": \"user1\"}}}`

`enc_properties`

(optional) A map of maps that contains the encrypted values for sensitive properties which are specific to the connection type. Each connection type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most connections have required properties within the \"default\" category. To determine the set of optional and required properties for a connection type, a query can be done on '/types?type=connection' that returns a collection of all connection types. The appropriate connection type, which will include definitions of all of it's properties, can be identified from this collection. Example: `{\"encProperties\": { \"default\": { \"password\": \"example-password\"}}}`

`is_default`

(optional) Indicates whether this connection is the default connection.

### DBMS_CLOUD_OCI_DATACATALOG_UPDATE_CUSTOM_PROPERTY_DETAILS_T Type

Properties used in custom atrribute update operations.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of the data asset.

`is_sortable`

(optional) If this field allows to sort from UI

`is_filterable`

(optional) If this field allows to filter or create facets from UI

`is_multi_valued`

(optional) If this field allows multiple values to be set

`is_hidden`

(optional) If this field is a hidden field

`is_editable`

(optional) If this field is a editable field

`is_shown_in_list`

(optional) If this field is displayed in a list view of applicable objects.

`is_hidden_in_search`

(optional) If this field is allowed to pop in search results

`is_event_enabled`

(optional) If an OCI Event will be emitted when the custom property is modified.

`allowed_values`

(optional) Allowed values for the custom property if any

`properties`

(optional) A map of maps that contains the properties which are specific to the asset type. Each data asset type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most data assets have required properties within the \"default\" category. Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_UPDATE_DATA_ASSET_DETAILS_T Type

Properties used in data asset update operations.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of the data asset.

`custom_property_members`

(optional) The list of customized properties along with the values for this object

`properties`

(optional) A map of maps that contains the properties which are specific to the asset type. Each data asset type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most data assets have required properties within the \"default\" category. Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_UPDATE_ENTITY_DETAILS_T Type

Properties used in entity update operations.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`business_name`

(optional) Optional user friendly business name of the data entity. If set, this supplements the harvested display name of the object.

`description`

(optional) Detailed description of a data entity.

`time_external`

(optional) Last modified timestamp of the object in the external system.

`is_logical`

(optional) Property to indicate if the object is a physical materialized object or virtual. For example, View.

`is_partition`

(optional) Property to indicate if the object is a sub object of a parent physical object.

`folder_key`

(optional) Key of the associated folder.

`pattern_key`

(optional) Key of the associated pattern if this is a logical entity.

`realized_expression`

(optional) The expression realized after resolving qualifiers . Used in deriving this logical entity

`harvest_status`

(optional) Status of the object as updated by the harvest process. When an entity object is created, it's harvest status will indicate if the entity's metadata has been fully harvested or not. The harvest process can perform shallow harvesting to allow users to browse the metadata and can on-demand deep harvest on any object This requires a harvest status indicator for catalog objects.

Allowed values are: 'COMPLETE', 'ERROR', 'IN_PROGRESS', 'DEFERRED'

`last_job_key`

(optional) Key of the last harvest process to update this object.

`custom_property_members`

(optional) The list of customized properties along with the values for this object

`properties`

(optional) A map of maps that contains the properties which are specific to the entity type. Each entity type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most entities have required properties within the \"default\" category. To determine the set of required and optional properties for an entity type, a query can be done on '/types?type=dataEntity' that returns a collection of all entity types. The appropriate entity type, which includes definitions of all of it's properties, can be identified from this collection. Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_UPDATE_FOLDER_DETAILS_T Type

Properties used in folder update operations.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`business_name`

(optional) Optional user friendly business name of the folder. If set, this supplements the harvested display name of the object.

`description`

(optional) Detailed description of a folder.

`parent_folder_key`

(optional) The key of the containing folder.

`custom_property_members`

(optional) The list of customized properties along with the values for this object

`properties`

(optional) A map of maps that contains the properties which are specific to the folder type. Each folder type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most folders have required properties within the \"default\" category. To determine the set of optional and required properties for a folder type, a query can be done on '/types?type=folder' that returns a collection of all folder types. The appropriate folder type, which includes definitions of all of it's properties, can be identified from this collection. Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`

`time_external`

(optional) Last modified timestamp of this object in the external system.

`harvest_status`

(optional) Harvest status of the folder.

Allowed values are: 'COMPLETE', 'ERROR', 'IN_PROGRESS', 'DEFERRED'

`last_job_key`

(optional) The key of the last harvest process to update the metadata of this object.

### DBMS_CLOUD_OCI_DATACATALOG_UPDATE_GLOSSARY_DETAILS_T Type

Properties used in glossary update operations.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of the glossary.

`owner`

(optional) OCID of the user who is the owner of the glossary.

`workflow_status`

(optional) Status of the approval process workflow for this business glossary.

Allowed values are: 'NEW', 'APPROVED', 'UNDER_REVIEW', 'ESCALATED'

`custom_property_members`

(optional) The list of customized properties along with the values for this object

### DBMS_CLOUD_OCI_DATACATALOG_UPDATE_JOB_DEFINITION_DETAILS_T Type

Update information for a job definition resource.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`is_incremental`

(optional) Specifies if the job definition is incremental or full.

`data_asset_key`

(optional) The key of the data asset for which the job is defined.

`glossary_key`

(optional) Unique key of the glossary to which this job applies.

`description`

(optional) Detailed description of the job definition.

`connection_key`

(optional) The key of the connection resource to be used for harvest, sampling, profiling jobs.

`is_sample_data_extracted`

(optional) Specify if sample data to be extracted as part of this harvest.

`sample_data_size_in_m_bs`

(optional) Specify the sample data size in MB, specified as number of rows, for this metadata harvest.

`properties`

(optional) A map of maps that contains the properties which are specific to the job type. Each job type definition may define it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most job definitions have required properties within the \"default\" category. Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_UPDATE_JOB_DETAILS_T Type

Job properties that can be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of the job.

`schedule_cron_expression`

(optional) Interval on which the job will be run. Value is specified as a cron-supported time specification \"nickname\". The following subset of those is supported: @monthly, @weekly, @daily, @hourly. For metastore sync, an additional option @default is supported, which will schedule jobs at a more granular frequency.

`time_schedule_begin`

(optional) Date that the schedule should be operational. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_schedule_end`

(optional) Date that the schedule should end from being operational. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`connection_key`

(optional) The key of the connection resource that is used for the harvest by this job.

### DBMS_CLOUD_OCI_DATACATALOG_UPDATE_METASTORE_DETAILS_T Type

Information to be updated for an existing metastore.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Mutable name of the metastore.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DATACATALOG_UPDATE_NAMESPACE_DETAILS_T Type

Properties used in namespace update operations.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of the namespace.

`is_service_defined`

(optional) If this field is defined by service or by a user

### DBMS_CLOUD_OCI_DATACATALOG_UPDATE_PATTERN_DETAILS_T Type

Properties used in pattern update operations.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of the Pattern.

`expression`

(optional) Input string which drives the selection process, allowing for fine-grained control using qualifiers. Refer to the user documentation for details of the format and examples. A pattern cannot include both a prefix and an expression.

`file_path_prefix`

(optional) Input string which drives the selection process. Refer to the user documentation for details of the format and examples. A pattern cannot include both a prefix and an expression.

`check_file_path_list`

(optional) List of file paths against which the pattern can be tried, as a check. This documents, for reference purposes, some example objects a pattern is meant to work with. If isEnableCheckFailureLimit is set to true, this will be run as a validation during the request, such that if the check fails the request fails. If isEnableCheckFailureLimit instead is set to (the default) false, a pattern will still be created or updated even if the check fails, with a lifecycleState of FAILED.

`is_enable_check_failure_limit`

(optional) Indicates whether the pattern check, against the checkFilePathList, will fail the request if the count of UNMATCHED files is above the checkFailureLimit.

`check_failure_limit`

(optional) The maximum number of UNMATCHED files, in checkFilePathList, above which the check fails. Optional, if checkFilePathList is provided - but if isEnableCheckFailureLimit is set to true it is required.

`properties`

(optional) A map of maps that contains the properties which are specific to the pattern type. Each pattern type definition defines it's set of required and optional properties. Example: `{\"properties\": { \"default\": { \"tbd\"}}}`

### DBMS_CLOUD_OCI_DATACATALOG_UPDATE_TERM_DETAILS_T Type

Properties used in term update operations.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Detailed description of the term.

`parent_term_key`

(optional) The parent key of the term. In the case of a root-level category only, the term would have no parent and this should be left unset.

`owner`

(optional) OCID of the user who is the owner of this business terminology.

`workflow_status`

(optional) Status of the approval process workflow for this business term in the glossary

Allowed values are: 'NEW', 'APPROVED', 'UNDER_REVIEW', 'ESCALATED'

`custom_property_members`

(optional) The list of customized properties along with the values for this object

### DBMS_CLOUD_OCI_DATACATALOG_UPDATE_TERM_RELATIONSHIP_DETAILS_T Type

Properties used in term relationship update operations.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name. Is changeable. The combination of 'displayName' and 'parentTermKey' must be unique. Avoid entering confidential information. This is the same as 'relationshipType' for 'termRelationship'.

`description`

(optional) Detailed description of the term relationship usually defined at the time of creation.

### DBMS_CLOUD_OCI_DATACATALOG_UPLOAD_CREDENTIALS_DETAILS_T Type

Upload credential file and connection metadata.

Syntax
```

```

Fields

Field Description

`connection_detail`

(optional)

`credential_payload`

(required) Information used in updating connection credentials.

### DBMS_CLOUD_OCI_DATACATALOG_VALIDATE_CONNECTION_DETAILS_T Type

Validate connection from the connection metadata or oracle wallet file.

Syntax
```

```

Fields

Field Description

`connection_detail`

(optional)

`connection_payload`

(optional) The information used to validate the connection.

### DBMS_CLOUD_OCI_DATACATALOG_VALIDATE_CONNECTION_RESULT_T Type

Details regarding the validation of a connection resource.

Syntax
```

```

Fields

Field Description

`message`

(optional) The message from the connection validation.

`status`

(required) The status returned from the connection validation.

Allowed values are: 'SUCCEEDED', 'FAILED'

### DBMS_CLOUD_OCI_DATACATALOG_VALIDATE_PATTERN_DETAILS_T Type

Validate pattern using the expression and file list.

Syntax
```

```

Fields

Field Description

`expression`

(optional) Input string which drives the selection process, allowing for fine-grained control using qualifiers. Refer to the user documentation for details of the format and examples. A pattern cannot include both a prefix and an expression.

`file_path_prefix`

(optional) Input string which drives the selection process. Refer to the user documentation for details of the format and examples. A pattern cannot include both a prefix and an expression.

`check_file_path_list`

(optional) List of file paths against which the pattern can be tried, as a check. This documents, for reference purposes, some example objects a pattern is meant to work with. If provided with the request,this overrides the list which already exists as part of the pattern, if any.

`check_failure_limit`

(optional) The maximum number of UNMATCHED files, in checkFilePathList, above which the check fails. Optional, if checkFilePathList is provided. If provided with the request, this overrides the value which already exists as part of the pattern, if any.

### DBMS_CLOUD_OCI_DATACATALOG_DERIVED_LOGICAL_ENTITIES_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_derived_logical_entities_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_VALIDATE_PATTERN_RESULT_T Type

Details regarding the validation of a pattern resource.

Syntax
```

```

Fields

Field Description

`message`

(optional) The message from the pattern validation.

`status`

(required) The status returned from the pattern validation.

`expression`

(optional) The expression used in the pattern validation.

`file_path_prefix`

(optional) The prefix used in the pattern validation.

`derived_logical_entities`

(optional) Collection of logical entities derived from the pattern, as applied to a list of file paths.

### DBMS_CLOUD_OCI_DATACATALOG_WORK_REQUEST_RESOURCE_T Type

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

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'MOVED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET to access the resource metadata

### DBMS_CLOUD_OCI_DATACATALOG_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_datacatalog_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATACATALOG_WORK_REQUEST_T Type

A description of workrequest status.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'CREATE_CATALOG', 'UPDATE_CATALOG', 'DELETE_CATALOG', 'MOVE_CATALOG', 'CREATE_CATALOG_PRIVATE_ENDPOINT', 'DELETE_CATALOG_PRIVATE_ENDPOINT', 'UPDATE_CATALOG_PRIVATE_ENDPOINT', 'MOVE_CATALOG_PRIVATE_ENDPOINT', 'ATTACH_CATALOG_PRIVATE_ENDPOINT', 'DETACH_CATALOG_PRIVATE_ENDPOINT', 'CREATE_METASTORE', 'UPDATE_METASTORE', 'DELETE_METASTORE', 'MOVE_METASTORE'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The id of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used.

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

### DBMS_CLOUD_OCI_DATACATALOG_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed on (https://docs.us-phoenix-1.oraclecloud.com/Content/API/References/apierrors.htm)

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) The time the error occured. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

### DBMS_CLOUD_OCI_DATACATALOG_WORK_REQUEST_LOG_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string

- [Data Catalog Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-42B6F546-1440-46BA-A338-3AD9C2D69966)
- [DBMS_CLOUD_OCI_DATACATALOG_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-D4B361FE-12F1-4B2A-9E43-33656C8CAF8D)
- [DBMS_CLOUD_OCI_DATACATALOG_ADD_RESOURCE_LOCK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-51629232-DCF5-4B1C-A587-C1F9D074A0C4)
- [DBMS_CLOUD_OCI_DATACATALOG_OBJECT_STORAGE_OBJECT_REFERENCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-90F1842C-5A86-4FC0-B290-FC07C283E0CE)
- [DBMS_CLOUD_OCI_DATACATALOG_ASYNCHRONOUS_EXPORT_GLOSSARY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-C5FC7EE9-6DB6-40E1-9939-A5A8865E05CF)
- [DBMS_CLOUD_OCI_DATACATALOG_ASYNCHRONOUS_EXPORT_GLOSSARY_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-8701F179-EF55-4EA4-88E4-C6731DBE3C07)
- [DBMS_CLOUD_OCI_DATACATALOG_ASYNCHRONOUS_EXPORT_REQUEST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-E793E9F9-E7B0-4CEC-AA43-A5A29317BB17)
- [DBMS_CLOUD_OCI_DATACATALOG_ASYNCHRONOUS_EXPORT_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-56CA0900-880F-4E0D-950E-6329C9381C6B)
- [DBMS_CLOUD_OCI_DATACATALOG_ATTACH_CATALOG_PRIVATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-6DB497BD-5776-4DC7-9901-28B9B1836115)
- [DBMS_CLOUD_OCI_DATACATALOG_OBJECT_RELATIONSHIP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-C0BB1D03-542B-40E3-8AFB-84951BD685DE)
- [DBMS_CLOUD_OCI_DATACATALOG_CUSTOM_PROPERTY_GET_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-CEB9BAC7-C264-4712-8821-E125C659DFAD)
- [DBMS_CLOUD_OCI_DATACATALOG_OBJECT_RELATIONSHIP_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-2E368792-FC76-4679-A80E-D41CF5C01FDA)
- [DBMS_CLOUD_OCI_DATACATALOG_CUSTOM_PROPERTY_GET_USAGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-0748AC5D-0E30-441F-8CFC-953180F2AB51)
- [DBMS_CLOUD_OCI_DATACATALOG_ATTRIBUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-3DAEA662-4920-49FF-8970-EF0365D4328B)
- [DBMS_CLOUD_OCI_DATACATALOG_ATTRIBUTE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-A53EFCA0-2066-42DF-98EE-32DCBD87963A)
- [DBMS_CLOUD_OCI_DATACATALOG_ATTRIBUTE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-DB369783-ACA1-484F-9257-66A62FFA462D)
- [DBMS_CLOUD_OCI_DATACATALOG_ATTRIBUTE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-580E08EC-6602-4BB0-8AAD-2FD099E3355A)
- [DBMS_CLOUD_OCI_DATACATALOG_ATTRIBUTE_TAG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-299B2A31-CC60-44A7-8093-34A7A0851942)
- [DBMS_CLOUD_OCI_DATACATALOG_ATTRIBUTE_TAG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-CBD58A6E-559E-461A-9CBF-2E95D3336845)
- [DBMS_CLOUD_OCI_DATACATALOG_ATTRIBUTE_TAG_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-4834134C-A649-4628-AF2B-DF24335F7C21)
- [DBMS_CLOUD_OCI_DATACATALOG_ATTRIBUTE_TAG_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-B5251225-E717-4813-AECC-971B3A266870)
- [DBMS_CLOUD_OCI_DATACATALOG_BASE_PERMISSIONS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-0387FB65-76B3-4656-B73C-A174B3AE9B9C)
- [DBMS_CLOUD_OCI_DATACATALOG_BASE_TAG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-B18D9DAE-577B-4B4A-804C-B25EE6993FC4)
- [DBMS_CLOUD_OCI_DATACATALOG_BASE_TAG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-8C8EEC62-D7EF-4C00-AF2B-827C4552F649)
- [DBMS_CLOUD_OCI_DATACATALOG_RESOURCE_LOCK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-25FA372E-BD97-42E1-97AC-42E65575128A)
- [DBMS_CLOUD_OCI_DATACATALOG_RESOURCE_LOCK_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-58A19721-B1F0-4C5F-AD21-BE8D88FCD118)
- [DBMS_CLOUD_OCI_DATACATALOG_CATALOG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-1340805B-704C-4BEA-BC6A-327086E08FC0)
- [DBMS_CLOUD_OCI_DATACATALOG_CATALOG_PERMISSIONS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-08B9B1CA-66E8-442E-87F7-64313FA14F97)
- [DBMS_CLOUD_OCI_DATACATALOG_CATALOG_PRIVATE_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-01623DFB-EAB3-4400-8CE7-3FF83D8385C1)
- [DBMS_CLOUD_OCI_DATACATALOG_CATALOG_PRIVATE_ENDPOINT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-2E9AC063-AD29-4589-A3D6-F524D088E3B6)
- [DBMS_CLOUD_OCI_DATACATALOG_CATALOG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-90B76082-D20B-42D5-B2F1-D24E99DECDCB)
- [DBMS_CLOUD_OCI_DATACATALOG_CHANGE_CATALOG_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-7C036892-5601-4311-BD5A-965EC68A5B0A)
- [DBMS_CLOUD_OCI_DATACATALOG_CHANGE_CATALOG_PRIVATE_ENDPOINT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-0B932CBD-029E-4975-9DD2-79933A6B6EA4)
- [DBMS_CLOUD_OCI_DATACATALOG_CHANGE_METASTORE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-DD931417-D70D-4A24-9980-6A2E96F39AF2)
- [DBMS_CLOUD_OCI_DATACATALOG_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-E0A4326D-7676-434B-8C23-402077D02EF1)
- [DBMS_CLOUD_OCI_DATACATALOG_CONNECTION_ALIAS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-C6480C19-3BF5-4451-8863-6B090667883B)
- [DBMS_CLOUD_OCI_DATACATALOG_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-5B2653B3-0C73-4C36-81E7-7F41E1122B60)
- [DBMS_CLOUD_OCI_DATACATALOG_CONNECTION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-D69A40E3-1B89-402C-B14F-3978BF483E25)
- [DBMS_CLOUD_OCI_DATACATALOG_CONNECTION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-E3AD8477-57EA-41D9-AB8B-856AF4E064B4)
- [DBMS_CLOUD_OCI_DATACATALOG_CUSTOM_PROPERTY_SET_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-860FE69F-A73C-4516-AF51-E00D3B7FC5D2)
- [DBMS_CLOUD_OCI_DATACATALOG_CUSTOM_PROPERTY_SET_USAGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-BB5B9955-1D02-4B50-96F8-DE5040C33EE2)
- [DBMS_CLOUD_OCI_DATACATALOG_CREATE_ATTRIBUTE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-E0E50912-C564-492D-8339-074DD77BA2FF)
- [DBMS_CLOUD_OCI_DATACATALOG_CREATE_CATALOG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-17EBBE03-D30F-40B6-948B-258D036B8BA1)
- [DBMS_CLOUD_OCI_DATACATALOG_CREATE_CATALOG_PRIVATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-8A7B3894-035B-464E-8BD8-BB76B6FE0BDA)
- [DBMS_CLOUD_OCI_DATACATALOG_CREATE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-D9ABEC46-1297-4E90-A29D-BED3F72A7461)
- [DBMS_CLOUD_OCI_DATACATALOG_CREATE_CUSTOM_PROPERTY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-CBE00119-308F-4F07-B95D-FEBC3A01E6FC)
- [DBMS_CLOUD_OCI_DATACATALOG_CREATE_DATA_ASSET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-2E7D9313-69C9-40C9-9D6E-244E6C245C5B)
- [DBMS_CLOUD_OCI_DATACATALOG_CREATE_ENTITY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-A31132BD-492F-43E5-B090-C5DEE7CA3A1F)
- [DBMS_CLOUD_OCI_DATACATALOG_CREATE_FOLDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-BF946952-3BA6-4601-A5B2-F5AD4F1E8BD3)
- [DBMS_CLOUD_OCI_DATACATALOG_CREATE_GLOSSARY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-A942F270-0583-415B-A5B5-2CACB03659CB)
- [DBMS_CLOUD_OCI_DATACATALOG_CREATE_JOB_DEFINITION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-3331DAA6-C3A7-44EC-84AA-992CD1E223EE)
- [DBMS_CLOUD_OCI_DATACATALOG_CREATE_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-AEC70DC9-E5C7-4650-BD16-9FD776622DE9)
- [DBMS_CLOUD_OCI_DATACATALOG_CREATE_JOB_EXECUTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-469F3162-B1AB-4839-AC5D-82D8ECE17CC8)
- [DBMS_CLOUD_OCI_DATACATALOG_CREATE_METASTORE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-490B07B8-0400-47CD-B253-FB39D193475E)
- [DBMS_CLOUD_OCI_DATACATALOG_CREATE_NAMESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-C1B0C175-BC86-4473-8702-3FD29F42624A)
- [DBMS_CLOUD_OCI_DATACATALOG_CREATE_PATTERN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-C40850A5-C2BE-41B3-A2CD-AF4417CB2581)
- [DBMS_CLOUD_OCI_DATACATALOG_CREATE_TAG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-3A445DA1-54CA-45DB-B544-EBE4C4D2E583)
- [DBMS_CLOUD_OCI_DATACATALOG_CREATE_TERM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-D8205335-D5E4-47B5-94DE-6B364104A7A4)
- [DBMS_CLOUD_OCI_DATACATALOG_CREATE_TERM_RELATIONSHIP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-F99691DC-62BE-4E68-8605-256798E64E24)
- [DBMS_CLOUD_OCI_DATACATALOG_CUSTOM_PROPERTY_TYPE_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-9A701BF4-117F-4A9B-A120-E30500EEDE5D)
- [DBMS_CLOUD_OCI_DATACATALOG_EVENT_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-AB85B4DF-9DAE-4C18-85BC-FA372D95FB0A)
- [DBMS_CLOUD_OCI_DATACATALOG_CUSTOM_PROPERTY_TYPE_USAGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-E3606132-77BB-4DC0-9052-3B4BE8842185)
- [DBMS_CLOUD_OCI_DATACATALOG_EVENT_CONFIG_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-FEC39AC1-F0C0-4362-AAC6-3B2E77F4B662)
- [DBMS_CLOUD_OCI_DATACATALOG_CUSTOM_PROPERTY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-25BE7119-4386-409F-8E8D-89F054523DFC)
- [DBMS_CLOUD_OCI_DATACATALOG_CUSTOM_PROPERTY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-C60B796F-E0E8-4202-89E3-2AE972D40D21)
- [DBMS_CLOUD_OCI_DATACATALOG_CUSTOM_PROPERTY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-CE9F145D-F395-468B-B682-F98EBD3A4EE4)
- [DBMS_CLOUD_OCI_DATACATALOG_CUSTOM_PROPERTY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-E93D7205-037B-468E-9F90-C5925B87458A)
- [DBMS_CLOUD_OCI_DATACATALOG_PATTERN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-D47E2B57-421E-4F59-82C1-18A0B52E5884)
- [DBMS_CLOUD_OCI_DATACATALOG_PATTERN_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-489E63E3-1756-4DE3-9A14-579973047F65)
- [DBMS_CLOUD_OCI_DATACATALOG_DATA_ASSET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-0280AA27-F1AA-4620-8481-D97EEA50D962)
- [DBMS_CLOUD_OCI_DATACATALOG_DATA_ASSET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-3656BF2B-3D0D-4BE2-84CD-A74C97E77863)
- [DBMS_CLOUD_OCI_DATACATALOG_DATA_ASSET_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-2292631C-CF33-4F2C-832E-B084280D9C60)
- [DBMS_CLOUD_OCI_DATACATALOG_DATA_ASSET_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-7A597C7D-EE4F-467E-B100-2DEEBE9EB43C)
- [DBMS_CLOUD_OCI_DATACATALOG_DATA_ASSET_EXPORT_SCOPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-741F638F-202E-448D-82CA-72C49458D26E)
- [DBMS_CLOUD_OCI_DATACATALOG_DATA_ASSET_PERMISSIONS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-776388A5-CDEB-4769-B9E5-CA6DC48DF577)
- [DBMS_CLOUD_OCI_DATACATALOG_DATA_ASSET_TAG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-94EB7E0A-068E-4117-BAFF-2CF9244EF514)
- [DBMS_CLOUD_OCI_DATACATALOG_DATA_ASSET_TAG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-E9AC96B9-4D16-4912-BD41-6D4DFA1A8BFE)
- [DBMS_CLOUD_OCI_DATACATALOG_DATA_ASSET_TAG_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-2F421405-868F-4616-A2CB-F4167B9103BD)
- [DBMS_CLOUD_OCI_DATACATALOG_DATA_ASSET_TAG_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-A1880530-624F-4865-9113-FCDC8168D509)
- [DBMS_CLOUD_OCI_DATACATALOG_DATA_SELECTOR_PATTERN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-B9FD2DFB-5285-4AE3-A30C-15343893F4F5)
- [DBMS_CLOUD_OCI_DATACATALOG_DERIVED_LOGICAL_ENTITIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-ADA4799F-8210-42E3-BC34-870BFBA757E2)
- [DBMS_CLOUD_OCI_DATACATALOG_DETACH_CATALOG_PRIVATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-DF2F1FC2-B6EE-4117-A684-43E2195F36DA)
- [DBMS_CLOUD_OCI_DATACATALOG_ENTITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-8040D1AE-ED92-47A3-9C07-75EB1C096438)
- [DBMS_CLOUD_OCI_DATACATALOG_ENTITY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-DC9C4BED-84ED-4973-A242-2D7BA0EEBE92)
- [DBMS_CLOUD_OCI_DATACATALOG_ENTITY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-5961D330-E515-4B6A-A8A3-CF310894E937)
- [DBMS_CLOUD_OCI_DATACATALOG_ENTITY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-390F19D6-9BB9-4478-8DC1-F8346DCC522B)
- [DBMS_CLOUD_OCI_DATACATALOG_LINEAGE_OBJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-C7B6E5D2-DBF6-4E6C-8A5E-635610B7B38B)
- [DBMS_CLOUD_OCI_DATACATALOG_LINEAGE_RELATIONSHIP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-25F40583-BB3C-47EE-9F11-791E52A2B24F)
- [DBMS_CLOUD_OCI_DATACATALOG_LINEAGE_OBJECT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-6356CF27-FBDB-458E-8FCB-B6994C1091F4)
- [DBMS_CLOUD_OCI_DATACATALOG_LINEAGE_RELATIONSHIP_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-38F10258-2B8B-4E83-8369-B20D572A4512)
- [DBMS_CLOUD_OCI_DATACATALOG_ENTITY_LINEAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-77514D5A-09C0-4B97-BA11-EA4BB3B4A063)
- [DBMS_CLOUD_OCI_DATACATALOG_ENTITY_TAG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-1112E84B-6FEA-4179-B38B-9E71EEA0A190)
- [DBMS_CLOUD_OCI_DATACATALOG_ENTITY_TAG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-04B98875-CE3B-4051-AD1D-F64339BE497E)
- [DBMS_CLOUD_OCI_DATACATALOG_ENTITY_TAG_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-77A86156-392E-4121-B94B-A4B9A40EF5E4)
- [DBMS_CLOUD_OCI_DATACATALOG_ENTITY_TAG_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-69181C76-85C6-4FCA-889F-C0C5BE969AB1)
- [DBMS_CLOUD_OCI_DATACATALOG_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-080EA96E-0E66-4D46-AA33-068348D8A696)
- [DBMS_CLOUD_OCI_DATACATALOG_DATA_ASSET_EXPORT_SCOPE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-4565D53E-59AA-411B-89F7-49F86733C728)
- [DBMS_CLOUD_OCI_DATACATALOG_EXPORT_DATA_ASSET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-D2ABFCEE-F75A-496C-B454-3E7D21283504)
- [DBMS_CLOUD_OCI_DATACATALOG_FACETED_SEARCH_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-232B28CC-F6A6-41B1-8A0B-0B9FE2FBCDF1)
- [DBMS_CLOUD_OCI_DATACATALOG_FACETED_SEARCH_CUSTOM_PROPERTY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-BC2A84B5-A4F6-4A2A-BF28-CB00B486868C)
- [DBMS_CLOUD_OCI_DATACATALOG_FACETED_SEARCH_DATE_FILTER_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-E5DC2974-0D14-43EF-808C-02B998C59A2B)
- [DBMS_CLOUD_OCI_DATACATALOG_FACETED_SEARCH_STRING_FILTER_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-886BEC68-E22C-4D7A-A4C7-637FDF04435C)
- [DBMS_CLOUD_OCI_DATACATALOG_FACETED_SEARCH_DATE_FILTER_REQUEST_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-1AB95F97-0385-4EDD-AC97-634A79785E17)
- [DBMS_CLOUD_OCI_DATACATALOG_FACETED_SEARCH_STRING_FILTER_REQUEST_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-1EB13BA0-963A-4BB1-8BE5-F6E5E0B21872)
- [DBMS_CLOUD_OCI_DATACATALOG_FACETED_SEARCH_FILTER_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-FE8C6EEA-8FBE-46B8-B9A7-83F6971BB2A6)
- [DBMS_CLOUD_OCI_DATACATALOG_FACETED_SEARCH_SORT_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-048772A2-41DC-4589-9182-7229D19E5D5C)
- [DBMS_CLOUD_OCI_DATACATALOG_FETCH_ENTITY_LINEAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-0F3100EE-7F84-40C9-A3A1-5DF9E6CF269B)
- [DBMS_CLOUD_OCI_DATACATALOG_FOLDER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-F4417000-4AEE-49C4-BD7C-0B908F205DC6)
- [DBMS_CLOUD_OCI_DATACATALOG_FOLDER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-7B24F553-9733-4DE7-842E-E2E5E971F862)
- [DBMS_CLOUD_OCI_DATACATALOG_FOLDER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-7955C837-F849-439D-8069-3EF376811F1E)
- [DBMS_CLOUD_OCI_DATACATALOG_FOLDER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-231658EE-7900-4F87-9206-8F63F81D32BD)
- [DBMS_CLOUD_OCI_DATACATALOG_FOLDER_TAG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-75A74A81-B67B-47B9-AF31-DE6613BFA363)
- [DBMS_CLOUD_OCI_DATACATALOG_FOLDER_TAG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-BA22A710-C707-46CC-ADF9-C84A47F98268)
- [DBMS_CLOUD_OCI_DATACATALOG_FOLDER_TAG_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-B3D489B2-0717-4D86-91A5-BC6033EA5E3D)
- [DBMS_CLOUD_OCI_DATACATALOG_FOLDER_TAG_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-F288B9CC-3FD6-4DBF-9693-2B8E4988AE1C)
- [DBMS_CLOUD_OCI_DATACATALOG_GLOSSARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-1B041E1A-5D58-4416-B4C6-E0192BE11E0D)
- [DBMS_CLOUD_OCI_DATACATALOG_GLOSSARY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-D4ACA665-723C-49FF-882F-BC999ADDF5E4)
- [DBMS_CLOUD_OCI_DATACATALOG_GLOSSARY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-F2BA1BA2-AE0C-4CBE-81D5-596DE15184C8)
- [DBMS_CLOUD_OCI_DATACATALOG_GLOSSARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-8385FFE1-19CC-4972-B7CA-FBB4FFD1F290)
- [DBMS_CLOUD_OCI_DATACATALOG_GLOSSARY_PERMISSIONS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-9DD31650-2EB6-4F5F-8A07-5AE81540AA3E)
- [DBMS_CLOUD_OCI_DATACATALOG_GLOSSARY_TREE_ELEMENT_ABS_T](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-81BF6771-151F-4F85-94C4-DCB1D7F812F8)
- [DBMS_CLOUD_OCI_DATACATALOG_GLOSSARY_TREE_ELEMENT_ABS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-FDD6534B-8C4C-4583-A3BA-059F28C21912)
- [DBMS_CLOUD_OCI_DATACATALOG_GLOSSARY_TREE_ELEMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-45F32FFE-B68C-4C16-8CFF-2DF8FA3A6493)
- [DBMS_CLOUD_OCI_DATACATALOG_GLOSSARY_TREE_ELEMENT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-B94EB63B-59CB-4171-AEC8-6E12DEC9E890)
- [DBMS_CLOUD_OCI_DATACATALOG_IMPORT_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-E420EE24-515E-4475-8167-134F9177F491)
- [DBMS_CLOUD_OCI_DATACATALOG_IMPORT_DATA_ASSET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-B7A75850-2A58-4902-9CF6-F861AE085684)
- [DBMS_CLOUD_OCI_DATACATALOG_IMPORT_DATA_ASSET_JOB_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-96DAB002-8056-48BA-AD02-F6563347E3A8)
- [DBMS_CLOUD_OCI_DATACATALOG_IMPORT_GLOSSARY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-357AD1E4-CEB2-4825-B23D-64CDAEBD4BD3)
- [DBMS_CLOUD_OCI_DATACATALOG_JOB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-8ED93D46-3566-4D07-8CC3-1C41ABE88697)
- [DBMS_CLOUD_OCI_DATACATALOG_JOB_EXECUTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-426AFF2E-B014-4CD7-9863-09E394DA6F75)
- [DBMS_CLOUD_OCI_DATACATALOG_JOB_EXECUTION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-A179310D-26D9-4AF5-808C-79AF9B169EE7)
- [DBMS_CLOUD_OCI_DATACATALOG_JOB_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-C1A09766-B98F-4031-B00D-71FF6019BC52)
- [DBMS_CLOUD_OCI_DATACATALOG_JOB_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-BD36122D-3DE2-4121-A0CC-324B0E5F27B5)
- [DBMS_CLOUD_OCI_DATACATALOG_JOB_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-ED0BB0B1-467E-4A81-A0BA-023BB811AB4D)
- [DBMS_CLOUD_OCI_DATACATALOG_JOB_DEFINITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-826A2533-1B06-4B44-BCF9-926F73634C31)
- [DBMS_CLOUD_OCI_DATACATALOG_JOB_DEFINITION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-AB4CB184-59A5-47CA-8B58-A30809A24114)
- [DBMS_CLOUD_OCI_DATACATALOG_JOB_DEFINITION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-238842F1-26BB-430D-BC5D-9F508A501CDE)
- [DBMS_CLOUD_OCI_DATACATALOG_JOB_DEFINITION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-3283292B-F696-4B93-9BB6-7E4B0363C516)
- [DBMS_CLOUD_OCI_DATACATALOG_JOB_DEFINITION_PERMISSIONS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-49D7E6C3-3430-4590-9629-E0B7373FDA79)
- [DBMS_CLOUD_OCI_DATACATALOG_JOB_DEFINITION_SCOPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-3F243EDD-B1CD-4CEF-B597-B551D210A83F)
- [DBMS_CLOUD_OCI_DATACATALOG_JOB_EXECUTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-ED2CF299-F17A-466A-89FA-F254DD7F57A0)
- [DBMS_CLOUD_OCI_DATACATALOG_JOB_EXECUTION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-1EB36214-8E47-43AA-ACA6-843F25ADBA3E)
- [DBMS_CLOUD_OCI_DATACATALOG_JOB_LOG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-7115225E-01B1-46F0-9AA9-58C596255BFC)
- [DBMS_CLOUD_OCI_DATACATALOG_JOB_LOG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-1D634BD5-53F6-4241-818E-ECB6BA4111B9)
- [DBMS_CLOUD_OCI_DATACATALOG_JOB_LOG_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-9C10D65F-BE11-447B-83FB-6F280CF9F611)
- [DBMS_CLOUD_OCI_DATACATALOG_JOB_LOG_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-C0F38857-FCD8-4775-B8A1-81AD874AD994)
- [DBMS_CLOUD_OCI_DATACATALOG_JOB_METRIC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-8980E6A5-58B5-412A-A5E9-8D54CF08CAF3)
- [DBMS_CLOUD_OCI_DATACATALOG_JOB_METRIC_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-B393393E-5DF3-4ACC-AAE9-97AB36482A4B)
- [DBMS_CLOUD_OCI_DATACATALOG_JOB_METRIC_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-267EA620-2F47-4994-8786-3B2E9CE1827F)
- [DBMS_CLOUD_OCI_DATACATALOG_JOB_METRIC_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-F65E7FCE-6984-4896-912D-D50B16120919)
- [DBMS_CLOUD_OCI_DATACATALOG_METASTORE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-0991EBAE-5E95-4F64-9092-603CFEE9DD36)
- [DBMS_CLOUD_OCI_DATACATALOG_METASTORE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-0601FF33-0AF2-49F6-A6F6-D9D3324416D4)
- [DBMS_CLOUD_OCI_DATACATALOG_NAMESPACE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-191FBCBA-2F88-42D4-8D31-63278C7327D5)
- [DBMS_CLOUD_OCI_DATACATALOG_NAMESPACE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-3E06DBBD-DA44-4B5C-9C7B-EE65D788DD37)
- [DBMS_CLOUD_OCI_DATACATALOG_NAMESPACE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-C575C6F3-B25A-4675-97F5-0A484BDF7ED4)
- [DBMS_CLOUD_OCI_DATACATALOG_NAMESPACE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-4FAE21E9-7CD1-42EA-AD02-4AC1EB8E3736)
- [DBMS_CLOUD_OCI_DATACATALOG_OBJECT_LINEAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-9AB15B35-C078-4802-B662-7283FE61A11D)
- [DBMS_CLOUD_OCI_DATACATALOG_OBJECT_LINEAGE_REQUEST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-CFAAEA6D-1A97-42D9-9C7D-868FCFA0D21D)
- [DBMS_CLOUD_OCI_DATACATALOG_PARSE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-EAFA09CC-7276-4308-B4A8-19B12575861A)
- [DBMS_CLOUD_OCI_DATACATALOG_PATTERN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-7FCED36F-C100-49F8-BA59-CD3DDB753AB0)
- [DBMS_CLOUD_OCI_DATACATALOG_PATTERN_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-CEE5B07D-66AE-40C3-BCC7-96DB4E6C30F7)
- [DBMS_CLOUD_OCI_DATACATALOG_PROCESS_RECOMMENDATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-497DC355-FAD7-4AF4-AF6C-8B739B41B055)
- [DBMS_CLOUD_OCI_DATACATALOG_PROPERTY_DEFINITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-53572959-900F-4626-B745-39EE21746D03)
- [DBMS_CLOUD_OCI_DATACATALOG_RECOMMENDATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-39B49B76-F7AB-4460-9EAC-EF479A5D0BC9)
- [DBMS_CLOUD_OCI_DATACATALOG_RECOMMENDATION_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-3768E315-B959-4EC5-AC88-8A1791A06717)
- [DBMS_CLOUD_OCI_DATACATALOG_RECOMMENDATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-A6D3FC48-183E-4131-9154-2A1C59CDD58C)
- [DBMS_CLOUD_OCI_DATACATALOG_REMOVE_RESOURCE_LOCK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-6080782C-0895-4204-B114-8793DA037257)
- [DBMS_CLOUD_OCI_DATACATALOG_RULE_ATTRIBUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-15618C43-E433-4E68-B80C-2400D57C2766)
- [DBMS_CLOUD_OCI_DATACATALOG_RULE_ATTRIBUTE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-5026F2CA-3773-4519-98A9-F7C78C1EF6AB)
- [DBMS_CLOUD_OCI_DATACATALOG_RULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-03EB3CD4-2387-44EF-9E5B-6C1497743829)
- [DBMS_CLOUD_OCI_DATACATALOG_RULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-375B76B7-808A-4BBF-86C7-A22F2A330924)
- [DBMS_CLOUD_OCI_DATACATALOG_RULE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-8F8C3774-4CC5-4C78-84F9-D30F20E79DFB)
- [DBMS_CLOUD_OCI_DATACATALOG_FACETED_SEARCH_SORT_REQUEST_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-4BC5C025-5D59-4A01-8987-4047F422628F)
- [DBMS_CLOUD_OCI_DATACATALOG_SEARCH_CRITERIA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-2ECE8301-4DF3-4411-96A4-04C610D3FBD4)
- [DBMS_CLOUD_OCI_DATACATALOG_SEARCH_TAG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-D89B8101-4993-4504-96A0-7D70CA1CE150)
- [DBMS_CLOUD_OCI_DATACATALOG_SEARCH_TERM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-D78D1228-D228-421C-81B7-B3AC6FA0A214)
- [DBMS_CLOUD_OCI_DATACATALOG_SEARCH_TAG_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-CB77C2A4-AB90-4E72-8253-D4E01946F8B9)
- [DBMS_CLOUD_OCI_DATACATALOG_SEARCH_TERM_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-985F6DF9-6B15-432B-A85B-1861E916708E)
- [DBMS_CLOUD_OCI_DATACATALOG_FACETED_SEARCH_CUSTOM_PROPERTY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-3A3A653E-DA8A-4AD1-B9A6-524B3AB70F35)
- [DBMS_CLOUD_OCI_DATACATALOG_SEARCH_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-2BE7D9F8-F317-4BB3-A7DF-754FF8BA4424)
- [DBMS_CLOUD_OCI_DATACATALOG_SEARCH_RESULT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-88A617AB-99ED-4F6A-AFF1-B797D29CB958)
- [DBMS_CLOUD_OCI_DATACATALOG_FACETED_SEARCH_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-B65188E5-DDC1-4656-B273-CA80CB3454AD)
- [DBMS_CLOUD_OCI_DATACATALOG_SEARCH_RESULT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-C8BC12E0-CCA1-4A8E-8AC9-C5D29E16CA11)
- [DBMS_CLOUD_OCI_DATACATALOG_SUGGEST_LIST_ITEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-0E615F42-FC97-45D8-AB37-E77C9F5E2E55)
- [DBMS_CLOUD_OCI_DATACATALOG_SUGGEST_LIST_ITEM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-28D74680-8343-4B6A-98AD-4E2C7B175A26)
- [DBMS_CLOUD_OCI_DATACATALOG_SUGGEST_RESULTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-DC4B0911-3C24-457D-9582-4C16C5654802)
- [DBMS_CLOUD_OCI_DATACATALOG_TERM_ASSOCIATED_OBJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-8688BDBE-1AE6-420B-A3EA-720E74FA3F1C)
- [DBMS_CLOUD_OCI_DATACATALOG_TERM_ASSOCIATED_OBJECT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-EF274024-78D6-4634-A580-3EE794259A03)
- [DBMS_CLOUD_OCI_DATACATALOG_TERM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-E44E96C0-622F-4111-BEA9-9EF9A300A8CE)
- [DBMS_CLOUD_OCI_DATACATALOG_TERM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-50FFCA45-8B74-4CBF-96CD-D1AE98F17A56)
- [DBMS_CLOUD_OCI_DATACATALOG_TERM_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-57F636FB-E59F-4DEE-8EA3-91C17363F488)
- [DBMS_CLOUD_OCI_DATACATALOG_TERM_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-84FB10BE-434F-46CE-9DF1-21D6742DE598)
- [DBMS_CLOUD_OCI_DATACATALOG_TERM_RELATIONSHIP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-CB15860C-613E-4C10-9D15-0E2A9A424FA9)
- [DBMS_CLOUD_OCI_DATACATALOG_TERM_RELATIONSHIP_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-43766C8B-9751-4FAB-A1A2-96146B70D1E0)
- [DBMS_CLOUD_OCI_DATACATALOG_TERM_RELATIONSHIP_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-0709947B-57BE-42F2-8175-945E46C1A0B7)
- [DBMS_CLOUD_OCI_DATACATALOG_TERM_RELATIONSHIP_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-4F937479-CFD6-4900-9F7C-C6574243C199)
- [DBMS_CLOUD_OCI_DATACATALOG_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-98E5E10C-28A3-4F02-A269-E695F648AD3E)
- [DBMS_CLOUD_OCI_DATACATALOG_TYPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-B23166EA-B65B-4AB2-8C9D-453D26D7FD11)
- [DBMS_CLOUD_OCI_DATACATALOG_TYPE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-FF7D859E-9723-4FF9-84FE-7E17303C8A54)
- [DBMS_CLOUD_OCI_DATACATALOG_TYPE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-D8DC91CB-24CF-4100-923E-79B74254D576)
- [DBMS_CLOUD_OCI_DATACATALOG_TYPE_CUSTOM_PROPERTY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-BA23BBDF-55F9-4045-9052-3D5E905677B5)
- [DBMS_CLOUD_OCI_DATACATALOG_UPDATE_ATTRIBUTE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-F2F2E481-4233-4D18-8D91-B49A0E084950)
- [DBMS_CLOUD_OCI_DATACATALOG_UPDATE_CATALOG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-7D9AB67B-8FCA-4946-BE11-D9F3DE1C71DC)
- [DBMS_CLOUD_OCI_DATACATALOG_UPDATE_CATALOG_PRIVATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-910D736E-CAB3-40D1-9C8A-5C0D38BF07A7)
- [DBMS_CLOUD_OCI_DATACATALOG_UPDATE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-784F13DC-A52B-46E3-8CAD-D85E7D92B3E9)
- [DBMS_CLOUD_OCI_DATACATALOG_UPDATE_CUSTOM_PROPERTY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-722129AD-21F1-4737-931A-FFFD6F6DEF1A)
- [DBMS_CLOUD_OCI_DATACATALOG_UPDATE_DATA_ASSET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-B4EC56C1-ACC2-466B-B2C6-BE513C383593)
- [DBMS_CLOUD_OCI_DATACATALOG_UPDATE_ENTITY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-5A002C8D-FE6C-4A0B-B4CC-E5D189100473)
- [DBMS_CLOUD_OCI_DATACATALOG_UPDATE_FOLDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-A5B32F43-8934-49EE-A21A-389108BCE42D)
- [DBMS_CLOUD_OCI_DATACATALOG_UPDATE_GLOSSARY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-0E0C2247-5C47-42EB-93A6-D2D299D5C23C)
- [DBMS_CLOUD_OCI_DATACATALOG_UPDATE_JOB_DEFINITION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-2FC475C2-7011-4D44-A939-FA39A5F43BA3)
- [DBMS_CLOUD_OCI_DATACATALOG_UPDATE_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-5DBF6183-321E-4E6D-9E7E-9C5B012ABBDE)
- [DBMS_CLOUD_OCI_DATACATALOG_UPDATE_METASTORE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-EE920C8C-2A69-47B1-9115-A07DE0C2EC8B)
- [DBMS_CLOUD_OCI_DATACATALOG_UPDATE_NAMESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-1761C88B-6CDB-49E5-B194-6CC6A9FBAD0E)
- [DBMS_CLOUD_OCI_DATACATALOG_UPDATE_PATTERN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-884BBEE9-DF83-4E5E-840A-F634A290D733)
- [DBMS_CLOUD_OCI_DATACATALOG_UPDATE_TERM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-10602C94-1FD4-41B2-83EE-5D0FB4DD7B44)
- [DBMS_CLOUD_OCI_DATACATALOG_UPDATE_TERM_RELATIONSHIP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-EF846BD3-C429-4A14-9A25-213652380913)
- [DBMS_CLOUD_OCI_DATACATALOG_UPLOAD_CREDENTIALS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-3D8F56A1-C8FC-42DC-AB35-C07695BEB149)
- [DBMS_CLOUD_OCI_DATACATALOG_VALIDATE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-704B3078-BDAA-4F83-9E60-6AF371206FED)
- [DBMS_CLOUD_OCI_DATACATALOG_VALIDATE_CONNECTION_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-BBB7D209-3116-4766-82DB-4B6DCF964C9A)
- [DBMS_CLOUD_OCI_DATACATALOG_VALIDATE_PATTERN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-00832A1F-D535-4F10-A286-E8E8F85E97A1)
- [DBMS_CLOUD_OCI_DATACATALOG_DERIVED_LOGICAL_ENTITIES_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-41AB4FED-A3DB-4B6C-ACAA-97C878832D16)
- [DBMS_CLOUD_OCI_DATACATALOG_VALIDATE_PATTERN_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-95A90AE5-9718-4872-B155-1605C6E9C467)
- [DBMS_CLOUD_OCI_DATACATALOG_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-D547C32B-33F0-4F72-B2B9-085A18DF8B86)
- [DBMS_CLOUD_OCI_DATACATALOG_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-5AF176E9-0EBB-47A8-99EE-07F84A841B68)
- [DBMS_CLOUD_OCI_DATACATALOG_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-7508CA85-4BE4-4508-8FBD-986487142ED2)
- [DBMS_CLOUD_OCI_DATACATALOG_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-A68296D2-9A06-4B7C-A61E-9891C35D1BAF)
- [DBMS_CLOUD_OCI_DATACATALOG_WORK_REQUEST_LOG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datacatalog_t.html#ADSDK-GUID-B235A63B-F73E-40C0-9E17-E22FE5B07A6A)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
