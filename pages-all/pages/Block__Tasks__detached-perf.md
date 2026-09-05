# Detached Volume Performance Autotuning
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detached-perf.htm
- Fetched: 2026-09-05 01:46 CDT

# Detached Volume Performance Autotuning

The detached volume performance autotuning feature enables Block Volume to adjust the volume's performance level to the optimal level based on the attached state of the volume.

Tasks:
- [Enabling Detached Volume Autotuning for a New Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detached-perf-new.htm)
- [Enabling Detached Volume Autotuning for an Existing Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detached-perf-existing.htm)

If this feature is enabled, when the volume is detached, the Block Volume service adjusts the performance level to Lower Cost (0 VPUs/GB) for both block volumes and boot volumes. When the volume is reattached, the performance is adjusted back to the performance level specified by the default VPUs/GB setting. If performance based dynamic scaling with autotuning is also enabled, it will take effect at this point to further dynamically scale performance as needed by workloads that use the volume.

When viewing the Block Volume Details or Boot Volume Details pages in the Console, the applicable fields are:
- 

Default Performance : When Performance Based Auto-tune is disabled, this is the volume's performance level that you specify when you create the volume or when you change the performance setting for an existing volume. When the volume is attached, regardless of whether Detached Volume Auto-tune is enabled or not, this is the volume's performance.
- 

Auto-tuned Performance : This is the volume's effective performance. If Detached Volume Auto-tune is enabled for the volume, Auto-tuned Performance will be adjusted to Lower Cost when the volume is detached. Note that Auto-tuned Performance won't show the performance setting as Lower Cost until the performance adjustment is complete.
- 

Detached Volume Auto-tune : This field indicates whether Detached Volume Auto-tune is enabled for the volume. When it is off, the volume's effective performance is always the same as what is specified for Default Performance . When it is on, the volume performance is adjusted to Lower Cost when the volume is detached.

For details about when these settings take effect, see[Timing Limits and Considerations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detached-perf.htm#timing).

## Timing Limits and Considerations

The following list identifies some timing considerations you should be aware of when using the detached volume autotuning feature.
- 

When you enable Detached Volume Auto-tune for a detached volume, the Block Volume service starts the performance adjustment to Lower Cost after 14 days.
- 

When you enable Detached Volume Auto-tune for an attached volume, the Block Volume service starts the performance adjustment to Lower Cost 14 days after you detach the volume.
- 

If you disable Detached Volume Auto-tune while a volume is detached, Block Volume service starts the performance adjustment to the Default Performance setting right away.
- 

If you change the Default Performance for a detached volume with Detached Volume Auto-tune enabled, the Auto-tuned Performance for the volume will remain Lower Cost until you reattach the volume.
- 

If you clone a detached volume with Detached Volume Auto-tune enabled, the Block Volume service starts the performance adjustment to Lower Cost after 14 days.
- 
To optimize performance for a volume configured for Ultra High Performance , the volume attachment needs to be enabled for multipath. When you reattach a volume that has had the detached volume autotuned to Lower Cost , but the volume is configured for Ultra High Performance , you need to confirm that the attachment is multipath-enabled after the volume is reattached. For more information, see:
- [Attaching Ultra High Performance Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-volume-attachment.htm#multipath)
- [Checking If a Volume Attachment is Multipath-Enabled](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-multipath-enable-check-compute-volume-attachment.htm)
- [Supported Compute Shapes for Multipath-Enabled Paravirtualized Attachments](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/configuringmultipathattachments.htm#multipath_shapes_pv)
