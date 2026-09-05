# Getting an Object Storage Bucket's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_view_bucket_details.htm
- Fetched: 2026-09-05 02:51 CDT

# Getting an Object Storage Bucket's Details

View the details of an Object Storage bucket.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_view_bucket_details.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_view_bucket_details.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_view_bucket_details.htm#)
- 

On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
The Details tab shows the following details about the bucket organized by category:

## General

- Namespace : The namespace to which the bucket belongs.
- Compartment : The compartment to which the bucket belongs.
- Created : The timestamp of bucket creation.
- ETag : The entity tag (ETag) for the bucket.
- OCID : The Oracle Cloud ID for the bucket.

## Features

- Default storage tier : The type of storage tier such as Standard or Archive.
- Visibility : Displays whether the bucket is a private or public bucket. See[Changing an Object Storage Bucket's Visibility](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_change_the_visibility_of_a_bucket.htm).
- 

Encryption key : The master encryption key name assigned to the bucket.
- Also confirms whether bucket level key is enabled.
- Auto-tiering : Displays whether auto-tiering is enabled or disabled. See[Managing Auto-Tiering for an Object Storage Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_enable_or_disable_auto_tiering.htm).
- Emit object events : Displays whether the option to emit objects events is enabled or disabled. See[Managing Emitting Events for Object State Changes in an Object Storage Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_enable_or_disable_emitting_events_for_object_state_changes.htm).
- Object versioning : Displays whether object versioning is enabled or disabled. See[Managing Object Versioning in an Object Storage Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_enable_or_suspend_object_versioning.htm).

## Usage

- Approximate count : Approximate number of objects in the bucket.
- Approximate size : Approximate total size of all the objects.
- Uncommitted multipart uploads approximate count : The approximate number of objects with uncommitted or failed multipart uploads.
- Uncommitted multipart uploads approximate size : The total approximate size of the uncommitted multipart uploads in the bucket. If this size exceeds the threshold, a warning icon is displayed.
- 
- 

Use the[oci os bucket get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/get.html)command and required parameters to get the details of a bucket:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

## Viewing Bucket Size and Number of Objects in the Bucket

Use the`fields`parameter and its supported values to get information on the count and size of objects contained in a bucket.
- `approximateCount`is the approximate number of objects in the bucket. Count statistics are reported periodically. You might see a lag between what is displayed and the actual object count.
- `approximateSize`is the approximate total size of all objects in the bucket. Size statistics are reported periodically. You might see a lag between what is displayed and the actual size of the bucket.

For example:

```

```
For example:
```

```

- 

Run the[GetBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/GetBucket)operation to get the details of a bucket.

When accessing the Object Storage API, the bucket name is used with the Object Storage namespace name to form the request URL:
```

```
