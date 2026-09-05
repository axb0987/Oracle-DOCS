# Attaching a VCN to a DRG
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/attach-vcn-drg.htm
- Fetched: 2026-09-05 02:43 CDT

# Attaching a VCN to a DRG

Attach a Virtual Cloud Network (VCN) to a Dynamic Routing Gateway (DRG).

A VCN can be attached to only one DRG at a time, but a DRG can be attached to many VCNs (see[Networking Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#network_limits)). The attachment is automatically created in the compartment that holds the VCN. The VCN and DRG don't need to be in the same compartment. You can optionally specify a display name for the attachment itself, otherwise a default is provided. You can decide to connect VCNs in the same region using a single DRG instead of local peering gateways (see[Local VCN Peering Through an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm)for more information about that use case). The default routing policies in a DRG allow traffic to be routed between all VCNs attached to it. If you're attaching a DRG to a VCN in another tenancy, you need to have IAM configurations in both tenancies as described in[IAM Policies for Routing Between VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm). You also need the OCID of the VCN.

When you create an attachment to a DRG (the DRG can be in another tenancy in the same OCI region), attachments on both the DRG and VCN are created and connected in one step. Attaching a DRG to a VCN results in a`DrgAttachment`object with its own OCID.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/attach-vcn-drg.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/attach-vcn-drg.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/attach-vcn-drg.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- Select the Gateways tab. Dynamic Routing Gateway Attachments is the first section on the page.
- Under Resources , select Dynamic Routing Gateways Attachments .
- Select Create DRG Attachment .
A VCN can only have one DRG attachment at a time.
- Enter a friendly name for the DRG attachment. It doesn't have to be unique. Avoid entering confidential information.
- In the DRG Location section, select Current Tenancy or Another tenancy depending on the location of the DRG you want to attach.

- If you select Current Tenancy , select a DRG from the list. If the DRG is in another compartment, select that compartment and then select the DRG.
- If you select Another tenancy , enter the OCID of the DRG.
- (Optional) If you're setting up an[advanced scenario for transit routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm), you can associate a VCN route table with the DRG attachment (you can do this later):
- Select Advanced Options .
- In the Route Table Association section. Select the Select Exisiting option and then select a VCN route table that you want to associate with the VCN attachment to the DRG. If you select None , the default VCN route table is used.
- (Optional) In the Tags section, add one or more tags. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create DRG attachment .

The attachment is in the Attaching state for a short period.

When the attachment is ready, create a route rule in the subnet's route table directing subnet traffic to the DRG. See[To route a subnet's traffic to a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables_topic-working.htm#add_route_rule).

From the Dynamic Routing Gateway Attachments list, you can also select the Actions menu (three dots) for the DRG attachment to view its details, manage its tags, and delete it.
- 

Use the[network drg-attachment create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-attachment/create.html)command and required parameters to attach a VCN to a DRG:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateDrgAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgAttachment/CreateDrgAttachment)
