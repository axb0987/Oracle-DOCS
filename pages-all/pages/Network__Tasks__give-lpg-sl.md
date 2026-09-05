# Configuring Security Rules to Use an LPG
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/give-lpg-sl.htm
- Fetched: 2026-09-05 02:44 CDT

# Configuring Security Rules to Use an LPG

Update a security list in a Virtual Cloud Network (VCN) to include a new rule that allows traffic destined for the other VCN's CIDR to flow through a local peering gateway (LPG).

Each administrator can perform this task before or after the connection is established.

Prerequisite: Each administrator must have the CIDR block or specific subnets for the other VCN. In general, use the same CIDR block you used in the route table rule in[Task E: Configure the route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Step4).

Before you begin, decide which subnets in the VCN need to communicate with the other VCN. Update the security list for each of those subnets to include rules to allow the intended egress or ingress traffic for the CIDR block or subnet of the other VCN.

We recommend adding the following rules:
- Ingress rules for the types of traffic to allow from the other VCN's CIDR or specific subnets.
- An egress rule to allow outgoing traffic from the VCN to the other VCN. If the subnet already has a broad egress rule for all types of protocols to all destinations (0.0.0.0/0), then you don't need to add a special one for the other VCN.

For more information about security rules, see[Security Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securityrules.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/give-lpg-sl.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/give-lpg-sl.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/give-lpg-sl.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the requestor LPG you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Security tab, go to the Security Lists section.
- Under Resources , select Security Lists .
- Select the security list you're interested in.
- On the details page for the security list, perform one of the following actions depending on the option that you see and depending on the type of rule you want to work with:

- Select the Security rules tab. Ingress Rules is the first section on the page, and Egress Rules is the second section.
- Under Resources , select either Ingress Rules or Egress Rules .
- To add a rule, select Add Ingress Rule or Add Egress Rule .

Example

You want to add a stateful rule that enables ingress HTTPS (port 443) traffic from the other VCN's CIDR. Here is the basic information that you would enter in the Add Ingress Rule panel::
- Stateless: Leave this checkbox unselected.
- Source Type: Leave as CIDR.
- Source CIDR: Enter the same CIDR block that the route rules use (see[Configuring VCN Route Tables to Use an LPG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/give-lpg-rt.htm)).
- IP Protocol: Leave as TCP.
- Source Port Range: Leave as All.
- Destination Port Range: Enter 443.
- Description: An optional description of the rule.
- To delete an existing rule, select the Actions menu (three dots) , and then select Remove .
- If you wanted to edit an existing rule, select the Actions menu (three dots) , and then select Edit .
- 

Use the[network security-list update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/security-list/update.html)command and required parameters to update the rules used in a particular security list:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/UpdateSecurityList)
