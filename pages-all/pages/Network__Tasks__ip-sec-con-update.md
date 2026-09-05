# Updating an IPSec Connection
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-update.htm
- Fetched: 2026-09-05 02:45 CDT

# Updating an IPSec Connection

Update details for the specified IPSec connection.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-update.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-update.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-update.htm#)
- 

- On the Site-to-Site VPN list page, select the IPSec connection that you want to work with. If you need help finding the list page or the IPSec connection, see[Listing IPSec Connections](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-list.htm).
- Select Edit .
- Update the name, CPE IKE identifier, or[static route settings](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_static_route)as needed. Avoid entering confidential information. For descriptions of these settings, see[Creating an IPSec Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-create.htm).

If you're[Changing the CPE IKE Identifier That Oracle Uses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_cpe_ike_id), enter new values for CPE IKE Identifier Type and CPE IKE Identifier ,
- Select Save changes .
The changes take effect within a few seconds.
- 

Use the[network ip-sec-connection update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/ip-sec-connection/update.html)command and required parameters to update details for the specified IPSec connection:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateIPSecConnection](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnection/UpdateIPSecConnection)operation to update details for the specified IPSec connection.

Run the[UpdateIPSecConnectionTunnelDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateIPSecConnectionTunnelDetails)
