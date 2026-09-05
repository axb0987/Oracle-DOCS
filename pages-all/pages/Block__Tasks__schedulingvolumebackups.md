# Backup Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm
- Fetched: 2026-09-05 01:47 CDT

# Backup Policies

Use custom and predefined backup policies to schedule backups for volumes and volume groups in Block Volume for adherence to data compliance and regulatory requirements. Predefined (Oracle-defined) backup policies have a set backup frequency and retention period that can't be changed. Custom (user-defined) backup policies include configurable frequency, retention, optional cross-region copy, and optional schedules. You can apply both Oracle-defined and user-defined backup policies to volumes and volume groups.
Caution  
  

Deleting Block Volumes with Policy-Based Backups

All policy-based backups eventually expire. To keep a volume backup indefinitely,[manually back up the volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-backup.htm).

## Tasks

- [Listing Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-backup-policies.htm)
- [Creating a User-defined Backup Policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-volume-backup-policy.htm)
- [Getting Details for a Backup Policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-volume-backup-policy.htm)
- [Updating a Backup Policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-backup-policy.htm)
- [Updating the Display Name for a User-defined Backup Policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-display-name-bv-volume-backup-policy.htm)
- [Enabling Cross-region Copy for a User-defined Backup Policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-destinationregion-bv-volume-backup-policy.htm)
- [Adding a Schedule to a User-defined Backup Policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-schedule-bv-volume-backup-policy.htm)
- [Updating a Schedule for a User-defined Backup Policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-bv-volume-backup-policy.htm)
- [Deleting a Schedule for a User-defined Backup Policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/delete-schedule-bv-volume-backup-policy.htm)
- [Disabling Cross-region Copy for a User-defined Backup Policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/delete-destinationregion-bv-volume-backup-policy.htm)
- [Duplicating a Backup Policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copy-bv-volume-backup-policy.htm)
- [Deleting a User-defined Backup Policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/delete-bv-volume-backup-policy.htm)

See also:
- [Assigning a Backup Policy to a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-volume-backup-policy-assignment.htm)
- [Viewing the Backup Policy Assigned to a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-volume-backup-policy-assignment.htm)
- [Retrieving a Specific Backup Policy Assignment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-volume-backup-policy-assignment-specific.htm)
- [Checking for Volume Group Management of Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/check-policy-mgmt.htm)

## Timing for Scheduled Backups

Scheduled volume backups aren't guaranteed to start at the exact time specified by the backup schedule. You might see up to several hours of delay between the scheduled start time and the actual start time for the volume backup in scenarios where the system is overloaded. This situation applies to both user defined and Oracle defined backup policies. Volume backups are point-in-time snapshots of volume data. For more information about volume backups, see[Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumebackups.htm).

## User-Defined Backup Policies

To get started with user-defined backup policies,[create a policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-volume-backup-policy.htm),[add schedules](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-schedule-bv-volume-backup-policy.htm)to the policy, and finally,[assign the policy to a volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-volume-backup-policy-assignment.htm)or[assign the policy to a volume group](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/create-assign-to-group-bv-volume-backup-policy-assignment.htm).

### Duplicating Existing Backup Policies

Both Oracle-defined and user-defined policies can be duplicated.

If one of the Oracle-defined policies is close to meeting your volume backup requirements, but requires some changes, you can create a new backup policy by duplicating the Oracle-defined policy. This creates a new user-defined backup policy with schedules already assigned, enabling you to use the Oracle-defined policy's settings as a starting point to save time and simplify the process.

You can create a new backup policy by[duplicating an existing backup policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copy-bv-volume-backup-policy.htm).

### Scheduling Volume Backup Copies Across Regions

The Block Volume service enables you to copy volume backups from one region to another for business continuity and disaster recovery scenarios, for more information, see[Copying Block Volume Backups Across Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumebackups.htm#Copying). With user-defined policies, you can automate this process, so that volume backups are copied to another region on a schedule. Enabling the automatic copying of scheduled volume backups is only supported with user-defined policies, so if you need to use this feature for a volume currently configured with an Oracle-defined policy, you need to duplicate the policy and then enable cross region copy. The volume backup copy in the target region has the same retention period as the volume backup in the source region.
Note  
  
Vault encryption keys for volumes aren't copied to the destination region for scheduled volume and volume group backups enabled for cross region copy. Instead, you can specify a Vault encryption key for the backup copied to the destination region when you assign the backup policy. When you assign the backup policy, if it's enabled for cross region backup copies, select Encrypt using customer-managed keys for Cross region backup copy encryption to encrypt the volume backup in the destination region. If you select this option, you must specify the OCID for a valid encryption key in the destination region, see[Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm#cust-key-xrr)for more information.
Note  
  
Copying daily scheduled volume backups to the target region can take up to 24 hours. You can verify that the volume backup was copied by switching to the target region and checking the list of volume backups for that region. If the volume backup hasn't been copied yet, you can perform a manual copy of that volume backup to the target region using the steps described in[Copying a Volume Backup Between Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copy-bv-backup.htm).

#### Cost

Once this feature is enabled, your bill will include charges for storing volume backups in both the source region and the destination region. You may also see an increase in network costs. For pricing details, see[Oracle Storage Cloud Pricing](https://www.oracle.com/cloud/storage/pricing.html). The Object Storage price applies to backup storage. Outbound Data Transfer price will be applicable for network costs with cross-region backup copies.

## Oracle-Defined Backup Policies

There are three Oracle-defined backup policies: bronze, silver, and gold. Each backup policy is comprised of schedules with a set backup frequency and a retention period that you cannot modify. If the backup policy settings for Oracle-defined policies don't meet your requirements, use[User-Defined Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#custom)instead. With user-defined backup policies, you define and control the schedules. You can also enable the automatic copying of volume backups to a second region, which isn't supported with Oracle-defined policies.
Note  
  
Oracle-defined backup policies aren't supported for scheduled volume group backups.
Caution  
  

Full Backups and Oracle-Defined Policies

As of November 3, 2021, Oracle-defined policies no longer include full backups. See[Full backups removed from Oracle defined backup policies](https://docs.oracle.com/iaas/Content/servicechanges.htm#servicechanges_topic-Full_backups_removed_from_Oracle_defined_policies). Incremental backups are functionally the same as full backups for data recovery purposes. Some compliance scenarios may require scheduled full backups. For these compliance scenarios, configure a user-defined backup policy instead. You can create a new user-defined policy from an existing backup policy, see[Duplicating Existing Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#duplicatepolicy).

### Bronze Policy

The bronze policy includes monthly incremental backups, run on the first day of the month. These backups are retained for twelve months. This policy also includes an incremental backup, run yearly during the first part of January. This backup is retained for five years.

### Silver Policy

The silver policy includes weekly incremental backups that run on Sunday. These backups are retained for four weeks. This policy also includes monthly incremental backups, run on the first day of the month and are retained for twelve months. Also includes an incremental backup, run yearly during the first part of January. This backup is retained for five years.

### Gold Policy

The gold policy includes daily incremental backups, retained for seven days, along with weekly incremental backups, run on Sunday and retained for four weeks. Includes monthly incremental backups, run on the first day of the month, retained for twelve months. Also includes an incremental backup, run yearly during the first part of January. This backup is retained for five years.

## Working with Backup Policies

### Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.
Important  
  
To view or work with backup policies, you need access to the root compartment, which is where the predefined backup policies are located.

For administrators: The policy in[Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups)lets the specified group do everything with block volumes and backups. The policy in[Let volume backup admins manage only backups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-backup-admins-manage-only-backups)further restricts access to just creating and managing backups.

Tip  
  
When users create a backup from a volume or restore a volume from a backup, the volume and backup don't have to be in the same compartment . However, users must have access to both compartments.
If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see[Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).

### Applying Tags

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

## Tracking the Status of Backup Operations with Events

You can use Oracle Cloud Infrastructure Events to track the status of Block Volume backup operations. See[Block Volume Events](https://docs.oracle.com/iaas/Content/Events/Reference/eventsproducers.htm#blockevents__block_volume)for a list of these event types. All Block Volume event types include a status attribute. The status attribute value is either operationFailed or operationSucceed , depending on the whether the backup operation succeeded or failed.
Note  
  
You need to manually type the operationFailed and operationSucceed attribute values into the text box when creating a rule in the Console.

For a walkthrough of how to use the Create Volume Backup End event's status attribute to notify you when a scheduled volume backup fails, see[Using Events to Notify When a Volume Backup Fails](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/backupstatusevents.htm)
