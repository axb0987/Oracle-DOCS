# High Performance Computing Metrics
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/References/high-performance-computing-metrics.htm
- Fetched: 2026-09-05 01:49 CDT

# High Performance Computing Metrics

Oracle Cloud Infrastruture provides specialized metrics to improve visibility into the performance of HPC instances.

HPC metrics are similar to standard compute instance metrics, however, the HPC metrics are available only on instances that have the HPC plugin with GPU and RDMA monitoring enabled and are located in the`gpu_infrastructure_health`and`rdma_infrastructure_health`customer namespaces. See[Compute Instance Metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm)for details on accessing and managing compute metrics.

## Available Metrics: gpu_infrastructure_health

The compute instance metrics help you measure the activity level and throughput of compute instances. The metrics listed in the following table are available for any[monitoring-enabled](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/enablingmonitoring.htm)compute instance. To get these metrics, enable monitoring on the instance.

The metrics in this namespace are aggregated across all the related resources on the instance. For example,`DiskBytesRead`is aggregated across all the instance's attached storage volumes, and`NetworkBytesIn`is aggregated across all the instance's attached VNICs.

For metrics emitted by the metric namespace`gpu_infrastructure_health`, data points are sampled every ten seconds. A batch of six of data points is emitted every minute. Therefore, for every minute granularity, the aggregate count is always six, the aggregate sum is the sum of the six data points, and the aggregate average is the average of the six data points.

You also can use the Monitoring service to create[custom queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric.htm).

Each metric includes the following dimensions : component GPU or rdma_nic timestamp UTC time when the payload/heartbeat is emitted version The payload version number for compatibility

Metric Metric Display Name Unit Description Dimensions
`GpuUtilization`GPU utilization percent

Activity level from GPU. Expressed as a percentage of total time.

For instance pools, the value is averaged across all instances in the pool.

`availabilityDomain`

`faultDomain`

`gpuId`

`imageId`

`instancePoolId`

`region`

`resourceDisplayName`

`resourceId`

`shape`
`GpuMemoryUtilization`GPU memory utilization percent The percentage of the GPU memory resource in use.
`GpuPowerDraw`GPU power draw integer The amount of GPU power used.
`GpuTemperature`GPU temperature integer The GPU temperature reported.
`GpuEccSingleBitErrors`GPU single-bit errors integer The number of GPU single bit ECC errors reported.
`GpuEccDoubleBitErrors`GPU double-bit errors integer The number of GPU double bit ECC errors reported.

### Fault Metrics: gpu_infrastructure_health

Metric Metric Display Name Unit Description Dimensions
`Fault`GPU fault count

If the value is 0, there are no faults. If the value is 1, faults are detected.

`availabilityDomain`

`faultCode`

`faultDomain`

`gpuId`

`imageId`

`instancePoolId`

`pcieAddress`

`region`

`resourceDisplayName`

`resourceId`

`shape`

## Available Metrics: rdma_infrastructure_health

The compute instance metrics help you measure activity level and throughput of compute instances. The metrics listed in the following table are available for any[monitoring-enabled](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/enablingmonitoring.htm)compute instance. To get these metrics, enable monitoring on the instance.

The metrics in this namespace are aggregated across all the related resources on the instance. For example,`DiskBytesRead`is aggregated across all the instance's attached storage volumes, and`NetworkBytesIn`is aggregated across all the instance's attached VNICs.

For metrics emitted by the metric namespace`rdma_infrastructure_health`, data points are sampled every ten seconds. A batch of six of data points is emitted every minute. Therefore, for every minute granularity, the aggregate count is always six, the aggregate sum is the sum of the six data points, and the aggregate average is the average of the six data points.

You also can use the Monitoring service to create[custom queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric.htm).

Each metric includes the following dimensions : component GPU or rdma_nic timestamp UTC time when the payload/heartbeat is emitted version The payload version number for compatibility

Metric Metric Display Name Unit Description Dimensions
`RdmaTxBytes`RDMA aggregate network transmit bytes bytes The bytes transmitted on the RDMA interface.

`availabilityDomain`

`faultDomain`

`imageId`

`instancePoolId`

`rdmaId`

`region`

`resourceDisplayName`

`resourceId`

`shape`
`RdmaRxBytes`RDMA aggregate network receive bytes bytes The bytes received on the RDMA interface.
`RdmaTxPackets`RDMA aggregate network transmit packets integer The number of RDMA interface packets transmitted.
`RdmaRxPackets`RDMA aggregate network receive packets integer The number of RDMA interface packets received.

### Fault Metrics: rdma_infrastructure_health

Metric Metric Display Name Unit Description Dimensions
`RdmaLinkSpeedFault`Faults count Detects if a link speed fault is present.

If the value is 0, there are no faults. If the value is 1, faults are detected.

`availabilityDomain`

`faultDomain`

`imageId`

`instancePoolId`

`pcieAddress`

`rdmaId`

`region`

`resourceDisplayName`

`resourceId`

`shape`
`RdmaPcieAddressFault`Faults count Detects if a PCIE address fault is present.

If the value is 0, there are no faults. If the value is 1, faults are detected.
`RdmaPcieBerCheckFault`Faults count Detects if a PCIE BER fault is present.

If the value is 0, there are no faults. If the value is 1, faults are detected.
`RdmaPcieCableFlapFault`Faults count Detects if a PCIE cable flap fault is present.

If the value is 0, there are no faults. If the value is 1, faults are detected.
`RdmaPcieCablePlugFault`Faults count Detects if a PCIE cable plug fault is present.

If the value is 0, there are no faults. If the value is 1, faults are detected.
`RdmaPcieCableStateFault`Faults count Detects if a PCIE cable state fault is present.

If the value is 0, there are no faults. If the value is 1, faults are detected.

## Available Metrics: oci_gpu_infrastructure

The compute instance metrics help you measure activity level and throughput of compute instances. The metrics listed in the following table are available for any[monitoring-enabled](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/enablingmonitoring.htm)compute instance. To get these metrics, enable monitoring on the instance.

For metrics emitted by the metric namespace`oci_gpu_infrastructure`, data points are sampled every minute. A batch of 13 data points is emitted every minute. For a host with N RDMA NICs , each metric produces N datapoints/minute .

For the 13 new metrics in this table, the total datapoints per host per minute are:

RDMA NICs/host Datapoints per metric/minute Total datapoints/minute (all 13 metrics)
1 1 13
4 4 52
8 8 104
16 (worst case) 16 208

You also can use the Monitoring service to create[custom queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric.htm).

Each metric includes the following dimensions : component GPU or rdma_nic timestamp UTC time when the payload/heartbeat is emitted version The payload version number for compatibility

### Metric Counters: oci_gpu_infrastructure

Metric Metric Display Name Unit Description Dimensions
`NpEcnMarkedRocePacketsCount`Count count

ECN-marked RoCEv2 packets received (ECN=11).

RDMA HW counter.

`baremetal_cluster_ocid`

`customer_network_block_ocid`

`gpu_shape`

`host_serial`

`hpc_island_id`

`poolname`

`port_pci`

`tailnode_serial`
`OutOfSequenceCount`Count count

Out-of-sequence packets received.

Error counter.
`NpCnpSentCount`Count count

CNP packets sent by Notification Point.

RDMA HW counter.
`RpCnpHandledCount`Count count

CNP packets handled by Reaction Point.

RDMA HW counter.
`SymbolErrorCount`Count count

Minor link errors on physical lanes.

Port counter.
`TxPacketsPhyCount`Count count

Packets transmitted on physical port.

Ethtool counter.
`RxPacketsPhyCount`Count count

Packets received on physical port.

Ethtool counter.
`RxMulticastPhyCount`Count count

Multicast packets received.

Ethtool counter.
`RxCrcErrorsPhyCount`Count count

Packets dropped due to CRC errors.

Error counter.
`RxDiscardsPhyCount`Count count

Packets dropped due to lack of buffers.

Congestion indicator.
`TxDiscardsPhyCount`Count count

Packets discarded on transmit.

Congestion indicator.
`LinkDownEventsPhyCount`Count count

Link transitioned to DOWN (flapping).

Link health.
`RxPcsSymbolErrPhyCount`Count count

PCS symbol errors not corrected by FEC.

Link health.

## High Performance Computing Policies

Create a dynamic group

This example creates a group that contains all instances in a specific compartment.
```

```

Use Fault Management by OCI

This example creates a policy that allows OCI to manage your faults.
```

```
or
```

```
