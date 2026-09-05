# Identify Front and Rear Panel Items
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/rear_panel_identification.htm
- Fetched: 2026-09-05 03:02 CDT

# Identify Front and Rear Panel Items

Use one of the following illustrations to familiarize yourself with the Roving Edge connectors.
- [Roving Edge Device 2 – Rear Panel](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/rear_panel_identification.htm#rear_panel_identification__red2-rearpanel)
- [Roving Edge Device 2 – Front Panel](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/rear_panel_identification.htm#rear_panel_identification__red2-front-panel)
- [Roving Edge Ultra – Front Panel](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/rear_panel_identification.htm#rear_panel_identification__ultra-front-panel)
- [Roving Edge Device 1 – Rear Panel](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/rear_panel_identification.htm#rear_panel_identification__red1-rear-panel)
Note  
  

To meet MIL-STD-461 Rev G RE102 requirements, all Ethernet network cables attached to the Roving Edge Device must be CAT8 rated. Otherwise, the minimum requirement for Ethernet cables is CAT6.

## Roving Edge Device 2 – Rear Panel

No. Description
1

PCIe 0: 1 Quad port 10GBASE-T Ethernet card with RJ-45 port assignments from left to right: 3, 2, 1, 0

For all shapes, use the following ports:
- Port 0 (rightmost port) – Connect this port to your data center network. See[Cable the Roving Edge Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/cable-device.htm#install-the-device).
- Ports 1 and 2 – Can optionally be used for Ethernet bonding with port 0. See[Managing Ethernet Bonding](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/../Getting_Started/managing_network_bonding.htm#managing_network_bonding)
- Port 3 (leftmost port) – Reserved Ethernet port 3. Don't connect to this port.
2A

[Compute shape](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/../device_specifications.htm#DeviceSpecifications)includes 2 additional Quad port 10GBASE-T Ethernet cards.

All the ports on PCIe 2 and PCIe 3 can optionally be used for Ethernet bonding with PCIe 0 port 0. You can also optionally use PCIe 0 ports 1 and 2 (see Item 1 in this table). See[Managing Ethernet Bonding](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/../Getting_Started/managing_network_bonding.htm#managing_network_bonding).
2B

[GPU shape](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/../device_specifications.htm#DeviceSpecifications)includes 3 NVIDIA AD104GL [L4] GPUs.
2C

[Storage shape](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/../device_specifications.htm#DeviceSpecifications)includes 4 additional 15.38 SSDs.
3 Power receptacle
4

System status LED
- On – Critical event occurred
- Off – Normal
5 Reserved RJ-45 port, for Oracle use only.
6

Two USB 3.0 ports. Top port is reserved for factory troubleshooting use. Bottom port can be connected to USB-enabled instances. For requirements, see[Connecting USB Devices to Instances](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/../usb_device_usage.htm#top).
7 Reset button
8

Power switch and LED
- On – Host is powered on
- Off – Host is powered off
- Amber – Fault See[Power On the Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/power-on-device.htm#unlock-the-device).
9 DB-9 serial console port.

Your initial communication with the device is made through the serial console that's connected to a controlling host computer, such a laptop. See[Cable the Roving Edge Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/cable-device.htm#install-the-device).

What's next?

[Cable the Roving Edge Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/cable-device.htm#install-the-device)

## Roving Edge Device 2 – Front Panel

No. Description
1

Pullout card. The card shows where to get the documentation, and lists the serial and model numbers. View both sides of the card.

## Roving Edge Ultra – Front Panel

No. Description
1 Power switch
2 One removable SSD
3 Status LEDs
4 Two 10 Gb SFP+ Ethernet ports
5 Two 1 Gb copper Ethernet RJ-45 ports
6

Two USB 3.0 ports. Both ports can be connected to USB-enabled instances. For requirements, see[Connecting USB Devices to Instances](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/../usb_device_usage.htm#top).
7 Disabled VGA port
8 NVMe-based VIK+ storage with 512GB capacity
9 Serial console RJ-45 port

What's next?

[Cable the Roving Edge Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/cable-device.htm#install-the-device)

## Roving Edge Device 1 – Rear Panel

No. Description
1 Power override switch
2

Two 100GbE QSFP28 Ethernet ports
3 Power receptacle
4 Power switch
5

Two 10GB RJ45 Ethernet ports.

Use port labeled 4 for connectivity to your network.

Port 3 can optionally be used for Ethernet bonding with port 4. See[Managing Ethernet Bonding](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/../Getting_Started/managing_network_bonding.htm#managing_network_bonding).
6 DB-9 serial console port

What's next?

[Cable the Roving Edge Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/cable-device.htm#install-the-device)
