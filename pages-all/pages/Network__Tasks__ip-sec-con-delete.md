# Deleting an IPSec Connection
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-delete.htm
- Fetched: 2026-09-05 02:44 CDT

# Deleting an IPSec Connection

Delete an IPSec connection from OCI.

To disable Site-to-Site VPN between an on-premises network and VCN, you can detach the DRG from the VCN instead of deleting the IPSec connection. If you're also using the DRG with[FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/fastconnect.htm), detaching the DRG would also interrupt the flow of traffic over FastConnect.

You can delete the IPSec connection. However, if you later want to reestablish it, a network engineer must configure the CPE device again with a new set of tunnel configuration information from Oracle.

To permanently delete Site-to-Site VPN, you must first terminate the IPSec connection. Then you can[delete the CPE object](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-delete.htm). If you're not using the DRG for another connection to an on-premises network, you can[detach it from the VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-delete-attachment.htm)and then[delete it](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-delete.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-delete.htm#)
- 

To delete an IPSec connection, follow these steps:

- On the Site-to-Site VPN list page, find the IPSec connection that you want to delete. If you need help finding the list page or the IPSec connection, see[Listing IPSec Connections](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-list.htm).
- From the Actions menu (three dots) for the IPSec connection you want to delete, select Terminate .
- When prompted, confirm the deletion.

The IPSec connection is in the Terminating state for a short period while it's being deleted.
- 

Use the[network ip-sec-connection delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/ip-sec-connection/delete.html)command and required parameters to delete an IPSec connection:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteIPSecConnection](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnection/DeleteIPSecConnection)
