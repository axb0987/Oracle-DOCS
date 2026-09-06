# Data Labeling Service Dataplane Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html
- Fetched: 2026-09-05 19:02 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#dcoc-content-body)

## Data Labeling Service Dataplane Common Types

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_ENTITY_T Type

An entity allows the labeler to identify an object in the record to label. This can be, for example, a snippet of text, an entire image, or a bounding box within an image. All entity types have an array of labels that are indexed. If more than one label is provided, but the annotationType on the corresponding dataset is for a single class, the API rejects the create annotation request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The entity type described in the annotation. GENERIC - An extensible entity type that is the base entity type for some annotation formats. IMAGEOBJECTSELECTION- - This allows the labeler to use specify a bounding polygon on the image to represent an object and apply labels to it. TEXTSELECTION - This allows the labeler to highlight text, by specifying an offset and a length, and apply labels to it. KEYVALUESELECTION - This allows the labeler to apply label the highlighted text from OCR.

Allowed values are: 'GENERIC', 'IMAGEOBJECTSELECTION', 'TEXTSELECTION', 'KEYVALUESELECTION'

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_ENTITY_TBL Type

Nested table type of dbms_cloud_oci_data_labeling_service_dataplane_entity_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_ANNOTATION_T Type

An annotation represents a user- or machine-generated annotation for a given record. The details of the annotation are captured in the RecordAnnotationDetails.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the annotation.

`time_created`

(required) The date and time the annotation was created, in the timestamp format defined by RFC3339.

`time_updated`

(required) The date and time the resource was updated, in the timestamp format defined by RFC3339.

`created_by`

(required) The OCID of the principal which created the annotation.

`updated_by`

(required) The OCID of the principal which updated the annotation.

`record_id`

(required) The OCID of the record annotated.

`entities`

(required) The entity types are validated against the dataset to ensure consistency.

`compartment_id`

(required) The OCID of the compartment for the annotation. This is tied to the dataset. It is not changeable on the record itself.

`lifecycle_state`

(required) The lifecycle state of an annotation. ACTIVE - The annotation is active to be used for labeling. INACTIVE - The annotation has been marked as inactive and should not be used for labeling. DELETED - Tha annotation been deleted and no longer available for labeling.

Allowed values are: 'ACTIVE', 'INACTIVE', 'DELETED'

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) The defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_LABEL_T Type

A label is a string value. The API validates that it's one of the dataset's pre-defined labels.

Syntax
```

```

Fields

Field Description

`label`

(required) The label provided by the annotator.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_ANNOTATION_AGGREGATION_DIMENSIONS_T Type

The dimensions to summarize annotations for a given dataset.

Syntax
```

```

Fields

Field Description

`label`

(optional)

`updated_by`

(optional) The OCID of the principal which updated the resource.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_ANNOTATION_ANALYTICS_AGGREGATION_T Type

Aggregation entities are required by the API consistency guidelines for API Consistency Guidelines#AnalyticsAPIs. These are used to summarize annotations for a given dataset and will be used to populate UI elements. Aggregations need to have the fields that identify the exact scope that they're summarizing. Any filters applied to the list API, have to show up in the aggregation.

Syntax
```

```

Fields

Field Description

`l_count`

(required) The count of the matching results.

`dataset_id`

(required) The OCID of the dataset the annotations belong to.

`dimensions`

(optional)

`updated_by`

(optional) The OCID of the principal which updated the annotation.

`compartment_id`

(required) The OCID of the compartment containing the annotations.

`lifecycle_state`

(optional) Describes the lifecycle state.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_ANNOTATION_ANALYTICS_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_data_labeling_service_dataplane_annotation_analytics_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_ANNOTATION_ANALYTICS_AGGREGATION_COLLECTION_T Type

Aggregation entities are required by the API consistency guidelines for API Consistency Guidelines#AnalyticsAPIs. These are used to summarize annotations for a given dataset and will be used to populate UI elements. Aggregations need to have the fields that identify the exact scope that they're summarizing. Any filters applied to the list API, have to show up in the aggregation.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of annotation entities.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_ANNOTATION_SUMMARY_T Type

An annotation summary is the representation returned in list views. It is usually a subset of the full annotation entity and should not contain any potentially sensitive information.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the annotation.

`time_created`

(required) The date and time the annotation was created, in the timestamp format defined by RFC3339.

`time_updated`

(required) The date and time the resource was updated, in the timestamp format defined by RFC3339.

`record_id`

(required) The OCID of the record annotated.

`compartment_id`

(required) The OCID of the compartment for the annotation.

`lifecycle_state`

(required) Describes the lifecycle state.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) The defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_ANNOTATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_data_labeling_service_dataplane_annotation_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_ANNOTATION_COLLECTION_T Type

The results of an annotations search. It contains AnnotationSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of annotations.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_NORMALIZED_VERTEX_T Type

A NormalizedVertex is a cartesian coordinate that represents a corner between two segments of a polygon.

Syntax
```

```

Fields

Field Description

`x`

(required) The X axis coordinate.

`y`

(required) The Y axis coordinate.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_NORMALIZED_VERTEX_TBL Type

Nested table type of dbms_cloud_oci_data_labeling_service_dataplane_normalized_vertex_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_BOUNDING_POLYGON_T Type

A polygon used to describe the location of an object.

Syntax
```

```

Fields

Field Description

`normalized_vertices`

(required) The normalized vertices that make up the polygon. They are in the order of the segments they connect.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_CREATE_ANNOTATION_DETAILS_T Type

This is the payload sent in the CreateAnnotation operation. It contains all the information required for a user to create an annotation for a record.

Syntax
```

```

Fields

Field Description

`record_id`

(required) The OCID of the record annotated.

`compartment_id`

(required) The OCID of the compartment for the annotation.

`entities`

(required) The entity types are validated against the dataset to ensure consistency.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) The defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_CREATE_SOURCE_DETAILS_T Type

The source information is a polymorphic entity. It captures the details of how to access the data for record creation. The discriminator type must match the dataset's source type. The convention will be enforced by the API. It should only provide the difference in data necessary to access the content, i.e. the object storage path, or the database record id.

Syntax
```

```

Fields

Field Description

`source_type`

(required) The type of data source. OBJECT_STORAGE - The source details for an object storage bucket.

Allowed values are: 'OBJECT_STORAGE'

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_CREATE_OBJECT_STORAGE_SOURCE_DETAILS_T Type

Object Storage Source Details.

Syntax
```

```

`dbms_cloud_oci_data_labeling_service_dataplane_create_object_storage_source_details_t`is a subtype of the`dbms_cloud_oci_data_labeling_service_dataplane_create_source_details_t`type.

Fields

Field Description

`relative_path`

(required) The path relative to the prefix specified in the dataset source details (file name).

`offset`

(optional) The offset into the file containing the content.

`length`

(optional) The length from offset into the file containing the content.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_RECORD_METADATA_T Type

Collection of record's metadata. This can be, for example, the height, width or depth of image for an image record.

Syntax
```

```

Fields

Field Description

`record_type`

(optional) The record type based on dataset format details. IMAGE_METADATA - Collection of metadata related to image record. TEXT_METADATA - Collection of metadata related to text record. DOCUMENT_METADATA - Collection of metadata related to document record.

Allowed values are: 'IMAGE_METADATA', 'TEXT_METADATA', 'DOCUMENT_METADATA'

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_CREATE_RECORD_DETAILS_T Type

A record represents an entry in a dataset that needs labeling.

Syntax
```

```

Fields

Field Description

`name`

(required) The name is automatically assigned by the service. It is unique and immutable.

`dataset_id`

(required) The OCID of the dataset to associate the record with.

`compartment_id`

(required) The OCID of the compartment for the record. This is tied to the dataset. It is not changeable on the record itself.

`source_details`

(required)

`record_metadata`

(optional)

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) The defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_DATASET_SOURCE_DETAILS_T Type

This allows the customer to specify the source of the dataset.

Syntax
```

```

Fields

Field Description

`source_type`

(required) The source type. OBJECT_STORAGE allows the user to describe where in object storage the dataset is.

Allowed values are: 'OBJECT_STORAGE'

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_DATASET_FORMAT_DETAILS_T Type

It specifies how to process the data. Supported formats include DOCUMENT, IMAGE, and TEXT.

Syntax
```

```

Fields

Field Description

`format_type`

(required) The format type. DOCUMENT format is for record contents that are PDFs or TIFFs. IMAGE format is for record contents that are JPEGs or PNGs. TEXT format is for record contents that are TXT files.

Allowed values are: 'DOCUMENT', 'IMAGE', 'TEXT'

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_LABEL_NAME_T Type

It represents a label.

Syntax
```

```

Fields

Field Description

`name`

(optional) An unique name for a label within its dataset.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_LABEL_NAME_TBL Type

Nested table type of dbms_cloud_oci_data_labeling_service_dataplane_label_name_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_LABEL_SET_T Type

An ordered collection of labels that are unique by name.

Syntax
```

```

Fields

Field Description

`items`

(optional) An ordered collection of labels that are unique by name.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_INITIAL_RECORD_GENERATION_CONFIGURATION_T Type

The initial generate records configuration. It generates records from the dataset's source.

Syntax
```

```

Fields

Field Description

`limit`

(optional) The maximum number of records to generate.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_IMPORT_FORMAT_T Type

File format details used for importing dataset

Syntax
```

```

Fields

Field Description

`name`

(required) Name of import format

Allowed values are: 'JSONL_CONSOLIDATED', 'JSONL_COMPACT_PLUS_CONTENT', 'CONLL', 'SPACY', 'COCO', 'YOLO', 'PASCAL_VOC'

`version`

(optional) Version of import format

Allowed values are: 'V2003', 'V5'

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_IMPORT_METADATA_PATH_T Type

Object storage path for the metadata file

Syntax
```

```

Fields

Field Description

`source_type`

(required) The type of data source. OBJECT_STORAGE - The source details for an object storage bucket.

Allowed values are: 'OBJECT_STORAGE'

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_INITIAL_IMPORT_DATASET_CONFIGURATION_T Type

Initial import dataset configuration. Allows user to create dataset from existing dataset files.

Syntax
```

```

Fields

Field Description

`import_format`

(required)

`import_metadata_path`

(required)

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_DATASET_T Type

A dataset is a logical collection of records. The dataset contains all the information necessary to describe a record's source, format, the type of annotations allowed for the record, and the labels allowed on annotations.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the Dataset.

`display_name`

(optional) A user-friendly display name for the resource.

`compartment_id`

(required) The OCID of the compartment of the resource.

`description`

(optional) A user provided description of the dataset

`time_created`

(required) The date and time the resource was created, in the timestamp format defined by RFC3339.

`time_updated`

(required) The date and time the resource was last updated, in the timestamp format defined by RFC3339.

`lifecycle_state`

(required) The state of a dataset. CREATING - The dataset is being created. It will transition to ACTIVE when it is ready for labeling. ACTIVE - The dataset is ready for labeling. UPDATING - The dataset is being updated. It and its related resources may be unavailable for other updates until it returns to ACTIVE. NEEDS_ATTENTION - A dataset updation operation has failed due to validation or other errors and needs attention. DELETING - The dataset and its related resources are being deleted. DELETED - The dataset has been deleted and is no longer available. FAILED - The dataset has failed due to validation or other errors.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'NEEDS_ATTENTION', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in FAILED or NEEDS_ATTENTION state.

`lifecycle_substate`

(optional) The sub-state of the dataset. IMPORT_DATASET - The dataset is being imported.

Allowed values are: 'IMPORT_DATASET'

`annotation_format`

(required) The annotation format name required for labeling records.

`dataset_source_details`

(required)

`dataset_format_details`

(required)

`label_set`

(required)

`initial_record_generation_configuration`

(optional)

`initial_import_dataset_configuration`

(optional)

`labeling_instructions`

(optional) The labeling instructions for human labelers in rich text format

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) The defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) The usage of system tag keys. These predefined keys are scoped to namespaces. For example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`additional_properties`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_TEXT_FILE_TYPE_METADATA_T Type

Metadata for files with text content.

Syntax
```

```

Fields

Field Description

`format_type`

(required) It defines the format type of text files.

Allowed values are: 'DELIMITED'

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_DELIMITED_FILE_TYPE_METADATA_T Type

Metadata of delimited files.

Syntax
```

```

`dbms_cloud_oci_data_labeling_service_dataplane_delimited_file_type_metadata_t`is a subtype of the`dbms_cloud_oci_data_labeling_service_dataplane_text_file_type_metadata_t`type.

Fields

Field Description

`column_name`

(optional) The name of a selected column.

`column_index`

(required) The index of a selected column. This is a zero-based index.

`column_delimiter`

(optional) A column delimiter

`line_delimiter`

(optional) A line delimiter.

`escape_character`

(optional) An escape character.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_DOCUMENT_DATASET_FORMAT_DETAILS_T Type

It indicates the dataset is comprised of document files. It is open for further configurability.

Syntax
```

```

`dbms_cloud_oci_data_labeling_service_dataplane_document_dataset_format_details_t`is a subtype of the`dbms_cloud_oci_data_labeling_service_dataplane_dataset_format_details_t`type.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_DOCUMENT_ENTITY_METADATA_T Type

This is dedicated Entity to store Document related info.

Syntax
```

```

Fields

Field Description

`page_number`

(required) This stores page number of document.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_DOCUMENT_METADATA_T Type

Collection of metadata related to document record.

Syntax
```

```

`dbms_cloud_oci_data_labeling_service_dataplane_document_metadata_t`is a subtype of the`dbms_cloud_oci_data_labeling_service_dataplane_record_metadata_t`type.

Fields

Field Description

`job_id`

(optional) Job id ocid of OCR batch call.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_ERROR_T Type

Error Information.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error. It is for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_LABEL_TBL Type

Nested table type of dbms_cloud_oci_data_labeling_service_dataplane_label_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_GENERIC_ENTITY_T Type

This is an extensible entity type for users, and the base entity type for some annotation formats.

Syntax
```

```

`dbms_cloud_oci_data_labeling_service_dataplane_generic_entity_t`is a subtype of the`dbms_cloud_oci_data_labeling_service_dataplane_entity_t`type.

Fields

Field Description

`document_entity_metadata`

(optional)

`labels`

(required) A collection of label entities.

`extended_metadata`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_IMAGE_DATASET_FORMAT_DETAILS_T Type

It indicates the dataset is comprised of images.

Syntax
```

```

`dbms_cloud_oci_data_labeling_service_dataplane_image_dataset_format_details_t`is a subtype of the`dbms_cloud_oci_data_labeling_service_dataplane_dataset_format_details_t`type.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_IMAGE_METADATA_T Type

Collection of metadata related to image record.

Syntax
```

```

`dbms_cloud_oci_data_labeling_service_dataplane_image_metadata_t`is a subtype of the`dbms_cloud_oci_data_labeling_service_dataplane_record_metadata_t`type.

Fields

Field Description

`height`

(optional) Height of the image record.

`width`

(optional) Width of the image record.

`depth`

(optional) Depth of the image record.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_IMAGE_OBJECT_SELECTION_ENTITY_T Type

This lets the labeler specify a series of coordinates in the image to represent an object and apply labels to it. The coordinates are connected in the order that they are provided. The last coordinate in the array is connected to the first coordinate.

Syntax
```

```

`dbms_cloud_oci_data_labeling_service_dataplane_image_object_selection_entity_t`is a subtype of the`dbms_cloud_oci_data_labeling_service_dataplane_entity_t`type.

Fields

Field Description

`labels`

(required) A collection of label entities.

`bounding_polygon`

(required)

`extended_metadata`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_KEY_VALUE_SELECTION_ENTITY_T Type

This allows the labeler to apply label the highlighted text from OCR, this includes labelled and unlabelled data.

Syntax
```

```

`dbms_cloud_oci_data_labeling_service_dataplane_key_value_selection_entity_t`is a subtype of the`dbms_cloud_oci_data_labeling_service_dataplane_entity_t`type.

Fields

Field Description

`text`

(required) Entity Name.

`labels`

(optional) A collection of label entities.

`bounding_polygon`

(required)

`rotation`

(optional) Integer value.

`confidence`

(required) float value, score from OCR.

`page_number`

(optional) Integer value.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_OBJECT_STORAGE_DATASET_SOURCE_DETAILS_T Type

Specifies the dataset location in object storage. This requires that all records are in this bucket, and under this prefix. We do not support a dataset with objects in arbitrary locations across buckets or prefixes.

Syntax
```

```

`dbms_cloud_oci_data_labeling_service_dataplane_object_storage_dataset_source_details_t`is a subtype of the`dbms_cloud_oci_data_labeling_service_dataplane_dataset_source_details_t`type.

Fields

Field Description

`namespace`

(required) The namespace of the bucket that contains the dataset data source.

`bucket`

(required) The object storage bucket that contains the dataset data source.

`prefix`

(optional) A common path prefix shared by the objects that make up the dataset. Except for the CSV file type, records are not generated for the objects whose names exactly match with the prefix.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_OBJECT_STORAGE_IMPORT_METADATA_PATH_T Type

Object Storage details for import metadata path.

Syntax
```

```

`dbms_cloud_oci_data_labeling_service_dataplane_object_storage_import_metadata_path_t`is a subtype of the`dbms_cloud_oci_data_labeling_service_dataplane_import_metadata_path_t`type.

Fields

Field Description

`namespace`

(required) Bucket namespace name

`bucket`

(required) Bucket name

`path`

(required) Path for the metadata file.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_SOURCE_DETAILS_T Type

The source information is a polymorphic entity. It captures the details of data used for record creation. The discriminator type must match the dataset's source type. The convention is enforced by the API.

Syntax
```

```

Fields

Field Description

`source_type`

(required) The type of data source. OBJECT_STORAGE - The source details for an object storage bucket.

Allowed values are: 'OBJECT_STORAGE'

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_OBJECT_STORAGE_SOURCE_DETAILS_T Type

Object Storage Source Details.

Syntax
```

```

`dbms_cloud_oci_data_labeling_service_dataplane_object_storage_source_details_t`is a subtype of the`dbms_cloud_oci_data_labeling_service_dataplane_source_details_t`type.

Fields

Field Description

`relative_path`

(required) The path relative to the prefix specified in the dataset source details (file name).

`path`

(required) The full path of the file this record belongs to.

`offset`

(optional) The offset into the file containing the content.

`length`

(optional) The length from the offset into the file containing the content.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_RECORD_T Type

A record represents an entry in a dataset that needs labeling.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the record.

`name`

(required) The name is created by the user. It is unique and immutable.

`time_created`

(required) The date and time the resource was created, in the timestamp format defined by RFC3339.

`time_updated`

(required) The date and time the resource was updated, in the timestamp format defined by RFC3339.

`dataset_id`

(required) The OCID of the dataset to associate the record with.

`compartment_id`

(required) The OCID of the compartment for the task.

`source_details`

(required)

`is_labeled`

(required) Whether or not the record has been labeled and has associated annotations.

`lifecycle_state`

(required) The lifecycle state of the record. ACTIVE - The record is active and ready for labeling. INACTIVE - The record has been marked as inactive and should not be used for labeling. DELETED - The record has been deleted and is no longer available for labeling.

Allowed values are: 'ACTIVE', 'INACTIVE', 'DELETED'

`record_metadata`

(optional)

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) The defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_RECORD_AGGREGATION_DIMENSIONS_T Type

The dimensions to summarize record information for a given dataset.

Syntax
```

```

Fields

Field Description

`is_labeled`

(optional) Whether or not the record has been labeled and has associated annotations.

`annotation_label_contains`

(optional) Whether or not the annotation contains a label.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_RECORD_ANALYTICS_AGGREGATION_T Type

Aggregation entities are required by the API consistency guidelines for API Consistency Guidelines#AnalyticsAPIs. These are used to summarize record information for a given dataset and are used to populate UI elements. Aggregations need to have the fields that identify the exact scope that they're summarizing. Any filters applied to the list API, have to show up in the aggregation.

Syntax
```

```

Fields

Field Description

`l_count`

(required) the count of the matching results

`dimensions`

(optional)

`dataset_id`

(required) ocid of the dataset the annotation belongs to

`compartment_id`

(required) ocid of the compartment the records

`lifecycle_state`

(optional) Describes the lifecycle state.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_RECORD_ANALYTICS_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_data_labeling_service_dataplane_record_analytics_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_RECORD_ANALYTICS_AGGREGATION_COLLECTION_T Type

Collection of records aggregated.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of record entities.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_RECORD_SUMMARY_T Type

A record summary is the representation returned in list views. It is usually a subset of the full record entity and should not contain any potentially sensitive information.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the record.

`name`

(required) The name is automatically assigned by the service. It is unique and immutable

`time_created`

(required) The date and time the resource was created, in the timestamp format defined by RFC3339.

`time_updated`

(required) The date and time the resource was updated, in the timestamp format defined by RFC3339.

`dataset_id`

(required) The OCID of the dataset to associate the record with.

`compartment_id`

(required) The OCID of the compartment for the task.

`is_labeled`

(required) Whether or not the record has been labeled and has associated annotations.

`lifecycle_state`

(required) Describes the lifecycle state.

`record_metadata`

(optional)

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) The defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_RECORD_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_data_labeling_service_dataplane_record_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_RECORD_COLLECTION_T Type

The results of a record search. It contains RecordSummary items and other data.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of records.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_TEXT_DATASET_FORMAT_DETAILS_T Type

It indicates the dataset is comprised of TXT files.

Syntax
```

```

`dbms_cloud_oci_data_labeling_service_dataplane_text_dataset_format_details_t`is a subtype of the`dbms_cloud_oci_data_labeling_service_dataplane_dataset_format_details_t`type.

Fields

Field Description

`text_file_type_metadata`

(optional)

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_TEXT_METADATA_T Type

Collection of metadata related to text record.

Syntax
```

```

`dbms_cloud_oci_data_labeling_service_dataplane_text_metadata_t`is a subtype of the`dbms_cloud_oci_data_labeling_service_dataplane_record_metadata_t`type.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_TEXT_SPAN_T Type

A wrapper class for offset and length, which together, represent a span of text in a text document.

Syntax
```

```

Fields

Field Description

`offset`

(optional) The offset of the selected text within the entire text.

`length`

(optional) The length of the selected text.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_TEXT_SELECTION_ENTITY_T Type

This lets the labeler highlight text, by specifying an offset and a length, and apply labels to it.

Syntax
```

```

`dbms_cloud_oci_data_labeling_service_dataplane_text_selection_entity_t`is a subtype of the`dbms_cloud_oci_data_labeling_service_dataplane_entity_t`type.

Fields

Field Description

`labels`

(required) A collection of label entities.

`text_span`

(required)

`extended_metadata`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_UPDATE_ANNOTATION_DETAILS_T Type

This is the payload sent in the CreateAnnotation operation. It contains all the information required for a user to create an annotation for a record.

Syntax
```

```

Fields

Field Description

`entities`

(optional) The entity types are validated against the dataset to ensure consistency.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) The defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_UPDATE_RECORD_DETAILS_T Type

The details of the tags that is updated.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) The defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`record_metadata`

(optional)

- [Data Labeling Service Dataplane Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-D8C26A58-EE14-430F-B91A-89F3E474C592)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-C4D343DD-72A8-4262-ACE6-2191A46246BA)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_ENTITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-956CA40F-68F7-42F9-B497-A22B98F57638)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_ENTITY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-274A22EC-791F-43D2-BD48-187E27ABD48A)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_ANNOTATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-41B6F70C-54FA-4E42-8D52-4FC7DAC0CA80)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_LABEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-04ACE79F-8D65-4FB5-A9A0-5D3A6056C439)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_ANNOTATION_AGGREGATION_DIMENSIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-93CF4D54-24F6-4CD4-B03B-983028C6D575)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_ANNOTATION_ANALYTICS_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-BAFC9362-86CF-4007-8139-7C3C9C3E317D)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_ANNOTATION_ANALYTICS_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-2498E41A-ECDE-4275-99BF-F5D09BA0D63D)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_ANNOTATION_ANALYTICS_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-3B414908-714F-4B8A-AED3-08D4FB74D197)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_ANNOTATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-41DD0572-16EE-4F8E-A2B0-2DE226BF2DFE)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_ANNOTATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-242D4E6D-155E-4F8D-8C44-5AD0044B5D02)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_ANNOTATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-F6D1E129-519B-4F03-81DA-B2911AA8E0B2)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_NORMALIZED_VERTEX_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-7E5B0A78-72E7-4980-8972-8C4E0C7044CA)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_NORMALIZED_VERTEX_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-91FC076D-9EE2-4EA3-8FE0-BEBB1B707D27)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_BOUNDING_POLYGON_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-9406F387-E330-4498-9EDD-BAB15375E953)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_CREATE_ANNOTATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-D9B9B6AF-D45C-4B03-B592-EC326C7D4DEE)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_CREATE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-F9CC3997-5802-495A-AC61-CB2E74D09CDF)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_CREATE_OBJECT_STORAGE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-C579E691-D4C7-4B82-99DA-BD5471EFA6B2)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_RECORD_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-7B471D8B-61B4-41B0-9DB8-DFFF065737C0)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_CREATE_RECORD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-2CECE47A-6A64-4681-BD93-D2EADE0914C9)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_DATASET_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-368407CF-0699-4E3F-AF3D-6353BFC4EF98)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_DATASET_FORMAT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-1287B1D8-FBBE-4908-9D2E-7255628E32D7)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_LABEL_NAME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-CAE6FBA9-060F-4F4B-AD97-BC0487C5A408)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_LABEL_NAME_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-9FE4204C-DDFF-438F-82DF-6B3F0C3CA0A1)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_LABEL_SET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-23BA8689-6182-4482-ACE9-FEA865EED119)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_INITIAL_RECORD_GENERATION_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-0DC6D600-2496-4B4B-81D8-EE7C2A47A4B3)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_IMPORT_FORMAT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-4EBF296C-8988-4D32-9844-A667863F93DB)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_IMPORT_METADATA_PATH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-FE135081-30D2-4A3B-9667-5FE237759508)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_INITIAL_IMPORT_DATASET_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-B1ACE2F4-AE59-4AC8-B9EC-F56B5BF4AE91)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_DATASET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-ABD82E33-48CF-4795-9B48-B7D664C3CF1E)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_TEXT_FILE_TYPE_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-05EF21BF-15C2-482D-9681-17B1A093443B)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_DELIMITED_FILE_TYPE_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-006F65B5-12E8-469E-8B31-55B7D442826A)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_DOCUMENT_DATASET_FORMAT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-9BE99733-ACAC-45A2-9A44-758F269E22E1)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_DOCUMENT_ENTITY_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-9FC92BD3-313D-4674-9718-03DF6BDC0B86)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_DOCUMENT_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-3438A1B1-D86A-4F4D-88AE-A8C620973400)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-D733BE7E-4331-43A9-8C7F-FEB48A27BFF5)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_LABEL_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-CBCB2050-62A1-48DE-995C-C33069823536)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_GENERIC_ENTITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-2D6013EA-06E1-4F8D-80DE-04B2C2EC20D9)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_IMAGE_DATASET_FORMAT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-1A21263E-741D-41BE-9937-1141712E9D6F)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_IMAGE_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-1191C66D-F24F-4D01-9EC2-8EC7A9043973)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_IMAGE_OBJECT_SELECTION_ENTITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-5231A6DF-1F0C-45A2-AADE-CE8523D5EF24)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_KEY_VALUE_SELECTION_ENTITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-BB4E049D-1636-494C-B833-067EE0EA70DC)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_OBJECT_STORAGE_DATASET_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-8EBF7CB3-0054-4F9A-B265-89775C12FB9C)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_OBJECT_STORAGE_IMPORT_METADATA_PATH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-9DFC6579-436B-412D-ACF1-5F20F3C4AAD2)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-F94EC956-6A0D-43C9-B494-7BDC062CDC5A)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_OBJECT_STORAGE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-DC221EA5-D07C-42D1-84C1-2A6E99E7C0D0)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_RECORD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-73CC0114-F4DE-427A-A913-55A237BB1F8A)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_RECORD_AGGREGATION_DIMENSIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-153A9BCF-144C-451B-A223-3914C058985C)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_RECORD_ANALYTICS_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-863D73F1-B1B2-44E0-8CBA-6FF89C439358)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_RECORD_ANALYTICS_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-636F9C53-D84F-467C-A0C7-C44E91DF5CE5)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_RECORD_ANALYTICS_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-AC958942-AC2C-47F8-9595-6C1A780AAA9E)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_RECORD_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-207A21ED-F86E-4D26-A9E6-E49E3CB4EC98)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_RECORD_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-F974A02D-C324-4209-A414-00C287B5C60A)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_RECORD_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-D19AD3DF-7E15-4D99-B569-CECCFFF5BFF9)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_TEXT_DATASET_FORMAT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-BC08A28B-9CB4-44E2-B256-CC19815C32D6)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_TEXT_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-3AF4C7D9-747E-473D-906B-BF3115A5D832)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_TEXT_SPAN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-0D065956-33C6-4F82-A56E-673C2EA97289)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_TEXT_SELECTION_ENTITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-6EA05766-73AD-42D1-99C0-464796354360)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_UPDATE_ANNOTATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-5038A29C-B8A1-41C5-998B-49ACD49D1510)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATAPLANE_UPDATE_RECORD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_dataplane_t.html#ADSDK-GUID-033B0231-8D1F-485C-A69C-E2D9F41AD783)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
