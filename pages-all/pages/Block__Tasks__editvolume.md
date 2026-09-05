# Editing a Block Volume's Settings
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/editvolume.htm
- Fetched: 2026-09-05 01:46 CDT

# Editing a Block Volume's Settings

Edit the settings for a block volume in the Block Volume service.

You can edit the following settings for block volumes:
- 

Volume name
- 

Volume size
- 

Volume performance
- 

Autotune settings for dynamic performance scaling
- 

Assigned backup policy for scheduled volume backups
- 

Cross region replication

You can update these settings when volumes are online and attached to instances or when they're detached from instances.

This topic provides the basic steps for editing a volume. For instructions applicable to the specific volume setting that you're editing, and more information about that setting, select the links provided in the steps.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/editvolume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/editvolume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/editvolume.htm#)
- 

- On the Block Volumes list page, find the volume that you want to work with. If you need help finding the list page or the volumes, see[Listing Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/listingvolumes.htm).
- From the Actions menu (three dots) for the volume, select Edit .
- In the Edit block volume panel, update the fields you want to change.

- Name : User-friendly name for the volume. Avoid entering confidential information.
- Volume size and performance : Size of the volume, between 50 GB and 32 TB . You can change by 1 GB increments within this range. You must specify a[larger size for the volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/resizingavolume.htm).

After you increase a volume's size, you need to rescan the disk and extend the partition. See[Rescanning the Disk for a Block Volume or Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/rescanningdisk.htm)and[Extending the Partition for a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingblockpartition.htm).
- Target volume performance :
- Performance based auto-tune
- Detached volume auto-tune

See[Dynamic Performance Scaling](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-autotunepolicies-bv-volume.htm).
- Reservations : Enable or disable[persistent reservations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/persistent-reservations.htm)for the volume.
- Backup policies : Change the[backup policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm).

If you select a backup policy enabled for cross region backup copies you can encrypt the backup copy in the destination region with your own Vault encryption key by selecting Encrypt using customer-managed keys for Cross region backup copy encryption . If you select this option, you must specify the OCID for a valid encryption key in the destination region, see[Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm#cust-key-xrr)for more information.
- Cross ad/region replication encryption : Enable or disable[asynchronous cross-region replication for the volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/volumereplication.htm).

If you enable cross-region replication, you can encrypt the volume replica in the destination region with your own Vault encryption key. See[Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm#cust-key-xrr). To use your own key, select Encrypt using customer-managed keys and enter the OCID for a valid encryption key in the destination region.
- Select Save changes .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/update.html)oci bv volume update`command and required parameters to edit a block volume:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/UpdateVolume)UpdateVolume`operation and specify the`volumeId`parameter in the request body and specify the`autotunePolicies`,`blockVolumeReplicas`,`definedTags`,`displayName`,`freeformTags`,`isAutoTuneEnabled`,`isReservationsEnabled`,`sizeInGBs`and/or`vpusPerGB`attributes of the[`UpdateVolumeDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateVolumeDetails)
