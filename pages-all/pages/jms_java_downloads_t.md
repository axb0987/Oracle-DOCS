# Java Downloads Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html
- Fetched: 2026-09-05 19:17 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#dcoc-content-body)

## Java Downloads Common Types

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_CREATE_JAVA_DOWNLOAD_REPORT_DETAILS_T Type

Attributes to create a Java download report.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)here should be the tenancy OCID.

`time_start`

(optional) The start time from when download records have to be included (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_end`

(optional) The end time until when the download records have to be included (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`sort_by`

(optional) The property to be used for sorting the reports.

Allowed values are: 'timeDownloaded', 'downloadSourceId', 'downloadType'

`sort_order`

(optional) The sort order for the reports.

Allowed values are: 'ASC', 'DESC'

`format`

(required) The format of the report that is generated.

Allowed values are: 'CSV'

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_CREATE_JAVA_DOWNLOAD_TOKEN_DETAILS_T Type

The attributes to create a new JavaDownloadToken.

Syntax
```

```

Fields

Field Description

`display_name`

(required) User provided display name of the JavaDownloadToken.

`description`

(required) User provided description of the JavaDownloadToken.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tenancy scoped to the JavaDownloadToken.

`is_default`

(optional) The token default attribute.

`time_expires`

(required) Expiry time of the token.

`java_version`

(required) The Java version associated with the token.

`license_type`

(required) The license type(s) associated with the JavaDownloadToken.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`. (See[Managing Tags and Tag Namespaces](https://docs.oracle.com/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm).)

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See[Understanding Free-form Tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm)).

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_CREATE_JAVA_LICENSE_ACCEPTANCE_RECORD_DETAILS_T Type

The attributes to create a new JavaLicenseAcceptanceRecord.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The tenancy[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user accepting the license.

`license_type`

(required) License type for the Java version.

Allowed values are: 'OTN', 'NFTC', 'RESTRICTED'

`license_acceptance_status`

(required) Status of license acceptance.

Allowed values are: 'ACCEPTED', 'REVOKED'

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_DOWNLOAD_URL_T Type

Download Url object for the Java artifact.

Syntax
```

```

Fields

Field Description

`download_url`

(required) The URL for downloading the artifact.

`download_url_type`

(required) The type of download URL.

Allowed values are: 'OSS', 'CDN'

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_ERROR_T Type

An error code and message from an API request failure.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that describes the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_GENERATE_ARTIFACT_DOWNLOAD_URL_DETAILS_T Type

The attributes to generate a DownloadUrl for a Java runtime artifact.

Syntax
```

```

Fields

Field Description

`artifact_id`

(required) Unique identifier for the Java runtime artifact.

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_COUNT_AGGREGATION_T Type

Count of Java downloads aggregated by the specified type.

Syntax
```

```

Fields

Field Description

`download_count`

(required) Count of Java downloads.

`family_version`

(optional) The Java family version.

`family_display_name`

(optional) The Java family display name.

`release_version`

(optional) The Java release version. Applicable only to `JAVA_RELEASE` aggregationType.

`os_family`

(optional) The target Operating System family for the artifact. Applicable only to `PLATFORM` aggregationType.

`architecture`

(optional) The target Operating System architecture for the artifact. Applicable only to `PLATFORM` aggregationType.

`package_type`

(optional) The package type(typically the file extension) of the artifact. Applicable only to `PLATFORM` aggregationType.

`package_type_detail`

(optional) Additional information about the package type. Applicable only to `PLATFORM` aggregationType.

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_COUNT_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_jms_java_downloads_java_download_count_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_COUNT_AGGREGATION_COLLECTION_T Type

Collection of download count aggregations.

Syntax
```

```

Fields

Field Description

`aggregation_type`

(required) Aggregation type

Allowed values are: 'JAVA_FAMILY', 'JAVA_RELEASE', 'PLATFORM'

`items`

(required) A list of download count aggregations.

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_RECORD_T Type

A record of Java artifact download in a tenancy.

Syntax
```

```

Fields

Field Description

`family_version`

(optional) The Java family version identifier.

`family_display_name`

(optional) The Java family display name.

`release_version`

(optional) The Java release version identifier.

`os_family`

(optional) The target Operating System family for the artifact.

`architecture`

(optional) The target Operating System architecture for the artifact.

`package_type`

(optional) The package type(typically the file extension) of the artifact.

`package_type_detail`

(optional) Additional information about the package type.

`download_source_id`

(required) Identifier of the source that downloaded the artifact.

`time_downloaded`

(required) Timestamp of download.

`download_type`

(required) Type of download.

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_RECORD_SUMMARY_T Type

A summary of Java artifact download in a tenancy.

Syntax
```

```

Fields

Field Description

`family_version`

(optional) The Java family version identifier.

`family_display_name`

(optional) The Java family display name.

`release_version`

(optional) The Java release version identifier.

`os_family`

(optional) The target Operating System family for the artifact.

`architecture`

(optional) The target Operating System architecture for the artifact.

`package_type`

(optional) The package type(typically the file extension) of the artifact.

`package_type_detail`

(optional) Additional information about the package type.

`download_source_id`

(required) Identifier of the source that downloaded the artifact.

`time_downloaded`

(required) Timestamp of download.

`download_type`

(required) Type of download.

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_RECORD_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_jms_java_downloads_java_download_record_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_RECORD_COLLECTION_T Type

Collection of Java download records.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of Java download records in a tenancy.

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_PRINCIPAL_T Type

An authorized principal.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the principal.

`display_name`

(optional) The name of the principal.

`email`

(optional) The email of the principal.

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_REPORT_T Type

Details about a Java download report in a tenancy. The report is a file in Object Storage. It contains the download records in a specific format.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Java download report.

`display_name`

(required) Display name for the Java download report.

`format`

(required) The file format of the Java download report.

Allowed values are: 'CSV'

`file_size_in_bytes`

(required) Approximate size of the Java download report file in bytes.

`checksum_type`

(required) The algorithm used for calculating the checksum.

Allowed values are: 'SHA256'

`checksum_value`

(required) The checksum value of the Java download report file.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tenancy scoped to the Java download report.

`created_by`

(required)

`time_created`

(required) The time the Java download report was created. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the Java download report.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'NEEDS_ATTENTION', 'UPDATING'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`. (See[Managing Tags and Tag Namespaces](https://docs.oracle.com/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm).)

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See[Understanding Free-form Tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm)).

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_REPORT_SUMMARY_T Type

A summary of the Java download report in a tenancy.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Java download report.

`display_name`

(required) Display name for the Java download report.

`format`

(required) The file format of the Java download report.

Allowed values are: 'CSV'

`file_size_in_bytes`

(required) Approximate size of the Java download report file in bytes.

`checksum_type`

(required) The algorithm used for calculating the checksum.

Allowed values are: 'SHA256'

`checksum_value`

(required) The checksum value of the Java download report file.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tenancy scoped to the Java download report.

`created_by`

(required)

`time_created`

(required) The time the Java download report was created. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the Java download report.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'NEEDS_ATTENTION', 'UPDATING'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`. (See[Managing Tags and Tag Namespaces](https://docs.oracle.com/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm).)

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See[Understanding Free-form Tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm)).

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_REPORT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_jms_java_downloads_java_download_report_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_REPORT_COLLECTION_T Type

Collection of JavaDownloadReportSummary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of JavaDownloadReportSummary objects in a tenancy.

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_TOKEN_T Type

A JavaDownloadToken is a primary resource for the script friendly URLs. The value of this token serves as the authorization token for the download.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the JavaDownloadToken.

`display_name`

(required) User provided display name of the JavaDownloadToken.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tenancy scoped to the JavaDownloadToken.

`created_by`

(required)

`last_updated_by`

(optional)

`description`

(required) User provided description of the JavaDownloadToken.

`value`

(required) Uniquely generated value for the JavaDownloadToken.

`time_created`

(required) The time the JavaDownloadToken was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the JavaDownloadToken was updated. An RFC3339 formatted datetime string.

`time_last_used`

(optional) The time the JavaDownloadToken was last used for download. An RFC3339 formatted datetime string.

`time_expires`

(required) The expiry time of the JavaDownloadToken. An RFC3339 formatted datetime string.

`java_version`

(required) The associated Java version of the JavaDownloadToken.

`license_type`

(optional) The license type(s) associated with the JavaDownloadToken.

`is_default`

(optional) A flag to indicate if the token is default.

`lifecycle_state`

(required) The current state of the JavaDownloadToken.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'NEEDS_ATTENTION', 'UPDATING'

`lifecycle_details`

(optional) Possible lifecycle substates.

Allowed values are: 'EXPIRED', 'REVOKING', 'REVOKED'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`. (See[Managing Tags and Tag Namespaces](https://docs.oracle.com/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm).)

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See[Understanding Free-form Tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm)).

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_TOKEN_SUMMARY_T Type

Summary of the JavaDownloadToken.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the JavaDownloadToken.

`display_name`

(required) User provided display name of the JavaDownloadToken.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tenancy scoped to the JavaDownloadToken.

`created_by`

(required)

`last_updated_by`

(optional)

`description`

(required) User provided description of the JavaDownloadToken.

`value`

(required) Uniquely generated value for the JavaDownloadToken.

`time_created`

(required) The time the JavaDownloadToken was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the JavaDownloadToken was updated. An RFC3339 formatted datetime string.

`time_last_used`

(optional) The time the JavaDownloadToken was last used for download. An RFC3339 formatted datetime string.

`time_expires`

(required) The expiry time of the JavaDownloadToken. An RFC3339 formatted datetime string.

`java_version`

(required) The associated Java version of the JavaDownloadToken.

`license_type`

(optional) The license type(s) associated with the JavaDownloadToken.

`is_default`

(optional) A flag to indicate if the token is default.

`lifecycle_state`

(required) The current state of the JavaDownloadToken.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'NEEDS_ATTENTION', 'UPDATING'

`lifecycle_details`

(optional) Possible lifecycle substates.

Allowed values are: 'EXPIRED', 'REVOKING', 'REVOKED'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`. (See[Managing Tags and Tag Namespaces](https://docs.oracle.com/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm).)

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See[Understanding Free-form Tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm)).

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_TOKEN_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_jms_java_downloads_java_download_token_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_TOKEN_COLLECTION_T Type

Contains a list of JavaDownloadTokenSummary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) List of JavaDownloadTokens.

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_LICENSE_T Type

Details about a license type for Java.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Commonly used name for the license type.

`license_type`

(required) License Type

Allowed values are: 'OTN', 'NFTC', 'RESTRICTED'

`license_url`

(required) Publicly accessible license URL containing the detailed terms and conditions.

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_LICENSE_ACCEPTANCE_RECORD_T Type

User acceptance record for a Java license.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier for the acceptance record.

`license_acceptance_status`

(required) Status of license acceptance.

Allowed values are: 'ACCEPTED', 'REVOKED'

`compartment_id`

(required) The tenancy[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user accepting the license.

`license_type`

(required) License type associated with the acceptance.

Allowed values are: 'OTN', 'NFTC', 'RESTRICTED'

`created_by`

(required)

`last_updated_by`

(optional)

`time_accepted`

(required) The date and time of license acceptance(formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_last_updated`

(optional) The date and time of last update(formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`lifecycle_state`

(optional) The current state of the JavaLicenseAcceptanceRecord.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'NEEDS_ATTENTION', 'UPDATING'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`. (See[Managing Tags and Tag Namespaces](https://docs.oracle.com/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm).)

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See[Understanding Free-form Tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm)).

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_LICENSE_ACCEPTANCE_RECORD_SUMMARY_T Type

User acceptance record summary for a Java license.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier for the acceptance record.

`license_acceptance_status`

(required) Status of license acceptance.

Allowed values are: 'ACCEPTED', 'REVOKED'

`compartment_id`

(required) The tenancy[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user accepting the license.

`license_type`

(required) License type associated with the acceptance.

Allowed values are: 'OTN', 'NFTC', 'RESTRICTED'

`created_by`

(required)

`last_updated_by`

(optional)

`time_accepted`

(required) The date and time of license acceptance(formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_last_updated`

(optional) The date and time of last update(formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`lifecycle_state`

(optional) The current state of the JavaLicenseAcceptanceRecord.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'NEEDS_ATTENTION', 'UPDATING'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`. (See[Managing Tags and Tag Namespaces](https://docs.oracle.com/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm).)

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See[Understanding Free-form Tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm)).

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_LICENSE_ACCEPTANCE_RECORD_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_jms_java_downloads_java_license_acceptance_record_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_LICENSE_ACCEPTANCE_RECORD_COLLECTION_T Type

Contains a list of JavaLicenseAcceptanceRecordSummary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) List of JavaLicenseAcceptanceRecords.

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_LICENSE_SUMMARY_T Type

Summary of a license type for Java.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Commonly used name for the license type.

`license_type`

(required) License Type

Allowed values are: 'OTN', 'NFTC', 'RESTRICTED'

`license_url`

(required) Publicly accessible license URL containing the detailed terms and conditions.

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_LICENSE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_jms_java_downloads_java_license_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_LICENSE_COLLECTION_T Type

Collection of the Java license summary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of JavaLicenseSummary objects.

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_REQUEST_SUMMARIZED_JAVA_DOWNLOAD_COUNTS_DETAILS_T Type

Attributes to summarize the Java download counts in a tenancy.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)here should be the tenancy OCID.

`group_as`

(required) Group as property specifying the aggregation type for download counts.

Allowed values are: 'JAVA_FAMILY', 'JAVA_RELEASE', 'PLATFORM'

`family_version`

(optional) Unique Java family version identifier.

`release_version`

(optional) Unique Java release version identifier.

`time_start`

(optional) The start time from when download data has to be included (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_end`

(optional) The end time until when the download data has to be included (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`sort_by`

(optional) The property to be used for sorting the aggregated report.

Allowed values are: 'FAMILY_VERSION', 'DOWNLOAD_COUNT'

`sort_order`

(optional) The sort order for the aggregated report.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous call.

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_UPDATE_JAVA_DOWNLOAD_TOKEN_DETAILS_T Type

The attributes of the JavaDownloadToken to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) User provided display name of the JavaDownloadToken.

`description`

(optional) User provided description of the JavaDownloadToken.

`is_default`

(optional) Update the token default status.

`time_expires`

(optional) Expiry time of the token.

`license_type`

(optional) The license type(s) associated with the JavaDownloadToken.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`. (See[Managing Tags and Tag Namespaces](https://docs.oracle.com/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm).)

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See[Understanding Free-form Tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm)).

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_UPDATE_JAVA_LICENSE_ACCEPTANCE_RECORD_DETAILS_T Type

The attributes for updating a Java license acceptance record.

Syntax
```

```

Fields

Field Description

`license_acceptance_status`

(required) Status of license acceptance.

Allowed values are: 'ACCEPTED', 'REVOKED'

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_WORK_REQUEST_RESOURCE_T Type

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

(optional) The URI path that the user can do a GET on to access the resource metadata.

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_jms_java_downloads_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_WORK_REQUEST_T Type

A description of workrequest status.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'CREATE_JAVA_DOWNLOAD_TOKEN', 'UPDATE_JAVA_DOWNLOAD_TOKEN', 'DELETE_JAVA_DOWNLOAD_TOKEN', 'CREATE_JAVA_DOWNLOAD_REPORT', 'DELETE_JAVA_DOWNLOAD_REPORT'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'NEEDS_ATTENTION', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tenancy scoped to the work request.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the request was completed, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_WORK_REQUEST_ERROR_T Type

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

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_jms_java_downloads_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestError objects.

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_jms_java_downloads_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a workRequestLog search. Contains both workRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestLogEntries.

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'CREATE_JAVA_DOWNLOAD_TOKEN', 'UPDATE_JAVA_DOWNLOAD_TOKEN', 'DELETE_JAVA_DOWNLOAD_TOKEN', 'CREATE_JAVA_DOWNLOAD_REPORT', 'DELETE_JAVA_DOWNLOAD_REPORT'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'NEEDS_ATTENTION', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tenancy scoped to the work request.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the request was completed, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_jms_java_downloads_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestSummary objects.

- [Java Downloads Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-8AB6B607-0110-4537-AEBC-DE3F472D6F00)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-078F1EC3-3513-429F-BD6F-59D26BADCCAF)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_CREATE_JAVA_DOWNLOAD_REPORT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-E350129E-9B83-4ACD-9CAC-8D3C7AA918B5)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_CREATE_JAVA_DOWNLOAD_TOKEN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-8BDF6DE5-5C92-4E5C-81AF-5F7CB309D99C)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_CREATE_JAVA_LICENSE_ACCEPTANCE_RECORD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-2E903457-B8F1-4C6A-AAC8-942AE78270A4)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_DOWNLOAD_URL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-0196ACE0-47DB-4667-83AD-C934455E29DD)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-980052CF-1ED2-442E-B72C-160E1BE1AE0D)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_GENERATE_ARTIFACT_DOWNLOAD_URL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-3129419B-6836-4BC6-A079-55C813D357FF)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_COUNT_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-2ED80FB0-970D-420F-980B-AE4A58B8B8E8)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_COUNT_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-30339BF0-2FA1-470E-8BFC-4FAAA7F82999)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_COUNT_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-B7E0BB45-A878-437D-8BA9-B7FB06219487)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_RECORD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-899167F2-394A-4EED-BCAD-1D11B22F7EFD)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_RECORD_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-870426AE-1623-4345-B15B-001C4C8EF8E2)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_RECORD_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-88F41630-932E-41BC-9BE6-A0AD14006AF2)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_RECORD_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-4089778E-D7A7-4345-A119-14364C86ED62)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_PRINCIPAL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-9FC475C3-23CE-4A70-A504-49DA0374DFFA)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_REPORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-CB003FE8-64C9-4E3E-A33E-4EBFB6C50D68)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_REPORT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-A54CAA82-8DBF-4D02-8156-A351B00D78CA)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_REPORT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-C0B4FB22-AAE8-4DDC-88AC-6B2BCA5A0315)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_REPORT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-ACC292F0-E022-4E31-89DD-BDE213D87026)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_TOKEN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-10E101BB-9198-4CBC-A177-57EAC376DD31)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_TOKEN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-51624F93-EB27-4FA0-B1CF-31B428FB1558)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_TOKEN_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-BC16F664-0ACD-4865-8059-FC1C23A787DE)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_DOWNLOAD_TOKEN_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-BFE47D60-7228-4130-A5B7-C98E4E198F9B)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_LICENSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-A96801BA-AFB8-4228-8528-46FC0E03225A)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_LICENSE_ACCEPTANCE_RECORD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-DE63649B-652F-406D-8621-9CCDEB471CF8)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_LICENSE_ACCEPTANCE_RECORD_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-A1FD6793-2345-4E48-9875-01D94ADD0EE6)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_LICENSE_ACCEPTANCE_RECORD_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-FC14F7C6-5E19-47D2-8F00-95862E5261FB)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_LICENSE_ACCEPTANCE_RECORD_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-3FDBFB07-9101-4035-B575-F47C2D092BFC)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_LICENSE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-E5CF2EAF-F632-4382-BEC9-BEADFE09E0BD)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_LICENSE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-49BEB50F-A87B-4E31-BCB1-03BC156542CF)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_JAVA_LICENSE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-C0AE0A39-6F31-48C7-B21A-400913F47AC7)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_REQUEST_SUMMARIZED_JAVA_DOWNLOAD_COUNTS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-074A1E40-DA41-4BB4-B2A9-4B5A8A97D948)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_UPDATE_JAVA_DOWNLOAD_TOKEN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-CFF9C2C1-0C04-4B8A-B24C-C9E589D80580)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_UPDATE_JAVA_LICENSE_ACCEPTANCE_RECORD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-C96DFB14-F944-4381-8D7B-192E68698F16)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-E1D4ED97-7F37-40AD-B668-1D3EC0FCEA44)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-4744A098-FA41-4BD8-8765-26D63B15241B)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-CC0687C3-0996-478B-896D-785192D5417A)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-75AA4E01-0E5F-4506-AC22-8565682E9A1E)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-CCF60768-6E7F-4E53-A542-8D3277F58F58)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-F3643038-64BD-42E1-8B64-F7D2B6B0D7A4)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-67691F53-8086-4200-ABFB-BB3F079C416F)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-A157D11F-F4D0-4057-B2A1-1C7636A541DD)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-77241B97-6FFF-4C46-BDEA-00457EDD6CF0)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-1467FDE1-E2FE-4F26-836A-CEABDA71F865)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-7CA61D2A-F83B-459B-BD61-65DF9D1BEC4A)
- [DBMS_CLOUD_OCI_JMS_JAVA_DOWNLOADS_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_java_downloads_t.html#ADSDK-GUID-5A96374A-D2E9-408B-B529-B12E135E3B27)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
