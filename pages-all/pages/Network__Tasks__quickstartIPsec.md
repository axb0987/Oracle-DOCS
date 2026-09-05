# Site-to-Site VPN Wizard
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartIPsec.htm
- Fetched: 2026-09-05 02:46 CDT

# Site-to-Site VPN Wizard

The Site-to-Site VPN wizard is the quickest way to set up a site-to-site VPN between an on-premises network and a virtual cloud network (VCN) . The wizard is a guided, step-by-step process in the Console that sets up the VPN plus related Networking service components.

Other secure VPN solutions include OpenVPN, a Client VPN solution that can be accessed in the[Oracle Marketplace](https://cloudmarketplace.oracle.com/marketplace/listing/67830324). OpenVPN connects individual devices to a VCN, but not whole sites or networks.

## Purpose of the Wizard

Site-to-Site VPN involves setting up and configuring several Networking service components. The wizard sets up those components for you. In general, the wizard does the following:
- Uses a template with[assumptions](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartIPsec.htm#assumptions)that helps you get started.
- Asks you for some basic network information.
- Sets up the Networking service components for you.
- Lets you generate configuration content for a network engineer to use when configuring a customer-premises equipment (CPE) device.

The wizard is a task within the overall process of setting up Site-to-Site VPN, which is illustrated in the following diagram. The wizard is the shaded box.
[

Notice that the overall process includes work by an on-premises network engineer. That engineer provides information that you, in turn, must supply when running the wizard. The wizard returns information that the network engineer needs when configuring the CPE device. You can use the[CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm)to provide the necessary information to the network engineer.

The following short sections summarize each task.

Task 1: Information to get from the network engineer
- CPE device's public IP address. (The address must be IPv4, but IPv6 traffic is supported)
- CPE vendor. model, and version
- CPE IKE identifier. For more information, see[Overview of Site-to-Site VPN Components](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#components).
- On-premises network routes.
- If you use BGP dynamic routing with the VPN:
- The on-premises network's BGP ASN
- For each of the two IPSec tunnels that are created, the pair of BGP IP addresses (with subnet mask) that you want to use for the inside tunnel interfaces at the ends of each tunnel. For example:
- Tunnel 1: Inside tunnel interface - CPE: 10.0.0.16/31
- Tunnel 1: Inside tunnel interface - Oracle: 10.0.0.17/31
- Tunnel 2: Inside tunnel interface - CPE: 10.0.0.8/31
- Tunnel 2: Inside tunnel interface - Oracle: 10.0.0.9/31

Task 2: Wizard

You walk through the wizard in the Console. For more information, see these sections:
- [Where to Access the Wizard in the Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartIPsec.htm#location)
- [What the Wizard Creates for You](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartIPsec.htm#results)

Task 3: Information to give to the network engineer

You use the[CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm)to generate configuration content that the network engineer can use to configure the CPE.

The content includes these items:
- The Oracle VPN IP address and shared secret for each IPSec tunnel.
- The supported IPSec parameter values.
- Information about the VCN.
- CPE-specific configuration information.

Task 4: CPE configuration

The network engineer takes the information you provide and configures the CPE device.

Task 5: Testing

You and the network engineer test the connection and confirm that traffic is flowing.

## Alternative to the Wizard

If you prefer, you can manually set up Site-to-Site VPN yourself. For step-by-step instructions, see[Setting Up Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm).

## What the Wizard Creates for You

Most Oracle customers who set up Site-to-Site VPN already have a VCN to connect to their on-premises network. In that case, the wizard creates the numbered components in the following diagram. The table describes each component.
[

Number Component Description Can Use Existing One or Create New One?
1 CPE A CPE is a virtual representation of the actual CPE device. This virtual representation contains basic information such as the CPE device's public IP address. Yes, you can either use an existing CPE or the wizard creates a new one.
2 IPSec tunnels

The wizard creates two[IPSec tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm), each with specific configuration information that you must provide to a network engineer.

Note: The wizard uses IKEv1 or IKEv2 for the tunnels. For more information on IKEv2, see[Using IKEv2](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#using_ikev2). No. The wizard automatically creates the tunnels.
3 Dynamic Routing Gateway (DRG) A[DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm)is a virtual representation of the actual router at the Oracle end of the Site-to-Site VPN. Yes.
4 Internet Gateway

If the VCN you select doesn't already have an[Internet Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm), you can let the wizard create one to enable direct connectivity to the internet. Yes, you can either use an existing internet gateway or let the wizard create a new one.
5 Subnet Route table

Destination CIDR Route Target
10.0.0.0/16 DRG
Note  
  
To create any new resource the service limit for that resource must not already have been reached. After the service limit for a resource type has been reached, you can either remove unused resources of that type or[request a service limit increase](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm).

In addition, during the wizard you specify which subnets in the VCN to configure with access to the on-premises network. The wizard updates each subnet's route table and security rules as follows:
- Route rules: The wizard adds one or more rules to route VCN traffic to an on-premises network by way of the DRG. You need to provide one rule per on-premises network route in the wizard. If the VCN has an internet gateway (or if you create one) and a public subnet is selected, the wizard also adds a rule to send remaining traffic (not destined for the on-premises network) to the internet gateway.
- Security list rules: The wizard also adds one or more rules to allow all types of traffic from an on-premises network. You need to provide one rule per on-premises network route in the wizard. If the VCN has an internet gateway (or you create one) and a public subnet is selected, the wizard also adds a rule to allow SSH over port 22 from the internet.

You can edit the rules and add more if you want.

After the wizard completes, you can use the[CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm)to generate configuration content that the on-premises network engineer can use to configure the CPE.

## Where to Access the Wizard in the Console

To access this wizard from the Networking Overview page:
- Open the navigation menu, select Networking , and then select Overview .
- In the Add internet connectivity and Site-to-Site VPN to a VCN section, select Start VCN wizard .

To access this wizard from the Virtual cloud networks list page:
- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- On the Virtual cloud networks list page, perform one of the following actions depending on the option that you see:
- Select the Actions button, and then select Start VCN Wizard .
- Select Start VCN Wizard .
- Select Add Site-to-Site VPN and Internet Connectivity to a VCN , and then select Start VCN Wizard .

To access this wizard from the Site-to-Site VPN list page:
- Open the navigation menu and select Networking . Under Customer connectivity , select Site-to-Site VPN .
- Select Start VPN Wizard .

## Related Topics

- [Site-to-Site VPN Overview](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm)
- [Setting Up Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm)
- [Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/supportedIPsecparams.htm)
- [CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm)
- [Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/CPElist.htm)
- [Using the CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm)
- [Working with Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm)
- [Site-to-Site VPN FAQ](https://www.oracle.com/cloud/networking/site-to-site-vpn/faq/)
