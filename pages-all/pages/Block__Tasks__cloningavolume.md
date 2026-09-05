# Cloning a Block Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/cloningavolume.htm
- Fetched: 2026-09-05 01:45 CDT

# Cloning a Block Volume

Create a clone from a volume by using the Block Volume service. Cloning lets you to make a copy of an existing block volume without needing to go through the backup and restore process.

A cloned volume is a point-in-time direct disk-to-disk deep copy of the source volume, so all the data that is in the source volume when the clone is created is copied to the clone volume. Any subsequent changes to the data on the source volume are not copied to the clone. Because the clone is a copy of the source volume it is the same size as the source volume unless you specify a larger volume size when you create the clone.

The clone operation occurs immediately, and you can attach and use the cloned volume as a regular volume as soon as the state changes to Available. At that point, the volume data is being copied in the background, and can take up to thirty minutes depending on the size of the volume.

There is a single point-in-time reference for a source volume while it is being cloned. If the source volume is attached when you create a clone, you need to wait for the first clone operation to complete from the source volume before creating additional clones. If the source volume is detached, you can create up to ten clones from the same source volume simultaneously.

You can create a clone for a volume only within the same region, availability domain and tenancy. You can create a clone for a volume between compartments if you have the required access permissions for the operation.

For information to help you decide whether to create a backup or a clone of a volume, see[Differences Between Block Volume Backups and Clones](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumebackups.htm#backupsvsclones).
Note  
  
Volumes created with a cluster placement group might be incompatible with instances that aren't part of the same cluster placement group or are in a different group. Depending on latency constraints in OCI, attempting to attach such a volume to a non-compatible instance might result in failure.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/cloningavolume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/cloningavolume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/cloningavolume.htm#)
- 

- On the Block Volumes list page, select the volume that you want to clone. If you need help finding the list page or the volumes, see[Listing Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/listingvolumes.htm).
- From the Actions menu (three dots) , select Create Clone .
- In the Create clone panel, enter the following information.
- Name : Specify a name for the clone. Avoid entering confidential information.
- Create in compartment : Select the compartment to create the clone in, if different from the current compartment.
- Cluster Placement Group : (Optional) Select the cluster placement group in which to clone the volume to.
Note  
  
This option is visible when cluster placement groups are enabled for the tenancy, and you've created and activated a cluster placement group with the capability added for volume resources. See[Cluster Placement Groups for Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/clusterplacementgroups.htm).
- Custom : (Optional) Clone the block volume to a larger size volume, or change the performance setting for a clone. Then perform one or both of the following actions:
- 

In Volume size (GB) , enter the new size.

You can only increase the size of the volume; you can't decrease it. If you clone the block volume to a larger-size volume, you need to extend the volume's partition. See[Extending the Partition for a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingblockpartition.htm).
- 

Under Target volume performance , select the performance level that you want the volume clone to use. See[Block Volume Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumeperformance.htm).

You can also change the performance level after you have cloned the volume. See[Changing the Performance of a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/changingvolumeperformance.htm).
- 

Enable reservations : (Optional) Turn on to enable[persistent reservations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/persistent-reservations.htm)for the volume.
- Enable cross ad/region replication : (Optional) Turn on to enable[asynchronous cross-region replication](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/volumereplication.htm)for the volume clone.
- 

Volume Encryption : (Optional) Encrypt the data in this volume by using your own Vault encryption key. Select Encrypt using customer-managed keys , and then select the vault compartment and vault that contain the master encryption key you want to use. Then, select the master encryption key compartment and master encryption key.
Important  
  
The Block Volume service doesn't support encrypting volumes with keys that are encrypted using the Rivest-Shamir-Adleman (RSA) algorithm. When you use your own keys, you must use keys that are encrypted using the Advanced Encryption Standard (AES) algorithm. This restriction applies to block volumes and boot volumes.
- 

Select Create clone .

The volume is ready to use when its state is AVAILABLE in the volume list. At that point, you can perform various actions on the volume, such as creating a clone from the volume, attaching it to an instance, or deleting the volume.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/create.html)oci bv volume create`command and specify the`--source-volume-id`parameter to clone a block volume:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/CreateVolume)CreateVolume`operation and specify the`sourceDetails`attribute in the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/requests/VolumeSourceFromVolumeDetails)VolumeSourceFromVolumeDetails`resource for the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/requests/CreateVolumeDetails)CreateVolumeDetails`
