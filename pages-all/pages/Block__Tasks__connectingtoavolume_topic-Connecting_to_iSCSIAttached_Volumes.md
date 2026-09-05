# Connecting to iSCSI-Attached Block Volumes
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/connectingtoavolume_topic-Connecting_to_iSCSIAttached_Volumes.htm
- Fetched: 2026-09-05 01:45 CDT

# Connecting to iSCSI-Attached Block Volumes

Connect to an iSCSI-attached block volume.

Connecting to an iSCSI-attached volume doesn't require a specific IAM policy. However, you might need permission to run the necessary commands on the attached instance's guest OS. Contact your system administrator for more information.

## Prerequisites

You must attach the volume to the instance before you can connect the volume to the instance's guest OS. For details, see[Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-volume-attachment.htm).

To connect the volume, you need the following information:
- iSCSI IP address
- iSCSI port numbers
- CHAP credentials (if you enabled CHAP)
- IQN

The Console provides the commands required to configure, authenticate, and log on to iSCSI.

## Connecting to a Volume on a Linux Instance

- 

Use the Console to obtain the iSCSI data that you need to connect the volume:
- Open the navigation menu and select Compute . Under Compute , select Instances .
- Under List scope , select the compartment that contains the instance.
- Select the name of the instance to display the instance details.
- 

Under Resources , select Attached block volumes to view the attached block volume.
- 

Select the Actions menu (three dots) next to the volume that you're interested in, and then select iSCSI Commands and Information .

The iSCSI Commands and Information dialog box displays specific identifying information about the volume and the iSCSI commands you need. The commands are ready to use with the appropriate information included. You can copy the commands and paste them into your instance session window for each of the following steps.
- Log in to the instance's guest OS.
- 

Register the volume with the`iscsiadm`tool.

```

```

A successful registration response resembles the following example:
```

```

- 

Configure iSCSI to automatically connect to the authenticated block volumes after a reboot:

```

```

Note: All command arguments are essential. Success returns no response.
- 

If you enabled CHAP when you attached the volume, authenticate the iSCSI connection by providing the volume's CHAP credentials as follows:

```

```

```

```

```

```

Success returns no response.
- 

Log in to iSCSI:

```

```

A successful login response resembles the following example:
```

```

- 

You can now format (if needed) and mount the volume. To get a list of mountable iSCSI devices on the instance, run the following command:

```

```

The connected volume listing resembles the following example:
```

```

Tip  
  

If you have multiple volumes that don't have CHAP enabled, you can log in to them all at once by using the following commands:

```

```

## Connecting to a Volume on a Windows Instance

Caution  
  
When you're connecting to a Windows boot volume as a data volume from a second instance, you need to append`-IsMultipathEnabled $True`to the`Connect-IscsiTarget`command. See[Attaching a Windows boot volume as a data volume to another instance fails](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../known-issues.htm#attach-win).
- 

Use the Console to obtain the iSCSI data that you need to connect the volume:
- Open the navigation menu and select Compute . Under Compute , select Instances .
- Under List scope , select the compartment that contains the instance.
- Select the name of the instance to display the instance details.
- Under Resources , select Attached block volumes to view the attached block volume.
- 

Select the Actions menu (three dots) next to the volume that you're interested in, and then select iSCSI Commands and Information .

The iSCSI Commands and Information dialog box displays the volume's IP address and port, which you need to know later in this procedure.
- Log in to the instance by using a Remote Desktop client.
- 

On the Windows instance, open the iSCSI Initiator. The steps to open the iSCSI Initiator vary depending on the version of Windows.

For example: Open Server Manager , select Tools , and then select iSCSI Initiator .
- In the iSCSI Initiator Properties dialog box, select the Discovery tab, and then select Discover Portal .
- Enter the block volume IP address and port , and then select OK .
- Select the Targets tab.
- Under Discovered targets , select the volume IQN.
- Select Connect .
- Ensure that the Add this connection to the list of favorite targets check box is selected, and then select OK .
- 

You can now format (if needed) and mount the volume. To view a list of mountable iSCSI devices on your instance, in Server Manager , select File and Storage Services , and then select Disks .
