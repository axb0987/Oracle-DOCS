# Roving Edge Troubleshooting
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/troubleshooting.htm
- Fetched: 2026-09-05 03:03 CDT

# Roving Edge Troubleshooting

Use troubleshooting information to identify and address common issues that can occur while working with Roving Edge Infrastructure.

Troubleshooting sections are grouped under the following categories:
- [General](https://docs.oracle.com/en-us/iaas/Content/Rover/troubleshooting.htm#general)
- [Self-Provisioning](https://docs.oracle.com/en-us/iaas/Content/Rover/troubleshooting.htm#troubleshooting-device-provisioning)
- [System Upgrade](https://docs.oracle.com/en-us/iaas/Content/Rover/troubleshooting.htm#system-upgrade)
- [Networking](https://docs.oracle.com/en-us/iaas/Content/Rover/troubleshooting.htm#networking)
- [Storage](https://docs.oracle.com/en-us/iaas/Content/Rover/troubleshooting.htm#storage)
- [Compute/Instances](https://docs.oracle.com/en-us/iaas/Content/Rover/troubleshooting.htm#compute-instances)
- [Data Synchronization](https://docs.oracle.com/en-us/iaas/Content/Rover/troubleshooting.htm#data-synchronization)

## General

### Getting Oracle Support

If after reviewing and using these troubleshooting tips you still need help, open a service request for your issue. See[Open a Support Ticket](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport_topic-Open_a_support_service_request.htm)for more information.

### Device is locked again

Roving Edge Infrastructure devices require that you unlock them after every reboot and power cycle. If the RED is unexpectedly locked, verify that the power connection is steady, and check if it was recently restarted. Check that the power connection is steady and that the Roving Edge Infrastructure device did not restart.

### No Serial Console Output

If you've connected your controlling host to the Roving Edge device serial port with the supplied cable, but you don't see any output after you power on the device, check these items:
- Ensure that a USB serial port driver is installed on your host OS. See[Set Up Terminal Emulation](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/setting-up-terminal-emulation.htm#setting-up-terminal-emulation).
- Ensure that you're using the recommended terminal emulation software. See[Set Up Terminal Emulation](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/setting-up-terminal-emulation.htm#setting-up-terminal-emulation).

### Device Console URL gives "unavailable" or "not trusted" message

The Device Console communicates with TLS/HTTPS on port 8015 of each Roving Edge Infrastructure device. When your browser displays a security warning indicating the URL is unavailable or is not a trusted URL, ensure that the TLS certificate is installed and trusted on their machine.

If the Device Console's TLS certificate is not installed and trusted on your host computer, add the TLS certificate from the Device Console using the browser to your host computer's keychain/certificate collection and mark it as trusted. In browsers such as Chrome, Edge, and Firefox, the TLS certificate resides in the browser window to the left of the URL. Consult your particular browser's documentation for more information on how to download the certificate.

An "unavailable" or "not trusted" message might also occur if the system is partially down. Examples include when rebooting for a system upgrade or starting for the first time after a power outage. To help diagnose whether the issue is related to the TLS certificate or a system outage, check for a good or bad response to the`https://<host>:12060/v1/tenants/orei`endpoint in the operator's browser or with a tool like CURL. If accessing that endpoint results in a security warning, check that the Roving Edge Infrastructure device's TLS certificate is properly installed and trusted. If the endpoint times out or returns a non-200 response the system might be experiencing a partial outage.

### Browser Security Warning When Accessing the Device Console

The Device Console communicates with TLS/HTTPS on port 8015 of a given device. When the Device Console browser displays a security warning, ensure that the TLS certificate is installed and trusted on your Roving Edge Infrastructure device. If the Device Console's TLS certificate is not installed and trusted on the host computer, add the TLS certificate from the Device Console in the browser to the host computer's keychain/certificate collection. Then mark it as trusted. In browsers such as Chrome, Edge, and Firefox, the TLS certificate resides in the browser window to the left of the URL. Consult your browser documentation for more information on how to download the certificate.

### "Service unknown" when creating policies for "service rover"

If you get the error "Service unknown" when creating policies for "service rover," you might need to create a child tenancy in Oracle Cloud Infrastructure. See[Creating a New Child Tenancy](https://docs.oracle.com/iaas/Content/General/Concepts/organization_management_overview.htm#creating_new_child_tenancy)in the Oracle Cloud Infrastructure documentation for more information on this feature.

### You Can't Unlock the Device

Problem

You enter the unlock passphrase, but the device doesn't unlock.

Possible Causes and Resolutions

The device master key might be shredded due to one of the following reasons:
- Somebody intentionally shredded the key using the`Shred Key`serial console option. See[Shredding the Master Key for Roving Edge Infrastructure Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/shred_master_key.htm#ShredMasterKey).
- Somebody entered the wrong unlock passphrase for the serial console too many times, and the device shredded the key for security reasons.

For self-provisioned devices:

The only way to recover is to run`Recover Key`in the serial console, then enter the recovery key. The recovery key was displayed during the initial configuration of the device.

If you don't know the recovery key, there is no way to unlock and recover the device. You must return the device. See[Returning Roving Edge Infrastructure Devices to Oracle](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/returning_devices.htm#ReturnDevice).

For devices provisioned by Oracle: See[Recovering Your Roving Edge Infrastructure Device After Shredding the Master Key](https://docs.oracle.com/en-us/iaas/Content/Rover/recover_key.htm#recover_key).

## Self-Provisioning

Use the following sections to work through issues that might occur during self-provisioning:
- [Collecting Self-Provisioning Logs](https://docs.oracle.com/en-us/iaas/Content/Rover/troubleshooting.htm#troubleshooting-device-provisioning__collecting-logs)
- [Unable to Register the Device or Complete the Registration](https://docs.oracle.com/en-us/iaas/Content/Rover/troubleshooting.htm#troubleshooting-device-provisioning__register-problems)
- [Invalid Activation Code](https://docs.oracle.com/en-us/iaas/Content/Rover/troubleshooting.htm#troubleshooting-device-provisioning__activation-code)
- [The server TOTP doesn't match client TOTP](https://docs.oracle.com/en-us/iaas/Content/Rover/troubleshooting.htm#troubleshooting-device-provisioning__totp)

### Collecting Self-Provisioning Logs

While using the Roving Edge Basic Configuration Interface in the serial console, as described in[Self-Provision the Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device), you can collect logs that might help diagnose problems.
- From the Roving Edge Basic Configuration Interface main menu, select Advanced Operations .
- 

Select Collect Logs .

The log output is displayed.
- Copy and save the BASE64 output (text between === lines) to a file, then send the file to Oracle support.

### Checking for Roving Edge Basic Configuration Interface Updates

The Roving Edge Basic Configuration Interface is the name of the serial console interface that enables you to self-provision a device. Updating the interface is optional, unless Oracle directs you to do so.
- From the Roving Edge Basic Configuration Interface main menu, select Advanced Operations .
- 

Select Check for Configuration Interface Software Updates .

If an update is available, it's displayed.
- 

If an update is available, select it to upgrade the interface.

### Unable to Register the Device or Complete the Registration

Problem

You get an error when you try to run either of the following commands"
- 
```

```

- 
```

```

Error:
```

```

Possible Causes and Resolutions
- 

Your session token and session private key has either expired or is invalid.

Verify that you're using the correct private key.

Use the OCI CLI to generate a new session token on your laptop.
- 

The Roving Edge device clock is out of sync with the OCI server clock.

Return to the`Configure Networking`menu and run`Check OCI server clock and device`.

### Invalid Activation Code

Problem

You get an error when you run`Register device to OCI`.

Error:
```

```

Possible Causes and Resolutions

The activation code is incorrect. Ensure that the activation code is entered correctly. An Activation code can only be used on the device for which it was issued.

### The server TOTP doesn't match client TOTP

Problem

You get an error when you run`Complete device registration`.

Error:
```

```

Possible Causes and Resolutions

You might not have a required dynamic group or the associated policy isn't configured, or is incorrectly configured in your tenancy.

In your tenancy, ensure that the dynamic group and the policy is configured. See[Allowing Roving Edge Infrastructure Devices to be Self-Provisioned](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_policies.htm#allowing-roving-edge-infrastructure-devices-to-be-provisioned).

### During self-provisioning, you get a RED_RECOVERY_KEY error

During self-provisioning, when you[set up connectivity to OCI](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device__oci-connectivity), you might see the following error:
```

```

The self-provisioning process expects the recovery key secret content to exactly match`RED_RECOVERY_KEY`. If your secret content doesn't match`RED_RECOVERY_KEY`, it's a sign that something isn't configured properly. The self-provisioning process displays the error to prevent accidentally overwriting a recovery key that might be configured for another device. Possible Causes and Resolutions
- 

When you[prepare to self-provision a device](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device__gather-information), ensure that the secret content is set to`RED_RECOVERY_KEY`.

To check the secret content, see[Getting a Secret's Contents](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/concepts_concepts_concepts_secretrules_view_secret_content.htm).
- 

If you need to change the secret content to`RED_RECOVERY_KEY`, see[Creating a Secret Version](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/concepts_concepts_secretrules_create_secret_rule.htm).

Select Secret Type Template as plain-text , secret contents as`RED_RECOVERY_KEY`, and don't select Set to Pending .
- When you[set up connectivity to OCI](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device__oci-connectivity), ensure that you specify the correct secret OCID for the device you're provisioning.

## System Upgrade

### System Upgrade loading icon keeps spinning

The System Upgrade tool persists in its loading state until a timeout occurs, after which it indicates that the system upgrade status cannot be determined. This timeout occurs most often when the REDs are disconnected from the internet. The System Upgrade requires a connection to OCI to determine whether an upgrade for the RED is available.

If your device is disconnected from the internet, you can update your device using the disconnected upgrade process. See[Upgrading the Roving Edge Device Software while Disconnected](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/upgrade_devices_offline.htm#update-device-software-disconnected)for more information.

### System Upgrade bundle download process fails

Check your internet connection and press Download Upgrade to attempt the download. If the download is not successful after multiple attempts, reach out to Oracle support for help.

## Networking

### Data sync, system upgrades, or sanitization operations not working

If you have trouble performing any of the following operations, ensure that the device has connectivity to your OCI Object Storage service.
- [Synchronize data to OCI Object Storage](https://docs.oracle.com/en-us/iaas/Content/Rover/Data_Sync/datasynctask_management.htm#DataSyncTaskManagement)
- [Upgrade the device software while connected to OCI.](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/software_update.htm#update-node-software-connected)
- [Sanitizing a Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/sanitizing-a-device.htm#sanitizing-a-device)

We recommend verifying network connectivity by running a traceroute to the OCI object storage service as follows:
- Identify the Object Storage endpoint for the region that's associated with the device. See[Object Storage Service API endpoints](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/)
- Connect to the serial console. See[Operating the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_up_devices.htm#OperatingSerialConsole).
- In the Roving Edge Device serial console main menu, select Advanced Menu .
- Select Network Management .
- Select Diagnostic Commands (for more information about diagnostic commands, see[Testing Network Connectivity](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/testing-network-connectivity.htm#testing-network-connectivity)).
- Select Traceroute .
- 

When prompted, enter the destination hostname or IP address and optionally, change the default number of hops. After collecting the responses, press ENTER to stop the traceroute.

The following traceroute example shows a valid connection to the us-ashburn-1 Object Storage service:
```

```

If the traceroute is unsuccessful, check the[device network configuration](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/configuring_devices.htm#ConfigureNetworking). See if another device such as a laptop in the same subnet as the device can reach the same destination.

### IP address range for the public IP pool configuration does not get submitted

After typing an IP range and pressing Enter , press Enter again on the blank input line to submit. If more IP ranges are required, press Enter after each range to open another line of input. Submit a blank input line as the last entry to submit everything. To cancel and go back, press Ctrl+C .

### Cannot access public service endpoints (169.254.169.254 at ports 8015, 18336, and so forth)

Ensure that the firewall on the instance does not block the 196.254.0.0/16 address range. It is common for an OCI-exported image to block link-local address range by default. If so, remove the rule that is blocking any connections to 196.254.0.0/16 from the firewall settings. Consult your operating system documentation regarding firewall configuration procedure.

## Storage

### Lack of available storage space causes block volume operations to fail

Lack of available storage space might cause block storage operations to fail. Free up space by deleting resources that are no longer needed, such as Object Storage objects, boot and block volumes, and instances. Regularly check your REDs' available storage to ensure you are not at risk of running out. See[Roving Edge Infrastructure Device Monitoring](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Monitoring/device_monitoring.htm#NodeManagement)for more information.

### Low object storage available capacity triggers warnings and read-only

When the system reaches 80% capacity used, it triggers a Warning status in the Monitoring page. When the system reaches 95% capacity used, it enters read-only mode, and the Monitoring page shows Object Storage status as Degraded or Warning .

Oracle recommends avoiding running intensive writing operations when the system is functioning at 80% capacity used. If you are at or close to 80%, transfer data to the OCI cloud until the system is well below 80% capacity.

If the system exceeds 95% capacity used threshold, it enters read-only mode, and core functionality (including Compute and Object Storage) is limited. All Compute operations, such as custom instances, boot volumes, and block volumes, and all Object Storage operations are suspended. The suspension of the system prevents you from writing to a storage device when durability and redundancy cannot be guaranteed.

If no available storage space remains on the device, you can free more space by deleting resources that are no longer needed, such as objects in Object Storage, boot and block volumes, and instances. If delete requests fail because no storage space remains and the system is in read-only mode, you can activate Safe Mode through the serial console. Safe Mode permits you to make the necessary deletions.

### Avoiding oversubscribing storage problems

Follow best practice recommendations on how to set up or plan Compute, Block Storage, and Object Storage resource consumption to avoid oversubscription problems. Block Storage and Compute do not reserve storage space for volumes in advance. Instead, storage space is consumed when data is written to the volume. For example, if a 100 GB block volume is created, it does not mean that 100 GB is reserved from the total available storage space for this volume. The storage space remains available to all services and can be exhausted before the 100 GB volume is filled with data.

Also, Compute and Block Storage do not validate the specified size of a created volume against the available storage space. This lack of validation can lead to oversubscription when the total size of created volumes exceeds the storage space available on the device. Do not rely on block volume sizes to calculate storage space utilization. Instead, follow the information about storage space usage displayed in the Device Console's Monitoring page.

### Monitoring page shows Object Storage status as "Degraded" or "Warning"

If the storage function within a RED malfunctions or has physical problems, the Monitoring page on the Device Console might show the Warning or Degraded status periodically for the Object Storage service. If this situation occurs, the RED attempts to rebalance its storage and recover declared redundancy level. Eventually it shows a healthy state if RED has available space and is able to recover enough redundant copies on remaining the RED devices being used for storage.

### Image import from Object Storage to Compute is taking a long time

If an image does not appear in the Custom Images list, the import has failed. If the import fails, check the device nodes Details page:
- 

Open the navigation menu and select Node Management &gt; Nodes . The Nodes page appears, displaying the service and feature status of all your Roving Edge Infrastructure devices in tabular format.
- 

Select the node whose status you want to monitor and view its Details page.
- 

Select the Storage tab and review what percentage of the device of storage has been used.

If the Object Storage service is not healthy, the Monitoring page displays Degraded or Warning as the status. If Object Storage is healthy, check the Monitoring page to ensure that enough available space exists. If insufficient space is available, remove any images, objects, instances, and other items to make room for the wanted image.

### Objects with certain version IDs can cause problems
Running a CLI command where the object's version ID starts with a dash ("`-`") and contains the characters`h`or`i`causes the CLI to enter interactive mode. For example:
```

```

If this occurs, you can use one of the following workarounds:
- 

Include the equal sign ("`=`") between the`--version-id`parameter and its value. Do not include any spaces before of after the`=`. For example:
```

```

Only use double-quotes around the value.
- Include the`--from-json`parameter in the command and specify the input in a JSON format. See[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON)for more information.

## Compute/Instances

### Instance creation attempt results in "Out of Capacity" message

Instance capacity is limited by the number of available cores and available memory. Terminate some of the existing instances that are not in use and try again. Stopped instances count toward the resources used.

### Image Import Failure

Large images take a while to import, much longer if other disk-heavy applications or operations are on going. If an import is taking too long and you want to end it, select Terminate from the Import menu. An image import will automatically time out and cancel after four hours.

### Instance launches into Running state, but upon connection looping on some boot messages

Roving Edge Infrastructure only supports`.oci`and`.qcow2`images, with UEFI booting. To check for image-related problems, open the Device Console and go to the Details page of the compute instance. Check whether the image format is`.oci`,`.qcow2`, or another type. Images exported from OCI cloud are usually`.oci`type. Confirm the image and boot type with the provider of the image.

On a Linux machine, use the`qemu-img`utility to see image info using the following command:
```

```

### Can't Access External Resource from an Instance
- 

If the domain name is referencing an external resource, ensure that external DNS resolvers are added to the list of nameservers inside the instance. Consult your operating system documentation regarding DNS configuration procedure.

For example, on some Linux-based systems, nameserver IPs needs to be added to`/etc/resolv.conf`file.
- Ensure that the RED external connectivity settings are correct. See[Administering Devices Through the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_up_devices.htm#AdminDevices)
- Ensure that the instance firewall settings do not block outgoing connections. Consult your operating system documentation regarding firewall configuration procedures.

### Can't Connect to an Instance Using SSH
- 

Ensure that the instance is running. Open the Device Console and check the Details page of the compute instance page to ensure that the instance state is RUNNING . If the instance is not running, enter Start to launch the instance. Wait for state to change to RUNNING .
- 

Ensure that the instance has public IP address assigned. Open the Device Console and go to the Details page of the compute instance. Select the instance name and verify that the instance has public IP assigned by reviewing Public IP Address value under Instance Access section.

If the instance doesn't have a public IP assigned, add one using the following steps:
- 

Open the Details page of the compute instance.
- 

Select Attached VNICs under Resources to display the list of attached VNICs.
- 

Select the primary VNIC.
- 

The Details page for the primary VNIC appears.
- 

Select Edit .

Alternately, select the Actions menu ( ) for the VNIC you want to edit and select Edit .

The Edit VNIC dialog box appears.
- 

Select the Ephemeral Public IP option.
- 

Select Update .
- 

If public IP assignment fails, open the serial console and select Network Configuration to ensure that the RED's public IP address pool is set up and has IPs available.
- 

Ensure that RED external connectivity settings are correct. Open the serial console and select Configuring Devices . Ensure the RED's IP address, network prefix length, and gateway IP address are set up correctly.
- 

Ensure that the instance is reachable through ICMP requests. Run following command:
```

```

where`100.100.1.10`is target instance's public IP address. If the command is successful, the problem might be with instance configuration (SSH service, firewall rules). Consult your operating system documentation regarding SSH and firewall setup for more information.
- 

Ensure that the instance has started correctly. If running the`ping 100.100.1.10`command is not successful, check the instance console history to look for a successful start sequence. See[Console History Capture for Roving Edge Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Console_History/console-history_management.htm#ConsoleHistoryManagement).
- 

Reboot the node using the device's power button or through the serial console.

### Can't Access a Port on an Instance From the External Machine
- 

Ensure that RED external connectivity settings are correct. See[Administering Devices Through the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_up_devices.htm#AdminDevices).
- 

Ensure that instance firewall settings do not block incoming connections. Consult your operating system documentation regarding firewall configuration procedure.
- 

Ensure that the public IP address is accessing the instance, not the private IP address or fully qualified domain name (FQDN). Instance private IP address is visible only inside VCN subnet. Instance FQDN is visible only when the default VCN internal DNS service is being used (169.254.169.254), which is not accessible outside of the VCN network.

### Can't access an instance from another instance
- 

Ensure that the target instance is running. Open the Device Console and check the Details page of the compute instance to ensure that the target instance state is Running .
- 

Ensure that the request-sending instance has its network configuration, such as IP address, network mask, and gateway, set up correctly. Follow the subnet settings guidelines when performing the configuration. Consult your operating system documentation regarding network configuration for more information.

On Linux-based systems, verify the setup using the following command:
```

```

- 

Ensure that the target instance firewall settings do not block incoming connections. Consult your operating system documentation regarding firewall configuration procedure for more information.
- 

Ensure that the request-sending instance firewall settings do not block outgoing connections. Consult your operating system documentation regarding firewall configuration procedure.
- 

If ICMP is not blocked on the target instance, ensure the`ping`command is successful. Run the following command from the request-sending instance shell:
```

```

where`10.0.0.2`is the target instance's private IP.
- 

If the`ping`command result is`No route to host`, ensure that the default route is set to subnet gateway. Consult your operating system documentation regarding default route settings. For example, for Linux-based operating systems, the command might be:

`ip route show default`

with the expected output:

`default via 10.0.0.1 dev eth0`

where`10.0.0.1`is 10.0.0.0/24 subnet's gateway IP address (VCN subnet gateway always uses the first address in the subnet range).

### Can't access another instance by fully qualified domain name

Ensure that the target instance is running. Open the Device Console and check the Details page of the compute instance to ensure that the target instance state is Running . If the target instance is Stopped , restart it. Confirm that the request-sending instance has 169.254.169.254 set as a nameserver. Consult your operating system documentation regarding DNS configuration procedure for any questions.

### Instance launches, but there's no public IP address to connect to using SSH

When creating an instance, select the Assign a public IP address option. Ensure that the public IP pool specified during device setup (using the serial console) has enough addresses for the number of instances (including ones in Stopped state). If not enough addresses exist, terminate some instances to free up addresses, or create more public IPs using the serial console.

### Instance creation goes right to Terminating state

This is likely because of one of the following:
- 

Lack of public IPs : Lack of IPs can occur because of the public IP pool not being set up in the serial console, or is out of IPs for some other undetermined reason. Check that the RED's public IP pool range has been set (if creating an instance with the default option of public IP):
- 

Open the serial console.
- 

Select Configure Networking (option 3).
- 

Select Display Public IP Pool Status (option 4).

If the public IP pool has not been set, go back and select Public IP Pool Range for Compute Instances . Follow the displayed instructions to input public IP ranges. The serial console includes a usage guide for more information.
- 

Full ceph object/block storage : The inability to allocate space for the instance's boot volume can cause the instance to enter the Termination state. Ensure that the object/block storage is not full by checking the top of the Monitoring page in the RED console.
- 

Full CPU usage : There exists a maximum of 32 OCPUs in total across instances, including those OCPUs that are stopped. On the Device Console's Compute page, ensure that the total OCPU count of existing instances is less than the maximum of 32. If all 32 OCPUs are being used, terminate some instances to free up resources.
- 

Full GPU usage : There exists a maximum of one GPU-shape instance, including those GPUs that are stopped. A RED can only have a single GPU-shaped instance provisioned at a time. Attempts to create more GPU-shape instances terminate during provisioning. On the Device Console's Compute page, ensure that there are no instances with GPU shape in Running or Stopped state. If a GPU shaped instance exists, terminate it.
- 

Invalid image : Roving Edge Infrastructure only supports`.oci`and`.qcow2`image formats, with UEFI booting. On the Device Console's Compute page, open the Instances section and determine which instance is terminating. Select the terminating instance to open its Details page, where you can note the image name. The image name and extension indicates whether it is`.oci`or`.qcow2`or another type. Images exported from OCI cloud are usually`.oci`type. Verify the image and boot type with the person who provided the image.

On a Linux machine, use the`qemu-img`utility to see image info using the following command:
```

```

### Slow instance performance or slow terminal usage using SSH

Slow RED performance can result when other instances are experiencing heavy usage, such as those running disk- or network-intensive applications. Resource-heavy device operations, such as importing large object storage contents or compute images, can also degrade performance. If you are working with an intensive application, use an instance shape with higher OCPU count, as they also come with more RAM. Stop or terminate the current instance, then create another instance using the same image, but with the bigger shape.

### Your instance launches into Running state, but the SSH rejects your key, refuses connection, or times out.

If you launch an instance whose state listed as Running , but SSH rejects your key, refuses the connection, or times out, try the following:
- 

Ensure that you are trying to connect to the instance's public IP address using SSH.
- 

Ensure that you are using the private key (not public) as part of the SSH command on your host computer.
- 

Give the instance a minute or longer to fully launch. Providing this time allows the SSH service to load. Then try again to connect.
- 

In rare cases, if the image your uploaded or imported already contains public user SSH keys, the new keys uploaded or copy/pasted as part of the instance creation process might not be included. Take a snapshot of the original image with the wanted keys added, and use that modified image.

### Instance stuck for a long time

Provisioning of certain images and resources, such as boot volumes, GPU, and bigger shapes, can take 10 minutes or more. If a instance has been stuck for a long time, do the following:
- 

Access the Device Console and open the Details page for the instance.
- 

Review the Attached Block Volumes and Attached VNICs sections, and note any resources stuck in Attaching or Detaching state.
- 

If any block volumes or VNICs are seen stuck in attaching/detaching state, check the Monitoring page to see if Block Storage and VCN services are healthy.
- 

If used storage space is nearly full, there might not be enough capacity to provision an instance. Consider terminating other instances, removing block volumes, or both to free up space.
- 

If the public IP pool is used up, provisioning a new instance with public IP (specified by default) isn't doable. Either terminate existing instances to free up IPs, or add public IPs using the serial console.
- 

Review the Monitoring page for any other services are unhealthy.

If the solutions listed in here do not solve the issue, consider terminating the instance.

Stuck instances will be cleared out automatically after a few hours, otherwise they might need to be manually terminated.

## Data Synchronization

### Create Task Fails with Error "Same or Circular Task Exists"

Data Sync tasks are uni-directional and are sensitive to circular references. You cannot set up a bidirectional sync using two tasks and the same object storage buckets used by OCI and the REDs. Ensure that the task you are creating does not attempt to reverse the sync direction of a previously created task. If it does, modify one of the tasks needs to not reverse the direction of the other.

### Tasks are specified, but sync operations do not start

Data Sync requires that you assign a connection for each REDs to an OCI cloud location where you want the data sync operations to occur. Check the[OCI status page](https://ocistatus.oraclecloud.com)to see if OCI services are running. If network or object storage issues occur, resolve these issues before attempting to run or schedule a data sync. Next, see if the local network has connectivity by running`ping`OCI from the host machine to verify connectivity between Roving Edge Infrastructure and OCI. If pinging OCI does not work, verify that no firewall or network rules blocking connectivity exist.

If you create a Data Sync task job for synchronizing a bucket from RED-to-OCI or OCI-to-RED, and its estimated runtime is more than 12 hours, then exactly after 12 hours the Data Sync job fails because the authentication token expires after every 12 hours. If the Data Sync job fails after running more than 12 hours, do the following
- 

Open the navigation menu and select Data Sync .

The Data Sync Tasks page appears. All data sync tasks are listed in tabular form.
- 

Check the data sync task that failed.
- 

Select Start .

Alternately, select the Actions menu ( ) for the data sync task that you checked and select Start
-
