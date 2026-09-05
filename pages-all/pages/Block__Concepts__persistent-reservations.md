# Persistent Reservations
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/persistent-reservations.htm
- Fetched: 2026-09-05 01:44 CDT

# Persistent Reservations

SCSI Persistent Reservation (SCSI PR) is a feature of the SCSI (Small Computer System Interface) protocol that allows multiple devices to share access to a single storage device. This feature enables applications to reserve and manage access to the shared storage device. This feature is particularly useful in environments where multiple devices need to share access to a single storage device especially in clustering environments.

For more information about SCSI PR, see[SCSI Primary Commands - 3 (SPC-3)](https://www.t10.org/members/w_spc3.htm). For more information about attaching block volumes to multiple instances, see[Attaching a Volume to Multiple Instances](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/attach-to-multiple-instances-compute-volume-attachment.htm).

## Tasks

Following are tasks that you can do with persistent reservations.
- [Enabling Persistent Reservations for an Existing Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/enable-persistent-reservations-existing.htm)
- [Enabling Persistent Reservations for a New Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/enable-persistent-reservations-new.htm)

## Limitations and Considerations

Persistent reservations are supported for iSCSI-attached volumes, for new and existing block volumes attached to Linux and Windows-based instances.
- Persistent reservations aren't supported for the following:
- Boot volumes, including boot volumes attached to instances as data volumes for troubleshooting.
- Paravirtualized-attached volumes.
- You can't configure the persistent reservation setting while a volume is attached to an instance.
- When you create block volumes during the compute instance creation process, you can't configure the persistent reservation setting until after the volume is created.
- For a volume configured for the Ultra High Performance level with persistent reservations enabled, the maximum performance available is 50,000 IOPS. For more information, see[Volume Performance with Persistent Reservations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/persistent-reservations.htm#performance).

## Volume Performance with Persistent Reservations

Block volumes with persistent reservations enabled support the Ultra High Performance level. However, such volumes don't use multipath-enabled attachments, so the details about enabling and troubleshooting multipath-enabled attachments don't apply to these volumes.

Higher Performance level maximums are supported by a block volume that is enabled for persistent reservations and attached to a single instance. To achieve the maximum performance associated with the Ultra High Performance level, configure the Ultra High Performance level for the volume and attach the volume to more than one instance. The combined performance from all attachments will be up to the Ultra High Performance level maximums.

For more information about performance levels, see[Block Volume Performance Levels](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels)
