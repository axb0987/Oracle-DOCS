# Pre-Authenticated Request Object URLs in Object Storage
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-Working_with_PreAuthenticated_Requests.htm
- Fetched: 2026-09-05 02:52 CDT

# Pre-Authenticated Request Object URLs in Object Storage

Use a tool such as curl to read and write data using the pre-authenticated requests for an object.
Important  
  

- The unique URL provided by the system when you create a pre-authenticated request is the only way a user can access the request target. Copy the URL to durable storage. The URL is displayed only at the time of creation, isn't stored in Object Storage, and can't be retrieved later.
- The URL generated when you create a pre-authenticated request for an object with a prefix doesn't contain the prefix by default. The user must manually add the prefix to the URL to access the object.

Using the unique request URL, you can use a tool such as curl to read and write data using the pre-authenticated request. Object Storage now supports[writing large files](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-Working_with_PreAuthenticated_Requests.htm#To_put_a_large_object)using[multipart uploads](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads.htm)with pre-authenticated requests.

## Putting an Object

```

```

For example:

```

```

## Putting an Object with Custom Metadata

You can also provide custom metadata for any object using`opc-meta- name : value`headers.

```

```

For example:

```

```

## Putting a Large Object

Multipart uploads accommodate objects that are too large for a single upload operation. We recommend that you use multipart uploads to upload objects larger than 100 MiB. The maximum size for an uploaded object is 10 TiB. Object parts must be no larger than 50 GiB. Using multipart uploads, you have the flexibility of pausing between the uploads of individual parts, and resuming the upload when your schedule and resources allow.

Step 1 : To direct Object Storage to create a multipart upload, include the header`opc-multipart: true`in the`PUT`command.

```

```

For example:

```

```

The`PUT`with the`opc-multipart: true`header returns an access URI to use to upload parts and commit the multipart upload, for example:
```

```

Step 2 : Use the access URI together with the Object Storage hostname for the target region to upload parts, specifying the part number at the end of the URI. For example, to upload an object in three parts, issue the following`PUT`commands:

```

```

Step 3 : To commit the multipart upload, use the`POST`command with the access URI. For example:

```

```

You can delete all parts of an uncommitted or failed multipart upload using the`DELETE`command with the access URI. For example:

```

```

You can also provide custom metadata for any object using`opc-meta-`headers. The`" -H opc-meta- name : value`" is only needed on the first pre-authenticated request that creates the multipart upload, not on each individual part. See[Putting an Object with Custom Metadata](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-Working_with_PreAuthenticated_Requests.htm#To_put_an_object_with_metadata)for more information.

## Getting an Object

```

```

For example:

```

```

## Getting a List of Objects

For pre-authenticated requests that apply to several objects, the request creator can optionally let you list objects.

```

```

For example:

```

```

By default, the object list returns only the names of the objects. Optionally, you can use the`fields`query parameter to also include the`size`(object size in bytes),`etag`,`md5`,`timeCreated`(object creation date and time),`timeModified`(object modification date and time),`storageTier`, and`archivalState`fields. Specify the value of this parameter as a comma-separated, case-insensitive list of those field names that you want to include in the object list. For example:

```

```

In addition to`fields`, pre-authenticated requests support all other[ListObjects](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/ListObjects)query parameters and[list pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

## Getting Metadata from an Object

```

```

For example:

```

```

## Getting an Object with Custom Response Headers

You can override the response headers in the PAR GET requests by using the following query parameters:

- `httpResponseContentDisposition`
- `httpResponseCacheControl`
- `httpResponseContentType`
- `httpResponseContentLanguage`
- `httpResponseContentEncoding`
- `httpResponseExpires`

For example:

```

```

```

```

```

```
