# Securing Object Storage
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/objectstorage_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing Object Storage

This topic provides security information and recommendations for Object Storage.

The[Object Storage](https://docs.oracle.com/iaas/Content/Object/home.htm)service is a high-performance storage platform that offers reliable and cost-efficient data durability. You can store an unlimited amount of unstructured data of any content type, including analytic data and rich content, like images and videos.

## Security Responsibilities

To use Object Storage securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.
- Encryption and Confidentiality: Use encryption keys and secrets to protect your data and connect to secured resources. Rotate these keys regularly.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure Object Storage in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users and resources[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/objectstorage_security.htm#iam-policies)
Encrypt resources using a custom key[Data Encryption](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/objectstorage_security.htm#data-encryption)
Secure network access to resources[Network Security](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/objectstorage_security.htm#network-security)
Enable and configure Cloud Guard (optional)[Cloud Guard](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/objectstorage_security.htm#cloud-guard)
Create a security zone (optional)[Security Zones](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/objectstorage_security.htm#security-zones)

## Routine Security Tasks

After getting started with Object Storage use this checklist to identify security tasks that we recommend you perform regularly.

Task More Information
Rotate encryption keys[Data Encryption](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/objectstorage_security.htm#data-encryption)
Respond to problems detected in Cloud Guard[Cloud Guard](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/objectstorage_security.htm#cloud-guard)
Take regular backups[Data Durability](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/objectstorage_security.htm#durability)
Ensure the integrity of your data when it's moved or copied to different locations[Checksums in Data Security](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/objectstorage_security.htm#data-security)
Perform a security audit[Auditing](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/objectstorage_security.htm#auditing)

## IAM Policies

Use policies to limit access to Object Storage.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

Assign least privileged access to resource types in`object-family`(buckets and objects). For example, the`inspect`verb lets you check to see if a bucket exists (`HeadBucket`) and list the buckets in a compartment (`ListBucket`). The`manage`verb gives all permissions on the resource.

We recommend that you give`DELETE`permissions to a minimum set of IAM users and groups. This practice minimizes loss of data from inadvertent deletes by authorized users or from malicious actors. Only give`DELETE`permissions to tenancy and compartment administrators.

In the following examples, the policies are scoped to a tenancy. However, specifying a compartment name reduces the scope to a specific compartment in a tenancy.

[Allow User Access to a Specific Folder](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/objectstorage_security.htm#)

You can allow access to any user to a specific folder in a bucket by using a combination of specific bucket name (`target.bucket.name`) and specific object pattern (`target.object.name`). You can use an asterisk ("*") as a wildcard to match any sequence of string characters (`/*name/`,`/name*/`,`/*name*/`). Restricting access to a folder by object pattern doesn't prevent listing all the objects in the containing bucket.

```

```

[Restrict Group Access to Specific Buckets](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/objectstorage_security.htm#)

You can restrict access by a group to a specific bucket by using the specific bucket name (`target.bucket.name`), defined tags (`target.tag.definition.name`), or you can use asterisk as a wildcard to match any sequence of string characters (`/*name/`,`/name*/`,`/*name*/`).

The following example of restrict access to users in the`BucketUsers`group to a specific bucket.

```

```

You can change this policy to restrict access to users in the group`BucketUsers`to all buckets whose names are prefixed with`ProjectA_`.

```

```

You can also match for post-fix (`/*_ProjectA/`) or substring (`/*ProjectA*/`).

[Restrict Group Access to Read or Write to Objects in a Specific Bucket](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/objectstorage_security.htm#)

The following example allows listing and reading objects by group`BucketUsers`from a specific bucket named`BucketFoo`.

```

```

The following policy modifies the previous policy to allow listing and writing objects to`BucketFoo`.

```

```

You can restrict this policy to read or write access to a set of buckets by using regular expressions or tags rather than a specific bucket.

[Restrict Group Access to Read or Write to Objects based on Bucket Tags](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/objectstorage_security.htm#)

The following example allows listing and reading objects by group`BucketUsers`from all the buckets with the defined tag "`MyTagNamespace.TagKey = MyTagValue`".

```

```

The following policy modifies the previous policy to allow listing and writing objects to all the buckets where the defined tag on the bucket matches the defined tag on the group that the user belongs to.

```

```

[Restrict Resource Access to a Particular User](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/objectstorage_security.htm#)

You can restrict access to Object Storage resources to a specific user by adding a condition to the policy that specifies the user's OCID in a variable.

The following policy restricts access to the resources in`ObjectStorage`compartment to the user OCID specified:

```

```

[Restrict Access to Requests That Originate From an Allowed IP Address](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/objectstorage_security.htm#)

You can restrict access only to requests that originate from an allowed IP address. First, you create a network source to specify the allowed IP addresses, then you add a condition to your policy to restrict access to the IP addresses in the network source.

The following policy restricts access to only IP addresses in a network source`corpnet`that defines the allowed IP addresses:

```

```

For information on creating network sources and using them in a policy, see[Managing Network Sources](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingnetworksources.htm).

[Prevent Delete of Buckets or Objects](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/objectstorage_security.htm#)

In the following example, the group`BucketUsers`can perform all actions on buckets and objects except delete.

```

```

The following example further restricts object deletion from the specific bucket (`BucketFoo`).

```

```

[Enable WORM Compliance for Objects](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/objectstorage_security.htm#)

Use[retention rules](https://docs.oracle.com/iaas/Content/Object/Tasks/usingretentionrules.htm)to achieve WORM compliance. Retention rules are configured at the bucket level and are applied to all individual objects in the bucket. You cannot update, overwrite, or delete objects or object metadata until the retention rule is deleted (indefinite rule) or for the duration specified (time-bound rules).

The following policies let`BucketUsers`manage the buckets and objects in the tenancy and allow`BucketUsers`to create, manage, and delete retention rules. These policies also let`BucketUsers`lock retentions rules for a specified time.

```

```

The following more restrictive policies let`BucketUsers`perform all actions on buckets and objects except locking retention rules.

```

```

[Prevent Public Buckets Configuration](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/objectstorage_security.htm#)

`BUCKET_CREATE`and`BUCKET_UDPATE`permissions are required to create buckets or make existing private buckets public. Removing these permissions prevents users from creating buckets or making existing buckets public.

```

```

For more information about Object Storage policies and to view more examples, see[Details for Object Storage, Archive Storage, and Data Transfer](https://docs.oracle.com/iaas/Content/Identity/policyreference/objectstoragepolicyreference.htm).

## Access Control

In addition to creating IAM policies, lock down access to Object Storage using features like pre-authenticated requests.

### Public Buckets

A public bucket allows unauthenticated and anonymous reads to all objects in the bucket. Carefully evaluate the intended use case for public buckets before you enable public buckets.

We recommend that you use pre-authenticated requests to give bucket or object access to users without IAM credentials. By defaults, buckets are created with no public access (access type is set to`NoPublicAccess`).

You can make existing buckets public by updating the bucket access type to`ObjectRead`or`ObjectReadWithoutList`. To minimize the possibility of existing buckets being made public inadvertently or maliciously, restrict`BUCKET_UPDATE`permission to a minimal set of IAM groups.

The following CLI command returns the`public-access-type`assigned to a bucket.

```

```

If the attribute`public-access-type`has the value`NoPublicAccess`, the bucket is private. Any other value such as`ObjectRead`indicates a public bucket.

### Pre-Authenticated Requests

For users without IAM credentials, we recommend that you use pre-authenticated requests (PARs) to give time-bound access to objects or buckets.

In a pre-authenticated request, an IAM user who has appropriate privileges for accessing objects, can create special URLs that grant time-bound access to these objects. For more information, see[Using Pre-Authenticated Requests](https://docs.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm).

The creator of a pre-authenticated request must have`PAR_MANAGE`permission and the appropriate IAM permissions for the access type that you're granting. You can create a pre-authenticated request that grants read, write, or read/write access to one of the following:
- All objects in the bucket.
- A specific object in the bucket.
- All objects in the bucket that have a specified prefix.

For requests that apply to several objects, you can also decide whether you want to let users list those objects.

Pre-authenticated request accesses to a bucket are signed in Audit logs. Pre-authenticated request accesses to an object are logged in Service logs.
Important  
  
The unique URL provided by the system when you create a pre-authenticated request is the only way a user can access the request target. Copy the URL to durable storage. The URL is displayed only at the time of creation, isn't stored in Object Storage, and can't be retrieved later.

The following CLI command returns a list of object PARs in a bucket.

```

```

## Cloud Guard

Enable Cloud Guard and use it to detect and respond to security issues in Object Storage.

Upon detecting a problem, Cloud Guard suggests corrective actions. You can also configure Cloud Guard to automatically take certain actions. Cloud Guard includes the following detector rules for Object Storage.
- Bucket is public
- Object Storage bucket is encrypted with Oracle-managed key
- IAM customer keys created

For a list of all available detector rules in Cloud Guard, see[Detector Recipe Reference](https://docs.oracle.com/iaas/Content/cloud-guard/using/detect-recipes.htm).

If you haven't done so already, enable Cloud Guard and configure it to monitor the compartments that contain your resources. You can configure Cloud Guard targets to examine your entire tenancy (root compartment and all subcompartments), or to check only specific compartments. See[Getting Started with Cloud Guard](https://docs.oracle.com/iaas/Content/cloud-guard/using/part-start.htm).

After enabling Cloud Guard, you can view and resolve detected security problems. See[Processing Reported Problems](https://docs.oracle.com/iaas/Content/cloud-guard/using/part-problems.htm).

## Security Zones

Using Security Zones ensures your resources in Object Storage comply with security best practices.

A security zone is associated with one or more compartments and a security zone recipe. When you create and update resources in a security zone's compartment, Oracle Cloud Infrastructure validates these operations against the list of security zone policies in the recipe. If any policy in the recipe is violated, then the operation is denied. The following security zone policies are available for resources in Object Storage.
- `deny public_buckets`
- `deny buckets_without_vault_key`

For a list of all security zone policies, see[Security Zone Policies](https://docs.oracle.com/iaas/Content/security-zone/using/security-zone-policies.htm).

To move existing resources to a compartment that is in a security zone, the resources must comply with all security zone policies in the zone's recipe. Similarly, resources in a security zone can't be moved to a compartment outside of the security zone because it might be less secure. See[Managing Security Zones](https://docs.oracle.com/iaas/Content/security-zone/using/managing-security-zones.htm).
Note  
  

Using bucket level encryption is supported for buckets in Security Zones when the bucket uses a customer-managed Vault key. For more information see[Data Encryption](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/../../Object/Tasks/encryption.htm).

## Data Encryption

Create and rotate encryption keys in the Vault service to protect your resources in Object Storage.

All data in Object Storage is encrypted at rest by using AES-256. Encryption is on by default and cannot be turned off. Each object is encrypted with its encryption key, and the object encryption keys are encrypted with a master encryption key.

A vault is a logical entity that stores the encryption keys you use to protect your data. Depending on the protection mode, keys are either stored on the server, or they are stored on highly available and durable hardware security modules (HSMs). Our HSMs meet Federal Information Processing Standards (FIPS) 140-2 Security Level 3 security certification. See[Managing Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults.htm)and[Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm).

Although default encryption keys can be generated automatically when you create certain Oracle Cloud Infrastructure resources, we recommend that you create and manage your own custom encryption keys in the Vault service.

To assign a custom encryption key to a new bucket or an existing one, see:
- [Creating an Object Storage Bucket](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm)
- [Assigning a Key to an Object Storage Bucket](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_assign_a_Vault_master_encryption_key_to_a_bucket.htm)
- [Re-encrypting an Object Storage Bucket's Data Encryption Keys](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_reencrypt_a_buckets_data_encryption_keys.htm)
- [Re-encrypting an Object Storage Object](https://docs.oracle.com/iaas/Content/Object/Tasks/managingobjects_topic-To_reencrypt_an_object.htm)

Each master encryption key is automatically assigned a key version. When you rotate a key, the Vault service generates a new key version. Periodically rotating keys limits the amount of data encrypted or signed by one key version. If a key is ever comprised, key rotation reduces the risk to your data. See[Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm).

When using customer managed Vault (KMS) keys, Object Storage data can be encrypted at the object or bucket level. For more information see[Data Encryption](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/../../Object/Tasks/encryption.htm).

We recommend that you use IAM policies to strictly limit the creation, rotation, and deletion of encryption keys. See[Details for the Vault Service](https://docs.oracle.com/iaas/Content/Identity/Reference/keypolicyreference.htm).

You can also use client-side encryption to encrypt objects with their encryption keys before storing them in Object Storage buckets. An available option for customers is to use the Amazon S3 Compatibility API, along with client-side object encryption support available in AWS SDK for Java. See[Amazon S3 Compatibility API](https://docs.oracle.com/iaas/Content/Object/Tasks/s3compatibleapi.htm)for more details about on this SDK.

## Data Durability

Take regular backups of your data in Object Storage.
Minimize data loss because of inadvertent deletes by an authorized user or malicious deletes. We recommend the following:
- Use[object versioning](https://docs.oracle.com/iaas/Content/Object/Tasks/usingversioning.htm)to automatically create an object version each time a new object is uploaded, an existing object is overwritten, or when an object is deleted.
- Give`BUCKET_DELETE`and`OBJECT_DELETE`permissions to a minimum set of IAM users and groups. Grant delete permissions only to tenancy and compartment administrators.

"Write once, read many" (WORM) compliance requires that objects cannot be deleted or modified. Use[retention rules](https://docs.oracle.com/iaas/Content/Object/Tasks/usingretentionrules.htm)to achieve WORM compliance. Retention rules are configured at the bucket level and are applied to all individual objects in the bucket. You cannot update, overwrite, or delete objects or object metadata until the retention rule is deleted (indefinite rule) or for the duration specified (time-bound rules).

For an independent assessment of the Object Storage retention rules feature's ability to meet regulatory requirements for record management and retention, see Cohasset Associate's[SEC 17a-4(f), FINRA 4511(c), CFTC 1.31(c)-(d) and MiFID II Compliance Assessment](https://www.oracle.com/a/ocom/docs/oracle-object-storage-compliance-assessment-report.pdf).

## Checksums in Data Security

To verify object data integrity, an MD5 checksum is provided for all objects uploaded to Object Storage. In addition, you can apply one of the following optional checksums to objects uploaded to Object Storage:

- 

SHA256
- 

SHA384
- 

CRC32C

Using MD5 Checksum

We recommend that you verify that the offline MD5 checksum of an object matches the checksum value returned by the Console or API after upload. Oracle Cloud Infrastructure provides the object checksum value in`base64`encoding. To covert the`base64`encoded checksum value to hexadecimal, use the following command:
```

```

Linux provides an`md5sum`command line utility to compute the MD5 checksum value of an object in hexadecimal format.

Using MD5 Checksum with Multipart Uploads

Object Storage supports[multipart uploads](https://docs.oracle.com/iaas/Content/Object/Tasks/usingmultipartuploads.htm)for more efficient and resilient uploads, especially for large objects. In a multipart upload, a large object is broken up into smaller parts by specifying a part size in MiB. Each part is uploaded separately. Object Storage then combines all the parts to create the original object. If any of the parts fail to upload, only those parts need to be retried for upload, and not the entire object.

In a multipart upload, the MD5 checksum values are computed for each part, and an MD5 checksum computed over all the individual checksum values to get the output MD5 value. To verify the MD5 value returned for a multipart upload, follow the same process for offline MD5 checksum calculation. A sample script for the offline calculation of an MD5 checksum value for a multipart upload to Object Storage is available here:[https://gist.github.com/itemir/f5bc9fded6483cd79c89ebf4ca1cfd30](https://gist.github.com/itemir/f5bc9fded6483cd79c89ebf4ca1cfd30).

Using SHA256 or SHA384 Checksum

Some industries have regulatory requirements to use a checksum method that's considered to be stronger than MD5. Those requirements often explicitly require SHA256 or SHA384. You can select the algorithm required by their compliance regime. Note that the presence of MD5 isn't considered insecure or out of compliance, adding another checksum method provides an extra integrity check. Adding one of the SHA checksum types is expected to help meet these requirements.
Here are examples of using the SHA256 or SHA384 checksums:
```

```

```

```

Using CRC32C Checksum

You might want to compare the checksum calculated on a local storage system with those calculated by Object Storage. This is difficult to do with multipart uploads, because the calculated checksum depends on the exact size of each part, which might be different on different systems (or with different upload settings).

The CRC32C checksum type is designed to return the same checksum for the same object regardless of how it's uploaded. This allows customers to compare the CRC32C checksum calculated by Object Storage with the CRC32C checksum calculated by local storage or other clouds, regardless of the multi-part upload settings.

Using Additional Checksum Types

You can only use one additional checksum type per uploaded object. MD5 checksums are always calculated on every object. When using an additional checksum type, GET and PUT commands might incur slightly longer latency to complete, as compared to a GET or PUT on the same object without the additional checksum type.

## Network Security

Secure network access to your resources in Object Storage.

Data in transit between customer clients (for example, SDKs and CLIs) and Object Storage public endpoints is encrypted with TLS 1.2 by default. FastConnect public peering allows on-premises access to Object Storage over a private network, rather than the public internet. See[Access to Your On-Premises Network](https://docs.oracle.com/iaas/Content/Network/Concepts/connectivityonprem.htm).

## Auditing

Locate access logs and other security data for Object Storage.

The Audit service automatically records all API calls to Oracle Cloud Infrastructure resources. You can achieve your security and compliance goals by using the Audit service to monitor all user activity within your tenancy. Because all Console, SDK, and command line (CLI) calls go through our APIs, all activity from those sources is included. Audit records are available through an authenticated, filterable query API or they can be retrieved as batched files from Object Storage. Audit log contents include what activity occurred, the user that initiated it, the date and time of the request, as well as source IP, user agent, and HTTP headers of the request. See[Viewing Audit Log Events](https://docs.oracle.com/iaas/Content/Audit/Tasks/viewinglogevents.htm).

[Example Audit Log](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/objectstorage_security.htm#)

```

```

If you enabled Cloud Guard in your tenancy, then it reports any user activities that are potential security concerns. Upon detecting a problem, Cloud Guard suggests corrective actions. You can also configure Cloud Guard to automatically take certain actions. See[Getting Started with Cloud Guard](https://docs.oracle.com/iaas/Content/cloud-guard/using/part-start.htm)and[Processing Reported Problems](https://docs.oracle.com/iaas/Content/cloud-guard/using/part-problems.htm)
