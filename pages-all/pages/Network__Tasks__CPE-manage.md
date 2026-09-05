# CPE Object Management
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPE-manage.htm
- Fetched: 2026-09-05 02:42 CDT

# CPE Object Management

Learn how to manage a CPE object in Oracle Cloud Infrastructure.

In general, to use a CPE object, you must complete these minimal steps:
- Create a VCN with one or more subnets.
- Create a DRG.
- Attach the DRG to one or more VCNs. You can also attach a DRG to an on-premises network using FastConnect virtual circuits and Site-to-Site VPN IPSec tunnels.
- Create or update route tables and security lists in the VCN and DRG to allow traffic to flow from OCI to an on-premises network.
- Create an IPSec connection.
- Use the CPE Configuration Helper to generate configuration content that the on-premises network engineer can use to configure the CPE device.
- Have the network engineer configure the CPE device.

Before you create a CPE object, review[Setting Up Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm)and plan the Site-to-Site VPN implementation. Also, review[Working with Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm).

The following tasks are available for a CPE:
- [Listing CPEs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-list.htm)
- [Creating a CPE](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-create.htm)
- [Getting a CPE's Details](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-get.htm)
- [Updating a CPE](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-update.htm)
- [Moving a CPE to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-change_compartment.htm)
- [Deleting a CPE](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-delete.htm)
