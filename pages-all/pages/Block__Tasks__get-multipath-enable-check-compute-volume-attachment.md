# Checking If a Volume Attachment is Multipath-Enabled
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-multipath-enable-check-compute-volume-attachment.htm
- Fetched: 2026-09-05 01:46 CDT

# Checking If a Volume Attachment is Multipath-Enabled

Learn how to check if a resource attached to a volume is multipath-enabled.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-multipath-enable-check-compute-volume-attachment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-multipath-enable-check-compute-volume-attachment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-multipath-enable-check-compute-volume-attachment.htm#)
- 

Following are possible values for the Multipath column (Block Volume or Compute).
- 

Yes : The volume is configured for the Ultra High Performance level and the volume attachment is multipath-enabled. No further action is required.
- No without a warning icon: The volume isn't configured for the Ultra High Performance level, the volume doesn't need to be multipath-enabled. No further action is required.
- No with a warning icon: The volume is configured for the Ultra High Performance level, but the volume attachment isn't multipath-enabled. To achieve optimal performance, you need to ensure the volume is attached to a supported instance shape, and that the required prerequisites are configured.

To check this value in Block Volume:

- On the Block Volumes list page, select the volume that you want. If you need help finding the list page or the volumes, see[Listing Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/listingvolumes.htm).
- On the details page, select Attached Instances .
- Check the value displayed in the Multipath column.

To check this value in Compute:
- On the Compute Instances list page, select the instance that you want to view. If you need help finding the list page, see[Listing Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/list-instances.htm).
- On the details page, perform one of the following actions depending on the option that you see:
- Select Storage and then scroll down to Attached block volumes .
- Select Attached Block Volumes .
- Check the value displayed in the Multipath column.
- 

Use the[`oci compute volume-attachment get`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/volume-attachment/get.html)command and specify the`--volume-attachment-id`parameter to check the multipath enablement of a volume:

```

```

For example:

```

```

The`is-multipath`property will be`true`for multipath-enabled attachments and`false`for attachments that are not multipath-enabled.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeAttachment/GetVolumeAttachment)GetVolumeAttachment`operation and specify the`volumeAttachmentId`to get information for a volume attachment.

The`is-multipath`property will be`true`for multipath-enabled attachments and`false`
