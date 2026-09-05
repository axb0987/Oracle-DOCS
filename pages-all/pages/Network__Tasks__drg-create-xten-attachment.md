# Attaching a DRG to a VCN in a Different Tenancy
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-xten-attachment.htm
- Fetched: 2026-09-05 02:43 CDT

# Attaching a DRG to a VCN in a Different Tenancy

Learn to attach a Dynamic Routing Gateway (DRG) to a VCN in another tenancy.

The VCN you're connecting to must be in the same OCI region. Before you can create a cross-tenancy attachment, you must implement the IAM policies described in[Attaching to VCNs in Other Tenancies](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__xtenancy-VCN). Attaching a VCN in another tenancy requires knowing the OCID of the VCN, but otherwise isn't very different from[attaching a VCN in the same tenancy](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-attachment.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-xten-attachment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-xten-attachment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-xten-attachment.htm#)
- 

- On the Dynamic Routing Gateways list page, select the DRG that you want to work with. If you need help finding the list page or the DRG, see[Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Attachments tab, go to the Cross-tenancy attachments section and select Create cross-tenancy attachment .
- Under Resources , select Cross-tenancy attachments then select Create cross-tenancy attachment .
- (Optional) Give the attachment point a friendly name. If you don't specify a name, one is created for you.
- Enter the OCID of the VCN in another tenancy you want to attach to the DRG.
Because the VCN is in another tenancy, it's not possible to filter for it by name and compartment. Tenancies use different and unconnected namespaces. The OCID is the only reliable way to identify and specify resources across tenancies.
- (Optional) If you're setting up an[advanced scenario for transit routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm), you can associate a VCN route table with the DRG attachment (you can do this later):
- Select Show Advanced Options (if present).
- Go to the VCN route table tab (or section). Select the route table that you want to associate with the VCN attachment on the DRG.
If you select None , the default VCN route table is used.
- (Optional) If you're planning to use transit routing and need to associate a specific DRG route table to the attachment, go to the DRG route table tab (or section) and select an existing DRG route table. See[Creating a DRG Route Table](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-create.htm).
- (Optional) If you need to specify that you want to import VCN CIDRs into a DRG route table from the VCN attachment, go to the VCN Route type tab (or section) and select VCN CIDRs .
If you don't explicitly select VCN CIDRs , Subnet CIDRs is chosen for you and the subnet CIDRs are imported into a DRG route table from the VCN attachment. Routes from the VCN ingress route table are always imported.
- When you're finished, select Create cross-tenancy attachment .
- 

Use the[network drg-attachment create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-attachment/create.html)command and required parameters to attach a VCN in another tenancy to a DRG:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateDrgAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgAttachment/CreateDrgAttachment)
