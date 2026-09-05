# Restoring a Boot Volume Replica to Its Source Region
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-replica-boot-volume.htm
- Fetched: 2026-09-05 01:46 CDT

# Restoring a Boot Volume Replica to Its Source Region

To restore a boot volume replica to the source region, you must activate the replica in the destination region with volume replication enabled, and then select the original source region as the target region for replication.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-replica-boot-volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-replica-boot-volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-replica-boot-volume.htm#)
- 

- Switch to the region that contains the boot volume replica that you want to activate. See[Switching Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/working-with-regions.htm#Switchin).
- On the Boot Volume Replicas list page, find the boot volume replica you want to work with. If you need help finding the list page or the boot volume, see[Listing Boot Volume Replicas](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume-replica.htm).
- From the Actions menu (three dots) , select Activate and then Confirm .
- In the Activate Replica panel, enter the following information:
- Name : Replica name.
- Create in compartment : Compartment to create the replica in.
- Cluster Placement Group : (Optional) Select a cluster placement group for the replica.
Note  
  
This option is visible when cluster placement groups are enabled for the tenancy, and you've created and activated a cluster placement group with the capability added for volume resources. See[Cluster Placement Groups for Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/clusterplacementgroups.htm).
- Volume size and performance : Select default or custom.
- Enable cross ad/region replication : (Optional) Turn on to enable cross-region replication.
- Select the target region for the replica.
- Select the availability domain for the replica.
- Enter a name for the replica.
- Select Confirm .
- Encryption : (Optional) Encrypt the data in this volume by using your own encryption key. For more information, see[Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm#cust-key-xrr).
- Select Encrypt using customer-managed keys .
- Select the vault compartment and vault that contain the master encryption key you want to use.
- Select the master encryption key compartment and master encryption key.
Note  
  
The service doesn't support encrypting volumes with keys that are encrypted using the Rivest-Shamir-Adleman (RSA) algorithm. When you use your own keys, you must use keys that are encrypted using the Advanced Encryption Standard (AES) algorithm. This restriction applies to block volumes and boot volumes.
- Tagging: (Optional) Select Show tagging options to add tags to the volume. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Activate replica .

The new volume appears in the list, in the provisioning state. After the initial synchronization finishes, the restoration process is complete, and you can use the volume in the original source region.
- 

Use the`oci bv volume create`command and specify the`--availability-domain`,`--compartment-id`,`--display-name`,`--source-details`,`bootVolumeReplicaId`, and`"displayName"`parameters to restore a boot volume replica to its source region:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[`CreateVolume`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/CreateVolume)operation and specify the`compartmentId`,`bootVolumeReplicas`and`sourceDetails`for the[`CreateVolumeDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CreateVolumeDetails)
