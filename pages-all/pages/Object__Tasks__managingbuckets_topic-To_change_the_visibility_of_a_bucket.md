# Changing an Object Storage Bucket's Visibility
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_change_the_visibility_of_a_bucket.htm
- Fetched: 2026-09-05 02:51 CDT

# Changing an Object Storage Bucket's Visibility

Change the public or private visibility of an Object Storage bucket.

Buckets are private by default. For more information, see[Public Buckets](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets.htm#publicbuckets).
Important  
  
If a bucket is in a security zone, you can't change its visibility from private to public. We recommend using pre-authenticated requests instead of public buckets. Pre-authenticated requests support authorization, expiry, and scoping capabilities that aren't possible with public buckets.

See[Object Storage Pre-Authenticated Requests](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm)for details.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_change_the_visibility_of_a_bucket.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_change_the_visibility_of_a_bucket.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_change_the_visibility_of_a_bucket.htm#)
- 

- On the Buckets list page, find the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- From the Actions menu for the bucket you want, select Edit visibility .

The Edit visibility panel opens.
- 

Select Public or Private .

If you select Public to enable public access, decide whether you want to let users list the bucket contents. To set the visibility of bucket object lists, select Allow users to list objects from this bucket .
- Select Update .
- 

Use the[oci os bucket update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/update.html)command and required parameters to change the visibility of a bucket. Include the`public-access-type`parameter:

```

```

By default, the bucket is private. You can specify the bucket to be public by including the`public-access-type`parameter and one of its supported values:
- `NoPublicAccess`: Allows only an authenticated caller to access the bucket and bucket contents. This is the default visibility of a bucket.
- `ObjectReadWithoutList`: Allows public access for the`GetObject`,`HeadObject`, and`ListObjects`operations.
- 

`ObjectRead`: Allows public access for the`GetObject`and`HeadObject`operations.

For example:
```

```

To configure a public bucket to be private, run the`oci os bucket update`command with the`--public-access-type NoPublicAccess`parameter and value.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
-
