# IPSec Connection Management
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ipsec-manage.htm
- Fetched: 2026-09-05 02:45 CDT

# IPSec Connection Management

Learn how to manage Site-to-Site VPN IPSec connections in Oracle Cloud Infrastructure.

Site-to-Site VPN uses several resources to create network communication between Compute instances in OCI and an on-premises network, including an IPSec connection and a CPE. In general, to use an IPSec connection, you must complete these minimal steps:
- Create a VCN with one or more subnets.
- Create a DRG.
- Attach the DRG to one or more VCNs. You can also attach a DRG to an on-premises network using FastConnect virtual circuits and Site-to-Site VPN IPSec tunnels.
- Create or update route tables and security lists in the VCN and DRG to allow traffic to flow from OCI to an on-premises network.
- Create an IPSec connection.
- Use the CPE Configuration Helper to generate configuration content that the on-premises network engineer can use to configure the CPE device.
- Have the network engineer configure the CPE device.

Before you create an IPSec connection, review[Setting Up Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm)and plan the Site-to-Site VPN implementation. Also, review[Working with Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm).

The following tasks are available for an IPSec connection and the IPSec tunnels it contains:
- [Listing IPSec Connections](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-list.htm)
- [Creating an IPSec Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-create.htm)
- [Getting IPSec Connection Details](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-get.htm)
- [Updating an IPSec Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-update.htm)
- [Moving an IPSec Connection Between Compartments](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-change_compartment.htm)
- [Deleting an IPSec Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-delete.htm)
- [Listing IPSec Tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-tunnel_list.htm)
- [Getting an IPSec Tunnel's Details](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-tunnel_get.htm)
- [Updating an IPSec Tunnel](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-tunnel_update.htm)
