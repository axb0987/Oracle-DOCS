# DRG Management
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/manage-drg.htm
- Fetched: 2026-09-05 02:45 CDT

# DRG Management

Learn how to mange a Dynamic Routing Gateway (DRG) in Oracle Cloud Infrastructure.

In general, to use a DRG, you must complete these minimal steps:
- Create the DRG.
- Attach the DRG to one or more VCNs. You can also attach a DRG to an on-premises network using FastConnect virtual circuits and Site-to-Site VPN IPSec tunnels.
- Route subnet traffic to the DRG by updating the route table associated with each subnet that must send traffic to the DRG.

The following tasks are available for a DRG:
- [Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm)
- [Creating a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create.htm)
- [Getting a DRG's Details](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get.htm)
- [Getting a List of DRG Attachments](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-all-drg-attachments.htm)
- [Finding the DRG Upgrade Status](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-upgrade-status.htm)
- [Getting the DRG Redundancy Status](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-redundancy-status.htm)
- [Updating the Name of a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-update.htm)
- [Upgrading a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-upgrade.htm)
- [Moving a DRG to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-change-compartment.htm)
- [Deleting a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-delete.htm)

The following tasks are available for DRG attachments:
- [Attaching a DRG to a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-attachment.htm)
- [Getting a DRG Attachment's Details](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-attachment.htm)
- [Listing DRG Attachments](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list-attachment.htm)
- [Updating a DRG Attachment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-update-attachment.htm)
- [Deleting a DRG Attachment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-delete-attachment.htm)

## Limitations

Some functions might appear to be possible based on the structure of the resource interaction model, but the following functions aren't allowed:
- Explicit creation or deletion of RPC, IPSec tunnel, or virtual circuit attachments
- Static routes in DRG route tables with next-hop of IPSec tunnel or virtual circuit attachments
- Use or creation of new export route distributions other than the defaults
- Dynamic route export to VCN attachments
- Propagating a route through more than 3 DRG route tables
-
