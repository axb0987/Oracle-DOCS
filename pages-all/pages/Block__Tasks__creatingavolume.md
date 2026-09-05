# Creating a Block Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingavolume.htm
- Fetched: 2026-09-05 01:46 CDT

# Creating a Block Volume

Create a block volume in the Block Volume service.
Block volumes are detachable block storage devices that you can use to dynamically expand the storage capacity of an instance. For more information, see[Overview of Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm).
Note  
  
Volumes created with a cluster placement group might be incompatible with instances that aren't part of the same cluster placement group or are in a different group. Depending on latency constraints in OCI, attempting to attach such a volume to a non-compatible instance might result in failure.

See also[Enabling Performance-based Autotuning for a New Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/perf-based-new.htm)and[Enabling Detached Volume Autotuning for a New Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detached-perf-new.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingavolume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingavolume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingavolume.htm#)
- 

- On the Block Volumes list page, select Create block volume . If you need help finding the list page or the volumes, see[Listing Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/listingvolumes.htm).
- On the Create block volume page, enter the following values:

- Name : Enter a user-friendly name for the volume. Avoid entering confidential information.
- Create in compartment : Select the compartment to create the volume in, if different from the current compartment.
- Availability domain : Select the same availability domain as the instance you plan to attach the volume to.
- Cluster Placement Group : (Optional) Select the cluster placement group in which to create the volume.
Note  
  
This option is visible when cluster placement groups are enabled for the tenancy, and you've created and activated a cluster placement group with the capability added for volume resources. See[Cluster Placement Groups for Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/clusterplacementgroups.htm).
- Volume size and performance :
- Default
- Custom
- Volume size : Enter the size of the volume, between 50 GB and 32 TB . You can change by 1 GB increments within this range. The default size is 1024 GB. If you select a size outside of your service limit, then you might be prompted to request an increase. See[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm).
- Target volume performance : (Optional) Change from the default performance level of Balanced , selecting an[appropriate performance level](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumeperformance.htm)for your requirements.
- Detached volume auto-tune : (Optional) Turn on to automatically change the[performance level](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumeperformance.htm)to Lower Cost when the volume is detached.
- Reservations : (Optional) Turn on to enable[persistent reservations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/persistent-reservations.htm)for the volume.
- Backup policies : (Optional) Select the appropriate[backup policy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)for your requirements.

If you select a backup policy enabled for cross region backup copies you can encrypt the backup copy in the destination region with your own Vault encryption key by selecting Encrypt using customer-managed keys for Cross region backup copy encryption . If you select this option, you must specify the OCID for a valid encryption key in the destination region, see[Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm#cust-key-xrr)for more information.
- Cross ad/region replication encryption : (Optional) Turn on to enable[asynchronous cross-region replication for the volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/volumereplication.htm).

If you enable cross-region replication, you can encrypt the volume replica in the destination region with your own Vault encryption key. See[Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm#cust-key-xrr). To use your own key, select Encrypt using customer-managed keys and enter the OCID for a valid encryption key in the destination region.
- 
Volume Encryption : (Optional) Encrypt the data in this volume using your own Vault encryption key:
- Select Encrypt using customer-managed keys .
- Select the vault compartment and vault that contain the master encryption key.
- Select the master encryption key compartment and master encryption key.
Important  
  
The Block Volume service doesn't support encrypting volumes with keys that are encrypted using the Rivest-Shamir-Adleman (RSA) algorithm. When you use your own keys, you must use keys that are encrypted using the Advanced Encryption Standard (AES) algorithm. This restriction applies to block volumes and boot volumes.
- 

Show Tagging Options : (Optional) Add tags to the volume. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create block volume .
The block volume details page opens, and the volume is in the Provisioning state.
When the state changes to Available , the volume is ready to[attach to an instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-volume-attachment.htm).
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/create.html)oci bv volume create`command and required parameters to create a block volume:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[`CreateVolume`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/CreateVolume)operation and specify any of the parameters in the[`CreateVolumeDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CreateVolumeDetails)
