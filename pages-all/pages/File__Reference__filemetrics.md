# File System Metrics
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Reference/filemetrics.htm
- Fetched: 2026-09-05 02:02 CDT

# File System Metrics

You can monitor the health, capacity, and performance of your file systems and mount targets by using metrics , alarms , and[notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm).

This topic describes the metrics emitted by the metric namespace`oci_filestorage`(the File Storage service).

## Overview of Metrics for oci_filestorage

File Storage service metrics help you measure operations and throughput related to file systems and mount targets. The available metrics help you determine quickly if your file system is accessible, how much data is flowing through its associated mount target, and if operations are producing unexpected errors. You can get visibility into your workload IOPs and latency, and set up alarms to receive notifications if tolerance thresholds are exceeded.

File Storage metrics include these resources:
- File system : A high-performance shared storage entity made available to a network by an associated mount target.
- Mount target : An NFS endpoint that lives in a VCN subnet of your choice and provides network access for file systems.
- Replication : The control component of the replication process. It captures data updates by creating a replication snapshot and then transmits the snapshot to the replication target.
- Replication target : Receives a replication snapshot from the replication resource and applies the data to the target file system.
- Outbound connector : A connection between File Storage and an external service, such as an LDAP server.

Metrics provided for file systems can be filtered or grouped by their associated mount target.

## Raw Data Point Frequency

For every 1-minute interval, the File Storage service posts one raw data point to the Monitoring service. The Monitoring service charts show data points at 1-minute, 5-minute, 1-hour (60-minute), and 1-day intervals. Supported values for interval depend on the specified time range in the metric query (not applicable to alarm queries). More interval values are supported for smaller time ranges. For example, if you select one hour for the time range, then all interval values are supported. If you select 90 days for the time range, then only interval values between 1 hour and 1 day are supported. The available statistics are calculated by using the count of 1-minute data points in the select interval. For example, for a given metric:
- The mean for each 5-minute interval is calculated over 5 raw data points. If there are less than 5 raw data points, the average is used.
- The mean for each 60-minute interval is calculated over 60 raw data points. If there are less than 60 raw data points, the average is used.

## Required IAM Policy

To monitor resources, you must be granted the required type of access in a policy written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to both the monitoring services and the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which compartment you need to work in. For more information about user authorizations for monitoring, see[IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies).

## Available Metrics: oci_filestorage

The metrics listed in the following table are automatically available for any file system or mount target. You do not need to enable monitoring on the resource to get these metrics.

You also can use the Monitoring service to create[custom queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/buildingqueries.htm).

Each metric includes one or more of the following dimensions : resourceId The OCID of the file system or mount target. mountTargetId The OCID of the mount target exporting an associated file system. mtResourceName The name of the mount target exporting an associated file system. obcResourceName The name of the outbound connector used by the mount target exporting an associated file system. requestType The type of the request made by the mount target to an LDAP server. throughput The type of request throughput:
- `ReadThroughput`
- `WriteThroughput`size The request size range:
- `0B_to_8KiB`
- `8KiB_to_64KiB`
- `64KiB_to_1MiB`errorType The type of the error encountered by the mount target using an outbound connector. healthItem The type of health rate item:
- `SuccessRate`
- `ErrorRate`tenantId The OCID of the tenancy. lockMode The snapshot lock mode.

### File System Metrics

Metric Metric Display Name Unit Description Dimensions
`FileSystemReadThroughput`Read Throughput bytes Read throughput for the file system. If the file system is exported through multiple mount targets, total throughput for all mount targets is displayed. Expressed as bytes read per second.

`resourceId`

`mountTargetId`

`throughput`
`FileSystemWriteThroughput`Write Throughput bytes Write throughput for the file system. If the file system is exported through multiple mount targets, total throughput for all mount targets is displayed. Expressed as bytes written per second.
`FileSystemReadRequestsbySize`

Read Requests

operation Read requests by size. Expressed as operation per second, grouped by size.`resourceId`

`mountTargetId`

`size`
`FileSystemWriteRequestsbySize`

Write Requests operation Write requests by size. Expressed as operation per second, grouped by size.
`FileSystemReadAverageLatencybySize`Read Latency second Read latency by size. Expressed as average read latency per second, grouped by size.
`FileSystemWriteAverageLatencybySize`Write Latency second Write latency by size. Expressed as average write latency per second, grouped by size.
`MetadataRequestAverageLatency`Metadata Latency second

Average metadata request latency for the following NFS operations:`CREATE`,`GETATTR`,`SETATTR`, and`REMOVE`. Expressed as average latency per second, grouped by operation.`resourceId`

`mountTargetId`

`operation`
`MetadataIOPS`Metadata IOPs operation IOPs (Input/Output Operations Per Second) for the following NFS operations:`CREATE`,`GETATTR`,`SETATTR`, and`REMOVE`. Expressed as operations per second.
`FileSystemUsage`Usage bytes Total space utilization for a file system. Expressed as`GiB`consumed per second.`resourceId`

`mountTargetId`
`UserSoftQuotaViolations`Soft Quota Violations count Number of write requests that exceeded soft quota.

`resourceId`

`resourceName`

`resourceType`
`UserHardQuotaViolations`Hard Quota Violations count Number of write requests that exceeded hard quota.
`snapshotsGovernanceMode`Snapshots in Governance Mode count Count of snapshots in governance lock mode.`tenantId`
`snapshotsComplianceMode`Snapshots in Compliance Mode count Count of snapshots in compliance lock mode.`tenantId`
`retentionLockDuration`Retention Lock Duration days Retention lock duration for snapshot locks.`lockMode`

### Replication Metrics

Metric Metric Display Name Unit Description Dimensions
`ReplicationThroughput`

Replication Throughput bytes Throughput of the data transferred out of the source file system. Expressed as bytes read per interval.

`resourceId`

`resourceName`

`resourceType`
`ReplicationEgressThroughput`Replication Egress Bytes bytes Data that has been copied out of the source region. Only applicable for cross-region replication. Expressed as a sum of bytes written per interval.
`ReplicationRecoveryPointAge`Replication Recovery Point Age time Age of the last fully copied snapshot that was applied to the target file system. Or, how much older the data on the target file system is than the source file system. Expressed as time since the source snapshot was taken. Monitor this metric to ensure that the data on the target file system isn't older than your requirements allow (RPO).

### Replication Target Metrics

Metric Metric Display Name Unit Description Dimensions
`ReplicationThroughput`

Replication Throughput bytes Throughput of the data written to the target file system. Expressed as bytes written per interval.

`resourceId`

`resourceName`

`resourceType`
`ReplicationRecoveryPointAge`Replication Recovery Point Age time Age of the last fully copied snapshot that was applied to the target file system. Or, how much older the data on the target file system is than the source file system. Expressed as time since the source snapshot was taken. Monitor this metric to ensure that the data on the target file system isn't older than your requirements allow (RPO).

### Mount Target Metrics

Metric Metric Display Name Unit Description Dimensions
`MountTargetReadThroughput`

Read Throughput bytes Read throughput for the mount target. If the mount target exports multiple file systems, total throughput for all file systems is displayed. Expressed as bytes read per interval.

`resourceId`

`throughput`
`MountTargetWriteThroughput`Write Throughput bytes Write throughput for the mount target. If the mount target exports multiple file systems, total throughput for all file systems is displayed. Expressed as bytes written per interval.
`MountTargetConnections`

Connections

count Number of client connections for the mount target. Expressed as total connection count at the interval.`resourceId`
`MountTargetHealth`Health

percent Number of successfully executed NFS API requests. Expressed as a percentage of total requests per interval.`resourceId`

`healthItem`

### Mount Target NFS Metrics

Kerberos Metrics
Metric Metric Display Name Unit Description Dimensions
`KerberosErrors`Kerberos Errors

count Kerberos errors seen by the mount target while receiving IO from an NFS client. Expressed as a sum of errors per interval.

`resourceId`

`mtResourceName`

`errorType`

LDAP Metrics
Metric Metric Display Name Unit Description Dimensions
`LdapRequestThroughput`

LDAP Request Throughput count Requests from the mount target to the LDAP server through its outbound connector. Expressed as request type and outbound connector per interval.

`resourceId`

`mountTargetId`

`mtResourceName`

`obcResourceName`

`requestType`
`LdapRequestAverageLatency`LDAP Request Latency seconds Mount target to LDAP server request latency. Expressed as mean latency, in seconds, by request type and outbound connector.

`resourceId`

`mountTargetId`

`mtResourceName`

`obcResourceName`

`requestType`
`LdapConnectionErrors`LDAP Connection Errors

count Connection failures between the mount target and LDAP server. Expressed as total error count by error type and outbound connector per interval.

`resourceId`

`mountTargetId`

`mtResourceName`

`obcResourceName`

`errorType`
`LdapRequestErrors`

LDAP Request Errors

count LDAP query failures over an established connection between the mount target and LDAP server. Expressed as total error count by error type and outbound connector per interval.

`resourceId`

`mountTargetId`

`mtResourceName`

`obcResourceName`

`requestType`

`errorType`

### Outbound Connector Metrics

Metric Metric Display Name Unit Description Dimensions
`LdapRequestThroughput`

LDAP Request Throughput count Requests from mount targets to the LDAP server through this outbound connector. Expressed as a count of request type per interval.

`resourceId`

`mountTargetId`

`mtResourceName`

`obcResourceName`

`requestType`
`LdapRequestAverageLatency`LDAP Request Latency seconds Mount target to LDAP server request latency for this outbound connector. Expressed as mean latency, in seconds, by request type.

`resourceId`

`mountTargetId`

`mtResourceName`

`obcResourceName`

`requestType`
`LdapConnectionErrors`LDAP Connection Errors

count Connection failures between mount targets and the LDAP server for this outbound connector. Expressed as error count by error type per interval.

`resourceId`

`mountTargetId`

`mtResourceName`

`obcResourceName`

`errorType`
`LdapRequestErrors`

LDAP Request Errors

count LDAP query failures over an established connection between mount targets and the LDAP server for this outbound connector. Expressed as error count by error type per interval.

`resourceId`

`mountTargetId`

`mtResourceName`

`obcResourceName`

`requestType`

`errorType`

## Tips for Working with File Storage Metrics

You can use the following tables to help interpret the data you see in File Storage metric charts. You can familiarize yourself with the typical metrics emitted by the File Storage service using the chart defaults.
Tip  
  
For many charts, the default interval is one minute. If you're setting alarms based on these metrics, we suggest increasing the interval to a value such as 15 minutes to confirm that the behavior is consistent. A one minute spike in throughput, latency, or IOPs might not be a true indication of an issue.

### File System Charts

This chart... shows this information... using these defaults.... that you can use to...

Read Throughput/

Write Throughput

The read or write throughput of your file system in bytes per second. Read/write throughput is averaged across all mount targets that export the file system. Only the default mean statistic is meaningful.
- Statistic - mean
- Interval - 1 minute
- Time range - 3 hours
- y-axis - bytes per second
- Ensure that your workloads have sufficient read/write bandwidth for maximum performance.
- Identify which file systems have the highest and lowest throughput.
- Receive notifications when read or write throughput is above or below tolerance, so you can take action.

Read Requests/

Write Requests

Read or write operation requests processed by your file systems in bytes per second. Each operation is placed in one of these three size groups:
- `0-8 KiB`
- `8-64 KiB`
- `64 KiB - 1 MiB`

Only the default mean statistic is meaningful.
- Statistic - mean
- Interval - 1 minute
- Time range - 3 hours
- Grouped by: size
- y-axis - bytes per second
- See which file systems might have lower performance than expected.
- Measure impact of operation size on file system and workload performance.
- Identify and monitor file systems whose workloads are consistently receiving larger read or write requests and compare performance over time.
- Receive notifications when operation bytes per second for a larger group size is too high.

Read Latency/

Write Latency

Average latency of read or write operation requests processed by your file systems in bytes per second. Each operation is placed in one of these three size groups:
- `0-8 KiB`
- `8-64 KiB`
- `64 KiB - 1 MiB`

These charts don't report zero latency, or periods when there are no read/write operations happening. Information is presented in the charts as individual data points.
- Statistic - mean
- Interval - 1 minute
- Time range - 3 hours
- Grouped by: size
- See which file systems might have lower performance than expected due to operation latency.
- Measure impact of operation latency on file system and workload performance.
- Troubleshoot possible network or application issues that might increase file system latency.
- Receive notifications when operation latency exceeds tolerance, so you can take action.
Metadata Latency

Average latency of read or write metadata operation requests processed by your file systems in bytes per second.`CREATE`,`GETATTR`,`SETATTR`, and`REMOVE`operations are shown.

Each operation is placed in one of these three size groups:
- `0-8 KiB`
- `8-64 KiB`
- `64 KiB - 1 MiB`
- Statistic - mean
- Interval - 1 minute
- Time range - 3 hours
- Grouped by: size
- See which metadata operations requested by your workload have the highest and lowest latency.
- Measure impact of metadata operation latency on file system and workload performance.
- Receive notifications when a metadata operation exceeds tolerance.
- Troubleshoot your application workloads.
Metadata IOPs

IOPs per second of read or write metadata operation requests processed by your file systems.`CREATE`,`GETATTR`,`SETATTR`, and`REMOVE`operations are shown.
- Statistic - rate
- Interval - 1 minute
- Time range - 3 hours
- Grouped by: operation
- y-axis - bytes per second
- See which metadata operations requested by your workload have the highest and lowest IOPs.
- Identify specific operations that might consistently have higher or lower IOPs.
- Receive notifications when IOPs for a metadata operation are below tolerance.
- Troubleshoot your application workloads.
User Soft Quota Violations The number of soft quota violations by users of the file system.
- Statistic - sum
- Interval - 1 hour
- Time range - TBD
- y-axis - count
User Hard Quota Violations The number of hard quota violations by users of the file system.
- Statistic - sum
- Interval - 1 hour
- Time range - TBD
- y-axis - count
Usage

The total space utilization for each file system per hour. The data in this chart is presented differently than the utilization value shown in the Details tab of the file system:
- File system utilization is displayed in GiB. This chart displays GB.
- File system utilization is captured once every hour. This chart captures one data point every minute.
- There may be temporary discrepancies between the file system utilization value and the Usage chart. For example, if the usage for a file system briefly spikes during the file system's hourly update, the utilization value may temporarily appear higher than expected when compared to the Usage chart.
- Statistic - mean
- Interval - 1 hour
- Time range - 1 day
- See what the total space utilization is for all of your file systems.
- Identify which of your file systems are consuming the most and least space.
- Identify which of your file systems are incurring the most and least cost.
- Use in conjunction with the information in[File System Usage and Metering](https://docs.oracle.com/en-us/iaas/Content/File/Reference/../Concepts/FSutilization.htm)and receive notifications when usage isn't within expectations.

### Replication Charts

This chart... shows this information... using these defaults.... that you can use to...

Replication Throughput

For replication sources: Average throughput of the data transferred out of the source file system. Calculated from bytes per second over a one minute interval. Only the default mean statistic is meaningful.

For replication targets: Average throughput of the data applied to the target file system. Calculated from bytes per second over a one minute interval. Only the default mean statistic is meaningful.
- Statistic - mean
- Interval - 1 minute
- Time range - 1 hour
- y-axis - bytes per second
- Identify which replications have the highest and lowest throughput.
- Receive notifications when throughput is below tolerance, so you can take action.

Replication Egress Bytes

For replication sources: Bytes that have been copied out of the source region. Only meaningful for cross-region replication.

For replication targets: N/A
- Statistic - sum
- Interval - 1 minute
- Time range - 1 hour
- y-axis - bytes
- Monitor the network transfer costs associated with cross-region replication.

Replication Recovery Point Age Age of the last snapshot that was fully copied from the source and applied to the replication target. Expressed as time since the source snapshot was taken.
- Statistic - mean
- Interval - 1 minute
- Time range - 1 hour
- y-axis - seconds Ensure that the data on the target file system isn't older than your requirements allow (RPO).

### Mount Target Charts

This chart... shows this information... using these defaults.... that you can use to...

Read Throughput/

Write Throughput

The read or write throughput of your mount target in bytes per second. Read/write throughput is averaged across all file systems exported by the mount target. Only the default mean statistic is meaningful.
- Statistic - mean
- Interval - 1 minute
- Time range - 3 hours
- y-axis - bytes per second
- Ensure that your workloads have sufficient read/write bandwidth for maximum performance.
- Identify which mount targets have the highest and lowest throughput.
- Receive notifications when read or write throughput is below tolerance, so you can take action.

Connections

The number of active connections for each mount target. Typically, one connection represents one NFS client.
- Statistic - sum
- Interval - 1 minute
- Time range - 3 hours
- See how many active connections each mount target has.
- Measure impact of high connection count on file system and workload performance.
- Decide if additional mount targets are required for your workload.

Health

The percentage of requests processed successfully by the mount target.
- Statistic - mean
- Interval - 1 minute
- Time range - 3 hours
- See which mount targets have the highest and lowest percentage of successfully processed requests.
- Identify mount targets that aren't performing well and troubleshoot possible causes.
- Receive notifications when mount target health drops below tolerance, so you can take action.

### Mount Target NFS Charts

Mount target NFS charts show the interaction between a single mount target and the LDAP servers it is configured to use. Each mount target can have two outbound connectors. You can determine mount target-specific load and performance interacting with the LDAP server. These charts can also help you determine which outbound connector is being actively used by inspecting requests and error counts. If there are failures, you can determine which outbound connector connection to an LDAP server is failing and why. For more information, see[Using LDAP for Authorization](https://docs.oracle.com/en-us/iaas/Content/File/Reference/../Tasks/ldap.htm)and[Using Kerberos Authentication](https://docs.oracle.com/en-us/iaas/Content/File/Reference/../Tasks/kerberos.htm).

Kerberos Charts
This chart... shows this information... using these defaults.... that you can use to...

Kerberos Errors

Kerberos errors by error type. Error types include the following:
- Kerberos no keytab
- Kerberos no key
- Kerberos key version number mismatch
- Kerberos clock skew
- Kerberos Keytab Load Success*

*Kerberos Keytab Load Success is not an error.
- Statistic - sum
- Interval - 1 minute
- Time range - 1 hour
- y-axis - count of errors
- Receive notifications when errors occur, so that you can take action.

LDAP Charts
This chart... shows this information... using these defaults.... that you can use to...

LDAP Request Throughput

Requests from the mount target to the LDAP server through its outbound connector. Expressed as a count of request type by outbound connector and interval. Request types include:
- Ldap UserId By UserName Request Throughput
- Ldap UserName By UserId Request Throughput
- Ldap GroupIdList By UserName Request Throughput
- Statistic - sum
- Interval - 1 minute
- Time range - 1 hour
- y-axis - number of requests per minute
- Confirm which outbound connectors per mount target are being used. When rotating passwords, it's critical to know exactly which outbound connector is active.
- Troubleshoot NFS performance problems by inspecting LDAP request throughput and latency.

LDAP Request Latency

Mount target to LDAP server request latency. Expressed as mean latency, in seconds, by request type and outbound connector. Request types include:
- Ldap UserId By UserName Request Throughput
- Ldap UserName By UserId Request Throughput
- Ldap GroupIdList By UserName Request Throughput
- Statistic - mean
- Interval - 1 minute
- Time range - 1 hour
- y-axis - request latency in seconds
- Troubleshoot NFS performance problems by inspecting LDAP request throughput and latency.

LDAP Connection Errors

Connection failures between the mount target and LDAP server. Expressed as error count by error type and outbound connector. Error types include:
- LDAP Connection Timeout
- LDAP Connection Refused/Reset
- LDAP Name Resolution Failure
- LDAP Bind Login Failed
- LDAP Certificate Validation Failure
- LDAP connection success*

*LDAP connection success is not an error.
- Statistic - sum
- Interval - 1 minute
- Time range - 1 hour
- y-axis - count of errors
- Determine why connectivity from either outbound connector or mount target is failing.
- See a per mount target view of LDAP server connectivity by outbound connector.
- Receive notifications when errors occur, so that you can take action.

LDAP Request Errors

LDAP query failures over an established connection between the mount target and LDAP server. Expressed as total error count by query type and outbound connector per interval. Query types include:
- Lookup Username by UID
- Lookup UID by Username
- Lookup User Groups
- Statistic - sum
- Interval - 1 minute
- Time range - 1 hour
- y-axis - count of errors Monitor the network transfer costs associated with cross-region replication.

### Outbound Connector Charts

Outbound connector charts show a view of all ongoing LDAP operations across all mount targets for a given availability domain for that outbound connector. You can use these charts to determine if the aggregate load a given outbound connector generates is too high. You can also see if an outbound connector is working for some mount targets, but not others. For more information, see[Using LDAP for Authorization](https://docs.oracle.com/en-us/iaas/Content/File/Reference/../Tasks/ldap.htm)and[Managing Outbound Connectors](https://docs.oracle.com/en-us/iaas/Content/File/Reference/../Tasks/managing-outbound-connectors.htm).

This chart... shows this information... using these defaults.... that you can use to...

LDAP Request Throughput

Requests from the mount target to the LDAP server through its outbound connector. Expressed as a count of request type by outbound connector and interval. Request types include:
- Ldap UserId By UserName Request Throughput
- Ldap UserName By UserId Request Throughput
- Ldap GroupIdList By UserName Request Throughput
- Statistic - sum
- Interval - 1 minute
- Time range - 1 hour
- y-axis - number of requests per minute
- Understand the aggregate load all mount targets are placing on your LDAP servers.
- Troubleshoot NFS performance problems by inspecting LDAP request throughput and latency.

LDAP Request Latency

Mount target to LDAP server request latency. Expressed as mean latency, in seconds, by request type and outbound connector. Request types include:
- Ldap UserId By UserName Request Throughput
- Ldap UserName By UserId Request Throughput
- Ldap GroupIdList By UserName Request Throughput
- Statistic - mean
- Interval - 1 minute
- Time range - 1 hour
- y-axis - request latency in seconds
- Troubleshoot NFS performance problems by inspecting LDAP request throughput and latency.

LDAP Connection Errors

Connection failures between the mount target and LDAP server. Expressed as error count by error type and outbound connector. Error types include:
- LDAP Connection Timeout
- LDAP Connection Refused/Reset
- LDAP Name Resolution Failure
- LDAP Bind Login Failed
- LDAP Certificate Validation Failure
- LDAP connection success*

*LDAP connection success isn't an error.
- Statistic - sum
- Interval - 1 minute
- Time range - 1 hour
- y-axis - count of errors
- Determine why connectivity from the outbound connector is failing
- See a per login view of LDAP server connectivity. For example, do LDAP requests from one mount target succeed and requests from another fail?
- Receive notifications when errors occur, so that you can take action.

LDAP Request Errors

LDAP query failures over an established connection between the mount target and LDAP server. Expressed as total error count by query type and outbound connector per interval. Query types include:
- Lookup Username by UID
- Lookup UID by Username
- Lookup User Groups
- Statistic - sum
- Interval - 1 minute
- Time range - 1 hour
- y-axis - count of errors Receive notifications when errors occur, so that you can take action.

## Using the Console

[To view default metric charts for a single file system](https://docs.oracle.com/en-us/iaas/Content/File/Reference/filemetrics.htm#)

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Reference/../Tasks/list-file-systems.htm).
- Select Metrics .

For more information about monitoring metrics and using alarms, see[Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see[Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).

[To view default metric charts for a single mount target](https://docs.oracle.com/en-us/iaas/Content/File/Reference/filemetrics.htm#)

- On the Mount Targets list page, select the mount target that you want to work with. If you need help finding the list page or the mount target, see[Listing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Reference/../Tasks/list-mount-targets.htm).
- Select Metrics .

For more information about monitoring metrics and using alarms, see[Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see[Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).

[To view default metric charts for a single outbound connector](https://docs.oracle.com/en-us/iaas/Content/File/Reference/filemetrics.htm#)

- On the Outbound Connectors list page, select the outbound connector that you want to work with. If you need help finding the list page or the outbound connector, see[Listing Outbound Connectors](https://docs.oracle.com/en-us/iaas/Content/File/Reference/../Tasks/list-outbound-connectors.htm).
- Select Metrics .

For more information about monitoring metrics and using alarms, see[Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see[Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).

[To view default metric charts for multiple file systems and mount targets](https://docs.oracle.com/en-us/iaas/Content/File/Reference/filemetrics.htm#)

- Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Service Metrics .
- For Compartment , select the compartment that contains the resources that you're interested in.
- 

For Metric namespace , select`oci_filestorage`.

The Service Metrics page dynamically updates the page to show charts for each metric that's emitted by the selected metric namespace.

For more information about monitoring metrics and using alarms, see[Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see[Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following APIs for monitoring:
- [Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/)for metrics and alarms
- [Notifications API](https://docs.oracle.com/iaas/api/#/en/notification/latest/)
