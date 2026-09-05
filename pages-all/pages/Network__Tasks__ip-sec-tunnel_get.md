# Getting an IPSec Tunnel's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-tunnel_get.htm
- Fetched: 2026-09-05 02:45 CDT

# Getting an IPSec Tunnel's Details

Get configuration details for an IPSec tunnel in an IPSec connection.

When you successfully create the IPSec connection, Oracle produces important configuration information for each of the resulting IPSec tunnels. You can view that information and the status of the tunnels at any time. This includes the BGP status if the tunnel is configured to use BGP dynamic routing.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-tunnel_get.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-tunnel_get.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-tunnel_get.htm#)
- 

- On the Site-to-Site VPN list page, select the IPSec connection that contains the tunnel you want to work with. If you need help finding the list page or the IPSec connection, see[Listing IPSec Connections](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-list.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- Select the Tunnels tab, then select the name of the tunnel you want to work with.
- Scroll down to the table following the IPSec connection details, which lists the IPSec tunnels in the IPSec connection. Then select the name of the tunnel you want to work with.
- To view a tunnel's shared secret, perform one of the following actions depending on the option that you see:

- Next to Shared secret on the tunnel details tab, select the Actions menu (three dots) and then select Show .
- Next to Shared secret on the tunnel information tab, select Show .
- To[change a tunnel's shared secret](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_shared_secret), perform one of the following actions depending on the option that you see:

- Next to Shared secret on the tunnel details tab, select the Actions menu (three dots) and then select Edit .
- Next to Shared secret on the tunnel information tab, select Edit .

From here, you can enter a new value for the shared secret. Only numbers, letters, and spaces are allowed. Then select Save Changes .
- To view Phase one (ISAKMP) information and Phase two (IPSec) information , select the Phase details tab.
- To view a tunnel's BGP advertised and received routes (including the AS PATH for each route) perform one of the following actions depending on the option that you see:

- Select either the BGP Routes Received tab or the BGP Routes Advertised tab.
- Under Resources , select either BGP Routes Received or BGP Routes Advertised .
- To access the[CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm)from this location, perform one of the following actions depending on the option that you see:

- Select Open CPE configuration helper .
- Select the Actions button, then select Open CPE configuration helper .

The helper opens on the right side of the page.

It shows information such as the CPE's public IP address and vendor. See[Get CPE Device Configuration Information](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-get_device_config_content.htm)for more about using the helper.
- 

Use the[network ip-sec-tunnel get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/ip-sec-tunnel/get.html)command and required parameters to get configuration details for an IPSec tunnel:

```

```

Use the[network ip-sec-psk get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/ip-sec-psk/get.html)command and required parameters to get the specified tunnel's shared secret (pre-shared key):

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetIPSecConnectionTunnel](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnectionTunnel/GetIPSecConnectionTunnel)operation to get configuration details for an IPSec tunnel.

Run the[GetIPSecConnectionTunnelSharedSecret](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnectionTunnelSharedSecret/GetIPSecConnectionTunnelSharedSecret)
