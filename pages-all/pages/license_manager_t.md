# License Manager Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html
- Fetched: 2026-09-05 19:17 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#dcoc-content-body)

## License Manager Common Types

### DBMS_CLOUD_OCI_LICENSE_MANAGER_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_LICENSE_MANAGER_BULK_UPLOAD_CELL_INFO_T Type

Error information corresponding to each column that was required but was invalid.

Syntax
```

```

Fields

Field Description

`column_index`

(required) Column index as in the given bulk upload file.

`error_info`

(required) Error information corresponding to a particular column.

### DBMS_CLOUD_OCI_LICENSE_MANAGER_BULK_UPLOAD_FAILED_RECORD_INFO_T Type

Error information for a valid license record that could not be uploaded.

Syntax
```

```

Fields

Field Description

`row_number`

(required) Refers to the license record number as provided in the bulk upload file.

`product_name`

(required) Product name of the failed row.

`error`

(required) Failed license record error information.

### DBMS_CLOUD_OCI_LICENSE_MANAGER_BULK_UPLOAD_LICENSE_RECORDS_DETAILS_T Type

Details required for bulk uploading of license records.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)where license records are created.

`file_name`

(required) Name of the file that is being uploaded.

`file_content`

(required) The file to be uploaded.

### DBMS_CLOUD_OCI_LICENSE_MANAGER_BULK_UPLOAD_CELL_INFO_TBL Type

Nested table type of dbms_cloud_oci_license_manager_bulk_upload_cell_info_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LICENSE_MANAGER_BULK_UPLOAD_VALIDATION_ERROR_INFO_T Type

Detailed error information corresponding to each column for a particular supported license record that could not be uploaded.

Syntax
```

```

Fields

Field Description

`row_number`

(required) Refers to the license record number as provided in the bulk upload file.

`product_name`

(required) Product name of invalid row.

`row_error`

(required) Error information corresponding to each column.

### DBMS_CLOUD_OCI_LICENSE_MANAGER_BULK_UPLOAD_VALIDATION_ERROR_INFO_TBL Type

Nested table type of dbms_cloud_oci_license_manager_bulk_upload_validation_error_info_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LICENSE_MANAGER_BULK_UPLOAD_FAILED_RECORD_INFO_TBL Type

Nested table type of dbms_cloud_oci_license_manager_bulk_upload_failed_record_info_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LICENSE_MANAGER_BULK_UPLOAD_RESPONSE_T Type

The bulk upload response.

Syntax
```

```

Fields

Field Description

`total_supported_records`

(required) The number of license records which were supported.

`total_supported_records_saved`

(required) The number of supported license records that were uploaded successfully.

`total_supported_duplicate_records`

(required) The number of supported license records that were valid but not uploaded since they were duplicates.

`total_supported_failed_license_records`

(required) The number of supported license records that were valid but failed with errors during upload.

`total_supported_invalid_records`

(required) The number of supported license records that could not be uploaded since they were invalid.

`validation_error_info`

(required) Detailed error information corresponding to each supported but invalid row for the uploaded file.

`failed_license_record_info`

(required) Error information corresponding to the supported records which are valid but could not be created.

`message`

(required) Response message for bulk upload.

### DBMS_CLOUD_OCI_LICENSE_MANAGER_BULK_UPLOAD_TEMPLATE_T Type

The bulk upload template file.

Syntax
```

```

Fields

Field Description

`template`

(required) The bulk upload template.

### DBMS_CLOUD_OCI_LICENSE_MANAGER_CONFIGURATION_T Type

Details of the compartment-specific configuration.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)to which the configuration is specified.

`email_ids`

(required) The list of associated configuration email IDs.

`time_created`

(optional) The time the configuration was created. An[RFC 3339](https://tools.ietf.org/html/rfc3339)-formatted datetime string.

`time_updated`

(optional) The time the configuration was updated. An[RFC 3339](https://tools.ietf.org/html/rfc3339)-formatted datetime string.

### DBMS_CLOUD_OCI_LICENSE_MANAGER_CREATE_LICENSE_RECORD_DETAILS_T Type

The details about the new license record.

Syntax
```

```

Fields

Field Description

`display_name`

(required) License record name.

`is_perpetual`

(required) Specifies if the license record term is perpertual.

`expiration_date`

(optional) The license record end date in[RFC 3339](https://tools.ietf.org/html/rfc3339)date format. Example: `2018-09-12`

`support_end_date`

(optional) The license record support end date in[RFC 3339](https://tools.ietf.org/html/rfc3339)date format. Example: `2018-09-12`

`is_unlimited`

(required) Specifies if the license count is unlimited.

`license_count`

(optional) The number of license units added by a user in a license record. Default 1

`product_id`

(optional) The license record product ID.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_LICENSE_MANAGER_IMAGE_DETAILS_T Type

Image details associated with the product license.

Syntax
```

```

Fields

Field Description

`listing_id`

(required) Marketplace image listing ID.

`package_version`

(required) Image package version.

### DBMS_CLOUD_OCI_LICENSE_MANAGER_IMAGE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_license_manager_image_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LICENSE_MANAGER_CREATE_PRODUCT_LICENSE_DETAILS_T Type

Details for creating a new product license.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)where product licenses are created.

`is_vendor_oracle`

(required) Specifies if the product license vendor is Oracle or a third party.

`display_name`

(required) Name of the product license.

`license_unit`

(required) The product license unit.

Allowed values are: 'OCPU', 'NAMED_USER_PLUS', 'PROCESSORS'

`vendor_name`

(optional) The product license vendor name, for example: Microsoft, RHEL, and so on.

`images`

(optional) The image details associated with the product license.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_LICENSE_MANAGER_ERROR_T Type

An error has occurred.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_LICENSE_MANAGER_IMAGE_RESPONSE_T Type

The collection of image details for the product license.

Syntax
```

```

Fields

Field Description

`id`

(optional) The image ID associated with the product license.

`listing_name`

(optional) The listing name associated with the product license.

`publisher`

(optional) The image publisher.

`listing_id`

(optional) The image listing ID.

`package_version`

(optional) The image package version.

### DBMS_CLOUD_OCI_LICENSE_MANAGER_LICENSE_METRIC_T Type

Overview of product license and resources usage.

Syntax
```

```

Fields

Field Description

`total_product_license_count`

(required) Total number of product licenses in a particular compartment.

`total_byol_instance_count`

(required) Total number of BYOL instances in a particular compartment.

`total_license_included_instance_count`

(required) Total number of License Included (LI) instances in a particular compartment.

`license_record_expiring_soon_count`

(required) Total number of license records that will expire within 90 days in a particular compartment.

### DBMS_CLOUD_OCI_LICENSE_MANAGER_LICENSE_RECORD_T Type

License record summary.

Syntax
```

```

Fields

Field Description

`id`

(required) The license record[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`product_license_id`

(optional) The product license[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)with which the license record is associated.

`compartment_id`

(optional) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)where the license record is created.

`display_name`

(required) The license record display name. Avoid entering confidential information.

`product_id`

(optional) The license record product ID.

`license_count`

(optional) The number of license units added by the user for the given license record. Default 1

`expiration_date`

(optional) The license record end date in[RFC 3339](https://tools.ietf.org/html/rfc3339)date format. Example: `2018-09-12`

`support_end_date`

(optional) The license record support end date in[RFC 3339](https://tools.ietf.org/html/rfc3339)date format. Example: `2018-09-12`

`is_unlimited`

(required) Specifies if the license count is unlimited.

`is_perpetual`

(required) Specifies if the license record term is perpertual.

`time_created`

(optional) The time the license record was created. An[RFC 3339](https://tools.ietf.org/html/rfc3339)-formatted datetime string.

`time_updated`

(optional) The time the license record was updated. An[RFC 3339](https://tools.ietf.org/html/rfc3339)-formatted datetime string.

`lifecycle_state`

(required) The current license record state.

Allowed values are: 'ACTIVE', 'INACTIVE', 'DELETED'

`license_unit`

(optional) The product license unit.

Allowed values are: 'OCPU', 'NAMED_USER_PLUS', 'PROCESSORS'

`product_license`

(optional) The product license name with which the license record is associated.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_LICENSE_MANAGER_LICENSE_RECORD_SUMMARY_T Type

The license record summary.

Syntax
```

```

Fields

Field Description

`id`

(required) The license record[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`product_license_id`

(optional) The product license[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)with which the license record is associated.

`compartment_id`

(optional) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)where the license record is created.

`display_name`

(required) License record display name. Avoid entering confidential information.

`product_id`

(optional) The license record product ID.

`license_count`

(optional) The number of license record units added by the user for the given license record. Default 1

`expiration_date`

(optional) The license record end date in[RFC 3339](https://tools.ietf.org/html/rfc3339)format. date format. Example: `2018-09-12`

`support_end_date`

(optional) The license record support end date in[RFC 3339](https://tools.ietf.org/html/rfc3339)format. date format. Example: `2018-09-12`

`is_unlimited`

(required) Specifies if the license count is unlimited.

`is_perpetual`

(required) Specifies if the license record term is perpertual.

`time_created`

(optional) The time the license record was created. An[RFC 3339](https://tools.ietf.org/html/rfc3339)-formatted datetime string.

`time_updated`

(optional) The time the license record was updated. An[RFC 3339](https://tools.ietf.org/html/rfc3339)-formatted datetime string.

`lifecycle_state`

(optional) The current license record state.

Allowed values are: 'ACTIVE', 'INACTIVE', 'DELETED'

`license_unit`

(optional) The product license unit.

Allowed values are: 'OCPU', 'NAMED_USER_PLUS', 'PROCESSORS'

`product_license`

(optional) The product license name with which the license record is associated.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_LICENSE_MANAGER_LICENSE_RECORD_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_license_manager_license_record_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LICENSE_MANAGER_LICENSE_RECORD_COLLECTION_T Type

The license record summary collection.

Syntax
```

```

Fields

Field Description

`items`

(required) The license record summary collection.

### DBMS_CLOUD_OCI_LICENSE_MANAGER_PRODUCT_T Type

Details of product.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the product.

`l_count`

(required) Units required for the missing product.

`category`

(required) Product category base or option.

Allowed values are: 'BASE', 'OPTION'

### DBMS_CLOUD_OCI_LICENSE_MANAGER_IMAGE_RESPONSE_TBL Type

Nested table type of dbms_cloud_oci_license_manager_image_response_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LICENSE_MANAGER_PRODUCT_LICENSE_T Type

The product license details.

Syntax
```

```

Fields

Field Description

`id`

(required) The product license[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)where the product license is created.

`status`

(required) The current product license status.

Allowed values are: 'INCOMPLETE', 'ISSUES_FOUND', 'WARNING', 'OK'

`status_description`

(optional) Status description for the current product license status.

`total_active_license_unit_count`

(optional) The total number of licenses available for the product license, calculated by adding up all the license counts for active license records associated with the product license.

`lifecycle_state`

(optional) The current product license state.

Allowed values are: 'ACTIVE', 'INACTIVE', 'DELETED'

`total_license_units_consumed`

(optional) The number of license units consumed. Updated after each allocation run.

`total_license_record_count`

(optional) The number of license records associated with the product license.

`active_license_record_count`

(optional) The number of active license records associated with the product license.

`license_unit`

(required) The product license unit.

Allowed values are: 'OCPU', 'NAMED_USER_PLUS', 'PROCESSORS'

`is_vendor_oracle`

(required) Specifies whether the vendor is Oracle or a third party.

`is_over_subscribed`

(optional) Specifies whether or not the product license is oversubscribed.

`is_unlimited`

(optional) Specifies if the license unit count is unlimited.

`display_name`

(required) License record name

`vendor_name`

(optional) The vendor of the ProductLicense

`time_created`

(optional) The time the product license was created. An[RFC 3339](https://tools.ietf.org/html/rfc3339)-formatted datetime string.

`time_updated`

(optional) The time the product license was updated. An[RFC 3339](https://tools.ietf.org/html/rfc3339)-formatted datetime string.

`images`

(optional) The images associated with the product license.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_LICENSE_MANAGER_PRODUCT_LICENSE_SUMMARY_T Type

The product license summary.

Syntax
```

```

Fields

Field Description

`id`

(required) The product license[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)where the product license is created.

`status`

(required) The current product license status.

Allowed values are: 'INCOMPLETE', 'ISSUES_FOUND', 'WARNING', 'OK'

`status_description`

(optional) Status description for the current product license status.

`lifecycle_state`

(optional) The current product license state.

Allowed values are: 'ACTIVE', 'INACTIVE', 'DELETED'

`total_active_license_unit_count`

(optional) The total number of licenses available for the product license, calculated by adding up all the license counts for active license records associated with the product license.

`total_license_units_consumed`

(optional) The number of license units consumed. Updated after each allocation run.

`total_license_record_count`

(optional) The number of license records associated with the product license.

`active_license_record_count`

(optional) The number of active license records associated with the product license.

`license_unit`

(required) The product license unit.

Allowed values are: 'OCPU', 'NAMED_USER_PLUS', 'PROCESSORS'

`is_vendor_oracle`

(required) Specifies whether the vendor is Oracle or a third party.

`is_over_subscribed`

(optional) Specifies whether or not the product license is oversubscribed.

`is_unlimited`

(optional) Specifies if the license unit count is unlimited.

`display_name`

(required) License record name

`vendor_name`

(optional) The vendor of the ProductLicense

`time_created`

(optional) The time the product license was created. An[RFC 3339](https://tools.ietf.org/html/rfc3339)-formatted datetime string.

`time_updated`

(optional) The time the product license was updated. An[RFC 3339](https://tools.ietf.org/html/rfc3339)-formatted datetime string.

`images`

(optional) The images associated with the product license.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_LICENSE_MANAGER_PRODUCT_LICENSE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_license_manager_product_license_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LICENSE_MANAGER_PRODUCT_LICENSE_COLLECTION_T Type

The product license summary collection.

Syntax
```

```

Fields

Field Description

`items`

(required) The product license summary collection.

### DBMS_CLOUD_OCI_LICENSE_MANAGER_PRODUCT_TBL Type

Nested table type of dbms_cloud_oci_license_manager_product_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LICENSE_MANAGER_PRODUCT_LICENSE_CONSUMER_SUMMARY_T Type

Details of a resource that is consuming a particular product license.

Syntax
```

```

Fields

Field Description

`resource_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`resource_name`

(required) The display name of the resource.

`product_name`

(required) The resource product name.

`resource_compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the resource.

`resource_compartment_name`

(required) The display name of the compartment that contains the resource.

`resource_unit_type`

(required) The unit type for the resource.

Allowed values are: 'OCPU', 'ECPU'

`resource_unit_count`

(required) Number of units of the resource

`license_unit_type`

(required) The product license unit.

Allowed values are: 'OCPU', 'NAMED_USER_PLUS', 'PROCESSORS'

`license_units_consumed`

(required) Number of license units consumed by the resource.

`is_base_license_available`

(required) Specifies if the base license is available.

`are_all_options_available`

(required) Specifies if all options are available.

`missing_products`

(required) Collection of missing product licenses.

### DBMS_CLOUD_OCI_LICENSE_MANAGER_PRODUCT_LICENSE_CONSUMER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_license_manager_product_license_consumer_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LICENSE_MANAGER_PRODUCT_LICENSE_CONSUMER_COLLECTION_T Type

Collection of resources which have consumed licenses.

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of product license consumers.

### DBMS_CLOUD_OCI_LICENSE_MANAGER_TOP_UTILIZED_PRODUCT_LICENSE_SUMMARY_T Type

A summary of the top utilized product licenses.

Syntax
```

```

Fields

Field Description

`product_license_id`

(required) The product license[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`product_type`

(required) The product type.

`unit_type`

(required) The product license unit.

Allowed values are: 'OCPU', 'NAMED_USER_PLUS', 'PROCESSORS'

`total_units_consumed`

(required) Number of license units consumed.

`total_license_unit_count`

(required) Total number of license units in the product license provided by the user.

`is_unlimited`

(required) Specifies if the license unit count is unlimited.

`status`

(required) The current product license status.

Allowed values are: 'INCOMPLETE', 'ISSUES_FOUND', 'WARNING', 'OK'

### DBMS_CLOUD_OCI_LICENSE_MANAGER_TOP_UTILIZED_PRODUCT_LICENSE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_license_manager_top_utilized_product_license_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LICENSE_MANAGER_TOP_UTILIZED_PRODUCT_LICENSE_COLLECTION_T Type

A collection of top utilized product licenses.

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of top utilized product licenses.

### DBMS_CLOUD_OCI_LICENSE_MANAGER_TOP_UTILIZED_RESOURCE_SUMMARY_T Type

A summary of a top utlized resource.

Syntax
```

```

Fields

Field Description

`resource_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`resource_name`

(required) Resource canonical name.

`resource_compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)that contains the resource.

`resource_compartment_name`

(required) The display name of the compartment that contains the resource.

`total_units`

(required) Number of license units consumed by the resource.

`unit_type`

(required) The resource unit.

Allowed values are: 'OCPU', 'ECPU'

### DBMS_CLOUD_OCI_LICENSE_MANAGER_TOP_UTILIZED_RESOURCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_license_manager_top_utilized_resource_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LICENSE_MANAGER_TOP_UTILIZED_RESOURCE_COLLECTION_T Type

The collection of top utilized resources.

Syntax
```

```

Fields

Field Description

`items`

(required) The top utilized resource summary collection.

### DBMS_CLOUD_OCI_LICENSE_MANAGER_UPDATE_CONFIGURATION_DETAILS_T Type

The compartment-specific configuration.

Syntax
```

```

Fields

Field Description

`email_ids`

(required) List of email IDs associated with the configuration.

### DBMS_CLOUD_OCI_LICENSE_MANAGER_UPDATE_LICENSE_RECORD_DETAILS_T Type

The details about updates in the license record.

Syntax
```

```

Fields

Field Description

`display_name`

(required) License record name.

`is_perpetual`

(required) Specifies if the license record term is perpertual.

`expiration_date`

(optional) The license record end date in[RFC 3339](https://tools.ietf.org/html/rfc3339)date format. Example: `2018-09-12`

`support_end_date`

(optional) The license record support end date in[RFC 3339](https://tools.ietf.org/html/rfc3339)date format. Example: `2018-09-12`

`is_unlimited`

(required) Specifies if the license count is unlimited.

`license_count`

(optional) The number of license units added by a user in a license record. Default 1

`product_id`

(optional) The license record product ID.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_LICENSE_MANAGER_UPDATE_PRODUCT_LICENSE_DETAILS_T Type

Updates the product license object (only allows image updates).

Syntax
```

```

Fields

Field Description

`images`

(required) The image details associated with the product license.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

- [License Manager Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-2C494213-EDC7-4CCC-B011-1209BC2E44D5)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-B382C82B-CD2D-4F80-866D-BE1C6FE01509)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_BULK_UPLOAD_CELL_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-7F976874-458F-4571-BC08-291703B8FEF4)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_BULK_UPLOAD_FAILED_RECORD_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-1911E51B-7A6B-4583-A7F6-A8859161519E)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_BULK_UPLOAD_LICENSE_RECORDS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-77C05D0D-F3D7-4FD6-AA09-01CB54F4CC1B)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_BULK_UPLOAD_CELL_INFO_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-5B2A280B-D28B-48B3-A8C2-7ADA1C4C4081)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_BULK_UPLOAD_VALIDATION_ERROR_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-9FC90BC1-B137-48D0-BC7A-9FD1A8E36256)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_BULK_UPLOAD_VALIDATION_ERROR_INFO_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-D01B285B-E95B-45AE-B203-1EE861C236F4)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_BULK_UPLOAD_FAILED_RECORD_INFO_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-0E0FC504-6E06-4107-9252-9B621FDCE927)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_BULK_UPLOAD_RESPONSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-A837C06F-4459-4C04-8CE7-977CD0AFBA30)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_BULK_UPLOAD_TEMPLATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-9FAEB735-06B0-4FD2-BF65-BADBE1463C29)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-EC32BAE3-1A5E-480E-BF48-E1A9C73B9B1D)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_CREATE_LICENSE_RECORD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-2C36A51F-0969-42E2-8F47-68F92994115F)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_IMAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-89E604CD-41EB-4326-980C-5E9556CC5E18)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_IMAGE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-13CA7CB4-8826-4E86-AE45-18A87EE9B332)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_CREATE_PRODUCT_LICENSE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-4E880024-3B2A-4A84-9E07-77F9D8E0DD42)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-77802800-2AB9-458C-B413-0F494B19E69B)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_IMAGE_RESPONSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-86B3D7E1-C2F9-46E8-B4C3-5CE123E00157)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_LICENSE_METRIC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-EC82E7CC-CB88-40F1-AF52-166A84910389)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_LICENSE_RECORD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-346AF4EC-DD7C-47E1-939D-36BCDFCF2DEB)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_LICENSE_RECORD_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-140288B1-F47F-448A-A996-4101584246BC)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_LICENSE_RECORD_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-1D0F9837-DA1D-4566-AFF1-0C2EB57B9318)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_LICENSE_RECORD_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-71B57C52-0ADA-4659-A249-F62CD5D2798A)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_PRODUCT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-82AD3191-776B-4175-BC03-00FBD2782845)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_IMAGE_RESPONSE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-EFE89E4F-5445-4149-84BA-3B54736A4FCC)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_PRODUCT_LICENSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-56C8EE98-D784-4242-A4F0-947BEF9C6EE1)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_PRODUCT_LICENSE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-877C100B-04B8-47DF-BB38-D0BA012B7028)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_PRODUCT_LICENSE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-B3ACA93B-BF89-4999-A745-7E4A6DF82779)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_PRODUCT_LICENSE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-112E8C2D-827F-48F7-B59E-EAC2FAAF7EF6)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_PRODUCT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-383D6623-F7D6-4359-A6F3-66957CB9CDC1)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_PRODUCT_LICENSE_CONSUMER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-2763E08E-914C-4CDE-AA92-B76A524D419E)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_PRODUCT_LICENSE_CONSUMER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-18FF6AB3-18E8-4835-88C6-69687DADFD7F)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_PRODUCT_LICENSE_CONSUMER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-BFEFAB1B-1415-4854-A95A-2AAD434A17D5)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_TOP_UTILIZED_PRODUCT_LICENSE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-C9D04AEB-AEDC-4674-BFA2-F31FDBDDB524)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_TOP_UTILIZED_PRODUCT_LICENSE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-C13E545A-26FA-4B0E-8262-0BC4D06C3FA7)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_TOP_UTILIZED_PRODUCT_LICENSE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-913A668A-C019-46D4-8837-91EB0EE09FC9)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_TOP_UTILIZED_RESOURCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-42441399-3301-4CB1-A5EC-BEE7E32E54CF)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_TOP_UTILIZED_RESOURCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-8D968727-E660-44E3-BD17-894DE1691635)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_TOP_UTILIZED_RESOURCE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-0AC3B89B-DA4C-4821-8D09-B50025B0566D)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_UPDATE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-2D9729A0-DD95-454D-8435-EC3CD2128410)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_UPDATE_LICENSE_RECORD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-E4547A90-FEBD-477E-94F5-C216F4797D92)
- [DBMS_CLOUD_OCI_LICENSE_MANAGER_UPDATE_PRODUCT_LICENSE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/license_manager_t.html#ADSDK-GUID-2BAA0F53-A173-4248-8558-B6AA112B86C0)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
