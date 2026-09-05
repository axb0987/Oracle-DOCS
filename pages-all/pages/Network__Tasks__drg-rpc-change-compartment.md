# Moving an RPC to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-change-compartment.htm
- Fetched: 2026-09-05 02:44 CDT

# Moving an RPC to a Different Compartment

Move a remote peering connection (RPC) to a different compartment within the same tenancy.

You can move an RPC from one compartment to another. When you move an RPC to a new compartment, policies applied to that compartment apply immediately to the RPC.

For more information about using compartments and policies to control access to a cloud network, see[Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/accesscontrol.htm). For general information about compartments, see[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-change-compartment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-change-compartment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-change-compartment.htm#)
- 

This task can't be performed using the Console.
- 

Use the[network remote-peering-connection change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/remote-peering-connection/change-compartment.html)command and required parameters to move an RPC to a different compartment within the same tenancy:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeRemotePeeringConnectionCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RemotePeeringConnection/ChangeRemotePeeringConnectionCompartment)
