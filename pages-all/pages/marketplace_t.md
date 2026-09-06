# Marketplace Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html
- Fetched: 2026-09-05 19:18 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#dcoc-content-body)

## Marketplace Common Types

### DBMS_CLOUD_OCI_MARKETPLACE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_ACCEPTED_AGREEMENT_T Type

The model for an accepted terms of use agreement.

Syntax
```

```

Fields

Field Description

`id`

(optional) The unique identifier for the acceptance of the agreement within a specific compartment.

`display_name`

(optional) A display name for the accepted agreement.

`compartment_id`

(optional) The unique identifier for the compartment where the agreement was accepted.

`listing_id`

(optional) The unique identifier for the listing associated with the agreement.

`package_version`

(optional) The package version associated with the agreement.

`agreement_id`

(optional) The unique identifier for the terms of use agreement itself.

`time_accepted`

(optional) The time the agreement was accepted.

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_MARKETPLACE_ACCEPTED_AGREEMENT_SUMMARY_T Type

The model for a summary of an accepted agreement.

Syntax
```

```

Fields

Field Description

`id`

(optional) The unique identifier for the acceptance of the agreement within a specific compartment.

`display_name`

(optional) A display name for the accepted agreement.

`compartment_id`

(optional) The unique identifier for the compartment where the agreement was accepted.

`listing_id`

(optional) The unique identifier for the listing associated with the agreement.

`package_version`

(optional) The package version associated with the agreement.

`agreement_id`

(optional) The unique identifier for the terms of use agreement itself.

`time_accepted`

(optional) The time the agreement was accepted.

### DBMS_CLOUD_OCI_MARKETPLACE_AGREEMENT_T Type

The model for an end user license agreement.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier for the agreement.

`content_url`

(required) The content URL of the agreement.

`signature`

(required) A time-based signature that can be used to accept an agreement or remove a previously accepted agreement from the list that Marketplace checks before a deployment.

`compartment_id`

(optional) The unique identifier for the compartment.

`author`

(optional) Who authored the agreement.

Allowed values are: 'ORACLE', 'PARTNER'

`prompt`

(optional) Textual prompt to read and accept the agreement.

### DBMS_CLOUD_OCI_MARKETPLACE_AGREEMENT_SUMMARY_T Type

The model for a summary of an end user license agreement.

Syntax
```

```

Fields

Field Description

`id`

(optional) The unique identifier for the agreement.

`content_url`

(optional) The content URL of the agreement.

`author`

(optional) Who authored the agreement.

Allowed values are: 'ORACLE', 'PARTNER', 'PII'

`prompt`

(optional) Textual prompt to read and accept the agreement.

### DBMS_CLOUD_OCI_MARKETPLACE_CATEGORY_SUMMARY_T Type

The model for a summary of product categories for listings.

Syntax
```

```

Fields

Field Description

`name`

(optional) Name of the product category.

### DBMS_CLOUD_OCI_MARKETPLACE_CHANGE_PUBLICATION_COMPARTMENT_DETAILS_T Type

The model for the parameters needed move a publication from one compartment to another.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to move the publication.

### DBMS_CLOUD_OCI_MARKETPLACE_INTERNATIONAL_MARKET_PRICE_T Type

The model for international market pricing.

Syntax
```

```

Fields

Field Description

`currency_code`

(required) The currency of the pricing model.

Allowed values are: 'USD', 'CAD', 'INR', 'GBP', 'BRL', 'JPY', 'OMR', 'EUR', 'CHF', 'MXN', 'CLP'

`currency_symbol`

(optional) The symbol of the currency

`rate`

(required) The pricing rate.

### DBMS_CLOUD_OCI_MARKETPLACE_PRICING_MODEL_T Type

The model for pricing.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of the pricing model.

Allowed values are: 'FREE', 'BYOL', 'PAYGO'

`pay_go_strategy`

(optional) The type of pricing for a PAYGO model, eg PER_OCPU_LINEAR, PER_OCPU_MIN_BILLING, PER_INSTANCE. Null if type is not PAYGO.

Allowed values are: 'PER_OCPU_LINEAR', 'PER_OCPU_MIN_BILLING', 'PER_INSTANCE', 'PER_INSTANCE_MONTHLY_INCLUSIVE'

`currency`

(optional) The currency of the pricing model.

Allowed values are: 'USD', 'CAD', 'INR', 'GBP', 'BRL', 'JPY', 'OMR', 'EUR', 'CHF', 'MXN', 'CLP'

`rate`

(optional) The pricing rate.

`international_market_price`

(optional)

### DBMS_CLOUD_OCI_MARKETPLACE_OPERATING_SYSTEM_T Type

The operating system used by the listing.

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of the operating system.

### DBMS_CLOUD_OCI_MARKETPLACE_ITEM_T Type

The model for an item within an array of filter values.

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of the item.

`code`

(optional) A code assigned to the item.

### DBMS_CLOUD_OCI_MARKETPLACE_ITEM_TBL Type

Nested table type of dbms_cloud_oci_marketplace_item_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_REGION_T Type

The model for regions supported by a listing and package.

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of the region.

`code`

(optional) The code of the region.

`countries`

(optional) Countries in the region.

### DBMS_CLOUD_OCI_MARKETPLACE_REGION_TBL Type

Nested table type of dbms_cloud_oci_marketplace_region_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_LISTING_PACKAGE_T Type

A base object for all types of listing packages.

Syntax
```

```

Fields

Field Description

`description`

(optional) Description of this package.

`listing_id`

(required) The ID of the listing this package belongs to.

`version`

(required) The package version.

`package_type`

(required) The specified package's type.

Allowed values are: 'ORCHESTRATION', 'IMAGE', 'CONTAINER', 'KUBERNETES'

`pricing`

(optional)

`resource_id`

(optional) The unique identifier for the package resource.

`time_created`

(optional) The date and time this listing package was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`operating_system`

(optional)

`regions`

(optional) The regions where you can deploy the listing package. (Some packages have restrictions that limit their deployment to United States regions only.)

### DBMS_CLOUD_OCI_MARKETPLACE_CONTAINER_LISTING_PACKAGE_T Type

A listing package for container.

Syntax
```

```

`dbms_cloud_oci_marketplace_container_listing_package_t`is a subtype of the`dbms_cloud_oci_marketplace_listing_package_t`type.

### DBMS_CLOUD_OCI_MARKETPLACE_CREATE_ACCEPTED_AGREEMENT_DETAILS_T Type

The model for the parameters needed to accept a terms of use agreement.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A display name for the accepted agreement.

`compartment_id`

(required) The unique identifier for the compartment where the agreement will be accepted.

`listing_id`

(required) The unique identifier for the listing associated with the agreement.

`package_version`

(required) The package version associated with the agreement.

`agreement_id`

(required) The agreement to accept.

`signature`

(required) A signature generated for the listing package agreements that you can retrieve with[GetAgreement](https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/Agreement/GetAgreement).

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_MARKETPLACE_EULA_T Type

A base object for all types of end user license agreements.

Syntax
```

```

Fields

Field Description

`eula_type`

(required) The end user license agreement's type.

Allowed values are: 'TEXT'

### DBMS_CLOUD_OCI_MARKETPLACE_EULA_TBL Type

Nested table type of dbms_cloud_oci_marketplace_eula_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_CREATE_PUBLICATION_PACKAGE_T Type

A base object for creating a publication package.

Syntax
```

```

Fields

Field Description

`package_version`

(required) The package version.

`package_type`

(required) The package's type.

Allowed values are: 'ORCHESTRATION', 'IMAGE', 'CONTAINER', 'KUBERNETES'

`operating_system`

(required)

`eula`

(required) The end user license agreeement (EULA) that consumers of this listing must accept.

### DBMS_CLOUD_OCI_MARKETPLACE_CREATE_IMAGE_PUBLICATION_PACKAGE_T Type

An object for creating an image publication package.

Syntax
```

```

`dbms_cloud_oci_marketplace_create_image_publication_package_t`is a subtype of the`dbms_cloud_oci_marketplace_create_publication_package_t`type.

Fields

Field Description

`image_id`

(optional) The unique identifier for the base image of the publication.

### DBMS_CLOUD_OCI_MARKETPLACE_SUPPORT_CONTACT_T Type

Contact information to use to get support.

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of the contact.

`phone`

(optional) The phone number of the contact.

`email`

(optional) The email of the contact.

`subject`

(optional) The email subject line to use when contacting support.

### DBMS_CLOUD_OCI_MARKETPLACE_SUPPORT_CONTACT_TBL Type

Nested table type of dbms_cloud_oci_marketplace_support_contact_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_CREATE_PUBLICATION_DETAILS_T Type

The model for the parameters needed to create a publication.

Syntax
```

```

Fields

Field Description

`listing_type`

(required) The publisher category to which the publication belongs. The publisher category informs where the listing appears for use.

Allowed values are: 'COMMUNITY', 'PARTNER', 'PRIVATE'

`name`

(required) The name of the publication, which is also used in the listing.

`short_description`

(required) A short description of the publication to use in the listing.

`long_description`

(optional) A long description of the publication to use in the listing.

`support_contacts`

(required) Contact information for getting support from the publisher for the listing.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create the publication.

`package_details`

(required)

`is_agreement_acknowledged`

(required) Whether the publisher acknowledged that they have the right and authority to share the contents of the publication and that they accepted the Oracle terms of use agreements required to create a publication.

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_MARKETPLACE_DOCUMENTATION_LINK_T Type

A link to a documentation resource on the internet.

Syntax
```

```

Fields

Field Description

`name`

(optional) Text that describes the resource.

`url`

(optional) The URL of the resource.

`document_category`

(optional) The category that the document belongs to.

### DBMS_CLOUD_OCI_MARKETPLACE_ERROR_ENTITY_T Type

The model for the error entity.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_MARKETPLACE_EXPORT_PACKAGE_DETAILS_T Type

The model for the parameters needed to export a listing.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to export container image or helm chart.

`container_repository_path`

(required) The repository path (/Content/General/Concepts/identifiers.htm) of the container reposistory where the container image or helm chart should be exported.

### DBMS_CLOUD_OCI_MARKETPLACE_SEARCH_LISTINGS_DETAILS_T Type

A base request type that contains common criteria for Marketplace Search Listings details.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of SearchDetails, whether FreeText or Structured.

Allowed values are: 'FreeText', 'Structured'

`matching_context_type`

(optional) The type of matching context returned in the response. If you specify HIGHLIGHTS, then the service will highlight fragments in its response. The default value is NONE.

Allowed values are: 'NONE', 'HIGHLIGHTS'

### DBMS_CLOUD_OCI_MARKETPLACE_FREE_TEXT_SEARCH_DETAILS_T Type

A request containing arbitrary text that must be present in the Marketplace Applications.

Syntax
```

```

`dbms_cloud_oci_marketplace_free_text_search_details_t`is a subtype of the`dbms_cloud_oci_marketplace_search_listings_details_t`type.

Fields

Field Description

`text`

(required) The text to search for.

### DBMS_CLOUD_OCI_MARKETPLACE_IMAGE_LISTING_PACKAGE_T Type

A package for image listings.

Syntax
```

```

`dbms_cloud_oci_marketplace_image_listing_package_t`is a subtype of the`dbms_cloud_oci_marketplace_listing_package_t`type.

Fields

Field Description

`app_catalog_listing_id`

(optional) The ID of the listing resource associated with this listing package. For more information, see[AppCatalogListing](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogListing/)in the Core Services API.

`app_catalog_listing_resource_version`

(optional) The resource version of the listing resource associated with this listing package.

`image_id`

(optional) The ID of the image corresponding to the package.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLICATION_PACKAGE_T Type

A base object for all types of publication packages.

Syntax
```

```

Fields

Field Description

`description`

(optional) A description of the package.

`listing_id`

(required) The ID of the listing that the specified package belongs to.

`version`

(required) The package version.

`package_type`

(required) The specified package's type.

Allowed values are: 'ORCHESTRATION', 'IMAGE', 'CONTAINER', 'KUBERNETES'

`resource_id`

(optional) The unique identifier for the package resource.

`time_created`

(optional) The date and time the publication package was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`operating_system`

(optional)

### DBMS_CLOUD_OCI_MARKETPLACE_IMAGE_PUBLICATION_PACKAGE_T Type

A publication package for image publications.

Syntax
```

```

`dbms_cloud_oci_marketplace_image_publication_package_t`is a subtype of the`dbms_cloud_oci_marketplace_publication_package_t`type.

Fields

Field Description

`app_catalog_listing_id`

(optional) The ID of the listing resource associated with this publication package. For more information, see[AppCatalogListing](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogListing/)in the Core Services API.

`app_catalog_listing_resource_version`

(optional) The resource version of the listing resource associated with this publication package.

`image_id`

(optional) The ID of the image that corresponds to the package.

### DBMS_CLOUD_OCI_MARKETPLACE_KUBERNETES_LISTING_PACKAGE_T Type

A listing package for kubernetes.

Syntax
```

```

`dbms_cloud_oci_marketplace_kubernetes_listing_package_t`is a subtype of the`dbms_cloud_oci_marketplace_listing_package_t`type.

### DBMS_CLOUD_OCI_MARKETPLACE_LAUNCH_ELIGIBILITY_T Type

Tenant eligibility and other information for launching a PIC image

Syntax
```

```

Fields

Field Description

`image_id`

(required) PIC Image ID

`is_launch_allowed`

(required) Is the tenant permitted to launch the PIC image

`meters`

(optional) related meters for the PIC image

`ineligibility_reason`

(optional) Reason the account is ineligible to launch paid listings

Allowed values are: 'INELIGIBLE_ACCOUNT_COUNTRY', 'INELIGIBLE_REGION', 'INELIGIBLE_ACCOUNT_BLACKLISTED', 'INELIGIBLE_ACCOUNT_FEATURE_DISABLED', 'INELIGIBLE_ACCOUNT_CURRENCY', 'INELIGIBLE_ACCOUNT_NOT_PAID', 'INELIGIBLE_ACCOUNT_INTERNAL', 'INELIGIBLE_ACCOUNT_GOV_SUBSCRIPTION', 'INELIGIBLE_PAID_LISTING_THROTTLED', 'INELIGIBLE_ACCOUNT_NOT_AVAILABLE', 'INELIGIBLE_ACCOUNT_NOT_MONTHLY_INCLUSIVE', 'IMAGE_META_DATA_SO', 'INELIGIBLE_ACCOUNT_TENANCY_NOT_ALLOWED_ACCESS_IMAGE', 'INELIGIBLE_ACCOUNT_GOV_LAUNCH_NON_GOV_LISTING', 'AGREEMENT_NOT_ACCEPTED', 'NOT_AUTHORIZED', 'ELIGIBLE'

### DBMS_CLOUD_OCI_MARKETPLACE_LINK_T Type

The model for links.

Syntax
```

```

Fields

Field Description

`rel`

(optional) Reference links to the previous page, next page, and other pages.

Allowed values are: 'SELF', 'CANONICAL', 'NEXT', 'TEMPLATE', 'PREV'

`href`

(optional) The anchor tag.

### DBMS_CLOUD_OCI_MARKETPLACE_UPLOAD_DATA_T Type

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

`file_extension`

(optional) The file extension of the upload data.

### DBMS_CLOUD_OCI_MARKETPLACE_LINK_TBL Type

Nested table type of dbms_cloud_oci_marketplace_link_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_T Type

The model for a publisher.

Syntax
```

```

Fields

Field Description

`id`

(optional) Unique identifier for the publisher.

`name`

(optional) The name of the publisher.

`description`

(optional) A description of the publisher.

`year_founded`

(optional) The year the publisher's company or organization was founded.

`website_url`

(optional) The publisher's website.

`contact_email`

(optional) The email address of the publisher.

`contact_phone`

(optional) The phone number of the publisher.

`hq_address`

(optional) The address of the publisher's headquarters.

`logo`

(optional)

`links`

(optional) Reference links.

### DBMS_CLOUD_OCI_MARKETPLACE_SCREENSHOT_T Type

The model for a listing's screenshot.

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of the screenshot.

`description`

(optional) A description of the screenshot.

`content_url`

(optional) The content URL of the screenshot.

`mime_type`

(optional) The MIME type of the screenshot.

`file_extension`

(optional) The file extension of the screenshot.

### DBMS_CLOUD_OCI_MARKETPLACE_NAMED_LINK_T Type

A link to a resource on the internet.

Syntax
```

```

Fields

Field Description

`name`

(optional) Text that describes the resource.

`url`

(optional) The URL of the resource.

### DBMS_CLOUD_OCI_MARKETPLACE_SCREENSHOT_TBL Type

Nested table type of dbms_cloud_oci_marketplace_screenshot_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_NAMED_LINK_TBL Type

Nested table type of dbms_cloud_oci_marketplace_named_link_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_DOCUMENTATION_LINK_TBL Type

Nested table type of dbms_cloud_oci_marketplace_documentation_link_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_OPERATING_SYSTEM_TBL Type

Nested table type of dbms_cloud_oci_marketplace_operating_system_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_LISTING_T Type

The model for an Oracle Cloud Infrastructure Marketplace listing.

Syntax
```

```

Fields

Field Description

`id`

(optional) The unique identifier for the listing in Marketplace.

`name`

(optional) The name of the listing.

`version`

(optional) The version of the listing.

`tagline`

(optional) The tagline of the listing.

`keywords`

(optional) Keywords associated with the listing.

`short_description`

(optional) A short description of the listing.

`usage_information`

(optional) Usage information for the listing.

`long_description`

(optional) A long description of the listing.

`license_model_description`

(optional) A description of the publisher's licensing model for the listing.

`system_requirements`

(optional) System requirements for the listing.

`time_released`

(optional) The release date of the listing.

`release_notes`

(optional) Release notes for the listing.

`categories`

(optional) Categories that the listing belongs to.

`publisher`

(optional)

`languages`

(optional) Languages supported by the listing.

`screenshots`

(optional) Screenshots of the listing.

`videos`

(optional) Videos of the listing.

`support_contacts`

(optional) Contact information to use to get support from the publisher for the listing.

`support_links`

(optional) Links to support resources for the listing.

`documentation_links`

(optional) Links to additional documentation provided by the publisher specifically for the listing.

`icon`

(optional)

`banner`

(optional)

`compatible_architectures`

(optional) The list of compatible architectures supported by the listing

Allowed values are: 'X86', 'ARM'

`regions`

(optional) The regions where you can deploy the listing. (Some listings have restrictions that limit their deployment to United States regions only.)

`package_type`

(optional) The listing's package type.

Allowed values are: 'ORCHESTRATION', 'IMAGE', 'CONTAINER', 'KUBERNETES'

`default_package_version`

(optional) The default package version.

`links`

(optional) Links to reference material.

`is_featured`

(optional) Indicates whether the listing is included in Featured Listings.

`listing_type`

(optional) The publisher category to which the listing belongs. The publisher category informs where the listing appears for use.

Allowed values are: 'COMMUNITY', 'PARTNER', 'PRIVATE'

`supported_operating_systems`

(optional) List of operating systems supported by the listing.

### DBMS_CLOUD_OCI_MARKETPLACE_LISTING_PACKAGE_SUMMARY_T Type

The model for a summary of a package.

Syntax
```

```

Fields

Field Description

`listing_id`

(optional) The ID of the listing that the specified package belongs to.

`package_version`

(optional) The version of the specified package.

`package_type`

(optional) The specified package's type.

Allowed values are: 'ORCHESTRATION', 'IMAGE', 'CONTAINER', 'KUBERNETES'

`pricing`

(optional)

`regions`

(optional) The regions where you can deploy the listing package. (Some packages have restrictions that limit their deployment to United States regions only.)

`resource_id`

(optional) The unique identifier for the package resource.

`time_created`

(optional) The date and time this listing package was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_SUMMARY_T Type

Summary details about the publisher of the listing.

Syntax
```

```

Fields

Field Description

`id`

(optional) The unique identifier for the publisher.

`name`

(optional) The name of the publisher.

`description`

(optional) A description of the publisher.

### DBMS_CLOUD_OCI_MARKETPLACE_LISTING_SUMMARY_T Type

The model for a summary of an Oracle Cloud Infrastructure Marketplace listing.

Syntax
```

```

Fields

Field Description

`id`

(optional) The unique identifier for the listing in Marketplace.

`name`

(optional) The name of the listing.

`short_description`

(optional) A short description of the listing.

`is_rover_exportable`

(optional) True if this application is Rover exportable

`tagline`

(optional) The tagline of the listing.

`icon`

(optional)

`package_type`

(optional) The listing's package type.

Allowed values are: 'ORCHESTRATION', 'IMAGE', 'CONTAINER', 'KUBERNETES'

`pricing_types`

(optional) Summary of the pricing types available across all packages in the listing.

Allowed values are: 'FREE', 'BYOL', 'PAYGO'

`compatible_architectures`

(optional) The list of compatible architectures supported by the listing

Allowed values are: 'X86', 'ARM'

`regions`

(optional) The regions where you can deploy the listing. (Some listings have restrictions that limit their deployment to United States regions only.)

`is_featured`

(optional) Indicates whether the listing is featured.

`categories`

(optional) Product categories that the listing belongs to.

`publisher`

(optional)

`supported_operating_systems`

(optional) The list of operating systems supported by the listing.

`listing_type`

(optional) The publisher category to which the listing belongs. The publisher category informs where the listing appears for use.

Allowed values are: 'COMMUNITY', 'PARTNER', 'PRIVATE'

### DBMS_CLOUD_OCI_MARKETPLACE_ORCHESTRATION_VARIABLE_T Type

The model of a variable for an orchestration resource.

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of the variable.

`default_value`

(optional) The variable's default value.

`description`

(optional) A description of the variable.

`data_type`

(optional) The data type of the variable.

Allowed values are: 'STRING', 'INTEGER'

`is_mandatory`

(optional) Whether the variable is mandatory.

`hint_message`

(optional) A brief textual description that helps to explain the variable.

### DBMS_CLOUD_OCI_MARKETPLACE_ORCHESTRATION_VARIABLE_TBL Type

Nested table type of dbms_cloud_oci_marketplace_orchestration_variable_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_ORCHESTRATION_LISTING_PACKAGE_T Type

A listing package for orchestration.

Syntax
```

```

`dbms_cloud_oci_marketplace_orchestration_listing_package_t`is a subtype of the`dbms_cloud_oci_marketplace_listing_package_t`type.

Fields

Field Description

`resource_link`

(optional) Link to the orchestration resource.

`variables`

(optional) List of variables for the orchestration resource.

### DBMS_CLOUD_OCI_MARKETPLACE_ORCHESTRATION_PUBLICATION_PACKAGE_T Type

A publication package for stack publications.

Syntax
```

```

`dbms_cloud_oci_marketplace_orchestration_publication_package_t`is a subtype of the`dbms_cloud_oci_marketplace_publication_package_t`type.

Fields

Field Description

`resource_link`

(optional) A link to the stack resource.

`variables`

(optional) A list of variables for the stack resource.

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLICATION_T Type

The model for an Oracle Cloud Infrastructure Marketplace publication.

Syntax
```

```

Fields

Field Description

`lifecycle_state`

(optional) The lifecycle state of the publication.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where the publication exists.

`id`

(required) The unique identifier for the publication in Marketplace.

`name`

(required) The name of the publication, which is also used in the listing.

`short_description`

(optional) A short description of the publication to use in the listing.

`long_description`

(optional) A long description of the publication to use in the listing.

`support_contacts`

(optional) Contact information for getting support from the publisher for the listing.

`icon`

(optional)

`package_type`

(optional) The listing's package type.

Allowed values are: 'ORCHESTRATION', 'IMAGE', 'CONTAINER', 'KUBERNETES'

`listing_type`

(required) The publisher category to which the publication belongs. The publisher category informs where the listing appears for use.

Allowed values are: 'COMMUNITY', 'PARTNER', 'PRIVATE'

`supported_operating_systems`

(optional) The list of operating systems supprted by the listing.

`time_created`

(optional) The date and time the publication was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLICATION_PACKAGE_SUMMARY_T Type

The model for a summary of a publication package.

Syntax
```

```

Fields

Field Description

`listing_id`

(required) The ID of the listing that the specified package belongs to.

`package_version`

(required) The version of the specified package.

`package_type`

(required) The specified package's type.

Allowed values are: 'ORCHESTRATION', 'IMAGE', 'CONTAINER', 'KUBERNETES'

`resource_id`

(required) The unique identifier for the package resource.

`time_created`

(optional) The date and time the publication package was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_MARKETPLACE_PUBLICATION_SUMMARY_T Type

The model for a summary of an Oracle Cloud Infrastructure publication.

Syntax
```

```

Fields

Field Description

`lifecycle_state`

(required) The lifecycle state of the publication.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where the publication exists.

`id`

(required) The unique identifier for the publication in Marketplace.

`name`

(required) The name of the publication, which is also used in the listing.

`short_description`

(optional) A short description of the publication to use in the listing.

`icon`

(optional)

`package_type`

(optional) The listing's package type.

Allowed values are: 'ORCHESTRATION', 'IMAGE', 'CONTAINER', 'KUBERNETES'

`supported_operating_systems`

(optional) The list of operating systems supported by the listing.

`listing_type`

(required) The publisher category to which the publication belongs. The publisher category informs where the listing appears for use.

Allowed values are: 'COMMUNITY', 'PARTNER', 'PRIVATE'

`time_created`

(optional) The date and time the publication was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_MARKETPLACE_REPORT_SUMMARY_T Type

The model of a single report.

Syntax
```

```

Fields

Field Description

`report_type`

(required) The type of report.

`l_date`

(required) The date of the report.

`l_columns`

(required) The columns in the report.

`content`

(required) The contents of the report in comma-separated values (CSV) file format.

### DBMS_CLOUD_OCI_MARKETPLACE_REPORT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_marketplace_report_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_REPORT_COLLECTION_T Type

A collection of reports that match the parameters of the request.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of reports.

### DBMS_CLOUD_OCI_MARKETPLACE_REPORT_TYPE_SUMMARY_T Type

The model of the description of a report.

Syntax
```

```

Fields

Field Description

`report_type`

(optional) The type of report.

`name`

(optional) The name of the report.

`description`

(optional) A description of the report.

`l_columns`

(optional) The columns in the report.

### DBMS_CLOUD_OCI_MARKETPLACE_REPORT_TYPE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_marketplace_report_type_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_REPORT_TYPE_COLLECTION_T Type

A collection of report types.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of report types.

### DBMS_CLOUD_OCI_MARKETPLACE_STRUCTURED_SEARCH_DETAILS_T Type

A request that uses Search's structured query language to specify filter conditions to apply to search listings. For more information about writing search queries, see[Search Language Syntax](https://docs.oracle.com/iaas/Content/Search/Concepts/querysyntax.htm).

Syntax
```

```

`dbms_cloud_oci_marketplace_structured_search_details_t`is a subtype of the`dbms_cloud_oci_marketplace_search_listings_details_t`type.

Fields

Field Description

`query`

(required) The structured query describing which resources to search for.

### DBMS_CLOUD_OCI_MARKETPLACE_TAX_SUMMARY_T Type

Tax implication that current tenant may be eligible while using specific listing

Syntax
```

```

Fields

Field Description

`code`

(required) Unique code for the tax.

`name`

(optional) Name of the tax code.

`country`

(optional) Country, which imposes the tax.

`url`

(optional) The URL with more details about this tax.

### DBMS_CLOUD_OCI_MARKETPLACE_TEXT_BASED_EULA_T Type

An end user license agreement that is provided as text.

Syntax
```

```

`dbms_cloud_oci_marketplace_text_based_eula_t`is a subtype of the`dbms_cloud_oci_marketplace_eula_t`type.

Fields

Field Description

`license_text`

(optional) The text of the end user license agreement.

### DBMS_CLOUD_OCI_MARKETPLACE_THIRD_PARTY_PAID_LISTING_ELIGIBILITY_T Type

Tenant eligibility for using third party paid listings

Syntax
```

```

Fields

Field Description

`is_paid_listing_eligible`

(required) Whether the tenant is permitted to use paid listings

`is_paid_listing_throttled`

(required) Whether the tenant is currently prevented from using paid listings because of throttling

`eligibility_reason`

(required) Reason the account is ineligible to launch paid listings

Allowed values are: 'ELIGIBLE', 'INELIGIBLE_ACCOUNT_COUNTRY', 'INELIGIBLE_REGION', 'INELIGIBLE_ACCOUNT_BLACKLISTED', 'INELIGIBLE_ACCOUNT_FEATURE_DISABLED', 'INELIGIBLE_ACCOUNT_CURRENCY', 'INELIGIBLE_ACCOUNT_NOT_PAID', 'INELIGIBLE_ACCOUNT_INTERNAL', 'INELIGIBLE_ACCOUNT_GOV_SUBSCRIPTION', 'NOT_AUTHORIZED'

### DBMS_CLOUD_OCI_MARKETPLACE_UPDATE_ACCEPTED_AGREEMENT_DETAILS_T Type

The model for the parameters needed to update an accepted terms of use agreement.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A display name for the accepted agreement.

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_MARKETPLACE_UPDATE_PUBLICATION_DETAILS_T Type

The model for the parameters needed to update a publication.

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of the publication, which is also used in the listing.

`short_description`

(optional) A short description of the publication to use in the listing.

`long_description`

(optional) A long description of the publication to use in the listing.

`support_contacts`

(optional) Contact information for getting support from the publisher for the listing.

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_MARKETPLACE_WORK_REQUEST_RESOURCE_T Type

Details about the resource entity.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way in which this resource was affected by the work tracked by the work request. A resource being created, updated, or deleted remains in the `IN_PROGRESS` state until work is complete for that resource. At that point, the resource transitions to the `CREATED`, `UPDATED`, or `DELETED` state.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'NEEDS_ATTENTION', 'FAILED', 'SUCCEEDED', 'CANCELED'

`identifier`

(required) The resource identifier the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata

`metadata`

(optional) Additional information about the resource.

### DBMS_CLOUD_OCI_MARKETPLACE_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_marketplace_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_WORK_REQUEST_T Type

A description of workrequest

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'EXPORT_LISTING'

`status`

(required) The current status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED'

`id`

(required) The OCID of the work request.

`compartment_id`

(required) The OCID of the compartment that contains the work request.

`resources`

(optional) The resources affected by this work request.

`percent_complete`

(required) How much progress the operation has made.

`time_accepted`

(required) Date and time the work was accepted, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_started`

(optional) Date and time the work started, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_finished`

(optional) Date and time the work completed, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`listing_id`

(optional) The listing id associated with the work request.

`package_version`

(optional) The package version associated with the work request.

### DBMS_CLOUD_OCI_MARKETPLACE_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'EXPORT_LISTING'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED'

`id`

(required) The id of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects.

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

`listing_id`

(optional) The listing id associated with the work request.

`package_version`

(optional) The package version associated with the work request.

### DBMS_CLOUD_OCI_MARKETPLACE_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_marketplace_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_WORK_REQUEST_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestSummary objects.

### DBMS_CLOUD_OCI_MARKETPLACE_WORK_REQUEST_ERROR_T Type

Details about errors encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occurred. Error codes are listed (https://docs.cloud.oracle.com/Content/API/References/apierrors.htm)

`message`

(required) A human-readable error string.

`l_timestamp`

(required) Date and time the error happened, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_MARKETPLACE_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_marketplace_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_WORK_REQUEST_ERROR_COLLECTION_T Type

A list of work request errors that match filter criteria, if any. Results contain `WorkRequestError` objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A collection of work request errors.

### DBMS_CLOUD_OCI_MARKETPLACE_WORK_REQUEST_LOG_ENTRY_T Type

Details about the log entity.

Syntax
```

```

Fields

Field Description

`message`

(required) A human-readable string.

`l_timestamp`

(required) Date and time the log was written, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_MARKETPLACE_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_marketplace_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MARKETPLACE_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

A list of work request logs that match filter criteria, if any. Results contain `WorkRequestLogEntry` objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A collection of work request log entries.

- [Marketplace Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-DB23649A-D3BD-4B72-88E3-05E7D49C82CA)
- [DBMS_CLOUD_OCI_MARKETPLACE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-F5161A27-0A1A-4077-B118-7EBB0AFC3EC5)
- [DBMS_CLOUD_OCI_MARKETPLACE_ACCEPTED_AGREEMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-414DC5F3-57A5-43F7-ACA0-0E0FA0228BB4)
- [DBMS_CLOUD_OCI_MARKETPLACE_ACCEPTED_AGREEMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-747DC427-EA8A-496C-95FF-F469AD787D82)
- [DBMS_CLOUD_OCI_MARKETPLACE_AGREEMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-886CFC6C-E901-442E-B1BA-2BD18ECEE371)
- [DBMS_CLOUD_OCI_MARKETPLACE_AGREEMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-9C2CA08C-7392-45FE-9EC8-61F5BB9F7757)
- [DBMS_CLOUD_OCI_MARKETPLACE_CATEGORY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-B177C9C7-4796-48D9-9F74-F79C79B428E1)
- [DBMS_CLOUD_OCI_MARKETPLACE_CHANGE_PUBLICATION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-5480E5F5-7970-4C8F-9E9B-CDE93DC399E0)
- [DBMS_CLOUD_OCI_MARKETPLACE_INTERNATIONAL_MARKET_PRICE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-AE1DF180-5CA1-47DF-B520-64F730E9A3CD)
- [DBMS_CLOUD_OCI_MARKETPLACE_PRICING_MODEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-7996A6CB-5C70-451F-BC83-8AB7AAD2EA1F)
- [DBMS_CLOUD_OCI_MARKETPLACE_OPERATING_SYSTEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-521D6261-70F3-4D39-9AB9-13B96F7A8106)
- [DBMS_CLOUD_OCI_MARKETPLACE_ITEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-0C62FB0D-2870-48F4-AC11-CE5C6CF9B4AE)
- [DBMS_CLOUD_OCI_MARKETPLACE_ITEM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-3014B94D-CE44-43AA-B3F0-515BC3847DFA)
- [DBMS_CLOUD_OCI_MARKETPLACE_REGION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-8F44374D-0711-4B6B-A827-A6CC06656374)
- [DBMS_CLOUD_OCI_MARKETPLACE_REGION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-53421B0D-01FB-4381-B4FE-23079BC88605)
- [DBMS_CLOUD_OCI_MARKETPLACE_LISTING_PACKAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-291922F5-B680-489E-ABC0-15C2091846DB)
- [DBMS_CLOUD_OCI_MARKETPLACE_CONTAINER_LISTING_PACKAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-A56B821C-F9DF-4539-BDEC-D17F2A9B4883)
- [DBMS_CLOUD_OCI_MARKETPLACE_CREATE_ACCEPTED_AGREEMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-3698DD7B-D628-48B4-9669-570ABFC97125)
- [DBMS_CLOUD_OCI_MARKETPLACE_EULA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-2E8CF4CD-6812-4A71-884F-9CE1AC9A5A47)
- [DBMS_CLOUD_OCI_MARKETPLACE_EULA_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-450421C5-E60A-49B7-A03E-23FBB3EF3690)
- [DBMS_CLOUD_OCI_MARKETPLACE_CREATE_PUBLICATION_PACKAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-CDB4AD69-5477-4186-9CCE-08BF26F8C76D)
- [DBMS_CLOUD_OCI_MARKETPLACE_CREATE_IMAGE_PUBLICATION_PACKAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-5DDE4C18-4E27-4776-BD78-16C9D865B7F0)
- [DBMS_CLOUD_OCI_MARKETPLACE_SUPPORT_CONTACT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-B423857B-DB09-412D-9D99-E06298D8A499)
- [DBMS_CLOUD_OCI_MARKETPLACE_SUPPORT_CONTACT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-2242A075-B454-4A9B-B484-93C03671829F)
- [DBMS_CLOUD_OCI_MARKETPLACE_CREATE_PUBLICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-C3BCF70B-2C8F-4F80-B31A-5B7C61B893FE)
- [DBMS_CLOUD_OCI_MARKETPLACE_DOCUMENTATION_LINK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-11238067-B377-459A-9E50-F48F51A064D5)
- [DBMS_CLOUD_OCI_MARKETPLACE_ERROR_ENTITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-5ED1C2A5-4B50-49F2-B83E-36D2114FB5CE)
- [DBMS_CLOUD_OCI_MARKETPLACE_EXPORT_PACKAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-BD032F13-1285-4A7D-BDF9-153189CCBCAA)
- [DBMS_CLOUD_OCI_MARKETPLACE_SEARCH_LISTINGS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-D027F6B3-E198-4AA0-A158-CA8FD28BDBC8)
- [DBMS_CLOUD_OCI_MARKETPLACE_FREE_TEXT_SEARCH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-2C84F6CF-44DA-41C3-890F-F34F4BF19B29)
- [DBMS_CLOUD_OCI_MARKETPLACE_IMAGE_LISTING_PACKAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-1B79CD6C-7496-43DE-BE08-A83D046385B8)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLICATION_PACKAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-99C34EE8-8DB9-478C-B8AB-5D7663273D32)
- [DBMS_CLOUD_OCI_MARKETPLACE_IMAGE_PUBLICATION_PACKAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-77B838ED-8F4A-41EC-85FC-B3943C39CCEE)
- [DBMS_CLOUD_OCI_MARKETPLACE_KUBERNETES_LISTING_PACKAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-3C5B36C7-1C13-4263-9794-EBD0C9F3EE34)
- [DBMS_CLOUD_OCI_MARKETPLACE_LAUNCH_ELIGIBILITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-3311C268-7C9E-4F31-A27E-8DC285A0021E)
- [DBMS_CLOUD_OCI_MARKETPLACE_LINK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-3C3EE113-293A-489B-8829-5B6E2D82A057)
- [DBMS_CLOUD_OCI_MARKETPLACE_UPLOAD_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-CB92FAD3-9C71-4F41-96E9-F3315468127B)
- [DBMS_CLOUD_OCI_MARKETPLACE_LINK_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-F245DB40-5285-4829-BC68-6E46FF374640)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-FE50AF75-EE80-4F87-8960-CBF2EAFFC68E)
- [DBMS_CLOUD_OCI_MARKETPLACE_SCREENSHOT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-23FDA77C-91B6-4B53-89B0-48CB73732C1B)
- [DBMS_CLOUD_OCI_MARKETPLACE_NAMED_LINK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-FC3D19FD-0538-4F9B-B1D6-386F06BCD407)
- [DBMS_CLOUD_OCI_MARKETPLACE_SCREENSHOT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-F4F70664-46DE-480B-8ED5-BD65481AAA9C)
- [DBMS_CLOUD_OCI_MARKETPLACE_NAMED_LINK_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-F22A409B-93BE-43DC-9289-A8C6F5640762)
- [DBMS_CLOUD_OCI_MARKETPLACE_DOCUMENTATION_LINK_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-E7EEA6FC-BF23-4EB3-A613-173A12487340)
- [DBMS_CLOUD_OCI_MARKETPLACE_OPERATING_SYSTEM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-8D315D6A-82F1-4E7B-B477-5E4F3DAA1416)
- [DBMS_CLOUD_OCI_MARKETPLACE_LISTING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-634F35C1-CB5A-4D01-AE66-5B9FB0D87FC1)
- [DBMS_CLOUD_OCI_MARKETPLACE_LISTING_PACKAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-F36B09F1-BFC8-49E5-95F0-7B32357FD956)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLISHER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-D0B587CD-9EF9-4241-B8C0-F6A52A35AA49)
- [DBMS_CLOUD_OCI_MARKETPLACE_LISTING_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-BF456128-7AA4-43FD-A4CC-4BC55BEBB5E3)
- [DBMS_CLOUD_OCI_MARKETPLACE_ORCHESTRATION_VARIABLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-D211D6E6-5642-4DC3-A8FA-C8B9C7C68353)
- [DBMS_CLOUD_OCI_MARKETPLACE_ORCHESTRATION_VARIABLE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-DF199FC6-6A32-424F-B15E-B2FC87ADD0EE)
- [DBMS_CLOUD_OCI_MARKETPLACE_ORCHESTRATION_LISTING_PACKAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-23A9113D-37D1-47FD-B762-E9A0802A06F0)
- [DBMS_CLOUD_OCI_MARKETPLACE_ORCHESTRATION_PUBLICATION_PACKAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-CA676781-5026-4325-A9D7-7B2B1372C860)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLICATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-5C9944B5-9CED-469D-A0A2-CF2F613E4CAE)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLICATION_PACKAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-344B46C9-59E5-4430-A04E-A7D16560145F)
- [DBMS_CLOUD_OCI_MARKETPLACE_PUBLICATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-48B89717-10DF-40AC-9885-B16D1C035483)
- [DBMS_CLOUD_OCI_MARKETPLACE_REPORT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-7DF77C49-0BF1-46D3-B89D-0451FCEC255C)
- [DBMS_CLOUD_OCI_MARKETPLACE_REPORT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-E58D9324-D9D8-48EF-8F2C-10384265BC05)
- [DBMS_CLOUD_OCI_MARKETPLACE_REPORT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-0B3DDFC0-D678-4B7D-90B8-EC2F29E81653)
- [DBMS_CLOUD_OCI_MARKETPLACE_REPORT_TYPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-2354BC39-73CD-4895-99FB-A132A380B2DA)
- [DBMS_CLOUD_OCI_MARKETPLACE_REPORT_TYPE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-572093BC-693C-49E9-BD29-9220F403E00C)
- [DBMS_CLOUD_OCI_MARKETPLACE_REPORT_TYPE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-8DBC2E2A-B3C1-43E4-B495-2EB1C70EF75A)
- [DBMS_CLOUD_OCI_MARKETPLACE_STRUCTURED_SEARCH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-DEBE1645-DD79-4CEB-A219-804EC3FCF6C1)
- [DBMS_CLOUD_OCI_MARKETPLACE_TAX_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-4B6875B1-BD17-4AF2-93A1-BE5D5C51EB63)
- [DBMS_CLOUD_OCI_MARKETPLACE_TEXT_BASED_EULA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-AD71F99D-816A-45A3-9AA4-134121B20499)
- [DBMS_CLOUD_OCI_MARKETPLACE_THIRD_PARTY_PAID_LISTING_ELIGIBILITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-21E95903-E698-41F3-9B14-873E1797472A)
- [DBMS_CLOUD_OCI_MARKETPLACE_UPDATE_ACCEPTED_AGREEMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-47DB86DC-2ACB-4DA6-A194-7D9CF16B5802)
- [DBMS_CLOUD_OCI_MARKETPLACE_UPDATE_PUBLICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-BC08472F-D59C-44F9-80F6-6254FF1CB436)
- [DBMS_CLOUD_OCI_MARKETPLACE_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-DB888264-CC41-40ED-A32B-B7156DF0C110)
- [DBMS_CLOUD_OCI_MARKETPLACE_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-74EAFB51-4FC8-4F58-8565-190BF3CE5FC7)
- [DBMS_CLOUD_OCI_MARKETPLACE_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-7FC1DA5C-41C2-4AFC-935E-021228CEDED6)
- [DBMS_CLOUD_OCI_MARKETPLACE_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-63BE0E62-97B7-4167-9C54-0A0BB8C92B64)
- [DBMS_CLOUD_OCI_MARKETPLACE_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-CBDDC6B4-AD98-4B2F-95ED-95F5071415FE)
- [DBMS_CLOUD_OCI_MARKETPLACE_WORK_REQUEST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-9A440778-D020-47B8-BC77-7E6217587AAB)
- [DBMS_CLOUD_OCI_MARKETPLACE_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-7122CD1A-3092-4624-A0BF-82AEAF401332)
- [DBMS_CLOUD_OCI_MARKETPLACE_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-BC4D58F9-B47D-456F-9B9F-3C4F19084E94)
- [DBMS_CLOUD_OCI_MARKETPLACE_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-0A9DE7F4-4DDD-4AAD-8183-BA631DD76CF7)
- [DBMS_CLOUD_OCI_MARKETPLACE_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-C6F00B8B-589A-4534-B350-41DF82993AAC)
- [DBMS_CLOUD_OCI_MARKETPLACE_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-CF8576FF-F70D-4478-8805-D0DEAE6ADD7B)
- [DBMS_CLOUD_OCI_MARKETPLACE_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/marketplace_t.html#ADSDK-GUID-EA56278A-BA87-4913-83C7-3D87DDE8DBCE)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
