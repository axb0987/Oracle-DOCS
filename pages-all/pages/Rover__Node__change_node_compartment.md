# Moving a Roving Edge Infrastructure Device Node Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Node/change_node_compartment.htm
- Fetched: 2026-09-05 03:01 CDT

# Moving a Roving Edge Infrastructure Device Node Between Compartments

Move a Roving Edge Infrastructure device node between compartments in Oracle Cloud Infrastructure.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Node/change_node_compartment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Node/change_node_compartment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Node/change_node_compartment.htm#)
- 

- 

In the Oracle Cloud Console, open the navigation menu, select Hybrid , then select Nodes .
- 

If needed, change the compartment to find the resource you want.
- 

(Optional) Select a State from the list under Tag filters to limit the device nodes displayed to that state.
- 

Select the node you want to move to a different compartment. The node's Details page appears.
- 

From the Actions menu at the top of the table, select Move resource . The Move resource dialog box appears.
- 

Select the compartment to which you want to move your device node from the Destination Compartment list.
- 

Select Move resource .

The device node now appears in the nodes list within the compartment where you moved it.
- 

Use the[oci rover node change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/rover/node/change-compartment.html)command and required parameters to move a Roving Edge Infrastructure device node between compartments in Oracle Cloud Infrastructure:
```

```

To determine your Roving Edge Infrastructure device compartment OCID, see[Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/Node/../compartments.htm#comparments).

`compartment_ocid`is the destination compartment.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
- 

Run the[ChangeRoverNodeCompartment](https://docs.oracle.com/iaas/api/#/en/rover/latest/RoverNode/ChangeRoverNodeCompartment)
