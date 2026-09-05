# Cloning a Boot Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-clone-bv-boot-volume.htm
- Fetched: 2026-09-05 01:45 CDT

# Cloning a Boot Volume

Learn how to create a clone from an existing boot volume without repeating the backup and restore process.

You can create a clone from a boot volume using the Oracle Cloud Infrastructure Block Volume service. Cloning enables you to make a copy of an existing boot volume without needing to go through the backup and restore process. For more information about the Block Volume service, see[Overview of Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm)and the[Block Volume FAQ](https://cloud.oracle.com/infrastructure/storage/block-volume/faq).

A boot volume clone is a point-in-time direct disk-to-disk deep copy of the source boot volume, so all the data that is in the source boot volume when the clone is created is copied to the boot volume clone. Any subsequent changes to the data on the source boot volume are not copied to the boot volume clone. Since the clone is a copy of the source boot volume it will be the same size as the source boot volume unless you specify a larger volume size when you create the clone.

The clone operation occurs immediately and you can use the cloned boot volume as soon as the state changes to available.

There is a single point-in-time reference for a source boot volume while it is being cloned, so if you clone a boot volume while the associated instance is running, you need to wait for the first clone operation to complete from the source before creating additional clones. You also need to wait for any backup operations to complete as well.

You can only create a clone for a boot volume within the same region, availability domain, and tenant. You can create a clone for a boot volume between compartments as long as you have the required access permissions for the operation.

## Differences Between Boot Volume Backups and Clones

Consider the following criteria when you decide whether to create a backup or a clone of a volume.

Criteria Volume Backup Volume Clone
Description Creates a point-in-time backup of data on a volume. You can restore multiple new volumes from the backup later. Creates a single point-in-time copy of a volume without having to go through the backup and restore process.
Use case

Retain a backup of the data in a volume, so that you can duplicate an environment later or preserve the data for future use.

Meet compliance and regulatory requirements, because the data in a backup remains unchanged over time.

Support business continuity requirements.

Reduce the risk of outages or data mutation over time.

Rapidly duplicate an existing environment. For example, you can use a clone to test configuration changes without impacting your production environment.
Speed Slower (minutes or hours) Faster (seconds)
Cost Lower cost Higher cost
Storage location Object Storage Block Volume
Retention policy Policy-based backups expire, manual backups do not expire No expiration
Volume groups Supported. You can back up a volume group. Supported. You can clone a volume group.

For more information about boot volume backups, see[Boot Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/bootvolumebackups.htm)and[Creating a Boot Volume Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-boot-volume-backup.htm).

## Steps

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-clone-bv-boot-volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-clone-bv-boot-volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-clone-bv-boot-volume.htm#)
- 

- On the Boot Volumes list page, select the boot volume you want to work with. If you need help finding the list page or the boot volume, see[Listing Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume.htm).
- On the details page, select Clones .
- 

Select Create Clone .
- 

Specify a name for the clone. Avoid entering confidential information.
- Select the compartment for the clone to be created in.
- (Optional) Select the cluster placement group to assign to the clone.
Note  
  
This option is visible when cluster placement groups are enabled for the tenancy, and you've created and activated a cluster placement group with the capability added for volume resources. See[Cluster Placement Groups for Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/clusterplacementgroups.htm).
- 

To clone the boot volume to a larger size volume, select Custom Boot Volume Size (GB) and then specify the new size. You can only increase the size of the volume, you can't decrease the size. If you clone the boot volume to a larger size volume, you need to extend the volume's partition. See[Extending the Partition for a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingbootpartition.htm)for more information.
- (Optional) Enable cross-region replication.
- In the Cross ad/region replication) , move the Enable cross ad/region replication toggle to the right to enable cross-region replication.
- Select the target region for the replica.
- Select the availability domain for the replica.
- Enter a name for the replica.
- 

Select Confirm to acknowledge the cost warning.
- (Optional) Encrypt the data for replicas of this clone by using your own encryption key. For more information, see[Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm#cust-key-xrr).
- Select Encrypt using customer-managed keys .
- Enter the OCID for the encryption key in the destination region.
Note  
  
The service doesn't support encrypting volumes with keys that are encrypted using the Rivest-Shamir-Adleman (RSA) algorithm. When you use your own keys, you must use keys that are encrypted using the Advanced Encryption Standard (AES) algorithm. This restriction applies to block volumes and boot volumes.
- (Optional) Encrypt the data in this volume by using your own encryption key. For more information, see[Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm#cust-key-xrr).
- Under Volume Encryption , select Encrypt using customer-managed keys .
- Select the vault compartment and vault that contain the master encryption key you want to use.
- Select the master encryption key compartment and master encryption key.
Note  
  
The service doesn't support encrypting volumes with keys that are encrypted using the Rivest-Shamir-Adleman (RSA) algorithm. When you use your own keys, you must use keys that are encrypted using the Advanced Encryption Standard (AES) algorithm. This restriction applies to block volumes and boot volumes.
- 

(Optional) Select Show tagging options to add tags to the volume. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- 

Select Create clone .

The clone is ready for use the State column lists it as Available in the Boot Volume Clones list.
- 

Use the[`oci bv boot-volume create --source-boot-volume-id`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/create.html)command and specify the`--source-boot-volume-id`parameter to clone that boot volume:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/CreateBootVolume)CreateBootVolume`operation and specify the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/requests/BootVolumeSourceFromBootVolumeDetails)BootVolumeSourceFromBootVolumeDetails`attribute for the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/requests/CreateBootVolumeDetails)CreateBootVolumeDetails`resource.

## Next Steps

After you have cloned a boot volume backup, you can:
- 

Use the boot volume to create an instance. For more information, see[Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm).
- 

Attach the boot volume to an instance as a data volume. For more information, see[Attaching a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-boot-volume-attachment.htm).

Making a boot volume clone while an instance is running creates a crash-consistent clone, meaning the data is in the identical state it was in at the time the clone was made. This is the same state it would be in the case of a loss of power or hard crash. In most cases you can use the cloned boot volume to create an instance, however to ensure a bootable image, you should create a custom image from your instance. For information about creating custom images, see[Managing Custom Images](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingcustomimages.htm)
