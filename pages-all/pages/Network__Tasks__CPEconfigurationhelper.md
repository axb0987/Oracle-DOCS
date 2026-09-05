# Using the CPE Configuration Helper
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm
- Fetched: 2026-09-05 02:42 CDT

# Using the CPE Configuration Helper

This topic describes how to use the CPE configuration helper to generate content that a network engineer can use to configure a CPE.

After you set up Site-to-Site VPN in OCI, a network engineer must configure the customer-premises equipment (CPE) at the on-premises end of the connection (often a router or firewall). The configuration uses details about the virtual cloud network (VCN) and the IPSec tunnels in the Site-to-Site VPN. This topic describes how to use the CPE configuration helper in the Oracle Console to generate the information that a network engineer uses to configure the CPE. Notice that the CPE configuration helper is also referred to as the helper .

## Overview of the Helper

For the IPSec tunnels in a Site-to-Site VPN to work, a network engineer must configure the on-premises CPE with specific information about the connection. The information comes from different sources. Oracle provides some of it in several places within the Oracle Console. The helper collects the necessary information into one place and then organizes it to make on-premises CPE configuration easier for the network engineer. You can copy or download the resulting content to a file.

The configuration information that the network engineer needs depends on which vendor makes the CPE. To ensure that the helper can produce vendor-specific content, you must specify which vendor makes the CPE.

Sometimes, the helper might ask for information about the on-premises network and include it in the content. If you don't know the answers, you can leave them blank. The resulting content then uses placeholder variables to show where the network engineer needs to provide the answers.

The helper produces content including these items:
- The Oracle VPN headend for the tunnel (the IP address at the Oracle end)
- The shared secret (pre-shared key) for the tunnel
- The VCN's CIDR
- Support for the[IPSec over FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/fastconnectsecurity.htm#ipsec)feature
- BGP information (if you're using BGP dynamic routing for the tunnel)
- The IPSec parameters that Oracle supports
- Other relevant information

## Working with the Helper

[Specify the CPE vendor](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm#)

If you didn't already select a vendor for the CPE when you[created the CPE object](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-create.htm), before you try to use the helper[edit the CPE](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-update.htm)and select the vendor. If you're not sure which vendor makes the CPE, or it's not in the list, select Other .

If prompted, select a value for Platform/Version . Use these guidelines:
- We recommend using a route-based configuration if possible.
- If you don't see a specific CPE platform or version in the list, select the closest platform/version that predates the CPE version.

[Open the Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm#)

You can access the helper from different locations in the Oracle Console. Where you access the helper controls the scope of the content it produces:
- See[Getting IPSec Connection Details](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-get.htm). From an IPSec connection's details page, the helper produces content for one individual IPSec connection (all tunnels within the connection).
- See[Getting an IPSec Tunnel's Details](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-tunnel_get.htm). From an IPSec tunnel's details page, the helper produces content for only that one tunnel in an IPSec connection.

[Generate the Content](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm#)

The helper has a Create Content button at the bottom. After you create the necessary content it and the content is produced, use the buttons to copy or download the content to a file. Give the content to the on-premises network engineer, along with the link to the configuration topic for the CPE type (see[Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/CPElist.htm)). You can return to the helper at any time and again generate the configuration content.

Instructions: See[Get CPE Device Configuration Information](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-get_device_config_content.htm).

### If You Update Site-to-Site VPN

When you change aspects of Site-to-Site VPN, you should generate the helper content again. For example, imagine that you have an IPSec connection that uses static routing, and you decide to change it to use BGP dynamic routing. After updating the Oracle Console with the new routing information, you can generate the helper content again for the IPSec connection. You can then give that new content to the network engineer to update the CPE to match.

To use[IPSec over FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/fastconnectsecurity.htm#ipsec)you can't update a CPE object to add that functionality, the support must be established at the CPE's initial setup. You also can't have the IPSec tunnels and virtual circuits for this connection use the same DRG route tables.

### Related Topics
- [Site-to-Site VPN Overview](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm)
- [Site-to-Site VPN Wizard](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartIPsec.htm)
- [Setting Up Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm)
- [Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/supportedIPsecparams.htm)
- [CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm)
- [Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/CPElist.htm)
- [Working with Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm)
- [Site-to-Site VPN FAQ](https://www.oracle.com/cloud/networking/site-to-site-vpn/faq/)
- [Creating a CPE](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-create.htm)
- [Updating a CPE](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-update.htm)
- [IPSec over FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/fastconnectsecurity.htm#ipsec)
