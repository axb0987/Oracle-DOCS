# Ultra High Performance
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeultrahighperformance.htm
- Fetched: 2026-09-05 01:44 CDT

# Ultra High Performance

The Ultra High Performance level is recommended for workloads with the highest I/O requirements, requiring the best possible performance, such as large databases.

This option provides the best linear performance scale with 225 IOPS/GB up to a maximum of 300,000 IOPS per volume (150,000 IOPS for paravirtualized attached volumes). Throughput also scales at the highest rate at 1,800 KB/s/GB up to a maximum of 2,680 MB/s per volume.

To optimize performance for a volume configured for the Ultra High Performance level, the volume attachment needs to be enabled for multipath. See[Attaching Ultra High Performance Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/attach-compute-volume-attachment.htm#multipath)and[Checking If a Volume Attachment is Multipath-Enabled](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/get-multipath-enable-check-compute-volume-attachment.htm)for more information.

See[Troubleshooting Ultra High Performance Volume Attachments](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/troubleshootingmultipathattachments.htm)for steps to take to troubleshoot issues you encounter when attaching a volume configured for the Ultra High Performance level.

See[Performance Details for Shapes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm#shapes_block_details)for performance characteristics and instance details for Compute shapes, as well as whether the shape supports multipath-enabled attachments for the Ultra High Performance level.
Note  
  
When you change the volume performance to Ultra High Performance from any other performance level you need to detach and then reattach the volume. See[Detaching a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/detachingavolume.htm)and[Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/attach-compute-volume-attachment.htm).

## Boot Volumes and Ultra High Performance

Boot volumes for VM instances with paravirtualized attachments support the Ultra High Performance level. Boot volumes configured for the Ultra High Performance level do not use multipath-enabled attachments, so the details about enabling and troubleshooting multipath-enabled attachments do not apply to boot volumes.

When a boot volume is configured for 120 VPUs/GB, the performance is 225 IOPS/GB. The performance scale factor will follow the VPUs/GB scale, with a maximum performance of 50,000 IOPS. Maximum performance for smaller boot volume sizes will be lower. Consider the following examples:
- 

Boot volume sized at 50 GBs, configured for the Ultra High Performance level, at 120 VPUs/GB. The maximum performance for this volume is 11,250 IOPS. (50 GB x 225 IOPS/GB = 11,250.)
- 

Boot volume sized at 223 GBs, configured for the Ultra High Performance level, at 120 VPUs/GB. The maximum performance for this volume is 50,000 IOPS. (223 GB x 225 IOPS/GB = 50,175, so maximum performance of 50,000 IOPS.) The minimum boot volume size to achieve the maximum performance of 50,000 IOPS is 223 GB. You can resize boot volumes, see[Resizing a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/resizingavolume.htm)for more information.
Note  
  
To achieve the maximum of 50,000 IOPS on VM instances, the number of configured OCPUs should be greater than or equal to 8.

## Performance Characteristics

The following table lists the performance characteristics for the specified number of volume performance units (VPUs) for the Ultra High Performance option.

Volume Performance Units (VPUs)

IOPS per GB

Max IOPS per Volume

Size for Max IOPS (GB)

KBPS per GB

Max MBPS per Volume
30 90 75,000 833 720 880
40 105 100,000 952 840 1,080
50 120 125,000 1,042 960 1,280
60 135 150,000 1,111 1,080 1,480
70 150 175,000 1,167 1,200 1,680
80 165 200,000 1,212 1,320 1,880
90 180 225,000 1,250 1,440 2,080
100 195 250,000 1,282 1,560 2,280
110 210 275,000 1,310 1,680 2,480
120 225 300,000 1,333 1,800 2,680

## Volume Size and Performance

The following table lists the Block Volume service's throughput and IOPS performance numbers based on volume size for the Ultra High Performance level, at 120 VPUs. IOPS and KB/s performance scales linearly per GB volume size up to the service maximums so you can predictably calculate the performance numbers for a specific volume size. If you're trying to achieve certain performance targets for volumes configured to use the Ultra High Performance level you can provision a minimum volume size using this table as a reference.

Volume Size

Max Throughput

(1 MB block size)

Max Throughput

(8 KB block size)

Max IOPS

(4 KB block size)
50 GB 90 MB/s 45 MB/s 11,500
100 GB 180 MB/s 90 MB/s 23,000
200 GB 360 MB/s 180 MB/s 46,000
400 GB 720 MB/s 360 MB/s 92,000
600 GB 1,080 MB/s 560 MB/s 138,000
800 GB 1,440 MB/s 760 MB/s 184,000
1,024 GB 1,842 MB/s 940 MB/s 235,320
1,200 GB 2,160 MB/s 1,024 MB/s 276,000
