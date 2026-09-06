# AI Speech Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ais_ai_service_speech.html
- Fetched: 2026-09-05 19:03 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ais_ai_service_speech.html#dcoc-content-body)

## AI Speech Functions

Package: DBMS_CLOUD_OCI_AIS_AI_SERVICE_SPEECH

### CANCEL_TRANSCRIPTION_JOB Function

Canceling the job cancels all the tasks under it.

Syntax
```

```

Parameters

Parameter Description

`transcription_job_id`

(required) Unique Transcription Job identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://speech.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CANCEL_TRANSCRIPTION_TASK Function

Cancel Transcription Task

Syntax
```

```

Parameters

Parameter Description

`transcription_job_id`

(required) Unique Transcription Job identifier.

`transcription_task_id`

(required) Unique Transcription Task identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://speech.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_TRANSCRIPTION_JOB_COMPARTMENT Function

Moves a transcription Job resource into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`transcription_job_id`

(required) Unique Transcription Job identifier.

`change_transcription_job_compartment_details`

(required) Details for changing the compartment of a transcription Job.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://speech.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_TRANSCRIPTION_JOB Function

Creates a new Transcription Job.

Syntax
```

```

Parameters

Parameter Description

`create_transcription_job_details`

(required) Details for the new Transcription Job.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://speech.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TRANSCRIPTION_JOB Function

Gets a Transcription Job by identifier

Syntax
```

```

Parameters

Parameter Description

`transcription_job_id`

(required) Unique Transcription Job identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://speech.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TRANSCRIPTION_TASK Function

Gets a Transcription Task by identifier

Syntax
```

```

Parameters

Parameter Description

`transcription_job_id`

(required) Unique Transcription Job identifier.

`transcription_task_id`

(required) Unique Transcription Task identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://speech.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TRANSCRIPTION_JOBS Function

Returns a list of Transcription Jobs.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The ID of the compartment in which to list resources.

`lifecycle_state`

(optional) A filter to return only resources whose lifecycleState matches the given lifecycleState.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`id`

(optional) Unique identifier(OCID).

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

(optional) The endpoint of the service to call using this function. e.g https://speech.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TRANSCRIPTION_TASKS Function

Returns a list of Transcription Tasks.

Syntax
```

```

Parameters

Parameter Description

`transcription_job_id`

(required) Unique Transcription Job identifier.

`lifecycle_state`

(optional) A filter to return only resources whose lifecycleState matches the given lifecycleState.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`id`

(optional) Unique identifier(OCID).

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

(optional) The endpoint of the service to call using this function. e.g https://speech.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TRANSCRIPTION_JOB Function

Updates the Transcription Job

Syntax
```

```

Parameters

Parameter Description

`transcription_job_id`

(required) Unique Transcription Job identifier.

`update_transcription_job_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://speech.aiservice.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [AI Speech Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ais_ai_service_speech.html#ADSDK-GUID-A9E94464-4DBA-49B2-B7AD-15BAB507342E)
- [CANCEL_TRANSCRIPTION_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ais_ai_service_speech.html#ADSDK-GUID-579F822E-F4AB-43A3-98C1-E836DF3DB1FD)
- [CANCEL_TRANSCRIPTION_TASK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ais_ai_service_speech.html#ADSDK-GUID-E9F7F5AB-DC8F-4923-8F6F-6324C36B6EBE)
- [CHANGE_TRANSCRIPTION_JOB_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ais_ai_service_speech.html#ADSDK-GUID-415FEFA0-A98D-408B-B49E-1859408B1C87)
- [CREATE_TRANSCRIPTION_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ais_ai_service_speech.html#ADSDK-GUID-CB23BF5E-0DB4-4A5C-9A2A-E72B63EF8418)
- [GET_TRANSCRIPTION_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ais_ai_service_speech.html#ADSDK-GUID-15EC517B-9BDE-47AF-A014-9C34C3A9A345)
- [GET_TRANSCRIPTION_TASK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ais_ai_service_speech.html#ADSDK-GUID-AEA5AC14-E86B-40CC-8461-CD4A49A473DA)
- [LIST_TRANSCRIPTION_JOBS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ais_ai_service_speech.html#ADSDK-GUID-809D05DC-3026-4537-89B7-697B4BE1A851)
- [LIST_TRANSCRIPTION_TASKS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ais_ai_service_speech.html#ADSDK-GUID-4E296DA7-FC53-4FB5-9747-47D4B59E2123)
- [UPDATE_TRANSCRIPTION_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ais_ai_service_speech.html#ADSDK-GUID-6E6F1AD2-9CE0-49E2-8134-909B17E3B7C0)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
