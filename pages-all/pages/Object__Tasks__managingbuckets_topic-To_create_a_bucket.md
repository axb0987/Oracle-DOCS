# Creating an Object Storage Bucket
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm
- Fetched: 2026-09-05 02:51 CDT

# Creating an Object Storage Bucket

Create a Object Storage bucket to store objects.

For information on the required permissions to create a bucket in Object Storage, see[Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets.htm#permissions).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm#)
- 

- On the Buckets list page, select Create bucket . If you need help finding the list page, see[Listing Object Storage Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
The Create bucket panel opens.
- Enter the following information:

- Bucket name : The system generates a default bucket name that reflects the current year, month, day, and time, for example bucket-2019030620230306-1359 . If you change this default to any other bucket name, use letters, numbers, dashes, underscores, and periods. Avoid entering confidential information.
- Default storage tier : Select the default tier in which you want to store your data. When you upload objects, the objects are automatically assigned to and uploaded to this tier.
- Standard is the primary, default storage tier used for[Object Storage](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/../Concepts/objectstorageoverview.htm)service data. Use this tier to store data that requires fast and immediate access. Standard buckets do, however, provide an option to assign and upload objects to different storage tiers (Infrequent Access and Archive) while remaining in the Standard bucket.
- Archive is the default storage tier used for[Archive Storage](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm)data. Use the Archive tier for storing data that requires long retention periods but not immediate access. Archived data must be restored before the data is accessible.

For more information, see[Object Storage Storage Tiers](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/../Concepts/understandingstoragetiers.htm).
- Enable auto-tiering : Enable this option to monitor and automatically move infrequently accessed objects from the Standard tier to the less expensive Infrequent Access storage tier. For more information, see[Auto-Tiering](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/../Concepts/understandingstoragetiers.htm#auto_tiering).
- Enable object versioning : Enable this option to create an object version each time the content changes or the object is deleted. For more information, see[Object Storage Versioning](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning.htm).
- Emit object events : Enable this option to allow the bucket to emit events for object state changes. For more information about events, see[Overview of Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsoverview.htm).
- Uncommited multipart uploads cleanup : Enable this option to create a lifecycle rule that automatically deletes all uncommitted multipart uploads after 7 days.
- Encryption : Select one of the following encryption key options:
- Enable Bucket Key : Enable this option to use the Bucket Key with SSE-KMS. We recommend this setting when using SSE-KMS key to reduce calls from Object Storage to KMS, which lowers PUT and GET latency, and decreases the likelihood of KMS throttling.
- Encrypt using Oracle-managed keys : Select to encrypt the bucket using Oracle-managed keys.
- Encrypt using customer-managed keys : Select to encrypt the bucket with your own keys. Select the Vault compartment and Vault that contain the master encryption key you want to use. Also select the master encryption key compartment and master encryption key. For more information about encryption, see[Overview of Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm). For details on how to create a vault, see[Managing Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults.htm).
- Bucket Scope : The bucket scope defines whether the bucket name must be a unique namespace within the tenancy and region. The bucket scope also defines whether the bucket supports virtual-hosted style URLs:
- NAMESPACE : Only supports path-style bucket access. Bucket name only needs to be unique within the tenancy and region.
- REGION : Supports both path-style and virtual-hosted URL style access, so bucket name must be unique across all tenancies in the region.
Note  
  

After the bucket scope is set, an update can only be made to change the scope from NAMESPACE to REGION . Bucket scope can't be changed from REGION to NAMESPACE .

## Tags

Add tags : Select if you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace.

For more information about tagging, see[Overview of Tagging](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm). If you're not sure whether to apply tags, skip this option (you can apply tags later) or ask your administrator.

## Resource logging

Enable to allow tracking, troubleshooting, and data insights of the Object Storage bucket you're creating.

Select Create bucket .

The bucket is created immediately and you can start uploading objects to it. Objects added to archive buckets are immediately archived and must be[restored](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm)before they're available for download.
- 

## Creating a Standard Default Storage Tier Bucket

By default, a bucket is created in the Standard Object Storage tier. You don't need to explicitly set`--storage-tier`. Standard is the primary, default storage tier used for[Object Storage](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/../Concepts/objectstorageoverview.htm)service data. Use the Standard tier for storing data that requires fast and immediate access. Standard buckets do, however, provide an option to assign and upload objects to different storage tiers (Infrequent Access and Archive), while remaining in the Standard bucket.

Use the[oci os bucket create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/create.html)command and required parameters to create a bucket:

```

```

For example:
```

```

You can also enable auto-tiering on a Standard bucket at creation time by specifying the optional`--auto-tiering InfrequentAccess`parameter. See[Auto-Tiering](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/../Concepts/understandingstoragetiers.htm#auto_tiering)for details. For example:
```

```

A Standard tier bucket is created immediately and you can start uploading objects.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

## Creating an Archive Default Storage Tier Bucket

To create an Archive tier bucket, you must explicitly set`--storage-tier Archive`. Archive is the default storage tier used for[Archive Storage](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm)service data. Use the[Archive](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm)tier for storing data that doesn't require immediate access, but requires long retention periods. Access to data in the Archive tier isn't immediate. Archived data must be[restored](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm)before the data is accessible.

```

```

For example:
```

```

An Archive Storage bucket is created and you can start uploading objects. Objects uploaded to Archive Storage buckets are immediately archived and must be[restored](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm)before they're available for download.

## Creating Public Bucket (Listing and Downloading Bucket Objects)

To create a public bucket that allows listing and downloading bucket objects, you must explicitly set`--public-access-type ObjectRead`.

```

```

For example:
```

```

## Creating Public Bucket (Downloading Bucket Objects)

To create a public bucket that allows just downloading bucket objects, you must explicitly set`--public-access-type ObjectReadWithoutList`.

```

```

For example:
```

```

## Creating a Bucket with Resource Tags

You can create standard Object Storage tier or[Archive](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm)tier buckets with[resource tags](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm).

To add resource tags when creating a bucket, set one or both of the`--defined-tags`and`--freeform-tags`options.
Tip  
  
The`--defined-tags`and`--freeform-tags`options require that the input to be a complex type formatted in valid JSON. See[Passing Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#Managing_CLI_Input_and_Output)and[Using a JSON File for Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON)for information about JSON formatting.

The following example syntax creates a standard Object Storage tier bucket with a defined tag:

```

```

Examples of defined tag formatting:
```

```

```

```

Note  
  
If you're running the CLI on a Windows computer, you might need to use the backslash (\) character to escape the strings containing the tag values. For example, a single defined tag is formatted`'{\"Logistics\": {\"Procurement\": \"Madrid Center\"}}'`

For example:
```

```

The following example syntax creates a Standard tier bucket with a free-form tag:

```

```

Examples of free-form tag formatting:
```

```

```

```

Note  
  
If you're running the CLI on a Windows computer, you might need to use the backslash (\) character to escape the strings containing the tag values. For example, a single free-form tag is formatted as`'{\"Chicago_Team\": {\"marketing_videos\"}}'`

For example:
```

```

## Assigning a Key to the Bucket

You can assign a Vault key to a bucket you're creating by including the`kms_key_id`parameter. We recommend enabling Bucket Key with SSE-KMS, we recommend this setting when using SSE-KMS key to reduce calls from Object Storage to KMS, which lowers PUT and GET latency, and decreases the likelihood of KMS throttling. For complete list of parameters and values for creating a bucket using SSE-KMS key see[`oci os bucket create`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/create.html).

You can assign a Vault key to a bucket you're creating by including the kms_key_id parameter.

```

```

where`kms_key_id`is the OCID of the[KMS key](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_create_a_new_key.htm)which is the Vault master encryption key used to encrypt the data in the bucket.

For example:
```

```

- 

Run the[CreateBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/CreateBucket)operation to create a bucket.

When accessing the Object Storage API, the bucket name is used with the Object Storage namespace name to form the request URL:
```

```

Two key properties in the payload are:
- `publicAccessType`property controls whether the bucket is private or public and limits the capability to list public bucket contents.
- `objectEventsEnabled`
