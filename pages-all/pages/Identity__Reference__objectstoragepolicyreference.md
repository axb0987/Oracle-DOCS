# Details for Object Storage and Archive Storage
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/objectstoragepolicyreference.htm
- Fetched: 2026-09-05 02:15 CDT

# Details for Object Storage and Archive Storage

This topic covers details for writing policies to control access to Archive Storage and Object Storage.
Tip  
  
The object lifecycle policies feature requires that you grant permissions to the Object Storage service to archive and delete objects on your behalf. See[Using Object Lifecycle Policies](https://docs.oracle.com/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm#permissions)for more information.

## Resource-Types

### Individual Resource-Types

`objectstorage-namespaces`

`buckets`

`objects`

### Aggregate Resource-Type

`object-family`

A policy that uses`<verb> object-family`is equivalent to writing one with a separate`<verb> <individual resource-type>`statement for each of the individual resource-types.

See the table in[Details for Verb + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/objectstoragepolicyreference.htm#Details)for details of the API operations covered by each verb, for each individual resource-type included in`object-family`.

## Supported Variables

Object Storage supports all the general variables (see[General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General)), plus the ones listed here:

Operations for This Resource-Type... Can Use This Variable Variable Type Comments
`buckets`and`objects``target.bucket.name`String and Patterns Use this variable to control access to a specific bucket. Important: Condition matching is case insensitive. If you have a bucket named "BucketA" and a bucket named "bucketA", the condition`where target.bucket.name="BucketA"`applies to both. To avoid potential issues with resource names in policy, give your resources distinct names.
`buckets`and`objects``target.bucket.tag.< TagNamespace >.< TagKeyDefinition >`String Use this variable to control access to the buckets that have the specific tag. See[Let users write objects to Object Storage buckets](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm#write-objects-to-buckets). Important: You cannot use this variable for`CreateBucket`operations and operations that involve multiple buckets such as`ListBucket`.
`objects``target.object.name`String and Patterns Use this variable to control access to a specific object or object patterns.
Note  
  
The`request.ipv4.ipaddress`and the`request.vcn.id`variables are deprecated. Instead of using these variables, create a network source to specify either an IP address range or a specific VCN ID. You can then use the network source in your policy to restrict access to only requests coming from the allowed networks. For more information, see[Overview of Network Sources](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/../networksources/managingnetworksources.htm).

## Details for Verb + Resource-Type Combinations

The following tables show the[permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm)and API operations covered by each verb. The level of access is cumulative as you go from`inspect`&gt;`read`&gt;`use`&gt;`manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access.

### For object-family Resource Types

[objectstorage-namespaces](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/objectstoragepolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
read OBJECTSTORAGE_NAMESPACE_READ`GetNamespace`none
use OBJECTSTORAGE_NAMESPACE_READ`GetNamespace`none
manage OBJECTSTORAGE_NAMESPACE_READ

OBJECTSTORAGE_NAMESPACE_UPDATE`GetNamespace`with optional`compartmentId`parameter

`GetNamespaceMetadata`

`UpdateNamespaceMetadata`none

[buckets](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/objectstoragepolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

BUCKET_INSPECT

`HeadBucket`

`ListBuckets`

none
read

INSPECT +

BUCKET_READ

INSPECT +

`GetBucket`

`ListMultipartUploads`

`GetObjectLifecyclePolicy`

`GetRetentionRule`

`ListRetentionRules`

`GetReplicationPolicy`

`ListReplicationPolicies`

`ListReplicationSources`

none
use

READ +

BUCKET_UPDATE

READ +

`UpdateBucket`

`DeleteObjectLifecyclePolicy`

`ReencryptBucket``PutObjectLifecyclePolicy`
manage

USE +

BUCKET_CREATE

BUCKET_DELETE

PAR_MANAGE

RETENTION_RULE_MANAGE

RETENTION_RULE_LOCK (if using optional rule locking)

USE +

`CreateBucket`

`DeleteBucket`

`CreatePreauthenticatedRequest`

`GetPreauthenticatedRequest`

`ListPreauthenticatedRequest`

`DeletePreauthenticatedRequest`

`CreateRetentionRule`

`UpdateRetentionRule`

`DeleteRetentionRule`

`CreateReplicationPolicy`,`DeleteReplicationPolicy`,`MakeBucketWritable`(these operations also need`manage objects`)

[objects](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/objectstoragepolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

OBJECT_INSPECT

`HeadObject`

`ListObjects`

`ListMultipartUploadParts`

none
read

INSPECT +

OBJECT_READ

INSPECT +

`GetObject`

none
use

READ +

OBJECT_OVERWRITE

READ +

`ReencryptObject`

READ +

`PutObject`(USE allows`PutObject`to overwrite existing objects, but creating a new object also requires OBJECT_CREATE)

`CreateMultipartUpload`,`UploadPart`,`CommitMultipartUpload`(these operations also need`manage objects`)
manage

USE +

OBJECT_CREATE

OBJECT_DELETE

OBJECT_VERSION_DELETE

OBJECT_RESTORE

OBJECT_UPDATE_TIER

USE +

`CreateObject`

`RenameObject`

`RestoreObject`

`DeleteObject`

`DeleteObjectVersion`

`UpdateObjectStorageTier`

`CreateMultipartUpload`

`UploadPart`

`CommitMultipartUpload`

`AbortMultipartUpload`

`PutObjectLifecyclePolicy`(also needs`manage objects`)

`CreateReplicationPolicy`,`DeleteReplicationPolicy`,`MakeBucketWritable`(these operations also need`manage buckets`)

## Permissions Required for Each API Operation

The following table lists the API operations in a logical order, grouped by resource type.

For information about permissions, see[Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/../Concepts/policyadvancedfeatures.htm#Permissi).

API Operation Permissions Required to Use the Operation
`GetNamespace`

API requires no permissions and returns the caller's namespace. Use the API to validate your credentials.

OBJECTSTORAGE_NAMESPACE_READ permission is required if you include the optional`compartmentId`parameter. Use the`compartmentId`parameter to find the namespace for a third-party tenancy.
`GetNamespaceMetadata`OBJECTSTORAGE_NAMESPACE_READ
`UpdateNamespaceMetadata`OBJECTSTORAGE_NAMESPACE_UPDATE
`CreateBucket`BUCKET_CREATE

If the KMS Key ID is provided to the operation, the following additional permissions are required:
- KEY_ASSOCIATE
- The objectstorage-&lt;location&gt; subject must also have: KEY_ENCRYPT, KEY_DECRYPT, KEY_READ.
`UpdateBucket`BUCKET_UPDATE

For a customer-managed key encrypted bucket, the objectstorage-&lt;location&gt; subject must also have: KEY_ENCRYPT, and KEY_DECRYPT.
`GetBucket`BUCKET_READ

For a customer-managed key encrypted bucket, the objectstorage-&lt;location&gt; subject must have KEY_DECRYPT.
`HeadBucket`BUCKET_INSPECT

For a customer-managed key encrypted bucket, the objectstorage-&lt;location&gt; subject must have KEY_DECRYPT.
`ListBuckets`BUCKET_INSPECT
`DeleteBucket`BUCKET_DELETE
`ReencryptBucket`BUCKET_UPDATE

The objectstorage-&lt;location&gt; subject must also have: KEY_ENCRYPT, and KEY_DECRYPT.
`PutObject`

The permission required depends on whether the object already exists in the bucket:
- OBJECT_CREATE is required when an object with that name doesn't already exist in the bucket.
- OBJECT_OVERWRITE is required when an object with that name already exists in the bucket.

For a customer-managed key encrypted bucket, the objectstorage-&lt;location&gt; subject must have KEY_ENCRYPT.
`RenameObject`OBJECT_CREATE and OBJECT_OVERWRITE
`GetObject`OBJECT_READ

For a customer-managed key encrypted bucket, the objectstorage-&lt;location&gt; subject must have KEY_DECRYPT.
`HeadObject`OBJECT_READ or OBJECT_INSPECT

For a customer-managed key encrypted bucket, the objectstorage-&lt;location&gt; subject must have KEY_DECRYPT.
`DeleteObject`OBJECT_DELETE
`DeleteObjectVersion`OBJECT_VERSION_DELETE
`ListObjects`OBJECT_INSPECT
`ListObjectVersions`OBJECT_INSPECT
`ReencryptObject`OBJECT_READ, OBJECT_OVERWRITE

For a customer-managed key encrypted bucket, the following permissions are required:
- KEY_ASSOCIATE
- Additionally, the objectstorage-&lt;location&gt; subject must also have KEY_ENCRYPT, KEY_DECRYPT, and KEY_READ.
`RestoreObjects`OBJECT_RESTORE
`UpdateObjectStorageTier`OBJECT_UPDATE_TIER
`CreateMultipartUpload`OBJECT_CREATE and OBJECT_OVERWRITE

For a customer-managed key encrypted bucket, the objectstorage-&lt;location&gt; subject must have KEY_ENCRYPT.
`UploadPart`OBJECT_CREATE and OBJECT_OVERWRITE

For a customer-managed key encrypted bucket, the objectstorage-&lt;location&gt; subject must have KEY_ENCRYPT.
`CommitMultipartUpload`BUCKET_READ, OBJECT_CREATE, OBJECT_READ, and OBJECT_OVERWRITE
`ListMultipartUploadParts`OBJECT_INSPECT
`ListMultipartUploads`BUCKET_READ
`AbortMultipartUpload`OBJECT_DELETE
`CreatePreauthenticatedRequest`PAR_MANAGE
`GetPreauthenticatedRequest`PAR_MANAGE or BUCKET_READ
`ListPreauthenticatedRequests`PAR_MANAGE or BUCKET_READ
`DeletePreauthenticatedRequest`PAR_MANAGE
`PutObjectLifecyclePolicy`BUCKET_UPDATE, OBJECT_CREATE, and OBJECT_DELETE

Additionally, the objectstorage-&lt;location&gt; subject must also have: BUCKET_INSPECT, BUCKET_READ, OBJECT_INSPECT.

If the bucket the lifecycle policy applies to is a customer-managed key encrypted bucket then the objectstorage-&lt;location&gt; subject must also have: KEY_ENCRYPT, and KEY_DECRYPT.

If the`PutObjectLifeCyclePolicy`operation also updates the object tier for example, from default to INFREQUENT_ACCESS, the user and the objectstorage-&lt;location&gt; subject must be granted OBJECT_UPDATE_TIER permission.
`GetObjectLifecyclePolicy`BUCKET_READ

For a customer-managed key encrypted bucket, the objectstorage-&lt;location&gt; subject must have KEY_DECRYPT.
`DeleteObjectLifecyclePolicy`BUCKET_UPDATE

For a customer-managed key encrypted bucket, the objectstorage-&lt;location&gt; subject must also have: KEY_ENCRYPT, and KEY_DECRYPT.
`CreateRetentionRule`BUCKET_UPDATE and RETENTION_RULE_MANAGE (and RETENTION_RULE_LOCK)

For a customer-managed key encrypted bucket, the objectstorage-&lt;location&gt; subject must also have: KEY_ENCRYPT, and KEY_DECRYPT.
`GetRetentionRule`BUCKET_READ
`ListRetentionRule`BUCKET_READ
`UpdateRetentionRule`BUCKET_UPDATE and RETENTION_RULE_MANAGE (and RETENTION_RULE_LOCK)

For a customer-managed key encrypted bucket, the objectstorage-&lt;location&gt; subject must also have: KEY_ENCRYPT, and KEY_DECRYPT.
`DeleteRetentionRule`BUCKET_UPDATE and RETENTION_RULE_MANAGE

For a customer-managed key encrypted bucket, the objectstorage-&lt;location&gt; subject must also have: KEY_ENCRYPT, and KEY_DECRYPT.
`CopyObjectRequest`OBJECT_READ, and the second user permission required depends on whether the object already exists in the bucket:
- OBJECT_CREATE is required when an object with that name doesn't already exist in the bucket.
- OBJECT_OVERWRITE is required when an object with that name already exists in the bucket.

Additionally, the objectstorage-&lt;location&gt; subject requires OBJECT_READ.

For a customer-managed key encrypted bucket, the objectstorage-&lt;location&gt; subject must also have KEY_ENCRYPT, KEY_DECRYPT.
`GetWorkRequest`OBJECT_READ
`ListWorkRequests`OBJECT_INSPECT
`CancelWorkRequest`OBJECT_DELETE
`CreateReplicationPolicy`OBJECT_READ, OBJECT_CREATE, OBJECT_OVERWRITE, OBJECT_INSPECT, OBJECT_DELETE, OBJECT_RESTORE, BUCKET_READ, and BUCKET_UPDATE

The objectstorage-&lt;location&gt; subject must have the same permissions as the user.
`GetReplicationPolicy`BUCKET_READ
`DeleteReplicationPolicy`OBJECT_READ, OBJECT_CREATE, OBJECT_OVERWRITE, OBJECT_INSPECT, OBJECT_DELETE, OBJECT_RESTORE, BUCKET_READ, and BUCKET_UPDATE
`ListReplicationPolicies`BUCKET_READ
`ListReplicationSources`BUCKET_READ
`MakeBucketWritable`
