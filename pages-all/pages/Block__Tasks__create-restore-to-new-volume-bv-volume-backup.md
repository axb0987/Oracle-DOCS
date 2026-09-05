# Restoring a Backup to a New Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-to-new-volume-bv-volume-backup.htm
- Fetched: 2026-09-05 01:46 CDT

# Restoring a Backup to a New Volume

Learn how to restore a backup of a volume as a new volume.

Caution  
  
To attach a restored volume that has the original volume attached, be aware that some operating systems don't allow you to restore identical volumes. To resolve this, change the partition IDs before restoring the volume. How to change an operating system's partition ID varies by operating system. For instructions, see your operating system's documentation.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-to-new-volume-bv-volume-backup.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-to-new-volume-bv-volume-backup.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-to-new-volume-bv-volume-backup.htm#)
- 

- On the Block Volume Backups list page, find the block volume backup that you want to work with. If you need help finding the list page or the block volume backups, see[Listing Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/list-bv-backup.htm).
- From the Actions menu (three dots) , select Restore block volume .
- In the Restore block volume panel, enter the following information:
- Name : Name for the block volume. Avoid entering confidential information.
- Create in compartment : The compartment that you want to restore the volume in.
- Availability domain : The availability domain that you want to restore the volume in.
- Cluster Placement Group : (Optional) The cluster placement group to restore the volume to.
Note  
  
This option is visible when cluster placement groups are enabled for the tenancy, and you've created and activated a cluster placement group with the capability added for volume resources. See[Cluster Placement Groups for Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/clusterplacementgroups.htm).
- 

Custom : (Optional) Restore the block volume backup to a larger volume size, specified in Volume size (in GB) .
Note  
  
You can only increase the size of the volume, you cannot decrease the size. If you restore the block volume backup to a larger size volume, you need to extend the volume's partition, see[Extending the Partition for a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingblockpartition.htm)for more information.
- Backup policies : (Optional) Select the appropriate backup policy for your requirements. See[Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)for more information about backup policies.
- 

Volume Encryption : (Optional) Encrypt the data in this volume using your own Vault encryption key.
- To use[Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)for your encryption needs, select the Encrypt using customer-managed keys checkbox.
- Select the vault compartment and vault that contains the master encryption key that you want to use, and then select the master encryption key compartment and master encryption key.
- Tagging: (Optional) Select Show Tagging Options to add tags to the volume.

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- 

Select Restore block volume .

The volume will be ready to attach once its icon no longer lists it as PROVISIONING in the volume list. For more information, see[Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-volume-attachment.htm).
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/create.html)oci bv volume create`command and specify the`--volume-backup-id`parameter to restore a volume backup to the newly created volume:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/CreateVolume)CreateVolume`operation and specify the`volumeBackupId`attribute in the`CreateVolumeDetails`
