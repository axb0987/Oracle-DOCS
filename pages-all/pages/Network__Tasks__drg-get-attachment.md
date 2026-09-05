# Getting a DRG Attachment's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-attachment.htm
- Fetched: 2026-09-05 02:43 CDT

# Getting a DRG Attachment's Details

Get the configuration details for a Dynamic Routing Gateway (DRG) attachment in Oracle Cloud Infrastructure.

For details about DRGs, see[Working with DRGs and DRG Attachments](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__drg_attach).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-attachment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-attachment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-attachment.htm#)
- 

- On the Dynamic Routing Gateways list page, select the DRG that you want to work with. If you need help finding the list page or the DRG, see[Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Attachments tab, go to the section that corresponds to the attachment's type.
- Under Resources , select an option corresponding to the attachment's type.

The available DRG attachment types are:
- VCN attachments
- Virtual circuit attachments
- IPSec tunnel attachments
- Remote peering connection attachments
- Loopback attachments
- Cross-tenancy attachments
- Select the name of the attachment you're interested in.
- 

Use the[network drg-attachment get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-attachment/get.html)command and required parameters to get details for a DRG attachment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetDrgAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgAttachment/GetDrgAttachment)
