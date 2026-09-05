# Moving a Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_move_a_compartment.htm
- Fetched: 2026-09-05 02:20 CDT

# Moving a Compartment

Move a compartment in an IAM tenancy.
To move a compartment, you must belong to a group that has`manage all-resources`permissions on the lowest shared parent compartment of the current compartment and the destination compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_move_a_compartment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_move_a_compartment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_move_a_compartment.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Compartments .

A list of the compartments that you have access to in the tenancy is displayed. If the compartment you want to move isn't directly beneath the root compartment, select through the hierarchy of compartments to find the compartment.
- For the compartment you want to move, select the Actions menu (three dots) , and then select Move resource .
- Select the destination compartment.
- Confirm that you're aware of the[implications of the move](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/Working_with_Compartments.htm#Understa).
- Select Move resource .
- 

Use the[move](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/compartment/move.html)command and required parameters to move a compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[MoveCompartment](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/MoveCompartment)
