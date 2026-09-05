# Editing a Node for Compute, GPU, and Storage Devices
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/update_node2.htm
- Fetched: 2026-09-05 03:01 CDT

# Editing a Node for Compute, GPU, and Storage Devices

Edit a Roving Edge node in Oracle Cloud Infrastructure.

You can't edit a Roving Edge node if you have already provisioned the Roving Edge device.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/update_node2.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/update_node2.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/update_node2.htm#)
- 

- 

In the Oracle Cloud Console, open the navigation menu, select Hybrid , then select Nodes .
- 

If needed, change the compartment to find the resource you want.
- 

(Optional) Select a State from the list under Tag filters to limit the device nodes displayed to that state.
- 

Select the device node that you want to edit. The device node's Details page appears.
- 

From the Actions menu at the top of the table, select Edit . The Edit Node dialog box appears.
- 

Make your edits. See[Creating and Submitting a Node for Compute, GPU, and Storage Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/create_node2.htm#top)for descriptions of the settings.
- 

Select Save changes .
- 

Use the[oci rover node update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/rover/node/update.html)command and required parameters to edit a Roving Edge Infrastructure device node in Oracle Cloud Infrastructure:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
- 

Run the[UpdateRoverNode](https://docs.oracle.com/iaas/api/#/en/rover/latest/RoverNode/UpdateRoverNode)
