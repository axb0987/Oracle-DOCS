# Block Volume Performance Tests on Windows-Based Instances
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/bv-perf-win-tests.htm
- Fetched: 2026-09-05 01:44 CDT

# Block Volume Performance Tests on Windows-Based Instances

This guide provides a repeatable method to benchmark OCI Block Volume performance and interpret results for Windows and Linux hosts.

## 1. Purpose

This guide provides a repeatable method to benchmark OCI Block Volume performance and interpret results for Windows and Linux hosts.

Use this guide to:
- Validate IOPS, throughput, and latency behavior.
- Compare observed results against expected Block Volume and instance limits.
- Identify common bottlenecks such as throttling, insufficient queue depth, instance shape limits, attachment configuration, and workload contention.
- Collect the right evidence before opening a support request.

## 2. Scope

Consider the following concepts when determining the scope for your tests.

Area In Scope Out of Scope
Performance validation IOPS, throughput, latency testing for OCI Block Volumes and Boot Volumes Application-level tuning, database tuning, non-OCI storage tuning
Tools fio on Linux, DiskSpd on Windows Third-party storage appliance benchmarks
Investigation Interpreting benchmark results and OCI metrics Long-term remediation or incident-specific RCA

## 3. Safety Warning

Benchmarking can generate high I/O load. Write tests can overwrite data. Before running any command:
- Use a disposable test volume whenever possible.
- Do not run write-heavy tests against production data.
- Do not run raw-device write tests unless the device is dedicated to benchmarking.
- Confirm the target device or file path before starting the test.
- Prefer file-level tests for safer validation.
- Run tests during an approved maintenance or test window if using a production host.

## 4. Before You Test

Before you test, record the following information.

Check Required Action
Volume identity Record the volume OCID, region, availability domain, size, and performance level.
Instance identity Record the instance OCID, shape, OCPU count, operating system, and attachment type.
Expected limits Check volume size/VPU limits and instance shape limits before interpreting results.
Workload isolation Stop or account for application/background I/O during tests.
Test target Use a dedicated test file or a dedicated raw block device.
Caching Use direct I/O / cache-bypass options in the test tool.
Metrics Capture OCI Block Volume metrics during the exact test window.
Tool version Record fio --version or DiskSpd version.

## 5. Determine Expected Performance First

Do not conclude that a volume is under performing until expected limits are calculated.

Effective performance is constrained by multiple limits. The effective maximum is the minimum of the following limits:
- Volume-size-derived limit
- Volume performance tier / VPU limit
- Maximum per-volume service limit
- Instance shape Block Volume IOPS / throughput limit
- Attachment and multipath configuration limits
- Guest OS / application / benchmark configuration limits

### Example Interpretation

The following table provides example scenarios along with example interpretations of those scenarios.

Scenario Interpretation
Volume can provide 50,000 IOPS, but instance shape supports 25,000 IOPS Expected maximum is 25,000 IOPS because the instance is the bottleneck.
Volume is small and does not have enough size-derived IOPS even at higher VPU Increase volume size or adjust workload expectations.
VolumeThrottledIOs is non-zero during the test Workload is hitting a configured or service-side limit. Validate volume size, VPU, and instance limits.
No throttling, but IOPS is low Check queue depth, threads, attachment type, multipath, guest CPU, filesystem, and competing workload.

Reference:[OCI Block Volume Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm)

## 6. Standard Benchmark Profiles

The following table provides suggested values for benchmarking.

Goal Block Size Pattern Queue Depth Threads / Jobs Duration Primary Metric
IOPS 4 KiB Random read or random mixed 64-128 4-8 120s+ IOPS
Throughput 256 KiB Sequential read or mixed 32-64 4-8 120s+ MB/s
Baseline latency 4 KiB Random read 1 1 120s+ avg, p95, p99 latency

Run each test more than once when validating a performance claim. Use the median result and retain latency percentiles.

## 7. Why I/O Size Matters

The table provides suggested I/O sizes to use during testing.

Test Goal Recommended I/O Size Reason
IOPS 4 KiB Small random I/O is the standard way to measure maximum operations per second.
Throughput 256 KiB or larger Larger I/O sizes transfer more data per operation and better measure bandwidth.
Latency 4 KiB Small I/O with low queue depth measures baseline response time without queueing effects.

Do not compare a 4 KiB random IOPS test to a 256 KiB throughput test as if they measure the same behavior. If the application uses a different I/O size, run an additional workload-specific profile after the standardized baseline test.

## 8. Why Queue Depth Matters

Queue depth is the number of outstanding I/O requests submitted to the storage path at the same time.

Queue Depth What It Measures When To Use
1 Baseline latency for a single outstanding I/O Latency and application response-time investigation
32-64 Moderate concurrency and throughput Sequential throughput or general validation
64-128+ Saturation behavior and maximum IOPS High-performance random I/O testing

A single thread with queue depth 1 usually cannot drive the maximum IOPS of a high-performance volume because each I/O must complete before the next one is submitted. Higher queue depth keeps multiple I/O requests in flight and is normally required to validate provisioned IOPS or throughput.

High queue depth can also increase latency. Always review p95 and p99 latency when using high queue depth.

## 9. Linux Benchmarking With fio

Follow these steps to benchmark using`fio`.

### 9.1 Identify the Test Device

Use stable identifiers when possible.

```

```

Do not assume`/dev/sdX`is the correct device. Device names can change after reboot or attach/detach operations.

### 9.2 Check fio Version

To check`fio`version, use:

```

```

### 9.3 IOPS: Read-Only Raw Device Test

This test is read-only but still generates high I/O load.

```

```

### 9.4 IOPS: Mixed File-Level Test

This test writes to the specified test file. Do not point it at application data.

```

```

### 9.5 Throughput: Read-Only Raw Device Test

The command tests read throughput.

```

```

### 9.6 Baseline Latency: Read-Only Raw Device Test

This command tests latency on a read-only device.

```

```

## 10. Windows Benchmarking With DiskSpd

Use the official DiskSpd releases:[DiskSpd GitHub Releases](https://github.com/microsoft/diskspd/releases)

### 10.1 Prepare a Test File

Use a dedicated test file on the target volume. Do not use application data files.

Example using`fsutil`:
```

```

This creates a 100 GiB test file.

### 10.2 IOPS: Random Read

This command performs a random read test.
```

```

### 10.3 IOPS: Random Mixed 50/50

This test writes to the test file.
```

```

### 10.4 Throughput: Sequential Read

This command tests throughput for sequential reads.
```

```

### 10.5 Baseline Latency: Random Read With Single Outstanding I/O

This command tests latency for random reads.
```

```

### 10.6 Windows Caveats

Windows results can be affected by filesystem behavior, antivirus scanning, filter drivers, backup agents, and guest CPU saturation. Disable or account for those factors before interpreting results.

## 11. fio and DiskSpd Parameter Mapping

This table compares`fio`and`DiskSpd`parameter options.

Intent fio DiskSpd
Random read --rw=randread -r -w0
Random mixed --rw=randrw --rwmixread=50 -r -w50
Sequential read --rw=read -si -w0
Block size --bs=4k / --bs=256k -b4K / -b256K
Queue depth --iodepth -o
Concurrency --numjobs -t
Runtime --runtime=120 --time_based -d120
Disable cache --direct=1 -Sh
Latency output latency percentiles -L

## 12. How To Read Results

The following table provides suggestions on what to check for various testing areas.

Result Area What To Check Interpretation
IOPS Total read/write IOPS for the workload Compare against calculated expected IOPS.
Throughput MB/s or MiB/s Compare against calculated expected throughput.
Average latency Mean response time Useful, but can hide tail latency.
p95/p99 latency Tail response time High tail latency can indicate queueing, throttling, noisy workload, or path bottleneck.
CPU usage Guest CPU and system CPU Benchmark can become CPU-bound before storage is saturated.
Throttling VolumeThrottledIOs during test window Nonzero throttling means workload exceeded a limit.

## 13. Throttling Metrics To Check

Block Volume metrics are emitted in the`oci_blockstore`metric namespace.

Metric / Signal What It Indicates Interpretation
VolumeThrottledIOs Total I/O operations throttled during the interval Workload is exceeding a configured or service-side limit.
Read/write operations Current IOPS Compare against expected IOPS.
Read/write throughput Current MB/s Compare against expected throughput.
Read/write latency Service response time High latency with throttling suggests saturation; high latency without throttling needs broader investigation.

References:
- [Block Volume Metrics](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../References/volumemetrics.htm)
- [Block Volume Metrics Reference](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../References/volumemetrics-reference.htm)
- [Boot Volume Metrics](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../References/bootvolumemetrics.htm)

## 14. Troubleshooting Low Performance

If your tests indicate low performance, consider the following troubleshooting steps.

Symptom Likely Area What To Check
Low IOPS, low queue depth Test configuration Increase queue depth and thread count for max-IOPS testing.
Low IOPS, high throttling Volume or instance limit Validate volume size, VPU, per-volume limit, and instance shape limit.
Low throughput with small I/O size Test profile Use larger block size such as 256 KiB for throughput testing.
High p99 latency with high queue depth Queueing / saturation Compare against queue depth 1 latency and check throttling.
Low results only during production workload Workload contention Re-test on dedicated volume/host or during quiet window.
UHP volume below expected performance Multipath / attachment Validate UHP prerequisites and multipath status.
No throttling but poor results Host/path/workload Check CPU, network, attachment type, multipath, OS logs, and competing I/O.

## 15. Ultra High Performance and Multipath Checks

For Ultra High Performance volumes, validate that the attachment is multipath-enabled and the guest operating system supports the required configuration.

Important checks:
- Confirm the volume is configured for the expected UHP level.
- Confirm the instance shape supports UHP and the required number of attachments.
- Confirm multipath is enabled for the attachment.
- Confirm the Block Volume Management plugin and guest configuration are correct where required.

References:
- [Configuring Attachments to Ultra High Performance Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/configuringmultipathattachments.htm)
- [Troubleshooting Ultra High Performance Volume Attachments](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/troubleshootingmultipathattachments.htm)

## 16. What To Provide When Opening a Support Request

If you determine you need to engage support, include the following information to make performance investigation actionable:

Required Information Example / Notes
Volume OCID Block Volume or Boot Volume OCID
Instance OCID Instance where the test ran
Region and availability domain Include fault domain if relevant
Volume size and VPU setting Include whether UHP is enabled
Instance shape Include OCPU count and OS version
Attachment type iSCSI, paravirtualized, multipath status
Test command Exact fio or DiskSpd command used
Tool version fio --version or DiskSpd version
Test timestamp UTC start/end time
Test output Full command output, including latency percentiles
OCI metrics IOPS, throughput, latency, and VolumeThrottledIOs for the test window
Workload context Whether production workload was active during the test
Expected result Expected IOPS/throughput calculation and source documentation

## 17. References

Consider the following links for more information.
- [OCI Block Volume Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm)
- [Attaching a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/attach-compute-volume-attachment.htm)
- [Higher Performance on Block Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumehigherperformance.htm)
- [Block Volume Overview](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../blockvolumes.htm)
- [Block Volume Metrics](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../References/volumemetrics.htm)
- [Block Volume Metrics Reference](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../References/volumemetrics-reference.htm)
- [DiskSpd GitHub Repository](https://github.com/microsoft/diskspd)
- [DiskSpd Releases](https://github.com/microsoft/diskspd/releases)
- [Sample fio commands](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../References/samplefiocommandslinux.htm)
