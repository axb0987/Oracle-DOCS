# Copying an Object to Another Bucket in Object Storage
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/copyingobjects.htm
- Fetched: 2026-09-05 02:50 CDT

# Copying an Object to Another Bucket in Object Storage

Copy an object to another bucket in Object Storage.
Caution  
  
Object copy doesn't work if you don't authorize the Object Storage service to copy objects on your behalf. See[Service Permissions](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/copyingobjects.htm#Service)for more information.

## Copy Object Overwrite Rules

Use the following overwrite rules to control the copying of objects based on their entity tag (ETag) values:
- Overwrite destination object : Use this option when you don't want to limit a copy operation by an ETag value. This option is the default. This option can be used for any copy operation, regardless of whether it involves overwriting an existing object.
- Do not overwrite any destination object : Use this option to prevent the overwriting an existing copy of an object in the destination location, regardless of the destination object's ETag value.
- Overwrite destination object only if it matches the specified ETag : Use this option to prevent the accidental overwriting of an object in the destination location that doesn't have the specified ETag. When you use this option, the copy operation only succeeds if the ETag you supply when starting the copy request matches the ETag of the destination object.
- Copy object only if the source matches the specified ETag : Use this option if you want the copy operation successful only if the ETag you supply when starting the copy request matches the ETag of the source object. For objects that are intentionally updated and overwritten as part of data management activity, this option ensures that only the specified version of the object (as indicated by the ETag) is allowed to be copied. If the object's ETag value changes after the copy work request is created, but before the copy operation is run, the copy operation doesn't complete.
Caution  
  
If you overwrite an object, the operation can't be undone.

## Scope and Constraints

- Objects can't be copied directly from[Archive Storage](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm). To copy objects that are in Archive Storage, you must first[restore](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm)the object to the Standard Object Storage tier. Objects can be copied directly to Archive tier buckets from the Standard or Infrequent Access tiers. When you copy objects into an Archive Storage bucket, the copy of the object is immediately archived.
- Specify an existing target bucket for the copy request. The copy operation doesn't automatically create buckets.
- When an object is copied, the destination object receives a new ETag value.
- If you rename, overwrite, or delete a source object during a copy operation, the copy operation fails and the destination object isn't created or overwritten.
- Bulk copying isn't supported. Identify a single object in the copy request.

## Service Permissions

Because Object Storage is a regional service, you must authorize the Object Storage service for each region carrying out copy operations on your behalf. For example, you might authorize the Object Storage service in region US East (Ashburn) to manage objects on your behalf. After you authorize the Object Storage service, you can copy an object stored in a US East (Ashburn) bucket to a bucket in another region.

To find the region identifier value of an Oracle Cloud Infrastructure region, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

For administrators :

To enable object copy, you must authorize the service to manage objects on your behalf:
- You can create a policy that authorizes the service in the specified region to manage Object Storage namespaces, buckets, and their associated objects in all compartments in the tenancy:

```

```

- Instead of using the[policy verb](https://docs.oracle.com/iaas/Content/Identity/policyreference/policyreference_topic-Verbs.htm)`manage`, you can create a policy that reduces the scope of access by instead using one of the following statements:

```

```

```

```

## Copying an Object

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/copyingobjects.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/copyingobjects.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/copyingobjects.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the bucket's details page, select Objects .
- From the Actions menu for the object you want, select Copy .
The Copy object panel opens.

The Console checks the IAM policies that are in place to perform this task successfully. If you see a policy missing warning, you can let the Console try to create any missing policies or copy the missing policy details to the clipboard to email your administrator. If you think you have the required policies in place, go ahead and try the copy operation.
- Enter the following information:

- Destination namespace : Enter the namespace of the destination bucket for the copied object. The namespace string of your tenancy is supplied as the default value. See[Understanding Namespaces](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/understandingnamespaces.htm)for more information.
- Destination region : Select the OCI region that contains the destination bucket for the copied object from the list. Your tenancy must be[subscribed to a region](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm#subscribe)for you to copy an object to a bucket in that region.
- Destination bucket : Enter the name of the destination bucket for the copied object. The destination must be an existing bucket in that you have access to. See[Buckets](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets.htm)for more information on how to create a bucket.
- Destination object name : (Optional) Enter an alternate name for the object being copied if you don't want to use its original name. By default, the name is the same name as the object that you're copying.
- Destination storage tier : (Optional) Specify the storage tier to upload the object to if you want it to be different than the source storage tier. The following storage tiers are supported:
- Standard tier
- Infrequent access
- Archive

If you don't specify a destination storage tier, the object is stored in the same storage tier as the bucket. See[Object Storage Storage Tiers](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/../Concepts/understandingstoragetiers.htm)for more information.

### Overwrite rule

Select the overwrite rule appropriate for the copy request:
- Overwrite destination object
- Do not overwrite any destination object
- Overwrite destination object only if it matches the specified ETag
- Copy object only if the source matches the specified ETag

See[Copy Object Overwrite Rules](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/copyingobjects.htm#overwrite)for descriptions of each of these rules.

Select Copy object .

The Work request details dialog box appears and confirms that the copy request is submitted successfully and tracks the status of the request.
- 

Use the[oci os object copy](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/copy.html)command and required parameters to copy an object to another bucket:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

### Copying an Object to a Different Region

Include the`destination-region`parameter and the region identifier to specify a target bucket in region on there than the one where the destination object resides.

For example:
```

```
Your tenancy must be[subscribed to a region](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm#subscribe)for you to copy an object to a bucket in that region.

### Copying to a Different Destination Storage Tier

Include the`destination-object-storage-tier`parameter and a supported storage tier value to copy the object to a different storage tier on the destination bucket than the tier where it resides on the source.

For example:
```

```

Supported values are:
- `Standard`
- `InfrequentAccess`
- `Archive`
- 

If you don't specify a destination storage tier, the object is stored in the same storage tier as the bucket. See[Object Storage Storage Tiers](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/../Concepts/understandingstoragetiers.htm)for more information.

### Specifying the Namespace of the Copied Object

Include the`destination-namespace`parameter and its value to specify the destination namespace to which the object is copied.

For example:
```

```
See[Understanding Namespaces](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/understandingnamespaces.htm)for more information.

### Specifying an Alternate Name for the Copied Object

Include the`destination-object-name`parameter and its value to apply an alternate name to the copied object.

For example:
```

```

By default, the name is the same name as the object that you're copying.
- 

Run the[CopyObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/CopyObject)
