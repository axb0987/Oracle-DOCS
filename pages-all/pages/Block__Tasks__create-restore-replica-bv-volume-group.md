# Restoring a Volume Group Replica to Its Source Region
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-replica-bv-volume-group.htm
- Fetched: 2026-09-05 01:46 CDT

# Restoring a Volume Group Replica to Its Source Region

To restore a boot volume replica to the source region, you must activate the replica in the destination region with volume replication enabled, and then select the original source region as the target region for replication.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-replica-bv-volume-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-replica-bv-volume-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-replica-bv-volume-group.htm#)
- 

- On the Volume Group Replicas list page, find the volume group replica you want to work with. If you need help finding the list page or the volume group replica, see[Listing Volume Group Replicas](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-volume-group-replica.htm).
- From the Actions menu (three dots) , select Activate and then Confirm .
- In the Activate Volume Group Replica panel, enter the following information:
- Compartment : Compartment to create the clone of the source volume group in.
- Volume Group Name : Replica name.
- Select Activate .

The new volume group appears in the list, in the provisioning state.

Once the volume group status has changed from Provisioning to Available , turn on replication for the volume group and specify the original source region as the destination region. For more information, see[Enabling Cross-Region Replication When Updating an Existing Volume Group](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-cross-region-replication-bv-volume-group.htm). Once the initial synchronization finishes, the failback process is complete, and you can activate the volume group in the original source region.
- 

Use the[`oci bv volume-group create`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/create.html)command and specify the`--availability_domain`,`--compartment-id`,`--display-name`,`--source-details`, and`--volume-group-replicas`parameters to restore a volume group replica to its source region:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[`CreateVolumeGroup`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/CreateVolumeGroup)operation and specify the`compartmentId`,`bootVolumeReplicas`and`sourceDetails`attributes for the[`CreateVolumeGroupDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CreateVolumeGroupDetails)
