# Securing Networking: VCN, Load Balancers, and DNS
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/networking_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing Networking: VCN, Load Balancers, and DNS

## Security Recommendations

The Networking service has a collection of features for enforcing network access control and securing VCN traffic. These features are listed in the following table.

VCN Feature Security Description
[Public and private subnets](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#connectivity)Your VCN can be partitioned into subnets. Subnets have historically been specific to an availability domain, but can now be regional (covering all availability domains in the region). Instances inside private subnets cannot have public IP addresses. Instances inside public subnets can optionally have public IP addresses at your discretion.
[Security rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm)Security rules provide stateful and stateless firewall capability to control network access to your instances. To implement security rules in your VCN, you can use[network security groups (NSGs)](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm)or[security lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm). For more information, see[Comparison of Security Lists and Network Security Groups](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm#comparison).
Gateways

Gateways let resources in a VCN communicate with destinations outside the VCN. The gateways include:
- [Internet gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIGs.htm): for internet connectivity (for resources with public IP addresses in public subnets)
- [NAT gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/NATgateway.htm): for internet connectivity without exposing the resources to incoming internet connections (for resources in private subnets)
- [Dynamic routing gateway (DRG)](https://docs.oracle.com/iaas/Content/Network/Tasks/managingDRGs.htm): for connectivity to networks outside the VCN's region (for example, your on-premises network by way of a Site-to-Site VPNor FastConnect, or a peered VCN in another region)
- [Service gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm): for private connectivity to Oracle services such as Object Storage
- [Local peering gateway (LPG)](https://docs.oracle.com/iaas/Content/Network/Tasks/localVCNpeering.htm): for connectivity to a peered VCN in the same region
[Route table rules](https://docs.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm)Route tables control how traffic is routed from your VCN's subnets to destinations outside the VCN. Routing targets can be VCN gateways or a private IP address in the VCN.
[IAM polices for virtual-network-family](https://docs.oracle.com/iaas/Content/Network/Concepts/accesscontrol.htm#Policies)IAM policies specify access and actions permitted by IAM groups to resources in a VCN. For example, IAM polices can give administrative privileges to network administrators who manage the VCNs, and scoped-down permissions to normal users.

Oracle recommends that you periodically monitor Oracle Cloud Infrastructure Audit logs to review changes to VCN network security groups, security lists, route table rules, and VCN gateways.

## Network Segmentation: VCN Subnets
- 

Formulate a tiered subnet strategy for the VCN, to control network access. A common design pattern is to have the following subnet tiers:
- DMZ subnet for load balancers
- Public subnet for externally accessible hosts such as NAT instances, intrusion detection (IDS) instances, and web application servers
- Private subnet for internal hosts such as databases

No special routing is required for the instances in the different subnets to communicate. However, you can control the types of traffic between the different tiers by using the VCN's network security groups or security lists.
- Instances in the private subnet only have private IP addresses and can be reached only by other instances in the VCN. Oracle recommends that you place security-sensitive hosts (DB systems, for example) in a private subnet, and use security rules to control the type of connectivity to hosts in a public subnet. In addition to VCN security rules, configure host-based firewalls such as iptables, firewalld for network access control, as a defense-in-depth mechanism.
- You can add a service gateway to your VCN to enable DB systems in the private subnet to directly back up to Object Storage without the traffic traversing the internet. You must set up the routing and security rules to enable that traffic. For more information for bare metal or virtual machine DB systems, see[Configure the Network](https://docs.oracle.com/en/cloud/paas/base-database/vcn-subnets/index.html). For more information for Exadata DB systems, see[Network Setup for Exadata Cloud Service Instances](https://docs.oracle.com/iaas/exadatacloud/exacs/ecs-network-setup.html).

## Network Access Control: VCN Security Rules
- Use your VCN's security rules to restrict network access to instances. A security rule is stateful by default, but can also be configured to be stateless. A common practice is to use stateless rules for high-performance applications. In a case where network traffic matches both stateful and stateless security lists, the stateless rule takes precedence. For more information about configuring VCN security rules, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm).
- To prevent unauthorized access or attacks on Compute instances, Oracle recommends that you use a VCN security rule to allow SSH or RDP access only from authorized CIDR blocks rather than leave them open to the internet (0.0.0.0/0). For additional security, you can temporarily enable SSH (port 22) or RDP (port 3389) access on an as-needed basis using the VCN API`UpdateNetworkSecurityGroupSecurityRules`(if you're using network security groups) or`UpdateSecurityList`(if you're using security lists). For more information about enabling RDP access, see[To enable RDP access](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm#prerequisites__enablerdp)in[Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm). For performing instance health checks, Oracle recommends that you configure VCN security rules to allow ICMP pings. For more information, see[Rules to Enable Ping](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm#ping).
- [Bastions](https://docs.oracle.com/iaas/Content/Bastion/Concepts/bastionoverview.htm)are logical entities that provide secured, public access to target resources in the cloud that you cannot otherwise reach from the internet. Bastions reside in a public subnet and establish the network infrastructure needed to connect a user to a target resource in a private subnet.
- VCN network security groups (NSGs) and security lists enable security-critical network access control to compute instances, and it is important to prevent any unintended or unauthorized changes to NSGs and security lists. To prevent unauthorized changes, Oracle recommends that you use IAM policies to allow only network administrators to make NSG and security list changes.

## Secure Connectivity: VCN Gateways and FastConnect Peering
- VCN gateways provide external connectivity (internet, on-premises, or peered VCN) to VCN hosts. See the table earlier in this topic for a list of the type of gateways. Oracle recommends that you use an IAM policy to allow only network administrators to create or modify VCN gateways.
- 

Carefully consider allowing internet access to any instances. For example, you don't want to accidentally allow internet access to sensitive database instances. In order for an instance in a VCN to be publicly accessible from the internet , you must configure the following VCN options:
- The instance must be in a VCN public subnet.
- The VCN containing the instance must have an internet gateway enabled and configured to be the routing target for outbound traffic.
- The instance must have a public IP address assigned to it.
- The VCN security list for the instance's subnet must be configured to allow inbound traffic from`0.0.0.0/0`. Or if you're using network security groups (NSG), the instance must be in an NSG that allows that traffic.
- VPN IPSec provides connectivity between a customer's on-premises network and VCN. You can create two IPSec tunnels for high availability. For more information about creating VPN tunnels to connect VCN DRG to customer CPEs, see[Site-to-Site VPN](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIPsec.htm).
- FastConnect peering allows you to connect your on-premises network to your VCN with a private circuit so that the traffic does not traverse the public internet. You can set up private peering (to connect to private IP addresses), or public peering (to connect to Oracle Cloud Infrastructure public endpoints, such as for Object Storage). For more information about FastConnect peering options, see[FastConnect](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm).

## Virtual Security Appliances in a VCN
- 

The Networking service lets you implement network security functions such as intrusion detection, application-level firewalls, and NAT (although you can instead use a[NAT gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/NATgateway.htm)with your VCN). You can do this by routing all the subnet traffic to a network security host, using route table rules that use a local VCN private IP address as a target. For more information, see[Using a Private IP as a Route Target](https://docs.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm#Route). For high availability, you can assign the gateway security host a secondary private IP address, which you can move to a VNIC on a standby host in case of primary host failure. Full network packet capture or network flow logs can be captured on the NAT instances using tcpdump, and the logs can be uploaded periodically to an Object Storage bucket.
- Virtual security appliances can be run as virtual machines (VMs) on a bring-your-own-hypervisor (BYOH) model on a bare metal instance. Virtual security appliance VMs running on the BYOH bare metal instance each have their own secondary VNIC, giving direct connectivity to other instances and services in the VNIC's VCN. For information about enabling BYOH on a bare metal instance using an open-source KVM hypervisor, see[Bringing Your Own Hypervisor Guest OS](https://docs.oracle.com/iaas/Content/Compute/References/bringyourownimage.htm#hypervisor).
- Virtual security appliances can also be installed on compute virtual machines (VMs) where VMDK or QCOW2 images of security appliances can be imported using the bring your own image (BYOI) feature. However, due to infrastructure dependencies, the BYOI feature might not work for some appliances, in which case the BYOH model would be another option to use. For more information about importing appliance images into Oracle Cloud Infrastructure, see[Bring Your Own Image (BYOI)](https://docs.oracle.com/iaas/Content/Compute/References/bringyourownimage.htm).

## Load Balancers
- Oracle Cloud Infrastructure load balancers enable end-to-end TLS connections between a client's applications and a customer's VCN. The TLS connection can be terminated at an HTTP load balancer, or on a back-end server by using a TCP load balancer. The load balancers use TLS1.2 by default. For information about configuring an HTTPS listener, see[Listeners for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managinglisteners.htm). You can also upload your own TLS certificates. For more information see[SSL Certificates for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingcertificates.htm).
- You can configure network access to load balancers by using VCN network security groups or security lists. This method provides similar functionality to traditional load balancer firewalls. For public load balancers, Oracle recommends that you use a regional public subnet (for example, DMZ subnet) for instantiating the load balancers in a highly available configuration across two different availability domains. You can configure the load balancer firewall rules by setting up the load balancer's network security groups or the subnet's security lists. For more information about creating load balancer security lists, see[Update Load Balancer Security Lists and Allow Internet Traffic to the Listener](https://docs.oracle.com/iaas/Content/GSG/Tasks/loadbalancing.htm#Update). Similarly, you must configure the VCN network security groups or security lists for the backend servers to limit traffic only from the public load balancers. For more information about configuring backend server security lists, see[Update Rules to Limit Traffic to Backend Servers](https://docs.oracle.com/iaas/Content/GSG/Tasks/loadbalancing.htm#Update2).

## DNS Zones and Records

DNS zones and records are critical for accessibility of web properties. Incorrect updates or unauthorized deletions could result in outage of services, accessed through the DNS names. Oracle recommends that you limit IAM users who can modify DNS zones and records.

## DNS Traffic Management Steering Policies

Incorrect updates or unauthorized deletions to DNS traffic management steering policies could result in outage of services due to traffic misdirection or failover failure. Oracle recommends that you limit IAM users who can modify DNS traffic management steering policies.

## Security Policy Examples

### Allow Users to Only View Security Lists

Your network administrators are the personnel who should have the ability to create and manage network security groups and security lists.

However, you may have network users who need to know what security rules are in a particular network security group (NSG) or security list.

The first line in the following example policy allows the NetworkUsers group to view security lists and their contents. This policy does not let the group create, attach, delete, or modify security lists.

The second line lets the NetworkUsers group view the security rules in NSGs, and also view what VNICs and parent resources are in NSGs. The second line does not let the NetworkUsers group change the security rules in NSGs.

```

```

### Prevent Users from Creating External Connection to the Internet

In some cases, you might need to prevent users from creating external internet connectivity to their VCN. In the following example policy, the NetworkUsers group is prevented from creating an internet gateway.

```

```

### Prevent Users from Updating DNS Records and Zones

In the following example policy, the NetworkUsers group is prevented from deleting and updating DNS zones and records

```

```

## Useful CLI Commands

In all the following examples, the environment variables $T, $C and $VCN are set to tenancy OCID, compartment OCID, and VCN OCID, respectively.

### List Open Security Lists in a VCN
```

```

### List Gateways in a VCN
```

```

### List Route Table Rules in a VCN
```

```
