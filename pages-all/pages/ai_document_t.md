# AI Document Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html
- Fetched: 2026-09-05 19:00 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#dcoc-content-body)

## AI Document Common Types

### DBMS_CLOUD_OCI_AI_DOCUMENT_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_FEATURE_T Type

The type of document analysis.

Syntax
```

```

Fields

Field Description

`feature_type`

(required) The type of document analysis requested. The allowed values are: - `LANGUAGE_CLASSIFICATION`: Detect the language. - `TEXT_EXTRACTION`: Recognize text. - `TABLE_EXTRACTION`: Detect and extract data in tables. - `KEY_VALUE_EXTRACTION`: Extract form fields. - `DOCUMENT_CLASSIFICATION`: Identify the type of document.

Allowed values are: 'LANGUAGE_CLASSIFICATION', 'TEXT_EXTRACTION', 'TABLE_EXTRACTION', 'KEY_VALUE_EXTRACTION', 'DOCUMENT_CLASSIFICATION'

### DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_DETAILS_T Type

The details of a document to analyze.

Syntax
```

```

Fields

Field Description

`source`

(required) The location of the document data. The allowed values are: - `INLINE`: The data is included directly in the request payload. - `OBJECT_STORAGE`: The document is in OCI Object Storage.

Allowed values are: 'INLINE', 'OBJECT_STORAGE'

### DBMS_CLOUD_OCI_AI_DOCUMENT_OUTPUT_LOCATION_T Type

The object storage location where to store analysis results.

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_METADATA_T Type

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_DIMENSIONS_T Type

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_DETECTED_DOCUMENT_TYPE_T Type

The detected document type.

Syntax
```

```

Fields

Field Description

`document_type`

(required) The document type.

`document_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Key-Value Extraction model that was used to extract the key-value pairs.

`confidence`

(required) The confidence score between 0 and 1.

### DBMS_CLOUD_OCI_AI_DOCUMENT_DETECTED_LANGUAGE_T Type

The language detected in a document.

Syntax
```

```

Fields

Field Description

`language`

(required) The document language, abbreviated according to the BCP 47 syntax.

`confidence`

(required) The confidence score between 0 and 1.

### DBMS_CLOUD_OCI_AI_DOCUMENT_NORMALIZED_VERTEX_T Type

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_NORMALIZED_VERTEX_TBL Type

Nested table type of dbms_cloud_oci_ai_document_normalized_vertex_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_BOUNDING_POLYGON_T Type

The object-bounding polygon box.

Syntax
```

```

Fields

Field Description

`normalized_vertices`

(required) An array of normalized points defining the polygon's perimeter, with an implicit segment between subsequent points and between the first and last point. Rectangles are defined with four points. For example, `[{\"x\": 0, \"y\": 0}, {\"x\": 1, \"y\": 0}, {\"x\": 1, \"y\": 0.5}, {\"x\": 0, \"y\": 0.5}]` represents the top half of an image.

### DBMS_CLOUD_OCI_AI_DOCUMENT_WORD_T Type

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_NUMBER_TBL Type

Nested table type of number.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_LINE_T Type

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_CELL_T Type

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_CELL_TBL Type

Nested table type of dbms_cloud_oci_ai_document_cell_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_TABLE_ROW_T Type

A single row in a table.

Syntax
```

```

Fields

Field Description

`cells`

(required) The cells in the row.

### DBMS_CLOUD_OCI_AI_DOCUMENT_TABLE_ROW_TBL Type

Nested table type of dbms_cloud_oci_ai_document_table_row_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_TABLE_T Type

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_FIELD_LABEL_T Type

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_FIELD_NAME_T Type

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_FIELD_VALUE_T Type

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_FIELD_T Type

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_DETECTED_DOCUMENT_TYPE_TBL Type

Nested table type of dbms_cloud_oci_ai_document_detected_document_type_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_DETECTED_LANGUAGE_TBL Type

Nested table type of dbms_cloud_oci_ai_document_detected_language_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_WORD_TBL Type

Nested table type of dbms_cloud_oci_ai_document_word_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_LINE_TBL Type

Nested table type of dbms_cloud_oci_ai_document_line_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_TABLE_TBL Type

Nested table type of dbms_cloud_oci_ai_document_table_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_FIELD_TBL Type

Nested table type of dbms_cloud_oci_ai_document_document_field_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_PAGE_T Type

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_PROCESSING_ERROR_T Type

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_PAGE_TBL Type

Nested table type of dbms_cloud_oci_ai_document_page_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_PROCESSING_ERROR_TBL Type

Nested table type of dbms_cloud_oci_ai_document_processing_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_ANALYZE_DOCUMENT_RESULT_T Type

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

`text_extraction_model_version`

(optional) The document text extraction model version.

`key_value_extraction_model_version`

(optional) The document keyValue extraction model version.

`table_extraction_model_version`

(optional) The document table extraction model version.

`errors`

(optional) The errors encountered during document analysis.

`searchable_pdf`

(optional) The searchable PDF file that was generated.

### DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_FEATURE_TBL Type

Nested table type of dbms_cloud_oci_ai_document_document_feature_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_ANALYZE_DOCUMENT_DETAILS_T Type

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

(optional) The compartment identifier.

`output_location`

(optional)

`language`

(optional) The document language, abbreviated according to the BCP 47 syntax.

`document_type`

(optional) The document type.

Allowed values are: 'INVOICE', 'RECEIPT', 'RESUME', 'TAX_FORM', 'DRIVER_LICENSE', 'PASSPORT', 'BANK_STATEMENT', 'CHECK', 'PAYSLIP', 'OTHERS'

`ocr_data`

(optional)

### DBMS_CLOUD_OCI_AI_DOCUMENT_CHANGE_MODEL_COMPARTMENT_DETAILS_T Type

The compartment the model should be moved to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The compartment identifier.

### DBMS_CLOUD_OCI_AI_DOCUMENT_CHANGE_PROJECT_COMPARTMENT_DETAILS_T Type

Which compartment the project should be moved to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The compartment identifier.

### DBMS_CLOUD_OCI_AI_DOCUMENT_COMPONENT_MODEL_T Type

The custom model selected for Composition.

Syntax
```

```

Fields

Field Description

`model_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of active custom Key Value model that need to be composed.

### DBMS_CLOUD_OCI_AI_DOCUMENT_DATASET_T Type

The base entity which is the input for creating and training a model.

Syntax
```

```

Fields

Field Description

`dataset_type`

(required) The dataset type, based on where it is stored.

Allowed values are: 'DATA_SCIENCE_LABELING', 'OBJECT_STORAGE'

### DBMS_CLOUD_OCI_AI_DOCUMENT_COMPONENT_MODEL_TBL Type

Nested table type of dbms_cloud_oci_ai_document_component_model_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_CREATE_MODEL_DETAILS_T Type

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

(required) The type of the Document model.

`compartment_id`

(required) The compartment identifier.

`is_quick_mode`

(optional) Set to true when experimenting with a new model type or dataset, so the model training is quick, with a predefined low number of passes through the training data.

`max_training_time_in_hours`

(optional) The maximum model training time in hours, expressed as a decimal fraction.

`training_dataset`

(optional)

`testing_dataset`

(optional)

`validation_dataset`

(optional)

`component_models`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)list of active custom Key Value models that need to be composed.

`alias_name`

(optional) the alias name of the model.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project that contains the model.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_AI_DOCUMENT_INPUT_LOCATION_T Type

The location of the inputs.

Syntax
```

```

Fields

Field Description

`source_type`

(required) The type of input location. The allowed values are: - `OBJECT_STORAGE_LOCATIONS`: A list of object locations in Object Storage. - `INLINE_DOCUMENT_CONTENT`: The content of an inline document.

Allowed values are: 'OBJECT_STORAGE_LOCATIONS', 'INLINE_DOCUMENT_CONTENT'

### DBMS_CLOUD_OCI_AI_DOCUMENT_PROCESSOR_CONFIG_T Type

The configuration of a processor.

Syntax
```

```

Fields

Field Description

`processor_type`

(required) The type of the processor.

Allowed values are: 'GENERAL'

### DBMS_CLOUD_OCI_AI_DOCUMENT_CREATE_PROCESSOR_JOB_DETAILS_T Type

The details used to create a processor job.

Syntax
```

```

Fields

Field Description

`input_location`

(required)

`output_location`

(required)

`compartment_id`

(required) The compartment identifier.

`display_name`

(optional) The display name of the processor job.

`processor_config`

(required)

### DBMS_CLOUD_OCI_AI_DOCUMENT_CREATE_PROJECT_DETAILS_T Type

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_DATA_SCIENCE_LABELING_DATASET_T Type

The dataset created by the Data Labeling Service.

Syntax
```

```

`dbms_cloud_oci_ai_document_data_science_labeling_dataset_t`is a subtype of the`dbms_cloud_oci_ai_document_dataset_t`type.

Fields

Field Description

`dataset_id`

(required) OCID of the Data Labeling dataset.

### DBMS_CLOUD_OCI_AI_DOCUMENT_DATASET_SUMMARY_T Type

Summary of count of samples used during model training.

Syntax
```

```

Fields

Field Description

`training_sample_count`

(optional) Number of samples used for training the model.

`validation_sample_count`

(optional) Number of samples used for validating the model.

`test_sample_count`

(optional) Number of samples used for testing the model.

### DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_CLASSIFICATION_CONFIDENCE_ENTRY_T Type

Confidence Entry.

Syntax
```

```

Fields

Field Description

`threshold`

(required) Threshold used to calculate precision and recall.

`precision`

(required) Precision under the threshold

`recall`

(required) Recall under the threshold

`f1_score`

(required) f1Score under the threshold

### DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_CLASSIFICATION_FEATURE_T Type

Identifying the document type.

Syntax
```

```

`dbms_cloud_oci_ai_document_document_classification_feature_t`is a subtype of the`dbms_cloud_oci_ai_document_document_feature_t`type.

Fields

Field Description

`max_results`

(optional) The maximum number of results to return.

`model_id`

(optional) The custom model ID.

`tenancy_id`

(optional) The custom model tenancy ID when modelId represents aliasName.

### DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_CLASSIFICATION_CONFIDENCE_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_ai_document_document_classification_confidence_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_CLASSIFICATION_LABEL_METRICS_REPORT_T Type

Label Metrics report for Document Classification Model.

Syntax
```

```

Fields

Field Description

`label`

(optional) Label name

`mean_average_precision`

(required) Mean average precision under different thresholds

`confidence_entries`

(required) List of document classification confidence report.

### DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_CLASSIFICATION_OVERALL_METRICS_REPORT_T Type

Overall Metrics report for Document Classification Model.

Syntax
```

```

Fields

Field Description

`mean_average_precision`

(required) Mean average precision under different thresholds

`confidence_entries`

(required) List of document classification confidence report.

### DBMS_CLOUD_OCI_AI_DOCUMENT_MODEL_METRICS_T Type

Trained Model Metrics.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The type of custom model trained.

Allowed values are: 'KEY_VALUE_EXTRACTION', 'DOCUMENT_CLASSIFICATION'

`dataset_summary`

(optional)

### DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_CLASSIFICATION_LABEL_METRICS_REPORT_TBL Type

Nested table type of dbms_cloud_oci_ai_document_document_classification_label_metrics_report_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_CLASSIFICATION_MODEL_METRICS_T Type

Metrics for Document Classification Model.

Syntax
```

```

`dbms_cloud_oci_ai_document_document_classification_model_metrics_t`is a subtype of the`dbms_cloud_oci_ai_document_model_metrics_t`type.

Fields

Field Description

`label_metrics_report`

(required) List of metrics entries per label.

`overall_metrics_report`

(required)

### DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_KEY_VALUE_EXTRACTION_FEATURE_T Type

Extracting form fields.

Syntax
```

```

`dbms_cloud_oci_ai_document_document_key_value_extraction_feature_t`is a subtype of the`dbms_cloud_oci_ai_document_document_feature_t`type.

Fields

Field Description

`model_id`

(optional) The custom model ID.

`tenancy_id`

(optional) The custom model tenancy ID when modelId represents aliasName.

### DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_LANGUAGE_CLASSIFICATION_FEATURE_T Type

Detecting the language of the document.

Syntax
```

```

`dbms_cloud_oci_ai_document_document_language_classification_feature_t`is a subtype of the`dbms_cloud_oci_ai_document_document_feature_t`type.

Fields

Field Description

`max_results`

(optional) The maximum number of results to return.

### DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_TABLE_EXTRACTION_FEATURE_T Type

Detecting and extracting data in tables.

Syntax
```

```

`dbms_cloud_oci_ai_document_document_table_extraction_feature_t`is a subtype of the`dbms_cloud_oci_ai_document_document_feature_t`type.

### DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_TEXT_EXTRACTION_FEATURE_T Type

Text recognition

Syntax
```

```

`dbms_cloud_oci_ai_document_document_text_extraction_feature_t`is a subtype of the`dbms_cloud_oci_ai_document_document_feature_t`type.

Fields

Field Description

`generate_searchable_pdf`

(optional) Whether or not to generate a searchable PDF file.

### DBMS_CLOUD_OCI_AI_DOCUMENT_ERROR_T Type

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_GENERAL_PROCESSOR_CONFIG_T Type

The configuration of a general processor.

Syntax
```

```

`dbms_cloud_oci_ai_document_general_processor_config_t`is a subtype of the`dbms_cloud_oci_ai_document_processor_config_t`type.

Fields

Field Description

`document_type`

(optional) The document type.

Allowed values are: 'INVOICE', 'RECEIPT', 'RESUME', 'TAX_FORM', 'DRIVER_LICENSE', 'PASSPORT', 'BANK_STATEMENT', 'CHECK', 'PAYSLIP', 'OTHERS'

`features`

(required) The types of document analysis requested.

`is_zip_output_enabled`

(optional) Whether or not to generate a ZIP file containing the results.

`language`

(optional) The document language, abbreviated according to the BCP 47 Language-Tag syntax.

### DBMS_CLOUD_OCI_AI_DOCUMENT_INLINE_DOCUMENT_CONTENT_T Type

The content of an inline document.

Syntax
```

```

`dbms_cloud_oci_ai_document_inline_document_content_t`is a subtype of the`dbms_cloud_oci_ai_document_input_location_t`type.

Fields

Field Description

`data`

(required) Raw document data with Base64 encoding.

### DBMS_CLOUD_OCI_AI_DOCUMENT_INLINE_DOCUMENT_DETAILS_T Type

The document incorporated in the request payload.

Syntax
```

```

`dbms_cloud_oci_ai_document_inline_document_details_t`is a subtype of the`dbms_cloud_oci_ai_document_document_details_t`type.

Fields

Field Description

`data`

(required) Raw document data with Base64 encoding.

### DBMS_CLOUD_OCI_AI_DOCUMENT_KEY_VALUE_DETECTION_CONFIDENCE_ENTRY_T Type

Key Value Detection Confidence Entry.

Syntax
```

```

Fields

Field Description

`threshold`

(required) Threshold used to calculate precision and recall.

`precision`

(required) Precision under the threshold

`recall`

(required) Recall under the threshold

`f1_score`

(required) f1Score under the threshold

`accuracy`

(required) accuracy under the threshold

### DBMS_CLOUD_OCI_AI_DOCUMENT_KEY_VALUE_DETECTION_CONFIDENCE_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_ai_document_key_value_detection_confidence_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_KEY_VALUE_DETECTION_LABEL_METRICS_REPORT_T Type

Label Metrics report for Key Value Detection Model.

Syntax
```

```

Fields

Field Description

`label`

(optional) Label name

`document_count`

(optional) Total test documents in the label.

`mean_average_precision`

(required) Mean average precision under different thresholds

`confidence_entries`

(required) List of key value detection confidence report.

### DBMS_CLOUD_OCI_AI_DOCUMENT_KEY_VALUE_DETECTION_OVERALL_METRICS_REPORT_T Type

Overall Metrics report for Key Value Detection Model.

Syntax
```

```

Fields

Field Description

`document_count`

(optional) Total test documents in the label.

`mean_average_precision`

(required) Mean average precision under different thresholds

`confidence_entries`

(required) List of key value detection confidence report.

### DBMS_CLOUD_OCI_AI_DOCUMENT_KEY_VALUE_DETECTION_LABEL_METRICS_REPORT_TBL Type

Nested table type of dbms_cloud_oci_ai_document_key_value_detection_label_metrics_report_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_KEY_VALUE_DETECTION_MODEL_METRICS_T Type

Metrics for Document Key Value Detection Model.

Syntax
```

```

`dbms_cloud_oci_ai_document_key_value_detection_model_metrics_t`is a subtype of the`dbms_cloud_oci_ai_document_model_metrics_t`type.

Fields

Field Description

`label_metrics_report`

(required) List of metrics entries per label.

`overall_metrics_report`

(required)

### DBMS_CLOUD_OCI_AI_DOCUMENT_MODEL_T Type

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

(required) The type of the Document model.

Allowed values are: 'KEY_VALUE_EXTRACTION', 'DOCUMENT_CLASSIFICATION'

`tenancy_id`

(optional) The tenancy id of the model.

`alias_name`

(optional) the alias name of the model.

`labels`

(optional) The collection of labels used to train the custom model.

`is_quick_mode`

(optional) Set to true when experimenting with a new model type or dataset, so model training is quick, with a predefined low number of passes through the training data.

`max_training_time_in_hours`

(optional) The maximum model training time in hours, expressed as a decimal fraction.

`trained_time_in_hours`

(optional) The total hours actually used for model training.

`training_dataset`

(optional)

`testing_dataset`

(optional)

`validation_dataset`

(optional)

`component_models`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)collection of active custom Key Value models that need to be composed.

`is_composed_model`

(optional) Set to true when the model is created by using multiple key value extraction models.

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

`metrics`

(optional)

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. For example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_AI_DOCUMENT_MODEL_SUMMARY_T Type

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

(required) The type of the Document model.

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

`tenancy_id`

(optional) The tenancy id of the model.

`alias_name`

(optional) the alias name of the model.

`training_dataset`

(optional)

`testing_dataset`

(optional)

`validation_dataset`

(optional)

`component_models`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)list of active custom Key Value models that need to be composed.

`is_composed_model`

(optional) Set to true when the model is created by using multiple key value extraction models.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. For example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_AI_DOCUMENT_MODEL_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_ai_document_model_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_MODEL_COLLECTION_T Type

The results of a model search.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of models.

### DBMS_CLOUD_OCI_AI_DOCUMENT_OBJECT_LOCATION_T Type

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_OBJECT_STORAGE_DATASET_T Type

The dataset that resides in Object Storage.

Syntax
```

```

`dbms_cloud_oci_ai_document_object_storage_dataset_t`is a subtype of the`dbms_cloud_oci_ai_document_dataset_t`type.

Fields

Field Description

`namespace_name`

(required) The namespace name of the Object Storage bucket that contains the input data file.

`bucket_name`

(required) The name of the Object Storage bucket that contains the input data file.

`object_name`

(required) The object name of the input data file.

### DBMS_CLOUD_OCI_AI_DOCUMENT_OBJECT_STORAGE_DOCUMENT_DETAILS_T Type

A document in OCI Object Storage.

Syntax
```

```

`dbms_cloud_oci_ai_document_object_storage_document_details_t`is a subtype of the`dbms_cloud_oci_ai_document_document_details_t`type.

Fields

Field Description

`namespace_name`

(required) The Object Storage namespace.

`bucket_name`

(required) The Object Storage bucket name.

`object_name`

(required) The Object Storage object name.

### DBMS_CLOUD_OCI_AI_DOCUMENT_OBJECT_LOCATION_TBL Type

Nested table type of dbms_cloud_oci_ai_document_object_location_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_OBJECT_STORAGE_LOCATIONS_T Type

A list of object locations in Object Storage.

Syntax
```

```

`dbms_cloud_oci_ai_document_object_storage_locations_t`is a subtype of the`dbms_cloud_oci_ai_document_input_location_t`type.

Fields

Field Description

`object_locations`

(required) The list of ObjectLocations.

### DBMS_CLOUD_OCI_AI_DOCUMENT_PATCH_MODEL_OPERATION_T Type

The metadata which can be edited after model creation.

Syntax
```

```

Fields

Field Description

`path`

(optional) The parameter of the resource to be changed.

`value`

(optional) The value of the parameter to be updated.

`operation`

(optional) The value of the parameter to be updated.

Allowed values are: 'DELETE', 'ADD', 'REPLACE'

### DBMS_CLOUD_OCI_AI_DOCUMENT_PATCH_MODEL_OPERATION_TBL Type

Nested table type of dbms_cloud_oci_ai_document_patch_model_operation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_PATCH_MODEL_DETAILS_T Type

The model parameters to be updated using patch operation.

Syntax
```

```

Fields

Field Description

`operations`

(optional) A list of patch operations for model.

### DBMS_CLOUD_OCI_AI_DOCUMENT_PATCH_RESPONSE_MESSAGE_T Type

The response containing the details of the patch operation status.

Syntax
```

```

Fields

Field Description

`message`

(required) The response message containing details of operation.

`model_id`

(optional) Model ID representing the conflicting patch operation.

`compartment_id`

(optional) Compartment ID representing the conflicting Model Compartment.

### DBMS_CLOUD_OCI_AI_DOCUMENT_PROCESSOR_JOB_T Type

Details of a processor job.

Syntax
```

```

Fields

Field Description

`id`

(required) The id of the processor job.

`compartment_id`

(required) The compartment identifier.

`display_name`

(optional) The display name of the processor job.

`processor_config`

(required)

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

(required) The current state of the processor job.

Allowed values are: 'SUCCEEDED', 'FAILED', 'ACCEPTED', 'CANCELED', 'IN_PROGRESS', 'CANCELING'

`lifecycle_details`

(optional) The detailed status of FAILED state.

Allowed values are: 'PARTIALLY_SUCCEEDED', 'COMPLETELY_FAILED'

### DBMS_CLOUD_OCI_AI_DOCUMENT_PROJECT_T Type

A Document Project containing models.

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

(required) The compartment identifier.

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_PROJECT_SUMMARY_T Type

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

`description`

(optional) An optional description of the project.

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_PROJECT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_ai_document_project_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_PROJECT_COLLECTION_T Type

The results of a project search.

Syntax
```

```

Fields

Field Description

`items`

(required) List of projects.

### DBMS_CLOUD_OCI_AI_DOCUMENT_UPDATE_MODEL_DETAILS_T Type

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_UPDATE_PROJECT_DETAILS_T Type

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_VALUE_ARRAY_T Type

The array of field values.

Syntax
```

```

`dbms_cloud_oci_ai_document_value_array_t`is a subtype of the`dbms_cloud_oci_ai_document_field_value_t`type.

Fields

Field Description

`items`

(required) The array of values.

### DBMS_CLOUD_OCI_AI_DOCUMENT_VALUE_DATE_T Type

The date field value.

Syntax
```

```

`dbms_cloud_oci_ai_document_value_date_t`is a subtype of the`dbms_cloud_oci_ai_document_field_value_t`type.

Fields

Field Description

`value`

(required) The date field value as yyyy-mm-dd.

### DBMS_CLOUD_OCI_AI_DOCUMENT_VALUE_INTEGER_T Type

The integer field value.

Syntax
```

```

`dbms_cloud_oci_ai_document_value_integer_t`is a subtype of the`dbms_cloud_oci_ai_document_field_value_t`type.

Fields

Field Description

`value`

(required) The integer value.

### DBMS_CLOUD_OCI_AI_DOCUMENT_VALUE_NUMBER_T Type

The floating point number field value.

Syntax
```

```

`dbms_cloud_oci_ai_document_value_number_t`is a subtype of the`dbms_cloud_oci_ai_document_field_value_t`type.

Fields

Field Description

`value`

(required) The number value.

### DBMS_CLOUD_OCI_AI_DOCUMENT_VALUE_PHONE_NUMBER_T Type

The phone number field value.

Syntax
```

```

`dbms_cloud_oci_ai_document_value_phone_number_t`is a subtype of the`dbms_cloud_oci_ai_document_field_value_t`type.

Fields

Field Description

`value`

(required) The phone number field value.

### DBMS_CLOUD_OCI_AI_DOCUMENT_VALUE_STRING_T Type

The string field value.

Syntax
```

```

`dbms_cloud_oci_ai_document_value_string_t`is a subtype of the`dbms_cloud_oci_ai_document_field_value_t`type.

Fields

Field Description

`value`

(required) The string text.

### DBMS_CLOUD_OCI_AI_DOCUMENT_VALUE_TIME_T Type

The time field value.

Syntax
```

```

`dbms_cloud_oci_ai_document_value_time_t`is a subtype of the`dbms_cloud_oci_ai_document_field_value_t`type.

Fields

Field Description

`value`

(required) The time field value as yyyy-mm-dd hh-mm-ss.

### DBMS_CLOUD_OCI_AI_DOCUMENT_WORK_REQUEST_RESOURCE_T Type

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

`metadata`

(optional) Additional information that helps to explain the resource.

### DBMS_CLOUD_OCI_AI_DOCUMENT_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_ai_document_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_WORK_REQUEST_T Type

The workrequest status details.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The type of work request.

Allowed values are: 'CREATE_PROJECT', 'UPDATE_PROJECT', 'DELETE_PROJECT', 'MOVE_PROJECT', 'CREATE_MODEL', 'UPDATE_MODEL', 'DELETE_MODEL', 'MOVE_MODEL', 'COMPOSE_MODEL'

`status`

(required) The status of the current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The ID of the work request.

`compartment_id`

(required) The compartment identifier.

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_WORK_REQUEST_ERROR_T Type

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_ai_document_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_WORK_REQUEST_ERROR_COLLECTION_T Type

The results of a workRequestError search.

Syntax
```

```

Fields

Field Description

`items`

(required) the list of workRequestError objects.

### DBMS_CLOUD_OCI_AI_DOCUMENT_WORK_REQUEST_LOG_ENTRY_T Type

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_ai_document_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

The results of a workRequestLog search.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of workRequestLogEntries.

### DBMS_CLOUD_OCI_AI_DOCUMENT_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The type of the work request.

Allowed values are: 'CREATE_PROJECT', 'UPDATE_PROJECT', 'DELETE_PROJECT', 'MOVE_PROJECT', 'CREATE_MODEL', 'UPDATE_MODEL', 'DELETE_MODEL', 'MOVE_MODEL', 'COMPOSE_MODEL'

`status`

(required) The status of the current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The ID of the work request.

`compartment_id`

(required) The compartment identifier.

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

### DBMS_CLOUD_OCI_AI_DOCUMENT_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_ai_document_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_DOCUMENT_WORK_REQUEST_SUMMARY_COLLECTION_T Type

The results of a workRequest search.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of workRequestSummary objects.

- [AI Document Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-F1CAFF67-5BF8-4866-84B0-AE24FEA4299A)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-59E50B9B-979C-44E6-B195-DD620AA5F658)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_FEATURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-A055068C-5147-4A39-8C85-15800C5831AD)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-A9F677F6-C435-40EC-962D-6A4D7270A6D8)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_OUTPUT_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-AE492702-3A0A-4FF3-A967-2D7487B67DDA)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-0D62AF60-1624-449B-92FF-A853DC73571A)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DIMENSIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-E94CF00B-BCDC-4C66-BCC4-260CB16C24E6)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DETECTED_DOCUMENT_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-CBAFEF72-4439-4C0B-8CB5-19E25792D08A)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DETECTED_LANGUAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-3DA323B9-A85B-4941-BEF1-4CFC45A19BED)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_NORMALIZED_VERTEX_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-14614E18-1696-4E50-8664-AACC8008F30E)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_NORMALIZED_VERTEX_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-4D197898-E6D9-4FA9-9D06-369575F3B17C)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_BOUNDING_POLYGON_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-7E33B603-42A7-46D4-A7C5-80B825DD6882)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_WORD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-55E61BDC-DCE8-4118-B52C-B53555000954)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_NUMBER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-698D6477-8D06-468B-9FD5-545372B9D105)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_LINE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-A4CD1F4C-9158-4ECC-A799-12A8626CCF69)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_CELL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-C0AD6A9F-FB21-4C05-ABED-7CBFA695CDCC)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_CELL_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-1A763266-479F-4C2F-BDC5-335F09960659)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_TABLE_ROW_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-422C540C-1CAD-45EC-9CAE-CE0C39393B42)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_TABLE_ROW_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-0F6B02CB-EEAD-45FB-A6F5-D701300307F3)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_TABLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-6EBBDB5C-0FED-4114-B7ED-DF8194534CFF)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_FIELD_LABEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-CD17A96E-AAC2-41D8-8266-CD3A668D6BE9)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_FIELD_NAME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-D2C13D58-F10D-41CF-AF2A-31FD78F5491E)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_FIELD_VALUE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-16F8864D-6FE8-48DE-AEEB-CE27999330BA)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_FIELD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-235AF8D1-C277-47D8-94A0-5B1B0667C58A)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DETECTED_DOCUMENT_TYPE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-60E83974-89AE-426B-9CDC-3A8D3C1ECC88)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DETECTED_LANGUAGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-50017BB9-3561-4428-B5A2-B2065FE8B5B9)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_WORD_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-18F083D8-0958-40B0-A8A3-D53A093AD693)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_LINE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-21C89650-AAA5-49D4-9226-3206CF1E5718)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_TABLE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-742F87E9-C763-4218-8DF4-8C03A4A18B1E)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_FIELD_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-8B2108DB-52EE-41E5-BD33-3D6A06205546)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_PAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-F46AB6A8-403E-4B9F-B318-AE17D28B6B89)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_PROCESSING_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-2E07519E-D684-4D48-83B6-F71B0E1E822F)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_PAGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-54707877-15AD-4244-893F-75AC9A23CBEB)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_PROCESSING_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-CF0A96ED-E4E7-4131-964D-032522655383)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_ANALYZE_DOCUMENT_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-0C73102A-3B0B-4339-83B1-8E3CA5DFAF5D)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_FEATURE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-506EA6D5-7487-4B9B-8D20-846C66883463)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_ANALYZE_DOCUMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-73F018B4-3C56-4B10-BB57-4289CC3B893D)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_CHANGE_MODEL_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-A48EFCC7-FEB7-458D-A41A-F3A5D03E35D6)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_CHANGE_PROJECT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-41A6AEE0-0EF3-45A2-981E-4ADA24A67552)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_COMPONENT_MODEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-B4C209DF-2ED0-45C6-ADC7-2BBAC5EECF70)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DATASET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-0D09A98B-B249-4678-B0EF-F1D76BBB6DD2)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_COMPONENT_MODEL_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-1FF1C3E1-CAB1-4031-907A-4D3A9F2D57AF)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_CREATE_MODEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-65C0585C-8F4F-4E0B-B22E-5030A91D43A0)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_INPUT_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-11B84284-DC28-466B-978B-745370A22E70)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_PROCESSOR_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-BE0635DC-C07F-440A-9434-AA3D95B120B7)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_CREATE_PROCESSOR_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-889EC456-DB20-4345-8143-12A87DBE95D7)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_CREATE_PROJECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-FC96757D-EA08-4D5C-80C9-415BD6D624B6)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DATA_SCIENCE_LABELING_DATASET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-AC43DE4B-488E-4B86-AF47-925829B7CFA1)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DATASET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-0FB27ED2-B08C-4D18-9200-583E9F1E2B2B)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_CLASSIFICATION_CONFIDENCE_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-CD03EF3E-9B07-4A19-8F25-902B6AE567AE)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_CLASSIFICATION_FEATURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-1581BEA7-F938-43E0-A092-8C5AB4814A60)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_CLASSIFICATION_CONFIDENCE_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-DB1F3BAA-5B56-44B7-A316-359A5DDB6838)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_CLASSIFICATION_LABEL_METRICS_REPORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-0960AA50-3D80-443A-93C8-1D2626FEA5DF)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_CLASSIFICATION_OVERALL_METRICS_REPORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-AA131592-1A22-44DD-A0CC-DBFD0EE94D02)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_MODEL_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-25CB92C6-A6A1-4A3C-9683-998985CBD481)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_CLASSIFICATION_LABEL_METRICS_REPORT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-4B8E6B87-2406-4D5B-A4DB-8C940323EED1)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_CLASSIFICATION_MODEL_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-D4D35514-8AA5-4835-81AE-AFB93DD1C2D9)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_KEY_VALUE_EXTRACTION_FEATURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-00C1225A-D923-4DCE-9D0E-F8AB0E42A966)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_LANGUAGE_CLASSIFICATION_FEATURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-2779D1C3-886C-4F7E-82F5-4D41B79EBEE8)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_TABLE_EXTRACTION_FEATURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-E27753DE-223C-4A55-BB97-70193EBB5C5B)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_DOCUMENT_TEXT_EXTRACTION_FEATURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-79AE47F8-9EAD-46AC-B767-30E35ED12DBC)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-C684B005-5E09-46B3-BB21-29B16E6817D4)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_GENERAL_PROCESSOR_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-680A4926-1DAB-45C6-BEF3-309CD0896997)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_INLINE_DOCUMENT_CONTENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-3BDDD2E8-EF8A-43AB-9CD1-8B24E111F96F)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_INLINE_DOCUMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-42C3F6B2-6C20-4B4A-88EB-3C38923ED685)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_KEY_VALUE_DETECTION_CONFIDENCE_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-C1538D13-8AFB-4DF7-8992-70D9AB2EC1AC)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_KEY_VALUE_DETECTION_CONFIDENCE_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-3D37033D-97E6-4A8C-96D0-C48C06D58D73)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_KEY_VALUE_DETECTION_LABEL_METRICS_REPORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-0220BE4E-78B5-4C92-85D8-8433E73A3BF8)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_KEY_VALUE_DETECTION_OVERALL_METRICS_REPORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-2C6E2005-C198-4EE8-8ABC-E2781115B066)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_KEY_VALUE_DETECTION_LABEL_METRICS_REPORT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-21877438-DC1C-48BD-9C8A-E578ACBAB8B9)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_KEY_VALUE_DETECTION_MODEL_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-2EFD42A3-F570-4ED6-AFBA-9A1BCA64963D)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_MODEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-28099243-2FAD-4A71-8CD1-740D7EA8D444)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_MODEL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-B3D0F7F1-B40A-4802-92E1-1AFC6968312E)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_MODEL_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-AF520758-72B7-461B-AA42-F185EF370831)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_MODEL_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-CE8C6618-C8E6-4233-8BC2-78DE69CFCCFF)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_OBJECT_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-E7C8FC54-4CA8-46F9-84EC-D160805AEB92)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_OBJECT_STORAGE_DATASET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-FE22807A-0951-4CEE-9C95-719989192D3E)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_OBJECT_STORAGE_DOCUMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-ED24006E-311A-412B-879F-AC2F6945A732)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_OBJECT_LOCATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-25612E58-A4EF-41EA-B33B-C2D151FA1D7E)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_OBJECT_STORAGE_LOCATIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-41F508D1-CEA0-4717-A8A1-4C9261F17DB9)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_PATCH_MODEL_OPERATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-53EC423C-7DC6-4946-B260-3CF6646EF07C)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_PATCH_MODEL_OPERATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-B29682F5-1631-4741-B6E6-E56DF12B7386)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_PATCH_MODEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-45C7A492-60C0-4EE8-8D5A-72ACB248F574)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_PATCH_RESPONSE_MESSAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-C19CCEC6-3C71-4093-8EEA-02412C8475C6)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_PROCESSOR_JOB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-7F0DF058-00BB-4411-9875-B0F3D2B4E4D2)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_PROJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-DDD65A3F-7098-4FDE-9DA2-E72352F22A5C)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_PROJECT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-C63A41B3-A4B8-43B9-B2E8-D272F6C07B65)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_PROJECT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-C7239B88-F398-4463-A139-D619CE8954F6)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_PROJECT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-1F5434FF-BC79-4282-B9D9-E06A5FE102B3)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_UPDATE_MODEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-CC442B64-6145-42B0-8FDC-64674196F98B)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_UPDATE_PROJECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-5B7211AB-892A-4665-A853-A3FC55159AD6)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_VALUE_ARRAY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-2288EC71-5E45-4414-AEA0-626B4D8DDF86)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_VALUE_DATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-B5343947-D019-4DC5-AE77-F0950D5038D4)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_VALUE_INTEGER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-172472C9-060B-4178-9C3D-0E93003E87DD)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_VALUE_NUMBER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-9C98295E-E43E-40A1-A96A-EEE034527728)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_VALUE_PHONE_NUMBER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-9C350625-6B73-4395-BD2A-6CCE04172399)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_VALUE_STRING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-6D29396F-EEB1-4A01-80B0-CAD0E2DA820A)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_VALUE_TIME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-4DB375D7-2725-443B-8747-A8E7CD65CFBF)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-8E1F7C5B-C96F-401C-8CE7-3562249935B7)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-6B600ADC-6404-4A90-9C33-D3C535378E56)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-E1D10CC0-AE18-4A4A-BAB2-0F794A167C31)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-5516A67A-BB7C-4667-859D-5B1052FF9FD0)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-ED625EDE-2942-4487-B7E1-C26E9C962E43)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-0F78C07B-B9E1-4F0C-B99F-13BE13A49976)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-1F34360C-44BE-48A5-8132-C9B9930C9938)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-048E690B-368C-42A9-B1E5-033A73436FD0)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-C56A461E-7547-4635-AF98-8145A7602289)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-6577EFA5-5E45-48A9-ACEB-49B8238D0574)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-288C9CBA-3B18-4479-B211-6D2358AA97DD)
- [DBMS_CLOUD_OCI_AI_DOCUMENT_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_document_t.html#ADSDK-GUID-D24DDAE0-AF0A-43B5-AEA4-C273797BD6EA)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
