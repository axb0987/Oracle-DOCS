# Enabling Object Versioning for Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/enabling-object_versions.htm
- Fetched: 2026-09-05 03:01 CDT

# Enabling Object Versioning for Roving Edge Infrastructure

Describes how to enable versioning of objects when creating an object storage bucket.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/enabling-object_versions.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/enabling-object_versions.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/enabling-object_versions.htm#)
- 

Follow the steps for creating a bucket using the Device Console as described in[Creating a Bucket](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/../Bucket/create_bucket.htm#top). Select Enable Object Versioning to apply versioning to all objects that you upload.
- 

Run the`oci os bucket create`command to create a bucket using the CLI as described in[Creating a Bucket](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/../Bucket/create_bucket.htm#top). Include the`--versioning enabled`parameter in the command. For example:

```

```

- 

Run the`CreateBucket`operation to create a bucket using the API as described in[Creating a Bucket](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/../Bucket/create_bucket.htm#top). Include the`versioning: enabled`
