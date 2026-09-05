# Ways to Secure a Network
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/waystosecure.htm
- Fetched: 2026-09-05 02:42 CDT

# Ways to Secure a Network

OCI has several ways you can control security for a cloud network and Compute instances:
- Public and private subnets: You can define a subnet as private, which means instances in the subnet can't have public IP addresses. For more information, see[Public vs. Private Subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Public).
- Security rules: To control packet-level traffic in and out of an instance. You configure security rules in the Oracle Cloud Infrastructure API or Console. To implement security rules, you can use network security groups or security lists. For more information, see[Security Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm).
- Zero Trust Packet Routing: You can use Zero Trust Packet Routing (ZPR) along with or in place of network security groups to manage network access to OCI resources . To do this, define ZPR policies that govern how resources communicate with each other, and then add security attributes to those resources. For more information, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm).
Caution  
  
If an endpoint has a Zero Trust Packet Routing (ZPR) security attribute, traffic to the endpoint must satisfy ZPR policies and also all NSG and security list rules. For example, if you're already using NSGs and you add a security attribute to an endpoint, all traffic to the endpoint is blocked. From then onward, a ZPR policy must explicitly allow traffic to the endpoint.
- Firewall rules: To control packet-level traffic in/out of an instance. You configure firewall rules directly on the instance itself. Notice that platform images that run Oracle Linux automatically include default rules that allow ingress on TCP port 22 for SSH traffic. Also, the Windows images include default rules that allow ingress on TCP port 3389 for Remote Desktop access. For more information, see[Platform Images](https://docs.oracle.com/iaas/Content/Compute/References/images.htm).
Important  
  

Firewall rules and security rules both operate at the instance level. However, you configure security lists at the subnet level, which means all resources in a particular subnet have the same set of security list rules. Also, the security rules in a network security group apply only to the resources in the group. When troubleshooting access to an instance, ensure that all the following items are set correctly: the network security groups that the instance is in, the security lists associated with the instance's subnet, and the instance's firewall rules.

If an instance is running Oracle Autonomous Linux 8.x, Oracle Autonomous Linux 7, Oracle Linux 8, Oracle Linux 7, or Oracle Linux Cloud Developer 8, you need to use[firewalld](https://oracle-base.com/articles/linux/linux-firewall-firewalld)to interact with the iptables rules. For reference, here are commands for opening a port (1521 in this example):

```

```

For instances with an iSCSI boot volume, the preceding`--reload`command can cause problems. For details and a workaround, see[Instances experience system hang after running firewall-cmd --reload](https://docs.oracle.com/iaas/Content/Compute/known-issues.htm#firewallReload).
- Gateways and route tables: To control general traffic flow from a cloud network to outside destinations (the internet, an on-premises network, or another VCN). You configure the cloud network's gateways and route tables in the Oracle Cloud Infrastructure API or Console. For more information about the gateways, see[Networking Components](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Componen). For more information about route tables, see[VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/managingroutetables.htm).
- IAM policies: To control who has access to the Oracle Cloud Infrastructure API or Console itself. You can control the type of access, and which cloud resources can be accessed. For example, you can control who can set up the networks and subnets, or who can update route tables, network security groups, or security lists. You configure policies in the Oracle Cloud Infrastructure API or Console. For more information, see[Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm).
- Security zones: To ensure that the network and other cloud resources comply with Oracle security principles and best practices, you can create them in a security zone. A security zone is associated with a compartment and checks all network management operations against security zone policies. For example, a security zone doesn't allow the use of public IP addresses and can contain only private subnets. For more information, see[Overview of Security Zones](https://docs.oracle.com/iaas/Content/security-zone/using/security-zones.htm)
