# Java Downloads Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html
- Fetched: 2026-09-05 19:08 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#dcoc-content-body)

## Java Downloads Functions

Package: DBMS_CLOUD_OCI_JJD_JAVA_DOWNLOAD

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

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_JAVA_DOWNLOAD_REPORT Function

Create a new report in the specified format containing the download details for the tenancy.

Syntax
```

```

Parameters

Parameter Description

`create_java_download_report_details`

(required) Details for the new report.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_JAVA_DOWNLOAD_TOKEN Function

Creates a new JavaDownloadToken in the tenancy with specified attributes.

Syntax
```

```

Parameters

Parameter Description

`create_java_download_token_details`

(required) Details for the new JavaDownloadToken.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_JAVA_LICENSE_ACCEPTANCE_RECORD Function

Creates a Java license acceptance record for the specified license type in a tenancy.

Syntax
```

```

Parameters

Parameter Description

`create_java_license_acceptance_record_details`

(required) Details for the new JavaLicenseAcceptanceRecord.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_JAVA_DOWNLOAD_REPORT Function

Deletes a JavaDownloadReport resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`java_download_report_id`

(required) Unique Java download report identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_JAVA_DOWNLOAD_TOKEN Function

Deletes a JavaDownloadToken resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`java_download_token_id`

(required) Unique JavaDownloadToken identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_JAVA_LICENSE_ACCEPTANCE_RECORD Function

Deletes a Java license acceptance record with the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`java_license_acceptance_record_id`

(required) Unique Java license acceptance record identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GENERATE_ARTIFACT_DOWNLOAD_URL Function

Generates a short-lived download URL and returns it in the response payload. The returned URL can then be used for downloading the specific Java runtime artifact. Use the`GET_JAVA_RELEASE`Function API to get information about available artifacts for a specific release. Each such artifact is uniquely identified by an `artifactId`. Refer`JAVA_ARTIFACT`Function for more details.

Syntax
```

```

Parameters

Parameter Description

`generate_artifact_download_url_details`

(required) Details for generating download URL for a Java artifact.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JAVA_DOWNLOAD_REPORT Function

Gets a JavaDownloadReport by the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`java_download_report_id`

(required) Unique Java download report identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JAVA_DOWNLOAD_REPORT_CONTENT Function

Retrieve a Java download report with the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`java_download_report_id`

(required) Unique Java download report identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JAVA_DOWNLOAD_TOKEN Function

Gets a JavaDownloadToken by identifier

Syntax
```

```

Parameters

Parameter Description

`java_download_token_id`

(required) Unique JavaDownloadToken identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JAVA_LICENSE Function

Return details of the specified Java license type.

Syntax
```

```

Parameters

Parameter Description

`license_type`

(required) Unique Java license type.

Allowed values are: 'OTN', 'NFTC', 'RESTRICTED'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JAVA_LICENSE_ACCEPTANCE_RECORD Function

Returns a specific Java license acceptance record in a tenancy.

Syntax
```

```

Parameters

Parameter Description

`java_license_acceptance_record_id`

(required) Unique Java license acceptance record identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_JAVA_DOWNLOAD_RECORDS Function

Returns a list of Java download records in a tenancy based on specified parameters. See`LIST_JAVA_RELEASES`Function for possible values of `javaFamilyVersion` and `javaReleaseVersion` parameters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tenancy.

`family_version`

(optional) Unique Java family version identifier.

`release_version`

(optional) Unique Java release version identifier.

`os_family`

(optional) Target Operating System family of the artifact.

`architecture`

(optional) Target Operating System architecture of the artifact.

`package_type_detail`

(optional) Packaging type detail of the artifact.

`time_start`

(optional) The start of the time period for which reports are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_end`

(optional) The end of the time period for which reports are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) If no value is specified _timeDownloaded_ is default.

Allowed values are: 'timeDownloaded', 'downloadSourceId', 'downloadType'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_JAVA_DOWNLOAD_REPORTS Function

Returns a list of JavaDownloadReports.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tenancy.

`lifecycle_state`

(optional) A filter to return only resources their lifecycleState matches the given lifecycleState.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'NEEDS_ATTENTION', 'UPDATING'

`display_name`

(optional) A filter to return only resources that match the display name.

`java_download_report_id`

(optional) Unique Java download report identifier.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. If no value is specified, _timeCreated_ is the default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_JAVA_DOWNLOAD_TOKENS Function

Returns a list of JavaDownloadTokens.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tenancy.

`lifecycle_state`

(optional) A filter to return only resources their lifecycleState matches the given lifecycleState.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'NEEDS_ATTENTION', 'UPDATING'

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`id`

(optional) Unique JavaDownloadToken identifier.

`value`

(optional) Unique JavaDownloadToken value.

`family_version`

(optional) Unique Java family version identifier.

`search_by_user`

(optional) A filter to return only resources that match the user principal detail. The search string can be any of the property values from the`PRINCIPAL`Function object. This object is used as response datatype for the `createdBy` and `lastUpdatedBy` fields in applicable resource.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. If no value is specified, _timeCreated_ is the default.

Allowed values are: 'timeCreated', 'timeExpires', 'state', 'displayName', 'javaVersion'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_JAVA_LICENSE_ACCEPTANCE_RECORDS Function

Returns a list of all the Java license acceptance records in a tenancy.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tenancy.

`search_by_user`

(optional) A filter to return only resources that match the user principal detail. The search string can be any of the property values from the`PRINCIPAL`Function object. This object is used as response datatype for the `createdBy` and `lastUpdatedBy` fields in applicable resource.

`id`

(optional) Unique Java license acceptance record identifier.

`license_type`

(optional) Unique Java license type.

Allowed values are: 'OTN', 'NFTC', 'RESTRICTED'

`status`

(optional) The status of license acceptance.

Allowed values are: 'ACCEPTED', 'REVOKED'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. If no value is specified, _timeAccepted_ is the default.

Allowed values are: 'timeAccepted', 'timeLastUpdated', 'licenseAcceptanceStatus'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_JAVA_LICENSES Function

Return a list with details of all Java licenses.

Syntax
```

```

Parameters

Parameter Description

`license_type`

(optional) Unique Java license type.

Allowed values are: 'OTN', 'NFTC', 'RESTRICTED'

`display_name`

(optional) A filter to return only resources that match the display name.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. If no value is specified, _licenseType_ is the default.

Allowed values are: 'licenseType', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timestamp is descending.

Allowed values are: 'timestamp'

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timestamp is descending.

Allowed values are: 'timestamp'

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

Lists the work requests in a tenancy.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tenancy.

`id`

(optional) The ID of an asynchronous work request.

`status`

(optional) A filter to return only resources their lifecycleState matches the given OperationStatus.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'NEEDS_ATTENTION', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`resource_id`

(optional) The ID of the resource affected by the work request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_SUMMARIZED_JAVA_DOWNLOAD_COUNTS Function

Returns list of download counts grouped by the specified property.

Syntax
```

```

Parameters

Parameter Description

`request_summarized_java_download_counts_details`

(required) Details for retreiving the summary of download counts.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_JAVA_DOWNLOAD_TOKEN Function

Updates the JavaDownloadToken specified by the identifier.

Syntax
```

```

Parameters

Parameter Description

`java_download_token_id`

(required) Unique JavaDownloadToken identifier.

`update_java_download_token_details`

(required) The attributes to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_JAVA_LICENSE_ACCEPTANCE_RECORD Function

Updates a specific Java license acceptance record in a tenancy.

Syntax
```

```

Parameters

Parameter Description

`java_license_acceptance_record_id`

(required) Unique Java license acceptance record identifier.

`update_java_license_acceptance_record_details`

(required) Attributes for updating the JavaLicenseAcceptanceRecord.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagementservice-download.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Java Downloads Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-CC6F33A3-1767-447E-8F44-A53050CF8C03)
- [CANCEL_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-78A3FFFB-CE0C-4019-A09B-08A113173A68)
- [CREATE_JAVA_DOWNLOAD_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-2189ED78-57B0-4CD6-9014-605A673FD976)
- [CREATE_JAVA_DOWNLOAD_TOKEN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-4E26C8E9-7560-461D-93D2-57DE39584AC3)
- [CREATE_JAVA_LICENSE_ACCEPTANCE_RECORD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-B5455E76-0FCA-4331-B27A-A870531AC727)
- [DELETE_JAVA_DOWNLOAD_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-598856D4-FC68-4E20-8381-2AEFC9236818)
- [DELETE_JAVA_DOWNLOAD_TOKEN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-9063C2C7-E010-43C2-BFA5-E3C79FA2598C)
- [DELETE_JAVA_LICENSE_ACCEPTANCE_RECORD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-D9E402A9-9E2A-46D6-948B-442EC49BE0E1)
- [GENERATE_ARTIFACT_DOWNLOAD_URL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-A7603686-147D-43F1-A3BB-40C0B51F9696)
- [GET_JAVA_DOWNLOAD_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-90F3A082-E66B-4175-854E-5EC795C9836C)
- [GET_JAVA_DOWNLOAD_REPORT_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-C7E96202-7EBF-45D0-B8E5-7A7584484002)
- [GET_JAVA_DOWNLOAD_TOKEN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-ED422D4F-E2D7-40AC-83F0-456BFDF9E042)
- [GET_JAVA_LICENSE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-C770579F-BBB3-48B5-83DD-CA16747D8738)
- [GET_JAVA_LICENSE_ACCEPTANCE_RECORD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-58A552AE-A354-4B90-B2D0-92F24D8A33B1)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-1D1AECFE-2265-41CC-A7AB-8ED3A25ADB5B)
- [LIST_JAVA_DOWNLOAD_RECORDS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-8CE846CB-028B-414C-A784-60193C36CAC2)
- [LIST_JAVA_DOWNLOAD_REPORTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-1AEDA1B3-F7C2-463C-BF67-6DF753571300)
- [LIST_JAVA_DOWNLOAD_TOKENS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-06F17242-4BBD-4D6A-BF44-37B53429E906)
- [LIST_JAVA_LICENSE_ACCEPTANCE_RECORDS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-D6EA8337-89C6-4B23-8474-0EFAD4281BE4)
- [LIST_JAVA_LICENSES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-F68EA2D9-520C-466B-BB56-363593A61B73)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-16237389-20B2-4277-AEFA-3C40D64F3E53)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-9BBC204A-7070-4661-AD8C-8808D847BC9D)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-3C5A4580-BB73-4ED4-9519-51CD3E3EDF12)
- [REQUEST_SUMMARIZED_JAVA_DOWNLOAD_COUNTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-D4B27776-371C-47E6-873A-1994C4121E44)
- [UPDATE_JAVA_DOWNLOAD_TOKEN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-A6DC8955-9E5F-48AE-B387-C7D468FCC412)
- [UPDATE_JAVA_LICENSE_ACCEPTANCE_RECORD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jjd_java_download.html#ADSDK-GUID-00505201-A876-4487-A3E4-F14BCC561B09)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
