# Marketplace Publisher Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html
- Fetched: 2026-09-05 19:09 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#dcoc-content-body)

## Marketplace Publisher Functions

Package: DBMS_CLOUD_OCI_MPP_MARKETPLACE_PUBLISHER

### ACTIVATE_TERM_VERSION Function

Mark the Term Version identified by the id as active

Syntax
```

```

Parameters

Parameter Description

`term_version_id`

(required) term version OCID

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CANCEL_WORK_REQUEST Function

Cancels the work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CASCADING_DELETE_LISTING Function

Cascade delete the listing and its subresources.

Syntax
```

```

Parameters

Parameter Description

`listing_id`

(required) listing OCID

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CASCADING_DELETE_LISTING_REVISION Function

Cascade delete listing revision and its subresources.

Syntax
```

```

Parameters

Parameter Description

`listing_revision_id`

(required) listing revision

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_ARTIFACT_COMPARTMENT Function

Moves the specified artifact to the specified compartment within the same tenancy.

Syntax
```

```

Parameters

Parameter Description

`artifact_id`

(required) artifact OCID

`change_artifact_compartment_details`

(required) Request to change the compartment of a given artifact.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_LISTING_COMPARTMENT Function

Moves a listing from one compartment to another

Syntax
```

```

Parameters

Parameter Description

`listing_id`

(required) listing OCID

`change_listing_compartment_details`

(required) Request to change the compartment of a given listing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_LISTING_REVISION_TO_NEW_STATUS Function

Updates the Listing Revision to New status

Syntax
```

```

Parameters

Parameter Description

`listing_revision_id`

(required) listing revision

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_TERM_COMPARTMENT Function

Moves a term from one compartment to another

Syntax
```

```

Parameters

Parameter Description

`term_id`

(required) term OCID

`change_term_compartment_details`

(required) Request to change the compartment of a given term.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CLONE_LISTING_REVISION Function

Clone the published/withdrawn Listing Revision identified by the identifier.

Syntax
```

```

Parameters

Parameter Description

`listing_revision_id`

(required) listing revision

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ARTIFACT Function

Creates a new artifact in your compartment. You must specify your compartment ID in the request object. You must also specify a *name* for the artifact(although it can be an empty string). It does not have to be unique, and you can change it anytime with`UPDATE_ARTIFACT`Function.. You must also specify a *artifactType* for the artifact. Allowed values are CONTAINER_IMAGE and HELM_CHART You must also provide the container or helm chart registry details for the corresponding images. Oracle container registry details (Registry/Concepts/registryoverview.htm). After you send your request, the new object's `status` will temporarily be IN_PROGRESS and `lifecycleState` will be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE and the status has changed to ‘AVAILABLE’ for the new Artifact.

Syntax
```

```

Parameters

Parameter Description

`create_artifact_details`

(required) Request object for creating a new artifact.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_LISTING Function

Creates a new listing in your compartment. You must specify your compartment ID in the request object. You must also specify a *name* for the listing and cannot be updated later. You must also specify a *packageType* for the listing. Allowed values are CONTAINER_IMAGE and HELM_CHART After you send your request, the new object's `lifecycleState` will be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE.

Syntax
```

```

Parameters

Parameter Description

`create_listing_details`

(required) Details for the new Listing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_LISTING_REVISION Function

Creates a new Listing Revision.

Syntax
```

```

Parameters

Parameter Description

`create_listing_revision_details`

(required) Details for the new Listing Revision.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_LISTING_REVISION_ATTACHMENT Function

Creates a new listing revision attachment.

Syntax
```

```

Parameters

Parameter Description

`create_listing_revision_attachment_details`

(required) Details for the new Listing Revision Attachment.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_LISTING_REVISION_NOTE Function

Creates a new Listing Revision Note.

Syntax
```

```

Parameters

Parameter Description

`create_listing_revision_note_details`

(required) Details for the new Listing Revision Note.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_LISTING_REVISION_PACKAGE Function

Creates a new Listing Revision Package.

Syntax
```

```

Parameters

Parameter Description

`create_listing_revision_package_details`

(required) Details for the new Listing Revision Package.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_TERM Function

Creates a new Term.

Syntax
```

```

Parameters

Parameter Description

`create_term_details`

(required) Details for the new Term.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_TERM_VERSION Function

Creates a new Term Version.

Syntax
```

```

Parameters

Parameter Description

`create_term_version_content`

(required) The term version file to upload.

`term_id`

(required) Unique OCID identifier for the term.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`display_name`

(optional) The name of the resource.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ARTIFACT Function

Deletes the specified artifact.

Syntax
```

```

Parameters

Parameter Description

`artifact_id`

(required) artifact OCID

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_LISTING Function

Deletes a listing by the identifier

Syntax
```

```

Parameters

Parameter Description

`listing_id`

(required) listing OCID

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_LISTING_REVISION Function

Deletes a listing by the identifier

Syntax
```

```

Parameters

Parameter Description

`listing_revision_id`

(required) listing revision

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_LISTING_REVISION_ATTACHMENT Function

Deletes a listing revision attachment by the identifier

Syntax
```

```

Parameters

Parameter Description

`listing_revision_attachment_id`

(required) attachment OCID

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_LISTING_REVISION_NOTE Function

Deletes a listing revision note by the identifier.

Syntax
```

```

Parameters

Parameter Description

`listing_revision_note_id`

(required) Unique listing revision note identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_LISTING_REVISION_PACKAGE Function

Deletes a listing revision package by the identifier

Syntax
```

```

Parameters

Parameter Description

`listing_revision_package_id`

(required) Unique listing revision package identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_TERM Function

Deletes a Term by the identifier

Syntax
```

```

Parameters

Parameter Description

`term_id`

(required) term OCID

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_TERM_VERSION Function

Deletes a Term by the identifier

Syntax
```

```

Parameters

Parameter Description

`term_version_id`

(required) term version OCID

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ARTIFACT Function

Gets the specified artifact's information.

Syntax
```

```

Parameters

Parameter Description

`artifact_id`

(required) artifact OCID

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CATEGORY Function

Gets the specified category's information.

Syntax
```

```

Parameters

Parameter Description

`category_code`

(required) Category Code

`compartment_id`

(required) The ID of the compartment in which to list resources.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_LISTING Function

Gets the details for a listing.

Syntax
```

```

Parameters

Parameter Description

`listing_id`

(required) listing OCID

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_LISTING_REVISION Function

Gets the details for a listing revision.

Syntax
```

```

Parameters

Parameter Description

`listing_revision_id`

(required) listing revision

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_LISTING_REVISION_ATTACHMENT Function

Get the details of the specified listing revision attachment.

Syntax
```

```

Parameters

Parameter Description

`listing_revision_attachment_id`

(required) attachment OCID

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_LISTING_REVISION_NOTE Function

Get note details by the identifier

Syntax
```

```

Parameters

Parameter Description

`listing_revision_note_id`

(required) Unique listing revision note identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_LISTING_REVISION_PACKAGE Function

Get the details of the specified version of a package.

Syntax
```

```

Parameters

Parameter Description

`listing_revision_package_id`

(required) Unique listing revision package identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MARKET Function

Gets the specified market's information.

Syntax
```

```

Parameters

Parameter Description

`market_code`

(required) Market Code

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PRODUCT Function

Gets a Product by code identifier

Syntax
```

```

Parameters

Parameter Description

`product_code`

(required) Product Code

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PUBLISHER Function

Gets a Publisher by identifier

Syntax
```

```

Parameters

Parameter Description

`publisher_id`

(required) Publisher OCID

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TERM Function

Gets a Term by identifier

Syntax
```

```

Parameters

Parameter Description

`term_id`

(required) term OCID

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TERM_VERSION Function

Gets a Term Version by the identifier

Syntax
```

```

Parameters

Parameter Description

`term_version_id`

(required) term version OCID

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets details of the work request with the given ID.

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

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ARTIFACTS Function

Lists the artifacts in your compartment. You must specify your compartment's OCID as the value for the compartment ID. For information about OCIDs, see Resource Identifiers (Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`lifecycle_state`

(optional) A filter to return only artifacts with their lifecycleState matches the given lifecycleState.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`status`

(optional) A filter to return only artifacts with specific status.

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

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CATEGORIES Function

Lists the categories in your compartment. You must specify your compartment's OCID as the value for the compartment ID. For information about OCIDs, see Resource Identifiers (Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`product_code`

(optional) product code to filter

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`name`

(optional) A filter to return only resources that match the entire name given.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_LISTING_REVISION_ATTACHMENTS Function

Gets the list of attachments for a listing revision in a compartment

Syntax
```

```

Parameters

Parameter Description

`listing_revision_id`

(required) OCID of the listing revision.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`lifecycle_state`

(optional) A filter to return only attachments their lifecycleState matches the given lifecycleState.

`compartment_id`

(optional) The unique identifier for the compartment.

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

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_LISTING_REVISION_NOTES Function

Gets the list of notes for a listing revision.

Syntax
```

```

Parameters

Parameter Description

`listing_revision_id`

(required) OCID of the listing revision.

`compartment_id`

(optional) The unique identifier for the compartment.

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

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_LISTING_REVISION_PACKAGES Function

Gets the list of packages for a listing revision.

Syntax
```

```

Parameters

Parameter Description

`listing_revision_id`

(required) OCID of the listing revision.

`compartment_id`

(optional) The unique identifier for the compartment.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`lifecycle_state`

(optional) A filter to return only packages their lifecycleState matches the given lifecycleState.

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

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_LISTING_REVISIONS Function

Lists the list of listing revisions for a specific listing ID, compartment ID or listing revision status. You can specify your compartment's OCID as the value for the compartment ID. For information about OCIDs, see Resource Identifiers (Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`listing_id`

(required) listing OCID

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`lifecycle_state`

(optional) A filter to return only listing revisions their lifecycleState matches the given lifecycleState.

`compartment_id`

(optional) The unique identifier for the compartment.

`listing_revision_status`

(optional) A filter to return only listing revisions their status matches the given listing revision status.

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

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_LISTINGS Function

Lists the listings in your compartment. You must specify your compartment's OCID as the value for the compartment ID. For information about OCIDs, see Resource Identifiers (Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`lifecycle_state`

(optional) A filter to return only listings their lifecycleState matches the given lifecycleState.

`name`

(optional) A filter to return only resources that match the entire name given.

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

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MARKETS Function

Lists the markets in your compartment. You must specify your compartment's OCID as the value for the compartment ID. For information about OCIDs, see Resource Identifiers (Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

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

`name`

(optional) A filter to return only resources that match the entire name given.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PRODUCTS Function

Lists the products in your compartment. You must specify your compartment's OCID as the value for the compartment ID. For information about OCIDs, see Resource Identifiers (Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

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

`name`

(optional) A filter to return only resources that match the entire name given.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PUBLISHERS Function

Returns a list of publishers.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

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

`name`

(optional) A filter to return only resources that match the entire name given.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TERM_VERSIONS Function

Returns a list of the publisher term versions.

Syntax
```

```

Parameters

Parameter Description

`term_id`

(required) term OCID

`compartment_id`

(optional) The unique identifier for the compartment.

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

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TERMS Function

Returns a list of the publisher terms.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

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

`name`

(optional) A filter to return only resources that match the entire name given.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Returns a (paginated) list of errors for the work request with the given ID.

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

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timestamp is descending.

Allowed values are: 'timestamp'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Returns a (paginated) list of logs for the work request with the given ID.

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

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timestamp is descending.

Allowed values are: 'timestamp'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

`status`

(optional) A filter to return only resources their lifecycleState matches the given OperationStatus.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'NEEDS_ATTENTION', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`resource_id`

(optional) The ID of the resource affected by the work request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### MARK_LISTING_REVISION_PACKAGE_AS_DEFAULT Function

Mark the Listing Revision Package identified by the id and package version as default

Syntax
```

```

Parameters

Parameter Description

`listing_revision_package_id`

(required) Unique listing revision package identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PUBLISH_LISTING_REVISION Function

Publish the Listing revision identified by Identifier.

Syntax
```

```

Parameters

Parameter Description

`listing_revision_id`

(required) listing revision

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PUBLISH_LISTING_REVISION_AS_PRIVATE Function

Updates the Listing Revision to PublishAsPrivate

Syntax
```

```

Parameters

Parameter Description

`publish_listing_revision_as_private_details`

(required) The listing revision publish as private information to be updated.

`listing_revision_id`

(required) listing revision

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PUBLISH_LISTING_REVISION_PACKAGE Function

Updates the Listing Revision Package to publish status

Syntax
```

```

Parameters

Parameter Description

`listing_revision_package_id`

(required) Unique listing revision package identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUBMIT_LISTING_REVISION_FOR_REVIEW Function

Update the Listing Revision identified by the id for review

Syntax
```

```

Parameters

Parameter Description

`submit_listing_revision_for_review_details`

(required) The listing revision review information to be updated.

`listing_revision_id`

(required) listing revision

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UN_PUBLISH_LISTING_REVISION_PACKAGE Function

Updates the Listing Revision Package to Unpublish status

Syntax
```

```

Parameters

Parameter Description

`listing_revision_package_id`

(required) Unique listing revision package identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ARTIFACT Function

Updates the specified artifact identified by the id.

Syntax
```

```

Parameters

Parameter Description

`artifact_id`

(required) artifact OCID

`update_artifact_details`

(required) Request object for updating an artifact.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_LISTING Function

Updates the specified Listing identified by the id.

Syntax
```

```

Parameters

Parameter Description

`listing_id`

(required) listing OCID

`update_listing_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_LISTING_REVISION Function

Updates the Listing Revision

Syntax
```

```

Parameters

Parameter Description

`listing_revision_id`

(required) listing revision

`update_listing_revision_details`

(required) The listing revision information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_LISTING_REVISION_ATTACHMENT Function

Updates the Listing Revision Attachment

Syntax
```

```

Parameters

Parameter Description

`listing_revision_attachment_id`

(required) attachment OCID

`update_listing_revision_attachment_details`

(required) The attachment to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_LISTING_REVISION_ATTACHMENT_CONTENT Function

Update a file to listing revision attachment

Syntax
```

```

Parameters

Parameter Description

`listing_revision_attachment_id`

(required) attachment OCID

`update_listing_revision_attachment_content`

(required) The attachment to upload.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_LISTING_REVISION_ICON_CONTENT Function

Updates the Listing Revision

Syntax
```

```

Parameters

Parameter Description

`listing_revision_id`

(required) listing revision

`update_listing_revision_icon_content`

(required) The listing revision icon to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_LISTING_REVISION_PACKAGE Function

Updates the Listing Revision Package.

Syntax
```

```

Parameters

Parameter Description

`listing_revision_package_id`

(required) Unique listing revision package identifier.

`update_listing_revision_package_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TERM Function

Updates the Term

Syntax
```

```

Parameters

Parameter Description

`term_id`

(required) term OCID

`update_term_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TERM_VERSION Function

Updates the Term Version

Syntax
```

```

Parameters

Parameter Description

`term_version_id`

(required) term version OCID

`update_term_version_details`

(required) Term Version details to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TERM_VERSION_CONTENT Function

Updates the Term Version attachment

Syntax
```

```

Parameters

Parameter Description

`term_version_id`

(required) term version OCID

`update_term_version_content`

(required) The term attachment to upload.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`display_name`

(optional) The name of the resource.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### VALIDATE_AND_PUBLISH_ARTIFACT Function

Validate and publish artifact.

Syntax
```

```

Parameters

Parameter Description

`artifact_id`

(required) artifact OCID

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### WITHDRAW_LISTING_REVISION Function

Update the Listing Revision identified by the id as Withdraw/UnPublished.

Syntax
```

```

Parameters

Parameter Description

`listing_revision_id`

(required) listing revision

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace-publisher.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Marketplace Publisher Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-462FE070-4942-419B-8866-1F832FC37A68)
- [ACTIVATE_TERM_VERSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-E9563B5A-9286-48E0-BC6F-32B7DA333053)
- [CANCEL_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-B306C26D-69B9-4E1B-A91F-14676E1C7EB3)
- [CASCADING_DELETE_LISTING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-B268CFC8-6CBB-436A-8752-D84B0ADF1F42)
- [CASCADING_DELETE_LISTING_REVISION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-7FEA2B93-BE0B-4B3E-9D7F-2D082A24A50A)
- [CHANGE_ARTIFACT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-A571569A-A9C5-40DE-A343-26D5A3837ECB)
- [CHANGE_LISTING_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-209F9C7A-E48D-440E-84AD-CCE83175E5AD)
- [CHANGE_LISTING_REVISION_TO_NEW_STATUS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-1490F6D5-F7AA-4F83-81D1-2238BB9715F4)
- [CHANGE_TERM_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-BF78B7C5-0C4C-4E98-A491-113274086D52)
- [CLONE_LISTING_REVISION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-1084818C-0637-45FD-90B0-0F9032948F55)
- [CREATE_ARTIFACT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-4FD6B633-DCC8-4399-9A90-65268CA856F2)
- [CREATE_LISTING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-B8AF6D72-729D-4884-AE0A-9C25AAE40233)
- [CREATE_LISTING_REVISION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-AFED863E-B3CB-4EB2-B89F-AD954622A541)
- [CREATE_LISTING_REVISION_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-0BAD2E6A-35CF-480F-BF9B-B93C7A080AA9)
- [CREATE_LISTING_REVISION_NOTE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-347C8748-B670-45A5-935F-4E21A7C9BBB1)
- [CREATE_LISTING_REVISION_PACKAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-5A8E65A6-53E7-4055-81EA-CD4F8B47E7B9)
- [CREATE_TERM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-F021AACB-B744-4EDA-A492-4021305636E3)
- [CREATE_TERM_VERSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-1A6DBE8D-6A86-4F9C-AB94-04D62B3A21D9)
- [DELETE_ARTIFACT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-A6AFC948-FDEE-4390-9E23-90D422731CB9)
- [DELETE_LISTING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-3E60C268-7630-4C47-BAE5-4760D77E22D3)
- [DELETE_LISTING_REVISION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-B162D0DA-DF43-45CF-B55B-6858B4A2B2E6)
- [DELETE_LISTING_REVISION_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-57B0C18B-DBE7-4F56-8803-E6FEA8BAF6E0)
- [DELETE_LISTING_REVISION_NOTE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-B6F701CB-94F7-4672-A45A-4BD310D217C7)
- [DELETE_LISTING_REVISION_PACKAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-DF37A56A-B657-444B-80EC-D4D419E541EF)
- [DELETE_TERM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-F4988C37-472C-4FAD-9CE2-7C1BB8ED1298)
- [DELETE_TERM_VERSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-30B6715B-B073-4B6A-B16D-32A8841DB67A)
- [GET_ARTIFACT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-F919E959-166B-428A-9245-7B35BD6B2692)
- [GET_CATEGORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-586C84FE-B527-4DD0-9A1E-E5C49B59EA53)
- [GET_LISTING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-E481DE25-ED78-4FF5-8FEA-1153BCF1FB1B)
- [GET_LISTING_REVISION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-150612E1-F94D-488B-A8FA-FFBBD055FE13)
- [GET_LISTING_REVISION_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-596DB681-4EAD-450B-A795-A2C6D5BCC076)
- [GET_LISTING_REVISION_NOTE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-99E807EA-DBD3-4974-B082-9D1CAEC1AB2A)
- [GET_LISTING_REVISION_PACKAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-870C8556-E326-46F3-9FF9-7A04352B6FA5)
- [GET_MARKET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-4F045CD8-5C06-4E82-B2EA-613185B3F67C)
- [GET_PRODUCT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-53024667-7935-4EC1-A442-40123FDCAC51)
- [GET_PUBLISHER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-580F1C72-A9E9-49D8-B8FA-2FE3B8045EDB)
- [GET_TERM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-32EE9884-AAC7-4B0C-8A02-FE49540E19AB)
- [GET_TERM_VERSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-43A83980-8D6D-43E8-8925-CEFFFE6BAC3B)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-0BCCBC6F-00AE-4BD9-B175-BCB6AE096957)
- [LIST_ARTIFACTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-8732CEB2-4232-454C-9A62-B7FCD5324F96)
- [LIST_CATEGORIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-BE4034E7-407F-44C3-AF39-740B34B03B90)
- [LIST_LISTING_REVISION_ATTACHMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-3F688A2D-5C33-4D71-BEA7-2C943D62101D)
- [LIST_LISTING_REVISION_NOTES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-91A31744-677A-463A-9A0B-91088B59D64B)
- [LIST_LISTING_REVISION_PACKAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-4BA2278E-CC40-49B4-9050-05487239D77E)
- [LIST_LISTING_REVISIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-64D65ADF-AA50-4633-B3D1-88562CE586CC)
- [LIST_LISTINGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-87253D28-4E87-4565-AE46-E76C68843146)
- [LIST_MARKETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-EDED9583-3B23-406E-BD95-195284872DA0)
- [LIST_PRODUCTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-E608E474-0DB7-4289-A694-D64326CC0212)
- [LIST_PUBLISHERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-493B6630-8144-43F5-98E9-812D7F71A67A)
- [LIST_TERM_VERSIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-A51F8EE0-36D9-468B-B626-91003B04FE2E)
- [LIST_TERMS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-B6D32231-5383-42CF-B359-A4679C60C003)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-13ADABE9-A986-4594-9666-0032004D09AE)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-69045228-B49D-4822-9D51-DE65F091C0D6)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-9E155926-0233-4F2B-9641-F60D79603456)
- [MARK_LISTING_REVISION_PACKAGE_AS_DEFAULT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-194DE7CE-D270-463E-96C7-4D344F9528E1)
- [PUBLISH_LISTING_REVISION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-C58BB4EA-757F-481A-8831-A83907AAAED3)
- [PUBLISH_LISTING_REVISION_AS_PRIVATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-C31D7476-3641-4C2A-BB0B-DBD475882247)
- [PUBLISH_LISTING_REVISION_PACKAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-4098B6DE-2D40-4608-A058-27544C5FC0D4)
- [SUBMIT_LISTING_REVISION_FOR_REVIEW Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-3CDC47AD-2DFE-43BC-B991-ABF07D4E32B8)
- [UN_PUBLISH_LISTING_REVISION_PACKAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-0AEBE9A1-FDF6-4895-8B07-057C53701529)
- [UPDATE_ARTIFACT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-81097C00-C20D-463A-B9EE-002BDE06DD30)
- [UPDATE_LISTING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-CDB2ED93-2028-47C9-AC10-F09590924A15)
- [UPDATE_LISTING_REVISION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-7505670A-6F0D-4EAB-9954-F8043B1CB0F5)
- [UPDATE_LISTING_REVISION_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-0494E92E-B087-45E0-8A87-8A81D7E23A68)
- [UPDATE_LISTING_REVISION_ATTACHMENT_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-6706AB49-095E-4B87-99BD-E8ADBE29DFBD)
- [UPDATE_LISTING_REVISION_ICON_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-DD046735-AED7-40AE-823B-93EFD2280C4B)
- [UPDATE_LISTING_REVISION_PACKAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-C96694CB-DF49-4C9D-88C9-6D242155FF3D)
- [UPDATE_TERM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-A3F575E5-DFD1-44C7-86F1-70BACCA33936)
- [UPDATE_TERM_VERSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-AC4F6A97-F2A0-4012-8E19-B6EF8D7986B4)
- [UPDATE_TERM_VERSION_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-E79F1F96-B5DD-4826-95F8-B02CD295FCC2)
- [VALIDATE_AND_PUBLISH_ARTIFACT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-246E29C9-B288-4B38-8C0C-68E1173F12C0)
- [WITHDRAW_LISTING_REVISION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mpp_marketplace_publisher.html#ADSDK-GUID-D0ECE5FE-484B-4220-B14C-1F4B7611FE97)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
