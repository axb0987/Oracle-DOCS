# Known Issues for Block Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/known-issues.htm
- Fetched: 2026-09-05 01:47 CDT

# Known Issues for Block Volume

Known issues have been identified in Block Volume.

See also[Troubleshooting Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/troubleshooting.htm).

## Attaching a Boot Volume Might Fail with an Incorrect Error Suggesting the Compute Instance Needs to be Running
Details

Attaching a boot volume using the[Attaching a Boot Volume procedure](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-boot-volume-attachment.htm)might fail with the following error, suggesting the Compute instance needs to be running.

`API Error Instance ocid1.instance.oc1.ap-tokyo-1.xxxx is in Stopped state, when it was expected to be in Running state`

Block data volumes can be attached to a running Compute instance, but boot volumes can not. Therefore, the error message is incorrect. Workaround

Until the error message is corrected, attach boot volumes to Compute instances from the Compute Console, CLI, and APIs using normal methods. See:
- [Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm)
- [Replacing a Boot Volume](https://docs.oracle.com/iaas/Content/Compute/Tasks/replacingbootvolume.htm)

If you get the preceding error, remember that block data volumes can be attached to a running Compute instance, but boot volumes require that the instance is stopped.

## Paravirtualized volume attachment not multipath-enabled after instance is resized
Details To achieve the optimal performance level for volumes configured for ultra high performance, the volume attachment must be[multpath-enabled](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-multipath-enable-check-compute-volume-attachment.htm). Multipath-enabled attachments to VM instances are only supported for instances based on shapes with 16 or greater OCPUs. If you have an instance with fewer than 16 OCPUs, you can resize it so that it has 16 or more OCPUs to support multipath-enabled attachments. This step doesn't work for instances where the original number of OCPUs was less than 8 and the volume attachment is paravirtualized. In this scenario, after the volume is detached and reattached, the volume attachment still isn't multipath-enabled even though the instance now supports multipath-enabled attachments. Workaround As a workaround, we recommend that you[create a new instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm)based on a[shape](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm)with 16 or more OCPUs, and then attach the volume to the new instance.

## Attaching the maximum number of block volumes to smaller VM.Standard.A1.Flex instances might fail
Details When you attempt to attach the maximum number of block volumes to a smaller`VM.Standard.A1.Flex`instance, the volumes might fail to attach. This failure happens because of limitations with the underlying physical host configuration. Workaround We're working on a resolution. As a workaround, we recommend that you increase the size of the VM by[resizing the VM](https://docs.oracle.com/iaas/Content/Compute/Tasks/resizinginstances.htm), and then try attaching the volumes again.

## Vault encryption keys not copied to destination region for scheduled cross region backup copies
Details When you schedule volume and volume group backups using a backup policy that is enabled for cross-region copy for volumes that are encrypted using Vault service encryption keys, the encryption keys are not copied with the volume backup to the destination region. The volume backup copies in the destination region are instead encrypted using Oracle-provided keys. Workaround We're working on a resolution. As a workaround, you can manually copy volume backups and volume group backups across regions, either manually or using a script, and specify the key management key ID in the target region for the copy operation. For more information about manual cross region copy, see[Copying a Volume Backup Between Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copy-bv-backup.htm).

## Attaching a Windows boot volume as a data volume to another instance fails
Details When you attach a Windows boot volume as a data volume to another instance, when you try to connect to the volume using the steps described in[Connecting to a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/connectingtoavolume.htm)the volume fails to attach and you might see the following error:`Connect-IscsiTarget : The target has already been logged in via an iSCSI session.`Workaround You need to append the following to the`Connect-IscsiTarget`command copied from the Console:

```

```

## bootVolumeSizeInGBs attribute is null
Details When calling[GetInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/GetInstance), the`bootVolumeSizeInGBs`attribute of[InstanceSourceViaImageDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/requests/InstanceSourceViaImageDetails)is null. Workaround We're working on a resolution. To work around this issue, call[GetBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/GetBootVolume), and use the`sizeInGBs`attribute of[BootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume).

## Notification emails for successful backup completion not sent because of change in backup file naming convention
Details After a successful backup, a notification is generated based on the generated file name. As the file naming convention has changed, a notification isn't generated. Workaround If you have set up notifications in this way, change the notification condition to match the new file naming convention.

## Resolved Issues for Block Volume

### Cross-region replication not supported for volumes encrypted with customer-managed keys
Details When you try to enable cross-region replication for a volume configured to use a Vault encryption key, the following error message occurs:`Edit Volume Error: You cannot enable cross-region replication for volume <volume_ID> as it uses a Vault encryption key.`
