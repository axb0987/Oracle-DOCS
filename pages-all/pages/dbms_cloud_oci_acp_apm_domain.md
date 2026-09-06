# Application Performance Monitoring Domain Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_acp_apm_domain.html
- Fetched: 2026-09-05 19:03 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_acp_apm_domain.html#dcoc-content-body)

## Application Performance Monitoring Domain Functions

Package: DBMS_CLOUD_OCI_ACP_APM_DOMAIN

### CHANGE_APM_DOMAIN_COMPARTMENT Function

Moves an APM domain into a different compartment. When provided, If-Match is checked against ETag values of the APM domain.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The OCID of the APM domain.

`change_apm_domain_compartment_details`

(required) The information to be used in changing compartment.

`if_match`

(optional) For optimistic concurrency control. Set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request therefore it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-cp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_APM_DOMAIN Function

Creates a new APM domain.

Syntax
```

```

Parameters

Parameter Description

`create_apm_domain_details`

(required) Details for the new APM domain.

`opc_retry_token`

(optional) A token that uniquely identifies a request therefore it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-cp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_APM_DOMAIN Function

Deletes the specified APM domain asynchronously. The APM domain is placed in the 'Deleting' state and will stop accepting any operation requests. All resources associated with the APM domain are eventually recovered. Use the returned work request ID to track the progress of the background activity to complete deleting the APM domain.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The OCID of the APM domain.

`if_match`

(optional) For optimistic concurrency control. Set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-cp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GENERATE_DATA_KEYS Function

Generates a set of new Data Keys for the specified APM domain with the specified names and types. These will be added to the existing set of Data Keys for the specified APM domain.

Syntax
```

```

Parameters

Parameter Description

`generate_data_keys_list_details`

(required) List of new Data Keys to be generated.

`apm_domain_id`

(required) The OCID of the APM domain.

`if_match`

(optional) For optimistic concurrency control. Set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-cp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_APM_DOMAIN Function

Gets the details of the APM domain specified by OCID.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The OCID of the APM domain.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-cp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets the details of the work request with the given ID.

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

(optional) The endpoint of the service to call using this function. e.g https://apm-cp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_APM_DOMAIN_WORK_REQUESTS Function

Returns a (paginated) list of work requests related to a specific APM domain.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The OCID of the APM domain.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-cp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_APM_DOMAINS Function

Lists all APM domains for the specified tenant compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`lifecycle_state`

(optional) A filter to return only resources that match the given life-cycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified, timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-cp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATA_KEYS Function

Lists all Data Keys for the specified APM domain. The caller may filter the list by specifying the 'dataKeyType' query parameter.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The OCID of the APM domain.

`data_key_type`

(optional) Data key type.

Allowed values are: 'PRIVATE', 'PUBLIC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-cp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Returns a (paginated) list of errors for a given work request.

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

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-cp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Returns a (paginated) list of logs for a given work request.

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

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-cp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

Returns a (paginated) list of work requests in a given compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-cp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_DATA_KEYS Function

Removes the set of specified Data Keys from the specified APM domain. Agents would no longer be able to use these data keys to upload to the APM domain once this operation is completed.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The OCID of the APM domain.

`remove_data_keys_list_details`

(required) List of Data Keys to be removed.

`if_match`

(optional) For optimistic concurrency control. Set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-cp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_APM_DOMAIN Function

Updates the APM domain.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The OCID of the APM domain.

`update_apm_domain_details`

(required) The information to be updated for the APM domain.

`if_match`

(optional) For optimistic concurrency control. Set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-cp.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Application Performance Monitoring Domain Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_acp_apm_domain.html#ADSDK-GUID-26574C19-B20F-416F-9310-491E560D31C0)
- [CHANGE_APM_DOMAIN_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_acp_apm_domain.html#ADSDK-GUID-B9447F17-D0AD-4AD2-B8CA-A04F83D6ACCE)
- [CREATE_APM_DOMAIN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_acp_apm_domain.html#ADSDK-GUID-8C53F252-14F5-4BF6-9777-DAAE00E9D165)
- [DELETE_APM_DOMAIN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_acp_apm_domain.html#ADSDK-GUID-3051FA50-EE91-4B67-B13A-86595FC1A253)
- [GENERATE_DATA_KEYS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_acp_apm_domain.html#ADSDK-GUID-F0C557AD-40CD-4479-8EEB-FD38EEC24F6C)
- [GET_APM_DOMAIN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_acp_apm_domain.html#ADSDK-GUID-233E4C2D-2BCD-47BD-AA1D-D946D0CE5AC4)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_acp_apm_domain.html#ADSDK-GUID-CD0AAC3E-2A09-45B7-A3DB-BCAD259AD424)
- [LIST_APM_DOMAIN_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_acp_apm_domain.html#ADSDK-GUID-6B391BA8-FB97-46F4-A89C-917199FCA704)
- [LIST_APM_DOMAINS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_acp_apm_domain.html#ADSDK-GUID-7689988E-762C-4C61-9C1B-96168F123151)
- [LIST_DATA_KEYS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_acp_apm_domain.html#ADSDK-GUID-20C92ACE-0020-47E6-BE6E-31EDC273D560)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_acp_apm_domain.html#ADSDK-GUID-91707109-2E64-4F56-99A9-E676F22245B8)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_acp_apm_domain.html#ADSDK-GUID-473251E8-8D35-4DEE-BD47-9F74113602FB)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_acp_apm_domain.html#ADSDK-GUID-D405BE09-81BC-4659-850F-E735EFE889CF)
- [REMOVE_DATA_KEYS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_acp_apm_domain.html#ADSDK-GUID-4FAADE64-762D-4F61-9B32-866947545BA4)
- [UPDATE_APM_DOMAIN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_acp_apm_domain.html#ADSDK-GUID-3BA6FFF8-E67F-448C-91A0-D49A5992D602)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
