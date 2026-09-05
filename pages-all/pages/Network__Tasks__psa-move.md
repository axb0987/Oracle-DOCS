# Moving a PSA Endpoint to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/psa-move.htm
- Fetched: 2026-09-05 02:46 CDT

# Moving a PSA Endpoint to a Different Compartment

Move a PSA endpoint into a different compartment within the same tenancy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/psa-move.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/psa-move.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/psa-move.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the PSA endpoint that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- Go to the Private service access tab.
- Select the the Actions menu (three dots) for the PSA endpoint, and then select Move Resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[psa private-service-access change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/psa/private-service-access/change-compartment.html)command and required parameters to move a PSA endpoint into a different compartment within the same tenancy:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangePrivateServiceAccessCompartment](https://docs.oracle.com/iaas/api/#/en/psasvc/latest/PrivateServiceAccess/ChangePrivateServiceAccessCompartment)
