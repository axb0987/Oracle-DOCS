# Media Services Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html
- Fetched: 2026-09-05 19:09 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#dcoc-content-body)

## Media Services Functions

Package: DBMS_CLOUD_OCI_MDS_MEDIA_SERVICES

### CHANGE_MEDIA_ASSET_COMPARTMENT Function

Moves a MediaAsset resource from one compartment identifier to another.

Syntax
```

```

Parameters

Parameter Description

`media_asset_id`

(required) Unique MediaAsset identifier

`change_media_asset_compartment_details`

(required) The information to be updated.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_MEDIA_WORKFLOW_COMPARTMENT Function

Moves a MediaWorkflow resource from one compartment identifier to another.

Syntax
```

```

Parameters

Parameter Description

`media_workflow_id`

(required) Unique MediaWorkflow identifier.

`change_media_workflow_compartment_details`

(required) The change compartment payload.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_MEDIA_WORKFLOW_CONFIGURATION_COMPARTMENT Function

Moves a MediaWorkflowConfiguration resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`media_workflow_configuration_id`

(required) Unique MediaWorkflowConfiguration identifier.

`change_media_workflow_configuration_compartment_details`

(required) The information to be updated.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_MEDIA_WORKFLOW_JOB_COMPARTMENT Function

Moves a MediaWorkflowJob resource from one compartment identifier to another.

Syntax
```

```

Parameters

Parameter Description

`media_workflow_job_id`

(required) Unique MediaWorkflowJob identifier.

`change_media_workflow_job_compartment_details`

(required) The change compartment payload.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_STREAM_DISTRIBUTION_CHANNEL_COMPARTMENT Function

Moves a Stream Distribution Channel resource from one compartment identifier to another.

Syntax
```

```

Parameters

Parameter Description

`stream_distribution_channel_id`

(required) Unique Stream Distribution Channel path identifier.

`change_stream_distribution_channel_compartment_details`

(required) The change compartment payload.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MEDIA_ASSET Function

Creates a new MediaAsset.

Syntax
```

```

Parameters

Parameter Description

`create_media_asset_details`

(required) Details for the new MediaAsset.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MEDIA_WORKFLOW Function

Creates a new MediaWorkflow.

Syntax
```

```

Parameters

Parameter Description

`create_media_workflow_details`

(required) Details for the new MediaWorkflow.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MEDIA_WORKFLOW_CONFIGURATION Function

Creates a new MediaWorkflowConfiguration.

Syntax
```

```

Parameters

Parameter Description

`create_media_workflow_configuration_details`

(required) Details for the new MediaWorkflowConfiguration.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MEDIA_WORKFLOW_JOB Function

Run the MediaWorkflow according to the given mediaWorkflow definition and configuration.

Syntax
```

```

Parameters

Parameter Description

`create_media_workflow_job_details`

(required) The information to run the mediaWorkflow.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_STREAM_CDN_CONFIG Function

Creates a new CDN Configuration.

Syntax
```

```

Parameters

Parameter Description

`create_stream_cdn_config_details`

(required) Details for the new StreamCdnConfig.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_STREAM_DISTRIBUTION_CHANNEL Function

Creates a new Stream Distribution Channel.

Syntax
```

```

Parameters

Parameter Description

`create_stream_distribution_channel_details`

(required) Details for the new Stream Distribution Channel.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_STREAM_PACKAGING_CONFIG Function

Creates a new Packaging Configuration.

Syntax
```

```

Parameters

Parameter Description

`create_stream_packaging_config_details`

(required) Details for the new Stream Packaging Configuration.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MEDIA_ASSET Function

Deletes a MediaAsset resource by identifier. If DeleteChildren is passed in as the mode, all the assets with the parentMediaAssetId matching the ID will be deleted. If DeleteDerivatives is set as the mode, all the assets with the masterMediaAssetId matching the ID will be deleted.

Syntax
```

```

Parameters

Parameter Description

`media_asset_id`

(required) Unique MediaAsset identifier

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`delete_mode`

(optional) DeleteMode decides whether to delete all the immediate children or all assets with the asset's ID as their masterMediaAssetId.

Allowed values are: 'DELETE_CHILDREN', 'DELETE_DERIVATIONS'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MEDIA_ASSET_DISTRIBUTION_CHANNEL_ATTACHMENT Function

Deletes a MediaAsset from the DistributionChannel by identifiers.

Syntax
```

```

Parameters

Parameter Description

`media_asset_id`

(required) Unique MediaAsset identifier

`distribution_channel_id`

(required) Unique DistributionChannel identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`version`

(optional) Version of the attachment.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MEDIA_WORKFLOW Function

The MediaWorkflow lifecycleState will change to DELETED.

Syntax
```

```

Parameters

Parameter Description

`media_workflow_id`

(required) Unique MediaWorkflow identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MEDIA_WORKFLOW_CONFIGURATION Function

Deletes a MediaWorkflowConfiguration resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`media_workflow_configuration_id`

(required) Unique MediaWorkflowConfiguration identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MEDIA_WORKFLOW_JOB Function

This is an asynchronous operation. The MediaWorkflowJob lifecycleState will change to CANCELING temporarily until the job is completely CANCELED.

Syntax
```

```

Parameters

Parameter Description

`media_workflow_job_id`

(required) Unique MediaWorkflowJob identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_STREAM_CDN_CONFIG Function

The StreamCdnConfig lifecycleState will change to DELETED.

Syntax
```

```

Parameters

Parameter Description

`stream_cdn_config_id`

(required) Unique StreamCdnConfig identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_STREAM_DISTRIBUTION_CHANNEL Function

The Stream Distribution Channel lifecycleState will change to DELETED.

Syntax
```

```

Parameters

Parameter Description

`stream_distribution_channel_id`

(required) Unique Stream Distribution Channel path identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_STREAM_PACKAGING_CONFIG Function

The Stream Packaging Configuration lifecycleState will change to DELETED.

Syntax
```

```

Parameters

Parameter Description

`stream_packaging_config_id`

(required) Unique Stream Packaging Configuration path identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MEDIA_ASSET Function

Gets a MediaAsset by identifier.

Syntax
```

```

Parameters

Parameter Description

`media_asset_id`

(required) Unique MediaAsset identifier

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MEDIA_ASSET_DISTRIBUTION_CHANNEL_ATTACHMENT Function

Gets a MediaAssetDistributionChannelAttachment for a MediaAsset by identifiers.

Syntax
```

```

Parameters

Parameter Description

`media_asset_id`

(required) Unique MediaAsset identifier

`distribution_channel_id`

(required) Unique DistributionChannel identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`version`

(optional) Version of the attachment.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MEDIA_WORKFLOW Function

Gets a MediaWorkflow by identifier.

Syntax
```

```

Parameters

Parameter Description

`media_workflow_id`

(required) Unique MediaWorkflow identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MEDIA_WORKFLOW_CONFIGURATION Function

Gets a MediaWorkflowConfiguration by identifier

Syntax
```

```

Parameters

Parameter Description

`media_workflow_configuration_id`

(required) Unique MediaWorkflowConfiguration identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MEDIA_WORKFLOW_JOB Function

Gets the MediaWorkflowJob.

Syntax
```

```

Parameters

Parameter Description

`media_workflow_job_id`

(required) Unique MediaWorkflowJob identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MEDIA_WORKFLOW_JOB_FACT Function

Get the MediaWorkflowJobFact identified by the mediaWorkflowJobId and Fact ID.

Syntax
```

```

Parameters

Parameter Description

`media_workflow_job_id`

(required) Unique MediaWorkflowJob identifier.

`key`

(required) Identifier of the MediaWorkflowJobFact within a MediaWorkflowJob.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_STREAM_CDN_CONFIG Function

Gets a StreamCdnConfig by identifier.

Syntax
```

```

Parameters

Parameter Description

`stream_cdn_config_id`

(required) Unique StreamCdnConfig identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_STREAM_DISTRIBUTION_CHANNEL Function

Gets a Stream Distribution Channel by identifier.

Syntax
```

```

Parameters

Parameter Description

`stream_distribution_channel_id`

(required) Unique Stream Distribution Channel path identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_STREAM_PACKAGING_CONFIG Function

Gets a Stream Packaging Configuration by identifier.

Syntax
```

```

Parameters

Parameter Description

`stream_packaging_config_id`

(required) Unique Stream Packaging Configuration path identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### INGEST_STREAM_DISTRIBUTION_CHANNEL Function

Ingests an Asset into a Distribution Channel.

Syntax
```

```

Parameters

Parameter Description

`stream_distribution_channel_id`

(required) Unique Stream Distribution Channel path identifier.

`ingest_stream_distribution_channel_details`

(required) Playlist entry information.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MEDIA_ASSET_DISTRIBUTION_CHANNEL_ATTACHMENTS Function

Lists the MediaAssetDistributionChannelAttachments for a MediaAsset by identifier.

Syntax
```

```

Parameters

Parameter Description

`media_asset_id`

(required) Unique MediaAsset identifier

`display_name`

(optional) A filter to return only the resources that match the entire display name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`opc_request_id`

(optional) The client request ID for tracing.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'mediaAssetId', 'distributionChannelId', 'displayName', 'version'

`distribution_channel_id`

(optional) Unique DistributionChannel identifier.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MEDIA_ASSETS Function

Returns a list of MediaAssetSummary.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The ID of the compartment in which to list resources.

`display_name`

(optional) A filter to return only the resources that match the entire display name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`lifecycle_state`

(optional) A filter to return only the resources with lifecycleState matching the given lifecycleState.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'compartmentId', 'type', 'lifecycleState', 'parentMediaAssetId', 'masterMediaAssetId', 'displayName', 'timeCreated', 'timeUpdated'

`opc_request_id`

(optional) The client request ID for tracing.

`distribution_channel_id`

(optional) Unique DistributionChannel identifier.

`parent_media_asset_id`

(optional) Unique MediaAsset identifier of the asset from which this asset is derived.

`master_media_asset_id`

(optional) Unique MediaAsset identifier of the first asset upload.

`l_type`

(optional) Filter MediaAsset by the asset type.

Allowed values are: 'AUDIO', 'VIDEO', 'PLAYLIST', 'IMAGE', 'CAPTION_FILE', 'UNKNOWN'

`bucket_name`

(optional) Filter MediaAsset by the bucket where the object is stored.

`object_name`

(optional) Filter MediaAsset by the name of the object in object storage.

`media_workflow_job_id`

(optional) The ID of the MediaWorkflowJob used to produce this asset, if this parameter is supplied then the workflow ID must also be supplied.

`source_media_workflow_id`

(optional) The ID of the MediaWorkflow used to produce this asset.

`source_media_workflow_version`

(optional) The version of the MediaWorkflow used to produce this asset.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MEDIA_WORKFLOW_CONFIGURATIONS Function

Returns a list of MediaWorkflowConfigurations.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The ID of the compartment in which to list resources.

`lifecycle_state`

(optional) A filter to return only the resources with lifecycleState matching the given lifecycleState.

`display_name`

(optional) A filter to return only the resources that match the entire display name given.

`id`

(optional) Unique MediaWorkflowConfiguration identifier.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MEDIA_WORKFLOW_JOB_FACTS Function

Internal API to get a point-in-time snapshot of a MediaWorkflowJob.

Syntax
```

```

Parameters

Parameter Description

`media_workflow_job_id`

(required) Unique MediaWorkflowJob identifier.

`key`

(optional) Filter by MediaWorkflowJob ID and MediaWorkflowJobFact key.

`l_type`

(optional) Types of details to include.

Allowed values are: 'runnableJob', 'taskDeclaration', 'workflow', 'configuration', 'parameterResolutionEvent'

`sort_by`

(optional) Types of details to include.

Allowed values are: 'key'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MEDIA_WORKFLOW_JOBS Function

Lists the MediaWorkflowJobs.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The ID of the compartment in which to list resources.

`id`

(optional) unique MediaWorkflowJob identifier

`media_workflow_id`

(optional) Unique MediaWorkflow identifier.

`display_name`

(optional) A filter to return only the resources that match the entire display name given.

`lifecycle_state`

(optional) A filter to return only the resources with lifecycleState matching the given lifecycleState.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The parameter sort by.

Allowed values are: 'timeCreated', 'workflowId', 'lifecycleState'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MEDIA_WORKFLOW_TASK_DECLARATIONS Function

Returns a list of MediaWorkflowTaskDeclarations.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The ID of the compartment in which to list resources.

`name`

(optional) A filter to return only the resources with their system defined, unique name matching the given name.

`version`

(optional) A filter to select MediaWorkflowTaskDeclaration by version.

`is_current`

(optional) A filter to only select the newest version for each MediaWorkflowTaskDeclaration name.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided.

Allowed values are: 'name', 'version'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MEDIA_WORKFLOWS Function

Lists the MediaWorkflows.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The ID of the compartment in which to list resources.

`id`

(optional) Unique MediaWorkflow identifier.

`lifecycle_state`

(optional) A filter to return only the resources with lifecycleState matching the given lifecycleState.

`display_name`

(optional) A filter to return only the resources that match the entire display name given.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_STREAM_CDN_CONFIGS Function

Lists the StreamCdnConfig.

Syntax
```

```

Parameters

Parameter Description

`distribution_channel_id`

(required) The Stream Distribution Channel identifier this CdnConfig belongs to.

`id`

(optional) Unique StreamCdnConfig identifier.

`lifecycle_state`

(optional) A filter to return only the resources with lifecycleState matching the given lifecycleState.

`display_name`

(optional) A filter to return only the resources that match the entire display name given.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_STREAM_DISTRIBUTION_CHANNELS Function

Lists the Stream Distribution Channels.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The ID of the compartment in which to list resources.

`id`

(optional) Unique Stream Distribution Channel identifier.

`lifecycle_state`

(optional) A filter to return only the resources with lifecycleState matching the given lifecycleState.

`display_name`

(optional) A filter to return only the resources that match the entire display name given.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_STREAM_PACKAGING_CONFIGS Function

Lists the Stream Packaging Configurations.

Syntax
```

```

Parameters

Parameter Description

`distribution_channel_id`

(required) Unique Stream Distribution Channel identifier.

`stream_packaging_config_id`

(optional) Unique Stream Packaging Configuration identifier.

`lifecycle_state`

(optional) A filter to return only the resources with lifecycleState matching the given lifecycleState.

`display_name`

(optional) A filter to return only the resources that match the entire display name given.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SYSTEM_MEDIA_WORKFLOWS Function

Lists the SystemMediaWorkflows that can be used to run a job by name or as a template to create a MediaWorkflow.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The ID of the compartment in which to list resources.

`name`

(optional) A filter to return only the resources with their system defined, unique name matching the given name.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MEDIA_ASSET Function

Updates the MediaAsset.

Syntax
```

```

Parameters

Parameter Description

`media_asset_id`

(required) Unique MediaAsset identifier

`update_media_asset_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MEDIA_WORKFLOW Function

Updates the MediaWorkflow.

Syntax
```

```

Parameters

Parameter Description

`media_workflow_id`

(required) Unique MediaWorkflow identifier.

`update_media_workflow_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MEDIA_WORKFLOW_CONFIGURATION Function

Updates the MediaWorkflowConfiguration.

Syntax
```

```

Parameters

Parameter Description

`media_workflow_configuration_id`

(required) Unique MediaWorkflowConfiguration identifier.

`update_media_workflow_configuration_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MEDIA_WORKFLOW_JOB Function

Updates the MediaWorkflowJob.

Syntax
```

```

Parameters

Parameter Description

`media_workflow_job_id`

(required) Unique MediaWorkflowJob identifier.

`update_media_workflow_job_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_STREAM_CDN_CONFIG Function

Updates the StreamCdnConfig.

Syntax
```

```

Parameters

Parameter Description

`stream_cdn_config_id`

(required) Unique StreamCdnConfig identifier.

`update_stream_cdn_config_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_STREAM_DISTRIBUTION_CHANNEL Function

Updates the Stream Distribution Channel.

Syntax
```

```

Parameters

Parameter Description

`stream_distribution_channel_id`

(required) Unique Stream Distribution Channel path identifier.

`update_stream_distribution_channel_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_STREAM_PACKAGING_CONFIG Function

Updates the Stream Packaging Configuration.

Syntax
```

```

Parameters

Parameter Description

`stream_packaging_config_id`

(required) Unique Stream Packaging Configuration path identifier.

`update_stream_packaging_config_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Media Services Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-AD909CBB-9D9C-4763-884E-6A55178239AA)
- [CHANGE_MEDIA_ASSET_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-B0AD6B4E-341B-452E-A585-6B41CC0E9782)
- [CHANGE_MEDIA_WORKFLOW_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-018184EB-9B26-40C7-9BAE-4C723F3C37D9)
- [CHANGE_MEDIA_WORKFLOW_CONFIGURATION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-C5990E71-744E-41AA-9D16-AAE0576472AA)
- [CHANGE_MEDIA_WORKFLOW_JOB_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-E26FC6A9-2FC0-40AE-8A4C-442F68486329)
- [CHANGE_STREAM_DISTRIBUTION_CHANNEL_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-4BC6F1B5-4E80-4ACB-8A16-81E739DD09E4)
- [CREATE_MEDIA_ASSET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-36B151ED-C293-4B7B-8E54-0809AAC3334A)
- [CREATE_MEDIA_WORKFLOW Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-4FFC5C8D-B441-46B8-8B82-9EF0E74059FF)
- [CREATE_MEDIA_WORKFLOW_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-35D3F92E-D90A-4DA0-B90B-E986FA7FCD02)
- [CREATE_MEDIA_WORKFLOW_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-FB5EAC11-6E6B-4BDA-B966-65FB7B38ADC4)
- [CREATE_STREAM_CDN_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-A3EE1D9B-9189-426E-B23B-5E39207C4260)
- [CREATE_STREAM_DISTRIBUTION_CHANNEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-18D57AC4-31B1-417E-9852-1D1203D4D17F)
- [CREATE_STREAM_PACKAGING_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-32BC8B6B-E4EC-4316-9D5E-34D2663C9E30)
- [DELETE_MEDIA_ASSET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-254CD4FC-5B5E-439A-B3CE-9F06E0A4EDC3)
- [DELETE_MEDIA_ASSET_DISTRIBUTION_CHANNEL_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-8B4D41F2-CECB-4A27-926B-C1A66C5C3877)
- [DELETE_MEDIA_WORKFLOW Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-24F22117-AF61-41A3-A28A-CA9E4D2E4526)
- [DELETE_MEDIA_WORKFLOW_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-74F29D65-80C0-4DF1-98A7-454DD20C8B29)
- [DELETE_MEDIA_WORKFLOW_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-6F0C8B73-BF9A-47F8-BD8E-C8828C181A4C)
- [DELETE_STREAM_CDN_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-30469F63-F5F8-47EA-B42A-2FAEF8D12FE6)
- [DELETE_STREAM_DISTRIBUTION_CHANNEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-75229D5F-A968-46EE-A534-546A8E96B93B)
- [DELETE_STREAM_PACKAGING_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-1C0BDDA7-7E37-4E7E-9D44-8925C560E1EB)
- [GET_MEDIA_ASSET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-AE693AD8-4B51-4F65-AA51-51FE166BC795)
- [GET_MEDIA_ASSET_DISTRIBUTION_CHANNEL_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-88ACA0A0-6CB4-464D-B3A7-12A2FEEFF505)
- [GET_MEDIA_WORKFLOW Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-AA6942B7-D549-480C-8776-40F7B2EC8F60)
- [GET_MEDIA_WORKFLOW_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-A52EA2A3-C6D5-40FD-B8EC-1B0FE34D2689)
- [GET_MEDIA_WORKFLOW_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-80819727-0BFB-4884-9EA0-22BDA48FD6FF)
- [GET_MEDIA_WORKFLOW_JOB_FACT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-E7EEA84A-CDCD-4968-9AE1-E5C23637FE50)
- [GET_STREAM_CDN_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-C47B1A13-5305-4AC1-8411-184498255176)
- [GET_STREAM_DISTRIBUTION_CHANNEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-628A67FF-98AA-4884-B45B-6B98E250DFB4)
- [GET_STREAM_PACKAGING_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-25CBB93E-A55F-4196-BF06-CE4CD0F82A3D)
- [INGEST_STREAM_DISTRIBUTION_CHANNEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-96E2AEF8-87D0-4FC7-8014-FBA5EBDDF5B6)
- [LIST_MEDIA_ASSET_DISTRIBUTION_CHANNEL_ATTACHMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-536143D3-970A-4CC0-B7D0-D3DC6B6A8A1E)
- [LIST_MEDIA_ASSETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-432AB798-46F8-4FA9-8EBA-9EC683A3700A)
- [LIST_MEDIA_WORKFLOW_CONFIGURATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-8C7F3E01-1B4E-4678-A51E-5F361740D8A9)
- [LIST_MEDIA_WORKFLOW_JOB_FACTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-D9B8A0D0-F821-4F6D-AB82-A426AF45C800)
- [LIST_MEDIA_WORKFLOW_JOBS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-F8638879-1D15-471A-B35A-BECAA859813E)
- [LIST_MEDIA_WORKFLOW_TASK_DECLARATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-879DAB70-954E-4652-ABCC-00CDFA2A822E)
- [LIST_MEDIA_WORKFLOWS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-51E4067E-5B0C-4C6E-90C8-8F17A98914C3)
- [LIST_STREAM_CDN_CONFIGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-D45DD20C-2838-404A-9C2D-42DECA2001F5)
- [LIST_STREAM_DISTRIBUTION_CHANNELS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-DDA65082-6242-47B9-AF8B-F7AB6878389F)
- [LIST_STREAM_PACKAGING_CONFIGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-59EC3679-40EF-4EFE-87F6-B144E2FFBC0B)
- [LIST_SYSTEM_MEDIA_WORKFLOWS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-10A9893A-30E5-4536-99DE-CB49C393BAD2)
- [UPDATE_MEDIA_ASSET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-3352DAD8-2121-4CDE-A382-CD662AC66F13)
- [UPDATE_MEDIA_WORKFLOW Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-4570CF12-9722-4E23-A7AF-F2681A53FA06)
- [UPDATE_MEDIA_WORKFLOW_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-3505CE2D-A537-4FA2-9988-D0FFF0CE14E9)
- [UPDATE_MEDIA_WORKFLOW_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-D6B84020-E7C0-4B1E-B03C-FE6B3A19AFEE)
- [UPDATE_STREAM_CDN_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-7C482E02-68AD-4BD7-BF78-F343A19B69EA)
- [UPDATE_STREAM_DISTRIBUTION_CHANNEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-711F910C-65CA-47DA-89EF-1A897C139B6E)
- [UPDATE_STREAM_PACKAGING_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_services.html#ADSDK-GUID-E87AC34C-3A59-42BC-A2CE-77E8E7F1AAE7)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
