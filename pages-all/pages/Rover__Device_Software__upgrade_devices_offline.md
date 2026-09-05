# Upgrading the Roving Edge Device Software while Disconnected
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/upgrade_devices_offline.htm
- Fetched: 2026-09-05 02:59 CDT

# Upgrading the Roving Edge Device Software while Disconnected

Learn how to upgrade the Roving Edge device software while the device isn't connected to your Oracle Cloud Infrastructure (OCI) tenancy.
Note  
  
The ability to upgrade device software while the device is disconnected was introduced in Roving Edge software version 2.6. If your device is running an earlier version (2.5 or earlier), you must[update the device software while connected](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/software_update.htm#update-node-software-connected). To find your device software version, see[Identifying the Device Software Version](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/identifying_the_device_software_version.htm#identifying_the_device_software_version).

The disconnected upgrade process consists of several tasks:
- Get the device's current software version.
- In OCI, request a system upgrade bundle.
- Transfer the upgrade bundle to a bucket on the Roving Edge device.
- On the device, import the upgrade bundle.
- Upgrade the device.

The steps for each task are described in this section.

You must have the required permissions to perform a software upgrade on a disconnected Roving Edge Infrastructure device. See[Enabling Disconnected Upgrade Bundle Delivery (Optional)](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/../Getting_Started/setting_policies.htm#enabling-disconnected-upgrade).
Note  
  

System upgrade bundles can be very large. They can take a long time to download and upload. Plan accordingly.

After the upgrade, the device reboots, and you must use the serial console to unlock the device. To prepare to use the serial console, see[Operating the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/../Getting_Started/setting_up_devices.htm#OperatingSerialConsole).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/upgrade_devices_offline.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/upgrade_devices_offline.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/upgrade_devices_offline.htm#)
- 

Task 1 – Get the Device's Current Software Version
- 

Sign in to the Device Console of the Roving Edge device you plan to upgrade.
- 

Select the System Status icon ( ) in the upper right corner of the Device Console.

System Upgrades displays your current software version.
- 

Record the current system software version. You use it later in the upgrade process. Task 2 – Request a System Upgrade Bundle
- 

In the Oracle Cloud Console, open the navigation menu, select Hybrid , then select Nodes .
- 

If needed, change the compartment to find the resource you want.
- 

Select the device node that you plan to upgrade.

The Node Details page is displayed.

The device node must be in the Customer Received or Customer Deployed state to request a system upgrade bundle.
- 

Select the System upgrades tab.
- 

Select Request system upgrade bundle .

The Request Node Upgrade Bundle dialog box is displayed.
- 

Enter the required information:
- 

Enter the device node's current software version in the Current Software Version box and select Get Next Upgrade Version .

The version number you enter is compared with the available upgrade bundles to see which is the appropriate match. The best match is displayed in the Compatible Upgrade Version box. Sometimes, you might need to perform an interim system software upgrade before you can perform the upgrade you want. The Compatible Upgrade Version box ensures you follow the required upgrade order.
- 

Select a bucket from the Destination Bucket list. The bucket you select receives the system bundle you're requesting. Select Change Compartment to select a destination bucket residing in a different compartment.
- 

Select Request System Upgrade Bundle .

The System Upgrade Bundle Requests list shows the transfer progress for the bundle to the specified destination bucket.

After the transfer is complete, the upgrade bundle file is stored in the Object Storage bucket, and remains there until you delete it.
- 

(Optional) In the Actions menu ( ), select View Details to show more information in the system upgrade bundle request. Upgrade bundle request work requests remain listed for 48 hours. Task 3 – Transfer the Upgrade Bundle to the Device.
- (While still signed in to the Oracle Cloud Console) After the upgrade bundle transfer is complete, select the Destination bucket name to view the file in the Object Storage bucket.
- 

Next to the upgrade bundle file, select the Actions menu (Actions menu ( )), and select Download .

The Download Object dialog box is displayed while the object is downloading, and shows the download status.
- 

Copy the downloaded bundle to a computer that you can connect to the same network as the Roving Edge Infrastructure device.
- 

Upload the upgrade bundle to the`rover-system-upgrade-staging`bucket in Roving Edge Object Storage. See[Uploading an Object to an Object Storage Bucket on a Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/../Object_Storage/Object/put_object.htm#top). Task 4 – On the Device, Import the Upgrade Bundle
- 

Sign in to the Device Console of the Roving Edge device you plan to upgrade.
- 

In the navigation menu, select Node Management , then select Offline System Upgrades .

Previous upgrade bundles are listed. If this is the first upgrade bundle request, the list is empty.
- 

Select Import Bundle .

The Import Bundle Requests panel is displayed.
- 

Under Object Name, select the upgrade bundle from the drop-down menu.
- 

Select Import Bundle .

The upgrade bundle is imported to the device and placed in an Object Storage bucket named`rover-system-upgrade-staging`. When the import is finished, the imported bundle state changes to Imported , and you can proceed to upgrade the device. Task 5 – Upgrade the Device
- 

(While still signed in to the Device Console) Ensure that the upgrade bundle import is finished. Select the System Status icon ( ) in the upper right corner of the Device Console.

The System Upgrades dialog box displays the status of the various stages of the import process. When the import is complete, the dialog box displays the device's current system software version and the new imported version.
- 

In the navigation menu, select Node Management &gt; Nodes .
- 

On the device node line, select the Actions menu ( ), and select Upgrade .
- 

Confirm the upgrade request.

The System Upgrades dialog box indicates when the upgrade is complete.

The device is automatically rebooted at the end of the upgrade process. You must unlock the rebooted device using the serial console. See[Operating the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/../Getting_Started/setting_up_devices.htm#OperatingSerialConsole).
- 

You can use the CLI to perform upgrade preparation tasks, but you can't use the CLI to perform the upgrade. Use the Device Console to upgrade the device.

#### Upgrade Preparation CLI Commands
Note  
  

The following commands are run on your OCI tenancy. Ensure that you use a CLI profile configured to reach the OCI tenancy.
- 

Get the compatible upgrade version : Run the[oci rover node rover-bundle-version get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/rover/node/rover-bundle-version/get.html)command and required parameters to get the compatible upgrade version for a Roving Edge Infrastructure device:
```

```

- 

Request a system upgrade bundle : Run the[oci rover node rover-bundle copy-to-customer](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/rover/node/rover-bundle/copy-to-customer.html)command and required parameters to request a system upgrade bundle for a Roving Edge Infrastructure device.
```

```

- 

List upgrade bundle requests : Run the[oci rover node rover-bundle-request list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/rover/node/rover-bundle-request/list.html)command and required parameters to list the upgrade bundle requests for a Roving Edge Infrastructure device:
```

```

- 

View the transfer progress for an upgrade request : Run the[oci rover node rover-bundle get-status](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/rover/node/rover-bundle/get-status.html)command and required parameters to view the transfer progress for an upgrade request for a Roving Edge Infrastructure device:
```

```

Note  
  

The following commands are run on the Roving Edge Device. Ensure that you use a CLI profile configured to reach the device (not your OCI tenancy).
- 

Upload the system bundle to the device on an Object Storage bucket named`rover-system-upgrade-staging`: Run the[oci rover device system-upgrade upload-bundle](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/rover/device/system-upgrade/upload-bundle.html)command and required parameters.
```

```

- 

Import the upgrade bundle to an Object Storage bucket on the device: Run the[oci rover device system-upgrade import-bundle](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/rover/device/system-upgrade/import-bundle.html)command.
```

```

where`object_name`is the name of the upgrade bundle object. For example:`2.5.3.20230808163434.rover_disconnected_release.tar`.
- 

View all import tasks: Run the[oci rover device system-upgrade get-import-history](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/rover/device/system-upgrade/get-import-history.html)command.
```

```

- 

View a specific task: Run the[oci rover device system-upgrade get-import-status](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/rover/device/system-upgrade/get-import-status.html)command.
```

```

After the import status indicates`COMPLETED`, you can proceed with the normal system software upgrade using the Device Console.
-
