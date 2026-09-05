# Accessing Object Storage using Swift Endpoints with Curl
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/swift-endpoints-curl.htm
- Fetched: 2026-09-05 02:51 CDT

# Accessing Object Storage using Swift Endpoints with Curl

Gain access to Object Storage and run tasks using Swift API endpoints with Curl.

Run the following Object Storage tasks using Swift API with Curl using the following command syntax. Include the appropriate username, token, namespace, and bucket. For a list of supported Swift API endpoints, see[Swift API Endpoints](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/swift-endpoints-curl.htm#swift-api-endpoints).

You must specify a compartment for the S3 Compatibility API. By default, buckets created using the Amazon S3 Compatibility API or the Swift API are created in the root compartment of the Oracle Cloud Infrastructure tenancy. You can select a different compartment where the Amazon S3 Compatibility API or Swift API can create buckets. For more information, see[Object Storage Compartments for the Amazon S3 Compatibility API and Swift API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/designatingcompartments.htm).

For more information on using Curl, see[curl man page](https://curl.se/docs/manpage.html).

## Listing Objects in a Bucket

Enter the following command at the prompt:
```

```

For example:
```

```

For more information, see[Listing Objects in a Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_list_objects_in_a_bucket.htm).

## Uploading an Object to a Bucket

Enter the following command at the prompt:
```

```

For example:
```

```

For more information, see[Uploading an Object to a Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_upload_objects_to_a_bucket.htm).

## Downloading an Object from a Bucket

Enter the following command at the prompt:
```

```

For example:
```

```

For more information, see[Downloading an Object from a Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_download_an_object_from_a_bucket.htm).

## Swift API Endpoints

Use the appropriate Swift API endpoint according to the Oracle Cloud Infrastructure region where your tenancy resides:
- https://swiftobjectstorage.us-ashburn-1.oraclecloud.com
- https://swiftobjectstorage.us-phoenix-1.oraclecloud.com
- https://swiftobjectstorage.ca-toronto-1.oraclecloud.com
- https://swiftobjectstorage.uk-london-1.oraclecloud.com
-
