# Configure Network Parameters for a Factory Provisioned Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/finish-the-set-up-for-preprovisioned-devices.htm
- Fetched: 2026-09-05 03:02 CDT

# Configure Network Parameters for a Factory Provisioned Device

Some Roving Edge Devices are shipped with software already installed. You complete the setup by performing the procedures in this section.
Note  
  

The procedures in this section only describe how to complete the setup for devices that were provisioned by Oracle. If your device was shipped as a self-provisioned device (software is installed on-site), instead follow the instructions in[Self-Provision the Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/../Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device).

Configure the Roving Edge Device network settings through your controlling host that's connected to the serial port.
Note  
  

For a list of serial console commands, see[Operating the Serial Console](https://docs.oracle.com/iaas/Content/Rover/Getting_Started/setting_up_devices.htm#OperatingSerialConsole)

The following procedure describes how to configure the minimum network parameters that are required during the initial device setup. For more network configuration information, see[Managing Advanced Network Settings](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/../Getting_Started/network_management.htm#ManageNetwork).

The minimum network parameters that you need to configure are as follows:
- Device IP address, subnet, and gateway.
- DNS
- NTP
- 

From the controlling host terminal window, select the Configure the Network menu option. The following options are displayed:
- 

Set Node IP Settings (Current Node Only) : Set the node IP address, subnet mask, and default gateway.
- 

Display Settings : Show the current network settings.
- 

Set Public IP Pool Range for Compute Instances : Set the external IP address pool for compute instances.

IP addresses are allocated from this pool when an instance is created with public IP address assigned to it.

Important – This operation removes the current external IP address pool, and replaces it with the ranges from the new input.

The best practice is to use a contiguous range of IPs. An ideal range is a CIDR range such as 10.10.0.0 - 10.10.0.15, which corresponds to 10.10.0.0/28, which is what is stored internally.

If you're updating your public IP pool range, none of the IPs in the existing range can be allocated to a compute instance during the operation. The best practice is to ensure all public IPs are dissociated with all compute instances before updating your public IP pool range.
- 

Display Public IP Pool Status : Show the current public IP pool range.
- 

Control Network Ports : Enable or disable network ports.
- 

Configure DNS : Configure the DNS servers for the current node control plane. Reboot the device for the DNS configurations to take effect, if the device is already unlocked.
- 

Configure Subnet Gateway : Configure the gateway for a given subnet. The destination can be the default IGW or a private IP Address. You can perform the following tasks:
- 

Show Configuration : Show the current subnet gateway configuration. The output shows whether the destination is IGW or a private IP address for each subnet.
- 

Update Configuration : Update the current subnet gateway configuration. For example:
```

```

- 

Configure NTP : Perform the following NTP configuration tasks:
- 

Display NTP Configuration : Configure external NTP servers. For example:
```

```

- 

Update NTP configuration : Identify the primary and secondary servers that set up the NTP configuration for the device.
- 

Reset Network : Reset the network by erasing all the network configurations such as Node IP, Public pool, DNS, NTP, and Gateway.
- 

Help : Display online help for the Network Configuration menu options.
- 

Go Back : Return to the main serial console menu.
- 

Use the menu options to configure the device network parameters according to your network environment. At minimum, configure these parameters:
- Network settings
- DNS
- NTP
- 

If you need to configure other network parameters like network bonding, see[Configuring the Network](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/../Getting_Started/configuring_devices.htm#ConfigureNetworking).

What's next?

[Unlock the Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/unlock-the-device.htm#unlock-the-device)
