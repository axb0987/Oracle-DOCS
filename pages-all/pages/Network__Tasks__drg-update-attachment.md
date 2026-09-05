# Updating a DRG Attachment
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-update-attachment.htm
- Fetched: 2026-09-05 02:44 CDT

# Updating a DRG Attachment

Update the configuration details of a Dynamic Routing Gateway (DRG) attachment in Oracle Cloud Infrastructure.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-update-attachment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-update-attachment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-update-attachment.htm#)
- 

You can use the Console to update the display name of an attachment and advanced options including DRG route table, VCN route table, and VCN route type.

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
- Select Edit .
- (Optional) Change the display name of the attachment.
- (Optional) Select Show Advanced options and change the other options associated with the attachment. The options can vary from attachment type to attachment type
- Select Save changes .
- 

Use the[network drg-attachment update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-attachment/update.html)command and required parameters to update a DRG attachment's configuration details:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateDrgAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgAttachment/UpdateDrgAttachment)
