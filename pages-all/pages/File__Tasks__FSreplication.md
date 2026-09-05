# File System Replication
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/FSreplication.htm
- Fetched: 2026-09-05 02:02 CDT

# File System Replication

Cross-region replication for File Storage provides protection from regional outages, aids in disaster recovery efforts, and addresses data redundancy compliance requirements.

Learn how to replicate the data in one file system to another file system in the same region or a different region.

## Replication Concepts
SOURCE FILE SYSTEM

The file system whose data you want to replicate to another region or availability domain at regular intervals. File system resource-specific data such as file locks, encryption keys, and tags aren't replicated.[Visit the source file system Details page for replication information. TARGET FILE SYSTEM

The destination for replicated data from the source file system. Replicated data in the target file system has the same file and folder structure, snapshots, metadata, and permissions settings as the source file system.[File System Quotas](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/file-system-quotas.htm)are copied from the parent, but they're disabled and must be enabled manually. Only a file system that has never been exported can be used as a target file system.[Visit the target file system Details page for replication information. REPLICATION RESOURCE

This is the control component of the replication process. It contains all of the necessary configuration information for the replication. The replication resource is attached to the source file system. It captures data updates by creating a replication snapshot and then transmits the snapshot to the replication target. Replications are listed in the Resources section of the source file system's Details page. Tags applied to a replication resource are copied to the replication target resource.[Visit the replication's Details page for information about the replication. REPLICATION TARGET RESOURCE The replication target resource resides in the destination region and availability domain. It receives a replication snapshot from the replication resource and applies the data to the target file system. The replication target is automatically created when you create a replication resource, and any tags applied to the replication resource are copied to the target. The only operation that you can perform manually on a replication target resource after it's created is to delete it during a failover procedure. You can see a file system's Replication Target link in its Details page.[Visit the replication target's Details page for information about the replication target. REPLICATION SNAPSHOT Captures incremental changes in the source file system since the last snapshot. The snapshot data is transmitted from the replication resource to the replication target, which applies it to the target file system. Replication snapshots are managed by the service. Replication snapshots are listed in the source and target file system's Snapshots page. See[Replication and Snapshots](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/replication-managing-snapshots.htm)for more information. DELTA CYCLE

A complete replication operation.
- Idle: The replication is not capturing or applying data.
- Capturing: The replication is capturing differentiated data in the source snapshot.
- Transferring: The replication is both capturing and committing snapshot data.
- Applying: The replication is committing the snapshot data to the target file system. REPLICATION INTERVAL The frequency that the replication operation is performed. You specify the interval when you create the replication resource. RECOVERY TIME OBJECTIVE (RTO) The maximum length of time allowed between an unexpected failure or disaster and the resumption of normal operations. The RTO defines the point in time after a disaster when the consequences of interruption become intolerable. RECOVERY POINT OBJECTIVE (RPO) The maximum acceptable amount of data loss measured in time. In the event that the source file system fails, the RPO is the last replication snapshot that was transmitted to the target. Use the[Replication Recovery Point Age metric](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Reference/filemetrics.htm)to monitor RPO.[Visit the replication target's Details page for information about the replication target.

## How Replication Works

To enable File Storage replication, you create a replication resource attached to the source file system. The replication resource specifies the target file system to replicate to, and how often the data is replicated. The location of the target file system can be in the same or different availability domain as the source file system, in the same or different region. Only a file system that has never been exported can be used as a target file system. After the replication resource is created, the target file system is read-only and updated only by replication. Data updates to the source file system are asynchronously replicated to the target file system. See[Creating a Replication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-creating-a-replication.htm).

Replicated data in the target file system has the same file and folder structure, snapshots, metadata, and permissions settings as the source file system.[Quota rules](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/file-system-quotas.htm)are copied from the source, but they're disabled and must be enabled manually. File system-specific data such as file locks, encryption keys, and tags aren't replicated. Clones of the source file system aren't replicated. Keys and tags for the target file system must be configured separately.

### The Replication Process

The replication resource creates a special replication snapshot in the source file system. Then, it transfers the snapshot to the replication target resource, which writes the new data to the target file system. The last completed replication snapshot remains in both the source and target file system until the next interval. At the next interval, the replication process automatically deletes the old replication snapshots and creates a new one. The replication process continues to repeat at the specified interval as long as the replication is in effect.
In this diagram, File System A in the primary availability domain is replicated to File System B. The replication captures the delta of data written to File System A in a replication snapshot. Then, the data is transferred from the replication resource to the replication target resource, and copied to File System B.
[

If there's an outage in the primary (source) availability domain, you can fail over to the target file system. To fail over to the target file system, export it so applications and users can access it. See[Disaster Recovery](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/replication-disaster-recovery.htm)for more information.

### Monitoring Replications and Outages

The File Storage service provides metrics so that you can track replication operations and potential outages. You can use metrics to analyze things such as transfer between the source and target file systems, bandwidth, and metadata operations performed by the replication resource. For example, to monitor bandwidth issues and potential bottlenecks, you can monitor the total number of write operations on the source file system and the total data egress from the source file system to target file system. You can also use metrics to monitor the time between snapshot creation on the source file system and the time it's applied to the target. In this way you can determine how far the target file system is behind the source, and how much data would be lost if there's an outage. See[File System Metrics](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Reference/filemetrics.htm)and[Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm).

We recommend that you configure alarms on metrics such as the error rate and latency in the source file system to indicate any impact to availability. You can also monitor OCI announcements and status dashboard for general service outages so that you can make necessary decisions about failover. Service outages don't always impact all customer resources equally, so it's very important that you determine your tolerances and put alarms in place. See[Console Announcements](https://docs.oracle.com/iaas/Content/General/Concepts/announcements.htm)and[Events](https://docs.oracle.com/iaas/Content/Events/home.htm).

## Next Steps

You can perform the following replication tasks:
- [Create a Replication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-creating-a-replication.htm)
- [Estimating Replication Time](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-estimating-replication-time.htm)
- [Listing Replications](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-replications.htm)
- [Listing Replication Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-replication-targets.htm)
- [Getting a Replication's Details](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-replication-details.htm)
- [Getting a Replication Target's Details](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-replication-target-details.htm)
- [Editing a Replication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-replication.htm)
- [Deleting a Replication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-replication.htm)
- [Deleting a Replication Target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-replication-target.htm)
- [Using Replication for Disaster Recovery](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/replication-disaster-recovery.htm)
- [Using Replication for Data Transfer](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/replication-copy-data.htm)

## Limitations and Considerations

- Your tenancy must be subscribed to the destination region for cross-region replication. To subscribe to a region, see[Managing Regions](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm). See[Recommended Target Regions](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/FSreplication.htm#limitations-and-considerations__target-regions)for more information.
- When you enable cross-region replication for a file system, the process includes an initial sync of the data from the source file system to the target file system. Depending on the amount of data written to the file system, this sync can take hours. See[Estimating Replication Time](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-estimating-replication-time.htm)for more information.
- You can configure up to three replication jobs for each file system.
- The minimum replication interval is 15 minutes.
- You can't use replication to migrate data from an on-premises location to Oracle Cloud Infrastructure.
- File system resource-specific data such as file locks, encryption keys, and tags aren't replicated.[Quota rules](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/file-system-quotas.htm)are copied from the source, but they're disabled and must be enabled manually. Tags applied to a replication resource are copied to a replication target resource .
- Only a file system that has never been exported can be used as a target file system. To use a previously exported file system as a target, first create a clone of the file system. Then, you can use the clone as a target.
- If you create or delete user snapshots on a file system, you can't use that file system as a target file system for replications, even if you haven't exported the file system.
- A file system with a[snapshot policy](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policies-and-schedules.htm)attached can't be used as a target file system.
- A file system with[quota rules](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/file-system-quotas.htm)that don't match the source file system can't be used as a target file system.
- If you delete a replication resource, replication snapshots on the target file system are converted to user snapshots. If you delete one of these snapshots, you can't reuse the target file system as a target file system for future replications.

### Cost Considerations for Replication

After you enable replication for a file system, the file system is replicated to a target file system in the specified region and availability domain. File Storage is metered for total capacity stored on disk for both the source and target file systems. Source and target file systems are priced at the same rate. See[File System Usage and Metering](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/FSutilization.htm)for more information.

Your bill includes any applicable network costs for the replication process between regions. As part of the replication process, all data being updated on the source file system is transferred to the file system replica, so file systems with continual updates incur higher network costs. There is no additional charge for cross-availability domain bandwidth within the same region or inbound data transfer.

Many replication scenarios use a clone of an original source or target file system. Cloning the source from the last completely applied snapshot ensures that the source and target are compatible. You can also choose to use a new file system for failback. However, using a clone of the original source file system tends to be both faster and more cost effective than using a new file system. See[Clone Metered Utilization](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/FSutilization.htm#FSutilization_topic-clone_metered_utilization)for more information about metering and billing for clones. See[Replication Metered Utilization](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/FSutilization.htm#FSutilization_topic-replication_metered_utilization)for detailed examples of metering for file systems, snapshots, and clones as they're used in replication.

### Recommended Target Regions

When you[enable replication for a file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-creating-a-replication.htm)and create a new target file system, you select a region to replicate to. The source region for the file system determines the recommended target regions available as a destination region for replication in the Console. Most regions have one or more regions available as recommended destination regions. Recommended target regions are selected based on geographical locations to maximize performance. If you need to replicate a file system to a region that's not recommended, you can[create a target file system for replication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-file-system.htm)in that region, or use the API or CLI.

The following table lists the recommendations for the Oracle Cloud Infrastructure commercial realm. To subscribe to a region, see[Managing Regions](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm).

Source Region Target Region
Australia East (Sydney)

Australia Southeast (Melbourne)

Japan East (Tokyo)

US West (San Jose)
Australia Southeast (Melbourne)

Australia East (Sydney)

Singapore (Singapore)

Singapore West (Singapore)
Brazil East (Sao Paulo)

Brazil Southeast (Vinhedo)

Chile Central (Santiago)

US East (Ashburn)

US West (Phoenix)
Brazil Southeast (Vinhedo)

Brazil East (Sao Paulo)

US East (Ashburn)
Canada Southeast (Montreal) Canada Southeast (Toronto)
Canada Southeast (Toronto) Canada Southeast (Montreal)
Chile Central (Santiago) Brazil East (Sao Paulo)
France Central (Paris)

France South (Marseille)

Germany Central (Frankfurt)

Italy Northwest (Milan)

Netherlands Northwest (Amsterdam)

UK South (London)

US East (Ashburn)
France South (Marseille)

France Central (Paris)

Germany Central (Frankfurt)

Italy Northwest (Milan)

Spain Central (Madrid)
Germany Central (Frankfurt)

France Central (Paris)

France South (Marseille)

Italy Northwest (Milan)

Israel Central (Jerusalem)

Japan East (Tokyo)

Netherlands Northwest (Amsterdam)

Sweden Central (Stockholm)

Switzerland North (Zurich)

UK South (London)

UK West (Newport)
India South (Hyderabad)

India West (Mumbai)

Singapore (Singapore)

Singapore West (Singapore)
India West (Mumbai)

India South (Hyderabad)

Singapore (Singapore)

Singapore West (Singapore)

UK South (London)
Israel Central (Jerusalem)

UK South (London)

Germany Central (Frankfurt)
Italy Northwest (Milan)

France Central (Paris)

France South (Marseille)

Germany Central (Frankfurt)

Switzerland North (Zurich)
Japan Central (Osaka)

Japan East (Tokyo)

South Korea North (Chuncheon)

US West (San Jose)
Japan East (Tokyo)

Japan Central (Osaka)

Australia East (Sydney)

Germany Central (Frankfurt)

Singapore (Singapore)

Singapore West (Singapore)

South Korea North (Chuncheon)

South Korea Central (Seoul)
Mexico Central (Queretaro)

US East (Ashburn)

US West (Phoenix)
Netherlands Northwest (Amsterdam)

France Central (Paris)

Germany Central (Frankfurt)

Sweden Central (Stockholm)

UK South (London)

US East (Ashburn)
Saudi Arabia West (Jeddah) UAE East (Dubai)
Singapore (Singapore)

Singapore West (Singapore)

Japan East (Tokyo)

India West (Mumbai)

India South (Hyderabad)

Australia Southeast (Melbourne)
Singapore West (Singapore)

Singapore (Singapore)

Japan East (Tokyo)

India West (Mumbai)

India South (Hyderabad)

Australia Southeast (Melbourne)
South Africa Central (Johannesburg) UK South (London)
South Korea Central (Seoul)

South Korea North (Chuncheon)

Japan East (Tokyo)
South Korea North (Chuncheon)

South Korea Central (Seoul)

Japan Central (Osaka)

Japan East (Tokyo)
Spain Central (Madrid) France South (Marseille)
Sweden Central (Stockholm)

Germany Central (Frankfurt)

Netherlands Northwest (Amsterdam)
Switzerland North (Zurich)

Germany Central (Frankfurt)

Italy Northwest (Milan)

UK South (London)
UAE Central (Abu Dhabi) UAE East (Dubai)
UAE East (Dubai)

Saudi Arabia West (Jeddah)

UAE Central (Abu Dhabi)
UK South (London)

UK West (Newport)

France Central (Paris)

Germany Central (Frankfurt)

India West (Mumbai)

Israel Central (Jerusalem)

Netherlands Northwest (Amsterdam)

South Africa Central (Johannesburg)

Switzerland North (Zurich)

US East (Ashburn)
UK West (Newport)

UK South (London)

Germany Central (Frankfurt)
US Midwest (Chicago)

US East (Ashburn)

US West (Phoenix)
US East (Ashburn)

US Midwest (Chicago)

US West (Phoenix)

US West (San Jose)

Brazil East (Sao Paulo)

Brazil Southeast (Vinhedo)

France Central (Paris)

Mexico Central (Queretaro)

Netherlands Northwest (Amsterdam)

UK South (London)
US West (Phoenix)

US East (Ashburn)

US Midwest (Chicago)

US West (San Jose)

Brazil East (Sao Paulo)

Mexico Central (Queretaro)
US West (San Jose)

US East (Ashburn)

US West (Phoenix)

Australia East (Sydney)

Japan Central (Osaka)

## Required IAM Service Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let users create, manage, and delete file systems](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#general-file-system-management)allows users to create and manage file systems and replications.

A more restrictive policy that allows creation and management of replications:
```

```

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Details for the File Storage Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/filestoragepolicyreference.htm)
