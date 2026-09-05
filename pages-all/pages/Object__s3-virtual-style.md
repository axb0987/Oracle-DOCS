# Amazon S3 Compatibility API Hosted Style Support in Object Storage
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/s3-virtual-style.htm
- Fetched: 2026-09-05 02:52 CDT

# Amazon S3 Compatibility API Hosted Style Support in Object Storage

Learn how the Object Storage Amazon S3 Compatibility API supports AWS virtual-hosted style URLs.

Oracle Cloud Infrastructure (OCI) now supports the following ways to address objects:
- Path style : URLs have the following format:
```

```

- Virtual-hosted style : URLs have the following format:
```

```

Here, the bucket name is part of the domain name in the URL and only`<object_name>`is part of the path.

Previously, the Object Storage Amazon S3 Compatibility API only supported the path style using the following format:
```

```

where`<namespace>`represents the Object Storage namespace that serves as the top-level container for all buckets and objects.

When your OCI account is created, each OCI tenant is assigned one unique system-generated and immutable Object Storage namespace name. The namespace spans all compartments across all regions. Bucket names must be unique within a namespace. While the namespace is region-specific, the namespace name itself is the same in all regions.

OCI has added support for virtual-hosted style access, allowing you to include the bucket name as part of the subdomain in the URL. You can use virtual-hosted style URLs with the new endpoint when accessing Object Storage with the AWS SDK:
```

```

Note  
  
When using virtual-hosted style URLs with OCI, the bucket name must be unique across all tenants within the same region.

Consider the following to understand the behavior of buckets:
- Buckets created with the virtual-hosted style URL are guaranteed to be unique across all tenants within the region.
- You can't create a bucket with a name that's already in use within the same region using the virtual-hosted style URL.
- You can still use the path-style URL to access existing buckets, as support for path-style access will continue.
- Bucket names must contain only lowercase letters, numbers, and hyphens.
- Bucket names can't begin with a hyphen character and can't contain consecutive hyphen characters.
- Bucket names must be a minimum of 3 characters long and a maximum of 63 characters long.
- The bucket name acts as a subdomain, so it must also follow standard DNS naming rules.
- If you have existing buckets created with a path-style URL then the bucket name must not already be in use by tenants across the region and the bucket scope must be updated to`REGION`. For more information, see[Updating a Bucket to Support Virtual-hosted Style URLs](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_update_to_support_vhost_urls.htm).

The following table shows the bucket access:

Native API Access S3 Path Style Access S3 Virtual-hosted Style Access
Buckets Created Using OCI Native API ✓ ✓ ✓
Buckets Created Using OCI S3 Path style API ✓ ✓
Buckets Created Using OCI S3 Virtual Style API ✓ ✓ ✓

## Accessing Object Storage Resources Across Tenancies

When working with virtual-hosted style support with the Amazon S3 Compatibility API, to access and share resources with another organization that has its own tenancy, all object, multipart upload, and tagging APIs are supported for cross-tenancy access. Bucket APIs, however, are limited to the following operations:
- [DeleteBucket](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Bucket/DeleteBucket)
- [GetLocation](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Bucket/GetLocation)
- [HeadBucket](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Bucket/HeadBucket)
- [GetService](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Bucket/GetService)(list all buckets)
- [ListObjects](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Bucket/ListObjects)
Note  
  
`PutBucket`, which creates a bucket, isn't supported for cross-tenancy operations with virtual-hosted style support with the OCI S3 API.

For more information about accessing Object Storage resources across tenancies, see[Accessing Object Storage Resources Across Tenancies](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/accessingresourcesacrosstenancies.htm)
