# Updating an IPSec Tunnel
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-tunnel_update.htm
- Fetched: 2026-09-05 02:45 CDT

# Updating an IPSec Tunnel

Edit the settings for an IPSec tunnel in an IPSec connection.

You can't create an IPSec tunnel without creating an IPSec connection.

When you change tunnel attributes such as the routing type (BGP dynamic routing, static routing, or policy-based) here are a few things to consider:
- 

If you change the tunnel's routing type or BGP session configuration, the tunnel goes down while it's reprovisioned.
- 

If you switch the tunnel's`routing`from`STATIC`to`BGP`, ensure that the tunnel's BGP session configuration attributes have been set.
- 

If you switch the tunnel's`routing`from`BGP`to`STATIC`, ensure that the IPSec connection already has at least one valid CIDR static route.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-tunnel_update.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-tunnel_update.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-tunnel_update.htm#)
- 

- On the Site-to-Site VPN list page, select the IPSec connection that contains the tunnel you want to work with. If you need help finding the list page or the IPSec connection, see[Listing IPSec Connections](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-list.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- Select the Tunnels tab.
- Scroll down to the table following the IPSec connection details, which lists the IPSec tunnels in the IPSec connection.
- Find the tunnel in the Tunnels list, select the Actions menu (three dots) for it, and then select Edit .
- Update the settings as needed. Avoid entering confidential information. For descriptions of the settings, see[Creating an IPSec Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-create.htm).
- Select Save changes .
- To[change a tunnel's shared secret](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_shared_secret), perform one of the following actions depending on the option that you see:

- Next to Shared secret on the tunnel details tab, select the Actions menu (three dots) and then select Edit . Make changes, then select Save changes .
- Next to Shared secret on the tunnel information tab, select Edit . Make changes, then select Save changes .
- To[change a tunnel from static routing to BGP dynamic routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#static_to_bgp):

Caution  
  
When you change a tunnel's routing type, the tunnel's IPSec status doesn't change during reprovisioning. However, routing through the tunnel is affected. Traffic is temporarily disrupted until a network engineer configures the CPE device in accordance with the routing type change. If an existing Site-to-Site VPN is configured to only use a single tunnel, this process disrupts the connection to Oracle. If a Site-to-Site VPN instead uses several tunnels, we recommend reconfiguring one tunnel at a time to avoid disrupting the connection to Oracle.

Read[Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing)and gather the necessary BGP routing information:
- The network's ASN. Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544. For the Government Cloud, see[Oracle's BGP ASN](https://docs.oracle.com/iaas/Content/gov-cloud/govinfo.htm#bgp_asn).
- For each tunnel: The BGP IP address for each end of the tunnel (the two addresses for a particular tunnel must be a pair from a /30 or /31 subnet, and they must be part of Site-to-Site VPN's encryption domain)
- For each tunnel in the IPSec connection, change the following settings, then select Save Changes .

- Routing Type: Select BGP Dynamic Routing .
- BGP ASN: Enter the network's BGP ASN.
- Inside Tunnel Interface - CPE: Enter the BGP IP address with subnet mask (either /30 or /31) for the CPE end of the tunnel. For example: 10.0.0.16/31.
- Inside Tunnel Interface - Oracle: Enter the BGP IP address with subnet mask (either /30 or /31) for the Oracle end of the tunnel. For example: 10.0.0.17/31.

The tunnel's BGP Status changes to Down.
- On the on-premises side of the connection, confirm that the tunnel's BGP session is in an established state. If it's not, ensure the configuration of the IP addresses for the tunnel is correct in the Oracle Console and also for the CPE device.
- Confirm that the tunnel's BGP Status is now Up in the Oracle Console.
- Confirm that the CPE device is learning routes from Oracle, and the CPE device is advertising routes to Oracle. To readvertise the Oracle routes from BGP back to the on-premises network, ensure the CPE device is configured to accept that. An existing policy to advertise the static routes to an on-premises network might not work for the BGP learned routes.
- Ping the Oracle BGP IP address from an side of the connection to confirm that traffic is flowing.
- After confirming the first tunnel is up and running with BGP, repeat the process for the second tunnel.

Important  
  

As noted in[Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing), the static routes that are still configured for the overall IPSec connection don't override the BGP routing. Those static routes are ignored when Oracle routes traffic through a tunnel configured to use BGP.

Also, you can change a tunnel's routing type back to static routing. You might do this if the scheduled downtime window for the CPE device is ending soon and you're having trouble establishing the BGP session. When you switch back to static routing, ensure the overall IPSec connection still has appropriate static routes configured.
- To[change existing route-based tunnels to use policy-based routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#workingwithIPsec-topic-migration-policy-based):
- For Routing type select Policy based routing . This presents an extra configuration option for Associations .
- Under Associations configure all relevant encryption domains. Each entry under On-premises CIDR blocks generates an encryption domain with all possible entries configured under Oracle Cloud CIDR blocks .

For more information see[Encryption domains for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm#spi_policy_based_tunnel).
- For On-premises CIDR blocks add all on-premises CIDR blocks that require connectivity to OCI over the IPSec tunnel.
- For Oracle Cloud CIDR blocks add all OCI CIDR blocks that must be reachable from the on-premises network.
- The values for IPv4 inside tunnel interface - CPE and IPv4 inside tunnel interface - Oracle can be retained as you changed the tunnel's routing type. No changes are required for these values.
- Select Save Changes .
- Navigate back to the parent IPSec connection and repeat the process for the other IPSec tunnel.
- 

Use the[network ip-sec-tunnel update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/ip-sec-tunnel/update.html)command and required parameters to update the settings for an IPSec tunnel:

```

```

Use the[network ip-sec-psk update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/ip-sec-psk/update.html)command and required parameters to update the shared secret (pre-shared key) for the specified tunnel:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateIPSecConnectionTunnel](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnectionTunnel/UpdateIPSecConnectionTunnel)operation to update the settings for an IPSec tunnel.

Run the[UpdateIPSecConnectionTunnelSharedSecret](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnectionTunnelSharedSecret/UpdateIPSecConnectionTunnelSharedSecret)
