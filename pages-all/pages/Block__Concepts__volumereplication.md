# Block Volume Replication
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm
- Fetched: 2026-09-05 01:44 CDT

# Block Volume Replication

The Block Volume service provides you with the capability to perform ongoing automatic asynchronous replication of block volumes, boot volumes, and volume groups to other regions and availability domains.

Block Volume supports two types of replication:
- [Cross region](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#volumereplication_topic-Cross_Region_Replication), for replication between regions.
- [Cross availability domain](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#volumereplication_topic-Cross_AD_Replication), for replication between availability domains within the same region.

This feature supports the following scenarios without requiring volume backups and volume group backups:
- Disaster recovery
- Migration
- Business expansion

The replication feature is complementary to the backup feature, not a replacement. Backups give you a point-in-time snapshot of volumes that enables you to return to a previous version of a volume or volume group. Replicas give you the current version of the data.

When you enable replication for a volume or volume group, the process includes an initial sync of the data from the source to the replica. Depending on volume size and amount of data written to volumes, this sync can take hours. After the initial synchronization process is complete, the replication process is continuous, with the typical Recovery Point Objective (RPO) target rate being less than thirty minutes for replication across regions, however the RPO can vary. See[Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#replicalimits).
Note  
  
Replication doesn't cause any downtime or impact on source volumes.

## Tasks

For tasks related to volume replication, see the following pages:
- [Replicating Block Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/replicating-block-volumes.htm)
- [Replicating Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/boot_volume_replicas.htm)
- [Replicating Volume Groups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm)

## Limitations and Considerations

The following applies to both replication to another region and replication to another availability domain within the same region.
- You can't resize a volume with replication enabled. When resizing a volume, you need to disable replication, which deletes the volume replica. After the volume is resized, you can reenable replication for the volume, which starts the replication process from scratch.
- While the typical RPO target rate is significantly less than thirty minutes for replication, the RPO can vary depending on the change rate of data on the source volume. For example, the RPO can be greater than an hour for volumes with a large amount of write I/O operations to the volume.

### Cost Considerations for Replication

After you enable replication for a volume or volume group, it will be replicated in the specified availability domain or the specified region and availability domain. Your bill will include storage costs for the volume or volume group replica in the destination. The replica in the destination is billed using the Block Storage Lower Cost option price, regardless of volume type in the source region.

See[Oracle Storage Cloud Pricing](https://www.oracle.com/cloud/storage/pricing.html)for information about storage pricing.

For cross region replication, your bill will also include applicable network costs, see[Network Costs for Cross Region Replication](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#volumereplication_topic-Cross_Region_Network_Costs).

## Cross Region Replication

Block Volume replication supports replicating a volume or volume group to another region. For this type of replication, when you enable replication for a volume or volume group, you select a different region than the current source region as the destination region to replicate to. If the destination region supports multiple availaiblity domains, you can also select the availability domain you want to replicate to.

The source region for the volume or volume group determines the target regions available to select as a destination region for replication. Each region has one or more regions available as possible destination regions. The destination regions are selected based on geographical locations. Your tenancy must be subscribed to the destination region for replication. See[Destination Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#regionmapping)for more information.

### Network Costs for Cross Region Replication

Your bill will also include any applicable network costs for the replication process between regions. Network costs for replication between availability domains within the same region are not billed. As part of the replication process, all data being updated on the source volume or source volume group is transferred to the replica, so volumes with continual updates incur higher network costs.

You can see the amount of data transferred for an individual volume during replication in the Console.

To see the amount of data transferred from the replication process for a volume
- Open the navigation menu and select Storage . Under Block Storage , select Block Volumes .
- Select the replica that you want to see the amount of data transferred for. On the Replica Details page, the Total Data Transferred field displays the amount of data, in GBs, that has been transferred during the replication process for the volume. This number includes all data from the point that volume replication was enabled to now.

See[Oracle Networking Cloud Pricing](https://www.oracle.com/cloud/networking/networking-pricing.html)for information about network pricing.

### Destination Regions

In most regions, you can select almost any subscribed destination region for cross-region replication. For exceptions, see[volume-replica-disallowed-regions.json](https://docs.oracle.com/iaas/tools/volume-replica-disallowed-regions.json).

If your tenancy isn't subscribed to any of the destination regions for the source region, and the source region only supports one availability domain, no regions are displayed in the region list and an error message is shown. For source regions containing multiple availability domains, the source region is displayed in the region list, and cross availability domain replication is the only replication available. To use cross region replication, you must subscribe to one of the destination regions for the source region. To subscribe to a region, see[Managing Regions](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm).
Note  
  
If you don't see a region that you're subscribed to in the destination region list,[open a support ticket](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm)to request that the region be added as a destination target for the source region for your volume or volume group.

## Cross Availability Domain Replication

Block Volume replication supports replicating a volume or volume group to another availability domain within the same region. For this type of replication, when you enable replication for a volume or volume group, if the current region contains more than one availability domain, the regions list will include the current region. Select this region as the source region, and then select the availaiblity domain that you want to replicate to.
Note  
  

Replication across availability domains is only supported in commercial regions with multiple availability domains. To determine which regions contain more than one availability domain, see the Availability Domains field in the table listing the commercial regions in[About Regions and Availaibility Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About).

## Replication Metrics

The Block Volume service emits metrics to help you track volume replication operations. For more information, see[Descriptions: Replication Metrics](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../References/volumemetrics-reference.htm#replicatmetrics)and[Descriptions: Performance Metrics](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../References/volumemetrics-reference.htm#perfmetrics).

## Applying Tags

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups)lets the specified group do everything with block volumes, backups, and volume groups.
If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see[Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm)
