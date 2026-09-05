# Listing DRG Attachments
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list-attachment.htm
- Fetched: 2026-09-05 02:44 CDT

# Listing DRG Attachments

Find a list of DRG attachments for a specified Dynamic Routing Gateway (DRG) and compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list-attachment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list-attachment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list-attachment.htm#)
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
- Cross-tenancy attachments The DRG attachments are displayed in sections and tables sorted by attachment type.
- 

Use the[network drg-attachment list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-attachment/list.html)command and parameters to find a list of DRG attachments for a specified DRG and compartment:

```

```

You can also filter the results by attached network, attachment type, DRG route table or VCN route table.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListDrgAttachments](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgAttachment/ListDrgAttachments)
