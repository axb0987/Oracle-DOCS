# FastConnect with Multiple DRGs and VCNs
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectmultipledrgs.htm
- Fetched: 2026-09-05 02:41 CDT

# FastConnect with Multiple DRGs and VCNs

Learn how to set up FastConnect with multiple private virtual circuits to multiple VCNs.

This topic summarizes an advanced networking scenario that enables communication between an on-premises network and multiple virtual cloud networks (VCNs) over a single[Oracle Cloud Infrastructure FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm). Each VCN has its own Dynamic Routing Gateway (DRG) , and you set up a separate FastConnect private virtual circuit to each DRG. This scenario is available to an implementation using either a legacy or upgraded[DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/managingDRGs.htm#overview__Versions).

This scenario is supported for only certain FastConnect setups:
- Using a[third-party provider](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm)or a[Colocation with Oracle in a FastConnect location](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm)is fully supported.
- Using multiple DRGs and VCNs with an[Oracle partner](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm)depends on your partner's support of this feature. Some partners also provide alternative solutions to achieve the same goal, so check with your chosen[Oracle partner](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm)for details.

There's a scenario called transit routing that also involves using multiple VCNs, but only a single DRG. It can be used with Site-to-Site VPN or FastConnect. It involves setting up the VCNs in a hub-and-spoke layout and filtering DRG traffic between spokes through a hub VCN, after which the DRG performs transit routing of traffic to the other VCNs. You might use this scenario if you need multiple VCNs for different parts of your organization, but you want to use one VCN for centralized services that all parts of the organization need. For more information, see[Routing traffic through a central network virtual appliance](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/scenario_g.htm).

## Highlights

- You can use a single FastConnect to connect your on-premises network with multiple VCNs in the same region. The scenario is supported only for FastConnect through a[third-party provider](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm)or through[colocation with Oracle](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm). You need at least one physical connection (cross-connect) in your connection.
- The VCNs must be in the same region and same tenancy . The VCNs can be in the same compartment or different ones in the tenancy. For accurate routing, the CIDR blocks of the various subnets of interest in the on-premises network and VCNs must not overlap.
- Each VCN has its own dynamic routing gateway (DRG) and private virtual circuit . Always use a different VLAN and different set of BGP IP addresses for each private virtual circuit.
- You can also use FastConnect public peering to give your on-premises network access to public endpoints of Oracle services and public resources inside a VCN via internet gateway. In this case, you set up a single public virtual circuit . With public peering, configure your edge device (also known as your customer-premises equipment or CPE ) to prefer FastConnect over your ISP for the Oracle Cloud Infrastructure public IP prefixes. Or, if you plan to also set up[private access to Oracle services through one of the VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/transitroutingoracleservices.htm), see the important routing details in[Routing Details for Connections to the On-premises Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem.htm).

## Overview of the Scenario

In this scenario, you have a single FastConnect that connects your existing on-premises network to Oracle Cloud Infrastructure. That FastConnect has at least one physical connection, or cross-connect .

In Oracle Cloud Infrastructure, you have multiple VCNs, all in the same region. Each VCN has its own DRG. For each VCN, there's a private virtual circuit that runs on the FastConnect and terminates at your CPE on one end, and on the VCN's DRG on the other end. The private virtual circuit enables communication that uses private IP addresses between the VCN and the on-premises network. See the following diagram.
[

For example, imagine that each department in your organization has its own subnet in your on-premises network and a corresponding departmental VCN in Oracle Cloud Infrastructure. You want to enable private communication between each department's subnet and VCN over the FastConnect.

Or, perhaps all the departments need to communicate with all the VCNs. For example, instead perhaps the VCNs are for separate development, test, and production environments, and each department needs access to all three VCNs.

The FastConnect and virtual circuits give you the general private connection where none of the traffic traverses the internet. You can separately control which on-premises subnets and VCNs can communicate by configuring route rules in your on-premises network and VCN[route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/managingroutetables.htm). You can optionally configure VCN[security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm)and other firewalls that you maintain to allow only certain types of traffic (such as SSH) between your on-premises network and VCN.

### Public Peering

You can also set up public peering on that same FastConnect by creating a public virtual circuit. In the following diagram, the public virtual circuit is shown separate from the private virtual circuits. It terminates at Oracle's edge. The public virtual circuit enables communication that uses public IP addresses but does not traverse the internet.

All public resources in a VCN can be reachable over public peering if there is internet access. See[FastConnect Public Peering Advertised Routes](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectpublicpeeringaddressranges.htm)for more detail. For other important details about how you can control route preferences when you have multiple connections between your on-premises network and Oracle, see[Routing Details for Connections to the On-premises Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem.htm).
[

When you set up public peering for your FastConnect, the public IP prefixes that you designate for the public virtual circuit are advertised to all the VCNs in your tenancy. The routes advertised to your on-premises network are all the Oracle Cloud Infrastructure public IP addresses (including the CIDRs for each of the VCNs in the tenancy).
Important  
  
Your network receives Oracle's public IP addresses through both FastConnect and your Internet Service Provider (ISP). When configuring your edge, give higher preference to FastConnect over your ISP, or you will not receive the benefits of FastConnect. If you plan to also set up[private access to Oracle services through one of the VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/transitroutingoracleservices.htm), see the important routing details in[Routing Details for Connections to the On-premises Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem.htm).

For more information, see[Basic Network Diagrams](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#diagrams).

## General Setup Process

The setup process and instructions are in these topics, based on your particular FastConnect setup:
- [FastConnect: With a Third-Party Provider](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm)
- [FastConnect: Colocation with Oracle](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm)

However, remember that:
- You set up a separate DRG for each VCN. A DRG can be attached to multiple VCNs, but each VCN can be attached to only a single DRG. In this example, there is a separate DRG for each VCN.
- You set up a separate private virtual circuit for each DRG.
- For each private virtual circuit, you must specify a different VLAN and a different set of BGP IP addresses .
-
