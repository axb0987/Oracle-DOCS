# Creating an Object Storage Pre-Authenticated Request
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_create_a_preauthenticated_request_for_all_objects_in_a_bucket.htm
- Fetched: 2026-09-05 02:51 CDT

# Creating an Object Storage Pre-Authenticated Request

Create a pre-authenticated request for all the objects in an Object Storage bucket or for a specific object.

For more information about pre-authenticated requests, see[Using Pre-Authenticated Requests](https://docs.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_create_a_preauthenticated_request_for_all_objects_in_a_bucket.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_create_a_preauthenticated_request_for_all_objects_in_a_bucket.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_create_a_preauthenticated_request_for_all_objects_in_a_bucket.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the bucket's details page, select Management and find the Pre-authenticated requests section.
All pre-authenticated requests are displayed in a table.
- Select Create pre-authenticated request .
- Enter the following information:

- Name : Enter a name for the pre-authenticated request or accept the default system-generated name. The system generates a request name that reflects the current year, month, day, and time, for example, par-bucket-20210330-1643 . Use only letters, numbers, dashes, underscores, and periods for the naming.
- Pre-authenticated request target : Select one of the following targets:
- Bucket : Creates a pre-authenticated request for all objects in the bucket.
- Object : Creates a pre-authenticated request for a specific object.
- Object with prefix : Creates a pre-authenticated request for all objects with a specific name prefix in the bucket.
- Object name : (Object target only) Enter the object name to which the pre-authenticated request applies.
- Prefix : (Object with prefix target only): Enter the prefix used to determine which objects the pre-authenticated request applies:
- You can specify a prefix that includes one or more forward slashes ("/") to match object names that simulate a hierarchy or a directory structure.
- You can specify a prefix string without a delimiter to match the left-most characters of the object name.

See[Object Naming Using Prefixes and Hierarchies](https://docs.oracle.com/iaas/Content/Object/Tasks/managingobjects.htm#nameprefix)for more information on prefixes.
- Access type :

Select one of the following types of access depending on the access type that the pre-authenticated request users have for the objects:

Bucket and Object access types:
- Permit object reads
- Permit object writes
- Permit object reads and writes

Object with prefix access type:
- Permit object reads on those with the specified prefix
- Permit object writes on those with the specified prefix
- Permit object reads and writes to those with the specified prefix
- Enable object listing : (Bucket and Object with prefix only) Select to let the pre-authenticated request user list the objects in the bucket.
- Expiration : Enter the date and time the pre-authentication access expires. Select in the box to display the calendar feature where you can select the month, day, and time. All times are in UTC. The default expiration time is one week from the creation of the pre-authenticated request.
- Select Create pre-authenticated request .
The Pre-authenticated request details dialog box opens, displaying the URL used to access the objects.
- Copy the URL that appears in the Pre-authenticated request URL box. You can also select the "copy" icon next to the box. Paste the URL somewhere in durable storage for future reference.
- Select Close .

Important  
  
The unique URL provided by the system when you create a pre-authenticated request is the only way a user can access the request target. The URL is displayed only at the time of creation and isn't stored in Object Storage. You can't access and retrieve it again after you close the Pre-Authenticated Request Details dialog box. Ensure you store it in a safe, recoverable place.
- 

Use the[oci os preauth-request create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/preauth-request/create.html)command and required parameters to create a pre-authenticated request:

```

```

The`name`parameter is the name of the pre-authenicated request. Avoid entering confidential information.

The`access-type`parameter value can be one of the following:
- `AnyObjectRead`: Permits reads on all objects in the bucket.
- `AnyObjectWrite`: Permits writes to all objects in the bucket.
- `AnyObjectReadWrite`: Permits reads and writes to all objects in the bucket.

The`expiration_timestamp`value is required to use an[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp. For example:`2021-04-02T22:25:27.322000+00:00`.

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

Listing Ojects

Listing objects is denied by default. If the`--access-type`is`AnyObjectRead`or`AnyObjectReadWrite`, you can specify the optional`--bucket-listing-action ListObjects`parameter when creating the pre-authenticated request that lets users list the objects in the bucket.
For example, to create a pre-authenticated request that allows read and write access to all objects in the bucket named`MyParBucket`:
```

```

Important  
  

The`access-uri`provided by the system when you create a pre-authenticated request is the key element of the URL you need to construct to provide user access to the target bucket. Copy the`access-uri`to durable storage. The`access-uri`is displayed only at the time of creation and can't be retrieved later.

The unique pre-authenticated request URL provided to users for the previous example is constructed as follows:
```

```

See[About Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About)for the list of valid region identifiers.

For example, here is the complete URL for the request that allows reads and writes to all objects in the bucket named`MyParBucket`:
```

```

Here is an example of using curl to`PUT`an object using the pre-authenticated request that allows reads and writes to all objects in the bucket named`MyParBucket`and has listing objects enabled:

```

```

Here is an example of using curl to`GET`objects using the same pre-authenticated request:

```

```

Notice the`GET`lists the recent`PUT`for`edit-lifecycle-rules.pdf`and all other objects in the bucket. Optionally, you can use the`fields`query parameter to also include the`size`(object size in bytes),`etag`,`md5`,`timeCreated`(object creation date and time),`timeModified`(object modification date and time),`storageTier`, and`archivalState`fields. See[Getting a List of Objects](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-Working_with_PreAuthenticated_Requests.htm#usingpreauthenticatedrequests_topic-To_get_a_list_of_objects)for more details.

## Creating a Pre-authenticated Request for a Specific Object

Include the`object-name`parameter and the object's name to create a pre-authenticated request for a specific object. For example, to create a pre-authenticated request that allows reads and writes to an object named`OCI_User_Guide.pdf`in the bucket named`MyParBucket`, run the following CLI command:

```

```

The unique pre-authenticated request URL provided to users for the previous example is constructed as follows:
```

```

For example, here is the complete URL for the request that allows reads and writes to an object named`OCI_User_Guide.pdf`in the bucket named`MyParBucket`:
```

```

Here is an example of using curl to`PUT`an object using the pre-authenticated request that allows reads and writes to the target object named`OCI_User_Guide.pdf`in the bucket named`MyParBucket`:

```

```

Here is an example of using curl to`GET`the target object using the same pre-authenticated request:

```

```

## Creating a Pre-authenticated Request for a Specific Object with Prefix

Include the`object-name`parameter and the prefix to create a pre-authenticated request for all objects whose names match the specified prefix. For example, to create a pre-authenticated request that allows reads and writes to objects with the prefix`service`in the bucket named`MyParBucket`:
```

```

Specify the prefix to match on in the`--object-name`parameter:
- You can specify a prefix that includes one or more forward slashes (/) to match on object names that simulate a hierarchy or a directory structure.
- You can specify a prefix string without a delimiter to match on the left-most characters of the object name.

The unique pre-authenticated request URL provided to users for the previous example is constructed as follows:
```

```

See[About Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About)for the list of valid region identifiers.

For example, here is the complete URL for the request that allows reads and writes to objects with the prefix`service`in the bucket named`MyParBucket`:
```

```

When you create a pre-authenticated request that limits the scope to objects with a specific prefix, request users can only`GET`and`PUT`objects with the prefix name specified in the request. Trying to`GET`or`PUT`an object without or with a different prefix fails.

Here is an example of using curl to`PUT`an object using the pre-authenticated request that allows reads and writes to objects with the prefix`service`in the bucket named`MyParBucket`:

```

```

Here is an example of using curl to`GET`objects using the same pre-authenticated request:

```

```

Notice the`GET`lists the recent`PUT`for`servicediscovery.dita`and all other objects with a`service`prefix. Optionally, you can use the`fields`query parameter to also include the`size`(object size in bytes),`etag`,`md5`,`timeCreated`(object creation date and time),`timeModified`(object modification date and time),`storageTier`, and`archivalState`fields. See[Getting a List of Objects](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-Working_with_PreAuthenticated_Requests.htm#usingpreauthenticatedrequests_topic-To_get_a_list_of_objects)for more details.

Here is another example of using curl to`PUT`an object using the same pre-authenticated request. The request fails because the object doesn't have a`service`prefix:

```

```

- 

Run the[CreatePreauthenticatedRequest](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/PreauthenticatedRequest/CreatePreauthenticatedRequest)
