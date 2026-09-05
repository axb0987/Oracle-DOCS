# Cluster Placement Groups for Block Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/clusterplacementgroups.htm
- Fetched: 2026-09-05 01:45 CDT

# Cluster Placement Groups for Block Volume

Oracle Cloud Infrastructure Cluster Placement Groups lets you create resources in close proximity to one another to support low-latency networking use cases.

With the Cluster Placement Groups service, you can deploy block volumes and compute instances into the same logical grouping, known as a cluster placement group , to ensure that they're placed physically near one another in an availability domain. For more information, see[Overview of Cluster Placement Groups](https://docs.oracle.com/iaas/Content/cluster-placement-groups/overview.htm).

## Prerequisites

The Cluster Placement Groups service can only be used if the following prerequisites are met:
- Cluster Placement Groups must be enabled for the tenancy.
- The region where you're creating the volume must have at least one cluster placement group[created](https://docs.oracle.com/iaas/Content/cluster-placement-groups/create-cluster-placement-group.htm)and[activated](https://docs.oracle.com/iaas/Content/cluster-placement-groups/activate-cluster-placement-group.htm), with the capabilities configured to support the volume resource for block-storage.

## Limitations and Considerations

- You must configure supported[capabilities](https://docs.oracle.com/iaas/Content/cluster-placement-groups/overview.htm#concepts)when you[create the cluster placement group](https://docs.oracle.com/iaas/Content/cluster-placement-groups/create-cluster-placement-group.htm). You can't edit the capabilities after the cluster placement group has been created. To view an existing cluster placement group's supported capabilities,[get its details](https://docs.oracle.com/iaas/Content/cluster-placement-groups/get-cluster-placement-group.htm). (In the Console, capabilities are listed in the Intended use field on the details page.)
- You must select the cluster placement group when you create the volume. This limitation applies to all methods of[creating the volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingavolume.htm), including[cloning](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/cloningavolume.htm), restoring a[backup](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumebackups.htm), and activating a[replica](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/volumereplication.htm). See[Cluster Placement Groups for Block Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/clusterplacementgroups.htm#clusterplacementgroups_volumes).
- Volumes can't be moved from one cluster placement group to another. You can use volume clones or restore from backups as methods to migrate a volume to another cluster placement group.
- Volume creation fails when no capacity is available in the cluster placement group. In this situation, the new volume transitions from the initial provisioning state to the terminated state. (Compare to a successfully created volume, which transitions from provisioning to available.) To request capacity,[contact support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
- If latency performance is important, then we recommend that you place volumes and instances in the same cluster placement group, even though it's possible to attach volumes in one cluster placement group to an instance in a different cluster placement group, or to an instance that's not in any cluster placement group, or vice versa.
Note  
  
Volumes created with a cluster placement group might be incompatible with instances that aren't part of the same cluster placement group or are in a different group. Depending on latency constraints in OCI, attempting to attach such a volume to a non-compatible instance might result in failure.
- When attaching a volume to more than one instance, the instances don't need to be in the same cluster placement group.
- When you deactivate and delete a cluster placement group, any volume resources in that cluster placement group are disassociated from the cluster placement group, but no volumes are deleted.

## Cluster Placement Groups for Block Volumes

You can only add a block volume to a cluster placement group when you create the volume.

[Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/clusterplacementgroups.htm#top__prerequisites)must be met before you can specify a cluster placement group for a new volume. Otherwise, the Cluster Placement Group option isn't available in the Console, and CLI or API volume creation requests that specify a cluster placement group fail.

Following are methods for creating a volume:
- [Creating a block volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingavolume.htm)
- [Restoring a volume from a backup](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-to-new-volume-bv-volume-backup.htm)
- [Activating a volume replica](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-activate-replica-bv-volume.htm)
- [Cloning a volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/cloningavolume.htm)

## Cluster Placement Groups for Boot Volumes

When you[create an instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm), you can specify a cluster placement group. The instance's boot volume is created in the same cluster placement group as the instance.

You can select a cluster placement group for a boot volume when you[clone a boot volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-clone-bv-boot-volume.htm),[restore a boot volume backup](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-bv-boot-volume-backup.htm), or[activate a boot volume replica](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-activate-replica-bv-boot-volume.htm).

## Cluster Placement Groups for Volume Groups

When you add volumes to a volume group, you can select volumes that are in the same cluster placement group, different cluster placement groups, or no cluster placement groups.

If you select a cluster placement group when you[clone a volume group](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/clone-volume-group.htm),[activate a group volume replica](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-activate-replica-bv-volume-group.htm), or[restore a volume group from a volume group backup](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-bv-volume-group.htm)
