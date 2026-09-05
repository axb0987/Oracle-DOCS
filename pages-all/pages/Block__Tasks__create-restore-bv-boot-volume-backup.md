# Restoring a Boot Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-bv-boot-volume-backup.htm
- Fetched: 2026-09-05 01:46 CDT

# Restoring a Boot Volume

Before you can use a boot volume backup, you need to restore it.

After restoring a boot volume backup, you can use it to create an instance or you can attach it to another instance as a data volume.

You can restore a boot volume from any of your incremental or full boot volume backups. Both backup types enable you to restore the full boot volume contents to the point-in-time snapshot of the boot volume when the backup was taken. You don't need to keep the initial full backup or subsequent incremental backups in the backup chain and restore them in sequence, you only need to keep the backups taken for the times you care about. See[Boot Volume Backup Types](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/bootvolumebackups.htm#backuptypes)for information about full and incremental backup types.

Making a boot volume backup while an instance is running creates a crash-consistent backup, meaning the data is in the identical state it was in at the time the backup was made. This is the same state it would be in the case of a loss of power or hard crash. In most cases, you can restore a boot volume backup and use it to create an instance. Alternatively you can attach it to an instance as a data volume to repair it or recover data, see[Attaching a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-boot-volume-attachment.htm). To ensure a bootable image, you should create a custom image from your instance. For information about creating custom images, see[Managing Custom Images](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingcustomimages.htm).

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.
If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see[Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-bv-boot-volume-backup.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-bv-boot-volume-backup.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-bv-boot-volume-backup.htm#)
- 

- In the Boot Volume Backups list page, select the boot volume you want to work with. If you need help finding the list page or the boot volume, see[Listing Boot Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume-backup.htm).
- 

In the list of boot volume backups, select the Actions menu (three dots) for the boot volume backup you want to restore and then select Restore Boot Volume .
- 

Specify a name for the boot volume.
- 

Select the availability domain to for the boot volume.

(Optional) Select the cluster placement group to restore the boot volume to.
Note  
  
This option is visible when cluster placement groups are enabled for the tenancy, and you've created and activated a cluster placement group with the capability added for volume resources. See[Cluster Placement Groups for Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/clusterplacementgroups.htm).
- (Optional) In the Volume size and performance section, select Custom to restore the boot volume backup to a larger volume size.
Note  
  

You can only increase the size of the volume, you cannot decrease the size. If you restore the block volume backup to a larger size volume, you need to extend the volume's partition, see[Extending the Partition for a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingbootpartition.htm)for more information.
- Specify the new volume size in gigabytes (GB).
- (Optional) In the Target volume performance section, move the Performance based auto-tune to the right to[enable performance-based autotuning](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-autotunepolicies-bv-boot-volume.htm).
- Select your Volume Performance (VPUs) type.
- (Optional) Move the Enable detached volume auto-tune toggle to the right to enable[enable detached volume autotuning](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-autotunepolicies-detached-bv-boot-volume.htm).
- 

Choose a backup policy for scheduled backups. See[Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)for more information about scheduled backups and volume backup policies. Avoid entering confidential information.
- (Optional) Enable cross-region replication.
- In the Cross ad/region replication) , move the toggle to the right to enable cross-region replication.
- Select the target region for the replica.
- Select the availability domain for the replica.
- Enter a name for the replica.
- 

Select Confirm to acknowledge the cost warning.
- (Optional) Encrypt the data in this volume by using your own encryption key. For more information, see[Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm#cust-key-xrr).
- Select Encrypt using customer-managed keys .
- Select the vault compartment and vault that contain the master encryption key you want to use.
- Select the master encryption key compartment and master encryption key.
Note  
  
The service doesn't support encrypting volumes with keys that are encrypted using the Rivest-Shamir-Adleman (RSA) algorithm. When you use your own keys, you must use keys that are encrypted using the Advanced Encryption Standard (AES) algorithm. This restriction applies to block volumes and boot volumes.
- 
- 

(Optional) Select Show tagging options to add tags to the volume. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- 

Select Restore Boot Volume .

The boot volume will be ready to use when its State column lists is listed as Available in the Boot Volumes list page.
- 

Use the[`oci bv boot-volume create`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/create.html)command and specify the`--availability-domain`,`--compartment-id`and`"id"`and parameters to restore a boot volume:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/CreateBootVolume)CreateBootVolume`operation and specify the`[](https://docs.oracle.com/iaas/tools/dotnet/latest/api/Oci.CoreService.Models.BootVolumeSourceFromBootVolumeBackupDetails.html)BootVolumeSourceFromBootVolumeBackupDetails`attribute in the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CreateBootVolumeDetails)CreateBootVolumeDetails`resource to restore a boot volume.

## Next Steps

After you have restored the boot volume backup, you can:
- 

Use the boot volume to create an instance, for more information, see[Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm).
- 

Attach the boot volume to an instance as a data volume, for more information, see[Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-volume-attachment.htm).

Making a boot volume backup while an instance is running creates a crash-consistent backup, meaning the data is in the identical state it was in at the time the backup was made. This is the same state it would be in the case of a loss of power or hard crash. In most cases you can use the restored boot volume to create an instance, however to ensure a bootable image, you should create a custom image from your instance. For information about creating custom images, see[Managing Custom Images](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingcustomimages.htm)
