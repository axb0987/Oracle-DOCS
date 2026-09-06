# Artifacts Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html
- Fetched: 2026-09-05 19:01 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#dcoc-content-body)

## Artifacts Common Types

### DBMS_CLOUD_OCI_ARTIFACTS_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_ARTIFACTS_CHANGE_CONTAINER_REPOSITORY_COMPARTMENT_DETAILS_T Type

Change container repository compartment details.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which to move the resource.

### DBMS_CLOUD_OCI_ARTIFACTS_CHANGE_REPOSITORY_COMPARTMENT_DETAILS_T Type

Details for changing a repository's compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the repository should be moved.

### DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_CONFIGURATION_T Type

Container configuration.

Syntax
```

```

Fields

Field Description

`is_repository_created_on_first_push`

(required) Whether to create a new container repository when a container is pushed to a new repository path. Repositories created in this way belong to the root compartment.

`namespace`

(required) The tenancy namespace used in the container repository path.

### DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_IMAGE_LAYER_T Type

The container image layer metadata.

Syntax
```

```

Fields

Field Description

`digest`

(required) The sha256 digest of the image layer.

`size_in_bytes`

(required) The size of the layer in bytes.

`time_created`

(required) An RFC 3339 timestamp indicating when the layer was created.

### DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_VERSION_T Type

Container version metadata.

Syntax
```

```

Fields

Field Description

`created_by`

(required) The OCID of the user or principal that pushed the version.

`time_created`

(required) The creation time of the version.

`version`

(required) The version name.

### DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_IMAGE_LAYER_TBL Type

Nested table type of dbms_cloud_oci_artifacts_container_image_layer_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_VERSION_TBL Type

Nested table type of dbms_cloud_oci_artifacts_container_version_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_IMAGE_T Type

Container image metadata.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The compartment OCID to which the container image belongs. Inferred from the container repository.

`created_by`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user or principal that created the resource.

`digest`

(required) The container image digest.

`display_name`

(required) The repository name and the most recent version associated with the image. If there are no versions associated with the image, then last known version and digest are used instead. If the last known version is unavailable, then 'unknown' is used instead of the version. Example: `ubuntu:latest` or `ubuntu:latest@sha256:45b23dee08af5e43a7fea6c4cf9c25ccf269ee113168c19722f87876677c5cb2`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the container image. Example: `ocid1.containerimage.oc1..exampleuniqueID`

`layers`

(required) Layers of which the image is composed, ordered by the layer digest.

`layers_size_in_bytes`

(required) The total size of the container image layers in bytes.

`lifecycle_state`

(required) The current state of the container image.

Allowed values are: 'AVAILABLE', 'DELETED', 'DELETING'

`manifest_size_in_bytes`

(required) The size of the container image manifest in bytes.

`pull_count`

(required) Total number of pulls.

`repository_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the container repository.

`repository_name`

(required) The container repository name.

`time_created`

(required) An RFC 3339 timestamp indicating when the image was created.

`time_last_pulled`

(optional) An RFC 3339 timestamp indicating when the image was last pulled.

`version`

(optional) The most recent version associated with this image.

`versions`

(required) The versions associated with this image.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(required) The system tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_IMAGE_SUMMARY_T Type

Container image summary.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The compartment OCID to which the container image belongs. Inferred from the container repository.

`digest`

(required) The container image digest.

`display_name`

(required) The repository name and the most recent version associated with the image. If there are no versions associated with the image, then last known version and digest are used instead. If the last known version is unavailable, then 'unknown' is used instead of the version. Example: `ubuntu:latest` or `ubuntu:latest@sha256:45b23dee08af5e43a7fea6c4cf9c25ccf269ee113168c19722f87876677c5cb2`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the container image. Example: `ocid1.containerimage.oc1..exampleuniqueID`

`lifecycle_state`

(required) The current state of the container image.

`repository_id`

(required) The OCID of the container repository.

`repository_name`

(required) The container repository name.

`time_created`

(required) An RFC 3339 timestamp indicating when the image was created.

`version`

(optional) The most recent version associated with this image.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(required) The system tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_IMAGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_artifacts_container_image_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_IMAGE_COLLECTION_T Type

List container image results.

Syntax
```

```

Fields

Field Description

`items`

(required) Page of matching container images.

`remaining_items_count`

(required) Estimated number of remaining results.

### DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_IMAGE_SIGNATURE_T Type

Container image signature metadata.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the container repository exists.

`created_by`

(required) The id of the user or principal that created the resource.

`display_name`

(required) The last 10 characters of the kmsKeyId, the last 10 characters of the kmsKeyVersionId, the signingAlgorithm, and the last 10 characters of the signatureId. Example: `wrmz22sixa::qdwyc2ptun::SHA_256_RSA_PKCS_PSS::2vwmobasva`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the container image signature. Example: `ocid1.containerimagesignature.oc1..exampleuniqueID`

`image_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the container image. Example: `ocid1.containerimage.oc1..exampleuniqueID`

`kms_key_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the kmsKeyId used to sign the container image. Example: `ocid1.key.oc1..exampleuniqueID`

`kms_key_version_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the kmsKeyVersionId used to sign the container image. Example: `ocid1.keyversion.oc1..exampleuniqueID`

`message`

(required) The base64 encoded signature payload that was signed.

`signature`

(required) The signature of the message field using the kmsKeyId, the kmsKeyVersionId, and the signingAlgorithm.

`signing_algorithm`

(required) The algorithm to be used for signing. These are the only supported signing algorithms for container images.

Allowed values are: 'SHA_224_RSA_PKCS_PSS', 'SHA_256_RSA_PKCS_PSS', 'SHA_384_RSA_PKCS_PSS', 'SHA_512_RSA_PKCS_PSS'

`time_created`

(required) An RFC 3339 timestamp indicating when the image was created.

`lifecycle_state`

(required) The current state of the container image signature.

Allowed values are: 'AVAILABLE', 'DELETING', 'DELETED'

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(required) The system tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_IMAGE_SIGNATURE_SUMMARY_T Type

Container image signature summary.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment in which the container repository exists.

`display_name`

(required) The last 10 characters of the kmsKeyId, the last 10 characters of the kmsKeyVersionId, the signingAlgorithm, and the last 10 characters of the signatureId. Example: `wrmz22sixa::qdwyc2ptun::SHA_256_RSA_PKCS_PSS::2vwmobasva`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the container image signature. Example: `ocid1.containerimagesignature.oc1..exampleuniqueID`

`image_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the container image. Example: `ocid1.containerimage.oc1..exampleuniqueID`

`kms_key_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the kmsKeyId used to sign the container image. Example: `ocid1.key.oc1..exampleuniqueID`

`kms_key_version_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the kmsKeyVersionId used to sign the container image. Example: `ocid1.keyversion.oc1..exampleuniqueID`

`message`

(required) The base64 encoded signature payload that was signed.

`signature`

(required) The signature of the message field using the kmsKeyId, the kmsKeyVersionId, and the signingAlgorithm.

`signing_algorithm`

(required) The algorithm to be used for signing. These are the only supported signing algorithms for container images.

Allowed values are: 'SHA_224_RSA_PKCS_PSS', 'SHA_256_RSA_PKCS_PSS', 'SHA_384_RSA_PKCS_PSS', 'SHA_512_RSA_PKCS_PSS'

`time_created`

(required) An RFC 3339 timestamp indicating when the image was created.

`lifecycle_state`

(required) The current state of the container image signature.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(required) The system tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_IMAGE_SIGNATURE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_artifacts_container_image_signature_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_IMAGE_SIGNATURE_COLLECTION_T Type

List container image signature results.

Syntax
```

```

Fields

Field Description

`items`

(required) Page of matching container image signatures.

`remaining_items_count`

(required) Estimated number of remaining results.

### DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_REPOSITORY_README_T Type

Container repository readme.

Syntax
```

```

Fields

Field Description

`content`

(required) Readme content. Avoid entering confidential information.

`format`

(required) Readme format. Supported formats are text/plain and text/markdown.

Allowed values are: 'TEXT_MARKDOWN', 'TEXT_PLAIN'

### DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_REPOSITORY_T Type

Container repository metadata.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment in which the container repository exists.

`created_by`

(required) The id of the user or principal that created the resource.

`display_name`

(required) The container repository name.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the container repository. Example: `ocid1.containerrepo.oc1..exampleuniqueID`

`image_count`

(required) Total number of images.

`is_immutable`

(required) Whether the repository is immutable. Images cannot be overwritten in an immutable repository.

`is_public`

(required) Whether the repository is public. A public repository allows unauthenticated access.

`layer_count`

(required) Total number of layers.

`layers_size_in_bytes`

(required) Total storage in bytes consumed by layers.

`lifecycle_state`

(required) The current state of the container repository.

Allowed values are: 'AVAILABLE', 'DELETING', 'DELETED'

`readme`

(optional)

`time_created`

(required) An RFC 3339 timestamp indicating when the repository was created.

`time_last_pushed`

(optional) An RFC 3339 timestamp indicating when an image was last pushed to the repository.

`billable_size_in_g_bs`

(required) Total storage size in GBs that will be charged.

`namespace`

(required) The tenancy namespace used in the container repository path.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(required) The system tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_REPOSITORY_SUMMARY_T Type

Container repository summary.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment in which the container repository exists.

`display_name`

(required) The container repository name.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the container repository. Example: `ocid1.containerrepo.oc1..exampleuniqueID`

`image_count`

(required) Total number of images.

`is_public`

(required) Whether the repository is public. A public repository allows unauthenticated access.

`layer_count`

(required) Total number of layers.

`layers_size_in_bytes`

(required) Total storage in bytes consumed by layers.

`lifecycle_state`

(required) The current state of the container repository.

`time_created`

(required) An RFC 3339 timestamp indicating when the repository was created.

`billable_size_in_g_bs`

(required) Total storage size in GBs that will be charged.

`namespace`

(required) The tenancy namespace used in the container repository path.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(required) The system tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_REPOSITORY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_artifacts_container_repository_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_REPOSITORY_COLLECTION_T Type

List of container repository results.

Syntax
```

```

Fields

Field Description

`layer_count`

(required) Total number of layers.

`layers_size_in_bytes`

(required) Total storage in bytes consumed by layers.

`image_count`

(required) Total number of images.

`items`

(required) Collection of container repositories.

`remaining_items_count`

(required) Estimated number of remaining results.

`repository_count`

(required) Total number of repositories.

### DBMS_CLOUD_OCI_ARTIFACTS_CREATE_CONTAINER_IMAGE_SIGNATURE_DETAILS_T Type

Upload container image signature request details.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the container repository exists.

`image_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the container image. Example: `ocid1.containerimage.oc1..exampleuniqueID`

`kms_key_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the kmsKeyId used to sign the container image. Example: `ocid1.key.oc1..exampleuniqueID`

`kms_key_version_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the kmsKeyVersionId used to sign the container image. Example: `ocid1.keyversion.oc1..exampleuniqueID`

`message`

(required) The base64 encoded signature payload that was signed.

`signature`

(required) The signature of the message field using the kmsKeyId, the kmsKeyVersionId, and the signingAlgorithm.

`signing_algorithm`

(required) The algorithm to be used for signing. These are the only supported signing algorithms for container images.

Allowed values are: 'SHA_224_RSA_PKCS_PSS', 'SHA_256_RSA_PKCS_PSS', 'SHA_384_RSA_PKCS_PSS', 'SHA_512_RSA_PKCS_PSS'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_ARTIFACTS_CREATE_CONTAINER_REPOSITORY_DETAILS_T Type

Create container repository details.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which to create the resource.

`display_name`

(required) The container repository name.

`is_immutable`

(optional) Whether the repository is immutable. Images cannot be overwritten in an immutable repository.

`is_public`

(optional) Whether the repository is public. A public repository allows unauthenticated access.

`readme`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_ARTIFACTS_CREATE_REPOSITORY_DETAILS_T Type

Parameters needed to create an artifact repository.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name for the repository. If not present, will be auto-generated. It can be modified later. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the repository's compartment.

`repository_type`

(required) The repository's supported artifact type.

`description`

(optional) A short description of the repository. It can be updated later.

`is_immutable`

(required) Whether to make the repository immutable. The artifacts of an immutable repository cannot be overwritten.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_ARTIFACTS_CREATE_GENERIC_REPOSITORY_DETAILS_T Type

Parameters needed to create an artifact repository.

Syntax
```

```

`dbms_cloud_oci_artifacts_create_generic_repository_details_t`is a subtype of the`dbms_cloud_oci_artifacts_create_repository_details_t`type.

### DBMS_CLOUD_OCI_ARTIFACTS_ERROR_T Type

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_ARTIFACTS_GENERIC_ARTIFACT_T Type

The metadata of the artifact.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the artifact. Example: `ocid1.genericartifact.oc1..exampleuniqueID`

`display_name`

(required) The artifact name with the format of `&lt;artifact-path&gt;:&lt;artifact-version&gt;`. The artifact name is truncated to a maximum length of 255. Example: `project01/my-web-app/artifact-abc:1.0.0`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the repository's compartment.

`repository_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the repository.

`artifact_path`

(required) A user-defined path to describe the location of an artifact. Slashes do not create a directory structure, but you can use slashes to organize the repository. An artifact path does not include an artifact version. Example: `project01/my-web-app/artifact-abc`

`version`

(required) A user-defined string to describe the artifact version. Example: `1.1.0` or `1.2-beta-2`

`sha256`

(required) The SHA256 digest for the artifact. When you upload an artifact to the repository, a SHA256 digest is calculated and added to the artifact properties.

`size_in_bytes`

(required) The size of the artifact in bytes.

`lifecycle_state`

(required) The current state of the artifact.

Allowed values are: 'AVAILABLE', 'DELETING', 'DELETED'

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`time_created`

(required) An RFC 3339 timestamp indicating when the repository was created.

### DBMS_CLOUD_OCI_ARTIFACTS_GENERIC_ARTIFACT_SUMMARY_T Type

Summary information for an artifact.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the artifact. Example: `ocid1.genericartifact.oc1..exampleuniqueID`

`display_name`

(required) The artifact name with the format of `&lt;artifact-path&gt;:&lt;artifact-version&gt;`. The artifact name is truncated to a maximum length of 255. Example: `project01/my-web-app/artifact-abc:1.0.0`

`compartment_id`

(required) The OCID of the artifact's compartment.

`repository_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the repository.

`artifact_path`

(required) A user-defined path to describe the location of an artifact. Slashes do not create a directory structure, but you can use slashes to organize the repository. An artifact path does not include an artifact version. Example: `project01/my-web-app/artifact-abc`

`version`

(required) A user-defined string to describe the artifact version. Example: `1.1.0` or `1.2-beta-2`

`sha256`

(required) The SHA256 digest for the artifact. When you upload an artifact to the repository, a SHA256 digest is calculated and added to the artifact properties.

`size_in_bytes`

(required) The size of the artifact in bytes.

`lifecycle_state`

(required) The current state of the generic artifact.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`time_created`

(required) An RFC 3339 timestamp indicating when the artifact was created.

### DBMS_CLOUD_OCI_ARTIFACTS_GENERIC_ARTIFACT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_artifacts_generic_artifact_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ARTIFACTS_GENERIC_ARTIFACT_COLLECTION_T Type

A list of artifacts.

Syntax
```

```

Fields

Field Description

`items`

(required) The listed artifacts.

### DBMS_CLOUD_OCI_ARTIFACTS_REPOSITORY_T Type

The metadata for the artifact repository.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the repository. Example: `ocid1.artifactrepository.oc1..exampleuniqueID`

`display_name`

(required) The repository name.

`compartment_id`

(required) The OCID of the repository's compartment.

`repository_type`

(required) The repository's supported artifact type.

Allowed values are: 'GENERIC'

`description`

(required) The repository description.

`is_immutable`

(required) Whether the repository is immutable. The artifacts of an immutable repository cannot be overwritten.

`lifecycle_state`

(required) The current state of the repository.

Allowed values are: 'AVAILABLE', 'DELETING', 'DELETED'

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`time_created`

(required) An RFC 3339 timestamp indicating when the repository was created.

### DBMS_CLOUD_OCI_ARTIFACTS_GENERIC_REPOSITORY_T Type

The metadata for the artifact repository.

Syntax
```

```

`dbms_cloud_oci_artifacts_generic_repository_t`is a subtype of the`dbms_cloud_oci_artifacts_repository_t`type.

### DBMS_CLOUD_OCI_ARTIFACTS_REPOSITORY_SUMMARY_T Type

Summary information for a repository.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the repository. Example: `ocid1.artifactrepository.oc1..exampleuniqueID`

`display_name`

(required) The repository name.

`compartment_id`

(required) The OCID of the repository's compartment.

`repository_type`

(required) The repository's supported artifact type.

`description`

(optional) The repository description.

`is_immutable`

(required) Whether the repository is immutable. The artifacts of an immutable repository cannot be overwritten.

`lifecycle_state`

(required) The current state of the artifact repository.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`time_created`

(required) An RFC 3339 timestamp indicating when the repository was created.

### DBMS_CLOUD_OCI_ARTIFACTS_GENERIC_REPOSITORY_SUMMARY_T Type

Summary information for a repository.

Syntax
```

```

`dbms_cloud_oci_artifacts_generic_repository_summary_t`is a subtype of the`dbms_cloud_oci_artifacts_repository_summary_t`type.

### DBMS_CLOUD_OCI_ARTIFACTS_REMOVE_CONTAINER_VERSION_DETAILS_T Type

Remove version details.

Syntax
```

```

Fields

Field Description

`version`

(required) The version to remove.

### DBMS_CLOUD_OCI_ARTIFACTS_REPOSITORY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_artifacts_repository_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ARTIFACTS_REPOSITORY_COLLECTION_T Type

A list of repositories.

Syntax
```

```

Fields

Field Description

`items`

(required) The listed repositories.

### DBMS_CLOUD_OCI_ARTIFACTS_RESTORE_CONTAINER_IMAGE_DETAILS_T Type

Undelete container image request details.

Syntax
```

```

Fields

Field Description

`version`

(optional) Optional version to associate with image.

### DBMS_CLOUD_OCI_ARTIFACTS_UPDATE_CONTAINER_CONFIGURATION_DETAILS_T Type

Update container configuration request details.

Syntax
```

```

Fields

Field Description

`is_repository_created_on_first_push`

(optional) Whether to create a new container repository when a container is pushed to a new repository path. Repositories created in this way belong to the root compartment.

### DBMS_CLOUD_OCI_ARTIFACTS_UPDATE_CONTAINER_IMAGE_DETAILS_T Type

Details for updating a container image.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_ARTIFACTS_UPDATE_CONTAINER_IMAGE_SIGNATURE_DETAILS_T Type

Details for updating a container image signature.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_ARTIFACTS_UPDATE_CONTAINER_REPOSITORY_DETAILS_T Type

Update container repository request details.

Syntax
```

```

Fields

Field Description

`is_immutable`

(optional) Whether the repository is immutable. Images cannot be overwritten in an immutable repository.

`is_public`

(optional) Whether the repository is public. A public repository allows unauthenticated access.

`readme`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_ARTIFACTS_UPDATE_GENERIC_ARTIFACT_BY_PATH_DETAILS_T Type

Details for updating an artifact by providing its `artifactPath` and `version`.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_ARTIFACTS_UPDATE_GENERIC_ARTIFACT_DETAILS_T Type

Details for updating an artifact by providing its[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_ARTIFACTS_UPDATE_REPOSITORY_DETAILS_T Type

Details for updating a repository.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The repository name.

`repository_type`

(required) The repository's supported artifact type.

`description`

(optional) The repository description.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_ARTIFACTS_UPDATE_GENERIC_REPOSITORY_DETAILS_T Type

Details for updating an artifact repository.

Syntax
```

```

`dbms_cloud_oci_artifacts_update_generic_repository_details_t`is a subtype of the`dbms_cloud_oci_artifacts_update_repository_details_t`type.

- [Artifacts Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-6E77C5C7-6853-42C7-A5E0-48B8B0C4077C)
- [DBMS_CLOUD_OCI_ARTIFACTS_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-E7F75E1E-8EA7-4155-B3E1-AC48C58E7DA2)
- [DBMS_CLOUD_OCI_ARTIFACTS_CHANGE_CONTAINER_REPOSITORY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-5F79A9AC-8645-4712-B77D-4BBDC668E1E2)
- [DBMS_CLOUD_OCI_ARTIFACTS_CHANGE_REPOSITORY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-D28B940D-A4CE-4B6C-A715-7D4E202227D9)
- [DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-632F878B-3271-46E3-9E78-D925652FB052)
- [DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_IMAGE_LAYER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-27672DBE-CE33-4C27-A5BB-DB0A7E471B99)
- [DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_VERSION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-C0A24541-442F-4752-9DE5-4CE58C2A595B)
- [DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_IMAGE_LAYER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-145C82AF-12E7-418B-B187-CF8A779F159E)
- [DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_VERSION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-02FFFEA0-AE98-44D9-95BD-7D6574B69621)
- [DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_IMAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-5DC594D9-E906-414C-8582-B6D5714C3D65)
- [DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_IMAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-7909C0BB-8ED3-430E-96F2-55A27B87CB44)
- [DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_IMAGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-61CCE30C-F55E-46DA-B76A-B5E9ACB945F7)
- [DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_IMAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-36D5F992-FC9E-4332-B337-AAB1331C64A5)
- [DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_IMAGE_SIGNATURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-4EA291C3-3D22-4470-A676-AEC0E08A9CF2)
- [DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_IMAGE_SIGNATURE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-FA7001B6-5EFE-4544-B5D6-5E482DD951B5)
- [DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_IMAGE_SIGNATURE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-7D8ABF54-6C91-4B1D-86F3-472A25CA6E93)
- [DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_IMAGE_SIGNATURE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-13C8165D-4F61-4557-BEC9-753E495BBFA4)
- [DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_REPOSITORY_README_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-357578F6-4702-4EC2-B115-8D4F02ABECBE)
- [DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_REPOSITORY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-1AF54F65-0726-4681-A648-F5266E849421)
- [DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_REPOSITORY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-486A7F9A-007C-4E7D-8DC1-B672901E94E6)
- [DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_REPOSITORY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-C880E761-ED8B-43C1-9EC7-2CF8F97FC813)
- [DBMS_CLOUD_OCI_ARTIFACTS_CONTAINER_REPOSITORY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-0A2FA96A-09BE-4740-BFEE-ED7AFCA44376)
- [DBMS_CLOUD_OCI_ARTIFACTS_CREATE_CONTAINER_IMAGE_SIGNATURE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-54358958-0E26-4E97-85C8-34CEB0C75315)
- [DBMS_CLOUD_OCI_ARTIFACTS_CREATE_CONTAINER_REPOSITORY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-8303ABB4-24CA-4FEF-80F0-2849AEA91984)
- [DBMS_CLOUD_OCI_ARTIFACTS_CREATE_REPOSITORY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-47065E64-F2FA-436F-90C8-0CB526903A8B)
- [DBMS_CLOUD_OCI_ARTIFACTS_CREATE_GENERIC_REPOSITORY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-AAA76DD2-3CFD-4053-98BA-2813636C5D1A)
- [DBMS_CLOUD_OCI_ARTIFACTS_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-778FB6FA-4C8C-448C-A4D6-145773408DD2)
- [DBMS_CLOUD_OCI_ARTIFACTS_GENERIC_ARTIFACT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-C217D4F2-82BF-4B4A-A1A7-8A957178E332)
- [DBMS_CLOUD_OCI_ARTIFACTS_GENERIC_ARTIFACT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-2BEF691C-1EEF-4227-90B5-A4BFB1B9F217)
- [DBMS_CLOUD_OCI_ARTIFACTS_GENERIC_ARTIFACT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-494A8A2C-2D41-4159-9C79-9B9F48218365)
- [DBMS_CLOUD_OCI_ARTIFACTS_GENERIC_ARTIFACT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-A6373AFB-5B5E-44ED-857E-7C39E6837E6A)
- [DBMS_CLOUD_OCI_ARTIFACTS_REPOSITORY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-CA99481F-DB81-4D6D-BC86-A3745FCD8277)
- [DBMS_CLOUD_OCI_ARTIFACTS_GENERIC_REPOSITORY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-F01B3C64-C6AD-4D8E-A3A2-93DA66EE071B)
- [DBMS_CLOUD_OCI_ARTIFACTS_REPOSITORY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-87144550-66B6-41E8-A1EE-4E2F049B8EF3)
- [DBMS_CLOUD_OCI_ARTIFACTS_GENERIC_REPOSITORY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-D3ECAEB5-F044-4C6B-AA27-D3EB09CD6A8E)
- [DBMS_CLOUD_OCI_ARTIFACTS_REMOVE_CONTAINER_VERSION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-2DAAB037-C288-4384-BB5A-E5D2649C3E77)
- [DBMS_CLOUD_OCI_ARTIFACTS_REPOSITORY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-7FBA2364-A21D-41BE-B02C-7B788E1F6000)
- [DBMS_CLOUD_OCI_ARTIFACTS_REPOSITORY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-A5BE84B1-FD77-4B1A-B77B-3FAFD663B276)
- [DBMS_CLOUD_OCI_ARTIFACTS_RESTORE_CONTAINER_IMAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-92A0CDCD-5A9E-4060-834D-8A9D3C6962AD)
- [DBMS_CLOUD_OCI_ARTIFACTS_UPDATE_CONTAINER_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-60D2F733-CD65-4AC9-BF98-7647252F3787)
- [DBMS_CLOUD_OCI_ARTIFACTS_UPDATE_CONTAINER_IMAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-659E91B4-C37E-43DC-837E-B46F34BDC8F5)
- [DBMS_CLOUD_OCI_ARTIFACTS_UPDATE_CONTAINER_IMAGE_SIGNATURE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-BEFBDE40-AB01-4F9F-93FA-CAA0E5375DEE)
- [DBMS_CLOUD_OCI_ARTIFACTS_UPDATE_CONTAINER_REPOSITORY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-FBEAB817-C402-4597-8CFD-8057B2960BDE)
- [DBMS_CLOUD_OCI_ARTIFACTS_UPDATE_GENERIC_ARTIFACT_BY_PATH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-169A6AB0-E761-49BD-9799-B83CE4FE8E26)
- [DBMS_CLOUD_OCI_ARTIFACTS_UPDATE_GENERIC_ARTIFACT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-0A68E529-F411-4545-B08D-64FF6988740B)
- [DBMS_CLOUD_OCI_ARTIFACTS_UPDATE_REPOSITORY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-6A6C023C-3BC8-4C68-8D81-00F66D4495AC)
- [DBMS_CLOUD_OCI_ARTIFACTS_UPDATE_GENERIC_REPOSITORY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/artifacts_t.html#ADSDK-GUID-A1BDE6E4-4249-49F4-BE42-0AB1DEF16B43)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
