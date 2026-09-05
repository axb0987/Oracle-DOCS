# Deleting a Node for Compute, GPU, and Storage Devices
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/delete_node2.htm
- Fetched: 2026-09-05 03:01 CDT

# Deleting a Node for Compute, GPU, and Storage Devices

Delete a Roving Edge Infrastructure device node in Oracle Cloud Infrastructure.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/delete_node2.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/delete_node2.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/delete_node2.htm#)
- 

- 

In the Oracle Cloud Console, open the navigation menu, select Hybrid , then select Nodes .
- 

If needed, change the compartment to find the resource you want.
- 

(Optional) Select a State from the list under Tag filters to limit the device nodes displayed to that state.
- 

Select the node that you want to delete.
- 

From the Actions menu at the top of the table, select delete.
- 

Confirm the deletion when prompted.

The device node you deleted no longer appears in the nodes list.
- 

Use the[oci rover node delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/rover/node/delete.html)command and required parameters to delete a Roving Edge Infrastructure device node in Oracle Cloud Infrastructure:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
- 

Run the[DeleteRoverNode](https://docs.oracle.com/iaas/api/#/en/rover/latest/RoverNode/DeleteRoverNode)
