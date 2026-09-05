# Disconnecting From a Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/disconnectingfromavolume.htm
- Fetched: 2026-09-05 01:46 CDT

# Disconnecting From a Volume

Learn how to disconnect a block volume from an instance when it's no longer needed.

For volumes attached with[iSCSI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#iSCSI)as the volume attachment type you need to disconnect the volume from an instance before you detach the volume. For more information about attachment type options, see[Volume Attachment Types](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#attachtype).

## Required IAM Policy

Disconnecting a volume from an instance does not require a specific IAM policy. Don't confuse this with detaching a volume (see[Detaching a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingavolume.htm)).

## Disconnecting from a Volume on a Linux Instance

Caution  
  
We recommend that you unmount and disconnect the volume from the instance using`iscsiadm`before you detach the volume. Failure to do so may lead to loss of data.
- Log on to your instance's guest OS and unmount the volume.
- 

Run the following command to disconnect the instance from the volume:

```

```

A successful logout response resembles the following:

```

```

- You can now detach the volume without the risk of losing data.

## Disconnecting from a Volume on a Windows Instance

- Use a Remote Desktop client to log on to your Windows instance, and then open Disk Management .
- Right-select the volume you want to disconnect, and then select Offline .
- Open iSCSI Initiator , select the target, and then select Disconnect .
- Confirm the session termination. The status should show as Inactive .
- In iSCSI Initiator , select the Favorite Targets tab, select the target you are disconnecting, and then select Remove .
- Select the Volumes and Devices tab, select the volume from the Volume List , and then select Remove .
-
