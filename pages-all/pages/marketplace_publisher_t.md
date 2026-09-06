# Marketplace Publisher Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html
- Fetched: 2026-09-05 19:17 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#dcoc-content-body)

## Marketplace Publisher Common Types

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_ARTIFACT_T Type

Base model object for the artifacts.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique OCID identifier for the artifact.

`display_name`

(required) A display name for the artifact.

`artifact_type`

(required) Artifact type for the artifact.

Allowed values are: 'CONTAINER_IMAGE', 'HELM_CHART'

`status`

(required) The current status for the Artifact.

Allowed values are: 'IN_PROGRESS', 'AVAILABLE', 'UNAVAILABLE'

`status_notes`

(optional) Status notes for the Artifact.

`lifecycle_state`

(required) The current state for the Artifact.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(required) The date and time the artifact was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2022-09-15T21:10:29.600Z`

`compartment_id`

(required) The unique identifier for the compartment.

`publisher_id`

(required) The unique identifier for the publisher.

`time_updated`

(required) The date and time the artifact was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2022-09-15T21:10:29.600Z`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_ARTIFACT_SUMMARY_T Type

The model for the artifact summary.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier for the artifact.

`compartment_id`

(required) The unique identifier for the compartment.

`display_name`

(required) The display name for the artifact.

`artifact_type`

(required) Artifact Type for the artifact.

Allowed values are: 'CONTAINER_IMAGE', 'HELM_CHART'

`lifecycle_state`

(required) The current state for the Artifact.

`status`

(required) The current status for the Artifact.

`time_created`

(required) The date and time the artifact was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2023-03-27T21:10:29.600Z`

`time_updated`

(required) The date and time the artifact was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2023-03-27T21:10:29.600Z`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_ARTIFACT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_marketplace_publisher_artifact_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_ARTIFACT_COLLECTION_T Type

Results of the artifact search. Contains the artifact items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of artifact summary.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CATEGORY_T Type

The model for the category details.

Syntax
```

```

Fields

Field Description

`name`

(required) The name for the category.

`code`

(required) The code of the category.

`product_code`

(required) The product that the category belongs to.

`lifecycle_state`

(required) The current state for the category.

Allowed values are: 'ACTIVE', 'INACTIVE'

`time_created`

(required) The date and time the category was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2022-09-15T21:10:29.600Z`

`time_updated`

(required) The date and time the category was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2022-09-15T21:10:29.600Z`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CATEGORY_SUMMARY_T Type

The model for the category summary.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the category.

`code`

(required) The code of the category.

`product_code`

(required) The product that the category belongs.

`lifecycle_state`

(required) The current state of the category.

`time_created`

(required) The date and time the category was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2022-09-15T21:10:29.600Z`

`time_updated`

(required) The date and time the category was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2022-09-15T21:10:29.600Z`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CATEGORY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_marketplace_publisher_category_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CATEGORY_COLLECTION_T Type

Results of a category search. Contains the category items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of category summary.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CHANGE_ARTIFACT_COMPARTMENT_DETAILS_T Type

Contains details indicating which compartment the artifact should move to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The unique identifier of the compartment for the artifact.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CHANGE_LISTING_COMPARTMENT_DETAILS_T Type

Contains details indicating which compartment the listing should move to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The id of the compartment which the listing should be moved.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CHANGE_TERM_COMPARTMENT_DETAILS_T Type

Contains details indicating which compartment the term should move to

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The id of the compartment which the term should be moved.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CONTAINER_IMAGE_DETAILS_T Type

Container Image details.

Syntax
```

```

Fields

Field Description

`source_registry_id`

(optional) The source registry OCID of the container image.

`source_registry_url`

(required) The source registry url of the container image.

`validation_status`

(required) image validation status

Allowed values are: 'VALIDATION_IN_PROGRESS', 'VALIDATION_FAILED', 'VALIDATION_COMPLETED'

`validation_error`

(optional) image validation failure errors

`publication_status`

(required) image publication status

Allowed values are: 'PUBLICATION_IN_PROGRESS', 'PUBLICATION_COMPLETED', 'PUBLICATION_FAILED'

`publication_error`

(optional) image publication failure errors

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CONTAINER_IMAGE_ARTIFACT_T Type

Container Image artifact details.

Syntax
```

```

`dbms_cloud_oci_marketplace_publisher_container_image_artifact_t`is a subtype of the`dbms_cloud_oci_marketplace_publisher_artifact_t`type.

Fields

Field Description

`container_image`

(required)

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_PACKAGE_T Type

A base object for all types of listing revision packages.

Syntax
```

```

Fields

Field Description

`id`

(optional) The OCID for the listing revision package in Marketplace Publisher.

`display_name`

(required) The name of the listing revision package.

`description`

(optional) The description of this package.

`listing_revision_id`

(required) The unique identifier for the listing revision.

`compartment_id`

(required) The unique identifier for the compartment.

`artifact_id`

(required) The unique identifier for the artifact.

`term_id`

(required) The unique identifier for the term.

`package_version`

(required) The version for the package.

`package_type`

(required) The package type for the listing.

Allowed values are: 'CONTAINER_IMAGE', 'HELM_CHART'

`lifecycle_state`

(required) The current state for the listing revision package.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`status`

(required) The current status for the listing revision package.

Allowed values are: 'NEW', 'PUBLISH_IN_PROGRESS', 'UNPUBLISH_IN_PROGRESS', 'PUBLISH_FAILED', 'PUBLISHED', 'PUBLISHED_AS_PRIVATE', 'UNPUBLISHED'

`are_security_upgrades_provided`

(required) Identifies whether security upgrades will be provided for this package.

`is_default`

(required) Identifies that this will be default package for the listing revision.

`time_created`

(required) The date and time this listing revision package was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(required) The date and time this listing revision package was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`extended_metadata`

(optional) Additional metadata key/value pairs for the listing revision package summary. For example: `{\"partnerListingRevisionPackageStatus\": \"Published\",\"parentListingRevisionPackageId\": \"1\" }`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CONTAINER_PACKAGE_T Type

A package for container image listings.

Syntax
```

```

`dbms_cloud_oci_marketplace_publisher_container_package_t`is a subtype of the`dbms_cloud_oci_marketplace_publisher_listing_revision_package_t`type.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_ARTIFACT_DETAILS_T Type

Common Details to create Marketplace Publisher artifact.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The unique identifier for the compartment.

`display_name`

(optional) The display name for the artifact.

`artifact_type`

(required) Artifact Type for the artifact.

Allowed values are: 'CONTAINER_IMAGE', 'HELM_CHART'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_CONTAINER_IMAGE_DETAILS_T Type

Container image details required to create a container artifact.

Syntax
```

```

Fields

Field Description

`source_registry_id`

(required) The source registry id of the container image.

`source_registry_url`

(required) The source registry url of the container image.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_CONTAINER_IMAGE_ARTIFACT_DETAILS_T Type

Details to create a new container image artifact.

Syntax
```

```

`dbms_cloud_oci_marketplace_publisher_create_container_image_artifact_details_t`is a subtype of the`dbms_cloud_oci_marketplace_publisher_create_artifact_details_t`type.

Fields

Field Description

`container_image`

(required)

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_HELM_CHART_IMAGE_DETAILS_T Type

Helmchart image details required to create an helmchart artifact.

Syntax
```

```

Fields

Field Description

`source_registry_id`

(required) The source registry OCID of the container image.

`source_registry_url`

(required) The source registry url of the helmchart image.

`supported_kubernetes_versions`

(optional) The Supported Versions of Kubernetes

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_KUBERNETES_IMAGE_ARTIFACT_DETAILS_T Type

Details to create a new helm chart image artifact.

Syntax
```

```

`dbms_cloud_oci_marketplace_publisher_create_kubernetes_image_artifact_details_t`is a subtype of the`dbms_cloud_oci_marketplace_publisher_create_artifact_details_t`type.

Fields

Field Description

`helm_chart`

(required)

`container_image_artifact_ids`

(optional) List of container image artifact uniquie identifiers included in the helm chart.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_LISTING_DETAILS_T Type

Details to create a new listing.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The unique identifier for the compartment.

`name`

(required) The name for the listing.

`listing_type`

(required) The listing type for the listing.

Allowed values are: 'OCI_APPLICATION'

`package_type`

(required) The package type for the listing.

Allowed values are: 'CONTAINER_IMAGE', 'HELM_CHART'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_LISTING_REVISION_ATTACHMENT_DETAILS_T Type

Attachment uploaded by the publisher for the listing revision.

Syntax
```

```

Fields

Field Description

`listing_revision_id`

(required) The OCID for the listing revision in Marketplace Publisher.

`display_name`

(optional) The name for the listing revision attachment.

`description`

(optional) Description for this specified attachment.

`attachment_type`

(required) The specified attachment type.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_VERSION_DETAILS_T Type

A listing version provided by the Publisher.

Syntax
```

```

Fields

Field Description

`l_number`

(required) The version number.

`description`

(required) The version description.

`release_date`

(required) The version release date.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LANGUAGE_ITEM_T Type

The model for a language item within an array of filter values.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the item.

`code`

(required) A code assigned to the item.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_SUPPORT_CONTACT_T Type

Contact information to use to get support.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the contact.

`phone`

(optional) The phone number of the contact.

`email`

(optional) The email of the contact.

`subject`

(optional) The email subject line to use when contacting support.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_NAMED_LINK_T Type

A link to a resource on the internet.

Syntax
```

```

Fields

Field Description

`name`

(required) Text that describes the resource.

`url`

(required) The URL of the resource.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LANGUAGE_ITEM_TBL Type

Nested table type of dbms_cloud_oci_marketplace_publisher_language_item_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_SUPPORT_CONTACT_TBL Type

Nested table type of dbms_cloud_oci_marketplace_publisher_support_contact_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_NAMED_LINK_TBL Type

Nested table type of dbms_cloud_oci_marketplace_publisher_named_link_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_LISTING_REVISION_DETAILS_T Type

The model for an Oracle Cloud Infrastructure Marketplace Publisher listing revision.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The name for the listing revision.

`listing_id`

(required) The unique identifier for the listing this revision belongs to.

`version_details`

(optional)

`headline`

(required) Single line introduction for the listing revision.

`tagline`

(optional) The tagline for the listing revision.

`keywords`

(optional) Keywords associated with the listing revision.

`short_description`

(optional) A short description for the listing revision.

`usage_information`

(optional) Usage information for the listing revision.

`long_description`

(optional) A long description for the listing revision.

`system_requirements`

(optional) System requirements for the listing revision.

`categories`

(required) The categories for the listing revision.

`markets`

(optional) The markets supported by the listing revision.

`content_language`

(optional)

`supportedlanguages`

(optional) Languages supported by the publisher for the listing revision.

`support_contacts`

(optional) Contact information to use to get support from the publisher for the listing revision.

`support_links`

(optional) Links to support resources for the listing revision.

`status`

(optional) The current status of the Listing revision.

`pricing_type`

(required) The pricing model for the listing revision.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_LISTING_REVISION_NOTE_DETAILS_T Type

The model for an Oracle Cloud Infrastructure Marketplace Publisher listing revision note.

Syntax
```

```

Fields

Field Description

`listing_revision_id`

(required) The unique identifier of the listing revision that the specified note belongs to.

`note_details`

(required) Notes provided for the listing revision.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_LISTING_REVISION_PACKAGE_DETAILS_T Type

The model for an Oracle Cloud Infrastructure Marketplace Publisher listing revision package.

Syntax
```

```

Fields

Field Description

`listing_revision_id`

(required) The OCID for the listing revision in Marketplace Publisher.

`package_version`

(required) The version for the package.

`display_name`

(optional) The name for the listing revision package.

`description`

(optional) Description for this package.

`artifact_id`

(required) The unique identifier for the artifact.

`term_id`

(required) The unique identifier for the term.

`is_default`

(optional) Identifies that this will be default package for the listing revision.

`are_security_upgrades_provided`

(required) Identifies whether security upgrades will be provided for this package.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_RELATED_DOCUMENT_ATTACHMENT_DETAILS_T Type

Create Details of the related document attachment.

Syntax
```

```

`dbms_cloud_oci_marketplace_publisher_create_related_document_attachment_details_t`is a subtype of the`dbms_cloud_oci_marketplace_publisher_create_listing_revision_attachment_details_t`type.

Fields

Field Description

`document_category`

(required) The document category of the listing revision attachment.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_SCREEN_SHOT_ATTACHMENT_DETAILS_T Type

Create Details of the screenshot attachment.

Syntax
```

```

`dbms_cloud_oci_marketplace_publisher_create_screen_shot_attachment_details_t`is a subtype of the`dbms_cloud_oci_marketplace_publisher_create_listing_revision_attachment_details_t`type.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_TERM_DETAILS_T Type

Details to create Marketplace Publisher term.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the publisher's compartment.

`name`

(required) The name of the term.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_VIDEO_DETAILS_T Type

A link to a video on the internet.

Syntax
```

```

Fields

Field Description

`content_url`

(required) The URL of the video.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_VIDEO_ATTACHMENT_DETAILS_T Type

Create Details of the video attachment.

Syntax
```

```

`dbms_cloud_oci_marketplace_publisher_create_video_attachment_details_t`is a subtype of the`dbms_cloud_oci_marketplace_publisher_create_listing_revision_attachment_details_t`type.

Fields

Field Description

`video_attachment_details`

(required)

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_ERROR_T Type

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

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_HELM_CHART_IMAGE_DETAILS_T Type

Helmchart image details.

Syntax
```

```

Fields

Field Description

`source_registry_id`

(optional) The source registry OCID of the helmchart image.

`source_registry_url`

(required) source registry url of the helmchart image.

`supported_kubernetes_versions`

(optional) The supported versions of Kubernetes

`validation_status`

(required) image validation status.

Allowed values are: 'VALIDATION_IN_PROGRESS', 'VALIDATION_FAILED', 'VALIDATION_COMPLETED'

`validation_error`

(optional) image validation failure errors

`publication_status`

(required) image publication status

Allowed values are: 'PUBLICATION_IN_PROGRESS', 'PUBLICATION_COMPLETED', 'PUBLICATION_FAILED'

`publication_error`

(optional) image validation failure errors

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_HELM_CHART_PACKAGE_T Type

A package for container image listings.

Syntax
```

```

`dbms_cloud_oci_marketplace_publisher_helm_chart_package_t`is a subtype of the`dbms_cloud_oci_marketplace_publisher_listing_revision_package_t`type.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_KUBERNETES_IMAGE_ARTIFACT_T Type

Kubernetes HelmChart Image artifact details.

Syntax
```

```

`dbms_cloud_oci_marketplace_publisher_kubernetes_image_artifact_t`is a subtype of the`dbms_cloud_oci_marketplace_publisher_artifact_t`type.

Fields

Field Description

`helm_chart`

(required)

`container_image_artifact_ids`

(optional) List of container image artifact unique identifiers included in the helm chart.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_T Type

The model for the Marketplace Publisher listing.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique OCID identifier for the listing.

`compartment_id`

(required) The unique identifier for the compartment.

`publisher_id`

(required) The unique identifier for the publisher.

`listing_type`

(required) The listing type for the listing.

Allowed values are: 'OCI_APPLICATION'

`name`

(required) Name for the listing.

`package_type`

(required) The package type for the listing.

Allowed values are: 'CONTAINER_IMAGE', 'HELM_CHART'

`extended_metadata`

(optional) Additional metadata key/value pairs for the listing summary. For example: `{\"listingRevisionStatus\": \"Published\",\"listingRevision\": \"1\" }`

`lifecycle_state`

(optional) The current state of the Listing.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(required) The date and time the listing was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2023-03-27T21:10:29.600Z`

`time_updated`

(required) The date and time the listing was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2023-03-27T21:10:29.600Z`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_SUMMARY_T Type

The model for a summary of the publisher listing.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique OCID of the listing.

`compartment_id`

(required) The unique identifier of the compartment.

`listing_type`

(required) The listing type of the Listing.

Allowed values are: 'OCI_APPLICATION'

`name`

(required) The name of the listing.

`lifecycle_state`

(required) The current state for the Listing.

`package_type`

(required) The package type for the listing.

Allowed values are: 'CONTAINER_IMAGE', 'HELM_CHART'

`time_created`

(required) The date and time the listing was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2023-03-27T21:10:29.600Z`

`time_updated`

(required) The date and time the listing was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2023-03-27T21:10:29.600Z`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_marketplace_publisher_listing_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_COLLECTION_T Type

Results of listing search. Contains Listing items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of listing summary.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_ICON_ATTACHMENT_T Type

An attachment uploaded by the Publisher to be attached to the listing revision.

Syntax
```

```

Fields

Field Description

`content_url`

(required) The content URL of the uploaded data.

`mime_type`

(required) The MIME type of the uploaded data.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_T Type

The model for an Oracle Cloud Infrastructure Marketplace Publisher listing revision.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique OCID identifier for the listing revision in Marketplace Publisher.

`listing_id`

(required) The unique identifier for the listing this revision belongs to.

`compartment_id`

(optional) The unique identifier for the compartment.

`display_name`

(required) The name for the listing revision.

`revision_number`

(optional) The revision number for the listing revision. This is an internal attribute

`version_details`

(optional)

`headline`

(required) Single line introduction for the listing revision.

`tagline`

(optional) The tagline of the listing revision.

`keywords`

(optional) Keywords associated with the listing revision.

`short_description`

(optional) A short description for the listing revision.

`usage_information`

(optional) Usage information for the listing revision.

`long_description`

(optional) A long description for the listing revision.

`system_requirements`

(optional) System requirements for the listing revision.

`time_created`

(required) The time the listing revision was created. An RFC3339 formatted datetime string.

`time_updated`

(required) The time the listing revision was updated. An RFC3339 formatted datetime string.

`categories`

(required) The categories for the listing revsion.

`markets`

(optional) The markets supported by the listing revision.

`content_language`

(optional)

`supportedlanguages`

(optional) Languages supported by the publisher for the listing revision.

`support_contacts`

(optional) Contact information to use to get support from the publisher for the listing revision.

`support_links`

(optional) Links to support resources for the listing revision.

`icon`

(optional)

`status`

(required) The current status for the Listing revision.

Allowed values are: 'NEW', 'PENDING_REVIEW', 'REVIEW_IN_PROGRESS', 'REJECTED', 'APPROVED', 'PUBLISH_IN_PROGRESS', 'PUBLISH_FAILED', 'PUBLISHED', 'PUBLISH_AS_PRIVATE_FAILED', 'PUBLISHED_AS_PRIVATE', 'PUBLISH_AS_PRIVATE_IN_PROGRESS', 'UNPUBLISH_IN_PROGRESS', 'UNPUBLISHED'

`status_notes`

(optional) Status notes for the listing revision.

`lifecycle_state`

(required) The current state of the listing revision.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`package_type`

(required) The listing's package type. Populated from the listing.

Allowed values are: 'CONTAINER_IMAGE', 'HELM_CHART'

`pricing_type`

(required) The pricing model for the listing revision.

Allowed values are: 'FREE', 'BYOL', 'PAYGO'

`allowed_tenancies`

(optional) Allowed tenancies provided when a listing revision is published as private.

`are_internal_tenancy_launch_allowed`

(optional) Identifies whether publisher allows internal tenancy launches for the listing revision.

`extended_metadata`

(optional) Additional metadata key/value pairs for the listing revision summary.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_ATTACHMENT_T Type

A attachment for the listing revision. User can provide an external URL/upload a file

Syntax
```

```

Fields

Field Description

`id`

(required) Unique OCID identifier for the listing revision attachment.

`compartment_id`

(required) The unique identifier for the compartment.

`listing_revision_id`

(required) The unique identifier of the listing revision that the specified attachment belongs to.

`display_name`

(required) Name of the listing revision attachment.

`description`

(optional) Description of the listing revision attachment.

`attachment_type`

(required) Possible values for the publisher listing revision attachments. The attachment type informs the type of attachment for the listing revision.

Allowed values are: 'RELATED_DOCUMENT', 'SCREENSHOT', 'VIDEO'

`lifecycle_state`

(required) The current state of the attachment.

Allowed values are: 'ACTIVE', 'INACTIVE', 'DELETED'

`time_created`

(required) The time the attachment was created. An RFC3339 formatted datetime string.

`time_updated`

(required) The time the attachment was updated. An RFC3339 formatted datetime string.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_ATTACHMENT_SUMMARY_T Type

The model for a summary of a listing revision related attachments.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the listing revision attachment.

`listing_revision_id`

(required) The ID of the listing revision.

`compartment_id`

(required) The unique identifier for the compartment.

`display_name`

(required) The name of the specified document.

`attachment_type`

(required) The specified attachment type.

`content_url`

(required) The URL of the specified attachment.

`mime_type`

(optional) The MIME type of the screenshot.

`lifecycle_state`

(optional) The current state of the document.

`time_created`

(required) The date and time the related document was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2022-09-24T21:10:29.600Z`

`time_updated`

(required) The date and time the related document was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2022-09-24T21:10:29.600Z`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_ATTACHMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_marketplace_publisher_listing_revision_attachment_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_ATTACHMENT_COLLECTION_T Type

Results of the listing attachments search. Contains attachment items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of attachment summary.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_SUMMARY_T Type

The model for a summary of an Oracle Cloud Infrastructure Marketplace Publisher listing revision.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID for the listing revision in Marketplace Publisher.

`listing_id`

(required) The OCID for the listing in Marketplace Publisher.

`compartment_id`

(required) The unique identifier for the compartment.

`display_name`

(required) The name of the listing revision.

`status`

(required) The current status of the listing revision.

`lifecycle_state`

(required) The current state of the Listing.

`package_type`

(required) The listing's package type.

Allowed values are: 'CONTAINER_IMAGE', 'HELM_CHART'

`pricing_type`

(required) Pricing type of the listing.

`short_description`

(optional) A short description of the listing revision.

`tagline`

(optional) The tagline of the listing revision.

`icon`

(optional)

`markets`

(optional) The markets where you can deploy the listing.

`categories`

(required) Categories that the listing revision belongs to.

`time_created`

(required) The date and time the listing revision was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2022-09-15T21:10:29.600Z`

`time_updated`

(required) The date and time the listing revision was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2022-09-15T21:10:29.600Z`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_marketplace_publisher_listing_revision_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_COLLECTION_T Type

Results of listing revision search. Contains Listing revision items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of listing revision summary.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_NOTE_T Type

The model for the listing revision notes.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the listing revision note.

`listing_revision_id`

(required) The unique identifier of the listing revision that the specified note belongs to.

`compartment_id`

(required) The unique identifier for the compartment.

`note_source`

(required) type of the note.

Allowed values are: 'PUBLISHER', 'ADMINISTRATOR'

`note_details`

(required) Notes provided for the listing revision.

`lifecycle_state`

(optional) The current state of the listing revision note.

Allowed values are: 'ACTIVE', 'DELETED'

`time_created`

(required) The date and time the listing revision note was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2022-09-24T21:10:29.600Z`

`time_updated`

(required) The date and time the listing revision note was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2022-09-24T21:10:29.600Z`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_NOTE_SUMMARY_T Type

The model for a summary of a listing revision notes.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the listing revision note.

`listing_revision_id`

(required) The unique identifier of the listing revision that the specified note belongs to.

`compartment_id`

(required) The unique identifier for the compartment.

`note_source`

(required) type of the note.

`note_details`

(required) Notes provided for the listing revision.

`lifecycle_state`

(optional) The current state of the note.

`time_created`

(required) The date and time the listing revision note was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2022-09-24T21:10:29.600Z`

`time_updated`

(required) The date and time the listing revision note was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2022-09-24T21:10:29.600Z`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_NOTE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_marketplace_publisher_listing_revision_note_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_NOTE_COLLECTION_T Type

Results of note search. Contains listing revision note items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of note summary.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_PACKAGE_SUMMARY_T Type

The model for a summary of a package.

Syntax
```

```

Fields

Field Description

`id`

(required) The ID of the listing revision package.

`listing_revision_id`

(required) The ID of the listing revision.

`compartment_id`

(required) The unique identifier for the compartment.

`display_name`

(required) The name of the listing revision package.

`package_version`

(required) The version of the specified package.

`package_type`

(required) The specified package's type.

Allowed values are: 'CONTAINER_IMAGE', 'HELM_CHART'

`are_security_upgrades_provided`

(required) Identifies whether security upgrades will be provided for this package.

`lifecycle_state`

(required) The current state of the Package.

`status`

(required) The current status of the package.

`time_created`

(required) The date and time the publication package was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2022-09-24T21:10:29.600Z`

`time_updated`

(required) The date and time the publication package was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2022-09-24T21:10:29.600Z`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_PACKAGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_marketplace_publisher_listing_revision_package_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_PACKAGE_COLLECTION_T Type

Results of package search. Contains Package items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of package summary.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_MARKET_T Type

The model for the market details.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the market.

`code`

(required) The code of the market.

`category_code`

(required) The category code of the market.

`realm_code`

(optional) The realm code of the market.

`bill_to_countries`

(required) bill to countries for the market.

`lifecycle_state`

(required) The current state for the market.

Allowed values are: 'ACTIVE', 'INACTIVE'

`time_created`

(required) The date and time the market was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2022-09-15T21:10:29.600Z`

`time_updated`

(required) The date and time the market was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2022-09-15T21:10:29.600Z`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_MARKET_SUMMARY_T Type

The model for the market metadata.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the product.

`code`

(required) The code of the product.

`category_code`

(required) The category code for the market.

`bill_to_countries`

(required) Bill to countries for the market.

`lifecycle_state`

(required) The current state for the market.

`time_created`

(required) The date and time the market was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2022-09-15T21:10:29.600Z`

`time_updated`

(required) The date and time the market was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2022-09-15T21:10:29.600Z`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_MARKET_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_marketplace_publisher_market_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_MARKET_COLLECTION_T Type

Results of a market search. Contains the market items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of market summary.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_OPN_MEMBERSHIP_T Type

OPN membership information

Syntax
```

```

Fields

Field Description

`time_start`

(optional) OPN membership start date. An RFC3339 formatted datetime string

`time_end`

(optional) OPN membership end date. An RFC3339 formatted datetime string

`opn_status`

(optional) OPN status

Allowed values are: 'ACTIVE', 'INACTIVE', 'RENEWAL_IN_PROGRESS'

`opn_number`

(optional) OPN Number number

`opn_membership_type`

(optional) OPN membership type

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_PRIVATE_OFFER_ACCOUNT_DETAILS_T Type

Private Offer account details.

Syntax
```

```

Fields

Field Description

`meter`

(optional) Meter name

`sku`

(optional) SKU name

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_PRODUCT_T Type

The model for the product details.

Syntax
```

```

Fields

Field Description

`name`

(required) The name for the product.

`code`

(required) The code for the product.

`product_group`

(required) The product group for the product.

`lifecycle_state`

(required) The current state for the product.

Allowed values are: 'ACTIVE', 'INACTIVE'

`time_created`

(required) The date and time the product was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2022-09-15T21:10:29.600Z`

`time_updated`

(required) The date and time the product was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2022-09-15T21:10:29.600Z`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_PRODUCT_SUMMARY_T Type

The model for the product metadata.

Syntax
```

```

Fields

Field Description

`name`

(required) The name for the product.

`code`

(optional) The code for the product.

`product_group`

(optional) The product group for the product.

`lifecycle_state`

(required) The current state for the product.

`time_created`

(required) The date and time the product was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2022-09-15T21:10:29.600Z`

`time_updated`

(required) The date and time the product was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2022-09-15T21:10:29.600Z`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_PRODUCT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_marketplace_publisher_product_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_PRODUCT_COLLECTION_T Type

Results of a product search. Contains the product items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of product summary.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_PUBLISH_LISTING_REVISION_AS_PRIVATE_DETAILS_T Type

The model for an Oracle Cloud Infrastructure Marketplace Publisher publish as private listing revision.

Syntax
```

```

Fields

Field Description

`allowed_tenancies`

(optional) Allowed tenancies provided when a listing is published as private.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPLOAD_DATA_T Type

The model for upload data for images and icons.

Syntax
```

```

Fields

Field Description

`name`

(optional) The name used to refer to the upload data.

`content_url`

(optional) The content URL of the upload data.

`mime_type`

(optional) The MIME type of the upload data.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_PUBLISHER_T Type

The model for a publisher details.

Syntax
```

```

Fields

Field Description

`publisher_status`

(required) publisher status.

Allowed values are: 'NEW', 'APPROVED', 'SUSPENDED', 'REMOVED', 'REJECTED', 'CONTACTED'

`notification_email`

(optional) The private email address of the publisher product team.

`opn_membership`

(optional)

`private_offer_account_details`

(optional)

`id`

(required) Unique OCID identifier for the publisher.

`compartment_id`

(required) The root compartment of the Publisher.

`registry_namespace`

(required) The namespace for the publisher registry to persist artifacts.

`legacy_id`

(optional) Unique legacy service identifier for the publisher.

`display_name`

(required) The name of the publisher.

`description`

(optional) A description of the publisher.

`year_founded`

(optional) The year the publisher's company or organization was founded.

`website_url`

(optional) The publisher's website.

`contact_email`

(required) The public email address of the publisher for customers.

`contact_phone`

(required) The phone number of the publisher in E.164 format.

`hq_address`

(optional) The address of the publisher's headquarters.

`logo`

(optional)

`facebook_url`

(optional) Publisher's Facebook URL

`twitter_url`

(optional) Publisher's Twitter URL

`linkedin_url`

(optional) Publisher's LinkedIn URL

`publisher_type`

(required) publisher type.

Allowed values are: 'INTERNAL', 'EXTERNAL'

`time_created`

(required) The time the publisher was created. An RFC3339 formatted datetime string.

`time_updated`

(required) The time the publisher was updated. An RFC3339 formatted datetime string.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_PUBLISHER_SUMMARY_T Type

The model for a publisher.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique OCID identifier for the publisher.

`compartment_id`

(required) The root compartment of the Publisher.

`registry_namespace`

(required) The namespace for the publisher registry to persist artifacts.

`legacy_id`

(optional) Unique legacy service identifier for the publisher.

`display_name`

(required) The name of the publisher.

`description`

(optional) A description of the publisher.

`year_founded`

(optional) The year the publisher's company or organization was founded.

`website_url`

(optional) The publisher's website.

`contact_email`

(required) The public email address of the publisher for customers.

`contact_phone`

(required) The phone number of the publisher in E.164 format.

`hq_address`

(optional) The address of the publisher's headquarters.

`logo`

(optional)

`facebook_url`

(optional) Publisher's Facebook URL

`twitter_url`

(optional) Publisher's Twitter URL

`linkedin_url`

(optional) Publisher's LinkedIn URL

`publisher_type`

(required) publisher type.

Allowed values are: 'INTERNAL', 'EXTERNAL'

`time_created`

(required) The time the publisher was created. An RFC3339 formatted datetime string.

`time_updated`

(required) The time the publisher was updated. An RFC3339 formatted datetime string.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_PUBLISHER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_marketplace_publisher_publisher_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_PUBLISHER_COLLECTION_T Type

Results of a publisher search. Contains Publisher items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of publisher summary.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_RELATED_DOCUMENT_ATTACHMENT_T Type

Related document attachment for the listing revision.

Syntax
```

```

`dbms_cloud_oci_marketplace_publisher_related_document_attachment_t`is a subtype of the`dbms_cloud_oci_marketplace_publisher_listing_revision_attachment_t`type.

Fields

Field Description

`document_category`

(optional) Possible lifecycle states.

Allowed values are: 'CASE_STUDIES', 'CUSTOMIZATION_GUIDES', 'DATA_SHEETS', 'PRESS_RELEASE', 'PRODUCT_DOCUMENTATION', 'USER_GUIDES', 'WEBINAR'

`content_url`

(optional) URL of the uploaded document.

`mime_type`

(optional) The MIME type of the uploaded data.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_SCREEN_SHOT_ATTACHMENT_T Type

Screenshot attachment for the listing revision.

Syntax
```

```

`dbms_cloud_oci_marketplace_publisher_screen_shot_attachment_t`is a subtype of the`dbms_cloud_oci_marketplace_publisher_listing_revision_attachment_t`type.

Fields

Field Description

`content_url`

(optional) URL of the uploaded document.

`mime_type`

(optional) The MIME type of the uploaded data.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_SUBMIT_LISTING_REVISION_FOR_REVIEW_DETAILS_T Type

The model for an Oracle Cloud Infrastructure Marketplace Publisher review listing revision.

Syntax
```

```

Fields

Field Description

`note_details`

(optional) Notes provided for the listing revision.

`are_internal_tenancy_launch_allowed`

(optional) Identifies whether publisher allows internal tenancy launches for the listing revision.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_TERM_T Type

Base model object for the term.

Syntax
```

```

Fields

Field Description

`id`

(optional) Unique OCID identifier for the term.

`name`

(required) The name for the term.

`author`

(required) Who authored the term. Publisher terms will be defaulted to 'PARTNER'.

Allowed values are: 'ORACLE', 'PARTNER'

`compartment_id`

(required) The unique identifier for the compartment.

`publisher_id`

(required) The unique identifier for the publisher.

`lifecycle_state`

(required) The current state for the Term.

Allowed values are: 'ACTIVE', 'INACTIVE'

`time_created`

(required) The date and time the term was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2022-09-15T21:10:29.600Z`

`time_updated`

(required) The date and time the term was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2022-09-15T21:10:29.600Z`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_TERM_SUMMARY_T Type

The model for the term summary.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique OCID identifier for the term.

`compartment_id`

(required) The unique identifier for the compartment.

`name`

(required) The name for the term.

`author`

(required) Who authored the term. Publisher terms will be defaulted to as 'PARTNER'.

`lifecycle_state`

(required) The current state for the term version.

`time_created`

(required) The date and time the resource was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2022-09-15T21:10:29.600Z`

`time_updated`

(required) The date and time the resource was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2022-09-15T21:10:29.600Z`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_TERM_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_marketplace_publisher_term_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_TERM_COLLECTION_T Type

Results of the term search. Contains term items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of the Terms summary.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_TERM_VERSION_ATTACHMENT_T Type

An attachment uploaded by the Publisher for the term.

Syntax
```

```

Fields

Field Description

`content_url`

(required) The content URL of the uploaded data.

`mime_type`

(required) The MIME type of the uploaded data.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_TERM_VERSION_T Type

Model object for the term version details.

Syntax
```

```

Fields

Field Description

`id`

(optional) Unique OCID identifier for the term version.

`term_id`

(required) The unique identifier for the term.

`term_author`

(required) Who authored the term. Publisher terms will be defaulted to 'PARTNER'.

`display_name`

(required) The name for the term version.

`compartment_id`

(optional) The unique identifier for the compartment.

`attachment`

(required)

`status`

(required) The current status for the term version.

Allowed values are: 'AVAILABLE', 'NOT_AVAILABLE', 'DELETED'

`author`

(optional) Who authored the term. Publisher terms will be defaulted to 'PARTNER'.

`lifecycle_state`

(required) The current state for the term version.

Allowed values are: 'ACTIVE', 'INACTIVE'

`time_created`

(required) The date and time the term version was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2022-09-15T21:10:29.600Z`

`time_updated`

(required) The date and time the term version was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2022-09-15T21:10:29.600Z`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_TERM_VERSION_SUMMARY_T Type

The model for the term version summary.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique OCID identifier for the term version.

`compartment_id`

(required) The unique identifier for the compartment.

`display_name`

(required) The name for the term version.

`status`

(required) The current status for the term version.

`lifecycle_state`

(required) The current state for the Term version.

`time_created`

(required) The date and time the term version was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2022-09-15T21:10:29.600Z`

`time_updated`

(required) The date and time the time version was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2022-09-15T21:10:29.600Z`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_TERM_VERSION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_marketplace_publisher_term_version_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_TERM_VERSION_COLLECTION_T Type

Results of the term version search. Contains term version items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of the Terms version summary.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_ARTIFACT_DETAILS_T Type

The model for an Oracle Cloud Infrastructure Marketplace artifact.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The unique identifier for the compartment.

`display_name`

(optional) The display name for the artifact.

`artifact_type`

(optional) Artifact Type for the artifact.

Allowed values are: 'CONTAINER_IMAGE', 'HELM_CHART'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_CONTAINER_IMAGE_DETAILS_T Type

Container image details required to update a container artifact.

Syntax
```

```

Fields

Field Description

`source_registry_id`

(required) The source registry OCID of the container image.

`source_registry_url`

(required) The source registry url of the container image.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_CONTAINER_IMAGE_ARTIFACT_DETAILS_T Type

Details to update the container image artifact.

Syntax
```

```

`dbms_cloud_oci_marketplace_publisher_update_container_image_artifact_details_t`is a subtype of the`dbms_cloud_oci_marketplace_publisher_update_artifact_details_t`type.

Fields

Field Description

`container_image`

(optional)

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_HELM_CHART_IMAGE_DETAILS_T Type

Helmchart image details required to update an helmchart artifact.

Syntax
```

```

Fields

Field Description

`source_registry_id`

(required) The source registry OCID of the helmchart image.

`source_registry_url`

(required) The source registry url of the helmchart image.

`supported_kubernetes_versions`

(optional) The Supported Versions of Kubernetes

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_KUBERNETES_IMAGE_ARTIFACT_DETAILS_T Type

Details to update the kubernetes image artifact.

Syntax
```

```

`dbms_cloud_oci_marketplace_publisher_update_kubernetes_image_artifact_details_t`is a subtype of the`dbms_cloud_oci_marketplace_publisher_update_artifact_details_t`type.

Fields

Field Description

`helm_chart`

(optional)

`container_image_artifact_ids`

(optional) List of container image artifact unique identifiers included in the helm chart.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_LISTING_DETAILS_T Type

Details to update an existing listing.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_LISTING_REVISION_ATTACHMENT_DETAILS_T Type

Update the attachment for the listing revision.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The name for the listing revision attachment.

`description`

(optional) The description for the listing revision attachment.

`attachment_type`

(optional) The specified attachment type for the listing revision attachment.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_LISTING_REVISION_DETAILS_T Type

The model for an Oracle Cloud Infrastructure Marketplace Publisher listing revision.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The name for the listing revision.

`version_details`

(optional)

`headline`

(optional) Single line introduction for the listing revision.

`tagline`

(optional) The tagline for the listing revision.

`keywords`

(optional) Keywords associated for the listing revision.

`short_description`

(optional) A short description for the listing revision.

`usage_information`

(optional) Usage information for the listing revision.

`long_description`

(optional) A long description for the listing revision.

`system_requirements`

(optional) System requirements for the listing revision.

`categories`

(optional) The categories for the listing revision.

`markets`

(optional) The markets supported by the listing revision.

`content_language`

(optional)

`supportedlanguages`

(optional) Languages supported by the listing revision.

`support_contacts`

(optional) Contact information to use to get support from the publisher for the listing revision.

`support_links`

(optional) Links to support resources for the listing revision.

`pricing_type`

(optional) The pricing model for the listing revision.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_LISTING_REVISION_PACKAGE_DETAILS_T Type

The model for an Oracle Cloud Infrastructure Marketplace Listing revison package.

Syntax
```

```

Fields

Field Description

`package_version`

(optional) The version for the package.

`display_name`

(optional) The name for the listing revision package.

`description`

(optional) The description for this package.

`artifact_id`

(optional) The unique identifier for the artifact.

`term_id`

(optional) The unique term identifier.

`is_default`

(optional) Identifies that this will be default package for the listing revision.

`are_security_upgrades_provided`

(optional) Identifies whether security upgrades will be provided for this package.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_RELATED_DOCUMENT_ATTACHMENT_DETAILS_T Type

Update Details of the related document attachment.

Syntax
```

```

`dbms_cloud_oci_marketplace_publisher_update_related_document_attachment_details_t`is a subtype of the`dbms_cloud_oci_marketplace_publisher_update_listing_revision_attachment_details_t`type.

Fields

Field Description

`document_category`

(optional) The document category of the listing revision attachment.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_SCREEN_SHOT_ATTACHMENT_DETAILS_T Type

Update details of the screenshot attachment.

Syntax
```

```

`dbms_cloud_oci_marketplace_publisher_update_screen_shot_attachment_details_t`is a subtype of the`dbms_cloud_oci_marketplace_publisher_update_listing_revision_attachment_details_t`type.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_TERM_DETAILS_T Type

Details to update Marketplace Publisher term.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_TERM_VERSION_DETAILS_T Type

Details to update Marketplace Publisher term version.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The name for the term version.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_VIDEO_ATTACHMENT_DETAILS_T Type

Details of the video attachment.

Syntax
```

```

`dbms_cloud_oci_marketplace_publisher_update_video_attachment_details_t`is a subtype of the`dbms_cloud_oci_marketplace_publisher_update_listing_revision_attachment_details_t`type.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_VIDEO_ATTACHMENT_T Type

Video attachment for the listing revision.

Syntax
```

```

`dbms_cloud_oci_marketplace_publisher_video_attachment_t`is a subtype of the`dbms_cloud_oci_marketplace_publisher_listing_revision_attachment_t`type.

Fields

Field Description

`content_url`

(required) The URL for the video.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_WORK_REQUEST_RESOURCE_T Type

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

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED', 'FAILED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata

`metadata`

(optional) Additional information that helps to explain the resource.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_marketplace_publisher_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_WORK_REQUEST_T Type

A description of workrequest status

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'PUBLISH_LISTING_REVISION_PACKAGE', 'UNPUBLISH_LISTING_REVISION_PACKAGE', 'PUBLISH_LISTING_REVISION', 'PUBLISH_LISTING_REVISION_AS_PRIVATE', 'WITHDRAW_LISTING_REVISION', 'CLONE_LISTING_REVISION', 'CASCADING_DELETE_LISTING', 'CASCADING_DELETE_LISTING_REVISION', 'MARK_AS_DEFAULT_LISTING_REVISION_PACKAGE', 'CHANGE_LISTING_COMPARTMENT', 'CREATE_ARTIFACT', 'VALIDATE_AND_PUBLISH_ARTIFACT', 'CHANGE_ARTIFACT_COMPARTMENT', 'CHANGE_TERM_COMPARTMENT', 'DELETE_ARTIFACT'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'NEEDS_ATTENTION', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

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

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_WORK_REQUEST_ERROR_T Type

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

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_marketplace_publisher_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestError objects.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_WORK_REQUEST_LOG_ENTRY_T Type

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

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_marketplace_publisher_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a workRequestLog search. Contains both workRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestLogEntries.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'PUBLISH_LISTING_REVISION_PACKAGE', 'UNPUBLISH_LISTING_REVISION_PACKAGE', 'PUBLISH_LISTING_REVISION', 'PUBLISH_LISTING_REVISION_AS_PRIVATE', 'WITHDRAW_LISTING_REVISION', 'CLONE_LISTING_REVISION', 'CASCADING_DELETE_LISTING', 'CASCADING_DELETE_LISTING_REVISION', 'MARK_AS_DEFAULT_LISTING_REVISION_PACKAGE', 'CHANGE_LISTING_COMPARTMENT', 'CREATE_ARTIFACT', 'VALIDATE_AND_PUBLISH_ARTIFACT', 'CHANGE_ARTIFACT_COMPARTMENT', 'CHANGE_TERM_COMPARTMENT', 'DELETE_ARTIFACT'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'NEEDS_ATTENTION', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

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

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_marketplace_publisher_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestSummary objects.

- [Marketplace Publisher Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-B7B7EADE-6DCD-4F60-942E-97D81F48B355)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-8C972844-7A36-4257-8C93-82702EAABF5C)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_ARTIFACT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-A114F885-80B8-450D-B023-30C12C55BC6A)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_ARTIFACT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-A2DA943A-946E-4B4E-ABB3-0442602372DC)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_ARTIFACT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-56523B61-A689-47DE-88D3-F56AA1E9AE9D)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_ARTIFACT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-3814C493-0CC4-4920-8827-8F8122A28363)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CATEGORY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-21C1653B-ECCF-4145-8045-892E88902BD8)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CATEGORY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-36FC6F78-2B44-44FC-A7D8-A022434F4FCC)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CATEGORY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-68108546-D0FD-4951-B1D9-155AE999C771)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CATEGORY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-8F44EAF0-C171-472E-9EFB-4BAFC988C075)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CHANGE_ARTIFACT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-519DFCA2-8F16-47A5-8258-87B540AD5A27)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CHANGE_LISTING_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-F892BF79-C6C5-4912-A194-F54371501AE4)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CHANGE_TERM_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-F8BEA096-13AF-431D-BCFA-5B776D0955E4)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CONTAINER_IMAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-D1084267-B8B5-42BB-AA4F-9DE93F28B6A6)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CONTAINER_IMAGE_ARTIFACT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-FB4CFC14-7C98-4C86-A679-FEC73E8C6BCB)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_PACKAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-FAAE6C11-AC54-47E9-8F03-56E9BB55AD5A)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CONTAINER_PACKAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-5A0A9A54-2F07-435F-8B04-77234C8DE351)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_ARTIFACT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-14C8E7C5-6FCF-4C5D-8FC4-9E39A4B8789D)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_CONTAINER_IMAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-3C2EF3BF-853F-4F03-A5A8-FB1A41DE8C8F)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_CONTAINER_IMAGE_ARTIFACT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-390C95C0-5719-45EF-A32C-7C8B962A94C0)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_HELM_CHART_IMAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-7E018A2C-EF65-46D2-82E6-3650225F95AA)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_KUBERNETES_IMAGE_ARTIFACT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-0528B792-0901-4E9A-B4AE-D8E993470358)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_LISTING_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-3A9835B1-287D-449C-AB01-FB82677633AC)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_LISTING_REVISION_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-2A66A7A8-B7BA-4D94-8191-FD71F141DEF2)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_VERSION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-647CC61B-C722-468E-8F33-DEBEEC3E7936)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LANGUAGE_ITEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-26CA8630-5FF6-4A52-8442-7BECE7DC3E2A)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_SUPPORT_CONTACT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-9F315E02-0BB0-4CE2-8852-B6CB107FF035)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_NAMED_LINK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-B665F5B1-1BA7-4435-A423-8BC867561752)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LANGUAGE_ITEM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-47F92B86-52B7-4996-B3F4-0A4DD1A9FF25)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_SUPPORT_CONTACT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-08C881C8-2B21-4B74-9C23-D88EFCB47620)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_NAMED_LINK_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-B2B7C16F-30AB-4619-A1F8-7C25F0E14A03)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_LISTING_REVISION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-9D7A8B8F-2221-477B-8466-4FA4A44AEC69)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_LISTING_REVISION_NOTE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-C0CD4C3D-182E-49C7-B1AE-9E7E4A8D4C62)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_LISTING_REVISION_PACKAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-DCDB1761-F838-42B6-88D8-ECF51F845BA3)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_RELATED_DOCUMENT_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-679BA6EF-7F02-4130-8A4C-5A124B634A98)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_SCREEN_SHOT_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-B0876A81-7D79-4A18-A8C9-5F78DD18A6A2)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_TERM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-C45EE42C-CF27-479D-9F72-BBC6725FA687)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_VIDEO_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-96C86A05-8B7D-40C5-85CB-E783F4C0D861)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_CREATE_VIDEO_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-972183B3-1179-4393-ADD0-F9283E3D6D5E)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-370D3EEE-5287-4CB4-939F-DE0398F5F960)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_HELM_CHART_IMAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-362BF536-B02B-493A-8F7C-8C5091A9BBD2)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_HELM_CHART_PACKAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-2FEA1CCA-82DA-420E-A695-16BAEAB33372)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_KUBERNETES_IMAGE_ARTIFACT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-E3A1EB8B-C694-4123-9690-5C4DDFAF39E6)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-FC57D4F8-3400-4868-A8C0-07B51434B47E)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-2FAF8954-199F-498E-A9FE-6D5F61A41A43)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-3D8DCBFF-569C-487B-B2C6-648E1C8144F7)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-AA5A3CB1-5B25-465F-B609-11DFF9DE34FD)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_ICON_ATTACHMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-938A6FD8-0420-4651-81A3-CB712F79EFBC)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-44FEFB9D-F8E2-4AC5-9211-F79A70192EB9)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_ATTACHMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-399283B8-4CE6-42C2-9BF8-9D79CD3E4475)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_ATTACHMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-F0173866-E2E8-4FD8-947D-2F55CCDCF582)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_ATTACHMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-30B8BEE0-8A6A-4EB0-BBC2-598B106CD31B)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_ATTACHMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-DC3AE150-B138-4EE1-986D-D0E77474C16D)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-E6EBF9F0-B73D-467C-905F-48AEEC970F43)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-2F1C6A14-2859-4CFD-BECE-18C7374C225F)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-C939C839-75CC-464B-B4F8-4A7AED39115A)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_NOTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-A312BEF8-8EC2-4EFC-9058-024A642B291C)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_NOTE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-6DCDF0A8-AEDF-4388-8E03-1CC62C06BF92)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_NOTE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-59918AC4-C7AF-4171-A939-6BB853DD6D01)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_NOTE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-167F28FB-A87A-4F31-842F-F1A535C36FF2)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_PACKAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-9A109E63-2C9F-450C-B78F-21D89C9650AD)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_PACKAGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-BC4D404C-13A6-445D-BF3A-99677ECD1B4A)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_LISTING_REVISION_PACKAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-51547D77-B33E-4F7F-923E-65B0CF6CB9F7)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_MARKET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-4ADC299C-B8D5-4E0C-A55A-C0EE882167C3)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_MARKET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-77D06E1A-EB87-497D-B702-C2BC383476E1)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_MARKET_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-1125CB1D-B95A-42AD-988F-11FAB135CF9B)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_MARKET_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-831321BF-C4A1-4A91-AC98-07CCD883C867)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_OPN_MEMBERSHIP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-37964E41-C3EA-424F-B9C3-485BA4DFF66D)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_PRIVATE_OFFER_ACCOUNT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-395692FC-9EB7-4D89-9085-5F7943942A47)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_PRODUCT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-E551F142-0D9C-41E8-8DB9-4DB1C3F3C307)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_PRODUCT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-ABE71DCE-795A-4C2A-9DD7-5F1B0E185CA1)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_PRODUCT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-CD95A770-A35E-41F4-9F00-588027C2FEAB)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_PRODUCT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-321DC8A4-A192-46DA-BF7A-D327EBD4239A)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_PUBLISH_LISTING_REVISION_AS_PRIVATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-42CE2090-AE5D-47F2-9324-20E70AF74F63)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPLOAD_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-CCB8C4D8-30F8-4C7E-8679-DE128ECF0F1D)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_PUBLISHER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-58F9EFB4-265A-4637-BD6C-60865B0A6C2D)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_PUBLISHER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-0C1D320B-99E8-473E-9A33-F478B854CD6E)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_PUBLISHER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-FEA0FF13-54AE-407E-9FFB-D963B860DF57)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_PUBLISHER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-C8CF7CA6-64E9-4FE7-84E8-FBBC7BAE2918)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_RELATED_DOCUMENT_ATTACHMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-11FE7599-62DF-4664-9A39-43F713B29F86)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_SCREEN_SHOT_ATTACHMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-EC1563DB-DF94-45F3-B7E0-FBE76E5136F4)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_SUBMIT_LISTING_REVISION_FOR_REVIEW_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-F734342B-E7EE-455C-A61A-FA594A2317D0)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_TERM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-1BFDBFE1-577E-47D3-BD2A-965315675B60)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_TERM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-6012BC65-2037-4597-9464-7CA08907ADCB)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_TERM_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-83E3BCD8-5676-49C0-B09A-7EBCF80160C2)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_TERM_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-89B7F097-C5E9-42EC-A7D9-7AFD3A7BA619)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_TERM_VERSION_ATTACHMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-0B41D705-D879-42BC-99FB-9F6FB8CD66ED)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_TERM_VERSION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-28050EEF-5F06-454C-80E1-54AC959A8990)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_TERM_VERSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-8A34D4D1-B50B-41E0-BDAE-604F1FCFB9A5)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_TERM_VERSION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-EEE30483-4B76-474F-81AB-D688114480CD)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_TERM_VERSION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-31CEF8ED-9161-40C4-B0DB-07DED5B2C389)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_ARTIFACT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-26C72634-FA6C-4B09-9488-18076E5DBFFA)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_CONTAINER_IMAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-C3F67FAB-086B-494C-A1BD-320887AD742E)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_CONTAINER_IMAGE_ARTIFACT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-87786FD6-E4C2-48E7-AE50-EDB576B98DA7)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_HELM_CHART_IMAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-53D5B8B1-38A4-4D4F-A5AE-712CF2375E01)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_KUBERNETES_IMAGE_ARTIFACT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-8F15A4B8-2566-49FB-97AF-A4D87D20422C)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_LISTING_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-E2BDD2FA-F3C9-447D-A347-51BD07DF2650)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_LISTING_REVISION_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-2E38AB6C-9EF2-4D9E-9D0E-2D026DC66FEC)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_LISTING_REVISION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-E699394F-AA0E-4AB5-B2C2-B0522997B9C5)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_LISTING_REVISION_PACKAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-3BA3DBF7-9F88-4A69-AD31-8763FFE49747)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_RELATED_DOCUMENT_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-6719840B-318A-45AC-B931-2427F02C3B46)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_SCREEN_SHOT_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-28B99E69-BD0B-4FCB-8A4C-338589895FB1)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_TERM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-C0D3EA3F-C0E5-435A-95BA-B0F03116C576)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_TERM_VERSION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-370F4030-DC56-4A4D-8B90-15381BEEAA5F)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_UPDATE_VIDEO_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-2E66B794-199C-4E85-90ED-7A654F9C90A5)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_VIDEO_ATTACHMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-2ECF98B7-C528-48C1-A161-01B0A1F1C1FF)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-463E7897-C2A8-4A4B-9B92-0E64598756BA)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-4F8C95C4-9E2B-4499-A936-946633A6CE06)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-1C9DB200-FFCD-4BFB-B230-2EC8E38ABE4C)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-4DFB7732-C09A-4F06-81D1-EEBE6E3B5DBF)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-969C7A0F-7953-45DB-9052-41641F670A0E)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-E554D50D-8143-4E01-9DCD-A6772BD20ADD)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-B6BF53D8-423D-490A-9B88-55627B1A3D32)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-6B6BAE99-13B1-49E8-A04B-DEA3458D9361)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-304EE814-79F4-4089-BFEA-F5BD8C48FA1D)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-36318563-74F1-4415-AD14-D25AC9D656C2)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-8BA6E74B-FCD6-43AF-BF19-C93A161F30C1)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_publisher_t.html#ADSDK-GUID-9E7F32ED-F6E9-486F-9CF3-47F173FEFF34)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
