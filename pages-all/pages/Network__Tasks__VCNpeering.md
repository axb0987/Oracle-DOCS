# Access to Other VCNs: Peering
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm
- Fetched: 2026-09-05 02:43 CDT

# Access to Other VCNs: Peering

VCN peering is the process of connecting many virtual cloud networks (VCNs). Four types of VCN peering are available:
- [Local VCN peering (within region)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/localVCNpeering.htm)using LPGs
- [Remote VCN peering (across regions)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/remoteVCNpeering.htm)using RPCs
- [Local VCN Peering Through an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/scenario_d.htm)
- [Remote VCN Peering through an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/scenario_e.htm)

You can use VCN peering to divide a large network into several VCNs (for example, based on departments or lines of business), with each VCN having direct, private access to the others. Traffic doesn't need to flow over the internet or through an on-premises network by way of[Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/managingIPsec.htm)or[FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/fastconnect.htm). You can also place shared resources into a single VCN that all the other VCNs can access privately.

Each VCN can have up to 10 local peering gateways and can attach to only one DRG. A single DRG supports up to 300 VCN attachments, allowing traffic between them to flow as directed by the DRG's route tables. We recommend using the DRG if you need to peer with many VCNs. If you want the highest possible bandwidth and super low-latency traffic between two VCNs in the same region, use the scenario described in[Local VCN Peering using Local Peering Gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/localVCNpeering.htm).[Local VCN Peering Through an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/scenario_d.htm)gives you more flexibility in routing because of the greater number of attachments.

Because remote VCN peering crosses regions, you can use it (for example) to mirror or back up databases in one region to another region.

## Overview of Local VCN Peering

Local VCN peering is the process of connecting two VCNs in the same region so that their resources can communicate using private IP addresses without routing the traffic over the internet or through an on-premises network. The VCNs can be in the same Oracle Cloud Infrastructure tenancy or different ones. Without peering, a particular VCN would need an[internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm)and public IP addresses for the instances that need to communicate with another VCN.

[Local VCN Peering Through an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm)gives you more flexibility in routing and simplified management but comes at the cost of an increase in latency (by microseconds) from routing traffic through a virtual router, the DRG.

## Important Implications of Peering

This section summarizes some access control, security, and performance implications for peered VCNs. In general, you can control access and traffic between two peered VCNs by using IAM policies, route tables in each VCN, and security lists in each VCN.

### Controlling the Establishment of Peerings

With IAM policies, you can control:
- Who can[subscribe your tenancy to another region](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm)(required for remote VCN peering)
- Who in an organization has the authority to establish VCN peerings (for example, see the IAM policies in[Setting Up a Local Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Setting)and[Setting Up a Remote Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Setting)). Deletion of these IAM policies doesn't affect any existing peerings, only the ability for future peerings to be created.
- Who can[manage route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm)and[security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securitylists.htm)

### Controlling Traffic Flow Over the Connection

Even if a peering connection has been established between one VCN and another, you can control the packet flow over the connection with route tables in the VCN. For example, you can restrict traffic to only specific subnets in the other VCN.

Without ending the peering, you can stop traffic flow to the other VCN by removing route rules that direct traffic from one VCN to the other VCN. You can also effectively stop the traffic by removing any security list rules that enable ingress or egress traffic with the other VCN. This doesn't stop traffic flowing over the peering connection, but stops it at the[VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm)level.

For more information about the routing and security lists, see the discussions in these sections:

Local VCN peering using local peering groups:
- [Important Local Peering Concepts](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Importan)
- [Task E: Configure the route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Step4)
- [Task F: Configure the security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Step5)

Remote VCN peering using a remote peering connection:
- [Important Remote Peering Concepts](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Importan)
- [Task E: Configure the route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Step4)
- [Task F: Configure the security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Step5)

Local VCN peering using a Dynamic Routing Gateway (DRG) :
- [Important Local Peering Concepts](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenariod__lp_concepts)
- [Task D: Configure route tables in VCN-A to send traffic destined to VCN-B's CIDR to the DRG attachment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenario_dtask_d_dita)
- [Task E: Configure route tables in VCN-B to send traffic destined to VCN-A's CIDR to the DRG attachment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenario_dtask_e_dita)
- [Task F: Update security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenario_dtask_f_dita)

Remote VCN peering using a dynamic routing gateway (DRG):
- [Summary of Networking Components for Remote Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_e.htm#scenario_e__remote_components)
- [Task D: Configure the route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_e.htm#scenario_e_task_e)
- [Task E: Configure the security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_e.htm#scenario_e_task_f)

### Controlling the Specific Types of Traffic Allowed

Each VCN administrator ensures all outbound and inbound traffic with the other VCN is intended or expected and defined. In practice, this means implementing security list rules that explicitly state the types of traffic one VCN can send to the other and accept from the other.
Important  
  

Compute instances running[platform images](https://docs.oracle.com/iaas/Content/Compute/References/images.htm)also have OS firewall rules that control access to the instance. When troubleshooting access to an instance, ensure that all the following items are set correctly:
- The rules in the network security groups that the instance is in
- The rules in the security lists associated with the instance's subnet
- The instance's OS firewall rules

If an instance is running Oracle Autonomous Linux 8.x, Oracle Autonomous Linux 7, Oracle Linux 8, Oracle Linux 7, or Oracle Linux Cloud Developer 8, you need to use[firewalld](https://oracle-base.com/articles/linux/linux-firewall-firewalld)to interact with the iptables rules. For reference, here are commands for opening a port (1521 in this example):

```

```

For instances with an iSCSI boot volume, the preceding`--reload`command can cause problems. For details and a workaround, see[Instances experience system hang after running firewall-cmd --reload](https://docs.oracle.com/iaas/Content/Compute/known-issues.htm#firewallReload).

In addition to security lists and firewalls, evaluate other OS-based configuration on the instances in the local VCN. There could be default configurations that don't apply to the local VCN's CIDR, but inadvertently apply to the other VCN's CIDR.

### Using Default Security List Rules

If the local VCN's subnets use the[default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securitylists.htm#Default)with the default rules it comes with, be aware of two rules that allow ingress traffic from anywhere (0.0.0.0/0 and thus the other VCN):
- Stateful ingress rule that allows TCP port 22 (SSH) traffic from 0.0.0.0/0 and any source port
- Stateful ingress rule that allows ICMP type 3, code 4 traffic from 0.0.0.0/0 and any source port

Evaluate these rules and whether you want to keep or update them. As stated earlier, ensure that all inbound or outbound traffic that you allow is intended or expected and defined.

### Preparing for Performance Impact and Security Risks

In general, prepare the local VCN for the ways it could be affected by the other VCN. For example, the load on the local VCN or its instances could increase. Or the local VCN could experience a malicious attack directly from or by way of the other VCN.

Regarding performance: If the local VCN is providing a service to another, be prepared to scale up service to accommodate the demands of the other VCN. This might mean being prepared to create more Compute instances as necessary. Or if you're concerned about high levels of network traffic coming to the local VCN, consider using[stateless security list rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securityrules.htm#stateful)to limit the level of connection tracking the local VCN must perform. Stateless security list rules can also help slow the impact of a denial-of-service (DoS) attack.
