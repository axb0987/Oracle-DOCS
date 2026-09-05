# Replicating Volume Groups
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm
- Fetched: 2026-09-05 01:44 CDT

# Replicating Volume Groups

You can use the Block Volume service's replication feature for volume groups.

Volume group replicas themselves don't contain the full source data from the volumes in the group. Instead, the volume group replica contains references to individual replicas for each of the volumes in the group. This approach provides a seamless replication experience for volumes whether they remain in the volume group, are removed from the volume group, or if replication is turned off for the volume group itself.

When you activate a volume group replica, a new volume group is created. The activation process is the same as creating a clone of the volume group.

This topic covers information about the replication feature specific to volume groups. For general information about the replication feature and how it works, see[Block Volume Replication](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm).
Note  
  
Replication doesn't cause any downtime or impact on source volumes.

## Tasks

- [Listing Volume Group Replicas](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/list-bv-volume-group-replica.htm)
- [Enabling Cross-Region Replication When Creating a Volume Group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/create-cross-region-replication-bv-volume-group.htm)
- [Enabling Cross-Region Replication When Updating an Existing Volume Group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/update-cross-region-replication-bv-volume-group.htm)
- [Updating the Destination Region or Availability Domain Replication Settings for a Volume Group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/update-destination-region-ad-bv-volume-group.htm)
- [Disabling Cross-Region Replication for a Volume Group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/update-disable-cross-region-replication-bv-volume-group.htm)
- [Activating a Volume Group Replica](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/create-activate-replica-bv-volume-group.htm)
- [Getting Details for a Volume Group Replica](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/get-replica-bv-volume-group.htm)
- [Restoring a Volume Group Replica to Its Source Region](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/create-restore-replica-bv-volume-group.htm)

## Limitations and Considerations

The details specified in[Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#replicalimits)apply to volume group replication, in addition to the following:
- 

While it is possible to activate individual volume replicas separately from the volume group replica, to ensure consistency, you should activate the volume group replica instead. Activating the volume group replica ensures that all replicas are activated from the same coordinated synchronization point.
- 

When you remove a volume from a volume group, the volume is not available to add to another group until removal process is complete.
- 

When you add one or more volumes not configured for replication to a volume group that is configured for replication, the Recovery Point Object (RPO) for the volume group replication might degrade while the initial synchronization process runs for the volumes added to the group.

To prevent this impact to the volume group's RPO, you can enable replication for the volume and wait until the initial synchronization process is complete before you add the volume to the group. To determine when the initial synchronization process is complete, monitor the status of the replica for the volume. After it has changed from Provisioning to Available the process is complete, and you can add the volume to the volume group without degrading the volume group replication's RPO.
- 

When you configure replication for a volume group, if the group contains volumes that are already configured for replication, the volume's destination region and availability domain must match the volume group's destination region and availability domain for replication. If they don't match, a Conflicting volumes message occurs while creating the volume group. Remove these volumes from the group to successfully create the volume group.
- 

When you turn on replication for a volume group, all volumes in the group are included in the volume group replica in the destination region and availability domain. Volumes are no longer replicated individually, regardless of whether they were configured for replication before they were included in a volume group with replication turned on. You can no longer update the replication settings for an individual volume, the settings must be configured at the volume group level.
- 

When you turn off replication for a volume group, by default all volumes continue to replicate, but as separate volume replicas, they are no longer part of a volume group replica. You can turn off individual volume replication for all volumes at this point. Choose this option if you want to stop replication of all volumes. If you want to continue replication of some volumes, but not others, do not select this option. Instead, after replication for the volume group has been turned off, you can turn off replication for individual volumes.

To turn off replication for individual volumes, see[Disabling Cross-Region Replication for a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/update-disable-cross-region-replication-bv-volume.htm)and[Disabling Cross-Region Replication for a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/update-disable-cross-region-replication-bv-boot-volume.htm).

## Applying Tags

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
