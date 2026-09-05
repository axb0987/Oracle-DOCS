# Block Volume Metrics Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics-reference.htm
- Fetched: 2026-09-05 01:45 CDT

# Block Volume Metrics Reference

Review details about the metrics emitted for the metric namespace`oci_blockstore`(the Block Volume service).

## Before You Begin

IAM policies: To monitor resources, you must be granted the required type of access in a policy written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to both the monitoring services and the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which compartment you need to work in. For more information about user authorizations for monitoring, see[IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies).

Administrators: For common policies that give groups access to metrics, see[Metric Access for Groups](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#metric-groups)(Securing Monitoring). For common policies that give groups access to Block Volume, see[IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/blockstorage_security.htm#iam-policies).

## Overview of Metrics for an Instance and Its Storage Devices

If you're not already familiar with the different types of metrics available for an instance and its storage and network devices, see[Compute Instance Metrics](https://docs.oracle.com/iaas/Content/Compute/References/computemetrics.htm).

## Block Volume Resources That Have Metrics

Metrics are available for the following resources in Block Volume:
- [Block volumes](https://docs.oracle.com/en-us/iaas/Content/Block/References/../blockvolumes.htm)and[boot volumes](https://docs.oracle.com/en-us/iaas/Content/Block/References/../Concepts/bootvolumes.htm)- see[Descriptions: Performance Metrics](https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics-reference.htm#perfmetrics)
- [Replicas of block volumes, boot volumes, and volume groups](https://docs.oracle.com/en-us/iaas/Content/Block/References/../Concepts/volumereplication.htm)- see[Descriptions: Replication Metrics](https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics-reference.htm#replicatmetrics)

## Available Metrics: oci_blockstore

The Block Volume service includes metrics related to volume[performance](https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics-reference.htm#perfmetrics)and metrics related to volume[replication](https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics-reference.htm#replicatmetrics).

### Dimensions

Each metric includes at least one of the following dimensions : ATTACHMENTID The OCID of the volume attachment. RESOURCEID The OCID of the volume.

### Descriptions: Performance Metrics

The Block Volume service emits metrics to help you measure volume operations and throughput related to compute instances.

The metrics listed in the following table are automatically available for any block volume or boot volume, regardless of whether the attached instance has[monitoring enabled](https://docs.oracle.com/iaas/Content/Compute/Tasks/enablingmonitoring.htm). You don't need to enable monitoring on the volumes to get these metrics.

Metric Metric Display Name Unit Description Dimensions
`VolumeReadThroughput`* Volume Read Throughput bytes Read throughput. Expressed as bytes read per interval.

`attachmentId`

`resourceId`
`VolumeWriteThroughput`* Volume Write Throughput bytes Write throughput. Expressed as bytes written per interval.
`VolumeReadOps`* Volume Read Operations reads Activity level from I/O reads. Expressed as reads per interval.
`VolumeWriteOps`* Volume Write Operations writes Activity level from I/O writes. Expressed as writes per interval.
`VolumeThrottledIOs`* Volume Throttled Operations sum Total sum of all the I/O operations that were throttled during a given time interval.
`VolumeGuaranteedVPUsPerGB`* Volume Guaranteed VPUs/GB VPUs Rate of change for currently active VPUs/GB. Expressed as the average of active VPUs/GB during a given time interval.

`resourceId`
`VolumeGuaranteedIOPS`* Volume Guaranteed IOPS IOPS Rate of change for guaranteed IOPS per SLA. Expressed as the average of guaranteed IOPS during a given time interval.
`VolumeGuaranteedThroughput`* Volume Guaranteed Throughput megabytes Rate of change for guaranteed throughput per SLA. Expressed as megabytes per interval.

* The Compute service separately reports network-related metrics as measured on the instance itself and aggregated across all the attached volumes . Those metrics are available in the`oci_computeagent`metric namespace. For more information, see[Compute Instance Metrics](https://docs.oracle.com/iaas/Content/Compute/References/computemetrics.htm).

### Descriptions: Replication Metrics

The Block Volume service emits metrics to help you track volume replication operations. The metric emitted is determined by the resource type, either a[volume resource](https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics-reference.htm#volumeresources)or a[replica resource](https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics-reference.htm#replicationresources).

#### Volume Resources

The metric listed in the following table is automatically available for any volume resource with cross region replication enabled. This includes block volumes, boot volumes, and volume groups. You don't need to enable monitoring on volumes.

Metric Metric Display Name Unit Description Dimensions
`VolumeReplicationSecondsSinceLastUpload`Time since last cross region replica upload seconds Time elapsed since the last cross region replica was uploaded. Expressed in seconds.

`resourceId`

#### Replica Resources

The metric listed in the following table is automatically available for any replica resource, including block volume replicas, boot volume replicas, or volume group replicas. You don't need to enable monitoring on replicas to get these metrics.

Metric Metric Display Name Unit Description Dimensions
`VolumeReplicationSecondsSinceLastSync`Time since last cross region replica was synced seconds Time elapsed since the last synced cross region replica. Expressed in seconds.

`resourceId`
