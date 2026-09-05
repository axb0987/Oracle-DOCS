# Object Storage Buckets
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets.htm
- Fetched: 2026-09-05 02:51 CDT

# Object Storage Buckets

Learn about Object Storage buckets, in which you can store objects in a compartment.

In the Object Storage service, a bucket is a container for storing objects in a compartment within an Object Storage namespace. A bucket is associated with a single compartment. The compartment has policies that indicate what actions you can perform on a bucket and all the objects in the bucket.

You can't nest buckets—a bucket can't contain other buckets.

You can perform the following Object Storage bucket tasks:

[List the buckets in a compartment](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).

[Create a bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm).

[Get a bucket's details](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_view_bucket_details.htm).

[Change a bucket's visibility](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_change_the_visibility_of_a_bucket.htm).

[Move a bucket to a different compartment](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_move_a_bucket_to_a_different_compartment.htm).

[Update a bucket to support virtual-hosted URLs.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_update_to_support_vhost_urls.htm)

[Assign a key to an Object Storage bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_assign_a_Vault_master_encryption_key_to_a_bucket.htm).

[Update a bucket to use an SSE-KMS Bucket Key](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_update_a_bucket_to_use_sse_kms_bucket_key.htm).

[Remove a Vault key from a bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_remove_a_Vault_master_encryption_key_from_a_bucket.htm).

[Re-encrypt an Object Storage bucket's data encryption keys](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_reencrypt_a_buckets_data_encryption_keys.htm).

[Enable or disable auto-tiering in a bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_enable_or_disable_auto_tiering.htm).

[Enable or disable emitting events for object state changes in a bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_enable_or_disable_emitting_events_for_object_state_changes.htm).

[Enable or disable object versioning for a bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_enable_or_suspend_object_versioning.htm).

[Delete a bucket from your tenancy](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_delete_a_bucket.htm).

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).

### Object Storage Permissions

The policy[Let Object Storage admins manage buckets and objects](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#object-storage-admins-manage-buckets-objects)lets the specified group do everything with buckets and the associated objects. You must be a member of this group to create a bucket.

If you're an Object Storage administrator and want to impose more restrictive policies for buckets, update the policy to include those restrictions. See[Details for Object Storage, Archive Storage, and Data Transfer](https://docs.oracle.com/iaas/Content/Identity/policyreference/objectstoragepolicyreference.htm)for more information.

## Security Zones

[Security Zones](https://docs.oracle.com/iaas/Content/security-zone/home.htm)ensure that your cloud resources comply with Oracle security principles. If any operation on a resource in a security zone compartment violates a[policy for that security zone](https://docs.oracle.com/iaas/Content/security-zone/using/security-zone-policies.htm), then the operation is denied.

The following security zone policies affect your ability to manage buckets:
- You can't move a bucket from a security zone to a compartment that isn't in the same security zone, because it might be less secure. For details, see[Restrict Resource Movement](https://docs.oracle.com/iaas/Content/security-zone/using/security-zone-policies.htm).
- Buckets in a security zone must be private.
- 

Buckets in a security zone must use customer-managed master encryption keys in the Vault service.
- Using bucket level encryption is supported for buckets in Security Zones when the bucket uses a customer-managed Vault key. For more information, see[Object Storage Data Encryption](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/encryption.htm).

## Pre-Authenticated Requests

Pre-authenticated requests provide a way to let you access a bucket or an object without having your own credentials. For example, you can create a request that lets you upload backups to a bucket without owning API keys. See[Object Storage Pre-Authenticated Requests](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm)for details.

## Object Versioning

You can enable object versioning to retain previous versions of objects. Object versioning lets you view, retrieve, and recover previous versions of objects and provides protection against accidental or malicious object overwrite or deletion. For information about this feature, see[Object Storage Versioning](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning.htm).

## Object Lifecycle Policies

Using object lifecycle policies applied at the bucket level, you can automatically manage the archiving and deletion of objects according to a pre-defined schedule. For information about this feature, see[Object Storage Object Lifecycle Management](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm).

## Retention Rules

You can apply retention rules at the bucket level to provide immutable object storage options for data written to Object Storage for governance, regulatory compliance, and legal requirements. For information about this feature, see[Object Storage Data Retention Rules](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules.htm).

## Replication Policy

Using a replication policy for a bucket, you can automatically replicate the objects in one Object Storage bucket to another bucket in the same region or a different region. For information about this feature, see[Object Storage Replication](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication.htm).

## Tagging Resources

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

Object Storage supports adding tags to buckets.

## Monitoring Resources

You can monitor the health, capacity, and performance of your Oracle Cloud Infrastructure resources by using metrics, alarms, and notifications. For more information, see[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm)and[Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm).

For information about monitoring buckets, see[Object Storage Metrics](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/../Reference/objectstoragemetrics.htm).

## Usage Reports

A usage report is a comma-separated value (CSV) file that can be used to get a detailed breakdown of resources in Oracle Cloud Infrastructure for audit or invoice reconciliation. A usage report is generated daily and stored in an Object Storage bucket. For more information, see[Cost and Usage Reports Overview](https://docs.oracle.com/iaas/Content/Billing/Concepts/costusagereportsoverview.htm)and[Accessing Cost and Usage Reports](https://docs.oracle.com/iaas/Content/Billing/Concepts/usagereportsoverview.htm#Accessing_Cost_and_Usage_Reports).

## Creating Automation Using Events

You can create automation based on state changes for Oracle Cloud Infrastructure resources by using event types, rules, and actions. For more information, see[Overview of Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsoverview.htm).

Buckets emit events for bucket state changes by default. Events for objects are handled differently than other resources. Objects don't emit events by default. Use the Console, CLI, or API to enable a bucket to emit events for object state changes. You can enable events for object state changes during or after bucket creation. See[Enabling or Disabling Emitting Events for Object State Changes](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_enable_or_disable_emitting_events_for_object_state_changes.htm)for more information.

## Bucket Names

Bucket names are system generated by default, but you can overwrite the default with a name you specify.

### System-Generated Bucket Names

When a bucket is created, the system generates a default name for that bucket, for example bucket-20190306-1359 . This bucket name identifies the current year, month, and day that the bucket was created. You can use that system-generated name for your new bucket or you can specify a different name.

### User-Specified Bucket Names

### User-Specified Bucket Names

If you change this default bucket name or the name of any bucket, observe the following:
- Make the name unique within your tenancy's Object Storage namespace.
- Use from 1 to 256 characters.
- Valid characters are letters (upper or lowercase), numbers, hyphens, underscores, and periods.
Important  
  
Bucket names and object names are case-sensitive. Object Storage handles accounts-payable and Accounts-Payable as separate buckets.
- Avoid entering confidential information.

## Default Storage Tiers

When you create a bucket, you decide which default storage tier is appropriate for storing the objects:
- Use the[Standard](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/../Concepts/understandingstoragetiers.htm#understandingobjectstoragetiers_topic-Standard_Tier)tier for data to which you need fast, immediate, and frequent access.
- Use the[Archive](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/../Concepts/understandingstoragetiers.htm#understandingobjectstoragetiers_topi-Archive)tier for data to which you seldom or rarely access, but that must be retained and preserved for long periods of time.

The storage tier property is then assigned to each object that you upload to a bucket.

For more information, see[Object Storage Storage Tiers](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/../Concepts/understandingstoragetiers.htm). To automate the movement of data to the most cost effective tier, see[Auto-Tiering](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/../Concepts/understandingstoragetiers.htm#auto_tiering).
Important  
  
You can't change the default storage tier of a bucket after creation.

## Public Buckets

When you create a bucket, the bucket is considered a private bucket and the access to the bucket and bucket contents requires authentication and authorization. However, Object Storage supports anonymous, unauthenticated access to a bucket that is not in a security zone. You make a bucket public by enabling read access to the bucket.
Important  
  
Carefully assess the business requirement for public access to a bucket. When you enable anonymous access to a bucket, any user can obtain object metadata, download bucket objects, and optionally list bucket contents. We recommend using pre-authenticated requests instead of public buckets. Pre-authenticated requests support more authorization, expiry, and scoping capabilities not possible with public buckets. See[Object Storage Pre-Authenticated Requests](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm)for details.

### Required Permissions

The following permissions are required to configure a public bucket:
- 

To enable public access when creating a bucket, use permission`BUCKET_CREATE`.
- 

To enable public access for an existing bucket, use permission`BUCKET_UPDATE`.

### Options

When creating a public bucket, you have the following options:
- 

You can configure the access to allow listing and downloading objects. List and download access is the default.
- 

You can configure the access to allow downloading objects only. A user couldn't list bucket contents.

### Scope and Constraints

Understand the following scope and constraints regarding public access:
- Buckets in a security zone can't be public.
- Changing the type of access is bi-directional. You can change a bucket's access from public to private or from private to public.
- Changing the type of access doesn't affect existing pre-authenticated requests. Existing pre-authenticated requests still work.
