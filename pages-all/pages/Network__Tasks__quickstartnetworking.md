# Virtual Networking Wizards
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartnetworking.htm
- Fetched: 2026-09-05 02:46 CDT

# Virtual Networking Wizards

To make it easier to set up a Virtual Cloud Network (VCN) and connect to it, the Console has the following wizards that walk you through network setup.

## Create a VCN with Internet Connectivity

What this wizard does:
- Checks for resource availability. To create any new resource the service limit for that resource must not already have been reached. After the service limit for a resource type has been reached, you can either remove unused resources of that type or[request a service limit increase](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm).
- Creates a[VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNs.htm). This wizard can support the creation of a VCN with IPv6 addresses. For more information, see[IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/ipv6.htm).
- Creates an[internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm),[NAT gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/NATgateway.htm), and[service gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm)for the VCN.
- Creates a regional public subnet with routing to the internet gateway. Instances in a public subnet might optionally have public IP addresses.
- Creates a regional private subnet with routing to the NAT gateway and service gateway (and therefore the Oracle Services Network). Instances in a private subnet can't have public IP addresses.
- Sets up basic security list rules for the two subnets, including SSH access.

This wizard supports the creation of a VCN with IPv6 addresses. IPv6 addressing is supported for all commercial and government regions. For more information, see[IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/ipv6.htm).

To access this wizard from the Networking Overview page:
- Open the navigation menu, select Networking , and then select Overview .
- In the Create a VCN with internet connectivity section, select Start VCN wizard .

To access this wizard from the Virtual cloud networks list page:
- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- On the Virtual cloud networks list page, perform one of the following actions depending on the option that you see:
- Select the Actions button, and then select Start VCN Wizard .
- Select Start VCN Wizard .
- Select Create VCN with Internet Connectivity , and then select Start VCN Wizard .

## Add Internet Connectivity and Site-to-Site VPN to a VCN

What this wizard does:
- Checks for resource availability. To create any new resource the service limit for that resource must not already have been reached. After the service limit for a resource type has been reached, you can either remove unused resources of that type or[request a service limit increase](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm).
- Creates an[internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm)for the VCN.
- Creates a regional public subnet with access to the internet gateway. Instances in a public subnet can optionally have public IP addresses.
- Sets up basic security list rules for the subnet, including SSH access.
- Sets up all the Networking service resources required for a[Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm)between the VCN and an on-premises network. The wizard can optionally have the IPSec encrypted traffic use an existing FastConnect link between the VCN and an on-premises network. See[IPSec over FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/fastconnectsecurity.htm#ipsec)for details.
Note  
  
For the IPSec connection to work, a network engineer must also configure the customer-premises equipment (CPE) in the edge network.

For more information about this wizard see[Site-to-Site VPN Wizard](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartIPsec.htm).

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
-
