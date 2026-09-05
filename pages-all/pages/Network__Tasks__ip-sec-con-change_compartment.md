# Moving an IPSec Connection Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-change_compartment.htm
- Fetched: 2026-09-05 02:44 CDT

# Moving an IPSec Connection Between Compartments

You can move an IPSec connection from one compartment to another.

When you move an IPSec connection, its associated IPSec tunnels move with it to the new compartment. This changes the management of the resources with no changes to the routing of the traffic.

The IPSec connection is moved immediately. Resources attached to the IPSec connection are moved asynchronously and don't appear in the new compartment until the move is complete.

If any alarms are monitoring the connection, update the alarms to reference the new compartment. See[Updating an Alarm After Moving a Resource](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-after-resource-move.htm)for more information.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-change_compartment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-change_compartment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-change_compartment.htm#)
- 

- On the Site-to-Site VPN list page, find the IPSec connection that you want to move. If you need help finding the list page or the IPSec connection, see[Listing IPSec Connections](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-list.htm).
- From the Actions menu (three dots) for the IPSec connection, select Move Resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- If alarms monitor the IPSec connection, update the alarms to reference the new compartment. See[Updating an Alarm After Moving a Resource](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-after-resource-move.htm).
- 

Use the[network ip-sec-connection change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/ip-sec-connection/change-compartment.html)command and required parameters to move an IPSec connection from one compartment to another:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeIPSecConnectionCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnection/ChangeIPSecConnectionCompartment)
