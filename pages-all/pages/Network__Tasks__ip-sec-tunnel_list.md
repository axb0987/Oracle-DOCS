# Listing IPSec Tunnels
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-tunnel_list.htm
- Fetched: 2026-09-05 02:45 CDT

# Listing IPSec Tunnels

List the IPSec tunnels available in an IPSec connection.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-tunnel_list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-tunnel_list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-tunnel_list.htm#)
- 

- On the Site-to-Site VPN list page, select the IPSec connection that you want to work with. If you need help finding the list page or the IPSec connection, see[Listing IPSec Connections](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-list.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- Select the Tunnels tab.
- Scroll down to the table following the IPSec connection details, which lists the IPSec tunnels in the IPSec connection.

All tunnels in the IPSec connection are displayed in a table and the status for each tunnel is shown. When the BGP Status for the tunnel you're interested in shows only a hyphen (no value) that means that the tunnel is configured to use static routing.
- 

Use the[network ip-sec-tunnel list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/ip-sec-tunnel/list.html)command and required parameters to list the IPSec tunnels available in an IPSec connection:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListIPSecConnectionTunnels](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnectionTunnel/ListIPSecConnectionTunnels)
