# AI Vision Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html
- Fetched: 2026-09-05 19:00 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#dcoc-content-body)

## AI Vision Common Types

### DBMS_CLOUD_OCI_AI_VISION_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_DOCUMENT_FEATURE_T Type

The type of document analysis.

Syntax
```

```

Fields

Field Description

`feature_type`

(required) The type of document analysis requested. The allowed values are: - `LANGUAGE_CLASSIFICATION`: Detect the language. - `TEXT_DETECTION`: Recognize text. - `TABLE_DETECTION`: Detect and extract data in tables. - `KEY_VALUE_DETECTION`: Extract form fields. - `DOCUMENT_CLASSIFICATION`: Identify the type of document.

Allowed values are: 'LANGUAGE_CLASSIFICATION', 'TEXT_DETECTION', 'TABLE_DETECTION', 'KEY_VALUE_DETECTION', 'DOCUMENT_CLASSIFICATION'

### DBMS_CLOUD_OCI_AI_VISION_DOCUMENT_DETAILS_T Type

The details of a document to analyze.

Syntax
```

```

Fields

Field Description

`source`

(required) The location of the document data. The allowed values are: - `INLINE`: The data is included directly in the request payload. - `OBJECT_STORAGE`: The document is in OCI Object Storage.

Allowed values are: 'INLINE', 'OBJECT_STORAGE'

### DBMS_CLOUD_OCI_AI_VISION_OUTPUT_LOCATION_T Type

The Object Storage Location.

Syntax
```

```

Fields

Field Description

`namespace_name`

(required) The Object Storage namespace.

`bucket_name`

(required) The Object Storage bucket name.

`prefix`

(required) The Object Storage folder name.

### DBMS_CLOUD_OCI_AI_VISION_DOCUMENT_FEATURE_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_document_feature_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_ANALYZE_DOCUMENT_DETAILS_T Type

The details of how to analyze a document.

Syntax
```

```

Fields

Field Description

`features`

(required) The types of document analysis requested.

`document`

(required)

`compartment_id`

(optional) The OCID of the compartment that calls the API.

`output_location`

(optional)

`language`

(optional) The document language, abbreviated according to ISO 639-2.

Allowed values are: 'ENG', 'CES', 'DAN', 'NLD', 'FIN', 'FRA', 'DEU', 'ELL', 'HUN', 'ITA', 'NOR', 'POL', 'POR', 'RON', 'RUS', 'SLK', 'SPA', 'SWE', 'TUR', 'ARA', 'CHI_SIM', 'HIN', 'JPN', 'KOR', 'OTHERS'

`document_type`

(optional) The document type.

Allowed values are: 'INVOICE', 'RECEIPT', 'RESUME', 'TAX_FORM', 'DRIVER_LICENSE', 'PASSPORT', 'BANK_STATEMENT', 'CHECK', 'PAYSLIP', 'OTHERS'

### DBMS_CLOUD_OCI_AI_VISION_DOCUMENT_METADATA_T Type

The document information.

Syntax
```

```

Fields

Field Description

`page_count`

(required) Teh number of pages in the document.

`mime_type`

(required) The result data format.

### DBMS_CLOUD_OCI_AI_VISION_DIMENSIONS_T Type

The width and height of a page.

Syntax
```

```

Fields

Field Description

`width`

(required) the width of a page.

`height`

(required) The height of a page.

`unit`

(required) The unit of length.

Allowed values are: 'PIXEL', 'INCH'

### DBMS_CLOUD_OCI_AI_VISION_DETECTED_DOCUMENT_TYPE_T Type

The detected document type.

Syntax
```

```

Fields

Field Description

`document_type`

(required) The document type.

`confidence`

(required) The confidence score between 0 and 1.

### DBMS_CLOUD_OCI_AI_VISION_DETECTED_LANGUAGE_T Type

The language detected in a document.

Syntax
```

```

Fields

Field Description

`language_code`

(required) The language of the document, abbreviated according to ISO 639-2.

Allowed values are: 'ENG', 'CES', 'DAN', 'NLD', 'FIN', 'FRA', 'DEU', 'ELL', 'HUN', 'ITA', 'NOR', 'POL', 'POR', 'RON', 'RUS', 'SLK', 'SPA', 'SWE', 'TUR', 'ARA', 'CHI_SIM', 'HIN', 'JPN', 'KOR', 'OTHERS'

`confidence`

(required) The confidence score between 0 and 1.

### DBMS_CLOUD_OCI_AI_VISION_NORMALIZED_VERTEX_T Type

An (x, y) coordinate in the image with dimensions normalized from zero to one. The origin is at top left, with the positive x-axis pointing right and the positive y-axis pointing down. The bottom right corner is at (1, 1).

Syntax
```

```

Fields

Field Description

`x`

(required) The X-axis normalized coordinate.

`y`

(required) The Y-axis normalized coordinate.

### DBMS_CLOUD_OCI_AI_VISION_NORMALIZED_VERTEX_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_normalized_vertex_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_BOUNDING_POLYGON_T Type

The object-bounding polygon box.

Syntax
```

```

Fields

Field Description

`normalized_vertices`

(required) An array of normalized points defining the polygon's perimeter, with an implicit segment between subsequent points and between the first and last point. Rectangles are defined with four points. For example, `[{\"x\": 0, \"y\": 0}, {\"x\": 1, \"y\": 0}, {\"x\": 1, \"y\": 0.5}, {\"x\": 0, \"y\": 0.5}]` represents the top half of an image.

### DBMS_CLOUD_OCI_AI_VISION_WORD_T Type

A single word.

Syntax
```

```

Fields

Field Description

`text`

(required) The string of text characters in the word.

`confidence`

(required) the confidence score between 0 and 1.

`bounding_polygon`

(required)

### DBMS_CLOUD_OCI_AI_VISION_NUMBER_TBL Type

Nested table type of number.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_LINE_T Type

The line of text.

Syntax
```

```

Fields

Field Description

`text`

(required) The text recognized.

`confidence`

(required) The confidence score between 0 and 1.

`bounding_polygon`

(required)

`word_indexes`

(required) The array of words.

### DBMS_CLOUD_OCI_AI_VISION_CELL_T Type

A single cell in a table.

Syntax
```

```

Fields

Field Description

`text`

(required) The text recognized in the cell.

`row_index`

(required) The index of the cell inside the row.

`column_index`

(required) The index of the cell inside the column.

`confidence`

(required) The confidence score between 0 and 1.

`bounding_polygon`

(required)

`word_indexes`

(required) The words detected in the cell.

### DBMS_CLOUD_OCI_AI_VISION_CELL_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_cell_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_TABLE_ROW_T Type

A single row in a table.

Syntax
```

```

Fields

Field Description

`cells`

(required) The cells in the row.

### DBMS_CLOUD_OCI_AI_VISION_TABLE_ROW_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_table_row_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_TABLE_T Type

The table extracted from a document.

Syntax
```

```

Fields

Field Description

`row_count`

(required) The number of rows.

`column_count`

(required) The number of columns.

`header_rows`

(required) The header rows.

`body_rows`

(required) The body rows.

`footer_rows`

(required) the footer rows.

`confidence`

(required) The confidence score between 0 and 1.

`bounding_polygon`

(required)

### DBMS_CLOUD_OCI_AI_VISION_FIELD_LABEL_T Type

The label in a field.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the field label.

`confidence`

(optional) The confidence score between 0 and 1.

### DBMS_CLOUD_OCI_AI_VISION_FIELD_NAME_T Type

The name of a form field.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the field.

`confidence`

(optional) The confidence score between 0 and 1.

`bounding_polygon`

(optional)

`word_indexes`

(optional) The indexes of the words in the field name.

### DBMS_CLOUD_OCI_AI_VISION_FIELD_VALUE_T Type

The value of a form field.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The type of data detected.

Allowed values are: 'STRING', 'DATE', 'TIME', 'PHONE_NUMBER', 'NUMBER', 'INTEGER', 'ARRAY'

`text`

(optional) The detected text of a field.

`confidence`

(required) The confidence score between 0 and 1.

`bounding_polygon`

(required)

`word_indexes`

(required) The indexes of the words in the field value.

### DBMS_CLOUD_OCI_AI_VISION_DOCUMENT_FIELD_T Type

Form field.

Syntax
```

```

Fields

Field Description

`field_type`

(required) The field type.

Allowed values are: 'LINE_ITEM_GROUP', 'LINE_ITEM', 'LINE_ITEM_FIELD', 'KEY_VALUE'

`field_label`

(optional)

`field_name`

(optional)

`field_value`

(required)

### DBMS_CLOUD_OCI_AI_VISION_DETECTED_DOCUMENT_TYPE_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_detected_document_type_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_DETECTED_LANGUAGE_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_detected_language_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_WORD_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_word_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_LINE_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_line_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_TABLE_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_table_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_DOCUMENT_FIELD_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_document_field_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_PAGE_T Type

One page document analysis result.

Syntax
```

```

Fields

Field Description

`page_number`

(required) The document page number.

`dimensions`

(optional)

`detected_document_types`

(optional) An array of detected document types.

`detected_languages`

(optional) An array of detected languages.

`words`

(optional) The words detected on the page.

`lines`

(optional) The lines of text detected on the page.

`tables`

(optional) The tables detected on the page.

`document_fields`

(optional) The form fields detected on the page.

### DBMS_CLOUD_OCI_AI_VISION_PROCESSING_ERROR_T Type

The error in document processing.

Syntax
```

```

Fields

Field Description

`code`

(required) The error code.

`message`

(required) The error message.

### DBMS_CLOUD_OCI_AI_VISION_PAGE_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_page_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_PROCESSING_ERROR_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_processing_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_ANALYZE_DOCUMENT_RESULT_T Type

The document analysis results.

Syntax
```

```

Fields

Field Description

`document_metadata`

(required)

`pages`

(required) The array of a Page.

`detected_document_types`

(optional) An array of detected document types.

`detected_languages`

(optional) An array of detected languages.

`document_classification_model_version`

(optional) The document classification model version.

`language_classification_model_version`

(optional) The document language classification model version.

`text_detection_model_version`

(optional) The document text detection model version.

`key_value_detection_model_version`

(optional) The document keyValue detection model version.

`table_detection_model_version`

(optional) The document table detection model version.

`errors`

(optional) The errors encountered during document analysis.

`searchable_pdf`

(optional) The searchable PDF file that was generated.

### DBMS_CLOUD_OCI_AI_VISION_IMAGE_FEATURE_T Type

The type of image analysis.

Syntax
```

```

Fields

Field Description

`feature_type`

(required) The type of image analysis requested. The allowed values are: - `IMAGE_CLASSIFICATION`: Label the image. - `OBJECT_DETECTION`: Identify objects in the image with bounding boxes. - `TEXT_DETECTION`: Recognize text at the word and line level. - `FACE_DETECTION`: Identify faces in the image with bounding boxes and face landmarks.

Allowed values are: 'IMAGE_CLASSIFICATION', 'OBJECT_DETECTION', 'TEXT_DETECTION', 'FACE_DETECTION'

### DBMS_CLOUD_OCI_AI_VISION_IMAGE_DETAILS_T Type

The details of an image to analyze.

Syntax
```

```

Fields

Field Description

`source`

(required) The location of the image data. The allowed values are: - `INLINE`: The data is included directly in the request payload. - `OBJECT_STORAGE`: The image is in OCI Object Storage.

Allowed values are: 'INLINE', 'OBJECT_STORAGE'

### DBMS_CLOUD_OCI_AI_VISION_IMAGE_FEATURE_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_image_feature_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_ANALYZE_IMAGE_DETAILS_T Type

The details of how to analyze an image.

Syntax
```

```

Fields

Field Description

`features`

(required) The types of image analysis.

`image`

(required)

`compartment_id`

(optional) The OCID of the compartment that calls the API.

### DBMS_CLOUD_OCI_AI_VISION_IMAGE_OBJECT_T Type

The object detected in an image.

Syntax
```

```

Fields

Field Description

`name`

(required) The object category name. Every value returned by the pre-deployed model is in English.

`confidence`

(required) The confidence score, between 0 and 1.

`bounding_polygon`

(required)

### DBMS_CLOUD_OCI_AI_VISION_LABEL_T Type

A label describing an image. Every label returned by the pre-deployed model is in English.

Syntax
```

```

Fields

Field Description

`name`

(required) The classification catagory label name.

`confidence`

(required) The confidence score between 0 and 1.

### DBMS_CLOUD_OCI_AI_VISION_ONTOLOGY_CLASS_T Type

Images and ImageObjects can be labeled with an OntologyClass.

Syntax
```

```

Fields

Field Description

`name`

(required) The label name.

`parent_names`

(optional) The label parents.

`synonym_names`

(optional) The label synonyms.

### DBMS_CLOUD_OCI_AI_VISION_IMAGE_TEXT_T Type

The detected text.

Syntax
```

```

Fields

Field Description

`words`

(required) The words recognized in an image.

`lines`

(required) The lines of text recognized in an image.

### DBMS_CLOUD_OCI_AI_VISION_LANDMARK_T Type

The landmark on the face.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The face landmark type

Allowed values are: 'LEFT_EYE', 'RIGHT_EYE', 'NOSE_TIP', 'LEFT_EDGE_OF_MOUTH', 'RIGHT_EDGE_OF_MOUTH'

`x`

(required) The X-axis normalized coordinate.

`y`

(required) The Y-axis normalized coordinate.

### DBMS_CLOUD_OCI_AI_VISION_LANDMARK_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_landmark_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_FACE_T Type

The detected face.

Syntax
```

```

Fields

Field Description

`confidence`

(required) The confidence score, between 0 and 1.

`bounding_polygon`

(required)

`quality_score`

(required) The quality score of the face detected, between 0 and 1.

`landmarks`

(optional) A point of interest within a face.

### DBMS_CLOUD_OCI_AI_VISION_IMAGE_OBJECT_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_image_object_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_LABEL_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_label_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_ONTOLOGY_CLASS_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_ontology_class_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_FACE_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_face_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_ANALYZE_IMAGE_RESULT_T Type

The image analysis results.

Syntax
```

```

Fields

Field Description

`image_objects`

(optional) The detected objects.

`labels`

(optional) The image classification labels.

`ontology_classes`

(optional) The ontologyClasses of image labels.

`image_text`

(optional)

`detected_faces`

(optional) The detected faces.

`image_classification_model_version`

(optional) The image classification model version.

`object_detection_model_version`

(optional) The object detection model version.

`text_detection_model_version`

(optional) The text detection model version.

`face_detection_model_version`

(optional) The face detection model version.

`errors`

(optional) The errors encountered during image analysis.

### DBMS_CLOUD_OCI_AI_VISION_CHANGE_MODEL_COMPARTMENT_DETAILS_T Type

The compartment the model should be moved to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the model should be moved.

### DBMS_CLOUD_OCI_AI_VISION_CHANGE_PROJECT_COMPARTMENT_DETAILS_T Type

Which compartment the project should be moved to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the project should be moved.

### DBMS_CLOUD_OCI_AI_VISION_INPUT_LOCATION_T Type

The location of the inputs.

Syntax
```

```

Fields

Field Description

`source_type`

(required) The type of input location. The allowed values are: - `OBJECT_LIST_INLINE_INPUT_LOCATION`: A list of object locations in Object Storage.

Allowed values are: 'OBJECT_LIST_INLINE_INPUT_LOCATION'

### DBMS_CLOUD_OCI_AI_VISION_CREATE_DOCUMENT_JOB_DETAILS_T Type

The batch document analysis details.

Syntax
```

```

Fields

Field Description

`input_location`

(required)

`features`

(required) The list of requested document analysis types.

`output_location`

(required)

`compartment_id`

(optional) The compartment identifier from the requester.

`display_name`

(optional) The document job display name.

`language`

(optional) The language of the document, abbreviated according to ISO 639-2.

Allowed values are: 'ENG', 'CES', 'DAN', 'NLD', 'FIN', 'FRA', 'DEU', 'ELL', 'HUN', 'ITA', 'NOR', 'POL', 'POR', 'RON', 'RUS', 'SLK', 'SPA', 'SWE', 'TUR', 'ARA', 'CHI_SIM', 'HIN', 'JPN', 'KOR', 'OTHERS'

`document_type`

(optional) The type of documents.

Allowed values are: 'INVOICE', 'RECEIPT', 'RESUME', 'TAX_FORM', 'DRIVER_LICENSE', 'PASSPORT', 'BANK_STATEMENT', 'CHECK', 'PAYSLIP', 'OTHERS'

`is_zip_output_enabled`

(optional) Whether or not to generate a ZIP file containing the results.

### DBMS_CLOUD_OCI_AI_VISION_CREATE_IMAGE_JOB_DETAILS_T Type

The details of the batch image analysis.

Syntax
```

```

Fields

Field Description

`input_location`

(required)

`features`

(required) The list of requested image analysis types.

`output_location`

(required)

`compartment_id`

(optional) The compartment identifier from the requester.

`display_name`

(optional) The image job display name.

`is_zip_output_enabled`

(optional) Whether or not to generate a ZIP file containing the results.

### DBMS_CLOUD_OCI_AI_VISION_DATASET_T Type

The base entity which is the input for creating and training a model.

Syntax
```

```

Fields

Field Description

`dataset_type`

(required) The dataset type, based on where it is stored.

Allowed values are: 'DATA_SCIENCE_LABELING', 'OBJECT_STORAGE'

### DBMS_CLOUD_OCI_AI_VISION_CREATE_MODEL_DETAILS_T Type

The information needed to create a new model.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A human-friendly name for the model, which can be changed.

`description`

(optional) An optional description of the model.

`model_version`

(optional) The model version

`model_type`

(required) Which type of Vision model this is.

`compartment_id`

(required) The compartment identifier.

`is_quick_mode`

(optional) Set to true when experimenting with a new model type or dataset, so the model training is quick, with a predefined low number of passes through the training data.

`max_training_duration_in_hours`

(optional) The maximum model training duration in hours, expressed as a decimal fraction.

`training_dataset`

(required)

`testing_dataset`

(optional)

`validation_dataset`

(optional)

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project that contains the model.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_AI_VISION_CREATE_PROJECT_DETAILS_T Type

The information needed to create a new project.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A human-friendly name for the project, that can be changed.

`description`

(optional) An optional description of the project.

`compartment_id`

(required) The compartment identifier.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_AI_VISION_DATA_SCIENCE_LABELING_DATASET_T Type

The dataset created by the Data Labeling Service.

Syntax
```

```

`dbms_cloud_oci_ai_vision_data_science_labeling_dataset_t`is a subtype of the`dbms_cloud_oci_ai_vision_dataset_t`type.

Fields

Field Description

`dataset_id`

(required) OCID of the Data Labeling dataset.

### DBMS_CLOUD_OCI_AI_VISION_DOCUMENT_CLASSIFICATION_FEATURE_T Type

Identifying the document type.

Syntax
```

```

`dbms_cloud_oci_ai_vision_document_classification_feature_t`is a subtype of the`dbms_cloud_oci_ai_vision_document_feature_t`type.

Fields

Field Description

`max_results`

(optional) The maximum number of results to return.

`model_id`

(optional) The custom model ID.

### DBMS_CLOUD_OCI_AI_VISION_DOCUMENT_JOB_T Type

The job details for a batch document analysis.

Syntax
```

```

Fields

Field Description

`id`

(required) The job id.

`compartment_id`

(required) The OCID of the compartment that starts the job.

`display_name`

(optional) The document job display name.

`features`

(required) The list of requested document analysis types.

`language`

(optional) The document language, abbreviated according to ISO 639-2.

Allowed values are: 'ENG', 'CES', 'DAN', 'NLD', 'FIN', 'FRA', 'DEU', 'ELL', 'HUN', 'ITA', 'NOR', 'POL', 'POR', 'RON', 'RUS', 'SLK', 'SPA', 'SWE', 'TUR', 'ARA', 'CHI_SIM', 'HIN', 'JPN', 'KOR', 'OTHERS'

`document_type`

(optional) The type of document.

Allowed values are: 'INVOICE', 'RECEIPT', 'RESUME', 'TAX_FORM', 'DRIVER_LICENSE', 'PASSPORT', 'BANK_STATEMENT', 'CHECK', 'PAYSLIP', 'OTHERS'

`input_location`

(optional)

`time_accepted`

(required) The job acceptance time.

`time_started`

(optional) The job start time.

`time_finished`

(optional) The job finish time.

`percent_complete`

(optional) How much progress the operation has made, compared to the total amount of work to be performed.

`output_location`

(required)

`lifecycle_state`

(required) The current state of the batch document job.

Allowed values are: 'SUCCEEDED', 'FAILED', 'ACCEPTED', 'CANCELED', 'IN_PROGRESS', 'CANCELING'

`is_zip_output_enabled`

(optional) Whether or not to generate a ZIP file containing the results.

`lifecycle_details`

(optional) The detailed status of FAILED state.

Allowed values are: 'PARTIALLY_SUCCEEDED', 'COMPLETELY_FAILED'

### DBMS_CLOUD_OCI_AI_VISION_DOCUMENT_KEY_VALUE_DETECTION_FEATURE_T Type

Extracting form fields.

Syntax
```

```

`dbms_cloud_oci_ai_vision_document_key_value_detection_feature_t`is a subtype of the`dbms_cloud_oci_ai_vision_document_feature_t`type.

### DBMS_CLOUD_OCI_AI_VISION_DOCUMENT_LANGUAGE_CLASSIFICATION_FEATURE_T Type

Detecting the language of the document.

Syntax
```

```

`dbms_cloud_oci_ai_vision_document_language_classification_feature_t`is a subtype of the`dbms_cloud_oci_ai_vision_document_feature_t`type.

Fields

Field Description

`max_results`

(optional) The maximum number of results to return.

### DBMS_CLOUD_OCI_AI_VISION_DOCUMENT_TABLE_DETECTION_FEATURE_T Type

Detecting and extracting data in tables.

Syntax
```

```

`dbms_cloud_oci_ai_vision_document_table_detection_feature_t`is a subtype of the`dbms_cloud_oci_ai_vision_document_feature_t`type.

### DBMS_CLOUD_OCI_AI_VISION_DOCUMENT_TEXT_DETECTION_FEATURE_T Type

Text recognition

Syntax
```

```

`dbms_cloud_oci_ai_vision_document_text_detection_feature_t`is a subtype of the`dbms_cloud_oci_ai_vision_document_feature_t`type.

Fields

Field Description

`generate_searchable_pdf`

(optional) Whether or not to generate a searchable PDF file.

### DBMS_CLOUD_OCI_AI_VISION_ERROR_T Type

Error Information.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code for programmatic parsing.

`message`

(required) A human-readable error message.

### DBMS_CLOUD_OCI_AI_VISION_FACE_DETECTION_FEATURE_T Type

The face detection parameters.

Syntax
```

```

`dbms_cloud_oci_ai_vision_face_detection_feature_t`is a subtype of the`dbms_cloud_oci_ai_vision_image_feature_t`type.

Fields

Field Description

`max_results`

(optional) The maximum number of results to return.

`should_return_landmarks`

(optional) Whether or not return face landmarks.

### DBMS_CLOUD_OCI_AI_VISION_IMAGE_CLASSIFICATION_FEATURE_T Type

The image classification parameters.

Syntax
```

```

`dbms_cloud_oci_ai_vision_image_classification_feature_t`is a subtype of the`dbms_cloud_oci_ai_vision_image_feature_t`type.

Fields

Field Description

`max_results`

(optional) The maximum number of results to return.

`model_id`

(optional) The custom model ID.

### DBMS_CLOUD_OCI_AI_VISION_IMAGE_JOB_T Type

The job details for a batch image analysis.

Syntax
```

```

Fields

Field Description

`id`

(required) The job id

`compartment_id`

(required) The OCID of the compartment that starts the job.

`display_name`

(optional) The image job display name.

`features`

(required) The list of requested document analysis types.

`input_location`

(optional)

`time_accepted`

(required) The job acceptance time.

`time_started`

(optional) The job start time.

`time_finished`

(optional) The job finish time.

`percent_complete`

(optional) How much progress the operation has made, compared to the total amount of work to be performed.

`output_location`

(required)

`lifecycle_state`

(required) The current state of the batch image job.

Allowed values are: 'SUCCEEDED', 'FAILED', 'ACCEPTED', 'CANCELED', 'IN_PROGRESS', 'CANCELING'

`lifecycle_details`

(optional) The detailed status of FAILED state.

Allowed values are: 'PARTIALLY_SUCCEEDED', 'COMPLETELY_FAILED'

`is_zip_output_enabled`

(optional) Whether or not to generate a ZIP file containing the results.

### DBMS_CLOUD_OCI_AI_VISION_IMAGE_OBJECT_DETECTION_FEATURE_T Type

The object detection parameters.

Syntax
```

```

`dbms_cloud_oci_ai_vision_image_object_detection_feature_t`is a subtype of the`dbms_cloud_oci_ai_vision_image_feature_t`type.

Fields

Field Description

`max_results`

(optional) The maximum number of results to return.

`model_id`

(optional) The custom model ID.

### DBMS_CLOUD_OCI_AI_VISION_IMAGE_TEXT_DETECTION_FEATURE_T Type

The text detection parameters.

Syntax
```

```

`dbms_cloud_oci_ai_vision_image_text_detection_feature_t`is a subtype of the`dbms_cloud_oci_ai_vision_image_feature_t`type.

Fields

Field Description

`language`

(optional) The language of the document image, abbreviated according to ISO 639-2.

Allowed values are: 'ENG', 'CES', 'DAN', 'NLD', 'FIN', 'FRA', 'DEU', 'ELL', 'HUN', 'ITA', 'NOR', 'POL', 'POR', 'RON', 'RUS', 'SLK', 'SPA', 'SWE', 'TUR', 'ARA', 'CHI_SIM', 'HIN', 'JPN', 'KOR', 'OTHERS'

### DBMS_CLOUD_OCI_AI_VISION_INLINE_DOCUMENT_DETAILS_T Type

The document incorporated in the request payload.

Syntax
```

```

`dbms_cloud_oci_ai_vision_inline_document_details_t`is a subtype of the`dbms_cloud_oci_ai_vision_document_details_t`type.

Fields

Field Description

`data`

(required) Raw document data.

### DBMS_CLOUD_OCI_AI_VISION_INLINE_IMAGE_DETAILS_T Type

The image incorporated in the request payload.

Syntax
```

```

`dbms_cloud_oci_ai_vision_inline_image_details_t`is a subtype of the`dbms_cloud_oci_ai_vision_image_details_t`type.

Fields

Field Description

`data`

(required) Raw image data.

### DBMS_CLOUD_OCI_AI_VISION_MODEL_T Type

Machine-learned Model.

Syntax
```

```

Fields

Field Description

`id`

(required) A unique identifier that is immutable after creation.

`display_name`

(optional) A human-friendly name for the model, which can be changed.

`description`

(optional) An optional description of the model.

`compartment_id`

(required) The compartment identifier.

`model_type`

(required) What type of Vision model this is.

Allowed values are: 'IMAGE_CLASSIFICATION', 'OBJECT_DETECTION'

`is_quick_mode`

(optional) Set to true when experimenting with a new model type or dataset, so model training is quick, with a predefined low number of passes through the training data.

`max_training_duration_in_hours`

(optional) The maximum model training duration in hours, expressed as a decimal fraction.

`trained_duration_in_hours`

(optional) The total hours actually used for model training.

`training_dataset`

(required)

`testing_dataset`

(optional)

`validation_dataset`

(optional)

`model_version`

(required) The version of the model.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project that contains the model.

`time_created`

(required) When the model was created, as an RFC3339 datetime string.

`time_updated`

(optional) When the model was updated, as an RFC3339 datetime string.

`lifecycle_state`

(required) The current state of the model.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail, that can provide actionable information if training failed.

`precision`

(optional) The precision of the trained model.

`recall`

(optional) Recall of the trained model.

`average_precision`

(optional) The mean average precision of the trained model.

`confidence_threshold`

(optional) The intersection over the union threshold used for calculating precision and recall.

`total_image_count`

(optional) The number of images in the dataset used to train, validate, and test the model.

`test_image_count`

(optional) The number of images set aside for evaluating model performance metrics after training.

`metrics`

(optional) The complete set of per-label metrics for successfully trained models.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. For example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_AI_VISION_MODEL_SUMMARY_T Type

The metadata about the model.

Syntax
```

```

Fields

Field Description

`id`

(required) A unique identifier that is immutable after creation.

`display_name`

(optional) A human-friendly name for the model, which can be changed.

`description`

(optional) An optional description of the model.

`compartment_id`

(required) The compartment identifier.

`model_type`

(required) What type of Vision model this is.

`model_version`

(required) The version of the model.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project that contains the model.

`time_created`

(required) When the model was created, as an RFC3339 datetime string.

`time_updated`

(optional) When the model was modified, as an RFC3339 datetime string.

`lifecycle_state`

(required) The current state of the model.

`lifecycle_details`

(optional) A message describing the current state in more detail, that can provide actionable information if training failed.

`precision`

(optional) The precision of the trained model.

`training_dataset`

(optional)

`testing_dataset`

(optional)

`validation_dataset`

(optional)

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. For example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_AI_VISION_MODEL_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_model_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_MODEL_COLLECTION_T Type

The results of a model search.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of models.

### DBMS_CLOUD_OCI_AI_VISION_OBJECT_LOCATION_T Type

A location in Object Storage that is uniquely identified by namespace name, bucket name and object name.

Syntax
```

```

Fields

Field Description

`namespace_name`

(required) The Object Storage namespace name.

`bucket_name`

(required) The Object Storage bucket name.

`object_name`

(required) The Object Storage object name.

### DBMS_CLOUD_OCI_AI_VISION_OBJECT_LOCATION_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_object_location_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_OBJECT_LIST_INLINE_INPUT_LOCATION_T Type

A list of object locations in Object Storage.

Syntax
```

```

`dbms_cloud_oci_ai_vision_object_list_inline_input_location_t`is a subtype of the`dbms_cloud_oci_ai_vision_input_location_t`type.

Fields

Field Description

`object_locations`

(required) The list of ObjectLocations.

### DBMS_CLOUD_OCI_AI_VISION_OBJECT_STORAGE_DATASET_T Type

The dataset that resides in Object Storage.

Syntax
```

```

`dbms_cloud_oci_ai_vision_object_storage_dataset_t`is a subtype of the`dbms_cloud_oci_ai_vision_dataset_t`type.

Fields

Field Description

`namespace_name`

(required) The namespace name of the Object Storage bucket that contains the input data file.

`bucket_name`

(required) The name of the Object Storage bucket that contains the input data file.

`object_name`

(required) The object name of the input data file.

### DBMS_CLOUD_OCI_AI_VISION_OBJECT_STORAGE_DOCUMENT_DETAILS_T Type

A document in OCI Object Storage.

Syntax
```

```

`dbms_cloud_oci_ai_vision_object_storage_document_details_t`is a subtype of the`dbms_cloud_oci_ai_vision_document_details_t`type.

Fields

Field Description

`namespace_name`

(required) The Object Storage namespace.

`bucket_name`

(required) The Object Storage bucket name.

`object_name`

(required) The Object Storage object name.

### DBMS_CLOUD_OCI_AI_VISION_OBJECT_STORAGE_IMAGE_DETAILS_T Type

The image residing in OCI Object Storage.

Syntax
```

```

`dbms_cloud_oci_ai_vision_object_storage_image_details_t`is a subtype of the`dbms_cloud_oci_ai_vision_image_details_t`type.

Fields

Field Description

`namespace_name`

(required) The Object Storage namespace.

`bucket_name`

(required) The Object Storage bucket name.

`object_name`

(required) The Object Storage object name.

### DBMS_CLOUD_OCI_AI_VISION_PROJECT_T Type

A Vision Project containing models.

Syntax
```

```

Fields

Field Description

`id`

(required) A unique identifier that is immutable after creation.

`display_name`

(optional) A human-friendly name for the project, which can be changed.

`description`

(optional) An optional description of the project.

`compartment_id`

(required) A compartment identifier.

`time_created`

(required) When the project was created, as an RFC3339 datetime string.

`time_updated`

(optional) When the project was updated, as an RFC3339 datetime string.

`lifecycle_state`

(required) The current state of the project.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail, that can provide actionable information if creation failed.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. For example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_AI_VISION_PROJECT_SUMMARY_T Type

the metadata about the project.

Syntax
```

```

Fields

Field Description

`id`

(required) A unique identifier that is immutable after creation.

`display_name`

(optional) A human-friendly name for the project, that can be changed.

`compartment_id`

(required) The compartment identifier.

`time_created`

(required) When the project was created, as an RFC3339 datetime string.

`time_updated`

(optional) When the project was created, as an RFC3339 datetime string.

`lifecycle_state`

(required) The current state of the project.

`lifecycle_details`

(optional) A message describing the current state in more detail, that can provide actionable information if creation failed.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. For example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_AI_VISION_PROJECT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_project_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_PROJECT_COLLECTION_T Type

The results of a project search.

Syntax
```

```

Fields

Field Description

`items`

(required) List of projects.

### DBMS_CLOUD_OCI_AI_VISION_UPDATE_MODEL_DETAILS_T Type

The metadata which can be edited after model creation.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A human-friendly name of the model, which can be changed.

`description`

(optional) An optional description of the model.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_AI_VISION_UPDATE_PROJECT_DETAILS_T Type

The metadata that can be edited after project creation.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A human-friendly name for the project, that can be changed.

`description`

(optional) An optional description of the project.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_AI_VISION_VALUE_ARRAY_T Type

The array of field values.

Syntax
```

```

`dbms_cloud_oci_ai_vision_value_array_t`is a subtype of the`dbms_cloud_oci_ai_vision_field_value_t`type.

Fields

Field Description

`items`

(required)

### DBMS_CLOUD_OCI_AI_VISION_VALUE_DATE_T Type

The date field value.

Syntax
```

```

`dbms_cloud_oci_ai_vision_value_date_t`is a subtype of the`dbms_cloud_oci_ai_vision_field_value_t`type.

Fields

Field Description

`value`

(required) The date field value as yyyy-mm-dd.

### DBMS_CLOUD_OCI_AI_VISION_VALUE_INTEGER_T Type

The integer field value.

Syntax
```

```

`dbms_cloud_oci_ai_vision_value_integer_t`is a subtype of the`dbms_cloud_oci_ai_vision_field_value_t`type.

Fields

Field Description

`value`

(required) The integer value.

### DBMS_CLOUD_OCI_AI_VISION_VALUE_NUMBER_T Type

The floating point number field value.

Syntax
```

```

`dbms_cloud_oci_ai_vision_value_number_t`is a subtype of the`dbms_cloud_oci_ai_vision_field_value_t`type.

Fields

Field Description

`value`

(required) The number value.

### DBMS_CLOUD_OCI_AI_VISION_VALUE_PHONE_NUMBER_T Type

The phone number field value.

Syntax
```

```

`dbms_cloud_oci_ai_vision_value_phone_number_t`is a subtype of the`dbms_cloud_oci_ai_vision_field_value_t`type.

Fields

Field Description

`value`

(required) The phone number field value.

### DBMS_CLOUD_OCI_AI_VISION_VALUE_STRING_T Type

The string field value.

Syntax
```

```

`dbms_cloud_oci_ai_vision_value_string_t`is a subtype of the`dbms_cloud_oci_ai_vision_field_value_t`type.

Fields

Field Description

`value`

(required) The string text.

### DBMS_CLOUD_OCI_AI_VISION_VALUE_TIME_T Type

The time field value.

Syntax
```

```

`dbms_cloud_oci_ai_vision_value_time_t`is a subtype of the`dbms_cloud_oci_ai_vision_field_value_t`type.

Fields

Field Description

`value`

(required) The time field value as yyyy-mm-dd hh-mm-ss.

### DBMS_CLOUD_OCI_AI_VISION_WORK_REQUEST_RESOURCE_T Type

A resource created, or operated on, by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted remains in the IN_PROGRESS state until the work is complete for. At that point, it transitions to CREATED, UPDATED, or DELETED, as appropriate.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED', 'FAILED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata.

### DBMS_CLOUD_OCI_AI_VISION_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_WORK_REQUEST_T Type

The workrequest status details.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The type of work request.

Allowed values are: 'CREATE_PROJECT', 'UPDATE_PROJECT', 'DELETE_PROJECT', 'MOVE_PROJECT', 'CREATE_MODEL', 'UPDATE_MODEL', 'DELETE_MODEL', 'MOVE_MODEL'

`status`

(required) The status of the current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The ID of the work request.

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) The percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_AI_VISION_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed on (https://docs.cloud.oracle.com/Content/API/References/apierrors.htm).

`message`

(required) A human-readable description of the issue encountered.

`l_timestamp`

(required) When the error occured, as an RFC3339 formatted datetime.

### DBMS_CLOUD_OCI_AI_VISION_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_WORK_REQUEST_ERROR_COLLECTION_T Type

The results of a workRequestError search.

Syntax
```

```

Fields

Field Description

`items`

(required) the list of workRequestError objects.

### DBMS_CLOUD_OCI_AI_VISION_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) A human-readable log message.

`l_timestamp`

(required) When the log message was written, as an RFC3339 formatted datetime.

### DBMS_CLOUD_OCI_AI_VISION_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

The results of a workRequestLog search.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of workRequestLogEntries.

### DBMS_CLOUD_OCI_AI_VISION_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The type of the work request.

Allowed values are: 'CREATE_PROJECT', 'UPDATE_PROJECT', 'DELETE_PROJECT', 'MOVE_PROJECT', 'CREATE_MODEL', 'UPDATE_MODEL', 'DELETE_MODEL', 'MOVE_MODEL'

`status`

(required) The status of the current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The ID of the work request.

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment is used.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) The percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_AI_VISION_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_ai_vision_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_VISION_WORK_REQUEST_SUMMARY_COLLECTION_T Type

The results of a workRequest search.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of workRequestSummary objects.

- [AI Vision Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-3D37D814-B809-487B-95B6-430F2393685E)
- [DBMS_CLOUD_OCI_AI_VISION_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-460610F9-E213-4CD4-8A88-2E9716DDEA9F)
- [DBMS_CLOUD_OCI_AI_VISION_DOCUMENT_FEATURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-0F36E74B-B3AF-4FE9-B915-E2B25BFAD59D)
- [DBMS_CLOUD_OCI_AI_VISION_DOCUMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-D9A7E5F2-930E-4614-B691-07B659027944)
- [DBMS_CLOUD_OCI_AI_VISION_OUTPUT_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-5BEC050A-2E8C-4373-BF5E-39C930B84588)
- [DBMS_CLOUD_OCI_AI_VISION_DOCUMENT_FEATURE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-4B4ADB95-0882-4D4D-8586-791B56EA3D04)
- [DBMS_CLOUD_OCI_AI_VISION_ANALYZE_DOCUMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-73CEA7F7-C54B-437F-9D49-5E0C10BE1944)
- [DBMS_CLOUD_OCI_AI_VISION_DOCUMENT_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-12112499-6A2F-4EBC-8D2B-CC7F1E7FA139)
- [DBMS_CLOUD_OCI_AI_VISION_DIMENSIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-5A2AF33D-2DFA-4892-B788-A95E50A5FCB9)
- [DBMS_CLOUD_OCI_AI_VISION_DETECTED_DOCUMENT_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-8EEDDAE9-083F-4516-AF4E-65D736EFB329)
- [DBMS_CLOUD_OCI_AI_VISION_DETECTED_LANGUAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-5E2A823F-E772-498F-9857-CAD964EDB7E7)
- [DBMS_CLOUD_OCI_AI_VISION_NORMALIZED_VERTEX_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-DD01F391-0147-45E0-AE2E-F83132B5A1BA)
- [DBMS_CLOUD_OCI_AI_VISION_NORMALIZED_VERTEX_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-DA047E20-81BE-43BD-A6BC-D787CB3BEF33)
- [DBMS_CLOUD_OCI_AI_VISION_BOUNDING_POLYGON_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-8F79852E-108D-4F65-A0CB-78E313DB7958)
- [DBMS_CLOUD_OCI_AI_VISION_WORD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-7C8E3958-A083-4531-94F6-43A25B03B91B)
- [DBMS_CLOUD_OCI_AI_VISION_NUMBER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-A7226EFD-12D0-45C0-9719-051CC2E8A0E1)
- [DBMS_CLOUD_OCI_AI_VISION_LINE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-65C58D1F-4B22-4916-9F6A-A0C4F9967863)
- [DBMS_CLOUD_OCI_AI_VISION_CELL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-E3F18F18-F427-47CD-AF22-5D13C097A98B)
- [DBMS_CLOUD_OCI_AI_VISION_CELL_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-541895F3-9022-4F2A-8ED3-AAB153515EC5)
- [DBMS_CLOUD_OCI_AI_VISION_TABLE_ROW_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-B14F63DA-6E01-454A-A11E-7C7E76DED1CD)
- [DBMS_CLOUD_OCI_AI_VISION_TABLE_ROW_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-583BBE30-6BDA-430E-94C2-C540B18C4952)
- [DBMS_CLOUD_OCI_AI_VISION_TABLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-7A635E2E-CD2E-4659-8ED3-F501A7BC32ED)
- [DBMS_CLOUD_OCI_AI_VISION_FIELD_LABEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-C52B291A-FD8A-4417-9983-09F8C925FB22)
- [DBMS_CLOUD_OCI_AI_VISION_FIELD_NAME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-4A73D238-3FCA-4ADB-A560-FF0FAF5AB8DC)
- [DBMS_CLOUD_OCI_AI_VISION_FIELD_VALUE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-30CB5062-1918-4CFE-A227-FB6E9B35BB87)
- [DBMS_CLOUD_OCI_AI_VISION_DOCUMENT_FIELD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-98E2025D-3B8C-4EE9-A213-40BCFEDB5FD5)
- [DBMS_CLOUD_OCI_AI_VISION_DETECTED_DOCUMENT_TYPE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-AF0ADB2A-8585-4C2D-82DB-33CD28265CC9)
- [DBMS_CLOUD_OCI_AI_VISION_DETECTED_LANGUAGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-D1EC8BDA-B1B8-4C43-8E97-D9436CCD5436)
- [DBMS_CLOUD_OCI_AI_VISION_WORD_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-44CB2584-263C-440E-88C6-81DFA9427128)
- [DBMS_CLOUD_OCI_AI_VISION_LINE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-9685E250-D71A-4F86-9C47-898D02C087C8)
- [DBMS_CLOUD_OCI_AI_VISION_TABLE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-32E3DBBE-6289-4770-B1F1-50C7B5E820F7)
- [DBMS_CLOUD_OCI_AI_VISION_DOCUMENT_FIELD_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-B01FB91B-2D8A-4892-BE72-3D64A2724E15)
- [DBMS_CLOUD_OCI_AI_VISION_PAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-AF2BC18C-4DE3-44F1-9C54-D264BF20342D)
- [DBMS_CLOUD_OCI_AI_VISION_PROCESSING_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-6B60DA7E-6FFD-4C8D-A88E-4C3FA1181246)
- [DBMS_CLOUD_OCI_AI_VISION_PAGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-AC9691B5-918D-4728-91E7-F4F23EC94AC8)
- [DBMS_CLOUD_OCI_AI_VISION_PROCESSING_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-54E7B1F6-CD0A-4C2E-A45B-F3F6E814AC94)
- [DBMS_CLOUD_OCI_AI_VISION_ANALYZE_DOCUMENT_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-6B91072D-0F46-4007-9DFE-913A8085272E)
- [DBMS_CLOUD_OCI_AI_VISION_IMAGE_FEATURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-98D7DB6E-1045-4DCE-B70A-797926902D1C)
- [DBMS_CLOUD_OCI_AI_VISION_IMAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-B6FB5883-BC06-4748-A853-6A72CC3BE4E9)
- [DBMS_CLOUD_OCI_AI_VISION_IMAGE_FEATURE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-3B8B8399-8A17-4681-8F7F-8E22DACD4A0B)
- [DBMS_CLOUD_OCI_AI_VISION_ANALYZE_IMAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-67668434-8D06-4EC4-B156-3E9BE856E1B8)
- [DBMS_CLOUD_OCI_AI_VISION_IMAGE_OBJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-F78C14B6-688F-433F-8781-7F2DC9F6710B)
- [DBMS_CLOUD_OCI_AI_VISION_LABEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-A95D8013-9712-4380-A93A-FD2C45023259)
- [DBMS_CLOUD_OCI_AI_VISION_ONTOLOGY_CLASS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-B9F71752-2BFC-497F-8D98-A2011BA507F7)
- [DBMS_CLOUD_OCI_AI_VISION_IMAGE_TEXT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-56DB89E1-16EE-48B4-A51C-B49C9DF21027)
- [DBMS_CLOUD_OCI_AI_VISION_LANDMARK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-68785D62-E808-4FBE-A7BF-21C216CFAC29)
- [DBMS_CLOUD_OCI_AI_VISION_LANDMARK_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-2A257360-5165-45EC-8BF9-47B17C5BA33E)
- [DBMS_CLOUD_OCI_AI_VISION_FACE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-DEE46B01-5812-45C0-AEFE-232D8C5F5127)
- [DBMS_CLOUD_OCI_AI_VISION_IMAGE_OBJECT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-018E0CAD-EE67-4E49-9EB6-3F896FB1B4AB)
- [DBMS_CLOUD_OCI_AI_VISION_LABEL_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-03A83ADF-12F5-46DE-82C6-A60E919D8126)
- [DBMS_CLOUD_OCI_AI_VISION_ONTOLOGY_CLASS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-3204C31E-7F79-464F-9A64-7B3BD1FBA82B)
- [DBMS_CLOUD_OCI_AI_VISION_FACE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-F8F666B9-D73E-4F47-AB15-C5F7D805E538)
- [DBMS_CLOUD_OCI_AI_VISION_ANALYZE_IMAGE_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-157C4172-709C-4349-A08D-D79923871803)
- [DBMS_CLOUD_OCI_AI_VISION_CHANGE_MODEL_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-91314CA5-8D21-4408-A81D-3139493333F1)
- [DBMS_CLOUD_OCI_AI_VISION_CHANGE_PROJECT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-1442A82D-4C6B-47BA-9E09-28935BC09D35)
- [DBMS_CLOUD_OCI_AI_VISION_INPUT_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-03E1EABE-E814-49B4-A511-530AB3E338EB)
- [DBMS_CLOUD_OCI_AI_VISION_CREATE_DOCUMENT_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-984A6BCE-7090-4318-8BD9-47FC4D951124)
- [DBMS_CLOUD_OCI_AI_VISION_CREATE_IMAGE_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-FEC85DE6-EFC1-4F56-BA6D-4FD1B5DE7FC8)
- [DBMS_CLOUD_OCI_AI_VISION_DATASET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-39802D8C-1CA9-4F32-B4CB-BF4B66ACB3C6)
- [DBMS_CLOUD_OCI_AI_VISION_CREATE_MODEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-68CA4F57-7E0D-4342-875C-AEE1F27B5C46)
- [DBMS_CLOUD_OCI_AI_VISION_CREATE_PROJECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-4E9401B5-B6CA-4869-90BC-5E5AC217F4DA)
- [DBMS_CLOUD_OCI_AI_VISION_DATA_SCIENCE_LABELING_DATASET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-FE779C81-AC8F-4D94-83D0-1D5EA698042F)
- [DBMS_CLOUD_OCI_AI_VISION_DOCUMENT_CLASSIFICATION_FEATURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-B9930DEE-8FC8-4ACB-B075-A60E2EB73C9E)
- [DBMS_CLOUD_OCI_AI_VISION_DOCUMENT_JOB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-963ED81F-4570-4E00-B496-592FB1E6618D)
- [DBMS_CLOUD_OCI_AI_VISION_DOCUMENT_KEY_VALUE_DETECTION_FEATURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-A64BF963-9A59-472D-9086-04BE735F254D)
- [DBMS_CLOUD_OCI_AI_VISION_DOCUMENT_LANGUAGE_CLASSIFICATION_FEATURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-FD2D2FA5-A4B3-4D14-8D04-28EB3C214E31)
- [DBMS_CLOUD_OCI_AI_VISION_DOCUMENT_TABLE_DETECTION_FEATURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-697B5C38-ECB5-4468-961A-3C472E0B58D7)
- [DBMS_CLOUD_OCI_AI_VISION_DOCUMENT_TEXT_DETECTION_FEATURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-176F81F9-3AA8-4309-BACB-943D2B70BBAA)
- [DBMS_CLOUD_OCI_AI_VISION_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-658DFFF2-5661-4061-8F6A-0AA0A0C56E7A)
- [DBMS_CLOUD_OCI_AI_VISION_FACE_DETECTION_FEATURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-FF1DC4EC-3BA4-45DD-BC4E-4D3139802318)
- [DBMS_CLOUD_OCI_AI_VISION_IMAGE_CLASSIFICATION_FEATURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-2CF8784C-25F8-4BD3-B0D1-F439D0215436)
- [DBMS_CLOUD_OCI_AI_VISION_IMAGE_JOB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-0756EB9F-7C5D-4A39-AF71-B605B070B27D)
- [DBMS_CLOUD_OCI_AI_VISION_IMAGE_OBJECT_DETECTION_FEATURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-A0DC6622-BE6F-4587-A77E-E2CC08C3FFFE)
- [DBMS_CLOUD_OCI_AI_VISION_IMAGE_TEXT_DETECTION_FEATURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-B236057E-983C-4236-A893-007AC2DCFF74)
- [DBMS_CLOUD_OCI_AI_VISION_INLINE_DOCUMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-C344B8AD-1317-46EE-8EDB-344637888D82)
- [DBMS_CLOUD_OCI_AI_VISION_INLINE_IMAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-AC95CC75-0434-43AF-80DA-2A5F33BB1BD5)
- [DBMS_CLOUD_OCI_AI_VISION_MODEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-10569669-9363-43A7-8EE7-44E1BFCA14B5)
- [DBMS_CLOUD_OCI_AI_VISION_MODEL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-BC0B4610-67C6-4E0B-A000-507FB253B828)
- [DBMS_CLOUD_OCI_AI_VISION_MODEL_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-FB012966-C6C4-433E-A33A-6510AA6B3B61)
- [DBMS_CLOUD_OCI_AI_VISION_MODEL_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-3C685187-4688-4D29-875B-2E60EAD99037)
- [DBMS_CLOUD_OCI_AI_VISION_OBJECT_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-6A43CAC8-0B44-4E94-9277-4CC811D3A47C)
- [DBMS_CLOUD_OCI_AI_VISION_OBJECT_LOCATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-4262EC8C-3955-449F-A962-FEA97F071ECB)
- [DBMS_CLOUD_OCI_AI_VISION_OBJECT_LIST_INLINE_INPUT_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-73988858-6018-4879-9A86-B4205EB87F24)
- [DBMS_CLOUD_OCI_AI_VISION_OBJECT_STORAGE_DATASET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-22EADCB9-BD7E-4FAB-81A8-96546E404208)
- [DBMS_CLOUD_OCI_AI_VISION_OBJECT_STORAGE_DOCUMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-34605EEA-C26A-45C4-B49B-A987E191BF14)
- [DBMS_CLOUD_OCI_AI_VISION_OBJECT_STORAGE_IMAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-35C7CBC8-6ECA-4DD7-BBE9-B7D4F8A04553)
- [DBMS_CLOUD_OCI_AI_VISION_PROJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-42ECE125-5508-4EB5-9C13-D495A077DA18)
- [DBMS_CLOUD_OCI_AI_VISION_PROJECT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-961152E6-05BB-4AD5-A44A-DFAE89E1F881)
- [DBMS_CLOUD_OCI_AI_VISION_PROJECT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-17C5A078-FD4C-4561-A033-E7BE8353564B)
- [DBMS_CLOUD_OCI_AI_VISION_PROJECT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-5CB2E822-BE54-4ED7-9232-385ED1F20161)
- [DBMS_CLOUD_OCI_AI_VISION_UPDATE_MODEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-4FC9F422-688A-410E-85C0-CD9BE6C31599)
- [DBMS_CLOUD_OCI_AI_VISION_UPDATE_PROJECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-2F09F2E8-6C92-4DF6-8B4B-42EB6C165D72)
- [DBMS_CLOUD_OCI_AI_VISION_VALUE_ARRAY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-A299B065-D1C3-4FD4-9FE1-7D5093459B3D)
- [DBMS_CLOUD_OCI_AI_VISION_VALUE_DATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-229AF3CC-E698-4B57-9BBB-08BBB16C6193)
- [DBMS_CLOUD_OCI_AI_VISION_VALUE_INTEGER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-4DB14659-DFF1-40F1-9E2B-4E08593DE2D7)
- [DBMS_CLOUD_OCI_AI_VISION_VALUE_NUMBER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-87289838-FCAB-4FA0-82EA-0DA1579CB3ED)
- [DBMS_CLOUD_OCI_AI_VISION_VALUE_PHONE_NUMBER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-5CFDF4EE-E155-4C6D-9191-DD1AFF4C1B58)
- [DBMS_CLOUD_OCI_AI_VISION_VALUE_STRING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-48126B93-8C67-4C67-A7D2-CA5688A6AFB3)
- [DBMS_CLOUD_OCI_AI_VISION_VALUE_TIME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-6A9ECB06-DE3A-4ED8-8465-39B2449AA271)
- [DBMS_CLOUD_OCI_AI_VISION_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-A14CAEBF-37EF-46DD-9C9C-B68B4A1F0D77)
- [DBMS_CLOUD_OCI_AI_VISION_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-3CD1F82F-ADC7-4C65-8FA7-B341ADB3313A)
- [DBMS_CLOUD_OCI_AI_VISION_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-1A6C94ED-B7C0-40A6-9872-3A6A2D09C1C1)
- [DBMS_CLOUD_OCI_AI_VISION_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-741D5B33-1283-47E6-8697-2BF1405827FA)
- [DBMS_CLOUD_OCI_AI_VISION_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-293A44C8-602D-4F74-9318-34D49233BD1C)
- [DBMS_CLOUD_OCI_AI_VISION_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-7AF883DC-2CDD-4B80-88A6-7B4737C7C4A3)
- [DBMS_CLOUD_OCI_AI_VISION_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-05D1F53B-546D-4C5F-9F68-782D559FEC3B)
- [DBMS_CLOUD_OCI_AI_VISION_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-69C55E55-A437-47CC-9852-3205FBA053EE)
- [DBMS_CLOUD_OCI_AI_VISION_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-C256A815-AFC1-4663-9954-91E53F3A1CCD)
- [DBMS_CLOUD_OCI_AI_VISION_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-AAD0DA00-5D6F-4A0D-96F5-8C60289BD40E)
- [DBMS_CLOUD_OCI_AI_VISION_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-A69CF1B8-5B79-4753-9A86-DCEE26E65800)
- [DBMS_CLOUD_OCI_AI_VISION_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_vision_t.html#ADSDK-GUID-C10CD06F-2F21-4C8F-9FF5-68CE846379C2)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
