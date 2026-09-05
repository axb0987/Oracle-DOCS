# Deleting a DRG Attachment
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-delete-attachment.htm
- Fetched: 2026-09-05 02:43 CDT

# Deleting a DRG Attachment

Detach a Dynamic Routing Gateway (DRG) from a resource in Oracle Cloud Infrastructure.

You detach a DRG from a Virtual Cloud Network (VCN) by deleting the`DrgAttachment`resource. This doesn't require deleting the VCN.

When you delete a virtual circuit, IPSec tunnel, or remote peering connection (RPC) resource, the corresponding attachment to the DRG is automatically deleted. These resources can't be detached from a DRG without deleting the resource itself.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-delete-attachment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-delete-attachment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-delete-attachment.htm#)
- 

- On the Dynamic Routing Gateways list page, select the DRG that you want to work with. If you need help finding the list page or the DRG, see[Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Attachments tab, go to the section that corresponds to the attachment's type.
- Under Resources , select an option corresponding to the attachment's type.

You're only able to delete attachments with the DRG attachment types of:
- VCN attachments
- Cross-tenancy attachments
- From the Actions menu (three dots) for the DRG attachment, select Delete .
- When prompted, confirm the deletion.
- 

Use the[network drg-attachment delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-attachment/delete.html)command and required parameters to delete a DRG attachment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteDrgAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgAttachment/DeleteDrgAttachment)
