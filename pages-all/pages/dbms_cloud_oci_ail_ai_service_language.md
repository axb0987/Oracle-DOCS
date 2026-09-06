# AI Language Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html
- Fetched: 2026-09-05 19:03 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#dcoc-content-body)

## AI Language Functions

Package: DBMS_CLOUD_OCI_AIL_AI_SERVICE_LANGUAGE

### BATCH_DETECT_DOMINANT_LANGUAGE Function

The API returns the detected language and a related confidence score (between 0 and 1). It supports passing a batch of records.[List of supported languages.](https://docs.oracle.com/iaas/language/using/pretrain-models.htm#lang-detect)Limitations: - A batch may have up to 100 records. - A record may be up to 5000 characters long. - The total of characters to process in a request can be up to 20,000 characters.

Syntax
```

```

Parameters

Parameter Description

`batch_detect_dominant_language_details`

(required) The details to make a language detection detect call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### BATCH_DETECT_LANGUAGE_ENTITIES Function

The API extracts entities in text records. For each entity, its type/subtype and confidence score (between 0 and 1) is returned. It supports passing a batch of records.[List of supported entities.](https://docs.oracle.com/iaas/language/using/pretrain-models.htm#ner__sup-ner-entity)Limitations: - A batch may have up to 100 records. - A record may be up to 5000 characters long. - The total of characters to process in a request can be up to 20,000 characters.

Syntax
```

```

Parameters

Parameter Description

`batch_detect_language_entities_details`

(required) The details to make a Entity detect call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### BATCH_DETECT_LANGUAGE_KEY_PHRASES Function

The API extracts key-phrases in text records. For each key-phrase, a score (between 0 and 1) is returned that highlights the importance of the key-phrase in the context of the text. It supports passing a batch of records. Limitations: - A batch may have up to 100 records. - A record may be up to 5000 characters long. - The total of characters to process in a request can be up to 20,000 characters.

Syntax
```

```

Parameters

Parameter Description

`batch_detect_language_key_phrases_details`

(required) The details to make keyPhrase detect call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### BATCH_DETECT_LANGUAGE_PII_ENTITIES Function

The API extracts pii entities in text records. For each entity, its type and confidence score (between 0 and 1) is returned. It supports passing a batch of records. Limitations: - A batch may have up to 100 records. - A record may be up to 5000 characters long. - The total of characters to process in a request can be up to 20,000 characters.

Syntax
```

```

Parameters

Parameter Description

`batch_detect_language_pii_entities_details`

(required) The details to make a PII entity detect call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### BATCH_DETECT_LANGUAGE_SENTIMENTS Function

The API extracts aspect-based and sentence level sentiment in text records. For aspect-based sentiment analysis, a set of aspects and their respective sentiment is returned for each record. Similarly, for sentence-level sentiment analysis, the sentiment is returned at the sentence level. For sentiment analysis, confidence scores are provided for each of the classes (positive, negative, neutral and mixed). Learn more about sentiment analysis[here](https://docs.oracle.com/iaas/language/using/pretrain-models.htm#sentiment). Limitations: - A batch may have up to 100 records. - A record may be up to 5000 characters long. - The total of characters to process in a request can be up to 20,000 characters.

Syntax
```

```

Parameters

Parameter Description

`batch_detect_language_sentiments_details`

(required) The details to make sentiment detect call.

`opc_request_id`

(optional) The client request ID for tracing.

`l_level`

(optional) Set this parameter for sentence and aspect level sentiment analysis. Allowed values are: - ASPECT - SENTENCE

Allowed values are: 'ASPECT', 'SENTENCE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### BATCH_DETECT_LANGUAGE_TEXT_CLASSIFICATION Function

The API automatically classifies text into a set of pre-determined classes and sub-classes. A single class/subclass is returned for each record classified. It supports passing a batch of records. Learn more about text classification[here](https://docs.oracle.com/iaas/language/using/pretrain-models.htm#text-class). Limitations: - A batch may have up to 100 records. - A record may be up to 5000 characters long. - The total of characters to process in a request can be up to 20,000 characters.

Syntax
```

```

Parameters

Parameter Description

`batch_detect_language_text_classification_details`

(required) The details to make text classification detect call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### BATCH_LANGUAGE_TRANSLATION Function

Translate text to other language over pre-deployed model. Use state of the art neural machine translation to translate text between more than 15 languages. Limitations: - A batch may have up to 100 records. - A record may be up to 5000 characters long. - The total of characters to process in a request can be up to 20,000 characters.

Syntax
```

```

Parameters

Parameter Description

`batch_language_translation_details`

(required) The details to make language translation call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_ENDPOINT_COMPARTMENT Function

Moves a Endpoint into a different compartment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`endpoint_id`

(required) The OCID of the endpoint.

`change_endpoint_compartment_details`

(required)

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_MODEL_COMPARTMENT Function

Moves a Model into a different compartment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`model_id`

(required) unique model OCID.

`change_model_compartment_details`

(required)

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_PROJECT_COMPARTMENT Function

Moves a Project into a different compartment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`project_id`

(required) The OCID of the project.

`change_project_compartment_details`

(required)

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ENDPOINT Function

Creates a new endpoint and deploy the trained model

Syntax
```

```

Parameters

Parameter Description

`create_endpoint_details`

(required) Details for the new endpoint.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MODEL Function

Creates a new model for training and train the model with date provided.

Syntax
```

```

Parameters

Parameter Description

`create_model_details`

(required) Details for the new model.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PROJECT Function

Creates a new Project.

Syntax
```

```

Parameters

Parameter Description

`create_project_details`

(required) Details for the new Project.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ENDPOINT Function

Deletes a provisioned endpoint resource by identifier. This operation fails with a 409 error unless all associated resources are in a DELETED state. You must delete all associated resources before deleting a model.

Syntax
```

```

Parameters

Parameter Description

`endpoint_id`

(required) The OCID of the endpoint.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MODEL Function

Deletes a provisioned model resource by identifier. This operation fails with a 409 error unless all associated resources are in a DELETED state. You must delete all associated resources before deleting a model.

Syntax
```

```

Parameters

Parameter Description

`model_id`

(required) unique model OCID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PROJECT Function

Deletes a Project resource by identifier. This operation fails with a 409 error unless all associated resources (models deployments or data assets) are in a DELETED state. You must delete all associated resources before deleting a project.

Syntax
```

```

Parameters

Parameter Description

`project_id`

(required) The OCID of the project.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DETECT_DOMINANT_LANGUAGE Function

This API will be retired on Monday, 10 Oct 2023 00:00:00 GMT The API returns the detected language and a related confidence score (between 0 and 1).[List of supported languages.](https://docs.oracle.com/iaas/language/using/pretrain-models.htm#lang-detect)Limitations: - A record may be up to 1000 characters long.

Syntax
```

```

Parameters

Parameter Description

`detect_dominant_language_details`

(required) The details to make a language detection detect call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DETECT_LANGUAGE_ENTITIES Function

This API will be retired on Monday, 10 Oct 2023 00:00:00 GMT The API extracts entities in text records. For each entity, its type and confidence score (between 0 and 1) is returned. Limitations: - A text may be up to 1000 characters long.

Syntax
```

```

Parameters

Parameter Description

`detect_language_entities_details`

(required) The details to make a Entity detect call.

`opc_request_id`

(optional) The client request ID for tracing.

`model_version`

(optional) Named Entity Recognition model versions. By default user will get output from V2.1 implementation.

Allowed values are: 'V2_1', 'V1_1'

`is_pii`

(optional) If this parameter is set to true, you only get PII (Personally identifiable information) entities like PhoneNumber, Email, Person, and so on. Default value is false.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DETECT_LANGUAGE_KEY_PHRASES Function

This API will be retired on Monday, 10 Oct 2023 00:00:00 GMT The API extracts key-phrases in text records. For each key-phrase, a score (between 0 and 1) is returned that highlights the importance of the key-phrase in the context of the text. Limitations: - A record may be up to 1000 characters long.

Syntax
```

```

Parameters

Parameter Description

`detect_language_key_phrases_details`

(required) The details to make keyPhrase detect call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DETECT_LANGUAGE_SENTIMENTS Function

This API will be retired on Monday, 10 Oct 2023 00:00:00 GMT The API extracts aspect-based in text records. For aspect-based sentiment analysis, a set of aspects and their respective sentiment is returned. For sentiment analysis, confidence scores are provided for each of the classes (positive, negative, neutral). Learn more about sentiment analysis[here](https://docs.oracle.com/iaas/language/using/pretrain-models.htm#sentiment). Limitations: - A record may be up to 1000 characters long.

Syntax
```

```

Parameters

Parameter Description

`detect_language_sentiments_details`

(required) The details to make sentiment detect call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DETECT_LANGUAGE_TEXT_CLASSIFICATION Function

This API will be retired on Monday, 10 Oct 2023 00:00:00 GMT The API automatically classifies text into a set of pre-determined classes and sub-classes. A single class/subclass is returned for each record classified. Learn more about text classification[here](https://docs.oracle.com/iaas/language/using/pretrain-models.htm#text-class). Limitations: - A record may be up to 1000 characters long.

Syntax
```

```

Parameters

Parameter Description

`detect_language_text_classification_details`

(required) The details to make text classification detect call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ENDPOINT Function

Gets an endpoint by identifier

Syntax
```

```

Parameters

Parameter Description

`endpoint_id`

(required) The OCID of the endpoint.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MODEL Function

Gets a model by identifier

Syntax
```

```

Parameters

Parameter Description

`model_id`

(required) unique model OCID.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MODEL_TYPE Function

Gets model capabilities

Syntax
```

```

Parameters

Parameter Description

`model_type`

(required) Results like version and model supported info by specifying model type

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PROJECT Function

Gets a Project by identifier

Syntax
```

```

Parameters

Parameter Description

`project_id`

(required) The OCID of the project.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ENDPOINTS Function

Returns a list of Endpoints.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`endpoint_id`

(optional) The OCID of the endpoint.

`project_id`

(optional) The ID of the project for which to list the objects.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`model_id`

(optional) The ID of the trained model for which to list the endpoints.

`lifecycle_state`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the specified lifecycle state. Must be a valid state for the resource type.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeCreated`, the results are shown in descending order. When you sort by `displayName`, the results are shown in ascending order. Sort order for the `displayName` field is case sensitive.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EVALUATION_RESULTS Function

Get a (paginated) list of evaluation results for a given model.

Syntax
```

```

Parameters

Parameter Description

`model_id`

(required) unique model OCID.

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MODELS Function

Returns a list of models.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`model_id`

(optional) unique model OCID.

`project_id`

(optional) The ID of the project for which to list the objects.

`lifecycle_state`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the specified lifecycle state. Must be a valid state for the resource type.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeCreated`, the results are shown in descending order. When you sort by `displayName`, the results are shown in ascending order. Sort order for the `displayName` field is case sensitive.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PROJECTS Function

Returns a list of Projects.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`lifecycle_state`

(optional) &lt;b&gt;Filter&lt;/b&gt; results by the specified lifecycle state. Must be a valid state for the resource type.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`project_id`

(optional) The ID of the project for which to list the objects.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeCreated`, the results are shown in descending order. When you sort by `displayName`, the results are shown in ascending order. Sort order for the `displayName` field is case sensitive.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The ID of the compartment in which to list resources.

`work_request_id`

(optional) The ID of the asynchronous work request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`resource_id`

(optional) The ID of the resource for which list workrequests.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ENDPOINT Function

Update the Endpoint identified by the id

Syntax
```

```

Parameters

Parameter Description

`endpoint_id`

(required) The OCID of the endpoint.

`update_endpoint_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MODEL Function

Updates the model

Syntax
```

```

Parameters

Parameter Description

`model_id`

(required) unique model OCID.

`update_model_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PROJECT Function

Updates the Project

Syntax
```

```

Parameters

Parameter Description

`project_id`

(required) The OCID of the project.

`update_project_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://language.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [AI Language Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-640F37FB-3ED5-4F71-967B-996BACE7EC21)
- [BATCH_DETECT_DOMINANT_LANGUAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-76CCCFC9-DE65-4137-BF16-2DF9213B0CD7)
- [BATCH_DETECT_LANGUAGE_ENTITIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-44B8B7F2-D681-424B-8755-406908FAF49E)
- [BATCH_DETECT_LANGUAGE_KEY_PHRASES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-0DC507BE-2CB9-4C15-8334-A52A46B9098E)
- [BATCH_DETECT_LANGUAGE_PII_ENTITIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-53B5FFA5-3D51-4AC3-98FD-95770EC2E61A)
- [BATCH_DETECT_LANGUAGE_SENTIMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-EB0FB0BD-1CB4-4597-9330-CDA6C362CE60)
- [BATCH_DETECT_LANGUAGE_TEXT_CLASSIFICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-9897A25A-CB81-469B-8076-5D0082CA26A9)
- [BATCH_LANGUAGE_TRANSLATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-F51E72BF-2832-4FFB-99B1-BC5D9007F06F)
- [CHANGE_ENDPOINT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-5123697F-2688-463E-8C84-8496F336673B)
- [CHANGE_MODEL_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-E0ED5381-9BF1-41EC-8DAB-EDC86800F585)
- [CHANGE_PROJECT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-F4E24769-19D2-4BEC-985E-E03424F96E4A)
- [CREATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-9B50EDD9-118B-470B-BD9D-589C3E2F597A)
- [CREATE_MODEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-F1C2B47B-F7CD-40D6-B832-7507E9300800)
- [CREATE_PROJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-7D63C6D7-462F-42BF-A644-3206B7E1FEF0)
- [DELETE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-3FD8A9D5-9E50-4B74-A26A-FCEDBE77998D)
- [DELETE_MODEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-669F94C6-4235-451C-A6C4-393C47DF4DC1)
- [DELETE_PROJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-8907E7FB-F851-4387-9C9C-E35CED7A52E9)
- [DETECT_DOMINANT_LANGUAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-4DD6DC05-AD53-45C3-A1B2-340C1294108C)
- [DETECT_LANGUAGE_ENTITIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-5A277419-4D79-4902-8126-F42F99BDB0C1)
- [DETECT_LANGUAGE_KEY_PHRASES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-8F148E34-27A4-4432-B675-00FD79AADB71)
- [DETECT_LANGUAGE_SENTIMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-C2896FC8-4904-490E-88DD-187F0BACDD86)
- [DETECT_LANGUAGE_TEXT_CLASSIFICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-03502371-6596-4735-9DD1-DFAC1CCD7515)
- [GET_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-A9B973F3-3AC6-44F5-A571-9DE35E3AD986)
- [GET_MODEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-2025A5FE-D6BE-4B79-8E23-B001CE1163C9)
- [GET_MODEL_TYPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-8F99A6EA-7386-4980-9E9F-5BCE39519E60)
- [GET_PROJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-66575964-E8DC-41CF-BC55-23B70E6582DC)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-A61C5B60-F599-45D6-B234-2026EAFEB8D7)
- [LIST_ENDPOINTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-173890C9-ACE4-4A6F-93D5-F355236F0382)
- [LIST_EVALUATION_RESULTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-8852AEA8-A73C-4496-A947-6D93270616B3)
- [LIST_MODELS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-9C0E4057-09A1-4C14-A983-FBE803CDAD61)
- [LIST_PROJECTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-7E358C8D-6245-4E23-9303-675AB3D758F4)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-4191C047-3EAB-490F-99A8-4A42537F4963)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-3502EFD7-0FEC-48A7-A76A-0FE2353EDEC1)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-F9C95B1E-FFC2-4FDB-BB4B-22FC8880DD7F)
- [UPDATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-1223D5B6-5516-4A1C-B8ED-E4B9294C52E7)
- [UPDATE_MODEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-F259987A-97D6-414A-B114-5C7B6C17118B)
- [UPDATE_PROJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ail_ai_service_language.html#ADSDK-GUID-6101661B-9872-4158-928A-E20B50517021)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
