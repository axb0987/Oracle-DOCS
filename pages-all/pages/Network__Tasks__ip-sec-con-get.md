# Getting IPSec Connection Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-get.htm
- Fetched: 2026-09-05 02:44 CDT

# Getting IPSec Connection Details

View the settings for a particular Site-to-Site VPN IPSec connection.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-get.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-get.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-get.htm#)
- 

- On the Site-to-Site VPN list page, select the IPSec connection that you want to work with. If you need help finding the list page or the IPSec connection, see[Listing IPSec Connections](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-list.htm).

The details page opens and displays information about the IPSec connection. Some items on the page are read-only, and other items enable you to edit and update the IPSec connection's configuration. Access the various resources associated with the IPSec connection by selecting their links or tabs. These resources include the IPSec tunnels in the IPSec connection and the DRG attachments used by the tunnels.
- To access the[CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm)from this location, perform one of the following actions depending on the option that you see:

- Select Open CPE configuration helper .
- Select the Actions button, then select Open CPE configuration helper .

The helper opens on the right side of the page.

It shows basic information such as the CPE's public IP address and vendor.
- To enable message logging for the IPSec connection, perform one of the following actions depending on the option that you see:

- On the Logs tab, go to the Logs section. From the Actions menu (three dots) for the IPSec Tunnel Logs you want to enable, select Enable log .
- Under Resources , select Logs . From the Actions menu (three dots) for the IPSec Tunnel Logs you want to enable, select Enable log .

The Log detail page is displayed, and the log is in the process of being created (a "Creating log" message is displayed).
- To view log messages, perform one of the following actions depending on the option that you see:

- On the Logs tab, go to the Logs section. Select the Log Name of the log you're interested in. This opens a new browser tab showing the requested log.
- Under Resources , select Logs . Select the Log Name of the log you're interested in. This opens a new browser tab showing the requested log.

See[Getting a Log's Details](https://docs.oracle.com/iaas/Content/Logging/Task/get-logging-log.htm)for details on using the log screen.
- 

Use the[network ip-sec-connection get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/ip-sec-connection/get.html)command and required parameters to view the settings for a particular Site-to-Site VPN IPSec connection:

```

```

Use the[network ip-sec-tunnel get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/ip-sec-tunnel/get.html)command and required parameters to get information on a specified tunnel in the IPSec connection:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

Use the[network ip-sec-psk get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/ip-sec-psk/get.html)command and required parameters to get the specified tunnel's shared secret (pre-shared key):

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetIPSecConnection](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnection/GetIPSecConnection)operation to view the settings for a particular Site-to-Site VPN IPSec connection.

This gets the specified IPSec connection's basic information, including the static routes for the on-premises router. If you want the status of the connection (whether it's up or down), use[GetIPSecConnectionTunnel](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnectionTunnel/GetIPSecConnectionTunnel)
