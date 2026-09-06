# AI Language Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html
- Fetched: 2026-09-05 19:00 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#dcoc-content-body)

## AI Language Common Types

### DBMS_CLOUD_OCI_AI_LANGUAGE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_DOMINANT_LANGUAGE_DOCUMENT_T Type

The document details for language detect call.

Syntax
```

```

Fields

Field Description

`key`

(required) Document unique identifier defined by the user.

`text`

(required) Document text for detect language.

### DBMS_CLOUD_OCI_AI_LANGUAGE_DOMINANT_LANGUAGE_DOCUMENT_TBL Type

Nested table type of dbms_cloud_oci_ai_language_dominant_language_document_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_DETECT_DOMINANT_LANGUAGE_DETAILS_T Type

The documents details for language detect call.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that calls the API, inference will be served from pre trained model

`documents`

(required) List of Documents for detect language.

### DBMS_CLOUD_OCI_AI_LANGUAGE_DETECTED_LANGUAGE_T Type

Attributes to the detected language. Contains Language Name , Code, and Confidence Score.

Syntax
```

```

Fields

Field Description

`name`

(required) Full language name. Example: `English, Hindi, and so on`

`code`

(required) Detected language code as per[ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)standard. Example: `en, fr, hi etc`.

`score`

(required) Score or confidence of detected language code. Example: `0.9999856066867399`

### DBMS_CLOUD_OCI_AI_LANGUAGE_DETECTED_LANGUAGE_TBL Type

Nested table type of dbms_cloud_oci_ai_language_detected_language_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_DOMINANT_LANGUAGE_DOCUMENT_RESULT_T Type

The document response for language detect call.

Syntax
```

```

Fields

Field Description

`key`

(required) Document unique identifier defined by the user.

`languages`

(required) List of detected languages with results sorted in descending order of the scores. Most likely language is on top.

### DBMS_CLOUD_OCI_AI_LANGUAGE_ERROR_DETAILS_T Type

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

### DBMS_CLOUD_OCI_AI_LANGUAGE_DOCUMENT_ERROR_T Type

Error response for document.

Syntax
```

```

Fields

Field Description

`key`

(required) Document unique identifier defined by the user.

`error`

(required)

### DBMS_CLOUD_OCI_AI_LANGUAGE_DOMINANT_LANGUAGE_DOCUMENT_RESULT_TBL Type

Nested table type of dbms_cloud_oci_ai_language_dominant_language_document_result_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_DOCUMENT_ERROR_TBL Type

Nested table type of dbms_cloud_oci_ai_language_document_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_DETECT_DOMINANT_LANGUAGE_RESULT_T Type

Result of language detect call.

Syntax
```

```

Fields

Field Description

`documents`

(required) List of succeeded document response.

`errors`

(optional) List of failed document response.

### DBMS_CLOUD_OCI_AI_LANGUAGE_TEXT_DOCUMENT_T Type

The document details for language service call.

Syntax
```

```

Fields

Field Description

`key`

(required) Document unique identifier defined by the user.

`text`

(required) Document text for language service call.

`language_code`

(optional) Language code of the document. Please refer to respective model[API documentation](https://docs.oracle.com/iaas/language/using/overview.htm)for supported languages.

### DBMS_CLOUD_OCI_AI_LANGUAGE_TEXT_DOCUMENT_TBL Type

Nested table type of dbms_cloud_oci_ai_language_text_document_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_DETECT_LANGUAGE_ENTITIES_DETAILS_T Type

The documents details for entities detect call.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that calls the API, inference will be served from pre trained model

`endpoint_id`

(optional) The endpoint which have to be used for inferencing. If endpointId and compartmentId is provided, then inference will be served from custom model which is mapped to this Endpoint.

`documents`

(required) List of Documents for detect entities.

### DBMS_CLOUD_OCI_AI_LANGUAGE_HIERARCHICAL_ENTITY_T Type

Hierarchical entity object

Syntax
```

```

Fields

Field Description

`offset`

(optional) The number of Unicode code points preceding this entity in the submitted text.

`length`

(optional) Length of entity text

`text`

(optional) Entity text like name of person, location, and so on.

`l_type`

(optional) Type of entity text like PER, LOC.

`sub_type`

(optional) Sub-type of entity text like GPE for LOCATION type

`score`

(optional) Score or confidence for detected entity.

### DBMS_CLOUD_OCI_AI_LANGUAGE_HIERARCHICAL_ENTITY_TBL Type

Nested table type of dbms_cloud_oci_ai_language_hierarchical_entity_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_ENTITY_DOCUMENT_RESULT_T Type

The document response for entities detect call.

Syntax
```

```

Fields

Field Description

`key`

(required) Document unique identifier defined by the user.

`entities`

(required) List of detected entities.

`language_code`

(required) Language code supported - auto : Automatically detect language - ar : Arabic - pt-BR : Brazilian Portuguese - cs : Czech - da : Danish - nl : Dutch - en : English - fi : Finnish - fr : French - fr-CA : Canadian French - de : German - it : Italian - ja : Japanese - ko : Korean - no : Norwegian - pl : Polish - ro : Romanian - zh-CN : Simplified Chinese - es : Spanish - sv : Swedish - zh-TW : Traditional Chinese - tr : Turkish - el : Greek - he : Hebrew

### DBMS_CLOUD_OCI_AI_LANGUAGE_ENTITY_DOCUMENT_RESULT_TBL Type

Nested table type of dbms_cloud_oci_ai_language_entity_document_result_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_DETECT_LANGUAGE_ENTITIES_RESULT_T Type

Result of entities detect call.

Syntax
```

```

Fields

Field Description

`documents`

(required) List of succeeded document response.

`errors`

(optional) List of failed document response.

### DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_DETECT_LANGUAGE_KEY_PHRASES_DETAILS_T Type

The documents details for keyPhrases call.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that calls the API, inference will be served from pre trained model

`documents`

(required) List of Documents for detect keyPhrases.

### DBMS_CLOUD_OCI_AI_LANGUAGE_KEY_PHRASE_T Type

Key phrase for the given text.

Syntax
```

```

Fields

Field Description

`text`

(required) Key phrase exreacted from given text.

`score`

(required) Score or confidence of the key phrase. Example: `0.9999856066867399`

### DBMS_CLOUD_OCI_AI_LANGUAGE_KEY_PHRASE_TBL Type

Nested table type of dbms_cloud_oci_ai_language_key_phrase_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_KEY_PHRASE_DOCUMENT_RESULT_T Type

The document response for keyPhrases detect call.

Syntax
```

```

Fields

Field Description

`key`

(required) Document unique identifier defined by the user.

`key_phrases`

(required) List of detected keyPhrases.

`language_code`

(required) Language code supported - auto : Automatically detect language - ar : Arabic - pt-BR : Brazilian Portuguese - cs : Czech - da : Danish - nl : Dutch - en : English - fi : Finnish - fr : French - fr-CA : Canadian French - de : German - it : Italian - ja : Japanese - ko : Korean - no : Norwegian - pl : Polish - ro : Romanian - zh-CN : Simplified Chinese - es : Spanish - sv : Swedish - zh-TW : Traditional Chinese - tr : Turkish - el : Greek - he : Hebrew

### DBMS_CLOUD_OCI_AI_LANGUAGE_KEY_PHRASE_DOCUMENT_RESULT_TBL Type

Nested table type of dbms_cloud_oci_ai_language_key_phrase_document_result_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_DETECT_LANGUAGE_KEY_PHRASES_RESULT_T Type

Result of keyPhrases detect call.

Syntax
```

```

Fields

Field Description

`documents`

(required) List of succeeded document response.

`errors`

(optional) List of failed document response.

### DBMS_CLOUD_OCI_AI_LANGUAGE_PII_ENTITY_MASKING_T Type

Mask recognized PII entities with different modes.

Syntax
```

```

Fields

Field Description

`l_mode`

(required) The type of masking mode.

Allowed values are: 'REPLACE', 'MASK', 'REMOVE'

### DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_DETECT_LANGUAGE_PII_ENTITIES_DETAILS_T Type

The documents details to detect personal identification information.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that calls the API, inference will be served from pre trained model

`documents`

(required) List of documents to detect personal identification information.

`masking`

(optional) Mask recognized PII entities with different modes.

### DBMS_CLOUD_OCI_AI_LANGUAGE_PII_ENTITY_T Type

PII entity object.

Syntax
```

```

Fields

Field Description

`offset`

(optional) The number of Unicode code points preceding this entity in the submitted text.

`length`

(optional) Length of PII entity text.

`text`

(optional) Entity text like name of person, Organization and so on.

`l_type`

(optional) Type of PII entity text like PER, LOC.

`score`

(optional) Score or confidence for detected PII entity.

### DBMS_CLOUD_OCI_AI_LANGUAGE_PII_ENTITY_TBL Type

Nested table type of dbms_cloud_oci_ai_language_pii_entity_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_PII_ENTITY_DOCUMENT_RESULT_T Type

The document response for batch detect personal identification.

Syntax
```

```

Fields

Field Description

`key`

(required) Document unique identifier defined by the user.

`entities`

(required) List of batch detect personal identification.

`masked_text`

(required) Masked text per given mask mode.

`language_code`

(required) Language code supported - auto : Automatically detect language - ar : Arabic - pt-BR : Brazilian Portuguese - cs : Czech - da : Danish - nl : Dutch - en : English - fi : Finnish - fr : French - fr-CA : Canadian French - de : German - it : Italian - ja : Japanese - ko : Korean - no : Norwegian - pl : Polish - ro : Romanian - zh-CN : Simplified Chinese - es : Spanish - sv : Swedish - zh-TW : Traditional Chinese - tr : Turkish - el : Greek - he : Hebrew

### DBMS_CLOUD_OCI_AI_LANGUAGE_PII_ENTITY_DOCUMENT_RESULT_TBL Type

Nested table type of dbms_cloud_oci_ai_language_pii_entity_document_result_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_DETECT_LANGUAGE_PII_ENTITIES_RESULT_T Type

Result of batch detect personal identification.

Syntax
```

```

Fields

Field Description

`documents`

(required) List of succeeded document response.

`errors`

(optional) List of failed document response.

### DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_DETECT_LANGUAGE_SENTIMENTS_DETAILS_T Type

The documents details for sentiment call.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that calls the API, inference will be served from pre trained model

`documents`

(required) List of Documents for detect sentiments.

### DBMS_CLOUD_OCI_AI_LANGUAGE_SENTIMENT_ASPECT_T Type

Sentiment aspect object.

Syntax
```

```

Fields

Field Description

`offset`

(optional) The number of Unicode code points preceding this entity in the submitted text.

`length`

(optional) Length of aspect text.

`text`

(optional) Aspect text.

`sentiment`

(optional) The highest-score sentiment for the aspect text.

`scores`

(optional) Scores or confidences for each sentiment. Example: `{\"positive\": 1.0, \"negative\": 0.0}`

### DBMS_CLOUD_OCI_AI_LANGUAGE_SENTIMENT_SENTENCE_T Type

Sentiment sentence object.

Syntax
```

```

Fields

Field Description

`offset`

(optional) The number of Unicode code points preceding this entity in the submitted text.

`length`

(optional) Length of sentence text.

`text`

(optional) Sentence text.

`sentiment`

(optional) The highest-score sentiment for the sentence text.

`scores`

(optional) Scores or confidences for each sentiment. Example: `{\"positive\": 1.0, \"negative\": 0.0}`

### DBMS_CLOUD_OCI_AI_LANGUAGE_SENTIMENT_ASPECT_TBL Type

Nested table type of dbms_cloud_oci_ai_language_sentiment_aspect_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_SENTIMENT_SENTENCE_TBL Type

Nested table type of dbms_cloud_oci_ai_language_sentiment_sentence_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_SENTIMENT_DOCUMENT_RESULT_T Type

The document response for sentiment detect call.

Syntax
```

```

Fields

Field Description

`key`

(required) Document unique identifier defined by the user.

`document_sentiment`

(optional) Document level sentiment.

`document_scores`

(optional) Scores for each sentiment. Example: {\"positive\": 1.0, \"negative\": 0.0}

`aspects`

(required) List of detected aspects sentiment.

`sentences`

(optional) List of detected sentences sentiment.

`language_code`

(required) Language code supported - auto : Automatically detect language - ar : Arabic - pt-BR : Brazilian Portuguese - cs : Czech - da : Danish - nl : Dutch - en : English - fi : Finnish - fr : French - fr-CA : Canadian French - de : German - it : Italian - ja : Japanese - ko : Korean - no : Norwegian - pl : Polish - ro : Romanian - zh-CN : Simplified Chinese - es : Spanish - sv : Swedish - zh-TW : Traditional Chinese - tr : Turkish - el : Greek - he : Hebrew

### DBMS_CLOUD_OCI_AI_LANGUAGE_SENTIMENT_DOCUMENT_RESULT_TBL Type

Nested table type of dbms_cloud_oci_ai_language_sentiment_document_result_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_DETECT_LANGUAGE_SENTIMENTS_RESULT_T Type

Result of sentiments detect call.

Syntax
```

```

Fields

Field Description

`documents`

(required) List of succeeded document response.

`errors`

(optional) List of failed document response.

### DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_DETECT_LANGUAGE_TEXT_CLASSIFICATION_DETAILS_T Type

The documents details for text classification call.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that calls the API, inference will be served from pre trained model

`endpoint_id`

(optional) The endpoint which have to be used for inferencing. If endpointId and compartmentId is provided, then inference will be served from custom model which is mapped to this Endpoint.

`documents`

(required) List of Documents for detect text classification.

### DBMS_CLOUD_OCI_AI_LANGUAGE_TEXT_CLASSIFICATION_T Type

Text label and score for the given text.

Syntax
```

```

Fields

Field Description

`label`

(required) Label of the the given text.

`score`

(required) Score or confidence of extracted text label. Example: `0.9999856066867399`

### DBMS_CLOUD_OCI_AI_LANGUAGE_TEXT_CLASSIFICATION_TBL Type

Nested table type of dbms_cloud_oci_ai_language_text_classification_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_TEXT_CLASSIFICATION_DOCUMENT_RESULT_T Type

The document response for test classification detect call.

Syntax
```

```

Fields

Field Description

`key`

(required) Document unique identifier defined by the user.

`text_classification`

(required) List of detected text classes.

`language_code`

(required) Language code supported - auto : Automatically detect language - ar : Arabic - pt-BR : Brazilian Portuguese - cs : Czech - da : Danish - nl : Dutch - en : English - fi : Finnish - fr : French - fr-CA : Canadian French - de : German - it : Italian - ja : Japanese - ko : Korean - no : Norwegian - pl : Polish - ro : Romanian - zh-CN : Simplified Chinese - es : Spanish - sv : Swedish - zh-TW : Traditional Chinese - tr : Turkish - el : Greek - he : Hebrew

### DBMS_CLOUD_OCI_AI_LANGUAGE_TEXT_CLASSIFICATION_DOCUMENT_RESULT_TBL Type

Nested table type of dbms_cloud_oci_ai_language_text_classification_document_result_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_DETECT_LANGUAGE_TEXT_CLASSIFICATION_RESULT_T Type

Result of text classification detect call.

Syntax
```

```

Fields

Field Description

`documents`

(required) List of succeeded document response.

`errors`

(optional) List of failed document response.

### DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_LANGUAGE_TRANSLATION_DETAILS_T Type

The documents details for translation call.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that calls the API, inference will be served from pre trained model

`target_language_code`

(optional) Language code supported - auto : Automatically detect language - ar : Arabic - pt-BR : Brazilian Portuguese - cs : Czech - da : Danish - nl : Dutch - en : English - fi : Finnish - fr : French - fr-CA : Canadian French - de : German - it : Italian - ja : Japanese - ko : Korean - no : Norwegian - pl : Polish - ro : Romanian - zh-CN : Simplified Chinese - es : Spanish - sv : Swedish - zh-TW : Traditional Chinese - tr : Turkish - el : Greek - he : Hebrew

`documents`

(required) List of documents for translation.

### DBMS_CLOUD_OCI_AI_LANGUAGE_TRANSLATION_DOCUMENT_RESULT_T Type

The document response for translation call.

Syntax
```

```

Fields

Field Description

`key`

(required) Document unique identifier defined by the user.

`translated_text`

(required) Translated text in selected target language.

`source_language_code`

(required) Language code supported - auto : Automatically detect language - ar : Arabic - pt-BR : Brazilian Portuguese - cs : Czech - da : Danish - nl : Dutch - en : English - fi : Finnish - fr : French - fr-CA : Canadian French - de : German - it : Italian - ja : Japanese - ko : Korean - no : Norwegian - pl : Polish - ro : Romanian - zh-CN : Simplified Chinese - es : Spanish - sv : Swedish - zh-TW : Traditional Chinese - tr : Turkish - el : Greek - he : Hebrew

`target_language_code`

(required) Language code supported - auto : Automatically detect language - ar : Arabic - pt-BR : Brazilian Portuguese - cs : Czech - da : Danish - nl : Dutch - en : English - fi : Finnish - fr : French - fr-CA : Canadian French - de : German - it : Italian - ja : Japanese - ko : Korean - no : Norwegian - pl : Polish - ro : Romanian - zh-CN : Simplified Chinese - es : Spanish - sv : Swedish - zh-TW : Traditional Chinese - tr : Turkish - el : Greek - he : Hebrew

### DBMS_CLOUD_OCI_AI_LANGUAGE_TRANSLATION_DOCUMENT_RESULT_TBL Type

Nested table type of dbms_cloud_oci_ai_language_translation_document_result_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_LANGUAGE_TRANSLATION_RESULT_T Type

Result of translation call.

Syntax
```

```

Fields

Field Description

`documents`

(required) List of succeeded document response.

`errors`

(optional) List of failed document response.

### DBMS_CLOUD_OCI_AI_LANGUAGE_CAPABILITY_T Type

Capability supported

Syntax
```

```

Fields

Field Description

`details`

(optional) values

### DBMS_CLOUD_OCI_AI_LANGUAGE_CAPABILITIES_T Type

Capabilities supported

Syntax
```

```

Fields

Field Description

`capability`

(optional) Model information capabilities related to version

### DBMS_CLOUD_OCI_AI_LANGUAGE_CHANGE_ENDPOINT_COMPARTMENT_DETAILS_T Type

Details for changing the compartment of an Endpoint.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_AI_LANGUAGE_CHANGE_MODEL_COMPARTMENT_DETAILS_T Type

Details for changing the compartment of an Model.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_AI_LANGUAGE_CHANGE_PROJECT_COMPARTMENT_DETAILS_T Type

Details for changing the compartment of a Project.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_AI_LANGUAGE_CLASS_METRICS_T Type

class level Text Classification model metrics

Syntax
```

```

Fields

Field Description

`label`

(required) Text classification label

`f1`

(required) F1-score, is a measure of a model’s accuracy on a dataset

`precision`

(required) Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true positives plus the number of false positives)

`recall`

(required) Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what was actually tagged. The recall metric reveals how many of the predicted classes are correct.

`support`

(optional) number of samples in the test set

### DBMS_CLOUD_OCI_AI_LANGUAGE_CLASSIFICATION_TYPE_T Type

possible text classification modes

Syntax
```

```

Fields

Field Description

`classification_mode`

(required) classification Modes

Allowed values are: 'MULTI_CLASS', 'MULTI_LABEL'

### DBMS_CLOUD_OCI_AI_LANGUAGE_CLASSIFICATION_MULTI_CLASS_MODE_DETAILS_T Type

Possible text classification multi class mode details

Syntax
```

```

`dbms_cloud_oci_ai_language_classification_multi_class_mode_details_t`is a subtype of the`dbms_cloud_oci_ai_language_classification_type_t`type.

Fields

Field Description

`version`

(optional) Optional if nothing specified latest base model will be used for training. Supported versions can be found at /modelTypes/{modelType}

### DBMS_CLOUD_OCI_AI_LANGUAGE_CLASSIFICATION_MULTI_LABEL_MODE_DETAILS_T Type

Possible text classification multi label mode details

Syntax
```

```

`dbms_cloud_oci_ai_language_classification_multi_label_mode_details_t`is a subtype of the`dbms_cloud_oci_ai_language_classification_type_t`type.

Fields

Field Description

`version`

(optional) Optional if nothing specified latest base model will be used for training. Supported versions can be found at /modelTypes/{modelType}

### DBMS_CLOUD_OCI_AI_LANGUAGE_CONFUSION_MATRIX_DETAILS_T Type

confusion matrix details

Syntax
```

```

Fields

Field Description

`matrix`

(optional) confusion matrix data

### DBMS_CLOUD_OCI_AI_LANGUAGE_CREATE_ENDPOINT_DETAILS_T Type

The information needed to create a new endpoint and expose to end users.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name for the resource. It should be unique and can be modified. Avoid entering confidential information.

`description`

(optional) A short description of the an endpoint.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)compartment identifier for the endpoint

`model_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model to associate with the endpoint.

`inference_units`

(optional) Number of replicas required for this endpoint. This will be optional parameter. Default will be 1.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_AI_LANGUAGE_MODEL_DETAILS_T Type

Possible model types

Syntax
```

```

Fields

Field Description

`language_code`

(optional) supported language default value is en

`model_type`

(required) Model type

Allowed values are: 'NAMED_ENTITY_RECOGNITION', 'TEXT_CLASSIFICATION', 'PRE_TRAINED_NAMED_ENTITY_RECOGNITION', 'PRE_TRAINED_TEXT_CLASSIFICATION', 'PRE_TRAINED_SENTIMENT_ANALYSIS', 'PRE_TRAINED_KEYPHRASE_EXTRACTION', 'PRE_TRAINED_LANGUAGE_DETECTION', 'PRE_TRAINED_PII', 'PRE_TRAINED_TRANSLATION', 'PRE_TRAINED_HEALTH_NLU', 'PRE_TRAINED_SUMMARIZATION', 'PRE_TRAINED_UNIVERSAL'

### DBMS_CLOUD_OCI_AI_LANGUAGE_DATASET_DETAILS_T Type

Possible data set type

Syntax
```

```

Fields

Field Description

`dataset_type`

(required) Possible data sets

Allowed values are: 'OBJECT_STORAGE', 'DATA_SCIENCE_LABELING'

### DBMS_CLOUD_OCI_AI_LANGUAGE_TEST_STRATEGY_T Type

Possible strategy as testing and validation(optional) dataset.

Syntax
```

```

Fields

Field Description

`strategy_type`

(required) This information will define the test strategy different datasets for test and validation(optional) dataset.

Allowed values are: 'TEST_AND_VALIDATION_DATASET'

### DBMS_CLOUD_OCI_AI_LANGUAGE_CREATE_MODEL_DETAILS_T Type

The information needed to train a new model

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.

`description`

(optional) A short description of the a model.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the models compartment.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project to associate with the model.

`model_details`

(required)

`training_dataset`

(optional)

`test_strategy`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_AI_LANGUAGE_CREATE_PROJECT_DETAILS_T Type

Parameters needed to create a new project. Projects enable users to organise their language work.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.

`description`

(optional) A short description of the project.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the project's compartment.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_AI_LANGUAGE_DATA_SCIENCE_LABELING_DATASET_T Type

Dataset that uses data science labelling service as underlying data source.

Syntax
```

```

`dbms_cloud_oci_ai_language_data_science_labeling_dataset_t`is a subtype of the`dbms_cloud_oci_ai_language_dataset_details_t`type.

Fields

Field Description

`dataset_id`

(required) Data Science Labelling Service OCID

### DBMS_CLOUD_OCI_AI_LANGUAGE_DETECT_DOMINANT_LANGUAGE_DETAILS_T Type

The document details for language detect call.

Syntax
```

```

Fields

Field Description

`text`

(required) Document text for detect language.

### DBMS_CLOUD_OCI_AI_LANGUAGE_DETECT_DOMINANT_LANGUAGE_RESULT_T Type

Result of language detect call.

Syntax
```

```

Fields

Field Description

`languages`

(required) List of detected languages with results sorted in descending order of the scores. Most likely language is on top.

### DBMS_CLOUD_OCI_AI_LANGUAGE_DETECT_LANGUAGE_ENTITIES_DETAILS_T Type

The document details for entities detect call.

Syntax
```

```

Fields

Field Description

`text`

(required) Document text for detect entities.

### DBMS_CLOUD_OCI_AI_LANGUAGE_ENTITY_T Type

entity object

Syntax
```

```

Fields

Field Description

`offset`

(optional) The number of Unicode code points preceding this entity in the submitted text.

`length`

(optional) Length of entity text

`text`

(optional) Entity text like name of person, location, and so on.

`l_type`

(optional) Type of entity text like PER, LOC, GPE and NOPE.

`is_pii`

(optional) This flag is to indicate if it is PII entity or not.

`score`

(optional) Score or confidence of extracted entity type. Example: `0.9999856066867399`

### DBMS_CLOUD_OCI_AI_LANGUAGE_ENTITY_TBL Type

Nested table type of dbms_cloud_oci_ai_language_entity_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_DETECT_LANGUAGE_ENTITIES_RESULT_T Type

Result of entities detect call.

Syntax
```

```

Fields

Field Description

`entities`

(required) List of detected entities.

### DBMS_CLOUD_OCI_AI_LANGUAGE_DETECT_LANGUAGE_KEY_PHRASES_DETAILS_T Type

The document details for a keyPhrases detect call.

Syntax
```

```

Fields

Field Description

`text`

(required) Document text for detect keyPhrases.

### DBMS_CLOUD_OCI_AI_LANGUAGE_DETECT_LANGUAGE_KEY_PHRASES_RESULT_T Type

Result of a language keyPhrases detect call.

Syntax
```

```

Fields

Field Description

`key_phrases`

(required) List of detected keyPhrases.

### DBMS_CLOUD_OCI_AI_LANGUAGE_DETECT_LANGUAGE_SENTIMENTS_DETAILS_T Type

The document details for sentiments detect call.

Syntax
```

```

Fields

Field Description

`text`

(required) Document text for detect sentiments.

### DBMS_CLOUD_OCI_AI_LANGUAGE_DETECT_LANGUAGE_SENTIMENTS_RESULT_T Type

Result of sentiments detect call.

Syntax
```

```

Fields

Field Description

`aspects`

(required) List of detected aspects.

### DBMS_CLOUD_OCI_AI_LANGUAGE_DETECT_LANGUAGE_TEXT_CLASSIFICATION_DETAILS_T Type

The document details for text classification detect call.

Syntax
```

```

Fields

Field Description

`text`

(required) Document text for detect text classes.

### DBMS_CLOUD_OCI_AI_LANGUAGE_DETECT_LANGUAGE_TEXT_CLASSIFICATION_RESULT_T Type

Result of text classification detect call.

Syntax
```

```

Fields

Field Description

`text_classification`

(required) List of detected text classes.

### DBMS_CLOUD_OCI_AI_LANGUAGE_ENDPOINT_T Type

Description of the endpoint.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier endpoint OCID of an endpoint that is immutable on creation.

`display_name`

(required) A user-friendly display name for the resource. It should be unique and can be modified. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the endpoint compartment.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project to associate with the Endpoint.

`description`

(optional) A short description of the endpoint.

`time_created`

(required) The time the the endpoint was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the endpoint was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The state of the endpoint.

Allowed values are: 'DELETING', 'DELETED', 'FAILED', 'CREATING', 'ACTIVE', 'UPDATING'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in failed state.

`inference_units`

(optional) Number of replicas required for this endpoint.

`model_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model to associate with the endpoint.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{ \"orcl-cloud\": { \"free-tier-retained\": \"true\" } }`

### DBMS_CLOUD_OCI_AI_LANGUAGE_ENDPOINT_SUMMARY_T Type

Summary of the language endpoint.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier endpoint OCID of an endpoint that is immutable on creation.

`display_name`

(required) A user-friendly display name for the resource. It should be unique and can be modified. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the Endpoint compartment.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project to associate with the endpoint.

`description`

(optional) A short description of the endpoint.

`time_created`

(required) The time the the endpoint was created. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The state of the endpoint.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in failed state.

`inference_units`

(optional) Number of replicas required for this endpoint. This will be optional parameter. Default will be 1.

`model_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model to associate with the endpoint.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{ \"orcl-cloud\": { \"free-tier-retained\": \"true\" } }`

### DBMS_CLOUD_OCI_AI_LANGUAGE_ENDPOINT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_ai_language_endpoint_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_ENDPOINT_COLLECTION_T Type

Results of an endpoint list. Contains EndpointSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of endpoints

### DBMS_CLOUD_OCI_AI_LANGUAGE_ENTITY_LABEL_ERROR_ANALYSIS_T Type

Possible entity error label error details

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of entity text like PER, LOC, GPE, NOPE etc.

`offset`

(required) Starting index on text.

`length`

(required) Length of text

### DBMS_CLOUD_OCI_AI_LANGUAGE_ENTITY_METRICS_T Type

Entity level named entity recognition model metrics

Syntax
```

```

Fields

Field Description

`label`

(required) Entity label

`f1`

(required) F1-score, is a measure of a model’s accuracy on a dataset

`precision`

(required) Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true positives plus the number of false positives)

`recall`

(required) Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what was actually tagged. The recall metric reveals how many of the predicted classes are correct.

### DBMS_CLOUD_OCI_AI_LANGUAGE_ERROR_T Type

Error information.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_AI_LANGUAGE_EVALUATION_RESULT_SUMMARY_T Type

model evaluation analysis of different models

Syntax
```

```

Fields

Field Description

`model_type`

(required) Model type

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_AI_LANGUAGE_EVALUATION_RESULT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_ai_language_evaluation_result_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_EVALUATION_RESULT_COLLECTION_T Type

Results of a model evaluation analysis search. Contains EvaluationResultSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of model evaluation analysis

### DBMS_CLOUD_OCI_AI_LANGUAGE_EVALUATION_RESULTS_T Type

model training results of different models

Syntax
```

```

Fields

Field Description

`model_type`

(required) Model type

### DBMS_CLOUD_OCI_AI_LANGUAGE_LOCATION_DETAILS_T Type

Possible object storage location types

Syntax
```

```

Fields

Field Description

`location_type`

(required) Possible object storage location types

Allowed values are: 'OBJECT_LIST'

### DBMS_CLOUD_OCI_AI_LANGUAGE_MODEL_T Type

Description of the a Model.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier model OCID of a model that is immutable on creation

`display_name`

(required) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the model's compartment.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project to associate with the model.

`description`

(optional) A short description of the Model.

`model_details`

(required)

`time_created`

(required) The time the the model was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the model was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The state of the model.

Allowed values are: 'DELETING', 'DELETED', 'FAILED', 'CREATING', 'ACTIVE', 'UPDATING'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in failed state.

`training_dataset`

(optional)

`evaluation_results`

(optional)

`test_strategy`

(optional)

`version`

(optional) For pre trained models this will identify model type version used for model creation For custom identifying the model by model id is difficult. This param provides ease of use for end customer. &lt;&lt;service&gt;&gt;::&lt;&lt;service-name&gt;&gt;_&lt;&lt;model-type-version&gt;&gt;::&lt;&lt;custom model on which this training has to be done&gt;&gt; ex: ai-lang::NER_V1::CUSTOM-V0

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{ \"orcl-cloud\": { \"free-tier-retained\": \"true\" } }`

### DBMS_CLOUD_OCI_AI_LANGUAGE_MODEL_SUMMARY_T Type

Summary of the language Model.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier model OCID of a model that is immutable on creation

`display_name`

(required) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the model's compartment.

`description`

(optional) A short description of the Model.

`model_details`

(required)

`time_created`

(required) The time the the Model was created. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The state of the model.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in failed state.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project to associate with the model.

`version`

(optional) For pre trained models this will identify model type version used for model creation For custom identifying the model by model id is difficult. This param provides ease of use for end customer. &lt;&lt;service&gt;&gt;::&lt;&lt;service-name&gt;&gt;-&lt;&lt;model-type-version&gt;&gt;::&lt;&lt;custom model on which this training has to be done&gt;&gt; ex: ai-lang::NER_V1::CUSTOM-V0

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{ \"orcl-cloud\": { \"free-tier-retained\": \"true\" } }`

### DBMS_CLOUD_OCI_AI_LANGUAGE_MODEL_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_ai_language_model_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_MODEL_COLLECTION_T Type

Results of a model search. Contains ModelSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of models

### DBMS_CLOUD_OCI_AI_LANGUAGE_MODEL_TYPE_INFO_T Type

Model information like versions and capabilities

Syntax
```

```

Fields

Field Description

`versions`

(optional) Model versions available for this model type

`capabilities`

(required) Model information capabilities related to version

### DBMS_CLOUD_OCI_AI_LANGUAGE_ENTITY_LABEL_ERROR_ANALYSIS_TBL Type

Nested table type of dbms_cloud_oci_ai_language_entity_label_error_analysis_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_NAMED_ENTITY_RECOGNITION_EVALUATION_RESULT_T Type

Possible NER model error analysis

Syntax
```

```

`dbms_cloud_oci_ai_language_named_entity_recognition_evaluation_result_t`is a subtype of the`dbms_cloud_oci_ai_language_evaluation_result_summary_t`type.

Fields

Field Description

`record`

(required) For CSV format location is rowId(1 is header) and for JSONL location is jsonL line sequence(1 is metadata)

`true_entities`

(required) List of true(actual) entities in test data for NER model

`predicted_entities`

(required) List of true(actual) entities in test data for NER model

### DBMS_CLOUD_OCI_AI_LANGUAGE_NAMED_ENTITY_RECOGNITION_MODEL_METRICS_T Type

Model level named entity recognition metrics

Syntax
```

```

Fields

Field Description

`micro_f1`

(required) F1-score, is a measure of a model’s accuracy on a dataset

`micro_precision`

(required) Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true positives plus the number of false positives)

`micro_recall`

(required) Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what was actually tagged. The recall metric reveals how many of the predicted classes are correct.

`macro_f1`

(required) F1-score, is a measure of a model’s accuracy on a dataset

`macro_precision`

(required) Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true positives plus the number of false positives)

`macro_recall`

(required) Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what was actually tagged. The recall metric reveals how many of the predicted classes are correct.

`weighted_f1`

(optional) F1-score, is a measure of a model’s accuracy on a dataset

`weighted_precision`

(optional) Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true positives plus the number of false positives)

`weighted_recall`

(optional) Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what was actually tagged. The recall metric reveals how many of the predicted classes are correct.

### DBMS_CLOUD_OCI_AI_LANGUAGE_ENTITY_METRICS_TBL Type

Nested table type of dbms_cloud_oci_ai_language_entity_metrics_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_NAMED_ENTITY_RECOGNITION_EVALUATION_RESULTS_T Type

Named entity recognition model testing and evaluation results

Syntax
```

```

`dbms_cloud_oci_ai_language_named_entity_recognition_evaluation_results_t`is a subtype of the`dbms_cloud_oci_ai_language_evaluation_results_t`type.

Fields

Field Description

`metrics`

(optional)

`entity_metrics`

(optional) List of entity metrics

`confusion_matrix`

(optional) class level confusion matrix

`labels`

(optional) labels

### DBMS_CLOUD_OCI_AI_LANGUAGE_NAMED_ENTITY_RECOGNITION_MODEL_DETAILS_T Type

Possible NER model information

Syntax
```

```

`dbms_cloud_oci_ai_language_named_entity_recognition_model_details_t`is a subtype of the`dbms_cloud_oci_ai_language_model_details_t`type.

Fields

Field Description

`version`

(optional) Optional if nothing specified latest base model will be used for training. Supported versions can be found at /modelTypes/{modelType}

### DBMS_CLOUD_OCI_AI_LANGUAGE_OBJECT_LIST_DATASET_T Type

Data source details for object storage

Syntax
```

```

`dbms_cloud_oci_ai_language_object_list_dataset_t`is a subtype of the`dbms_cloud_oci_ai_language_location_details_t`type.

Fields

Field Description

`namespace_name`

(required) Object storage namespace

`bucket_name`

(required) Object storage bucket name

`object_names`

(required) Array of files which need to be processed in the bucket

### DBMS_CLOUD_OCI_AI_LANGUAGE_OBJECT_STORAGE_DATASET_T Type

Different type of location types supported for object storage

Syntax
```

```

`dbms_cloud_oci_ai_language_object_storage_dataset_t`is a subtype of the`dbms_cloud_oci_ai_language_dataset_details_t`type.

Fields

Field Description

`location_details`

(required)

### DBMS_CLOUD_OCI_AI_LANGUAGE_PII_ENTITY_MASK_T Type

Mask PII entities with the given masking character.

Syntax
```

```

`dbms_cloud_oci_ai_language_pii_entity_mask_t`is a subtype of the`dbms_cloud_oci_ai_language_pii_entity_masking_t`type.

Fields

Field Description

`masking_character`

(optional) Masking character. By default, the character is an asterisk (*)

`leave_characters_unmasked`

(optional) Number of characters to leave unmasked. By default, the whole entity is masked.

`is_unmasked_from_end`

(optional) Unmask from the end. By default, the whole entity is masked. This field works in concert with leaveCharactersUnmasked. For example, leaveCharactersUnmasked is 3 and isUnmaskedFromEnd is true, then if the entity is India the masked entity/result is **dia.

### DBMS_CLOUD_OCI_AI_LANGUAGE_PII_ENTITY_REMOVE_T Type

Remove PII entities from output.

Syntax
```

```

`dbms_cloud_oci_ai_language_pii_entity_remove_t`is a subtype of the`dbms_cloud_oci_ai_language_pii_entity_masking_t`type.

### DBMS_CLOUD_OCI_AI_LANGUAGE_PII_ENTITY_REPLACE_T Type

Replace PII entities with a given sequence of characters.

Syntax
```

```

`dbms_cloud_oci_ai_language_pii_entity_replace_t`is a subtype of the`dbms_cloud_oci_ai_language_pii_entity_masking_t`type.

Fields

Field Description

`replace_with`

(optional) Replace entities with given sequence of characters. By default PII entity will be replaced with &lt;ENTITY_TYPE&gt;.

### DBMS_CLOUD_OCI_AI_LANGUAGE_PRE_DEPLOYED_LANGUAGE_MODELS_T Type

Description of Language Entities.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)Compartment Identifier

`description`

(optional) Language Entities Description

### DBMS_CLOUD_OCI_AI_LANGUAGE_PRE_TRAINED_HEALTH_NLU_MODEL_DETAILS_T Type

Possible pre trained health NLU model information

Syntax
```

```

`dbms_cloud_oci_ai_language_pre_trained_health_nlu_model_details_t`is a subtype of the`dbms_cloud_oci_ai_language_model_details_t`type.

Fields

Field Description

`version`

(optional) Optional pre trained model version. if nothing specified latest pre trained model will be used. Supported versions can be found at /modelTypes/{modelType}

### DBMS_CLOUD_OCI_AI_LANGUAGE_PRE_TRAINED_KEY_PHRASE_EXTRACTION_MODEL_DETAILS_T Type

Possible pre trained TXT model information

Syntax
```

```

`dbms_cloud_oci_ai_language_pre_trained_key_phrase_extraction_model_details_t`is a subtype of the`dbms_cloud_oci_ai_language_model_details_t`type.

Fields

Field Description

`version`

(optional) Optional pre trained model version. if nothing specified latest pre trained model will be used. Supported versions can be found at /modelTypes/{modelType}

### DBMS_CLOUD_OCI_AI_LANGUAGE_PRE_TRAINED_LANGUAGE_DETECTION_MODEL_DETAILS_T Type

Possible pre trained TXT model information

Syntax
```

```

`dbms_cloud_oci_ai_language_pre_trained_language_detection_model_details_t`is a subtype of the`dbms_cloud_oci_ai_language_model_details_t`type.

Fields

Field Description

`version`

(optional) Optional pre trained model version. if nothing specified latest pre trained model will be used. Supported versions can be found at /modelTypes/{modelType}

### DBMS_CLOUD_OCI_AI_LANGUAGE_PRE_TRAINED_NAMED_ENTITY_RECOGNITION_MODEL_DETAILS_T Type

Possible pre trained NER model information

Syntax
```

```

`dbms_cloud_oci_ai_language_pre_trained_named_entity_recognition_model_details_t`is a subtype of the`dbms_cloud_oci_ai_language_model_details_t`type.

Fields

Field Description

`version`

(optional) Optional pre trained model version. if nothing specified latest pre trained model will be used. Supported versions can be found at /modelTypes/{modelType}

### DBMS_CLOUD_OCI_AI_LANGUAGE_PRE_TRAINED_PHI_MODEL_DETAILS_T Type

Possible pre trained PHI model information

Syntax
```

```

`dbms_cloud_oci_ai_language_pre_trained_phi_model_details_t`is a subtype of the`dbms_cloud_oci_ai_language_model_details_t`type.

Fields

Field Description

`version`

(optional) Optional pre trained model version. if nothing specified latest pre trained model will be used. Supported versions can be found at /modelTypes/{modelType}

### DBMS_CLOUD_OCI_AI_LANGUAGE_PRE_TRAINED_PII_MODEL_DETAILS_T Type

Possible pre trained PII model information

Syntax
```

```

`dbms_cloud_oci_ai_language_pre_trained_pii_model_details_t`is a subtype of the`dbms_cloud_oci_ai_language_model_details_t`type.

Fields

Field Description

`version`

(optional) Optional pre trained model version. if nothing specified latest pre trained model will be used. Supported versions can be found at /modelTypes/{modelType}

### DBMS_CLOUD_OCI_AI_LANGUAGE_PRE_TRAINED_SENTIMENT_ANALYSIS_MODEL_DETAILS_T Type

Possible pre trained TXT model information

Syntax
```

```

`dbms_cloud_oci_ai_language_pre_trained_sentiment_analysis_model_details_t`is a subtype of the`dbms_cloud_oci_ai_language_model_details_t`type.

Fields

Field Description

`version`

(optional) Optional pre trained model version. if nothing specified latest pre trained model will be used. Supported versions can be found at /modelTypes/{modelType}

### DBMS_CLOUD_OCI_AI_LANGUAGE_PRE_TRAINED_SUMMARIZATION_T Type

Possible pre trained summarization information

Syntax
```

```

`dbms_cloud_oci_ai_language_pre_trained_summarization_t`is a subtype of the`dbms_cloud_oci_ai_language_model_details_t`type.

Fields

Field Description

`version`

(optional) Optional pre trained model version. if nothing specified latest pre trained model will be used. Supported versions can be found at /modelTypes/{modelType}

### DBMS_CLOUD_OCI_AI_LANGUAGE_PRE_TRAINED_TEXT_CLASSIFICATION_MODEL_DETAILS_T Type

Possible pre trained TXT model information

Syntax
```

```

`dbms_cloud_oci_ai_language_pre_trained_text_classification_model_details_t`is a subtype of the`dbms_cloud_oci_ai_language_model_details_t`type.

Fields

Field Description

`version`

(optional) Optional pre trained model version. if nothing specified latest pre trained model will be used. Supported versions can be found at /modelTypes/{modelType}

### DBMS_CLOUD_OCI_AI_LANGUAGE_PRE_TRAINED_UNIVERSAL_MODEL_T Type

Possible pre trained universal model information

Syntax
```

```

`dbms_cloud_oci_ai_language_pre_trained_universal_model_t`is a subtype of the`dbms_cloud_oci_ai_language_model_details_t`type.

Fields

Field Description

`version`

(optional) Optional pre trained model version. if nothing specified latest pre trained model will be used. Supported versions can be found at /modelTypes/{modelType}

### DBMS_CLOUD_OCI_AI_LANGUAGE_PROJECT_T Type

Project enable users to organize their project resources.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier OCID of the project

`display_name`

(required) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the project's compartment.

`description`

(optional) A short description of a project.

`time_created`

(required) The date and time the resource was created in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_updated`

(optional) The date and time the resource was updated in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`lifecycle_state`

(required) The state of the project.

Allowed values are: 'DELETING', 'DELETED', 'FAILED', 'CREATING', 'ACTIVE', 'UPDATING'

`lifecycle_details`

(optional) A message describing the current state in more detail.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{ \"orcl-cloud\": { \"free-tier-retained\": \"true\" } }`

### DBMS_CLOUD_OCI_AI_LANGUAGE_PROJECT_SUMMARY_T Type

Summary of the project.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier OCID of a project

`display_name`

(required) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.

`description`

(optional) A short description of the project.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the project's compartment.

`time_created`

(required) The date and time the resource was created in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_updated`

(optional) The date and time the resource was updated in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`lifecycle_state`

(required) The state of the project.

`lifecycle_details`

(optional) A message describing the current state in more detail.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{ \"orcl-cloud\": { \"free-tier-retained\": \"true\" } }`

### DBMS_CLOUD_OCI_AI_LANGUAGE_PROJECT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_ai_language_project_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_PROJECT_COLLECTION_T Type

Results of a Project List. Contains ProjectSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of projects

### DBMS_CLOUD_OCI_AI_LANGUAGE_TEST_AND_VALIDATION_DATASET_STRATEGY_T Type

This information will be used capture training, testing and validation dataset.

Syntax
```

```

`dbms_cloud_oci_ai_language_test_and_validation_dataset_strategy_t`is a subtype of the`dbms_cloud_oci_ai_language_test_strategy_t`type.

Fields

Field Description

`testing_dataset`

(required)

`validation_dataset`

(optional)

### DBMS_CLOUD_OCI_AI_LANGUAGE_TEXT_CLASSIFICATION_MODEL_METRICS_T Type

Model level text classification metrics

Syntax
```

```

Fields

Field Description

`accuracy`

(required) The fraction of the labels that were correctly recognised .

`micro_f1`

(required) F1-score, is a measure of a model’s accuracy on a dataset

`micro_precision`

(required) Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true positives plus the number of false positives)

`micro_recall`

(required) Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what was actually tagged. The recall metric reveals how many of the predicted classes are correct.

`macro_f1`

(required) F1-score, is a measure of a model’s accuracy on a dataset

`macro_precision`

(required) Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true positives plus the number of false positives)

`macro_recall`

(required) Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what was actually tagged. The recall metric reveals how many of the predicted classes are correct.

`weighted_f1`

(optional) F1-score, is a measure of a model’s accuracy on a dataset

`weighted_precision`

(optional) Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true positives plus the number of false positives)

`weighted_recall`

(optional) Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what was actually tagged. The recall metric reveals how many of the predicted classes are correct.

### DBMS_CLOUD_OCI_AI_LANGUAGE_CLASS_METRICS_TBL Type

Nested table type of dbms_cloud_oci_ai_language_class_metrics_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_TEXT_CLASSIFICATION_EVALUATION_RESULTS_T Type

Text Classification model testing and evaluation results

Syntax
```

```

`dbms_cloud_oci_ai_language_text_classification_evaluation_results_t`is a subtype of the`dbms_cloud_oci_ai_language_evaluation_results_t`type.

Fields

Field Description

`metrics`

(optional)

`class_metrics`

(optional) List of text classification metrics

`confusion_matrix`

(optional) class level confusion matrix

`labels`

(optional) labels

### DBMS_CLOUD_OCI_AI_LANGUAGE_TEXT_CLASSIFICATION_MODEL_DETAILS_T Type

Possible TextClassificationModelDetails

Syntax
```

```

`dbms_cloud_oci_ai_language_text_classification_model_details_t`is a subtype of the`dbms_cloud_oci_ai_language_model_details_t`type.

Fields

Field Description

`classification_mode`

(optional)

### DBMS_CLOUD_OCI_AI_LANGUAGE_TEXT_CLASSIFICATION_MODEL_EVALUATION_RESULT_T Type

Possible TXTC model error analysis

Syntax
```

```

`dbms_cloud_oci_ai_language_text_classification_model_evaluation_result_t`is a subtype of the`dbms_cloud_oci_ai_language_evaluation_result_summary_t`type.

Fields

Field Description

`location`

(required) For CSV format location is rowId(1 is header) and for JSONL location is jsonL line sequence(1 is metadata)

`true_labels`

(required) List of true(actual) labels in test data for multi class or multi label TextClassification

`predicted_labels`

(optional) List of predicted labels by custom multi class or multi label TextClassification model

### DBMS_CLOUD_OCI_AI_LANGUAGE_UPDATE_ENDPOINT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name for the resource. It should be unique and can be modified. Avoid entering confidential information.

`description`

(optional) A short description of the endpoint.

`model_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model to associate with the endpoint.

`inference_units`

(optional) Number of replicas required for this endpoint. This will be optional parameter.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_AI_LANGUAGE_UPDATE_MODEL_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.

`description`

(optional) A short description of the a model.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_AI_LANGUAGE_UPDATE_PROJECT_DETAILS_T Type

The information to be updated for the project.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.

`description`

(optional) A short description of the project.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_AI_LANGUAGE_WORK_REQUEST_RESOURCE_T Type

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

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata

### DBMS_CLOUD_OCI_AI_LANGUAGE_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_ai_language_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_WORK_REQUEST_T Type

A description of workrequest status

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'CREATE_MODEL', 'UPDATE_MODEL', 'DELETE_MODEL', 'CREATE_PROJECT', 'UPDATE_PROJECT', 'DELETE_PROJECT', 'CREATE_ENDPOINT', 'UPDATE_ENDPOINT', 'DELETE_ENDPOINT'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'WAITING', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'NEEDS_ATTENTION'

`id`

(required) Unique identifier work request OCID of work request that is immutable on creation

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

`resources`

(optional) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_AI_LANGUAGE_WORK_REQUEST_ERROR_T Type

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

### DBMS_CLOUD_OCI_AI_LANGUAGE_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_ai_language_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestError objects.

### DBMS_CLOUD_OCI_AI_LANGUAGE_WORK_REQUEST_LOG_T Type

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

### DBMS_CLOUD_OCI_AI_LANGUAGE_WORK_REQUEST_LOG_TBL Type

Nested table type of dbms_cloud_oci_ai_language_work_request_log_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_WORK_REQUEST_LOG_COLLECTION_T Type

Results of a workRequestLog search. Contains both workRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestLogEntries.

### DBMS_CLOUD_OCI_AI_LANGUAGE_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'CREATE_MODEL', 'UPDATE_MODEL', 'DELETE_MODEL', 'CREATE_PROJECT', 'UPDATE_PROJECT', 'DELETE_PROJECT', 'CREATE_ENDPOINT', 'UPDATE_ENDPOINT', 'DELETE_ENDPOINT'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'WAITING', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'NEEDS_ATTENTION'

`id`

(required) Unique identifier work request OCID of work request that is immutable on creation

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

`resources`

(optional) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_AI_LANGUAGE_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_ai_language_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_LANGUAGE_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestSummary objects.

- [AI Language Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-6F526202-97E5-490A-AA9B-8C8948FC9826)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-CF873B5C-FC96-4D19-9E1C-5B91EDBD9245)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_DOMINANT_LANGUAGE_DOCUMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-D3013320-D571-458E-B66C-FCFE6C37AFC7)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_DOMINANT_LANGUAGE_DOCUMENT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-84E4F9EF-FC20-492D-B4ED-3A2ED3BC8340)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_DETECT_DOMINANT_LANGUAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-D064F4BE-51B6-431B-A85B-E11D5EEBD344)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_DETECTED_LANGUAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-EEB9A8E5-FC03-46BD-928E-F692C5757F94)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_DETECTED_LANGUAGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-A44C8D19-084F-4508-929A-584A9D17D3B3)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_DOMINANT_LANGUAGE_DOCUMENT_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-0D1A6F5B-D736-4068-B72B-AF2B8B1BFD35)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_ERROR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-89A7277B-27D0-4FF9-8FCF-CFF1D8849F6E)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_DOCUMENT_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-B1A61316-B172-4CB4-97C8-862C9E58E712)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_DOMINANT_LANGUAGE_DOCUMENT_RESULT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-F4F5437B-0F33-45E6-ACA3-248D7D106574)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_DOCUMENT_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-22C7AEC5-A9A3-45CE-A318-B767AB648001)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_DETECT_DOMINANT_LANGUAGE_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-2ED99E61-F012-4A3C-B3E3-4D9330BBFE93)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_TEXT_DOCUMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-64B8ED87-EE10-471E-B591-644556A251BA)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_TEXT_DOCUMENT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-C2E280B7-8641-4634-A42C-FDED5E0F7EC6)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_DETECT_LANGUAGE_ENTITIES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-E467B2E3-0899-41FF-BEE6-6F9B5FC96DAB)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_HIERARCHICAL_ENTITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-A3DCEA69-E067-4DD0-A85E-A43F6FF844A8)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_HIERARCHICAL_ENTITY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-6962E5E6-A2E2-4393-B750-1D2C92C446A7)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_ENTITY_DOCUMENT_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-3ECEF70B-6950-407F-A6EB-9605CDB9B4DB)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_ENTITY_DOCUMENT_RESULT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-F3E0280F-907D-49C2-A085-967BA824BBD5)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_DETECT_LANGUAGE_ENTITIES_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-2AA2D8BE-A113-4FFB-9C43-7C2C5F53C74D)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_DETECT_LANGUAGE_KEY_PHRASES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-8F17A24D-3190-44BB-AAB7-433C8356FBFE)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_KEY_PHRASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-C88C6F8F-5809-4C16-852E-4DAB0DC8BC6F)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_KEY_PHRASE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-BDCD5924-74A3-4EF1-B873-FC27D68FCA16)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_KEY_PHRASE_DOCUMENT_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-F899014F-62F3-474D-AA74-87640F7F65C7)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_KEY_PHRASE_DOCUMENT_RESULT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-BCB38411-38B0-4BE3-9835-F4D77FA67E12)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_DETECT_LANGUAGE_KEY_PHRASES_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-427CCE9A-5DCF-45D5-85DF-8C33162509D3)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_PII_ENTITY_MASKING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-0FA053A6-88CF-47F2-9B9B-449CAF35F373)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_DETECT_LANGUAGE_PII_ENTITIES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-C90472AF-87DF-481D-B2F3-32526CB04E76)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_PII_ENTITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-BA7B66D1-8651-4423-94F0-B5C27575F158)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_PII_ENTITY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-6A8F6C1F-3455-49FE-88BB-E85EBA4B0D1A)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_PII_ENTITY_DOCUMENT_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-12B8F91F-DD58-4045-B76D-247848178DE2)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_PII_ENTITY_DOCUMENT_RESULT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-90DCDFAB-3503-4C5F-8604-6EFFC8CFAE33)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_DETECT_LANGUAGE_PII_ENTITIES_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-CFD564FB-D4E1-4F7C-8AFD-C9A8D897D3B1)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_DETECT_LANGUAGE_SENTIMENTS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-3A77E325-E451-4561-AA54-AFEC8A4AA9F5)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_SENTIMENT_ASPECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-07658E41-C695-4177-B1EE-F324E7BC16E9)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_SENTIMENT_SENTENCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-AACE7433-0898-4531-A053-9D7777ADC87B)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_SENTIMENT_ASPECT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-3A124480-A33A-435B-BB9E-B036A1CF0353)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_SENTIMENT_SENTENCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-CDCC59B1-1318-4759-BA27-97E150A5AD08)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_SENTIMENT_DOCUMENT_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-66A30A3A-A449-4AAF-957E-8E9C2DDB0A99)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_SENTIMENT_DOCUMENT_RESULT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-4AC099BF-4211-45F4-9A9F-70E4DA8D75F5)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_DETECT_LANGUAGE_SENTIMENTS_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-FBFB6962-30C2-4F73-A10A-987254657E9F)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_DETECT_LANGUAGE_TEXT_CLASSIFICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-DD809F4E-D102-4FA0-A62E-B4F6E81BBAE7)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_TEXT_CLASSIFICATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-C81900F6-A582-46E8-8465-3A6E0E77DDA8)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_TEXT_CLASSIFICATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-7E7A1088-5F0E-4E95-A50C-CD33F31A5B68)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_TEXT_CLASSIFICATION_DOCUMENT_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-81F32BC0-D68A-4811-BD0E-BEB2E4E99BA8)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_TEXT_CLASSIFICATION_DOCUMENT_RESULT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-AD2B0DA2-C19D-4EC7-B9E2-0560BB25A40A)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_DETECT_LANGUAGE_TEXT_CLASSIFICATION_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-AC2FEB6E-5CE3-44D9-A2D5-7B5F302B1C9C)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_LANGUAGE_TRANSLATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-04D0D3F8-BEDD-4C95-B416-7AC30B286B18)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_TRANSLATION_DOCUMENT_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-B9D81703-6980-4186-9113-9E05640B28E7)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_TRANSLATION_DOCUMENT_RESULT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-89F281FF-0730-4919-A8DF-A7858B0ABFDB)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_BATCH_LANGUAGE_TRANSLATION_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-442CB7AA-B4A5-4C03-B445-E08E6985E1B0)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_CAPABILITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-5839D91F-0827-4704-9646-2333D383A4EA)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_CAPABILITIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-9F8C3E00-D135-46AF-B6FA-0F575E9072C6)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_CHANGE_ENDPOINT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-143DA147-F9B0-4206-84A1-989C81C7CE7A)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_CHANGE_MODEL_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-C49541F9-0A5A-4C27-B8D7-37FD8FBBD635)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_CHANGE_PROJECT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-CB401803-DC8D-48E4-9938-AB4E33AEEF5C)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_CLASS_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-5B56A224-4B1E-4188-A871-1C5803571B88)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_CLASSIFICATION_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-BA66FA13-3AFC-4176-BDF0-845E34B2DDBD)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_CLASSIFICATION_MULTI_CLASS_MODE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-3E6321AA-5363-4ED5-89AC-F1D105AB6880)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_CLASSIFICATION_MULTI_LABEL_MODE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-35BFA232-A006-4BC6-8A08-FE3A338C5EE7)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_CONFUSION_MATRIX_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-8220023D-FC97-40EB-918B-1A970349FB6F)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_CREATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-91D55A63-89AA-4F33-A4CC-FFF48B48BAE4)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_MODEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-D4F7EC06-023A-4A2E-9DB5-969FB66BB4DB)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_DATASET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-DF0753E2-FD00-4E0B-937E-B6ECDDB6780D)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_TEST_STRATEGY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-EB539EBA-D274-4310-8B61-FFC5518B60F7)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_CREATE_MODEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-6A81A829-2F94-42DA-A0AD-A2CB5C5308C3)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_CREATE_PROJECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-8E29A6A9-23B7-4C0C-B040-1100DA996411)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_DATA_SCIENCE_LABELING_DATASET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-D24E5E0A-A779-4743-9A31-2E20CFC04305)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_DETECT_DOMINANT_LANGUAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-6F9CCE9E-2C75-467F-A006-68AEB8C99F12)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_DETECT_DOMINANT_LANGUAGE_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-E4FCA98F-8FA9-459F-94D2-FA8265DA0551)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_DETECT_LANGUAGE_ENTITIES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-56645DAD-F502-428F-B6B3-9AA626D50D22)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_ENTITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-48285969-2EA3-46E1-8D33-E288DBF5D7A4)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_ENTITY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-AEF42B1D-8876-47A5-A5E6-EAE3C4602887)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_DETECT_LANGUAGE_ENTITIES_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-84C3C14F-48E7-4DC2-A96F-3223AA507923)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_DETECT_LANGUAGE_KEY_PHRASES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-2AA9852C-607F-4CDE-B840-26AE910A56A3)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_DETECT_LANGUAGE_KEY_PHRASES_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-2AC885D2-A744-43FB-84A2-53DD3540AD08)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_DETECT_LANGUAGE_SENTIMENTS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-C8D54BA3-B367-44DA-8C69-65066ED764DF)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_DETECT_LANGUAGE_SENTIMENTS_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-D3237227-4316-4306-81D5-30DB475CF2CB)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_DETECT_LANGUAGE_TEXT_CLASSIFICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-DD9228A5-2A8E-4972-A4AD-FF4CE915762C)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_DETECT_LANGUAGE_TEXT_CLASSIFICATION_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-52FD70FA-C68A-44C1-AEF4-6A8AF6D54EC2)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-FF7DB145-1DD8-46BA-9D39-829C310862A2)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_ENDPOINT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-A931C7CF-1348-4586-903C-A9167245A678)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_ENDPOINT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-0B533B4D-15D2-455F-A6C5-3D59B8295835)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_ENDPOINT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-E62BBFAC-56CC-4359-8BB2-9836AE7A91C8)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_ENTITY_LABEL_ERROR_ANALYSIS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-B64936DA-FE95-424D-84C2-3259E16A9B95)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_ENTITY_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-95743962-2FF1-4166-B169-41A0B7E43EB5)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-34986733-0C9C-4145-AE0C-CEBD7B7A9795)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_EVALUATION_RESULT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-8D1E8EAE-3B45-43ED-AA21-BE3A8B2C7C61)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_EVALUATION_RESULT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-CC2CE8B8-32ED-44AC-A069-1CDD6C354A33)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_EVALUATION_RESULT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-628E2AA8-8FD5-45EA-BD64-B0236D96EC2C)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_EVALUATION_RESULTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-FC2FAE54-4F6D-4DC7-B5B1-232523055DD6)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_LOCATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-E4CEDF77-5E9F-4639-A38E-589623CB780A)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_MODEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-4878DC3E-2FF5-4264-B669-9F0409C9BAA2)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_MODEL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-AA310E54-9F95-4E4A-9E24-6FD5311CE104)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_MODEL_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-0ADD78F6-B0A1-45DF-9F4D-51834F736836)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_MODEL_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-3DD4400C-9A11-472A-BE71-02ECCFAEC7FF)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_MODEL_TYPE_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-DF7A7A11-EC7A-4DA7-8161-D064F1E6DED7)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_ENTITY_LABEL_ERROR_ANALYSIS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-6D71AC5E-F6EE-455C-B79A-B859D5C0A21D)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_NAMED_ENTITY_RECOGNITION_EVALUATION_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-B75A34A3-0217-42F8-AD94-1E7FFF1B9534)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_NAMED_ENTITY_RECOGNITION_MODEL_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-FD2A995A-0866-4083-B8BC-F9D5A6E9B655)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_ENTITY_METRICS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-0623A900-805B-4B01-A7E6-8D5F74D76FA0)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_NAMED_ENTITY_RECOGNITION_EVALUATION_RESULTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-98B5DEF3-9A6B-4DFA-A06F-5756843F509C)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_NAMED_ENTITY_RECOGNITION_MODEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-2008BC6B-AB8B-4F5E-8591-DAACC64F34A8)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_OBJECT_LIST_DATASET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-40FBB78F-33DA-46A2-8E38-DFBBBBE65FD5)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_OBJECT_STORAGE_DATASET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-2417A134-BF96-42BB-94DB-4EF7DEF8E078)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_PII_ENTITY_MASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-111E2A91-1494-423F-9510-4478BD47C28A)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_PII_ENTITY_REMOVE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-E3D43B2D-111F-42AA-B615-B6EF56250CA5)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_PII_ENTITY_REPLACE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-B2BCD40B-7747-4682-A400-C14BC08B76C9)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_PRE_DEPLOYED_LANGUAGE_MODELS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-6CC59750-C0F3-47C8-9F62-D6B34960D383)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_PRE_TRAINED_HEALTH_NLU_MODEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-943B2507-553A-4B15-B7AA-4EF36BD7DF5B)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_PRE_TRAINED_KEY_PHRASE_EXTRACTION_MODEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-26A23CBF-7F71-4DFB-9F4F-AF8860DF3688)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_PRE_TRAINED_LANGUAGE_DETECTION_MODEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-DC4357F4-486A-4AE8-8700-C04B6034993F)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_PRE_TRAINED_NAMED_ENTITY_RECOGNITION_MODEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-43CD3AF7-1D17-43E5-8856-87437351F5DF)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_PRE_TRAINED_PHI_MODEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-21D9BD87-67EB-4446-A3A1-6BD6D70B02D8)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_PRE_TRAINED_PII_MODEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-DA834C58-C079-4718-8B13-272F491938F9)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_PRE_TRAINED_SENTIMENT_ANALYSIS_MODEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-235E981B-2394-45E0-979B-B699317EBF56)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_PRE_TRAINED_SUMMARIZATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-2FA0F0BE-7CC9-49B3-9CF3-4D972D181A30)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_PRE_TRAINED_TEXT_CLASSIFICATION_MODEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-3171B9FE-854B-4F64-9E03-6E83CA825F5D)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_PRE_TRAINED_UNIVERSAL_MODEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-F1EC2B1E-4451-4BDB-8002-495FE5EFEBBD)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_PROJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-03C0A720-2FA5-4B65-8034-3EA45C28FF63)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_PROJECT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-40D8C2FB-F0D8-4683-8EBA-A096E22413CE)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_PROJECT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-A0DC0407-FED0-479C-BE92-5767581BE803)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_PROJECT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-05209FBF-C6D5-45C5-92B5-3BDDF92D20C9)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_TEST_AND_VALIDATION_DATASET_STRATEGY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-93D95E0B-5A2D-478B-ACA6-A73310028F39)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_TEXT_CLASSIFICATION_MODEL_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-94735C95-FC52-4850-B479-9F9EEF94260A)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_CLASS_METRICS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-E1371796-CEC7-42F4-B9CC-A113A938C50C)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_TEXT_CLASSIFICATION_EVALUATION_RESULTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-06B69FFE-226E-465E-9369-D609D44C0D65)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_TEXT_CLASSIFICATION_MODEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-11D130A0-12C0-4452-8A9F-5E0667F9DBC5)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_TEXT_CLASSIFICATION_MODEL_EVALUATION_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-5DCCE53B-4D99-4127-AB29-0C06593BE5A2)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_UPDATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-B843AF2A-21E9-44EF-B69D-0608E070CAC8)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_UPDATE_MODEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-7534B086-A1B1-4891-9C61-25A2D547116B)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_UPDATE_PROJECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-3B6E2C4C-CA6D-41B0-8BE9-E1ED7B947443)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-15A609CE-989D-497B-BCC1-A13D44D5E377)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-B96C66A9-9048-464C-BFAF-79792D9403F5)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-C39A5D6D-39EC-4D7F-97A1-7F069AABA01A)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-95E90B2B-FA54-4B46-BA86-E0B0074BA9DA)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-F704F2D7-B63D-4E56-8D34-602CD478278E)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-3AC5D586-9D43-4C3C-B9AD-5E817DC13B46)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_WORK_REQUEST_LOG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-30285390-64EF-4CC6-B3B6-2BD2E1898121)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_WORK_REQUEST_LOG_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-66525C88-A9A0-4610-A65A-7E52DECC00ED)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_WORK_REQUEST_LOG_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-C700C5F8-8AB7-43CE-BABD-034014835781)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-2C48BD2F-332B-4FEC-9EA5-34A581C75085)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-7B0A7691-7F1F-4D19-9BB7-44976885D157)
- [DBMS_CLOUD_OCI_AI_LANGUAGE_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_language_t.html#ADSDK-GUID-579EF50F-BD4B-45F1-8C63-E98D952E50B5)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
