# Data Labeling Service Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html
- Fetched: 2026-09-05 19:02 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#dcoc-content-body)

## Data Labeling Service Common Types

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_LABEL_T Type

It represents a label.

Syntax
```

```

Fields

Field Description

`name`

(optional) An unique name for a label within its dataset.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_LABEL_TBL Type

Nested table type of dbms_cloud_oci_data_labeling_service_label_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_LABEL_SET_T Type

An ordered collection of labels that are unique by name.

Syntax
```

```

Fields

Field Description

`items`

(optional) An ordered collection of labels that are unique by name.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_ADD_DATASET_LABELS_DETAILS_T Type

Adds a subset of Labels to the Dataset's LabelSet. This LabelSet will be merged with the current Dataset's LabelSet. Requests with duplicate Labels will be rejected.

Syntax
```

```

Fields

Field Description

`label_set`

(optional)

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_ANNOTATION_FORMAT_T Type

annotation format

Syntax
```

```

Fields

Field Description

`name`

(required) A unique name for the target AnnotationFormat for the Dataset.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_ANNOTATION_FORMAT_SUMMARY_T Type

annotation format summary

Syntax
```

```

Fields

Field Description

`name`

(required) A unique name for the target AnnotationFormat for the Dataset.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_ANNOTATION_FORMAT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_data_labeling_service_annotation_format_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_ANNOTATION_FORMAT_COLLECTION_T Type

Collection of annotation formats.

Syntax
```

```

Fields

Field Description

`items`

(required) List of annotation formats.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_CHANGE_DATASET_COMPARTMENT_DETAILS_T Type

The payload sent to the Change Dataset compartment operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment where the resource should be moved.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATASET_SOURCE_DETAILS_T Type

This allows the customer to specify the source of the dataset.

Syntax
```

```

Fields

Field Description

`source_type`

(required) The source type. OBJECT_STORAGE allows the user to describe where in object storage the dataset is.

Allowed values are: 'OBJECT_STORAGE'

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATASET_FORMAT_DETAILS_T Type

It specifies how to process the data. Supported formats include DOCUMENT, IMAGE, and TEXT.

Syntax
```

```

Fields

Field Description

`format_type`

(required) The format type. DOCUMENT format is for record contents that are PDFs or TIFFs. IMAGE format is for record contents that are JPEGs or PNGs. TEXT format is for record contents that are TXT files.

Allowed values are: 'DOCUMENT', 'IMAGE', 'TEXT'

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_INITIAL_RECORD_GENERATION_CONFIGURATION_T Type

The initial generate records configuration. It generates records from the dataset's source.

Syntax
```

```

Fields

Field Description

`limit`

(optional) The maximum number of records to generate.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_IMPORT_FORMAT_T Type

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

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_IMPORT_METADATA_PATH_T Type

Object storage path for the metadata file

Syntax
```

```

Fields

Field Description

`source_type`

(required) The type of data source. OBJECT_STORAGE - The source details for an object storage bucket.

Allowed values are: 'OBJECT_STORAGE'

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_INITIAL_IMPORT_DATASET_CONFIGURATION_T Type

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

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_CREATE_DATASET_DETAILS_T Type

Parameters needed to create a new Dataset. A Dataset allows a user to describe the data source that provides the Records and how Annotations should be applied to the Records.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name for the resource.

`description`

(optional) A user provided description of the dataset

`compartment_id`

(required) The OCID of the compartment of the resource.

`annotation_format`

(required) The annotation format name required for labeling records.

`dataset_source_details`

(required)

`dataset_format_details`

(required)

`initial_record_generation_configuration`

(optional)

`initial_import_dataset_configuration`

(optional)

`label_set`

(required)

`labeling_instructions`

(optional) The labeling instructions for human labelers in rich text format

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) The defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATASET_T Type

A dataset is a logical collection of records. The dataset contains all the information necessary to describe a record's source, format, type of annotations allowed on these records, and labels allowed on annotations.

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

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATASET_SUMMARY_T Type

A dataset summary is the representation returned in list views. It is usually a subset of the full dataset entity and should not contain any potentially sensitive information.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the Dataset

`display_name`

(optional) A user-friendly display name for the resource.

`compartment_id`

(required) Compartment Identifier

`time_created`

(required) The time the the Dataset was created. An RFC3339 formatted datetime string

`time_updated`

(required) The date and time the resource was last updated, in the timestamp format defined by RFC3339.

`lifecycle_state`

(required) The state of a Dataset.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`annotation_format`

(required) The annotation format name required for labeling records.

`dataset_format_details`

(required)

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) The defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) The usage of system tag keys. These predefined keys are scoped to namespaces. For example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATASET_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_data_labeling_service_dataset_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATASET_COLLECTION_T Type

Results of a dataset list operation. Contains DatasetSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of datasets.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_TEXT_FILE_TYPE_METADATA_T Type

Metadata for files with text content.

Syntax
```

```

Fields

Field Description

`format_type`

(required) It defines the format type of text files.

Allowed values are: 'DELIMITED'

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DELIMITED_FILE_TYPE_METADATA_T Type

Metadata of delimited files.

Syntax
```

```

`dbms_cloud_oci_data_labeling_service_delimited_file_type_metadata_t`is a subtype of the`dbms_cloud_oci_data_labeling_service_text_file_type_metadata_t`type.

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

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DOCUMENT_DATASET_FORMAT_DETAILS_T Type

It indicates the dataset is comprised of document files. It is open for further configurability.

Syntax
```

```

`dbms_cloud_oci_data_labeling_service_document_dataset_format_details_t`is a subtype of the`dbms_cloud_oci_data_labeling_service_dataset_format_details_t`type.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_ERROR_T Type

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

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_EXPORT_FORMAT_T Type

Specifies the export format to be used for exporting snapshot.

Syntax
```

```

Fields

Field Description

`name`

(optional) Name of export format.

Allowed values are: 'JSONL', 'JSONL_CONSOLIDATED', 'CONLL', 'SPACY', 'COCO', 'YOLO', 'PASCAL_VOC', 'JSONL_COMPACT_PLUS_CONTENT'

`version`

(optional) Version of export format.

Allowed values are: 'V2003', 'V5'

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_GENERATE_DATASET_RECORDS_DETAILS_T Type

Generate Records from the Dataset's source.

Syntax
```

```

Fields

Field Description

`limit`

(optional) the maximum number of records to generate.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_IMAGE_DATASET_FORMAT_DETAILS_T Type

It indicates the dataset is comprised of images.

Syntax
```

```

`dbms_cloud_oci_data_labeling_service_image_dataset_format_details_t`is a subtype of the`dbms_cloud_oci_data_labeling_service_dataset_format_details_t`type.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_IMPORT_PRE_ANNOTATED_DATA_DETAILS_T Type

Allows user to import dataset labels, records and annotations from dataset files

Syntax
```

```

Fields

Field Description

`import_format`

(optional)

`import_metadata_path`

(optional)

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_OBJECT_STORAGE_IMPORT_METADATA_PATH_T Type

Object Storage details for import metadata path.

Syntax
```

```

`dbms_cloud_oci_data_labeling_service_object_storage_import_metadata_path_t`is a subtype of the`dbms_cloud_oci_data_labeling_service_import_metadata_path_t`type.

Fields

Field Description

`namespace`

(required) Bucket namespace name

`bucket`

(required) Bucket name

`path`

(required) Path for the metadata file.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_SNAPSHOT_EXPORT_DETAILS_T Type

Specifies where to output the export.

Syntax
```

```

Fields

Field Description

`export_type`

(required) The target destination for the snapshot. Using OBJECT_STORAGE means the snapshot will be written to Object Storage.

Allowed values are: 'OBJECT_STORAGE'

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_OBJECT_STORAGE_SNAPSHOT_EXPORT_DETAILS_T Type

Specifies where to output the export in Object Storage.

Syntax
```

```

`dbms_cloud_oci_data_labeling_service_object_storage_snapshot_export_details_t`is a subtype of the`dbms_cloud_oci_data_labeling_service_snapshot_export_details_t`type.

Fields

Field Description

`namespace`

(required) Bucket namespace name

`bucket`

(required) Bucket name

`prefix`

(optional) Object path prefix to put snapshot file(s)

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_OBJECT_STORAGE_SOURCE_DETAILS_T Type

Specifies the dataset location in object storage. This requires that all records are in this bucket, and under this prefix. We do not support a dataset with objects in arbitrary locations across buckets or prefixes.

Syntax
```

```

`dbms_cloud_oci_data_labeling_service_object_storage_source_details_t`is a subtype of the`dbms_cloud_oci_data_labeling_service_dataset_source_details_t`type.

Fields

Field Description

`namespace`

(required) The namespace of the bucket that contains the dataset data source.

`bucket`

(required) The object storage bucket that contains the dataset data source.

`prefix`

(optional) A common path prefix shared by the objects that make up the dataset. Except for the CSV file type, records are not generated for the objects whose names exactly match with the prefix.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_REMOVE_DATASET_LABELS_DETAILS_T Type

Removes a subset of Labels from the Dataset's LabelSet. This LabelSet will be subtracted from the current Dataset's LabelSet. Requests with non-existent Labels will be rejected.

Syntax
```

```

Fields

Field Description

`label_set`

(optional)

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_RENAME_DATASET_LABELS_DETAILS_T Type

Renames a subset of Labels in the Dataset's LabelSet. The Labels in the source LabelSet will be replaced with the Labels in the target LabelSet. Labels are correlated by index, i.e. the first Label in the source LabelSet will be replaced by the first Label in the target LabelSet. If the size of the source and target LabelSets are not equal, the request will be rejected.

Syntax
```

```

Fields

Field Description

`source_label_set`

(optional)

`target_label_set`

(optional)

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_SNAPSHOT_DATASET_DETAILS_T Type

Allows outputting the latest records paired with annotations and write them to object storage.

Syntax
```

```

Fields

Field Description

`are_annotations_included`

(required) Whether annotations are to be included in the export dataset digest.

`are_unannotated_records_included`

(required) Whether to include records that have yet to be annotated in the export dataset digest.

`export_details`

(required)

`export_format`

(optional)

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_TEXT_DATASET_FORMAT_DETAILS_T Type

It indicates the dataset is comprised of TXT files.

Syntax
```

```

`dbms_cloud_oci_data_labeling_service_text_dataset_format_details_t`is a subtype of the`dbms_cloud_oci_data_labeling_service_dataset_format_details_t`type.

Fields

Field Description

`text_file_type_metadata`

(optional)

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_UPDATE_DATASET_DETAILS_T Type

Once the Dataset is defined, it's largely immutable from a metadata perspective. The records found in the data source itself, may change over time.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name for the resource.

`description`

(optional) A user provided description of the dataset

`labeling_instructions`

(optional) The labeling instructions for human labelers in rich text format

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) The defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_WORK_REQUEST_RESOURCE_T Type

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

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'WRITTEN', 'RELATED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata

`metadata`

(optional) Additional information that helps to explain the resource.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_data_labeling_service_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_WORK_REQUEST_T Type

A description of workrequest status

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_DATASET', 'DELETE_DATASET', 'MOVE_DATASET', 'GENERATE_DATASET_RECORDS', 'SNAPSHOT_DATASET', 'ADD_DATASET_LABELS', 'REMOVE_DATASET_LABELS', 'RENAME_DATASET_LABELS', 'IMPORT_DATASET'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'FAILED'

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

(optional) The date and time the request was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_WORK_REQUEST_ERROR_T Type

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

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_data_labeling_service_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestError objects.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_WORK_REQUEST_LOG_ENTRY_T Type

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

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_data_labeling_service_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a workRequestLog search. Contains both workRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestLogEntries.

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_DATASET', 'DELETE_DATASET', 'MOVE_DATASET', 'GENERATE_DATASET_RECORDS', 'SNAPSHOT_DATASET', 'ADD_DATASET_LABELS', 'REMOVE_DATASET_LABELS', 'RENAME_DATASET_LABELS', 'IMPORT_DATASET'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'FAILED'

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

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_data_labeling_service_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestSummary objects.

- [Data Labeling Service Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-5C5D68EA-C4FF-41E9-A300-53999700B000)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-976F113B-8394-4029-96D6-1281C5C3CD48)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_LABEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-86CA1D15-8DF1-4B1B-9BD2-455C86ED4D1A)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_LABEL_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-3779FCF1-6476-4957-8310-138DF64DE2A9)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_LABEL_SET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-CFD214C0-EDAE-4354-9442-0181D7CD91F5)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_ADD_DATASET_LABELS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-0DFC1E29-FA99-47AC-8279-A2D36ED24E13)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_ANNOTATION_FORMAT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-E0A586AC-30CE-4FE5-9738-575FB4FF408C)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_ANNOTATION_FORMAT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-BDD57AE7-613E-4E6E-B1CE-14B9C7571A9D)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_ANNOTATION_FORMAT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-DDA02683-3B68-4779-B112-33A68A9BC98B)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_ANNOTATION_FORMAT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-A123A703-63F7-4FD3-BF08-EDF796C255C1)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_CHANGE_DATASET_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-CD4068E3-2757-45DB-A880-F6566FF79CB5)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATASET_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-F7B009DB-A8E5-4393-94A2-C5A20D2E9B36)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATASET_FORMAT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-A7445AAD-F57E-4CD3-9278-45EAE75A3E5C)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_INITIAL_RECORD_GENERATION_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-CD345C1D-33DD-4CDD-AB67-E133D4C525D1)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_IMPORT_FORMAT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-FA8D935E-CA36-4AD1-B7FB-57C223CD250A)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_IMPORT_METADATA_PATH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-7A68253C-C614-4397-B489-CF1EDA397E57)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_INITIAL_IMPORT_DATASET_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-9BEE8A60-F92C-4021-BEFE-B35F7983247D)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_CREATE_DATASET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-3C3A5772-623C-4C4A-B295-8B040D9A2492)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATASET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-652822DC-15BB-493F-BC72-48578A23FD5F)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATASET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-3D5E10A4-12F6-41BF-97C3-49940FB9F69D)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATASET_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-769C024C-D30C-4927-8856-457112A07062)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DATASET_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-D215948B-4A7C-42D8-AB85-70B498F3B87E)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_TEXT_FILE_TYPE_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-664F746F-11AF-4548-9E2C-71BC62AD5670)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DELIMITED_FILE_TYPE_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-9EB0AEA7-D117-411F-BD98-2BFB0B19D3C9)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_DOCUMENT_DATASET_FORMAT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-0A99DC88-072B-44B1-8CD5-4E3FF40E63CB)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-D671E450-1F66-4A1C-A0F6-139F3112ECEF)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_EXPORT_FORMAT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-DBC30EF7-8280-4992-B6BA-CA1A8A2E85BA)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_GENERATE_DATASET_RECORDS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-F15009FD-6C6C-42E2-8DE0-FF30720ED718)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_IMAGE_DATASET_FORMAT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-D0A96425-BDA4-438F-A138-8CDEDDD6B42E)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_IMPORT_PRE_ANNOTATED_DATA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-2FC9FE67-6F23-499D-8748-9E6D5DE1C2A8)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_OBJECT_STORAGE_IMPORT_METADATA_PATH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-0DA5AAB2-F0F1-4BF5-B372-20FB798AB0D6)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_SNAPSHOT_EXPORT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-C5EAB6EC-9FAF-4966-89CC-3083FB77E30A)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_OBJECT_STORAGE_SNAPSHOT_EXPORT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-5937E4EB-C0CF-45DE-8309-D8A0D08606E1)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_OBJECT_STORAGE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-4510F746-8175-47B6-8FCD-623BCD6FE32A)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_REMOVE_DATASET_LABELS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-7E17AA73-BF2C-48B9-8840-5CD916D0875A)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_RENAME_DATASET_LABELS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-2A595958-8E47-443E-9B6F-4B25BA4FDD80)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_SNAPSHOT_DATASET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-B3C374A7-4707-411A-943B-6B5FCF4D694E)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_TEXT_DATASET_FORMAT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-628CECE0-1239-49C4-8C06-C7E470E00B5A)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_UPDATE_DATASET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-37EB85D0-A513-4EA5-B398-15E34B931C1B)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-365CC9EF-385A-4095-9BCD-788352C598AF)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-90E6ABF8-84F4-46C5-A50C-FE53A2FC26B6)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-9E0E1F41-E1E6-47B7-B655-9869230013EF)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-A6D7CE1A-CBB8-4A4A-89BB-63EA28694EE2)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-7BC9EB58-9FCD-4B6C-9783-C05C9369FE3D)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-A75B5B5C-B767-46EF-9235-1E60FD8047C9)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-173B1365-4989-46D0-A211-00C5EEC0DEF7)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-7EB6DACE-0638-4A92-824A-5AF019668936)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-876357AE-F70F-4A09-A15B-78256A5529AC)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-FF16A04A-3681-4252-9170-83D4B2880B3F)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-4F3392B7-9257-4BBD-BEFD-96E443F5C62E)
- [DBMS_CLOUD_OCI_DATA_LABELING_SERVICE_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/data_labeling_service_t.html#ADSDK-GUID-40815A81-FF08-460F-8497-79F80992ED5C)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
