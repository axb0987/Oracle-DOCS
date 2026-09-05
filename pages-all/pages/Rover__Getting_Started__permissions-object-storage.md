# Object Storage Permissions for Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/permissions-object-storage.htm
- Fetched: 2026-09-05 02:59 CDT

# Object Storage Permissions for Roving Edge Infrastructure

Describes the details for writing user IAM policies that control access to rules for the Object Storage service for a Roving Edge Infrastructure device.

## Resource-Types

`object-family`

`buckets`

`objects`

`objectstorage-namespaces`

## Details for Verb + Resource-Type Combinations

The following tables show the permissions and API operations covered by each verb. The level of access is cumulative as you go from`inspect`&gt;`read`&gt;`use`&gt;`manage`.

### object-family

Verbs Permissions APIs Fully Covered APIs Partially Covered

inspect

BUCKET_INSPECT

OBJECT_INSPECT

HeadBucket

ListBuckets

None

read

BUCKET_INSPECT

BUCKET_READ

NBAC_READ

OBJECTSTORAGE_NAMESPACE_READ

OBJECT_INSPECT

OBJECT_READ

HeadBucket

ListBuckets

GetBucket

ListMultipartUploads

GetNamespace

GetObject

None

use

BUCKET_INSPECT

BUCKET_READ

BUCKET_UPDATE

NBAC_READ

OBJECTSTORAGE_NAMESPACE_READ

OBJECT_INSPECT

OBJECT_OVERWRITE

OBJECT_READ

None

CreateBucket (also need manage buckets)

PutObject (also need manage objects)

manage

BUCKET_CREATE

BUCKET_DELETE

BUCKET_INSPECT

BUCKET_READ

BUCKET_UPDATE

NBAC_MANAGE

NBAC_READ

OBJECTSTORAGE_NAMESPACE_READ

OBJECTSTORAGE_NAMESPACE_UPDATE

OBJECT_CREATEOBJECT_DELETE

OBJECT_INSPECT

OBJECT_OVERWRITE

OBJECT_READ

OBJECT_RESTORE

OBJECT_UPDATE_TIER

OBJECT_VERSION_DELETE

PAR_MANAGE

RETENTION_RULE_LOCK

RETENTION_RULE_MANAGE

DeleteBucket

AbortMultipartUpload

CreateBucket (also need manage buckets)

PutObject (also need manage objects)

CommitMultipartUpload (also need use objects)

CreateMultipartUpload (also need use objects)

UploadPart (also need use objects)

RenameObject (also need use objects)

DeleteObject (also need manage objects)

### buckets

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect BUCKET_INSPECT

HeadBucket

ListBuckets

None
read

BUCKET_INSPECT

BUCKET_READ

HeadBucket

ListBuckets

GetBucket

ListMultipartUploads

None
use

BUCKET_INSPECT

BUCKET_READ

BUCKET_UPDATE

None

CreateBucket (also need use buckets)
manage

BUCKET_INSPECT

BUCKET_READ

BUCKET_UPDATE

BUCKET_CREATE

BUCKET_DELETE

DeleteBucket

None

### objects

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

OBJECT_INSPECT

ListMultipart

UploadParts

ListObjects

ListObjectVersionsHeadObject

None
read

OBJECT_INSPECT

OBJECT_READ

ListMultipart

UploadParts

ListObjects

ListObjectVersionsHeadObject

GetObject

None
use

OBJECT_INSPECT

OBJECT_READ

OBJECT_OVERWRITE

None

PutObject,

CommitMultipartUpload,

CreateMultipartUpload,

UploadPart,

RenameObject (also need manage objects)
manage

OBJECT_INSPECT

OBJECT_READ

OBJECT_OVERWRITE

OBJECT_VERSION_DELETE

OBJECT_CREATE

OBJECT_DELETE

AbortMultipartUpload

PutObject,

CommitMultipartUpload,

CreateMultipartUpload,

UploadPart,

RenameObject (also need manage objects)

DeleteObject (also need manage objects)

### objectstorage-namespaces

Verbs Permissions APIs Fully Covered APIs Partially Covered

read

OBJECTSTORAGE_NAMESPACE_READ

GetNamespace

None

use

OBJECTSTORAGE_NAMESPACE_READ

GetNamespace

None

manage

OBJECTSTORAGE_NAMESPACE_READ

OBJECTSTORAGE_NAMESPACE_UPDATE

None
