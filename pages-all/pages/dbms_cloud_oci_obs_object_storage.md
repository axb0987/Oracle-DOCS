# Object Storage Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html
- Fetched: 2026-09-05 19:10 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#dcoc-content-body)

## Object Storage Functions

Package: DBMS_CLOUD_OCI_OBS_OBJECT_STORAGE

### ABORT_MULTIPART_UPLOAD Function

Aborts an in-progress multipart upload and deletes all parts that have been uploaded.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`object_name`

(required) The name of the object. Avoid entering confidential information. Example: `test/object1.log`

`upload_id`

(required) The upload ID for a multipart upload.

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CANCEL_WORK_REQUEST Function

Cancels a work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### COMMIT_MULTIPART_UPLOAD Function

Commits a multipart upload, which involves checking part numbers and entity tags (ETags) of the parts, to create an aggregate object.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`object_name`

(required) The name of the object. Avoid entering confidential information. Example: `test/object1.log`

`upload_id`

(required) The upload ID for a multipart upload.

`commit_multipart_upload_details`

(required) The part numbers and entity tags (ETags) for the parts you want to commit.

`if_match`

(optional) The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.

`if_none_match`

(optional) The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the resource already exists.

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### COPY_OBJECT Function

Creates a request to copy an object within a region or to another region. See[Object Names](https://docs.oracle.com/iaas/Content/Object/Tasks/managingobjects.htm#namerequirements)for object naming requirements.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`copy_object_details`

(required) The source and destination of the object to be copied.

`opc_client_request_id`

(optional) The client request ID for tracing.

`opc_sse_customer_algorithm`

(optional) The optional header that specifies \"AES256\" as the encryption algorithm. For more information, see[Using Your Own Keys for Server-Side Encryption](https://docs.oracle.com/iaas/Content/Object/Tasks/usingyourencryptionkeys.htm).

`opc_sse_customer_key`

(optional) The optional header that specifies the base64-encoded 256-bit encryption key to use to encrypt or decrypt the data. For more information, see[Using Your Own Keys for Server-Side Encryption](https://docs.oracle.com/iaas/Content/Object/Tasks/usingyourencryptionkeys.htm).

`opc_sse_customer_key_sha256`

(optional) The optional header that specifies the base64-encoded SHA256 hash of the encryption key. This value is used to check the integrity of the encryption key. For more information, see[Using Your Own Keys for Server-Side Encryption](https://docs.oracle.com/iaas/Content/Object/Tasks/usingyourencryptionkeys.htm).

`opc_source_sse_customer_algorithm`

(optional) The optional header that specifies \"AES256\" as the encryption algorithm to use to decrypt the source object. For more information, see[Using Your Own Keys for Server-Side Encryption](https://docs.oracle.com/iaas/Content/Object/Tasks/usingyourencryptionkeys.htm).

`opc_source_sse_customer_key`

(optional) The optional header that specifies the base64-encoded 256-bit encryption key to use to decrypt the source object. For more information, see[Using Your Own Keys for Server-Side Encryption](https://docs.oracle.com/iaas/Content/Object/Tasks/usingyourencryptionkeys.htm).

`opc_source_sse_customer_key_sha256`

(optional) The optional header that specifies the base64-encoded SHA256 hash of the encryption key used to decrypt the source object. This value is used to check the integrity of the encryption key. For more information, see[Using Your Own Keys for Server-Side Encryption](https://docs.oracle.com/iaas/Content/Object/Tasks/usingyourencryptionkeys.htm).

`opc_sse_kms_key_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a master encryption key used to call the Key Management service to generate a data encryption key or to encrypt or decrypt a data encryption key.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_BUCKET Function

Creates a bucket in the given namespace with a bucket name and optional user-defined metadata. Avoid entering confidential information in bucket names.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`create_bucket_details`

(required) Request object for creating a bucket.

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MULTIPART_UPLOAD Function

Starts a new multipart upload to a specific object in the given bucket in the given namespace. See[Object Names](https://docs.oracle.com/iaas/Content/Object/Tasks/managingobjects.htm#namerequirements)for object naming requirements.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`create_multipart_upload_details`

(required) Request object for creating a multipart upload.

`if_match`

(optional) The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.

`if_none_match`

(optional) The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the resource already exists.

`opc_client_request_id`

(optional) The client request ID for tracing.

`opc_sse_customer_algorithm`

(optional) The optional header that specifies \"AES256\" as the encryption algorithm. For more information, see[Using Your Own Keys for Server-Side Encryption](https://docs.oracle.com/iaas/Content/Object/Tasks/usingyourencryptionkeys.htm).

`opc_sse_customer_key`

(optional) The optional header that specifies the base64-encoded 256-bit encryption key to use to encrypt or decrypt the data. For more information, see[Using Your Own Keys for Server-Side Encryption](https://docs.oracle.com/iaas/Content/Object/Tasks/usingyourencryptionkeys.htm).

`opc_sse_customer_key_sha256`

(optional) The optional header that specifies the base64-encoded SHA256 hash of the encryption key. This value is used to check the integrity of the encryption key. For more information, see[Using Your Own Keys for Server-Side Encryption](https://docs.oracle.com/iaas/Content/Object/Tasks/usingyourencryptionkeys.htm).

`opc_sse_kms_key_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a master encryption key used to call the Key Management service to generate a data encryption key or to encrypt or decrypt a data encryption key.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PREAUTHENTICATED_REQUEST Function

Creates a pre-authenticated request specific to the bucket.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`create_preauthenticated_request_details`

(required) Information needed to create the pre-authenticated request.

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_REPLICATION_POLICY Function

Creates a replication policy for the specified bucket.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`create_replication_policy_details`

(required) The replication policy.

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_RETENTION_RULE Function

Creates a new retention rule in the specified bucket. The new rule will take effect typically within 30 seconds. Note that a maximum of 100 rules are supported on a bucket.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`create_retention_rule_details`

(required) The retention rule to create for the bucket.

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_BUCKET Function

Deletes a bucket if the bucket is already empty. If the bucket is not empty, use`DELETE_OBJECT`Function first. In addition, you cannot delete a bucket that has a multipart upload in progress or a pre-authenticated request associated with that bucket.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`if_match`

(optional) The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_OBJECT Function

Deletes an object.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`object_name`

(required) The name of the object. Avoid entering confidential information. Example: `test/object1.log`

`if_match`

(optional) The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.

`opc_client_request_id`

(optional) The client request ID for tracing.

`version_id`

(optional) VersionId used to identify a particular version of the object

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_OBJECT_LIFECYCLE_POLICY Function

Deletes the object lifecycle policy for the bucket.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`opc_client_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PREAUTHENTICATED_REQUEST Function

Deletes the pre-authenticated request for the bucket.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`par_id`

(required) The unique identifier for the pre-authenticated request. This can be used to manage operations against the pre-authenticated request, such as GET or DELETE.

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_REPLICATION_POLICY Function

Deletes the replication policy associated with the source bucket.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`replication_id`

(required) The ID of the replication policy.

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_RETENTION_RULE Function

Deletes the specified rule. The deletion takes effect typically within 30 seconds.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`retention_rule_id`

(required) The ID of the retention rule.

`if_match`

(optional) The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BUCKET Function

Gets the current representation of the given bucket in the given Object Storage namespace.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`if_match`

(optional) The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.

`if_none_match`

(optional) The entity tag (ETag) to avoid matching. Wildcards ('*') are not allowed. If the specified ETag does not match the ETag of the existing resource, the request returns the expected response. If the ETag matches the ETag of the existing resource, the request returns an HTTP 304 status without a response body.

`opc_client_request_id`

(optional) The client request ID for tracing.

`fields`

(optional) Bucket summary includes the 'namespace', 'name', 'compartmentId', 'createdBy', 'timeCreated', and 'etag' fields. This parameter can also include 'approximateCount' (approximate number of objects), 'approximateSize' (total approximate size in bytes of all objects) and 'autoTiering' (state of auto tiering on the bucket). For example 'approximateCount,approximateSize,autoTiering'.

Allowed values are: 'approximateCount', 'approximateSize', 'autoTiering'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_NAMESPACE Function

Each Oracle Cloud Infrastructure tenant is assigned one unique and uneditable Object Storage namespace. The namespace is a system-generated string assigned during account creation. For some older tenancies, the namespace string may be the tenancy name in all lower-case letters. You cannot edit a namespace. GetNamespace returns the name of the Object Storage namespace for the user making the request. If an optional compartmentId query parameter is provided, GetNamespace returns the namespace name of the corresponding tenancy, provided the user has access to it.

Syntax
```

```

Parameters

Parameter Description

`opc_client_request_id`

(optional) The client request ID for tracing.

`compartment_id`

(optional) This is an optional field representing either the tenancy[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)or the compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)within the tenancy whose Object Storage namespace is to be retrieved.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_NAMESPACE_METADATA Function

Gets the metadata for the Object Storage namespace, which contains defaultS3CompartmentId and defaultSwiftCompartmentId. Any user with the OBJECTSTORAGE_NAMESPACE_READ permission will be able to see the current metadata. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_OBJECT Function

Gets the metadata and body of an object.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`object_name`

(required) The name of the object. Avoid entering confidential information. Example: `test/object1.log`

`version_id`

(optional) VersionId used to identify a particular version of the object

`if_match`

(optional) The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.

`if_none_match`

(optional) The entity tag (ETag) to avoid matching. Wildcards ('*') are not allowed. If the specified ETag does not match the ETag of the existing resource, the request returns the expected response. If the ETag matches the ETag of the existing resource, the request returns an HTTP 304 status without a response body.

`opc_client_request_id`

(optional) The client request ID for tracing.

`range`

(optional) Optional byte range to fetch, as described in[RFC 7233](https://tools.ietf.org/html/rfc7233#section-2.1). Note that only a single range of bytes is supported.

`opc_sse_customer_algorithm`

(optional) The optional header that specifies \"AES256\" as the encryption algorithm. For more information, see[Using Your Own Keys for Server-Side Encryption](https://docs.oracle.com/iaas/Content/Object/Tasks/usingyourencryptionkeys.htm).

`opc_sse_customer_key`

(optional) The optional header that specifies the base64-encoded 256-bit encryption key to use to encrypt or decrypt the data. For more information, see[Using Your Own Keys for Server-Side Encryption](https://docs.oracle.com/iaas/Content/Object/Tasks/usingyourencryptionkeys.htm).

`opc_sse_customer_key_sha256`

(optional) The optional header that specifies the base64-encoded SHA256 hash of the encryption key. This value is used to check the integrity of the encryption key. For more information, see[Using Your Own Keys for Server-Side Encryption](https://docs.oracle.com/iaas/Content/Object/Tasks/usingyourencryptionkeys.htm).

`http_response_content_disposition`

(optional) Specify this query parameter to override the value of the Content-Disposition response header in the GetObject response.

`http_response_cache_control`

(optional) Specify this query parameter to override the Cache-Control response header in the GetObject response.

`http_response_content_type`

(optional) Specify this query parameter to override the Content-Type response header in the GetObject response.

`http_response_content_language`

(optional) Specify this query parameter to override the Content-Language response header in the GetObject response.

`http_response_content_encoding`

(optional) Specify this query parameter to override the Content-Encoding response header in the GetObject response.

`http_response_expires`

(optional) Specify this query parameter to override the Expires response header in the GetObject response.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_OBJECT_LIFECYCLE_POLICY Function

Gets the object lifecycle policy for the bucket.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PREAUTHENTICATED_REQUEST Function

Gets the pre-authenticated request for the bucket.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`par_id`

(required) The unique identifier for the pre-authenticated request. This can be used to manage operations against the pre-authenticated request, such as GET or DELETE.

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_REPLICATION_POLICY Function

Get the replication policy.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`replication_id`

(required) The ID of the replication policy.

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_RETENTION_RULE Function

Get the specified retention rule.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`retention_rule_id`

(required) The ID of the retention rule.

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets the status of the work request for the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### HEAD_BUCKET Function

Efficiently checks to see if a bucket exists and gets the current entity tag (ETag) for the bucket.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`if_match`

(optional) The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.

`if_none_match`

(optional) The entity tag (ETag) to avoid matching. Wildcards ('*') are not allowed. If the specified ETag does not match the ETag of the existing resource, the request returns the expected response. If the ETag matches the ETag of the existing resource, the request returns an HTTP 304 status without a response body.

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### HEAD_OBJECT Function

Gets the user-defined metadata and entity tag (ETag) for an object.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`object_name`

(required) The name of the object. Avoid entering confidential information. Example: `test/object1.log`

`version_id`

(optional) VersionId used to identify a particular version of the object

`if_match`

(optional) The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.

`if_none_match`

(optional) The entity tag (ETag) to avoid matching. Wildcards ('*') are not allowed. If the specified ETag does not match the ETag of the existing resource, the request returns the expected response. If the ETag matches the ETag of the existing resource, the request returns an HTTP 304 status without a response body.

`opc_client_request_id`

(optional) The client request ID for tracing.

`opc_sse_customer_algorithm`

(optional) The optional header that specifies \"AES256\" as the encryption algorithm. For more information, see[Using Your Own Keys for Server-Side Encryption](https://docs.oracle.com/iaas/Content/Object/Tasks/usingyourencryptionkeys.htm).

`opc_sse_customer_key`

(optional) The optional header that specifies the base64-encoded 256-bit encryption key to use to encrypt or decrypt the data. For more information, see[Using Your Own Keys for Server-Side Encryption](https://docs.oracle.com/iaas/Content/Object/Tasks/usingyourencryptionkeys.htm).

`opc_sse_customer_key_sha256`

(optional) The optional header that specifies the base64-encoded SHA256 hash of the encryption key. This value is used to check the integrity of the encryption key. For more information, see[Using Your Own Keys for Server-Side Encryption](https://docs.oracle.com/iaas/Content/Object/Tasks/usingyourencryptionkeys.htm).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BUCKETS Function

Gets a list of all BucketSummary items in a compartment. A BucketSummary contains only summary fields for the bucket and does not contain fields like the user-defined metadata. ListBuckets returns a BucketSummary containing at most 1000 buckets. To paginate through more buckets, use the returned `opc-next-page` value with the `page` request parameter. To use this and other API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`compartment_id`

(required) The ID of the compartment in which to list buckets.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`fields`

(optional) Bucket summary in list of buckets includes the 'namespace', 'name', 'compartmentId', 'createdBy', 'timeCreated', and 'etag' fields. This parameter can also include 'tags' (freeformTags and definedTags). The only supported value of this parameter is 'tags' for now. Example 'tags'.

Allowed values are: 'tags'

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MULTIPART_UPLOAD_PARTS Function

Lists the parts of an in-progress multipart upload.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`object_name`

(required) The name of the object. Avoid entering confidential information. Example: `test/object1.log`

`upload_id`

(required) The upload ID for a multipart upload.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MULTIPART_UPLOADS Function

Lists all of the in-progress multipart uploads for the given bucket in the given Object Storage namespace.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_OBJECT_VERSIONS Function

Lists the object versions in a bucket. ListObjectVersions returns an ObjectVersionCollection containing at most 1000 object versions. To paginate through more object versions, use the returned `opc-next-page` value with the `page` request parameter. To use this and other API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`prefix`

(optional) The string to use for matching against the start of object names in a list query.

`l_start`

(optional) Object names returned by a list query must be greater or equal to this parameter.

`l_end`

(optional) Object names returned by a list query must be strictly less than this parameter.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`delimiter`

(optional) When this parameter is set, only objects whose names do not contain the delimiter character (after an optionally specified prefix) are returned in the objects key of the response body. Scanned objects whose names contain the delimiter have the part of their name up to the first occurrence of the delimiter (including the optional prefix) returned as a set of prefixes. Note that only '/' is a supported delimiter character at this time.

`fields`

(optional) Object summary by default includes only the 'name' field. Use this parameter to also include 'size' (object size in bytes), 'etag', 'md5', 'timeCreated' (object creation date and time), 'timeModified' (object modification date and time), 'storageTier' and 'archivalState' fields. Specify the value of this parameter as a comma-separated, case-insensitive list of those field names. For example 'name,etag,timeCreated,md5,timeModified,storageTier,archivalState'.

Allowed values are: 'name', 'size', 'etag', 'timeCreated', 'md5', 'timeModified', 'storageTier', 'archivalState'

`opc_client_request_id`

(optional) The client request ID for tracing.

`start_after`

(optional) Object names returned by a list query must be greater than this parameter.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_OBJECTS Function

Lists the objects in a bucket. By default, ListObjects returns object names only. See the `fields` parameter for other fields that you can optionally include in ListObjects response. ListObjects returns at most 1000 objects. To paginate through more objects, use the returned 'nextStartWith' value with the 'start' parameter. To filter which objects ListObjects returns, use the 'start' and 'end' parameters. To use this and other API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`prefix`

(optional) The string to use for matching against the start of object names in a list query.

`l_start`

(optional) Object names returned by a list query must be greater or equal to this parameter.

`l_end`

(optional) Object names returned by a list query must be strictly less than this parameter.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`delimiter`

(optional) When this parameter is set, only objects whose names do not contain the delimiter character (after an optionally specified prefix) are returned in the objects key of the response body. Scanned objects whose names contain the delimiter have the part of their name up to the first occurrence of the delimiter (including the optional prefix) returned as a set of prefixes. Note that only '/' is a supported delimiter character at this time.

`fields`

(optional) Object summary by default includes only the 'name' field. Use this parameter to also include 'size' (object size in bytes), 'etag', 'md5', 'timeCreated' (object creation date and time), 'timeModified' (object modification date and time), 'storageTier' and 'archivalState' fields. Specify the value of this parameter as a comma-separated, case-insensitive list of those field names. For example 'name,etag,timeCreated,md5,timeModified,storageTier,archivalState'.

Allowed values are: 'name', 'size', 'etag', 'timeCreated', 'md5', 'timeModified', 'storageTier', 'archivalState'

`opc_client_request_id`

(optional) The client request ID for tracing.

`start_after`

(optional) Object names returned by a list query must be greater than this parameter.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PREAUTHENTICATED_REQUESTS Function

Lists pre-authenticated requests for the bucket.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`object_name_prefix`

(optional) User-specified object name prefixes can be used to query and return a list of pre-authenticated requests.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_REPLICATION_POLICIES Function

List the replication policies associated with a bucket.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`opc_client_request_id`

(optional) The client request ID for tracing.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_REPLICATION_SOURCES Function

List the replication sources of a destination bucket.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`opc_client_request_id`

(optional) The client request ID for tracing.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RETENTION_RULES Function

List the retention rules for a bucket. The retention rules are sorted based on creation time, with the most recently created retention rule returned first.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Lists the errors of the work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Lists the logs of the work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The ID of the compartment in which to list buckets.

`opc_client_request_id`

(optional) The client request ID for tracing.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### MAKE_BUCKET_WRITABLE Function

Stops replication to the destination bucket and removes the replication policy. When the replication policy was created, this destination bucket became read-only except for new and changed objects replicated automatically from the source bucket. MakeBucketWritable removes the replication policy. This bucket is no longer the target for replication and is now writable, allowing users to make changes to bucket contents.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PUT_OBJECT Function

Creates a new object or overwrites an existing object with the same name. The maximum object size allowed by PutObject is 50 GiB. See[Object Names](https://docs.oracle.com/iaas/Content/Object/Tasks/managingobjects.htm#namerequirements)for object naming requirements. See[Special Instructions for Object Storage PUT](https://docs.oracle.com/iaas/Content/API/Concepts/signingrequests.htm#ObjectStoragePut)for request signature requirements.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`object_name`

(required) The name of the object. Avoid entering confidential information. Example: `test/object1.log`

`content_length`

(optional) The content length of the body.

`put_object_body`

(required) The object to upload to the object store.

`if_match`

(optional) The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.

`if_none_match`

(optional) The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the resource already exists.

`opc_client_request_id`

(optional) The client request ID for tracing.

`expect`

(optional) A value of `100-continue` requests preliminary verification of the request method, path, and headers before the request body is sent. If no error results from such verification, the server will send a 100 (Continue) interim response to indicate readiness for the request body. The only allowed value for this parameter is \"100-Continue\" (case-insensitive).

`content_md5`

(optional) The optional base-64 header that defines the encoded MD5 hash of the body. If the optional Content-MD5 header is present, Object Storage performs an integrity check on the body of the HTTP request by computing the MD5 hash for the body and comparing it to the MD5 hash supplied in the header. If the two hashes do not match, the object is rejected and an HTTP-400 Unmatched Content MD5 error is returned with the message: \"The computed MD5 of the request body (ACTUAL_MD5) does not match the Content-MD5 header (HEADER_MD5)\"

`content_type`

(optional) The optional Content-Type header that defines the standard MIME type format of the object. Content type defaults to 'application/octet-stream' if not specified in the PutObject call. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to identify and perform special operations on text only objects.

`content_language`

(optional) The optional Content-Language header that defines the content language of the object to upload. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to identify and differentiate objects based on a particular language.

`content_encoding`

(optional) The optional Content-Encoding header that defines the content encodings that were applied to the object to upload. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to determine what decoding mechanisms need to be applied to obtain the media-type specified by the Content-Type header of the object.

`content_disposition`

(optional) The optional Content-Disposition header that defines presentational information for the object to be returned in GetObject and HeadObject responses. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to let users download objects with custom filenames in a browser.

`cache_control`

(optional) The optional Cache-Control header that defines the caching behavior value to be returned in GetObject and HeadObject responses. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to identify objects that require caching restrictions.

`opc_sse_customer_algorithm`

(optional) The optional header that specifies \"AES256\" as the encryption algorithm. For more information, see[Using Your Own Keys for Server-Side Encryption](https://docs.oracle.com/iaas/Content/Object/Tasks/usingyourencryptionkeys.htm).

`opc_sse_customer_key`

(optional) The optional header that specifies the base64-encoded 256-bit encryption key to use to encrypt or decrypt the data. For more information, see[Using Your Own Keys for Server-Side Encryption](https://docs.oracle.com/iaas/Content/Object/Tasks/usingyourencryptionkeys.htm).

`opc_sse_customer_key_sha256`

(optional) The optional header that specifies the base64-encoded SHA256 hash of the encryption key. This value is used to check the integrity of the encryption key. For more information, see[Using Your Own Keys for Server-Side Encryption](https://docs.oracle.com/iaas/Content/Object/Tasks/usingyourencryptionkeys.htm).

`opc_sse_kms_key_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a master encryption key used to call the Key Management service to generate a data encryption key or to encrypt or decrypt a data encryption key.

`storage_tier`

(optional) The storage tier that the object should be stored in. If not specified, the object will be stored in the same storage tier as the bucket.

Allowed values are: 'Standard', 'InfrequentAccess', 'Archive'

`opc_meta`

(optional) Optional user-defined metadata key and value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PUT_OBJECT_LIFECYCLE_POLICY Function

Creates or replaces the object lifecycle policy for the bucket.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`put_object_lifecycle_policy_details`

(required) The lifecycle policy to apply to the bucket.

`opc_client_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.

`if_none_match`

(optional) The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the resource already exists.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REENCRYPT_BUCKET Function

Re-encrypts the unique data encryption key that encrypts each object written to the bucket by using the most recent version of the master encryption key assigned to the bucket. (All data encryption keys are encrypted by a master encryption key. Master encryption keys are assigned to buckets and managed by Oracle by default, but you can assign a key that you created and control through the Oracle Cloud Infrastructure Key Management service.) The kmsKeyId property of the bucket determines which master encryption key is assigned to the bucket. If you assigned a different Key Management master encryption key to the bucket, you can call this API to re-encrypt all data encryption keys with the newly assigned key. Similarly, you might want to re-encrypt all data encryption keys if the assigned key has been rotated to a new key version since objects were last added to the bucket. If you call this API and there is no kmsKeyId associated with the bucket, the call will fail. Calling this API starts a work request task to re-encrypt the data encryption key of all objects in the bucket. Only objects created before the time of the API call will be re-encrypted. The call can take a long time, depending on how many objects are in the bucket and how big they are. This API returns a work request ID that you can use to retrieve the status of the work request task. All the versions of objects will be re-encrypted whether versioning is enabled or suspended at the bucket.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REENCRYPT_OBJECT Function

Re-encrypts the data encryption keys that encrypt the object and its chunks. By default, when you create a bucket, the Object Storage service manages the master encryption key used to encrypt each object's data encryption keys. The encryption mechanism that you specify for the bucket applies to the objects it contains. You can alternatively employ one of these encryption strategies for an object: - You can assign a key that you created and control through the Oracle Cloud Infrastructure Vault service. - You can encrypt an object using your own encryption key. The key you supply is known as a customer-provided encryption key (SSE-C).

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`object_name`

(required) The name of the object. Avoid entering confidential information. Example: `test/object1.log`

`reencrypt_object_details`

(required) Request object for re-encrypting the data encryption key associated with an object.

`version_id`

(optional) VersionId used to identify a particular version of the object

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RENAME_OBJECT Function

Rename an object in the given Object Storage namespace. See[Object Names](https://docs.oracle.com/iaas/Content/Object/Tasks/managingobjects.htm#namerequirements)for object naming requirements.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`rename_object_details`

(required) The sourceName and newName of rename operation. Avoid entering confidential information.

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RESTORE_OBJECTS Function

Restores one or more objects specified by the objectName parameter. By default objects will be restored for 24 hours. Duration can be configured using the hours parameter.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`restore_objects_details`

(required) Request to restore objects.

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_BUCKET Function

Performs a partial or full update of a bucket's user-defined metadata. Use UpdateBucket to move a bucket from one compartment to another within the same tenancy. Supply the compartmentID of the compartment that you want to move the bucket to. For more information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`update_bucket_details`

(required) Request object for updating a bucket.

`if_match`

(optional) The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_NAMESPACE_METADATA Function

By default, buckets created using the Amazon S3 Compatibility API or the Swift API are created in the root compartment of the Oracle Cloud Infrastructure tenancy. You can change the default Swift/Amazon S3 compartmentId designation to a different compartmentId. All subsequent bucket creations will use the new default compartment, but no previously created buckets will be modified. A user must have OBJECTSTORAGE_NAMESPACE_UPDATE permission to make changes to the default compartments for Amazon S3 and Swift.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`update_namespace_metadata_details`

(required) Request object for update NamespaceMetadata.

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_OBJECT_STORAGE_TIER Function

Changes the storage tier of the object specified by the objectName parameter.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`update_object_storage_tier_details`

(required) The object name and the desired storage tier.

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_RETENTION_RULE Function

Updates the specified retention rule. Rule changes take effect typically within 30 seconds.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`retention_rule_id`

(required) The ID of the retention rule.

`update_retention_rule_details`

(required) Request object for updating the retention rule.

`if_match`

(optional) The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.

`opc_client_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPLOAD_PART Function

Uploads a single part of a multipart upload.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The Object Storage namespace used for the request.

`bucket_name`

(required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`

`object_name`

(required) The name of the object. Avoid entering confidential information. Example: `test/object1.log`

`upload_id`

(required) The upload ID for a multipart upload.

`upload_part_num`

(required) The part number that identifies the object part currently being uploaded.

`content_length`

(optional) The content length of the body.

`upload_part_body`

(required) The part being uploaded to the Object Storage service.

`opc_client_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload the resource.

`if_none_match`

(optional) The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the resource already exists.

`expect`

(optional) A value of `100-continue` requests preliminary verification of the request method, path, and headers before the request body is sent. If no error results from such verification, the server will send a 100 (Continue) interim response to indicate readiness for the request body. The only allowed value for this parameter is \"100-Continue\" (case-insensitive).

`content_md5`

(optional) The optional base-64 header that defines the encoded MD5 hash of the body. If the optional Content-MD5 header is present, Object Storage performs an integrity check on the body of the HTTP request by computing the MD5 hash for the body and comparing it to the MD5 hash supplied in the header. If the two hashes do not match, the object is rejected and an HTTP-400 Unmatched Content MD5 error is returned with the message: \"The computed MD5 of the request body (ACTUAL_MD5) does not match the Content-MD5 header (HEADER_MD5)\"

`opc_sse_customer_algorithm`

(optional) The optional header that specifies \"AES256\" as the encryption algorithm. For more information, see[Using Your Own Keys for Server-Side Encryption](https://docs.oracle.com/iaas/Content/Object/Tasks/usingyourencryptionkeys.htm).

`opc_sse_customer_key`

(optional) The optional header that specifies the base64-encoded 256-bit encryption key to use to encrypt or decrypt the data. For more information, see[Using Your Own Keys for Server-Side Encryption](https://docs.oracle.com/iaas/Content/Object/Tasks/usingyourencryptionkeys.htm).

`opc_sse_customer_key_sha256`

(optional) The optional header that specifies the base64-encoded SHA256 hash of the encryption key. This value is used to check the integrity of the encryption key. For more information, see[Using Your Own Keys for Server-Side Encryption](https://docs.oracle.com/iaas/Content/Object/Tasks/usingyourencryptionkeys.htm).

`opc_sse_kms_key_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a master encryption key used to call the Key Management service to generate a data encryption key or to encrypt or decrypt a data encryption key.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://objectstorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Object Storage Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-726554DF-8388-4960-BCF2-B5A6BE208F56)
- [ABORT_MULTIPART_UPLOAD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-C6129F6A-199E-447A-A7DB-01EA522E6A14)
- [CANCEL_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-F420A6F0-864F-4B87-B4E3-E08FF9662D11)
- [COMMIT_MULTIPART_UPLOAD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-426CFB2D-552B-4C6C-8B06-C5AC3DB8A227)
- [COPY_OBJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-B7A440FE-CFCF-4500-8179-D2894F92305A)
- [CREATE_BUCKET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-305CA38B-7D43-410B-BD9D-7C465A33372B)
- [CREATE_MULTIPART_UPLOAD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-670FE6B0-44CF-4FF7-A946-FCDF409F7C85)
- [CREATE_PREAUTHENTICATED_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-C95E73E1-AAB0-401E-9D7C-EA8410ED0C51)
- [CREATE_REPLICATION_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-D50E9157-7777-4E8B-9B78-321F01A72C28)
- [CREATE_RETENTION_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-0DC8E7E9-ACE3-4CB4-8363-2570C6496A49)
- [DELETE_BUCKET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-228F5094-5FB9-465D-8DAB-6DA2F5E39B5F)
- [DELETE_OBJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-E6242EE5-3368-43C6-B524-25E02B6F771D)
- [DELETE_OBJECT_LIFECYCLE_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-38318304-BC7C-40AA-9729-1A50DC35B403)
- [DELETE_PREAUTHENTICATED_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-AEC85A16-F568-4B17-BEB4-DB659F97ADF2)
- [DELETE_REPLICATION_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-4174E672-A4D2-4F26-9233-A44098E6F9E7)
- [DELETE_RETENTION_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-173DBE11-BB14-4C70-B4D1-823F4439A019)
- [GET_BUCKET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-31F5A12E-29E7-4904-B952-C6ADFD10EF53)
- [GET_NAMESPACE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-84B5D10B-858C-4E5E-AFDB-64443F1E8FFE)
- [GET_NAMESPACE_METADATA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-1AE5945C-8F42-4098-BD87-26AAA288595C)
- [GET_OBJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-A4676FC8-23B1-48A2-BD4D-7487C64B536B)
- [GET_OBJECT_LIFECYCLE_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-86C1A4C6-8EF2-40C5-A833-AA3619220972)
- [GET_PREAUTHENTICATED_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-847E605B-F787-436F-9400-7A91BCCF52E0)
- [GET_REPLICATION_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-74DAFEFD-0B7F-4117-BF17-05DBF6D5E1A5)
- [GET_RETENTION_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-BFC904BF-C18A-4A88-884F-C61C6F0AAEF2)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-7B9D74C6-C98E-4490-A49A-1B933C18D940)
- [HEAD_BUCKET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-74950C61-1B9C-40D8-85AC-BAA17A70AF62)
- [HEAD_OBJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-EBF080BD-36DD-42FC-B738-5F779296D77B)
- [LIST_BUCKETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-EB8C3A64-3528-4008-ABE1-A85515F6111D)
- [LIST_MULTIPART_UPLOAD_PARTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-5C448A7F-17F5-4C39-B08E-74EAC9E934DE)
- [LIST_MULTIPART_UPLOADS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-F86B2048-9E98-4939-900B-B75A98D48714)
- [LIST_OBJECT_VERSIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-BE5B68D1-3FC1-40A4-B85E-ECD8EB17BDBB)
- [LIST_OBJECTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-838B5ACA-9560-4AAA-A13C-1DDA8C114C67)
- [LIST_PREAUTHENTICATED_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-BBDCDA6A-FD88-4E3A-8F92-91B2017976B6)
- [LIST_REPLICATION_POLICIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-526D0362-927F-4119-AA8F-F0165AE35900)
- [LIST_REPLICATION_SOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-B399CAC3-32BA-4C8E-B46F-76EA5D2A2592)
- [LIST_RETENTION_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-588AEE1A-24C1-4B00-838C-AC5B8813404A)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-1C60F735-E185-44C4-8746-29AA2467EED1)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-4174AFB1-78FD-4530-AF71-0B2AEAD7625B)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-1E7561DA-FEFB-42A6-B63B-80793F2A9AD1)
- [MAKE_BUCKET_WRITABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-D0448598-9425-4204-88A2-533E2D5EA6F9)
- [PUT_OBJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-8A54585B-0339-496E-8735-51162133E55B)
- [PUT_OBJECT_LIFECYCLE_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-218AC3A3-2003-4221-8016-89BE5DFC9A61)
- [REENCRYPT_BUCKET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-BA2340AD-3556-426E-9D95-89A781314A70)
- [REENCRYPT_OBJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-A7A8F13B-52F3-47CB-8CCC-316CC56275CD)
- [RENAME_OBJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-579EA42E-4FC7-4D10-BA2A-16529CCBA49A)
- [RESTORE_OBJECTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-BF5283D2-ED08-4B3C-80C7-61C2D4ED6189)
- [UPDATE_BUCKET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-124939F0-D07D-4643-B6AA-6E7271757EBD)
- [UPDATE_NAMESPACE_METADATA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-7DE2B1E9-B0CC-4EAF-B81C-49D3F3E7CCBA)
- [UPDATE_OBJECT_STORAGE_TIER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-6656848D-CB76-480E-8ABE-163A0B413581)
- [UPDATE_RETENTION_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-6D6EAC2E-D423-42EC-879E-FC8A3E07D0D6)
- [UPLOAD_PART Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_obs_object_storage.html#ADSDK-GUID-70063E20-8C9F-4E91-9701-F6B3C6DE6B80)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
