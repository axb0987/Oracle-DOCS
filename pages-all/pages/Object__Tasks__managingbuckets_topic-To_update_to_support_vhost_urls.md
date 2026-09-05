# Updating a Bucket to Support Virtual-hosted Style URLs
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_update_to_support_vhost_urls.htm
- Fetched: 2026-09-05 02:51 CDT

# Updating a Bucket to Support Virtual-hosted Style URLs

Update a bucket to support virtual-hosted style URLs.

By default, bucket scope is set to the tenancy namespace. If buckets meet the following criteria, they can be updated to a region scope which supports virtual-hosted style URLs:
- The bucket name is unique across all tenants within the region.
- Bucket names must contain only lowercase letters, numbers, and hyphens.
- Bucket names can't begin with a hyphen character and can't contain consecutive hyphen characters.
- Bucket names must be a minimum of 3 characters long and a maximum of 63 characters long.
- The bucket name acts as a subdomain, so it must also follow standard DNS naming rules.

The bucket scope can't be updated if the bucket name is already in use within the same region, doesn't meet character requirements, or doesn't follow DNS naming rules.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_update_to_support_vhost_urls.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_update_to_support_vhost_urls.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_update_to_support_vhost_urls.htm#)
- 

- On the Buckets list page, find the Object Storage bucket that you want to work with. For more information about the listing buckets page, see[Listing Object Storage Buckets](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
The Buckets list page opens. All buckets in the selected compartment are displayed in a table.
- From the Actions menu next to the relevant bucket, select Edit Bucket Scope .
The Edit Scopes panel opens.
- Select REGION .
- Select Update .

Note  
  

After the bucket scope is set, an update can only be made to change the scope from NAMESPACE to REGION . Bucket scope can't be changed from REGION to NAMESPACE .
- 

Use the[oci os bucket update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/update.html)command. Include the`public-access-type`parameter:
```

```

By default, the bucket scope is namespace. You can specify the bucket scope parameter and one of its supported values:
- NAMESPACE : Allows only path-style access to the bucket.
- REGION : Allows both path-style and virtual-hosted style URL access to the bucket.
Note  
  

After the bucket scope is set, an update can only be made to change the scope from NAMESPACE to REGION . Bucket scope can't be changed from REGION to NAMESPACE .

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
-
