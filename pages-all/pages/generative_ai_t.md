# Generative AI Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html
- Fetched: 2026-09-05 19:16 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#dcoc-content-body)

## Generative AI Common Types

### DBMS_CLOUD_OCI_GENERATIVE_AI_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_GENERATIVE_AI_CHANGE_DEDICATED_AI_CLUSTER_COMPARTMENT_DETAILS_T Type

The details to move a dedicated AI cluster to another compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment to move the dedicated AI cluster to.

### DBMS_CLOUD_OCI_GENERATIVE_AI_CHANGE_ENDPOINT_COMPARTMENT_DETAILS_T Type

The details to move an endpoint to another compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment to move the endpoint to.

### DBMS_CLOUD_OCI_GENERATIVE_AI_CHANGE_MODEL_COMPARTMENT_DETAILS_T Type

The details to move a custom model to another compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The compartment OCID to create the model in.

### DBMS_CLOUD_OCI_GENERATIVE_AI_CONTENT_MODERATION_CONFIG_T Type

The configuration details, whether to add the content moderation feature to the model. Content moderation removes toxic and biased content from responses. It's recommended to use content moderation.

Syntax
```

```

Fields

Field Description

`is_enabled`

(required) Whether to enable the content moderation feature.

### DBMS_CLOUD_OCI_GENERATIVE_AI_CREATE_DEDICATED_AI_CLUSTER_DETAILS_T Type

The data to create a dedicated AI cluster.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable.

`description`

(optional) An optional description of the dedicated AI cluster.

`l_type`

(required) The dedicated AI cluster type indicating whether this is a fine-tuning/training processor or hosting/inference processor. Allowed values are: - HOSTING - FINE_TUNING

`compartment_id`

(required) The compartment OCID to create the dedicated AI cluster in.

`unit_count`

(required) The number of dedicated units in this AI cluster.

`unit_shape`

(required) The shape of dedicated unit in this AI cluster. The underlying hardware configuration is hidden from customers. Allowed values are: - LARGE_COHERE - SMALL_COHERE - EMBED_COHERE - LLAMA2_70

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_GENERATIVE_AI_CREATE_ENDPOINT_DETAILS_T Type

The data to create an endpoint.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable.

`description`

(optional) An optional description of the endpoint.

`compartment_id`

(required) The compartment OCID to create the endpoint in.

`model_id`

(required) The ID of the model that's used to create this endpoint.

`dedicated_ai_cluster_id`

(required) The OCID of the dedicated AI cluster on which a model will be deployed to.

`content_moderation_config`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_GENERATIVE_AI_DATASET_T Type

The dataset used to fine-tune the model. Only one dataset is allowed per custom model, which is split 90-10 for training and validating. You must provide the dataset in a JSON Lines (JSONL) file. Each line in the JSONL file must have the format: `{\"prompt\": \"&lt;first prompt&gt;\", \"completion\": \"&lt;expected completion given first prompt&gt;\"}`

Syntax
```

```

Fields

Field Description

`dataset_type`

(required) The type of the data asset.

Allowed values are: 'OBJECT_STORAGE'

### DBMS_CLOUD_OCI_GENERATIVE_AI_TRAINING_CONFIG_T Type

The fine-tuning method and hyperparameters used for fine-tuning a custom model.

Syntax
```

```

Fields

Field Description

`training_config_type`

(required) The fine-tuning method for training a custom model.

Allowed values are: 'TFEW_TRAINING_CONFIG', 'VANILLA_TRAINING_CONFIG'

`total_training_epochs`

(optional) The maximum number of training epochs to run for.

`learning_rate`

(optional) The initial learning rate to be used during training

`training_batch_size`

(optional) The batch size used during training.

`early_stopping_patience`

(optional) Stop training if the loss metric does not improve beyond 'early_stopping_threshold' for this many times of evaluation.

`early_stopping_threshold`

(optional) How much the loss must improve to prevent early stopping.

`log_model_metrics_interval_in_steps`

(optional) Determines how frequently to log model metrics. Every step is logged for the first 20 steps and then follows this parameter for log frequency. Set to 0 to disable logging the model metrics.

### DBMS_CLOUD_OCI_GENERATIVE_AI_FINE_TUNE_DETAILS_T Type

Details about fine-tuning a custom model.

Syntax
```

```

Fields

Field Description

`training_dataset`

(required)

`dedicated_ai_cluster_id`

(required) The OCID of the dedicated AI cluster this fine-tuning runs on.

`training_config`

(optional)

### DBMS_CLOUD_OCI_GENERATIVE_AI_CREATE_MODEL_DETAILS_T Type

The data to create a custom model.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name.

`compartment_id`

(required) The compartment OCID for fine-tuned models. For pretrained models, this value is null.

`vendor`

(optional) The provider of the model.

`version`

(optional) The version of the model.

`description`

(optional) An optional description of the model.

`base_model_id`

(required) The OCID of the base model that's used for fine-tuning.

`fine_tune_details`

(required)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_GENERATIVE_AI_DEDICATED_AI_CLUSTER_CAPACITY_T Type

The total capacity for a dedicated AI cluster.

Syntax
```

```

Fields

Field Description

`capacity_type`

(required) The type of the dedicated AI cluster capacity.

Allowed values are: 'HOSTING_CAPACITY'

### DBMS_CLOUD_OCI_GENERATIVE_AI_DEDICATED_AI_CLUSTER_T Type

Dedicated AI clusters are compute resources that you can use for fine-tuning custom models or for hosting endpoints for custom models. The clusters are dedicated to your models and not shared with users in other tenancies. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator who gives OCI resource access to users. See[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Getting Access to Generative AI Resouces](https://docs.oracle.com/iaas/Content/generative-ai/iam-policies.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dedicated AI cluster.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable.

`description`

(optional) An optional description of the dedicated AI cluster.

`l_type`

(required) The dedicated AI cluster type indicating whether this is a fine-tuning/training processor or hosting/inference processor.

Allowed values are: 'HOSTING', 'FINE_TUNING'

`compartment_id`

(required) The compartment OCID to create the dedicated AI cluster in.

`time_created`

(required) The date and time the dedicated AI cluster was created, in the format defined by RFC 3339

`time_updated`

(optional) The date and time the dedicated AI cluster was updated, in the format defined by RFC 3339

`lifecycle_state`

(required) The current state of the dedicated AI cluster.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) A message describing the current state with detail that can provide actionable information.

`unit_count`

(required) The number of dedicated units in this AI cluster.

`unit_shape`

(required) The shape of dedicated unit in this AI cluster. The underlying hardware configuration is hidden from customers.

Allowed values are: 'LARGE_COHERE', 'SMALL_COHERE', 'EMBED_COHERE', 'LLAMA2_70'

`l_capacity`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_GENERATIVE_AI_DEDICATED_AI_CLUSTER_SUMMARY_T Type

Summary information about a dedicated AI cluster.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dedicated AI cluster.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable.

`description`

(optional) An optional description of the dedicated AI cluster.

`l_type`

(required) The dedicated AI cluster type indicating whether this is a fine-tuning/training processor or hosting/inference processor. Allowed values are: - HOSTING - FINE_TUNING

`compartment_id`

(required) The compartment OCID to create the dedicated AI cluster in.

`time_created`

(required) The date and time the dedicated AI cluster was created, in the format defined by RFC 3339.

`time_updated`

(optional) The date and time the dedicated AI cluster was updated, in the format defined by RFC 3339.

`lifecycle_state`

(required) The current state of the dedicated AI cluster. Allowed values are: - CREATING - ACTIVE - UPDATING - DELETING - DELETED - FAILED - NEEDS_ATTENTION

`lifecycle_details`

(optional) A message describing the current state of the dedicated AI cluster in more detail that can provide actionable information.

`unit_count`

(required) The number of dedicated units in this AI cluster.

`unit_shape`

(required) The shape of dedicated unit in this AI cluster. The underlying hardware configuration is hidden from customers.

`l_capacity`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_GENERATIVE_AI_DEDICATED_AI_CLUSTER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_generative_ai_dedicated_ai_cluster_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GENERATIVE_AI_DEDICATED_AI_CLUSTER_COLLECTION_T Type

Results of a dedicate AI cluster search. Contains DedicatedAiClusterSummary items and other information such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of dedicated AI clusters.

### DBMS_CLOUD_OCI_GENERATIVE_AI_DEDICATED_AI_CLUSTER_HOSTING_CAPACITY_T Type

The capacity of a hosting type dedicated AI cluster.

Syntax
```

```

`dbms_cloud_oci_generative_ai_dedicated_ai_cluster_hosting_capacity_t`is a subtype of the`dbms_cloud_oci_generative_ai_dedicated_ai_cluster_capacity_t`type.

Fields

Field Description

`total_endpoint_capacity`

(optional) The total number of endpoints that can be hosted on this dedicated AI cluster.

`used_endpoint_capacity`

(optional) The number of endpoints hosted on this dedicated AI cluster.

### DBMS_CLOUD_OCI_GENERATIVE_AI_ENDPOINT_T Type

To host a custom model for inference, create an endpoint for that model on a dedicated AI cluster of type HOSTING. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator who gives OCI resource access to users. See[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Getting Access to Generative AI Resouces](https://docs.oracle.com/iaas/Content/generative-ai/iam-policies.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) An OCID that uniquely identifies this endpoint resource.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable.

`description`

(optional) An optional description of the endpoint.

`model_id`

(required) The OCID of the model that's used to create this endpoint.

`compartment_id`

(required) The compartment OCID to create the endpoint in.

`dedicated_ai_cluster_id`

(required) The OCID of the dedicated AI cluster on which the model will be deployed to.

`time_created`

(required) The date and time that the endpoint was created in the format of an RFC3339 datetime string.

`time_updated`

(optional) The date and time that the endpoint was updated in the format of an RFC3339 datetime string.

`lifecycle_state`

(required) The current state of the endpoint.

Allowed values are: 'ACTIVE', 'CREATING', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state of the endpoint in more detail that can provide actionable information.

`content_moderation_config`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_GENERATIVE_AI_ENDPOINT_SUMMARY_T Type

Summary information for an endpoint resource.

Syntax
```

```

Fields

Field Description

`id`

(required) An OCID that uniquely identifies this endpoint resource.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable.

`description`

(optional) An optional description of the endpoint.

`model_id`

(required) The OCID of the model that's used to create this endpoint.

`compartment_id`

(required) The compartment OCID to create the endpoint in.

`dedicated_ai_cluster_id`

(required) The OCID of the dedicated AI cluster on which a model will be deployed to.

`time_created`

(required) The date and time that the endpoint was created in the format of an RFC3339 datetime string.

`time_updated`

(optional) The date and time the endpoint was updated in the format of n RFC3339 datetime string.

`lifecycle_state`

(required) The current state of the endpoint. Allowed values are: - ACTIVE - CREATING - UPDATING - DELETING - DELETED - FAILED

`lifecycle_details`

(optional) A message describing the current state with detail that can provide actionable information.

`content_moderation_config`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_GENERATIVE_AI_ENDPOINT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_generative_ai_endpoint_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GENERATIVE_AI_ENDPOINT_COLLECTION_T Type

Results of an endpoint search. Contains EndpointSummary items and other information such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of endpoints.

### DBMS_CLOUD_OCI_GENERATIVE_AI_ERROR_T Type

Error information.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error message.

### DBMS_CLOUD_OCI_GENERATIVE_AI_MODEL_METRICS_T Type

Model metrics during the creation of a new model.

Syntax
```

```

Fields

Field Description

`model_metrics_type`

(required) The type of the model metrics. Each type of model can expect a different set of model metrics.

Allowed values are: 'TEXT_GENERATION_MODEL_METRICS'

### DBMS_CLOUD_OCI_GENERATIVE_AI_MODEL_T Type

You can create a custom model by using your dataset to fine-tune an out-of-the-box text generation base model. Have your dataset ready before you create a custom model. See[Training Data Requirements](https://docs.oracle.com/iaas/Content/generative-ai/training-data-requirements.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator who gives OCI resource access to users. See[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Getting Access to Generative AI Resouces](https://docs.oracle.com/iaas/Content/generative-ai/iam-policies.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) An ID that uniquely identifies a pretrained or fine-tuned model.

`description`

(optional) An optional description of the model.

`compartment_id`

(required) The compartment OCID for fine-tuned models. For pretrained models, this value is null.

`capabilities`

(required) Describes what this model can be used for.

Allowed values are: 'TEXT_GENERATION', 'TEXT_SUMMARIZATION', 'TEXT_EMBEDDINGS', 'FINE_TUNE'

`lifecycle_state`

(required) The lifecycle state of the model.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state of the model in more detail that can provide actionable information.

`vendor`

(optional) The provider of the base model.

`version`

(optional) The version of the model.

`display_name`

(optional) A user-friendly name.

`time_created`

(required) The date and time that the model was created in the format of an RFC3339 datetime string.

`time_updated`

(optional) The date and time that the model was updated in the format of an RFC3339 datetime string.

`base_model_id`

(optional) The OCID of the base model that's used for fine-tuning. For pretrained models, the value is null.

`l_type`

(required) The model type indicating whether this is a pretrained/base model or a custom/fine-tuned model.

Allowed values are: 'BASE', 'CUSTOM'

`fine_tune_details`

(optional)

`model_metrics`

(optional)

`is_long_term_supported`

(optional) Whether a model is supported long-term. Only applicable to base models.

`time_deprecated`

(optional) Corresponds to the time when the custom model and its associated foundation model will be deprecated.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_GENERATIVE_AI_MODEL_SUMMARY_T Type

Summary of the model.

Syntax
```

```

Fields

Field Description

`id`

(required) An ID that uniquely identifies a pretrained or a fine-tuned model.

`compartment_id`

(required) The compartment OCID for fine-tuned models. For pretrained models, this value is null.

`capabilities`

(required) Describes what this model can be used for.

Allowed values are: 'TEXT_GENERATION', 'TEXT_SUMMARIZATION', 'TEXT_EMBEDDINGS', 'FINE_TUNE'

`lifecycle_state`

(required) The lifecycle state of the model. Allowed values are: - ACTIVE - CREATING - DELETING - DELETED - FAILED

`lifecycle_details`

(optional) A message describing the current state of the model with detail that can provide actionable information.

`display_name`

(optional) A user-friendly name.

`vendor`

(optional) The provider of the model.

`version`

(optional) The version of the model.

`time_created`

(required) The date and time that the model was created in the format of an RFC3339 datetime string.

`base_model_id`

(optional) The OCID of the base model that's used for fine-tuning. For pretrained models, the value is null.

`l_type`

(required) The model type indicating whether this is a pretrained/base model or a custom/fine-tuned model. Allowed values are: - BASE - CUSTOM

`fine_tune_details`

(optional)

`model_metrics`

(optional)

`is_long_term_supported`

(optional) Whether a model is supported long-term. Applies only to base models.

`time_deprecated`

(optional) Corresponds to the time when the custom model and its associated foundation model will be deprecated.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_GENERATIVE_AI_MODEL_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_generative_ai_model_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GENERATIVE_AI_MODEL_COLLECTION_T Type

Results of a model search. Contains ModelSummary items and other information such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) The results of a model search.

### DBMS_CLOUD_OCI_GENERATIVE_AI_OBJECT_STORAGE_DATASET_T Type

The dataset is stored in an OCI Object Storage bucket.

Syntax
```

```

`dbms_cloud_oci_generative_ai_object_storage_dataset_t`is a subtype of the`dbms_cloud_oci_generative_ai_dataset_t`type.

Fields

Field Description

`namespace_name`

(required) The Object Storage namespace.

`bucket_name`

(required) The Object Storage bucket name.

`object_name`

(required) The Object Storage object name.

### DBMS_CLOUD_OCI_GENERATIVE_AI_T_FEW_TRAINING_CONFIG_T Type

The TFEW training method hyperparameters.

Syntax
```

```

`dbms_cloud_oci_generative_ai_t_few_training_config_t`is a subtype of the`dbms_cloud_oci_generative_ai_training_config_t`type.

### DBMS_CLOUD_OCI_GENERATIVE_AI_TEXT_GENERATION_MODEL_METRICS_T Type

The text generation model metrics of the fine-tuning process.

Syntax
```

```

`dbms_cloud_oci_generative_ai_text_generation_model_metrics_t`is a subtype of the`dbms_cloud_oci_generative_ai_model_metrics_t`type.

Fields

Field Description

`final_accuracy`

(optional) Fine-tuned model accuracy.

`final_loss`

(optional) Fine-tuned model loss.

### DBMS_CLOUD_OCI_GENERATIVE_AI_UPDATE_DEDICATED_AI_CLUSTER_DETAILS_T Type

The data to update a dedicated AI cluster.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable.

`description`

(optional) An optional description of the dedicated AI cluster.

`unit_count`

(optional) The number of dedicated units in this AI cluster.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_GENERATIVE_AI_UPDATE_ENDPOINT_DETAILS_T Type

The data to update an endpoint.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable.

`description`

(optional) An optional description of the endpoint.

`content_moderation_config`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_GENERATIVE_AI_UPDATE_MODEL_DETAILS_T Type

The data to update a custom model.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name.

`description`

(optional) An optional description of the model.

`vendor`

(optional) The provider of the base model.

`version`

(optional) The version of the model.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_GENERATIVE_AI_VANILLA_TRAINING_CONFIG_T Type

The Vanilla training method hyperparameters.

Syntax
```

```

`dbms_cloud_oci_generative_ai_vanilla_training_config_t`is a subtype of the`dbms_cloud_oci_generative_ai_training_config_t`type.

Fields

Field Description

`num_of_last_layers`

(optional) The number of last layers to be fine-tuned.

### DBMS_CLOUD_OCI_GENERATIVE_AI_WORK_REQUEST_RESOURCE_T Type

The resource created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type that the work request affects.

`action_type`

(required) The way in which this resource is affected by the operation tracked in the work request. A resource being created, updated, or deleted remains in the IN_PROGRESS state until work is complete for that resource, at which point it transitions to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED', 'FAILED'

`identifier`

(required) An[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)or other unique identifier for the resource.

`entity_uri`

(optional) The URI path that you can use for a GET request to access the resource metadata.

`metadata`

(optional) Additional information that helps to explain the resource.

### DBMS_CLOUD_OCI_GENERATIVE_AI_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_generative_ai_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GENERATIVE_AI_WORK_REQUEST_T Type

An asynchronous work request. When you start a long-running operation, the service creates a work request. Work requests help you monitor long-running operations. A work request is an activity log that lets you track each step in the operation's progress. Each work request has an OCID that lets you interact with it programmatically and use it for automation.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The asynchronous operation tracked by this work request.

Allowed values are: 'CREATE_MODEL', 'DELETE_MODEL', 'MOVE_MODEL', 'CREATE_DEDICATED_AI_CLUSTER', 'DELETE_DEDICATED_AI_CLUSTER', 'UPDATE_DEDICATED_AI_CLUSTER', 'MOVE_DEDICATED_AI_CLUSTER', 'CREATE_ENDPOINT', 'DELETE_ENDPOINT', 'UPDATE_ENDPOINT', 'MOVE_ENDPOINT'

`status`

(required) The status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the work request.

`resources`

(required) The resources that are affected by the work request.

`percent_complete`

(required) Shows the progress of the operation tracked by the work request, as a percentage of the total work that must be performed.

`time_accepted`

(required) The date and time the work request was created, in the format defined by[RFC 3339](https://tools.ietf.org/html/rfc3339).

`time_started`

(optional) The date and time the work request was started, in the format defined by[RFC 3339](https://tools.ietf.org/html/rfc3339).

`time_finished`

(optional) The date and time the work request was finished, in the format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_GENERATIVE_AI_WORK_REQUEST_ERROR_T Type

An error encountered while performing an operation that is tracked by this work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occurred. For a list of error codes, see[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error message.

`l_timestamp`

(required) The date and time that the error occurred, in the format defined by[RFC 3339](https://tools.ietf.org/html/rfc3339).

### DBMS_CLOUD_OCI_GENERATIVE_AI_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_generative_ai_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GENERATIVE_AI_WORK_REQUEST_ERROR_COLLECTION_T Type

A list of work request errors. Can contain errors and other information such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of work request errors.

### DBMS_CLOUD_OCI_GENERATIVE_AI_WORK_REQUEST_LOG_ENTRY_T Type

The log message from performing an operation that is tracked by this work request.

Syntax
```

```

Fields

Field Description

`message`

(required) A human-readable log message.

`l_timestamp`

(required) The date and time the log message was written, in the format defined by[RFC 3339](https://tools.ietf.org/html/rfc3339).

### DBMS_CLOUD_OCI_GENERATIVE_AI_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_generative_ai_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GENERATIVE_AI_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

A list of work request logs. Can contain logs and other information such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of work request log entries.

### DBMS_CLOUD_OCI_GENERATIVE_AI_WORK_REQUEST_SUMMARY_T Type

Summary information about an asynchronous work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The asynchronous operation tracked by this work request.

Allowed values are: 'CREATE_MODEL', 'DELETE_MODEL', 'MOVE_MODEL', 'CREATE_DEDICATED_AI_CLUSTER', 'DELETE_DEDICATED_AI_CLUSTER', 'UPDATE_DEDICATED_AI_CLUSTER', 'MOVE_DEDICATED_AI_CLUSTER', 'CREATE_ENDPOINT', 'DELETE_ENDPOINT', 'UPDATE_ENDPOINT', 'MOVE_ENDPOINT'

`status`

(required) The status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the work request.

`resources`

(required) The resources that are affected by this work request.

`percent_complete`

(required) Shows the progress of the operation tracked by the work request, as a percentage of the total work that must be performed.

`time_accepted`

(required) The date and time the work request was created, in the format defined by[RFC 3339](https://tools.ietf.org/html/rfc3339).

`time_started`

(optional) The date and time the work request was started, in the format defined by[RFC 3339](https://tools.ietf.org/html/rfc3339).

`time_finished`

(optional) The date and time the work request was finished, in the format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_GENERATIVE_AI_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_generative_ai_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GENERATIVE_AI_WORK_REQUEST_SUMMARY_COLLECTION_T Type

A list of work requests. Can contain work requests and other information such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of work requests.

- [Generative AI Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-7150AC27-3815-46B5-B315-DEA0C000CE8E)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-EDF3D17D-AF24-4058-A3B3-9E10A216BE63)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_CHANGE_DEDICATED_AI_CLUSTER_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-61B52379-800B-47B8-9F03-71C1B294C308)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_CHANGE_ENDPOINT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-18B72E85-54F6-4F02-9AF4-0C54D31EC8E4)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_CHANGE_MODEL_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-EF221956-3086-46EB-B62D-BD0FE91D9C70)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_CONTENT_MODERATION_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-72283300-6A76-44F4-B11D-4C3CE29E7FEB)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_CREATE_DEDICATED_AI_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-CEE44ED9-8C9B-4F56-ACD7-6451B1A5AB8B)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_CREATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-B08BA491-09E7-4731-BD3D-A81802AF1FF7)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_DATASET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-A5C35E59-E70A-4F57-93E9-8CCFB80ACA30)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_TRAINING_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-16A9C75A-1661-4C89-889A-53767E6F33D4)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_FINE_TUNE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-C15B06C9-E40A-4555-9642-56931A480C2D)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_CREATE_MODEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-22DAD5AD-7240-421B-BC0D-9583D607E438)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_DEDICATED_AI_CLUSTER_CAPACITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-0DAE8AFD-145A-4307-A4B9-B83979480D7B)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_DEDICATED_AI_CLUSTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-379FEF2C-5BE3-4B7B-8132-E1F87742B9A7)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_DEDICATED_AI_CLUSTER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-BF42FC55-F154-4D91-92A8-EC70C3D6BCC7)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_DEDICATED_AI_CLUSTER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-975D1B9C-4F72-4975-A29F-9FC3D252C44C)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_DEDICATED_AI_CLUSTER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-A46290B2-8B5E-40C5-AA22-A2687F7A22EB)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_DEDICATED_AI_CLUSTER_HOSTING_CAPACITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-A926B654-2443-421A-A7A7-B0E52D80EB9B)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-A009A136-CE77-4520-802D-458C83D4B1A1)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_ENDPOINT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-3835118A-E96B-4D6A-A4C9-CA05540DF008)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_ENDPOINT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-5B7BD089-FA44-45B3-BBA1-FDFE9F50B0E7)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_ENDPOINT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-9C095F5F-AE55-4571-A4C9-F0885A804C83)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-83FC13C5-9359-411E-9C62-05B4EB8A9C49)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_MODEL_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-176C4BD1-BF3D-4F10-9138-DDFF94B3C454)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_MODEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-23583277-1B6A-4537-A550-47A29DBC31F5)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_MODEL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-95B36CF9-46DD-49A6-98A0-F0AC07D6B747)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_MODEL_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-B7C21CDF-B280-4877-8D1C-C05AD146300D)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_MODEL_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-94AEE56A-C1BF-4E0F-A7AC-9F13DE335283)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_OBJECT_STORAGE_DATASET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-EB041780-B3D6-4FE7-810C-F0C719FEDAF1)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_T_FEW_TRAINING_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-330ED46E-A459-4049-B5AB-1D59D6987D80)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_TEXT_GENERATION_MODEL_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-EF03E90D-A11E-4604-B57F-D035D86125CC)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_UPDATE_DEDICATED_AI_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-C8F888D1-BF0E-4BFE-9212-20996B8B099A)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_UPDATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-5FA6DE44-6DAD-4FEB-8460-6BE23BCAC6AE)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_UPDATE_MODEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-4D3BA5C4-1B83-4B06-9435-9745485FFBBB)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_VANILLA_TRAINING_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-E8CC0CC5-2F44-4386-BD0C-8F84A7D465A2)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-2D91B8F0-74D3-4509-9F3F-75A8BFC96840)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-93040755-97AA-4ACA-8AC5-44F10BD73F17)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-A741B4E3-429B-474F-B67B-68889DDCFB2F)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-6EE16C32-C634-4503-A935-F43B07F8E1E1)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-7E1398DB-DD70-4337-9D88-9B035B333347)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-916EED9F-F3A8-436C-B491-45D818139DD8)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-329BCEB4-3DBB-4BC8-B758-F63C7DBBDC04)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-053D5340-0C7C-4221-9694-666F7F122478)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-C5A0AC38-5B23-413E-A961-7F9F91E0DB3C)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-B7663A81-78A1-4E13-98C4-B3045C5E6B91)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-66660A3D-3C04-4F3A-B612-6FC2532C3902)
- [DBMS_CLOUD_OCI_GENERATIVE_AI_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generative_ai_t.html#ADSDK-GUID-C7A9E81C-8711-4371-8941-16F9A993D22C)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
