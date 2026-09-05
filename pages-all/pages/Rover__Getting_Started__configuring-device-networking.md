# Configuring Device Networking
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/configuring-device-networking.htm
- Fetched: 2026-09-05 02:59 CDT

# Configuring Device Networking

After you have entered your unlock passphrase and have full access to the Roving Edge Infrastructure device, you can configure the networking settings through your controlling host.
- 

Using terminal emulation, select the Configure the Network menu option. The following options appear:
- 

Set Node IP Settings (Current Node Only) : Use to set the node IP address, subnet mask, and default gateway.
- 

Display Settings : Use to show the current network settings.
- 

Set Public IP Pool Range for Compute Instances : Use to set the external IP address pool for Compute instances. IP addresses are being allocated from this pool when an instance is created with public IP address assigned to it. This operation removes current external IP address pool and replaces it with the ranges from the new input.
- 

Display Public IP Pool Status : Use to show the current public IP pool range.
- 

Control Network Ports : Use to enable or disable network ports.
- 

Configure DNS : Use to configure the DNS servers for the current node control plane. Reboot the device for the DNS configurations you make take effect if device is already unlocked.
- 

Configure Subnet Gateway : Use to configure the gateway for a given subnet. The destination can be the default IGW or a private IP Address. You can perform the following tasks:
- 

Show Configuration : Use to show the current subnet gateway configuration. The output shows whether the destination is IGW or a private IP address for each subnet.
- 

Update Configuration : Use to update the current subnet gateway configuration. For example:
```

```

- 

Configure NTP : Use to perform the following NTP configuration tasks:
- 

Display NTP Configuration : Use to configure external NTP servers. For example:
```

```

- 

Update NTP configuration : Use to identify the primary and secondary servers that set up the NTP configuration for the device.
- 

Reset Network : Use to reset the network by erasing all the network configurations such as Node IP, Public pool, DNS, NTP, and Gateway.
- 

Help : Use to display online help for the Network Configuration menu options.
-
