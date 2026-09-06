# Media Services Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html
- Fetched: 2026-09-05 19:18 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#dcoc-content-body)

## Media Services Common Types

### DBMS_CLOUD_OCI_MEDIA_SERVICES_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_CDN_CONFIG_SECTION_T Type

Base fields of the StreamCdnConfig configuration object.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The name of the CDN configuration type.

Allowed values are: 'EDGE', 'AKAMAI_MANUAL'

### DBMS_CLOUD_OCI_MEDIA_SERVICES_AKAMAI_MANUAL_STREAM_CDN_CONFIG_T Type

Configuration fields for manual Akamai configuration.

Syntax
```

```

`dbms_cloud_oci_media_services_akamai_manual_stream_cdn_config_t`is a subtype of the`dbms_cloud_oci_media_services_stream_cdn_config_section_t`type.

Fields

Field Description

`origin_auth_sign_type`

(optional) The type of data used to compute the signature.

Allowed values are: 'ForwardURL'

`origin_auth_sign_encryption`

(optional) The type of encryption used to compute the signature.

Allowed values are: 'SHA256-HMAC'

`origin_auth_secret_key_a`

(optional) The shared secret key A, two for errorless key rotation.

`origin_auth_secret_key_nonce_a`

(optional) Nonce identifier for originAuthSecretKeyA (used to determine key used to sign).

`origin_auth_secret_key_b`

(optional) The shared secret key B, two for errorless key rotation.

`origin_auth_secret_key_nonce_b`

(optional) Nonce identifier for originAuthSecretKeyB (used to determine key used to sign).

`edge_hostname`

(optional) The hostname of the CDN edge server to use when building CDN URLs.

`edge_path_prefix`

(optional) The path to prepend when building CDN URLs.

`is_edge_token_auth`

(optional) Whether token authentication should be used at the CDN edge.

`edge_token_key`

(optional) The encryption key to use for edge token authentication.

`edge_token_salt`

(optional) Salt to use when encrypting authentication token.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_INGEST_STREAM_DISTRIBUTION_CHANNEL_DETAILS_T Type

Ingest Payload Information.

Syntax
```

```

Fields

Field Description

`ingest_payload_type`

(required) Ingest Payload Type

Allowed values are: 'ASSET_METADATA_MEDIA_ASSET'

### DBMS_CLOUD_OCI_MEDIA_SERVICES_ASSET_METADATA_ENTRY_DETAILS_T Type

Asset Metadata entry information.

Syntax
```

```

`dbms_cloud_oci_media_services_asset_metadata_entry_details_t`is a subtype of the`dbms_cloud_oci_media_services_ingest_stream_distribution_channel_details_t`type.

Fields

Field Description

`media_asset_id`

(required) The Media Asset ID to ingest into the Distribution Channel.

`compartment_id`

(optional) The compartment ID where the Ingest Workflow Job will be run.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_CHANGE_MEDIA_ASSET_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) Compartment Identifier.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_CHANGE_MEDIA_WORKFLOW_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_CHANGE_MEDIA_WORKFLOW_CONFIGURATION_COMPARTMENT_DETAILS_T Type

The details of the compartment to which the MediaWorkflowConfiguration will be moved.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_CHANGE_MEDIA_WORKFLOW_JOB_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_CHANGE_STREAM_DISTRIBUTION_CHANNEL_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_METADATA_T Type

Technical metadata for this asset.

Syntax
```

```

Fields

Field Description

`metadata`

(required) JSON string containing the technial metadata for the media asset.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_ASSET_TAG_T Type

Tags of the MediaAsset.

Syntax
```

```

Fields

Field Description

`l_type`

(optional) Type of the tag.

Allowed values are: 'USER', 'SYSTEM'

`value`

(required) Tag of the MediaAsset.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_METADATA_TBL Type

Nested table type of dbms_cloud_oci_media_services_metadata_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_ASSET_TAG_TBL Type

Nested table type of dbms_cloud_oci_media_services_media_asset_tag_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MEDIA_SERVICES_CREATE_MEDIA_ASSET_DETAILS_T Type

The information about new MediaAsset.

Syntax
```

```

Fields

Field Description

`source_media_workflow_id`

(optional) The ID of the MediaWorkflow used to produce this asset.

`media_workflow_job_id`

(optional) The ID of the MediaWorkflowJob used to produce this asset.

`source_media_workflow_version`

(optional) The version of the MediaWorkflow used to produce this asset.

`display_name`

(optional) Display name for the Media Asset. Does not have to be unique. Avoid entering confidential information.

`compartment_id`

(required) Compartment Identifier.

`l_type`

(required) The type of the media asset.

Allowed values are: 'AUDIO', 'VIDEO', 'PLAYLIST', 'IMAGE', 'CAPTION_FILE', 'UNKNOWN'

`parent_media_asset_id`

(optional) The ID of the parent asset from which this asset is derived.

`master_media_asset_id`

(optional) The ID of the senior most asset from which this asset is derived.

`bucket_name`

(optional) The name of the object storage bucket where this asset is located.

`namespace_name`

(optional) The object storage namespace where this asset is located.

`object_name`

(optional) The object storage object name that identifies this asset.

`object_etag`

(optional) eTag of the underlying object storage object.

`metadata`

(optional) List of Metadata.

`segment_range_start_index`

(optional) The start index for video segment files.

`segment_range_end_index`

(optional) The end index for video segment files.

`media_asset_tags`

(optional) list of tags for the MediaAsset.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_CREATE_MEDIA_WORKFLOW_CONFIGURATION_DETAILS_T Type

The information needed to create a new MediaWorkflowConfiguration.

Syntax
```

```

Fields

Field Description

`display_name`

(required) MediaWorkflowConfiguration identifier. Avoid entering confidential information.

`parameters`

(required) Reuseable parameter values encoded as a JSON; the top and second level JSON elements are objects. Each key of the top level object refers to a task key that is unqiue to the workflow, each of the second level objects' keys refer to the name of a parameter that is unique to the task. taskKey -&gt; parameterName -&gt; parameterValue

`compartment_id`

(required) Compartment Identifier.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_TASK_T Type

Defines the type of processing to be run at a given point in the workflow, parameters to configure the processing, and any processing that must be completed before this processing begins.

Syntax
```

```

Fields

Field Description

`l_type`

(optional) The type of process to run at this task. Refers to the name of a MediaWorkflowTaskDeclaration.

`version`

(required) The version of the MediaWorkflowTaskDeclaration.

`key`

(required) A unique identifier for this task within its workflow. Keys are used to reference a task within workflows and MediaWorkflowJobs. Tasks are referenced as prerequisites and to track output and state.

`prerequisites`

(optional) Keys to the other tasks in this workflow that must be completed before execution of this task can begin.

`enable_parameter_reference`

(optional) Allows this task to be conditionally enabled. If no value or a blank value is given, the task is unconditionally enbled. Otherwise the given string specifies a parameter of the job created for this task's workflow using the JSON pointer syntax. The JSON pointer is validated when a job is created from the workflow of this task.

`enable_when_referenced_parameter_equals`

(optional) Used in conjunction with enableParameterReference to conditionally enable a task. When a job is created from the workflow of this task, the task will only be enabled if the value of the parameter specified by enableParameterReference is equal to the value of this property. This property must be prenset if and only if a enableParameterReference is given. The value is a JSON node.

`parameters`

(optional) Data specifiying how this task is to be run. The data is a JSON object that must conform to the JSON Schema specified by the parameters of the MediaWorkflowTaskDeclaration this task references. The parameters may contain values or references to other parameters.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_TASK_TBL Type

Nested table type of dbms_cloud_oci_media_services_media_workflow_task_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MEDIA_SERVICES_CREATE_MEDIA_WORKFLOW_DETAILS_T Type

The information about new MediaWorkflow.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Name for the MediaWorkflow. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(required) Compartment Identifier.

`tasks`

(optional) The processing to be done in this workflow. Each key of the MediaWorkflowTasks in this array must be unique within the array. The order of tasks given here will be preserved.

`media_workflow_configuration_ids`

(optional) Configurations to be applied to all the jobs for this workflow. Parameters in these configurations are overridden by parameters in the MediaWorkflowConfigurations of the MediaWorkflowJob and the parameters of the MediaWorkflowJob.

`parameters`

(optional) JSON object representing named parameters and their default values that can be referenced throughout this workflow. The values declared here can be overridden by the MediaWorkflowConfigurations or parameters supplied when creating MediaWorkflowJobs from this MediaWorkflow.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_CREATE_MEDIA_WORKFLOW_JOB_DETAILS_T Type

Information to run the MediaWorkflow.

Syntax
```

```

Fields

Field Description

`workflow_identifier_type`

(required) Discriminate identification of a workflow by name versus a workflow by ID.

Allowed values are: 'ID', 'NAME'

`media_workflow_configuration_ids`

(optional) Configurations to be applied to this run of the workflow.

`compartment_id`

(required) ID of the compartment in which the job should be created.

`display_name`

(optional) Name of the Media Workflow Job. Does not have to be unique. Avoid entering confidential information.

`parameters`

(optional) Parameters that override parameters specified in MediaWorkflowTaskDeclarations, the MediaWorkflow, the MediaWorkflow's MediaWorkflowConfigurations and the MediaWorkflowConfigurations of this MediaWorkflowJob. The parameters are given as JSON. The top level and 2nd level elements must be JSON objects (vs arrays, scalars, etc). The top level keys refer to a task's key and the 2nd level keys refer to a parameter's name.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_CREATE_MEDIA_WORKFLOW_JOB_BY_ID_DETAILS_T Type

Information to run a MediaWorkflow identified by its OCID.

Syntax
```

```

`dbms_cloud_oci_media_services_create_media_workflow_job_by_id_details_t`is a subtype of the`dbms_cloud_oci_media_services_create_media_workflow_job_details_t`type.

Fields

Field Description

`media_workflow_id`

(optional) OCID of the MediaWorkflow that should be run.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_CREATE_MEDIA_WORKFLOW_JOB_BY_NAME_DETAILS_T Type

Information to run a system MediaWorkflow identified by its name.

Syntax
```

```

`dbms_cloud_oci_media_services_create_media_workflow_job_by_name_details_t`is a subtype of the`dbms_cloud_oci_media_services_create_media_workflow_job_details_t`type.

Fields

Field Description

`media_workflow_name`

(optional) Name of the system MediaWorkflow that should be run.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_CREATE_STREAM_CDN_CONFIG_DETAILS_T Type

The information about the new CDN Configuration.

Syntax
```

```

Fields

Field Description

`display_name`

(required) CDN Config display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.

`distribution_channel_id`

(required) Distribution Channel Identifier.

`is_enabled`

(optional) Whether publishing to CDN is enabled.

`config`

(required)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_CREATE_STREAM_DISTRIBUTION_CHANNEL_DETAILS_T Type

The information about the new Stream Distribution Channel.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Stream Distribution Channel display name. Avoid entering confidential information.

`compartment_id`

(required) Compartment Identifier.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_PACKAGING_CONFIG_ENCRYPTION_T Type

The encryption used by the stream packaging configuration.

Syntax
```

```

Fields

Field Description

`algorithm`

(required) The encryption algorithm for the stream packaging configuration.

Allowed values are: 'NONE', 'AES128'

### DBMS_CLOUD_OCI_MEDIA_SERVICES_CREATE_STREAM_PACKAGING_CONFIG_DETAILS_T Type

The information about the new Packaging Configuration.

Syntax
```

```

Fields

Field Description

`distribution_channel_id`

(required) Unique identifier of the Distribution Channel that this stream packaging configuration belongs to.

`display_name`

(required) The name of the stream Packaging Configuration. Avoid entering confidential information.

`stream_packaging_format`

(required) The output format for the package.

Allowed values are: 'HLS', 'DASH'

`segment_time_in_seconds`

(required) The duration in seconds for each fragment.

`encryption`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_PACKAGING_CONFIG_T Type

A stream packaging configuration for a Distribution Channel.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`compartment_id`

(required) Compartment Identifier

`distribution_channel_id`

(required) Unique identifier of the Distribution Channel that this stream packaging configuration belongs to.

`display_name`

(required) The name of the stream packaging configuration. Avoid entering confidential information.

`stream_packaging_format`

(required) The output format for the package.

Allowed values are: 'HLS', 'DASH'

`segment_time_in_seconds`

(required) The duration in seconds for each fragment.

`encryption`

(optional)

`time_created`

(optional) The time when the Packaging Configuration was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time when the Packaging Configuration was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the Packaging Configuration.

Allowed values are: 'ACTIVE', 'NEEDS_ATTENTION', 'DELETED'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_DASH_STREAM_PACKAGING_CONFIG_T Type

Configuration fields for a DASH Packaging Configuration.

Syntax
```

```

`dbms_cloud_oci_media_services_dash_stream_packaging_config_t`is a subtype of the`dbms_cloud_oci_media_services_stream_packaging_config_t`type.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_EDGE_STREAM_CDN_CONFIG_T Type

Configuration fields for Edge configuration.

Syntax
```

```

`dbms_cloud_oci_media_services_edge_stream_cdn_config_t`is a subtype of the`dbms_cloud_oci_media_services_stream_cdn_config_section_t`type.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_ERROR_T Type

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

### DBMS_CLOUD_OCI_MEDIA_SERVICES_GENERATE_SESSION_TOKEN_DETAILS_T Type

Information about the new session token.

Syntax
```

```

Fields

Field Description

`time_expires`

(optional) Token expiry time. An RFC3339 formatted datetime string.

`scopes`

(required) Array of scopes the token can act upon.

Allowed values are: 'PLAYLIST', 'EDGE'

`packaging_config_id`

(required) The packaging config resource identifier used to limit the scope of the token.

`asset_ids`

(optional) Array of asset resource IDs used to limit the scope of the token.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_HLS_STREAM_PACKAGING_CONFIG_T Type

Configuration fields for a HLS Packaging Configuration.

Syntax
```

```

`dbms_cloud_oci_media_services_hls_stream_packaging_config_t`is a subtype of the`dbms_cloud_oci_media_services_stream_packaging_config_t`type.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_INGEST_STREAM_DISTRIBUTION_CHANNEL_RESULT_T Type

The Ingest Workflow Job information.

Syntax
```

```

Fields

Field Description

`media_workflow_job_id`

(required) Identifier of the Ingest Workflow Job created.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_JOB_OUTPUT_T Type

The output result of an executed MediaWorkflowJob.

Syntax
```

```

Fields

Field Description

`asset_type`

(optional) Type of job output.

Allowed values are: 'AUDIO', 'VIDEO', 'PLAYLIST', 'IMAGE', 'CAPTION_FILE', 'TRANSCRIPTION_JOB', 'VISION_JOB', 'TEXT_ANALYSIS', 'OTHER'

`namespace_name`

(optional) The namespace name of the job output.

`bucket_name`

(optional) The bucket name of the job output.

`object_name`

(optional) The object name of the job output.

`id`

(optional) The ID associated with the job output.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_ASSET_T Type

Represents the metadata associated with an asset that has been either produced by or registered with Media Services.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`compartment_id`

(required) The ID of the compartment containing the MediaAsset.

`source_media_workflow_id`

(optional) The ID of the MediaWorkflow used to produce this asset.

`media_workflow_job_id`

(optional) The ID of the MediaWorkflowJob used to produce this asset.

`source_media_workflow_version`

(optional) The version of the MediaWorkflow used to produce this asset.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`time_created`

(optional) The time when the MediaAsset was created. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the MediaAsset.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`l_type`

(required) The type of the media asset.

Allowed values are: 'AUDIO', 'VIDEO', 'PLAYLIST', 'IMAGE', 'CAPTION_FILE', 'UNKNOWN'

`parent_media_asset_id`

(optional) The ID of the parent asset from which this asset is derived.

`master_media_asset_id`

(optional) The ID of the senior most asset from which this asset is derived.

`bucket_name`

(optional) The name of the object storage bucket where this represented asset is located.

`namespace_name`

(optional) The object storage namespace where this asset is located.

`object_name`

(optional) The object storage object name that identifies this asset.

`object_etag`

(optional) eTag of the underlying object storage object.

`time_updated`

(optional) The time when the MediaAsset was updated. An RFC3339 formatted datetime string.

`segment_range_start_index`

(optional) The start index for video segment files.

`segment_range_end_index`

(optional) The end index of video segment files.

`metadata`

(optional) List of Metadata.

`media_asset_tags`

(optional) List of tags for the MediaAsset.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_ASSET_SUMMARY_T Type

Summary of the MediaAsset.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`compartment_id`

(required) The ID of the compartment containing the MediaAsset.

`display_name`

(optional) MediaAsset name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`time_created`

(optional) The time the the MediaAsset was created. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the MediaAsset.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`l_type`

(required) The type of the media asset.

Allowed values are: 'AUDIO', 'VIDEO', 'PLAYLIST', 'IMAGE', 'CAPTION_FILE', 'UNKNOWN'

`time_updated`

(optional) The time the MediaAsset was updated. An RFC3339 formatted datetime string.

`master_media_asset_id`

(optional) The ID of the senior most asset from which this asset is derived.

`parent_media_asset_id`

(optional) The ID of the parent asset from which this asset is derived.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_ASSET_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_media_services_media_asset_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_ASSET_COLLECTION_T Type

Results of a mediaAsset search. Contains both MediaAssetSummary items and other data.

Syntax
```

```

Fields

Field Description

`items`

(required) List of mediaAssets.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_ASSET_DISTRIBUTION_CHANNEL_ATTACHMENT_T Type

Attachment between MediaAsset and streaming DistributionChannel.

Syntax
```

```

Fields

Field Description

`distribution_channel_id`

(required) OCID of associated Distribution Channel.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`version`

(required) Version of the attachment.

`lifecycle_state`

(required) Lifecycle state of the attachment.

Allowed values are: 'CREATING', 'ACTIVE', 'NEEDS_ATTENTION', 'UPDATING'

`metadata_ref`

(required) The identifier for the metadata.

`media_workflow_job_id`

(optional) The ingest MediaWorkflowJob ID that created this attachment.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_ASSET_DISTRIBUTION_CHANNEL_ATTACHMENT_SUMMARY_T Type

Summary of the MediaAssetDistributionChannelAttachment.

Syntax
```

```

Fields

Field Description

`media_asset_id`

(required) OCID of associated media asset.

`display_name`

(optional) Display name for the MediaAssetDistributionChannelAttachment. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`distribution_channel_id`

(required) OCID of associated Distribution Channel.

`version`

(required) Version number of the attachment.

`lifecycle_state`

(required) Lifecycle state of the attachment.

Allowed values are: 'CREATING', 'ACTIVE', 'NEEDS_ATTENTION', 'UPDATING'

`metadata_ref`

(required) The identifier for the metadata.

`media_workflow_job_id`

(optional) The ingest MediaWorkflowJob ID that created this attachment.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_ASSET_DISTRIBUTION_CHANNEL_ATTACHMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_media_services_media_asset_distribution_channel_attachment_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_ASSET_DISTRIBUTION_CHANNEL_ATTACHMENT_COLLECTION_T Type

Results of a MediaAssetDistributionChannelAttachment search. Contains the MediaAssetDistributionChannelAttachmentSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of Distribution Channel attachments.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_T Type

Configurable workflows that define the series of tasks that will be used to process video files.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(required) Name of the Media Workflow. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(required) Compartment Identifier.

`tasks`

(optional) The processing to be done in this workflow. Each key of the MediaWorkflowTasks in this array is unique within the array. The order of the items is preserved from the order of the tasks array in CreateMediaWorkflowDetails or UpdateMediaWorkflowDetails.

`media_workflow_configuration_ids`

(optional) Configurations to be applied to all the runs of this workflow. Parameters in these configurations are overridden by parameters in the MediaWorkflowConfigurations of the MediaWorkflowJob and the parameters of the MediaWorkflowJob. If the same parameter appears in multiple configurations, the values that appear in the configuration at the highest index will be used.

`parameters`

(optional) JSON object representing named parameters and their default values that can be referenced throughout this workflow. The values declared here can be overridden by the MediaWorkflowConfigurations or parameters supplied when creating MediaWorkflowJobs from this MediaWorkflow.

`time_created`

(optional) The time when the MediaWorkflow was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time when the MediaWorkflow was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the MediaWorkflow.

Allowed values are: 'ACTIVE', 'NEEDS_ATTENTION', 'DELETED'

`lifecyle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`version`

(optional) The version of the MediaWorkflow.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_SUMMARY_T Type

Summary of the MediaWorkflow.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(optional) Name for the MediaWorkflow. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(required) Compartment Identifier.

`time_created`

(optional) The time when the MediaWorkflow was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time when the MediaWorkflow was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the MediaWorkflow.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`version`

(optional) The version of MediaWorkflow.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_media_services_media_workflow_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_COLLECTION_T Type

Results of a MediaWorkflow search. Contains both MediaWorkflowSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of all MediaWorkflows.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_CONFIGURATION_T Type

Resusable set of values that can be referenced either in a MediaWorkflow or when running a MediaWorkflowJob.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(required) Display name for the MediaWorkflowConfiguration. Avoid entering confidential information.

`compartment_id`

(required) Compartment Identifier.

`parameters`

(required) Reuseable parameter values encoded as a JSON; the top and second level JSON elements are objects. Each key of the top level object refer to a task key that is unqiue to the workflow, each of the second level objects' keys refer to the name of a parameter that is unique to the task. taskKey -&gt; parameterName -&gt; parameterValue

`time_created`

(optional) The time when the the MediaWorkflowConfiguration was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time when the MediaWorkflowConfiguration was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the MediaWorkflowConfiguration.

Allowed values are: 'ACTIVE', 'DELETED'

`lifecyle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_CONFIGURATION_SUMMARY_T Type

Summary of the MediaWorkflowConfiguration.

Syntax
```

```

Fields

Field Description

`id`

(required) Immutable unique identifier for the MediaWorkflowConfiguration.

`display_name`

(required) Name of the MediaWorkflowConfiguration. Avoid entering confidential information.

`compartment_id`

(required) Compartment identifier

`time_created`

(optional) The time when the MediaWorkflowConfiguration was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time when the MediaWorkflowConfiguration was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the MediaWorkflowConfiguration.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_CONFIGURATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_media_services_media_workflow_configuration_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_CONFIGURATION_COLLECTION_T Type

Results of a mediaWorkflowConfiguration search. Contains boh MediaWorkflowConfigurationSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of the mediaWorkflowConfigurationSummary objects.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_TASK_STATE_T Type

Status of a task in a workflow job being run.

Syntax
```

```

Fields

Field Description

`key`

(optional) Unique key within a MediaWorkflowJob for the task.

`lifecycle_state`

(optional) The current state of the MediaWorkflowJob task.

`lifecycle_details`

(optional) The lifecycle details of MediaWorkflowJob task.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_TASK_STATE_TBL Type

Nested table type of dbms_cloud_oci_media_services_media_workflow_task_state_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MEDIA_SERVICES_JOB_OUTPUT_TBL Type

Nested table type of dbms_cloud_oci_media_services_job_output_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_JOB_T Type

A MediaWorkflowJob represents a run of a MediaWorkflow for a specific set of parameters and configurations.

Syntax
```

```

Fields

Field Description

`media_workflow_configuration_ids`

(optional) Configurations to be applied to this run of the workflow.

`media_workflow_id`

(required) The workflow to execute.

`id`

(required) Unique identifier for this run of the workflow.

`compartment_id`

(required) Compartment Identifier.

`display_name`

(optional) Name of the Media Workflow Job. Does not have to be unique. Avoid entering confidential information.

`lifecycle_state`

(optional) The current state of the MediaWorkflowJob.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`lifecycle_details`

(optional) The lifecyle details.

`task_lifecycle_state`

(optional) Status of each task.

`parameters`

(optional) Parameters that override parameters specified in MediaWorkflowTaskDeclarations, the MediaWorkflow, the MediaWorkflow's MediaWorkflowConfigurations and the MediaWorkflowConfigurations of this MediaWorkflowJob. The parameters are given as JSON. The top level and 2nd level elements must be JSON objects (vs arrays, scalars, etc). The top level keys refer to a task's key and the 2nd level keys refer to a parameter's name.

`time_created`

(optional) Creation time of the job. An RFC3339 formatted datetime string.

`time_updated`

(optional) Updated time of the job. An RFC3339 formatted datetime string.

`runnable`

(optional) A JSON representation of the job as it will be run by the system. All the task declarations, configurations and parameters are merged. Parameter values are all fully resolved.

`outputs`

(optional) A list of JobOutput for the workflowJob.

`time_started`

(optional) Time when the job started to execute. An RFC3339 formatted datetime string.

`time_ended`

(optional) Time when the job finished. An RFC3339 formatted datetime string.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_JOB_SUMMARY_T Type

Summary of a MediaWorkflowJob.

Syntax
```

```

Fields

Field Description

`media_workflow_id`

(optional) The workflow to execute.

`id`

(optional) Unique identifier for this job.

`display_name`

(optional) Name of the Media Workflow Job. Does not have to be unique. Avoid entering confidential information.

`time_created`

(optional) Creation time of the job. An RFC3339 formatted datetime string.

`time_updated`

(optional) Updated time of the job. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the MediaWorkflowJob.

`lifecycle_details`

(optional) The lifecyle details.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_JOB_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_media_services_media_workflow_job_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_JOB_COLLECTION_T Type

Results of a mediaWorkflowJob search, a list of MediaWorkflowJobSummary items and metadata of the search.

Syntax
```

```

Fields

Field Description

`items`

(required) List of mediaWorkflowJob items.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_JOB_FACT_T Type

One fact of a list of facts associated to a MediaWorkflowJob that presents a point-in-time snapshot of the resources, data and events that were composed to generate a runnable job. This information will be used internally to trouble-shoot problematic workflows or jobs.

Syntax
```

```

Fields

Field Description

`media_workflow_job_id`

(required) Reference to the parent job.

`key`

(required) System generated serial number to uniquely identify a detail in order within a MediaWorkflowJob.

`name`

(required) Unique name. It is read-only and generated for the fact.

`l_type`

(required) The type of information contained in this detail.

`detail`

(required) The body of the detail captured as JSON.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_JOB_FACT_SUMMARY_T Type

Summary of a MediaWorkflowJobFact

Syntax
```

```

Fields

Field Description

`media_workflow_job_id`

(required) Reference to the parent job.

`key`

(required) System generated serial number to uniquely identify a detail in order within a MediaWorkflowJob.

`name`

(required) Unique name. It is read-only and generated for the fact.

`l_type`

(required) The type of information contained in this detail.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_JOB_FACT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_media_services_media_workflow_job_fact_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_JOB_FACT_COLLECTION_T Type

Results of a jobDetail search, a list of MediaWorkflowJobFacts items and metadata of the search.

Syntax
```

```

Fields

Field Description

`items`

(required) List of mediaWorkflowJob items.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_TASK_DECLARATION_T Type

The declaration of a type of task that can be used in a MediaWorkflow.

Syntax
```

```

Fields

Field Description

`name`

(required) MediaWorkflowTaskDeclaration identifier. The name and version should be unique among MediaWorkflowTaskDeclarations.

`version`

(required) The version of MediaWorkflowTaskDeclaration, incremented whenever the team implementing the task processor modifies the JSON schema of this declaration's definitions, parameters or list of required parameters.

`parameters_schema`

(required) JSON schema specifying the parameters supported by this type of task. This is used to validate tasks' parameters when jobs are created.

`parameters_schema_allowing_references`

(required) JSON schema similar to the parameterSchema, but permits parameter values to refer to other parameters using the ${/path/to/another/parmeter} syntax. This is used to validate task parameters when workflows are created.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_TASK_DECLARATION_TBL Type

Nested table type of dbms_cloud_oci_media_services_media_workflow_task_declaration_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_TASK_DECLARATION_COLLECTION_T Type

Results of the ListMediaWorkflowTaskDeclaration operation, a list of MediaWorkflowTaskDeclarations.

Syntax
```

```

Fields

Field Description

`items`

(required) List of MediaWorkflowTaskDeclaration objects.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_SESSION_TOKEN_T Type

The generated sessionToken details.

Syntax
```

```

Fields

Field Description

`token`

(required) The generated session token.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_CDN_CONFIG_T Type

Configuration used for integrating with a CDN.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(required) The CDN Configuration identifier or display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.

`compartment_id`

(required) Compartment Identifier.

`distribution_channel_id`

(required) Distribution Channel Identifier.

`is_enabled`

(required) Whether publishing to CDN is enabled.

`config`

(required)

`time_created`

(optional) The time when the CDN Config was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time when the CDN Config was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the CDN Configuration.

Allowed values are: 'ACTIVE', 'NEEDS_ATTENTION', 'DELETED'

`lifecyle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_CDN_CONFIG_SUMMARY_T Type

Summary of the StreamCdnConfig.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(required) The CDN Configuration identifier or display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.

`compartment_id`

(required) Compartment Identifier.

`distribution_channel_id`

(required) Distribution Channel Identifier.

`is_enabled`

(required) Whether publishing to CDN is enabled.

`time_created`

(optional) The time when the the CDN Configuration was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the CDN Configuration was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the CDN Configuration.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_CDN_CONFIG_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_media_services_stream_cdn_config_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_CDN_CONFIG_COLLECTION_T Type

Results of a streamCdnConfig search. Contains both StreamCdnConfigSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of streamCdnConfigs.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_DISTRIBUTION_CHANNEL_T Type

Channel used for delivering video streams to the end-users.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(required) Stream Distribution Channel display name. Avoid entering confidential information.

`compartment_id`

(required) Compartment Identifier.

`domain_name`

(optional) Unique domain name of the Distribution Channel.

`time_created`

(optional) The time when the Stream Distribution Channel was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time when the Stream Distribution Channel was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the Stream Distribution Channel.

Allowed values are: 'ACTIVE', 'NEEDS_ATTENTION', 'DELETED'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_DISTRIBUTION_CHANNEL_SUMMARY_T Type

Summary of the Stream Distribution Channel.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(required) Stream Distribution Channel display name. Avoid entering confidential information.

`compartment_id`

(required) Compartment Identifier.

`domain_name`

(optional) The unique domain name of the Distribution Channel.

`time_created`

(optional) The time when the Stream Distribution Channel was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time when the Stream Distribution Channel was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the Stream Distribution Channel.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_DISTRIBUTION_CHANNEL_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_media_services_stream_distribution_channel_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_DISTRIBUTION_CHANNEL_COLLECTION_T Type

Results of a Stream Distribution Channel search. Contains both StreamDistributionChannelSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of Stream Distribution Channels.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_PACKAGING_CONFIG_SUMMARY_T Type

Summary of the Packaging Configuration.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`compartment_id`

(required) Compartment Identifier.

`distribution_channel_id`

(required) Unique identifier of the distribution channel that this stream packaging configuration belongs to.

`display_name`

(required) Stream Packaging Configuration display name. Avoid entering confidential information.

`time_created`

(optional) The time when the Distribution Channel was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time when the Distribution Channel was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the Distribution Channel.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_PACKAGING_CONFIG_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_media_services_stream_packaging_config_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_PACKAGING_CONFIG_COLLECTION_T Type

Results of a Packaging Configuration search. Contains both StreamPackagingConfigSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of Packaging Configurations.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_PACKAGING_CONFIG_ENCRYPTION_AES128_T Type

AES128 encryption type (enabled by default).

Syntax
```

```

`dbms_cloud_oci_media_services_stream_packaging_config_encryption_aes128_t`is a subtype of the`dbms_cloud_oci_media_services_stream_packaging_config_encryption_t`type.

Fields

Field Description

`kms_key_id`

(optional) The identifier of the customer managed Vault KMS symmetric encryption key (null if Oracle managed).

### DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_PACKAGING_CONFIG_ENCRYPTION_NONE_T Type

Disables encryption.

Syntax
```

```

`dbms_cloud_oci_media_services_stream_packaging_config_encryption_none_t`is a subtype of the`dbms_cloud_oci_media_services_stream_packaging_config_encryption_t`type.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_SYSTEM_MEDIA_WORKFLOW_T Type

A named list of tasks to be used to run a job or as a template to create a MediaWorkflow.

Syntax
```

```

Fields

Field Description

`name`

(required) System provided unique identifier for this static media workflow.

`description`

(optional) Description of this workflow's processing and how that processing can be customized by specifying parameter values.

`parameters`

(optional) JSON object representing named parameters and their default values that can be referenced throughout this workflow. The values declared here can be overridden by the MediaWorkflowConfigurations or parameters supplied when creating MediaWorkflowJobs from this MediaWorkflow.

`tasks`

(required) The processing to be done in this workflow. Each key of the MediaWorkflowTasks in this array is unique within the array. The order of the items is preserved from the order of the tasks array in CreateMediaWorkflowDetails or UpdateMediaWorkflowDetails.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_SYSTEM_MEDIA_WORKFLOW_TBL Type

Nested table type of dbms_cloud_oci_media_services_system_media_workflow_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MEDIA_SERVICES_SYSTEM_MEDIA_WORKFLOW_COLLECTION_T Type

Result for the ListSystemMediaWorkflows operation.

Syntax
```

```

Fields

Field Description

`items`

(required) List of SytemMediaWorkflow items.

### DBMS_CLOUD_OCI_MEDIA_SERVICES_UPDATE_MEDIA_ASSET_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Display name for the Media Asset. Does not have to be unique. Avoid entering confidential information.

`l_type`

(optional) The type of the media asset.

Allowed values are: 'AUDIO', 'VIDEO', 'PLAYLIST', 'IMAGE', 'CAPTION_FILE', 'UNKNOWN'

`parent_media_asset_id`

(optional) The ID of the parent asset from which this asset is derived.

`master_media_asset_id`

(optional) The ID of the senior most asset from which this asset is derived.

`metadata`

(optional) List of Metadata.

`media_asset_tags`

(optional) List of tags for the MediaAsset.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_UPDATE_MEDIA_WORKFLOW_CONFIGURATION_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Name for the MediaWorkflowConfiguration. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`parameters`

(optional) Reuseable parameter values encoded as a JSON; the top and second level JSON elements are objects. Each key of the top level object refer to a task key that is unqiue to the workflow, each of the second level objects' keys refer to the name of a parameter that is unique to the task. taskKey -&gt; parameterName -&gt; parameterValue

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_UPDATE_MEDIA_WORKFLOW_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Name for the MediaWorkflow. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`tasks`

(optional) The processing to be done in this workflow. Each key of the MediaWorkflowTasks in this array must be unique within the array.

`media_workflow_configuration_ids`

(optional) Configurations to be applied to all jobs for this workflow. Parameters in these configurations are overridden by parameters in the MediaWorkflowConfigurations of the MediaWorkflogJob and the parameters of the MediaWorkflowJob.

`parameters`

(optional) JSON object representing named parameters and their default values that can be referenced throughout this workflow. The values declared here can be overridden by the MediaWorkflowConfigurations or parameters supplied when creating MediaWorkflowJobs from this MediaWorkflow.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_UPDATE_MEDIA_WORKFLOW_JOB_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Name for the MediaWorkflowJob. Does not have to be unique. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_UPDATE_STREAM_CDN_CONFIG_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) CDN Config display name.

`is_enabled`

(optional) Whether CDN is enabled for publishing.

`config`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_UPDATE_STREAM_DISTRIBUTION_CHANNEL_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Stream Distribution channel display name. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MEDIA_SERVICES_UPDATE_STREAM_PACKAGING_CONFIG_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The name of the stream Packaging Configuration. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

- [Media Services Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-54ECD611-F837-414B-85E0-907DAB600C38)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-C5FE9C62-4264-4C50-A2F7-AD2986AB45F9)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_CDN_CONFIG_SECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-5E20E0B5-731E-4604-98F4-248E9B1A3EE2)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_AKAMAI_MANUAL_STREAM_CDN_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-9E5F2267-2B68-48AB-AE0C-36361448B244)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_INGEST_STREAM_DISTRIBUTION_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-703AC3AB-F54F-4085-B854-06E477FF1FE6)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_ASSET_METADATA_ENTRY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-3CC85D9A-AFB2-4915-9706-3998C382C759)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_CHANGE_MEDIA_ASSET_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-F9B962BD-E827-4844-967C-5BFF5155A8F2)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_CHANGE_MEDIA_WORKFLOW_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-4514E746-4E26-4C71-A3AC-6685B33460FC)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_CHANGE_MEDIA_WORKFLOW_CONFIGURATION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-9579FE14-CD5F-48FC-B784-088F68542615)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_CHANGE_MEDIA_WORKFLOW_JOB_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-6E4B33DC-ACFC-4D3D-840D-A19DF09178FB)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_CHANGE_STREAM_DISTRIBUTION_CHANNEL_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-5EA8015D-572C-42D6-BC00-E0351F2ADDDB)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-57E6F646-F5CA-48CD-9946-2427C7F327A6)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_ASSET_TAG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-7B62C0A9-B9CC-4F96-8F7E-4CC394068153)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_METADATA_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-C7A26A60-1EA7-467F-BD2A-1CBC18CD0B5D)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_ASSET_TAG_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-D0A71D2A-8C13-470B-995C-ECA4E1175E0B)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_CREATE_MEDIA_ASSET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-61FDA156-6EBA-4558-88F8-75C11E7D13E2)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_CREATE_MEDIA_WORKFLOW_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-0FC52237-D050-45B8-8DDC-5C6AA6EED349)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-21F8C90F-E179-426D-9E8E-9EE14921BD8F)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_TASK_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-17C34613-18FF-485C-98BC-EF6E8421C70E)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_CREATE_MEDIA_WORKFLOW_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-24A460A8-C423-4868-8549-8487462A4EF1)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_CREATE_MEDIA_WORKFLOW_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-04A66EEE-C280-4FCF-9D92-10C51BDF9E5E)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_CREATE_MEDIA_WORKFLOW_JOB_BY_ID_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-A91C20CD-25CD-46F3-A9E9-284784C247A9)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_CREATE_MEDIA_WORKFLOW_JOB_BY_NAME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-B8405C84-9BE6-42B7-A026-70EDD22C6841)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_CREATE_STREAM_CDN_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-8CAD1517-83C8-48C1-9B8E-E916AD5B3AEF)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_CREATE_STREAM_DISTRIBUTION_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-30B15D08-C230-415E-B195-0367835B3F7D)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_PACKAGING_CONFIG_ENCRYPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-02A7ECDC-EF52-4022-971D-A23C70318D19)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_CREATE_STREAM_PACKAGING_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-09C6F14E-3C74-49CF-A10C-537A27A34A7B)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_PACKAGING_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-88D91FA9-470B-4940-9FB4-2A5816E072CC)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_DASH_STREAM_PACKAGING_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-53BFCA28-A669-48B1-95BB-674FE6B25185)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_EDGE_STREAM_CDN_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-2C95FBAC-2027-48D5-9B01-E49FC6593062)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-CD584EFB-C1EC-4DC5-BC84-4A8D39DCE581)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_GENERATE_SESSION_TOKEN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-089691B3-6A50-429F-AA76-1118150E5F05)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_HLS_STREAM_PACKAGING_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-EA2B03F1-33FB-4618-8A62-8A60439E7A7A)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_INGEST_STREAM_DISTRIBUTION_CHANNEL_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-737AAB54-8568-4BBB-89A4-CF491BB92754)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_JOB_OUTPUT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-1A117E60-1EDD-436D-ABB1-E5F4A5EB9203)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_ASSET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-8CDA19BB-590D-4CC3-BAB6-544E64646F85)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_ASSET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-4CACC808-9503-41DE-A927-EF70EF3FAB1E)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_ASSET_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-34C4B23F-4271-416C-BA59-EBE0C76B4065)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_ASSET_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-5E4C539E-7B9F-47CC-A4AD-773D0C243F98)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_ASSET_DISTRIBUTION_CHANNEL_ATTACHMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-1AFA587D-3322-460F-9867-2F1F02C5E1FE)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_ASSET_DISTRIBUTION_CHANNEL_ATTACHMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-8C82407D-BFEA-41DC-89F7-FC0915FB1595)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_ASSET_DISTRIBUTION_CHANNEL_ATTACHMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-9752178B-093C-4722-A69D-23C9AE637A8D)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_ASSET_DISTRIBUTION_CHANNEL_ATTACHMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-1D4DAD8A-BC0A-42CA-860A-ACD576D9D105)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-F59EBC3B-4231-4EB0-A56E-42A8C0D1767A)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-F8753B19-A20C-45C9-A151-9D7402D2B627)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-DFD49DAD-C580-4A6A-BFD3-E0D870A6F65B)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-9F1FE4A4-54EC-4EA2-B0C3-8FE8A6DABBF8)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-8EA00D2D-5E59-404D-A312-A72AC3DDB36C)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_CONFIGURATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-F9DBDEFA-CB0D-4F37-B088-4D4B0F2FD705)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_CONFIGURATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-B0236256-ACCE-4F00-B547-BD8BB1CF4F51)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_CONFIGURATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-B8802264-783F-4B35-88EF-0C3A059000F0)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_TASK_STATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-AF2D9903-E54E-4409-8929-40A35D717804)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_TASK_STATE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-8C8DCCED-C3CA-4944-BC08-61302F240979)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_JOB_OUTPUT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-4F405E39-10E1-440E-8739-4252B9900BD6)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_JOB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-43B66228-3766-4D82-925B-37D031A11E62)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_JOB_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-06F699E0-444B-4559-909F-93EB12FD3EEA)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_JOB_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-BB884A85-41DA-4D99-A70E-86923A546B99)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_JOB_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-BFB222BC-12BB-4DA3-9072-70E3603FC4F8)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_JOB_FACT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-B88F56C8-B694-4A5B-A1C4-9BD7CFFBD9E9)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_JOB_FACT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-05DD082C-F6F7-428C-9B83-9E44C745ECC0)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_JOB_FACT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-1C9C4F04-6151-4723-8A3F-19289B84DBCE)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_JOB_FACT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-EED18109-57E0-4CC0-B8B1-0169791A8974)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_TASK_DECLARATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-A018B47D-9EAC-4916-9569-39DCC8378816)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_TASK_DECLARATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-BBB364AE-F665-4F39-99DE-FA229C8E6B3E)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_MEDIA_WORKFLOW_TASK_DECLARATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-F637FBF8-4979-4C53-86EA-6768088E9363)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_SESSION_TOKEN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-2F03DE5A-F5B8-463D-B4CD-987EB7138F5F)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_CDN_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-A41C8FB1-3E5D-484F-A3C3-15421EB92F6B)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_CDN_CONFIG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-E4DC6B3E-D0C5-45E6-8CC3-A48D760AC3EE)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_CDN_CONFIG_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-132B1443-EC1E-4864-9B13-5E9B7A17966A)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_CDN_CONFIG_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-435C3AD8-79C2-4934-911D-A25E27910E6F)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_DISTRIBUTION_CHANNEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-00D09493-050B-4BD7-8BB3-99FBB60F6910)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_DISTRIBUTION_CHANNEL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-CCC45434-B565-4026-BB79-00204136F5B9)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_DISTRIBUTION_CHANNEL_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-A0BC2013-C8DC-47F5-9DE5-CD356F9D018D)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_DISTRIBUTION_CHANNEL_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-40186126-5B97-4F8B-94A1-1AFEF4AD11DC)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_PACKAGING_CONFIG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-2597ED6D-03A9-442C-BC1C-6DA2838BAACC)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_PACKAGING_CONFIG_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-81791639-E605-4749-9CBE-6A2934F7B139)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_PACKAGING_CONFIG_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-35959CFE-E48A-416C-8648-2B798014926A)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_PACKAGING_CONFIG_ENCRYPTION_AES128_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-3A8180A8-0FA1-48AD-B529-93BD2B91E4A9)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_STREAM_PACKAGING_CONFIG_ENCRYPTION_NONE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-36B2E5EE-D5CC-46E1-BF71-849A17A8A647)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_SYSTEM_MEDIA_WORKFLOW_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-9DE9170C-2F3B-4259-BA8C-822DA49CA4D5)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_SYSTEM_MEDIA_WORKFLOW_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-D0BF5FA2-D342-4C34-BA38-B79B47B23DBD)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_SYSTEM_MEDIA_WORKFLOW_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-61EDD897-99DD-4A3E-8AF3-29E209B07016)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_UPDATE_MEDIA_ASSET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-6876B0F4-1961-4CFB-9013-D0B58E003567)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_UPDATE_MEDIA_WORKFLOW_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-B02AC9B0-6F12-409E-9B99-44467BD2330C)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_UPDATE_MEDIA_WORKFLOW_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-4F0E62FA-0AAB-44EB-BA58-ED779FD57EC6)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_UPDATE_MEDIA_WORKFLOW_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-531E1186-088F-4143-94B6-A210F7F4D206)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_UPDATE_STREAM_CDN_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-8BF7AA05-A2F1-4524-BCAF-67AD92E6EA91)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_UPDATE_STREAM_DISTRIBUTION_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-5E420683-92B2-4B57-A38F-A11596A5816C)
- [DBMS_CLOUD_OCI_MEDIA_SERVICES_UPDATE_STREAM_PACKAGING_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/media_services_t.html#ADSDK-GUID-04D89DCA-FF34-479C-8E08-060608B918BF)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
