# Networking Scenarios
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarios.htm
- Fetched: 2026-09-05 02:47 CDT

# Networking Scenarios

## Basic Scenarios

All except the first of these basic routing scenarios send traffic from a subnet in the VCN to the DRG. To accomplish this,[set up a rule in the subnet's route table](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables_topic-working.htm#add_route_rule). The rule's destination CIDR is the CIDR of the network you want to reach through the DRG, and the rule's target is the DRG. For more information, see[VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm).
- [Scenario A: Public Subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioa.htm)(no DRG required)
- [Scenario B: Private Subnet with a VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenariob.htm)
- [Scenario C: Public and Private Subnets with a VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioc.htm)

## Peering

These scenarios all allow traffic to flow from one VCN to another.
- [Local VCN Peering Through an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm)(Upgraded DRG)
- [Remote VCN Peering through an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_e.htm)(Upgraded DRG)
- [Local VCN Peering using Local Peering Gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm)(Legacy DRG)
- [Remote VCN Peering using a Legacy DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm)(Legacy DRG)

## Advanced Scenarios Using a Single DRG

VCN Ingress Routing : Some advanced scenarios require ingress routing of traffic entering the VCN from a DRG through the VCN attachment. To accomplish this, you must associate a VCN route table (this is a route table created inside a VCN) with the VCN attachment. After a VCN route table is associated with a VCN attachment, there must always be a VCN route table associated with that attachment (you can't update the field in the corresponding data object to "Null"). Removing the VCN ingress routing functionality from a VCN attachment can only be done by emptying the associated VCN route table or updating the attachment to use an empty VCN route table.
- [Remote on-ramp](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_f.htm)(Upgraded DRG)
- [Routing traffic through a central network virtual appliance](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm)(Upgraded DRG)
- [Private Access to Oracle Services](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)
- [Transit Routing inside a hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)

## Advanced Scenario with Several DRGs and Several VCNs

The transit routing scenario illustrates the use of several DRGs and VCNs. In this case, each VCN has its own dynamic routing gateway (DRG) and its own FastConnect private virtual circuit . Contrast this with[Transit Routing inside a hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm), which has a single DRG with either Site-to-Site VPN or a single FastConnect private virtual circuit.

Here are some restrictions for using this scenario with several DRGs:
- The scenario works only with FastConnect through a[third-party provider](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/fastconnectthirdpartyprovider.htm)or through[colocation with Oracle](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/fastconnectcolocate.htm). The scenario isn't supported for FastConnect through an[Oracle partner](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/fastconnectprovider.htm).
- The scenario is supported only for VCNs in the same region and same tenancy. This is because all the virtual circuits use a single cross-connect, a regional resource.

See[FastConnect with Multiple DRGs and VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/fastconnectmultipledrgs.htm)
