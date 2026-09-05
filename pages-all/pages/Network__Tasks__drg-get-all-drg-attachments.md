# Getting a List of DRG Attachments
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-all-drg-attachments.htm
- Fetched: 2026-09-05 02:43 CDT

# Getting a List of DRG Attachments

Get a list of DRG attachments that belong to a particular dynamic routing gateway (DRG).

This task functions differently in the Console than in the API or CLI. The Console distinguishes by attachment type while the other methods don't.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-all-drg-attachments.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-all-drg-attachments.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-all-drg-attachments.htm#)
- 

- On the Dynamic Routing Gateways list page, select the DRG that you want to work with. If you need help finding the list page or the DRG, see[Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- Select the Attachments tab. The various attachment types are separated into sections.
- Under Resources , the attachment types are listed according to their type. The number of attachments with a particular type is listed. Scroll down to the table following the VCN details, which lists the subnets in the VCN.

The attachment types are:
- VCN attachments
- Virtual circuit attachments
- IPSec tunnel attachments
- Remote peering connection attachments
- Loopback attachments
- Cross-tenancy attachments
- 

Use the[network drg get-all-drg-attachments](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg/get-all-drg-attachments.html)command and required parameters to get a list of DRG attachments that belong to a particular DRG:

```

```

Use the parameters shown to get a list of attachments with a certain type that belong to a particular DRG:

```

```

Use the parameters shown to get a list of all attachments that belong to a different tenancy:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetAllDrgAttachments](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Drg/GetAllDrgAttachments)
