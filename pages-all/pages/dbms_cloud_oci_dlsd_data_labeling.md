# Data Labeling Service Dataplane Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dlsd_data_labeling.html
- Fetched: 2026-09-05 19:06 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dlsd_data_labeling.html#dcoc-content-body)

## Data Labeling Service Dataplane Functions

Package: DBMS_CLOUD_OCI_DLSD_DATA_LABELING

### CREATE_ANNOTATION Function

Creates an annotation.

Syntax
```

```

Parameters

Parameter Description

`create_annotation_details`

(required) Details for the new CreateAnnotation.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, without risk of executing that same action again, if there is a timeout or server error. Retry tokens expire after 24 hours, but can be invalidated before then if there are conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datalabeling-dp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_RECORD Function

Creates a record.

Syntax
```

```

Parameters

Parameter Description

`create_record_details`

(required) The details for the new record.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, without risk of executing that same action again, if there is a timeout or server error. Retry tokens expire after 24 hours, but can be invalidated before then if there are conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datalabeling-dp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ANNOTATION Function

It deletes an annotation resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`annotation_id`

(required) A unique annotation identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datalabeling-dp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_RECORD Function

Deletes a record resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`record_id`

(required) The OCID of the record annotated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datalabeling-dp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ANNOTATION Function

Gets an annotation.

Syntax
```

```

Parameters

Parameter Description

`annotation_id`

(required) A unique annotation identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datalabeling-dp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATASET Function

Gets a dataset by identifier.

Syntax
```

```

Parameters

Parameter Description

`dataset_id`

(required) A unique dataset OCID.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datalabeling-dp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_RECORD Function

Gets a record.

Syntax
```

```

Parameters

Parameter Description

`record_id`

(required) The OCID of the record annotated.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datalabeling-dp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_RECORD_CONTENT Function

Retrieves the content of the record from the dataset source.

Syntax
```

```

Parameters

Parameter Description

`record_id`

(required) The OCID of the record annotated.

`opc_request_id`

(optional) The client request ID for tracing.

`if_none_match`

(optional) For optimistic concurrency control. In the GET call for a resource, set the `if-none-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be fetched only if the etag you provide does not match the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datalabeling-dp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_RECORD_PREVIEW_CONTENT Function

Retrieves the preview of the record content from the dataset source.

Syntax
```

```

Parameters

Parameter Description

`record_id`

(required) The OCID of the record annotated.

`opc_request_id`

(optional) The client request ID for tracing.

`if_none_match`

(optional) For optimistic concurrency control. In the GET call for a resource, set the `if-none-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be fetched only if the etag you provide does not match the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datalabeling-dp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ANNOTATIONS Function

Returns a list of annotations.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`dataset_id`

(required) Filter the results by the OCID of the dataset.

`lifecycle_state`

(optional) A filter to return only resources whose lifecycleState matches the given lifecycleState.

`id`

(optional) The unique OCID identifier.

`updated_by`

(optional) The OCID of the principal which updated the annotation.

`record_id`

(optional) The OCID of the record annotated.

`time_created_greater_than_or_equal_to`

(optional) The date and time the resource was created, in the timestamp format defined by RFC3339.

`time_created_less_than_or_equal_to`

(optional) The date and time the resource was created, in the timestamp format defined by RFC3339.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. The default order for timeCreated is descending. If no value is specified timeCreated is used by default.

Allowed values are: 'timeCreated', 'label'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datalabeling-dp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RECORDS Function

The list of records in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`dataset_id`

(required) Filter the results by the OCID of the dataset.

`lifecycle_state`

(optional) A filter to return only resources whose lifecycleState matches the given lifecycleState.

`name`

(optional) The name of the record.

`id`

(optional) The unique OCID identifier.

`is_labeled`

(optional) Whether the record has been labeled and has associated annotations.

`annotation_labels_contains`

(optional) Lets the user filter records based on the related annotations.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. The default order for timeCreated is descending. The default order for name is ascending. If no value is specified, timeCreated is used by default.

Allowed values are: 'timeCreated', 'name'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datalabeling-dp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_ANNOTATION_ANALYTICS Function

Summarize the annotations created for a given dataset.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`dataset_id`

(required) Filter the results by the OCID of the dataset.

`lifecycle_state`

(optional) A filter to return only resources whose lifecycleState matches the given lifecycleState.

`label`

(optional) It summarizes annotations with the specified label.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. The default order is descending. If no value is specified, updatedBy is used by default.

Allowed values are: 'count', 'label', 'updatedBy'

`annotation_group_by`

(optional) The field to group by. If no value is specified, updatedBy is used by default.

Allowed values are: 'updatedBy', 'label'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datalabeling-dp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_RECORD_ANALYTICS Function

Summarize the records created for a given dataset.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`dataset_id`

(required) Filter the results by the OCID of the dataset.

`lifecycle_state`

(optional) A filter to return only resources whose lifecycleState matches the given lifecycleState.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`record_group_by`

(optional) The field to group by. If no value is specified isLabeled is used by default.

Allowed values are: 'isLabeled', 'annotationLabelContains'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. The default order is descending. If no value is specified, count is used by default.

Allowed values are: 'count', 'isLabeled'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datalabeling-dp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ANNOTATION Function

Updates an annotation.

Syntax
```

```

Parameters

Parameter Description

`annotation_id`

(required) A unique annotation identifier.

`update_annotation_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datalabeling-dp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_RECORD Function

Updates a record.

Syntax
```

```

Parameters

Parameter Description

`record_id`

(required) The OCID of the record annotated.

`update_record_details`

(required) Information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datalabeling-dp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Data Labeling Service Dataplane Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dlsd_data_labeling.html#ADSDK-GUID-87FF9462-7925-4088-9C3D-99AC5C0DC53F)
- [CREATE_ANNOTATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dlsd_data_labeling.html#ADSDK-GUID-AAC168B7-B007-4F9B-8663-FBE0FD6A650C)
- [CREATE_RECORD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dlsd_data_labeling.html#ADSDK-GUID-5AD6159B-6133-4E61-970B-459731374488)
- [DELETE_ANNOTATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dlsd_data_labeling.html#ADSDK-GUID-2A1F3FBB-BD48-434F-8B00-14A647BC9A4C)
- [DELETE_RECORD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dlsd_data_labeling.html#ADSDK-GUID-F91EE500-47BD-473E-8286-AFCFEED04C0D)
- [GET_ANNOTATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dlsd_data_labeling.html#ADSDK-GUID-78EBBB1B-48A2-45E2-AD01-AD42384C7232)
- [GET_DATASET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dlsd_data_labeling.html#ADSDK-GUID-D8BD6152-C5FA-4DBF-9AA1-62D64A085C9D)
- [GET_RECORD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dlsd_data_labeling.html#ADSDK-GUID-C10C4A7A-0263-440E-BD3C-BA061D273C55)
- [GET_RECORD_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dlsd_data_labeling.html#ADSDK-GUID-0F6611D6-A311-406D-8712-A2106450FF67)
- [GET_RECORD_PREVIEW_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dlsd_data_labeling.html#ADSDK-GUID-CEEBBEA0-8F3A-4D8B-B699-A340102D793F)
- [LIST_ANNOTATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dlsd_data_labeling.html#ADSDK-GUID-FF3EDEF7-9A4C-49E3-ADB2-E763BC33560A)
- [LIST_RECORDS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dlsd_data_labeling.html#ADSDK-GUID-CEE5148D-8F27-41F0-A8E7-DF59B6126E89)
- [SUMMARIZE_ANNOTATION_ANALYTICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dlsd_data_labeling.html#ADSDK-GUID-24B396EE-246B-4D72-BEB6-52B2E783640C)
- [SUMMARIZE_RECORD_ANALYTICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dlsd_data_labeling.html#ADSDK-GUID-7E0C7126-94C8-4B01-848A-36320250FD3B)
- [UPDATE_ANNOTATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dlsd_data_labeling.html#ADSDK-GUID-FB994702-11F5-4552-8F35-C7DC1FFB08EE)
- [UPDATE_RECORD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dlsd_data_labeling.html#ADSDK-GUID-BD22B286-0467-4C13-93E8-321875E236C4)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
