# Overview of Archive Storage
- Source: https://docs.oracle.com/en-us/iaas/Content/Archive/Concepts/archivestorageoverview.htm
- Fetched: 2026-09-05 01:39 CDT

# Overview of Archive Storage

Use Archive Storage to store data that is accessed infrequently and requires a longer retention period.

The Archive Storage service is ideal for storing data that is seldom accessed, but requires long retention periods. Archive Storage is more cost effective than Object Storage for preserving cold data. Unlike Object Storage , Archive Storage data retrieval is not instantaneous.

Oracle Cloud Infrastructure supports multiple[storage tiers](https://docs.oracle.com/iaas/Content/Object/Concepts/understandingstoragetiers.htm)that offer cost and performance flexibility. Archive is the default storage tier for Archive Storage buckets.

Archive Storage is Always Free eligible. For more information about Always Free resources, including capabilities and limitations, see[Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm).

## Using Archive Storage

Important  
  
You interact with the data stored in the Archive Storage using the same resources and[management interfaces](https://docs.oracle.com/en-us/iaas/Content/Archive/Concepts/archivestorageoverview.htm#WaysToAccess)that you use for data stored in[Object Storage . All Object Storage features are also supported in Archive Storage .

Use the following Object Storage resources to store and manage Archive Storage data.

### Buckets

Buckets are logical containers for storing objects. A bucket is associated with a single compartment that has policies that determine what actions a user can perform on a bucket and on all the objects in the bucket.

When you initially create the bucket container for your data, you decide which default[storage tier](https://docs.oracle.com/iaas/Content/Object/Concepts/understandingstoragetiers.htm#understandingobjectstoragetiers_topic-Standard_Tier)(Archive or Standard) is appropriate for your data. The default tier is automatically selected when you upload objects to the bucket, but you can instead select a different tier. Also, if objects meet the criteria of an[object lifecycle policy rule](https://docs.oracle.com/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm), Object Storage can automatically move objects to Archive, while remaining in the Standard tier bucket.

Once set, you cannot change the default storage tier property for a bucket:
- An existing Standard tier bucket cannot be changed to an Archive tier bucket.
- An existing Archive tier bucket cannot be changed to a Standard tier bucket.

In addition to the inability to change the default storage tier designation of a bucket, there are other reasons why storage tier selection for buckets requires careful consideration:
- The minimum storage retention period for the Archive tier is 90 days. If you delete or overwrite objects from the Archive tier before the minimum retention requirements are met, you are charged the prorated cost of storing the data for the full 90 days.
- When you restore objects, you are returning those objects to the Standard tier for access. You are billed for the Standard class tier while the restored objects reside in that tier.

You can use object lifecycle policy rules to automatically delete objects in an Archive Storage bucket based on the age of the object. You cannot , however, use object lifecycle policy rules to automatically restore archived objects to the Standard tier. See[Restoring and Downloading Objects](https://docs.oracle.com/en-us/iaas/Content/Archive/Concepts/archivestorageoverview.htm#Restoring_and_Downloading)for information on restoring objects.

See[Managing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets.htm)for detailed instructions on creating an Archive Storage bucket.

### Objects

Any type of data, regardless of content type, is stored as an object. The object is composed of the object itself and metadata about the object. Each object is stored in a bucket.

You upload objects to an Archive Storage bucket the same way you upload objects to a standard Object Storage bucket. The difference is that when you upload an object to an Archive Storage bucket, the object is immediately archived. You must first restore the object before you can download it.

Archived objects are displayed in the object listing of a bucket. You can also display the details of each object.

See[Managing Objects](https://docs.oracle.com/iaas/Content/Object/Tasks/managingobjects.htm)for detailed instructions on uploading objects to an Archive Storage bucket.

### Restoring and Downloading Objects

To download an object from Archive Storage , you must first restore the object. Restoration takes at most an hour from the time an Archive Storage restore request is made, to the time the first byte of data is retrieved. The retrieval time metric is measured as Time To First Byte (TTFB). How long the full restoration takes, depends on the size of the object. You can determine the status of the restoration by looking at the object Details . Once the status shows as Restored , you can then download the object.

After an object is restored, you have a window of time to download the object. By default, you have 24 hours to download an object, but you can alternatively specify a time from 1 to 240 hours. You can find out how much of the download time is remaining by looking at Available for Download in object Details . After the allotted download time expires, the object returns to Archive Storage . You can always access the metadata for an object, regardless of whether the object is in an archived or restored state.

See[Managing Objects](https://docs.oracle.com/iaas/Content/Object/Tasks/managingobjects.htm)for detailed instructions on restoring, checking status of, and downloading Archive Storage objects.

## Ways to Access Archive Storage

Archive Storage and Object Storage use the same management interfaces:
- 

The Console is an easy-to-use, browser-based interface. To access Archive Storage in the console, do the following:
- [Sign in](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm)to the Console .
- Open the navigation menu and click Storage . Under Object Storage , click Buckets . A list of the buckets in the compartment you're viewing is displayed. If you don’t see the one you're looking for, verify that you’re viewing the correct compartment (select from the list on the left side of the page).
- Click the name of the Archive Storage tier bucket you want to manage.
- 

The command line interface (CLI) provides both quick access and full functionality without the need for programming. For more information, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).

The syntax for CLI commands includes specifying a service. You use the Object Storage service designation`oci os`to manage Archive Storage using the CLI.
- The REST API provides the most functionality, but requires programming expertise.[API Reference and Endpoints](https://docs.oracle.com/iaas/api/)provides endpoint details and links to the available API reference documents. For general information about using the API, see[REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm). Object Storage is accessible with the following APIs:
- [Object Storage Service](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/)
- [Amazon S3 Compatibility API](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/)
- Swift API (for use with Oracle RMAN)
- Oracle Cloud Infrastructure provides SDKs that interact with Archive Storage and Object Storage without you having to create a framework. For general information about using the SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console , SDK or CLI, and REST API). IAM also manages user credentials for things like API signing keys, auth tokens, and customer secret keys for Amazon S3 Compatibility API . See[User Credentials](https://docs.oracle.com/iaas/Content/Identity/usercred/usercredentials.htm)for details.

An administrator in your organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control things like who can create users, create and manage the cloud network, launch instances, create buckets, and download objects. For more information, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm). For specific details about writing policies for each of the different services, see the[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/policyreference/policyreference.htm). For specific details about writing policies for Archive Storage , see[Details for Object Storage, Archive Storage, and Data Transfer](https://docs.oracle.com/iaas/Content/Identity/policyreference/objectstoragepolicyreference.htm).

If you’re a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that your company owns, contact your administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you should be using.

For administrators:
- The policy[Let Object Storage admins manage buckets and objects](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#object-storage-admins-manage-buckets-objects)lets the specified group do everything with buckets and objects.
- Users that need to restore archived objects require the OBJECT_RESTORE permission.

## WORM Compliance

Use retention rules to achieve WORM compliance with Archive Storage so that after the data is written, the data cannot be overwritten. Retention rules are configured at the bucket level and are applied to all individual objects in the bucket. You cannot update, overwrite, or delete objects or object metadata until the retention rule is deleted (indefinite rule) or for the duration specified (time-bound rules). You can, however, always restore an object from Archive Storage .

For more information, see[Using Retention Rules to Preserve Data](https://docs.oracle.com/iaas/Content/Object/Tasks/usingretentionrules.htm).

## Limits on Archive Storage Resources

See[Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm)for a list of applicable limits and instructions for requesting a limit increase.

Other limits include:
- Number of namespaces per root compartment: 1
- Maximum object size: 10 TiB
- Maximum object part size in a multipart upload: 50 GiB
- Maximum number of parts in a multipart upload: 10,000
- Maximum object size allowed by PutObject API: 50 GiB
-
