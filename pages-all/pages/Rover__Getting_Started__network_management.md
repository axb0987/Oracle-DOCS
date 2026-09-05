# Managing Advanced Network Settings
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/network_management.htm
- Fetched: 2026-09-05 02:59 CDT

# Managing Advanced Network Settings

You can manage various device network capabilities from the serial console.

For more information about the serial console, see[Operating the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_up_devices.htm#OperatingSerialConsole).
- 

Using terminal emulation, select the Advanced Menu &gt; Network Management menu option. The following options appear:
- 

MACsec Status : Use to show the current status of the network connection over MACsec. If the status isn't OK, the device attempts to repair the MACsec connection by flapping the interface.
- 

Internet Gateway Status : Use to show which internet gateways (IGWs) are active and how the connection from on-premises flows for instances on nodes without an IGW.
- 

VNIC Information Table : Use to show detailed information (IP, DNS Name, Attachment information) about all the VNICs that have been created on the system.
- 

Diagnostic Commands : Use to run diagnostics commands from the serial console to help troubleshoot network connectivity issues. Currently, Roving Edge Infrastructure supports the Ping and Traceroute commands. See[Testing Network Connectivity](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/testing-network-connectivity.htm#testing-network-connectivity).
-
