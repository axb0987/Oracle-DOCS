# Managing Ethernet Bonding
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/managing_network_bonding.htm
- Fetched: 2026-09-05 02:59 CDT

# Managing Ethernet Bonding

Ethernet bonding enables the use of multiple NICs to connect to your network, providing resiliency and higher throughput. Ethernet bonding works in 802.3ad mode, using layer2+3 hashing for traffic, so it's fully compatible with switch aggregation using LACP.

For Roving Edge devices, Ethernet bonding is managed using the device serial console. For information about accessing the serial console, see[Cable the Roving Edge Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Setup-RED/cable-device.htm#install-the-device)and[Set Up Terminal Emulation](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Setup-RED/setting-up-terminal-emulation.htm#setting-up-terminal-emulation). For information about the serial console menu options, see[Operating the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_up_devices.htm#OperatingSerialConsole).

You can perform the following tasks when the device is locked or unlocked.

## Displaying the Ethernet Bonding Status

In the following steps, select serial console menus by entering the menu number and pressing Return.
- In the serial console main menu, select Configure the Network .
- 

Select Configure Ethernet Bonding .

The Linux Ethernet Bonding options are displayed.
- 

Select Display Ethernet Bonding Status.

The Ethernet bonding information is displayed.

## Enabling Ethernet Bonding
Note  
  
Before you enable Ethernet bonding, perform these tasks:
- Connect Ethernet cables from your data center switch to the Ethernet bonding ports. See[Identify Front and Rear Panel Items](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Setup-RED/rear_panel_identification.htm#rear_panel_identification).
- Configure your data center switch to use aggregation/LACP in passive/active mode, and not forced on/off.
- In the serial console main menu, select Configure the Network .
- 

Select Configure Ethernet Bonding .

The Linux Ethernet Bonding options are displayed.
- 

Select Enable Ethernet Bonding .

If the device is unlocked, enabling bonding takes a few minutes to complete.

When complete, the list of interfaces that were added is displayed.

## Disabling Ethernet Bonding

When you disable Ethernet bonding on the device, also disable LACP aggregation in your data center switch.
- In the serial console main menu, select Configure the Network .
- 

Select Configure Ethernet Bonding .

The Linux Ethernet Bonding options are displayed.
- 

Select Disable Ethernet Bonding .

If the device is unlocked, enabling bonding takes a few minutes to complete.
