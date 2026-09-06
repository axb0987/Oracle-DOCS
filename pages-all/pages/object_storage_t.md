# Object Storage Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html
- Fetched: 2026-09-05 19:18 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#dcoc-content-body)

## Object Storage Common Types

### DBMS_CLOUD_OCI_OBJECT_STORAGE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_OBJECT_STORAGE_BUCKET_T Type

A bucket is a container for storing objects in a compartment within a namespace. A bucket is associated with a single compartment. The compartment has policies that indicate what actions a user can perform on a bucket and all the objects in the bucket. For more information, see[Managing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets.htm). To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`namespace`

(required) The Object Storage namespace in which the bucket resides.

`name`

(required) The name of the bucket. Avoid entering confidential information. Example: my-new-bucket1

`compartment_id`

(required) The compartment ID in which the bucket is authorized.

`metadata`

(required) Arbitrary string keys and values for user-defined metadata.

`created_by`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the bucket.

`time_created`

(required) The date and time the bucket was created, as described in[RFC 2616](https://tools.ietf.org/html/rfc2616#section-14.29).

`etag`

(required) The entity tag (ETag) for the bucket.

`public_access_type`

(optional) The type of public access enabled on this bucket. A bucket is set to `NoPublicAccess` by default, which only allows an authenticated caller to access the bucket and its contents. When `ObjectRead` is enabled on the bucket, public access is allowed for the `GetObject`, `HeadObject`, and `ListObjects` operations. When `ObjectReadWithoutList` is enabled on the bucket, public access is allowed for the `GetObject` and `HeadObject` operations.

Allowed values are: 'NoPublicAccess', 'ObjectRead', 'ObjectReadWithoutList'

`storage_tier`

(optional) The storage tier type assigned to the bucket. A bucket is set to `Standard` tier by default, which means objects uploaded or copied to the bucket will be in the standard storage tier. When the `Archive` tier type is set explicitly for a bucket, objects uploaded or copied to the bucket will be stored in archive storage. The `storageTier` property is immutable after bucket is created.

Allowed values are: 'Standard', 'Archive'

`object_events_enabled`

(optional) Whether or not events are emitted for object state changes in this bucket. By default, `objectEventsEnabled` is set to `false`. Set `objectEventsEnabled` to `true` to emit events for object state changes. For more information about events, see[Overview of Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsoverview.htm).

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`kms_key_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a master encryption key used to call the Key Management service to generate a data encryption key or to encrypt or decrypt a data encryption key.

`object_lifecycle_policy_etag`

(optional) The entity tag (ETag) for the live object lifecycle policy on the bucket.

`approximate_count`

(optional) The approximate number of objects in the bucket. Count statistics are reported periodically. You will see a lag between what is displayed and the actual object count.

`approximate_size`

(optional) The approximate total size in bytes of all objects in the bucket. Size statistics are reported periodically. You will see a lag between what is displayed and the actual size of the bucket.

`replication_enabled`

(optional) Whether or not this bucket is a replication source. By default, `replicationEnabled` is set to `false`. This will be set to 'true' when you create a replication policy for the bucket.

`is_read_only`

(optional) Whether or not this bucket is read only. By default, `isReadOnly` is set to `false`. This will be set to 'true' when this bucket is configured as a destination in a replication policy.

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the bucket.

`versioning`

(optional) The versioning status on the bucket. A bucket is created with versioning `Disabled` by default. For versioning `Enabled`, objects are protected from overwrites and deletes, by maintaining their version history. When versioning is `Suspended`, the previous versions will still remain but new versions will no longer be created when overwitten or deleted.

Allowed values are: 'Enabled', 'Suspended', 'Disabled'

`auto_tiering`

(optional) The auto tiering status on the bucket. A bucket is created with auto tiering `Disabled` by default. For auto tiering `InfrequentAccess`, objects are transitioned automatically between the 'Standard' and 'InfrequentAccess' tiers based on the access pattern of the objects.

Allowed values are: 'Disabled', 'InfrequentAccess'

### DBMS_CLOUD_OCI_OBJECT_STORAGE_BUCKET_SUMMARY_T Type

To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`namespace`

(required) The Object Storage namespace in which the bucket lives.

`name`

(required) The name of the bucket. Avoid entering confidential information. Example: my-new-bucket1

`compartment_id`

(required) The compartment ID in which the bucket is authorized.

`created_by`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the bucket.

`time_created`

(required) The date and time the bucket was created, as described in[RFC 2616](https://tools.ietf.org/html/rfc2616#section-14.29).

`etag`

(required) The entity tag (ETag) for the bucket.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OBJECT_STORAGE_COMMIT_MULTIPART_UPLOAD_PART_DETAILS_T Type

To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`part_num`

(required) The part number for this part.

`etag`

(required) The entity tag (ETag) returned when this part was uploaded.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_COMMIT_MULTIPART_UPLOAD_PART_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_object_storage_commit_multipart_upload_part_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OBJECT_STORAGE_NUMBER_TBL Type

Nested table type of number.

Syntax
```

```

### DBMS_CLOUD_OCI_OBJECT_STORAGE_COMMIT_MULTIPART_UPLOAD_DETAILS_T Type

To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`parts_to_commit`

(required) The part numbers and entity tags (ETags) for the parts to be committed.

`parts_to_exclude`

(optional) The part numbers for the parts to be excluded from the completed object. Each part created for this upload must be in either partsToExclude or partsToCommit, but cannot be in both.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_COPY_OBJECT_DETAILS_T Type

The parameters required by Object Storage to process a request to copy an object to another bucket. To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`source_object_name`

(required) The name of the object to be copied.

`source_object_if_match_e_tag`

(optional) The entity tag (ETag) to match against that of the source object. Used to confirm that the source object with a given name is the version of that object storing a specified ETag.

`source_version_id`

(optional) VersionId of the object to copy. If not provided then current version is copied by default.

`destination_region`

(required) The destination region the object will be copied to, for example \"us-ashburn-1\".

`destination_namespace`

(required) The destination Object Storage namespace the object will be copied to.

`destination_bucket`

(required) The destination bucket the object will be copied to.

`destination_object_name`

(required) The name of the destination object resulting from the copy operation. Avoid entering confidential information.

`destination_object_if_match_e_tag`

(optional) The entity tag (ETag) to match against that of the destination object (an object intended to be overwritten). Used to confirm that the destination object stored under a given name is the version of that object storing a specified entity tag.

`destination_object_if_none_match_e_tag`

(optional) The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the object already exists in the destination bucket.

`destination_object_metadata`

(optional) Arbitrary string keys and values for the user-defined metadata for the object. Keys must be in \"opc-meta-*\" format. Avoid entering confidential information. Metadata key-value pairs entered in this field are assigned to the destination object. If you enter no metadata values, the destination object will inherit any existing metadata values associated with the source object.

`destination_object_storage_tier`

(optional) The storage tier that the object should be stored in. If not specified, the object will be stored in the same storage tier as the bucket.

Allowed values are: 'Standard', 'InfrequentAccess', 'Archive'

### DBMS_CLOUD_OCI_OBJECT_STORAGE_CREATE_BUCKET_DETAILS_T Type

To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the bucket. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods. Bucket names must be unique within an Object Storage namespace. Avoid entering confidential information. example: Example: my-new-bucket1

`compartment_id`

(required) The ID of the compartment in which to create the bucket.

`metadata`

(optional) Arbitrary string, up to 4KB, of keys and values for user-defined metadata.

`public_access_type`

(optional) The type of public access enabled on this bucket. A bucket is set to `NoPublicAccess` by default, which only allows an authenticated caller to access the bucket and its contents. When `ObjectRead` is enabled on the bucket, public access is allowed for the `GetObject`, `HeadObject`, and `ListObjects` operations. When `ObjectReadWithoutList` is enabled on the bucket, public access is allowed for the `GetObject` and `HeadObject` operations.

Allowed values are: 'NoPublicAccess', 'ObjectRead', 'ObjectReadWithoutList'

`storage_tier`

(optional) The type of storage tier of this bucket. A bucket is set to 'Standard' tier by default, which means the bucket will be put in the standard storage tier. When 'Archive' tier type is set explicitly, the bucket is put in the Archive Storage tier. The 'storageTier' property is immutable after bucket is created.

Allowed values are: 'Standard', 'Archive'

`object_events_enabled`

(optional) Whether or not events are emitted for object state changes in this bucket. By default, `objectEventsEnabled` is set to `false`. Set `objectEventsEnabled` to `true` to emit events for object state changes. For more information about events, see[Overview of Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsoverview.htm).

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`kms_key_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a master encryption key used to call the Key Management service to generate a data encryption key or to encrypt or decrypt a data encryption key.

`versioning`

(optional) Set the versioning status on the bucket. By default, a bucket is created with versioning `Disabled`. Use this option to enable versioning during bucket creation. Objects in a version enabled bucket are protected from overwrites and deletions. Previous versions of the same object will be available in the bucket.

Allowed values are: 'Enabled', 'Disabled'

`auto_tiering`

(optional) Set the auto tiering status on the bucket. By default, a bucket is created with auto tiering `Disabled`. Use this option to enable auto tiering during bucket creation. Objects in a bucket with auto tiering set to `InfrequentAccess` are transitioned automatically between the 'Standard' and 'InfrequentAccess' tiers based on the access pattern of the objects.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_CREATE_MULTIPART_UPLOAD_DETAILS_T Type

To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`object`

(required) The name of the object to which this multi-part upload is targeted. Avoid entering confidential information. Example: test/object1.log

`content_type`

(optional) The optional Content-Type header that defines the standard MIME type format of the object to upload. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to identify and perform special operations on text only objects.

`content_language`

(optional) The optional Content-Language header that defines the content language of the object to upload. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to identify and differentiate objects based on a particular language.

`content_encoding`

(optional) The optional Content-Encoding header that defines the content encodings that were applied to the object to upload. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to determine what decoding mechanisms need to be applied to obtain the media-type specified by the Content-Type header of the object.

`content_disposition`

(optional) The optional Content-Disposition header that defines presentational information for the object to be returned in GetObject and HeadObject responses. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to let users download objects with custom filenames in a browser.

`cache_control`

(optional) The optional Cache-Control header that defines the caching behavior value to be returned in GetObject and HeadObject responses. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to identify objects that require caching restrictions.

`storage_tier`

(optional) The storage tier that the object should be stored in. If not specified, the object will be stored in the same storage tier as the bucket.

Allowed values are: 'Standard', 'InfrequentAccess', 'Archive'

`metadata`

(optional) Arbitrary string keys and values for the user-defined metadata for the object. Keys must be in \"opc-meta-*\" format. Avoid entering confidential information.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_CREATE_PREAUTHENTICATED_REQUEST_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`name`

(required) A user-specified name for the pre-authenticated request. Names can be helpful in managing pre-authenticated requests. Avoid entering confidential information.

`bucket_listing_action`

(optional) Specifies whether a list operation is allowed on a PAR with accessType \"AnyObjectRead\" or \"AnyObjectReadWrite\". Deny: Prevents the user from performing a list operation. ListObjects: Authorizes the user to perform a list operation.

`object_name`

(optional) The name of the object that is being granted access to by the pre-authenticated request. Avoid entering confidential information. The object name can be null and if so, the pre-authenticated request grants access to the entire bucket if the access type allows that. The object name can be a prefix as well, in that case pre-authenticated request grants access to all the objects within the bucket starting with that prefix provided that we have the correct access type.

`access_type`

(required) The operation that can be performed on this resource.

Allowed values are: 'ObjectRead', 'ObjectWrite', 'ObjectReadWrite', 'AnyObjectWrite', 'AnyObjectRead', 'AnyObjectReadWrite'

`time_expires`

(required) The expiration date for the pre-authenticated request as per[RFC 3339](https://tools.ietf.org/html/rfc3339). After this date the pre-authenticated request will no longer be valid.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_CREATE_REPLICATION_POLICY_DETAILS_T Type

The details to create a replication policy.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the policy. Avoid entering confidential information.

`destination_region_name`

(required) The destination region to replicate to, for example \"us-ashburn-1\".

`destination_bucket_name`

(required) The bucket to replicate to in the destination region. Replication policy creation does not automatically create a destination bucket. Create the destination bucket before creating the policy.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_DURATION_T Type

The amount of time that objects in the bucket should be preserved for and which is calculated in relation to each object's Last-Modified timestamp. If duration is not present, then there is no time limit and the objects in the bucket will be preserved indefinitely.

Syntax
```

```

Fields

Field Description

`time_amount`

(required) The timeAmount is interpreted in units defined by the timeUnit parameter, and is calculated in relation to each object's Last-Modified timestamp.

`time_unit`

(required) The unit that should be used to interpret timeAmount.

Allowed values are: 'YEARS', 'DAYS'

### DBMS_CLOUD_OCI_OBJECT_STORAGE_CREATE_RETENTION_RULE_DETAILS_T Type

The details to create a retention rule.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-specified name for the retention rule. Names can be helpful in identifying retention rules. Avoid entering confidential information.

`duration`

(optional)

`time_rule_locked`

(optional) The date and time as per[RFC 3339](https://tools.ietf.org/html/rfc3339)after which this rule is locked and can only be deleted by deleting the bucket. Once a rule is locked, only increases in the duration are allowed and no other properties can be changed. This property cannot be updated for rules that are in a locked state. Specifying it when a duration is not specified is considered an error.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_ERROR_T Type

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code meant for programmatic parsing that defines the error.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_OBJECT_SUMMARY_T Type

To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the object. Avoid entering confidential information. Example: test/object1.log

`l_size`

(optional) Size of the object in bytes.

`md5`

(optional) Base64-encoded MD5 hash of the object data.

`time_created`

(optional) The date and time the object was created, as described in[RFC 2616](https://tools.ietf.org/html/rfc2616#section-14.29).

`etag`

(optional) The current entity tag (ETag) for the object.

`storage_tier`

(optional) The storage tier that the object is stored in.

Allowed values are: 'Standard', 'InfrequentAccess', 'Archive'

`archival_state`

(optional) Archival state of an object. This field is set only for objects in Archive tier.

Allowed values are: 'Archived', 'Restoring', 'Restored'

`time_modified`

(optional) The date and time the object was modified, as described in[RFC 2616](https://tools.ietf.org/rfc/rfc2616), section 14.29.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_OBJECT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_object_storage_object_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OBJECT_STORAGE_LIST_OBJECTS_T Type

To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`objects`

(required) An array of object summaries.

`prefixes`

(optional) Prefixes that are common to the results returned by the request if the request specified a delimiter.

`next_start_with`

(optional) The name of the object to use in the `start` parameter to obtain the next page of a truncated ListObjects response. Avoid entering confidential information. Example: test/object1.log

### DBMS_CLOUD_OCI_OBJECT_STORAGE_MULTIPART_UPLOAD_T Type

Multipart uploads provide efficient and resilient uploads, especially for large objects. Multipart uploads also accommodate objects that are too large for a single upload operation. With multipart uploads, individual parts of an object can be uploaded in parallel to reduce the amount of time you spend uploading. Multipart uploads can also minimize the impact of network failures by letting you retry a failed part upload instead of requiring you to retry an entire object upload. See[Using Multipart Uploads](https://docs.oracle.com/iaas/Content/Object/Tasks/usingmultipartuploads.htm). To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`namespace`

(required) The Object Storage namespace in which the in-progress multipart upload is stored.

`bucket`

(required) The bucket in which the in-progress multipart upload is stored.

`object`

(required) The object name of the in-progress multipart upload.

`upload_id`

(required) The unique identifier for the in-progress multipart upload.

`time_created`

(required) The date and time the upload was created, as described in[RFC 2616](https://tools.ietf.org/html/rfc2616#section-14.29).

`storage_tier`

(optional) The storage tier that the object is stored in.

Allowed values are: 'Standard', 'InfrequentAccess', 'Archive'

### DBMS_CLOUD_OCI_OBJECT_STORAGE_MULTIPART_UPLOAD_PART_SUMMARY_T Type

Gets summary information about multipart uploads. To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`etag`

(required) The current entity tag (ETag) for the part.

`md5`

(required) The MD5 hash of the bytes of the part.

`l_size`

(required) The size of the part in bytes.

`part_number`

(required) The part number for this part.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_NAMESPACE_METADATA_T Type

NamespaceMetadata maps a namespace string to defaultS3CompartmentId and defaultSwiftCompartmentId values.

Syntax
```

```

Fields

Field Description

`namespace`

(required) The Object Storage namespace to which the metadata belongs.

`default_s3_compartment_id`

(required) If the field is set, specifies the default compartment assignment for the Amazon S3 Compatibility API.

`default_swift_compartment_id`

(required) If the field is set, specifies the default compartment assignment for the Swift API.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_OBJECT_NAME_FILTER_T Type

A filter that compares object names to a set of prefixes or patterns to determine if a rule applies to a given object. The filter can contain include glob patterns, exclude glob patterns and inclusion prefixes. The inclusion prefixes property is kept for backward compatibility. It is recommended to use inclusion patterns instead of prefixes. Exclusions take precedence over inclusions.

Syntax
```

```

Fields

Field Description

`inclusion_prefixes`

(optional) An array of object name prefixes that the rule will apply to. An empty array means to include all objects.

`inclusion_patterns`

(optional) An array of glob patterns to match the object names to include. An empty array includes all objects in the bucket. Exclusion patterns take precedence over inclusion patterns. A Glob pattern is a sequence of characters to match text. Any character that appears in the pattern, other than the special pattern characters described below, matches itself. Glob patterns must be between 1 and 1024 characters. The special pattern characters have the following meanings: \\ Escapes the following character * Matches any string of characters. ? Matches any single character . [...] Matches a group of characters. A group of characters can be: A set of characters, for example: [Zafg9@]. This matches any character in the brackets. A range of characters, for example: [a-z]. This matches any character in the range. [a-f] is equivalent to [abcdef]. For character ranges only the CHARACTER-CHARACTER pattern is supported. [ab-yz] is not valid [a-mn-z] is not valid Character ranges can not start with ^ or : To include a '-' in the range, make it the first or last character.

`exclusion_patterns`

(optional) An array of glob patterns to match the object names to exclude. An empty array is ignored. Exclusion patterns take precedence over inclusion patterns. A Glob pattern is a sequence of characters to match text. Any character that appears in the pattern, other than the special pattern characters described below, matches itself. Glob patterns must be between 1 and 1024 characters. The special pattern characters have the following meanings: \\ Escapes the following character * Matches any string of characters. ? Matches any single character . [...] Matches a group of characters. A group of characters can be: A set of characters, for example: [Zafg9@]. This matches any character in the brackets. A range of characters, for example: [a-z]. This matches any character in the range. [a-f] is equivalent to [abcdef]. For character ranges only the CHARACTER-CHARACTER pattern is supported. [ab-yz] is not valid [a-mn-z] is not valid Character ranges can not start with ^ or : To include a '-' in the range, make it the first or last character.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_OBJECT_LIFECYCLE_RULE_T Type

To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the lifecycle rule to be applied.

`target`

(optional) The target of the object lifecycle policy rule. The values of target can be either \"objects\", \"multipart-uploads\" or \"previous-object-versions\". This field when declared as \"objects\" is used to specify ARCHIVE, INFREQUENT_ACCESS or DELETE rule for objects. This field when declared as \"previous-object-versions\" is used to specify ARCHIVE, INFREQUENT_ACCESS or DELETE rule for previous versions of existing objects. This field when declared as \"multipart-uploads\" is used to specify the ABORT (only) rule for uncommitted multipart-uploads.

`action`

(required) The action of the object lifecycle policy rule. Rules using the action 'ARCHIVE' move objects from Standard and InfrequentAccess storage tiers into the[Archive storage tier](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm). Rules using the action 'INFREQUENT_ACCESS' move objects from Standard storage tier into the Infrequent Access Storage tier. Objects that are already in InfrequentAccess tier or in Archive tier are left untouched. Rules using the action 'DELETE' permanently delete objects from buckets. Rules using 'ABORT' abort the uncommitted multipart-uploads and permanently delete their parts from buckets.

`time_amount`

(required) Specifies the age of objects to apply the rule to. The timeAmount is interpreted in units defined by the timeUnit parameter, and is calculated in relation to each object's Last-Modified time.

`time_unit`

(required) The unit that should be used to interpret timeAmount. Days are defined as starting and ending at midnight UTC. Years are defined as 365.2425 days long and likewise round up to the next midnight UTC.

Allowed values are: 'DAYS', 'YEARS'

`is_enabled`

(required) A Boolean that determines whether this rule is currently enabled.

`object_name_filter`

(optional)

### DBMS_CLOUD_OCI_OBJECT_STORAGE_OBJECT_LIFECYCLE_RULE_TBL Type

Nested table type of dbms_cloud_oci_object_storage_object_lifecycle_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OBJECT_STORAGE_OBJECT_LIFECYCLE_POLICY_T Type

The collection of lifecycle policy rules that together form the object lifecycle policy of a given bucket.

Syntax
```

```

Fields

Field Description

`time_created`

(optional) The date and time the object lifecycle policy was created, as described in[RFC 3339](https://tools.ietf.org/html/rfc3339).

`items`

(optional) The live lifecycle policy on the bucket. For an example of this value, see the[PutObjectLifecyclePolicy API documentation](https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/ObjectLifecyclePolicy/PutObjectLifecyclePolicy).

### DBMS_CLOUD_OCI_OBJECT_STORAGE_OBJECT_VERSION_SUMMARY_T Type

To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the object. Avoid entering confidential information. Example: test/object1.log

`l_size`

(optional) Size of the object in bytes.

`md5`

(optional) Base64-encoded MD5 hash of the object data.

`time_created`

(optional) The date and time the object was created, as described in[RFC 2616](https://tools.ietf.org/html/rfc2616#section-14.29).

`time_modified`

(required) The date and time the object was modified, as described in[RFC 2616](https://tools.ietf.org/rfc/rfc2616#section-14.29).

`etag`

(optional) The current entity tag (ETag) for the object.

`storage_tier`

(optional) The storage tier that the object is stored in.

Allowed values are: 'Standard', 'InfrequentAccess', 'Archive'

`archival_state`

(optional) Archival state of an object. This field is set only for objects in Archive tier.

Allowed values are: 'Archived', 'Restoring', 'Restored'

`version_id`

(required) VersionId of the object.

`is_delete_marker`

(required) This flag will indicate if the version is deleted or not.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_OBJECT_VERSION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_object_storage_object_version_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OBJECT_STORAGE_OBJECT_VERSION_COLLECTION_T Type

To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`items`

(required) An array of object version summaries.

`prefixes`

(optional) Prefixes that are common to the results returned by the request if the request specified a delimiter.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_PATTERN_DETAILS_T Type

Specifying inclusion and exclusion patterns.

Syntax
```

```

Fields

Field Description

`inclusion_patterns`

(optional) An array of glob patterns to match the object names to include. An empty array includes all objects in the bucket. Exclusion patterns take precedence over inclusion patterns. A Glob pattern is a sequence of characters to match text. Any character that appears in the pattern, other than the special pattern characters described below, matches itself. Glob patterns must be between 1 and 1024 characters. The special pattern characters have the following meanings: \\ Escapes the following character * Matches any string of characters. ? Matches any single character . [...] Matches a group of characters. A group of characters can be: A set of characters, for example: [Zafg9@]. This matches any character in the brackets. A range of characters, for example: [a-z]. This matches any character in the range. [a-f] is equivalent to [abcdef]. For character ranges only the CHARACTER-CHARACTER pattern is supported. [ab-yz] is not valid [a-mn-z] is not valid Character ranges can not start with ^ or : To include a '-' in the range, make it the first or last character.

`exclusion_patterns`

(optional) An array of glob patterns to match the object names to exclude. An empty array is ignored. Exclusion patterns take precedence over inclusion patterns. A Glob pattern is a sequence of characters to match text. Any character that appears in the pattern, other than the special pattern characters described below, matches itself. Glob patterns must be between 1 and 1024 characters. The special pattern characters have the following meanings: \\ Escapes the following character * Matches any string of characters. ? Matches any single character . [...] Matches a group of characters. A group of characters can be: A set of characters, for example: [Zafg9@]. This matches any character in the brackets. A range of characters, for example: [a-z]. This matches any character in the range. [a-f] is equivalent to [abcdef]. For character ranges only the CHARACTER-CHARACTER pattern is supported. [ab-yz] is not valid [a-mn-z] is not valid Character ranges can not start with ^ or : To include a '-' in the range, make it the first or last character.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_PREAUTHENTICATED_REQUEST_T Type

Pre-authenticated requests provide a way to let users access a bucket or an object without having their own credentials. When you create a pre-authenticated request, a unique URL is generated. Users in your organization, partners, or third parties can use this URL to access the targets identified in the pre-authenticated request. See[Using Pre-Authenticated Requests](https://docs.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm). To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier to use when directly addressing the pre-authenticated request.

`name`

(required) The user-provided name of the pre-authenticated request.

`access_uri`

(required) The URI to embed in the URL when using the pre-authenticated request.

`object_name`

(optional) The name of the object that is being granted access to by the pre-authenticated request. Avoid entering confidential information. The object name can be null and if so, the pre-authenticated request grants access to the entire bucket. Example: test/object1.log

`bucket_listing_action`

(optional) Specifies whether a list operation is allowed on a PAR with accessType \"AnyObjectRead\" or \"AnyObjectReadWrite\". Deny: Prevents the user from performing a list operation. ListObjects: Authorizes the user to perform a list operation.

Allowed values are: 'Deny', 'ListObjects'

`access_type`

(required) The operation that can be performed on this resource.

Allowed values are: 'ObjectRead', 'ObjectWrite', 'ObjectReadWrite', 'AnyObjectWrite', 'AnyObjectRead', 'AnyObjectReadWrite'

`time_expires`

(required) The expiration date for the pre-authenticated request as per[RFC 3339](https://tools.ietf.org/html/rfc3339). After this date the pre-authenticated request will no longer be valid.

`time_created`

(required) The date when the pre-authenticated request was created as per specification[RFC 3339](https://tools.ietf.org/html/rfc3339).

`full_path`

(optional) The full Path for the object.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_PREAUTHENTICATED_REQUEST_SUMMARY_T Type

Get summary information about pre-authenticated requests.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier to use when directly addressing the pre-authenticated request.

`name`

(required) The user-provided name of the pre-authenticated request.

`object_name`

(optional) The name of object that is being granted access to by the pre-authenticated request. This can be null and if it is, the pre-authenticated request grants access to the entire bucket.

`bucket_listing_action`

(optional) Specifies whether a list operation is allowed on a PAR with accessType \"AnyObjectRead\" or \"AnyObjectReadWrite\". Deny: Prevents the user from performing a list operation. ListObjects: Authorizes the user to perform a list operation.

`access_type`

(required) The operation that can be performed on this resource.

Allowed values are: 'ObjectRead', 'ObjectWrite', 'ObjectReadWrite', 'AnyObjectWrite', 'AnyObjectRead', 'AnyObjectReadWrite'

`time_expires`

(required) The expiration date for the pre-authenticated request as per[RFC 3339](https://tools.ietf.org/html/rfc3339). After this date the pre-authenticated request will no longer be valid.

`time_created`

(required) The date when the pre-authenticated request was created as per[RFC 3339](https://tools.ietf.org/html/rfc3339).

### DBMS_CLOUD_OCI_OBJECT_STORAGE_PUT_OBJECT_LIFECYCLE_POLICY_DETAILS_T Type

Creates a new object lifecycle policy for a bucket.

Syntax
```

```

Fields

Field Description

`items`

(optional) The bucket's set of lifecycle policy rules.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_SSE_CUSTOMER_KEY_DETAILS_T Type

Specifies the details of the customer-provided encryption key (SSE-C) associated with an object.

Syntax
```

```

Fields

Field Description

`algorithm`

(required) Specifies the encryption algorithm. The only supported value is \"AES256\".

Allowed values are: 'AES256'

`key`

(required) Specifies the base64-encoded 256-bit encryption key to use to encrypt or decrypt the object data.

`key_sha256`

(required) Specifies the base64-encoded SHA256 hash of the encryption key. This value is used to check the integrity of the encryption key.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_REENCRYPT_OBJECT_DETAILS_T Type

The details used to re-encrypt the data encryption keys associated with an object. You can only specify either a kmsKeyId or an sseCustomerKey in the request payload, not both. If the request payload is empty, the object is encrypted using the encryption key assigned to the bucket. The bucket encryption mechanism can either be a master encryption key managed by Oracle or the Vault service. - The sseCustomerKey field specifies the customer-provided encryption key (SSE-C) that will be used to re-encrypt the data encryption keys of the object and its chunks. - The sourceSSECustomerKey field specifies information about the customer-provided encryption key that is currently associated with the object source. Specify a value for the sourceSSECustomerKey only if the object is encrypted with a customer-provided encryption key.

Syntax
```

```

Fields

Field Description

`kms_key_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the master encryption key used to call the Vault service to re-encrypt the data encryption keys associated with the object and its chunks. If the kmsKeyId value is empty, whether null or an empty string, the API will perform re-encryption by using the kmsKeyId associated with the bucket or the master encryption key managed by Oracle, depending on the bucket encryption mechanism.

`sse_customer_key`

(optional)

`source_sse_customer_key`

(optional)

### DBMS_CLOUD_OCI_OBJECT_STORAGE_RENAME_OBJECT_DETAILS_T Type

To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`source_name`

(required) The name of the source object to be renamed.

`new_name`

(required) The new name of the source object. Avoid entering confidential information.

`src_obj_if_match_e_tag`

(optional) The if-match entity tag (ETag) of the source object.

`new_obj_if_match_e_tag`

(optional) The if-match entity tag (ETag) of the new object.

`new_obj_if_none_match_e_tag`

(optional) The if-none-match entity tag (ETag) of the new object. The only valid value is '*', which indicates request should fail if the new object already exists.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_REPLICATION_POLICY_T Type

The details of a replication policy.

Syntax
```

```

Fields

Field Description

`id`

(required) The id of the replication policy.

`name`

(required) The name of the policy.

`destination_region_name`

(required) The destination region to replicate to, for example \"us-ashburn-1\".

`destination_bucket_name`

(required) The bucket to replicate to in the destination region. Replication policy creation does not automatically create a destination bucket. Create the destination bucket before creating the policy.

`time_created`

(required) The date when the replication policy was created as per[RFC 3339](https://tools.ietf.org/html/rfc3339).

`time_last_sync`

(required) Changes made to the source bucket before this time has been replicated.

`status`

(required) The replication status of the policy. If the status is CLIENT_ERROR, once the user fixes the issue described in the status message, the status will become ACTIVE.

Allowed values are: 'ACTIVE', 'CLIENT_ERROR'

`status_message`

(required) A human-readable description of the status.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_REPLICATION_POLICY_SUMMARY_T Type

The summary of a replication policy.

Syntax
```

```

Fields

Field Description

`id`

(required) The id of the replication policy.

`name`

(required) The name of the policy.

`destination_region_name`

(required) The destination region to replicate to, for example \"us-ashburn-1\".

`destination_bucket_name`

(required) The bucket to replicate to in the destination region. Replication policy creation does not automatically create a destination bucket. Create the destination bucket before creating the policy.

`time_created`

(required) The date when the replication policy was created as per[RFC 3339](https://tools.ietf.org/html/rfc3339).

`time_last_sync`

(required) Changes made to the source bucket before this time has been replicated.

`status`

(required) The replication status of the policy. If the status is CLIENT_ERROR, once the user fixes the issue described in the status message, the status will become ACTIVE.

Allowed values are: 'ACTIVE', 'CLIENT_ERROR'

`status_message`

(required) A human-readable description of the status.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_REPLICATION_SOURCE_T Type

The details of a replication source bucket that replicates to a target destination bucket.

Syntax
```

```

Fields

Field Description

`policy_name`

(required) The name of the policy.

`source_region_name`

(required) The source region replicating data from, for example \"us-ashburn-1\".

`source_bucket_name`

(required) The source bucket replicating data from.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_RESTORE_OBJECTS_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`object_name`

(required) An object that is in an archive storage tier and needs to be restored.

`hours`

(optional) The number of hours for which this object will be restored. By default objects will be restored for 24 hours. You can instead configure the duration using the hours parameter.

`version_id`

(optional) The versionId of the object to restore. Current object version is used by default.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_RETENTION_RULE_T Type

The details of a retention rule.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier for the retention rule.

`display_name`

(required) User specified name for the retention rule.

`duration`

(optional)

`etag`

(required) The entity tag (ETag) for the retention rule.

`time_rule_locked`

(optional) The date and time as per[RFC 3339](https://tools.ietf.org/html/rfc3339)after which this rule becomes locked. and can only be deleted by deleting the bucket.

`time_created`

(required) The date and time that the retention rule was created as per[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_modified`

(required) The date and time that the retention rule was modified as per[RFC3339](https://tools.ietf.org/html/rfc3339).

### DBMS_CLOUD_OCI_OBJECT_STORAGE_RETENTION_RULE_SUMMARY_T Type

The summary of a retention rule.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier for the retention rule.

`display_name`

(required) User specified name for the retention rule.

`duration`

(optional)

`etag`

(required) The entity tag (ETag) for the retention rule.

`time_rule_locked`

(optional) The date and time as per[RFC 3339](https://tools.ietf.org/html/rfc3339)after which this rule becomes locked. and can only be deleted by deleting the bucket.

`time_created`

(required) The date and time that the retention rule was created as per[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_modified`

(required) The date and time that the retention rule was modified as per[RFC3339](https://tools.ietf.org/html/rfc3339).

### DBMS_CLOUD_OCI_OBJECT_STORAGE_RETENTION_RULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_object_storage_retention_rule_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OBJECT_STORAGE_RETENTION_RULE_COLLECTION_T Type

Retention rule collection.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of retention rule summaries.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_RETENTION_RULE_DETAILS_T Type

The details to create or update a retention rule.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-specified name for the retention rule. Names can be helpful in identifying retention rules. Avoid entering confidential information.

`duration`

(optional)

`time_rule_locked`

(optional) The date and time as per[RFC 3339](https://tools.ietf.org/html/rfc3339)after which this rule is locked and can only be deleted by deleting the bucket. Once a rule is locked, only increases in the duration are allowed and no other properties can be changed. This property cannot be updated for rules that are in a locked state. Specifying it when a duration is not specified is considered an error.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_UPDATE_BUCKET_DETAILS_T Type

To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`namespace`

(optional) The Object Storage namespace in which the bucket lives.

`compartment_id`

(optional) The compartmentId for the compartment to move the bucket to.

`name`

(optional) The name of the bucket. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods. Bucket names must be unique within an Object Storage namespace. Avoid entering confidential information. Example: my-new-bucket1

`metadata`

(optional) Arbitrary string, up to 4KB, of keys and values for user-defined metadata.

`public_access_type`

(optional) The type of public access enabled on this bucket. A bucket is set to `NoPublicAccess` by default, which only allows an authenticated caller to access the bucket and its contents. When `ObjectRead` is enabled on the bucket, public access is allowed for the `GetObject`, `HeadObject`, and `ListObjects` operations. When `ObjectReadWithoutList` is enabled on the bucket, public access is allowed for the `GetObject` and `HeadObject` operations.

Allowed values are: 'NoPublicAccess', 'ObjectRead', 'ObjectReadWithoutList'

`object_events_enabled`

(optional) Whether or not events are emitted for object state changes in this bucket. By default, `objectEventsEnabled` is set to `false`. Set `objectEventsEnabled` to `true` to emit events for object state changes. For more information about events, see[Overview of Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsoverview.htm).

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}

`kms_key_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Key Management master encryption key to associate with the specified bucket. If this value is empty, the Update operation will remove the associated key, if there is one, from the bucket. (The bucket will continue to be encrypted, but with an encryption key managed by Oracle.)

`versioning`

(optional) The versioning status on the bucket. If in state `Enabled`, multiple versions of the same object can be kept in the bucket. When the object is overwritten or deleted, previous versions will still be available. When versioning is `Suspended`, the previous versions will still remain but new versions will no longer be created when overwitten or deleted. Versioning cannot be disabled on a bucket once enabled.

Allowed values are: 'Enabled', 'Suspended'

`auto_tiering`

(optional) The auto tiering status on the bucket. If in state `InfrequentAccess`, objects are transitioned automatically between the 'Standard' and 'InfrequentAccess' tiers based on the access pattern of the objects. When auto tiering is `Disabled`, there will be no automatic transitions between storage tiers.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_UPDATE_NAMESPACE_METADATA_DETAILS_T Type

UpdateNamespaceMetadataDetails is used to update the NamespaceMetadata. To update NamespaceMetadata, a user must have OBJECTSTORAGE_NAMESPACE_UPDATE permission.

Syntax
```

```

Fields

Field Description

`default_s3_compartment_id`

(optional) The updated compartment id for use by an S3 client, if this field is set.

`default_swift_compartment_id`

(optional) The updated compartment id for use by a Swift client, if this field is set.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_UPDATE_OBJECT_STORAGE_TIER_DETAILS_T Type

To change the storage tier of an object, we specify the object name and the desired storage tier in the body. Objects can be moved between Standard and InfrequentAccess tiers and from Standard or InfrequentAccess tier to Archive tier. If a version id is specified, only the specified version of the object is moved to a different storage tier, else the current version is used.

Syntax
```

```

Fields

Field Description

`object_name`

(required) An object for which the storage tier needs to be changed.

`storage_tier`

(required) The storage tier that the object should be moved to.

Allowed values are: 'Standard', 'InfrequentAccess', 'Archive'

`version_id`

(optional) The versionId of the object. Current object version is used by default.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_UPDATE_RETENTION_RULE_DETAILS_T Type

The details to update a retention rule.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-specified name for the retention rule. Names can be helpful in identifying retention rules. Avoid entering confidential information.

`duration`

(optional)

`time_rule_locked`

(optional) The date and time as per[RFC 3339](https://tools.ietf.org/html/rfc3339)after which this rule is locked and can only be deleted by deleting the bucket. Once a rule is locked, only increases in the duration are allowed and no other properties can be changed. This property cannot be updated for rules that are in a locked state. Specifying it when a duration is not specified is considered an error.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_WORK_REQUEST_RESOURCE_T Type

Syntax
```

```

Fields

Field Description

`action_type`

(optional) The status of the work request.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'RELATED', 'IN_PROGRESS', 'READ', 'WRITTEN'

`entity_type`

(optional) The resource type the work request affects.

`identifier`

(optional) The resource type identifier.

`entity_uri`

(optional) The URI path that you can use for a GET request to access the resource metadata.

`metadata`

(optional) The metadata of the resource.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_object_storage_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OBJECT_STORAGE_WORK_REQUEST_T Type

A description of workRequest status.

Syntax
```

```

Fields

Field Description

`operation_type`

(optional) The type of work request.

Allowed values are: 'COPY_OBJECT', 'REENCRYPT'

`status`

(optional) The status of the specified work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'COMPLETED', 'CANCELING', 'CANCELED'

`id`

(optional) The id of the work request.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the work request. Work requests are scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources and those resources are not in the same compartment, the OCID of the primary resource is used. For example, you can copy an object in a bucket in one compartment to a bucket in another compartment. In this case, the OCID of the source compartment is used.

`resources`

(optional)

`percent_complete`

(optional) Percentage of the work request completed.

`time_accepted`

(optional) The date and time the work request was created, as described in[RFC 3339](https://tools.ietf.org/html/rfc3339).

`time_started`

(optional) The date and time the work request was started, as described in[RFC 3339](https://tools.ietf.org/html/rfc3339).

`time_finished`

(optional) The date and time the work request was finished, as described in[RFC 3339](https://tools.ietf.org/html/rfc3339).

### DBMS_CLOUD_OCI_OBJECT_STORAGE_WORK_REQUEST_ERROR_T Type

Syntax
```

```

Fields

Field Description

`code`

(optional) A machine-usable code for the error that occurred. For the list of error codes, see[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(optional) A human-readable description of the issue that produced the error.

`l_timestamp`

(optional) The time the error occurred.

### DBMS_CLOUD_OCI_OBJECT_STORAGE_WORK_REQUEST_LOG_ENTRY_T Type

Syntax
```

```

Fields

Field Description

`message`

(optional) Human-readable log message.

`l_timestamp`

(optional) The date and time the log message was written, as described in[RFC 3339](https://tools.ietf.org/html/rfc3339).

### DBMS_CLOUD_OCI_OBJECT_STORAGE_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(optional) The type of work request.

Allowed values are: 'COPY_OBJECT', 'REENCRYPT'

`status`

(optional) The status of a specified work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'COMPLETED', 'CANCELING', 'CANCELED'

`id`

(optional) The id of the work request.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the work request. Work requests are scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources and those resources are not in the same compartment, the OCID of the primary resource is used. For example, you can copy an object in a bucket in one compartment to a bucket in another compartment. In this case, the OCID of the source compartment is used.

`resources`

(optional)

`percent_complete`

(optional) Percentage of the work request completed.

`time_accepted`

(optional) The date and time the work request was created, as described in[RFC 3339](https://tools.ietf.org/html/rfc3339).

`time_started`

(optional) The date and time the work request was started, as described in[RFC 3339](https://tools.ietf.org/html/rfc3339).

`time_finished`

(optional) The date and time the work request was finished, as described in[RFC 3339](https://tools.ietf.org/html/rfc3339).

- [Object Storage Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-309B9D22-394F-4A44-B15C-9CBE1612E4F8)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-40EBBD9A-ACA3-4643-9EE3-258B72FC15A5)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_BUCKET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-5E7A3F85-6E86-408E-A9AA-E2E76BCB937A)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_BUCKET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-775F3BAA-E442-4BD5-BB79-0929B2FFB799)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_COMMIT_MULTIPART_UPLOAD_PART_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-2BC0062D-267A-4798-81A3-7611ACA8EE5C)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_COMMIT_MULTIPART_UPLOAD_PART_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-D924AB45-F3FD-41DF-BF50-AED89C778727)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_NUMBER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-57B6B3F2-23FD-453B-89DB-9FECB8EA3093)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_COMMIT_MULTIPART_UPLOAD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-648CDCEB-141E-437A-AF54-D794DD8E26CE)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_COPY_OBJECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-6F105A28-93F3-40BC-AF1B-3219DF85779E)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_CREATE_BUCKET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-77B071C4-39C7-42AA-93D7-71966F9950D1)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_CREATE_MULTIPART_UPLOAD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-6C793AFB-B983-4E74-88C5-112A2B0AEED3)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_CREATE_PREAUTHENTICATED_REQUEST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-4C21E850-900D-4B64-8E71-BFC4C3EC6F26)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_CREATE_REPLICATION_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-8873B768-AAA0-433C-AA8E-1C39512EB99E)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_DURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-5DDB1BB0-7764-431D-BD32-698670CF562A)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_CREATE_RETENTION_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-B0DE6090-EC37-4A27-8C3F-E85DCC050FFC)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-30160499-93F0-497A-B45A-CD975BFBB9AC)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_OBJECT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-368C1A2F-AC6B-4D48-B545-097DDDDBE6E3)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_OBJECT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-924A646A-0259-4194-9B75-61301B82EEEB)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_LIST_OBJECTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-86168980-97FF-41FB-A0A0-295F103F6A14)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_MULTIPART_UPLOAD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-5C9E4FC1-B33E-4A30-A68C-3C8CDD95AEA4)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_MULTIPART_UPLOAD_PART_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-C8D9D2C7-3B7A-4A4C-9319-98313E88D803)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_NAMESPACE_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-2DEEC48A-4A6A-420A-837C-DABE09CAD77B)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_OBJECT_NAME_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-3E9DFA23-9FC8-4176-BF78-927B76FB51D5)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_OBJECT_LIFECYCLE_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-CE51B71E-3B42-4FA5-A033-3BD679995A23)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_OBJECT_LIFECYCLE_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-1B925494-5B08-4C03-A52C-C0944051CC3E)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_OBJECT_LIFECYCLE_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-88863B4E-60A4-45E7-9377-19BF2CAE411E)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_OBJECT_VERSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-D68DABD8-AE40-4D27-BE92-94B1507D6E80)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_OBJECT_VERSION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-6DF9A3ED-08FD-4465-969A-E0CCBC8B445B)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_OBJECT_VERSION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-0D9F8104-6781-4F87-8EF1-90C339298802)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_PATTERN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-CD39219B-7FF5-43A7-B1E0-1DC80E702938)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_PREAUTHENTICATED_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-AF91B9B5-BA63-4D32-80C9-251524D57234)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_PREAUTHENTICATED_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-0C80F209-95C7-4EA7-A88A-2FA8F0A58E9E)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_PUT_OBJECT_LIFECYCLE_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-DB112B77-8A07-49BC-A36F-6CAFDB3884A3)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_SSE_CUSTOMER_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-539C7CC5-EA54-42D3-98DF-7652FBC884BC)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_REENCRYPT_OBJECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-53C4E226-87E9-4F7A-87B2-00063D2852B4)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_RENAME_OBJECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-82EE9D90-2661-4A84-A61A-70EB33728418)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_REPLICATION_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-BD1A1323-6F0C-4B7F-90FD-171204A851F0)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_REPLICATION_POLICY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-A820BC93-EE02-42E4-866B-7BB3AF2E4075)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_REPLICATION_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-E20C0E90-51AA-4F15-9F7F-C1565B3006EF)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_RESTORE_OBJECTS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-19AB902D-DF9C-452B-A844-C38F1B591613)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_RETENTION_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-D9DFC6F5-1040-4DCE-84D8-28AE8DC17B97)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_RETENTION_RULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-4EEAB779-C9FB-4D89-9411-A8D674ABC3B4)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_RETENTION_RULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-29CBD110-AFD6-430F-892D-473A396212DF)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_RETENTION_RULE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-8D37EBF4-1BE7-419D-8D78-3A9AD3D41657)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_RETENTION_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-6478CE20-0570-4868-B9A5-A73D549983D1)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_UPDATE_BUCKET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-F6BB4A63-A181-4040-9B4B-283A0F93094F)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_UPDATE_NAMESPACE_METADATA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-60316367-9C25-4A5A-B25E-F8D1EA7C1169)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_UPDATE_OBJECT_STORAGE_TIER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-18B9A113-1A96-4F53-BB29-D5AB19FDAA2D)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_UPDATE_RETENTION_RULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-C169D29B-A20F-41D7-96EF-F20F4895D999)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-1853E977-08A3-490D-9A14-BFB947164BC8)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-CF0C165E-58D1-4C4C-A25F-8C6863A2C803)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-5474E2E0-C7EF-4189-8A1D-7573439953A4)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-7E5646B6-1D08-49BA-9180-6D15B66670FF)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-950BD619-AB02-4F4D-9DF8-40FAD2F6155F)
- [DBMS_CLOUD_OCI_OBJECT_STORAGE_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/object_storage_t.html#ADSDK-GUID-565A8E72-5AF1-477C-90E7-C5809CE58802)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
