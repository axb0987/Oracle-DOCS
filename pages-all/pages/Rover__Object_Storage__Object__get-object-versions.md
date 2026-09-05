# Getting an Object Version's Details for Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/get-object-versions.htm
- Fetched: 2026-09-05 03:01 CDT

# Getting an Object Version's Details for Roving Edge Infrastructure

Describes how to get the details for a particular version of an object in an object storage bucket on your Roving Edge Infrastructure device.

Only those objects that were uploaded to an object storage bucket with versioning enabled will have their versions available for getting details.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/get-object-versions.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/get-object-versions.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/get-object-versions.htm#)
- 

- Open the navigation menu and select Object Storage &gt; Object Storage . The Buckets page appears. All buckets are listed in tabular form.
- Select the bucket whose containing the object whose version details you want to get. The bucket's Details page appears. All objects are listed in tabular form.
- (optional) Enable Show Deleted Objects to display those objects that were versioned, but subsequently deleted.
- Select the Down arrow at the right side of the object's entry to display the versions.
- Select the Actions menu ( ) of the version whose details you want to get and select View Object Details .

The Object Version Details dialog box appears. It contains information on the object version including basic information on the version, response headers, and object contents.
- 

Run the`oci os object head`command to get details of an object's version from a bucket using the CLI as described in[Getting an Object's Details](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/head_object.htm#HeadObject). Include the`--version-id`parameter in the command to specify the version being deleted. For example:

```

```

- 

Run the`HeadObject`operation to get details of an object's version in the Roving Edge Infrastructure device's object storage bucket as described in[Getting an Object's Details](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/head_object.htm#HeadObject). Include the`versionId`
