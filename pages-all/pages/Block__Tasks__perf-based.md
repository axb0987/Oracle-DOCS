# Performance-Based Dynamic Scaling
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/perf-based.htm
- Fetched: 2026-09-05 01:47 CDT

# Performance-Based Dynamic Scaling

The performance based autotuning feature enables Block Volume to adjust the volume's performance between levels you specify, based on the actual monitored performance of a volume.

Tasks:
- [Enabling Performance-based Autotuning for a New Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/perf-based-new.htm)
- [Enabling Performance-based Autotuning for an Existing Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/perf-based-existing.htm)

When you enable performance-based dynamic scaling with autotuning, you specify the default performance setting (VPUs/GB), which is lowest performance level the volume will be adjusted to when attached to an instance. You also specify the maximum performance level (VPUs/GB), which is the maximum performance level the volume will be adjusted to. Block Volume monitors the volume's performance using the following metrics:
- Volume throttled operations
- Volume guaranteed VPUs/GB
- Volume guaranteed IOPS
- Volume guaranteed throughput

These metrics help the service determine the load on the volume and whether the performance level needs to be adjusted. For more information about these metrics, see[Descriptions: Performance Metrics](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../References/volumemetrics-reference.htm#perfmetrics)and[Block Volume Metrics](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../References/volumemetrics.htm).

When viewing the Block Volume Details or Boot Volume Details pages in the Console, the applicable fields are:
- 

Default Performance : When Performance Based Auto-tune is enabled, this is the lowest performance level that Block Volume will adjust the performance to when the volume is attached. If Performance Based Auto-tune is disabled, this is the volume's performance level. If you have enabled Detached Volume Auto-tune , and the volume is detached, this is the performance level the volume will be adjusted to when the volume is reattached to an instance.
- 

Auto-tuned Performance : This is the volume's effective performance. If Performance Based Auto-tune is disabled for the volume, this is the same as the default performance for the volume.
- 

Performance Based Auto-tune : This field indicates whether the performance based autotuning feature is enabled for the volume. When it is off, the volume's Auto-tuned Performance is always the same as what is specified for Default Performance .

When Performance Based Auto-tune is enabled, Block Volume adjusts the performance to the default level as much as possible. As load on the volume increases, the service ramps up the performance level up as needed, on a best-effort basis.
