# Listing PSA Endpoints
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/psa-list.htm
- Fetched: 2026-09-05 02:46 CDT

# Listing PSA Endpoints

List the PSA endpoints available in a particular VCN and compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/psa-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/psa-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/psa-list.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that has the PSA endpoints you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- Go to the Private service access tab.

All PSA endpoints in the VCN are displayed in a table.
- (Optional) You can also navigate to the[details for a specific subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-subnet.htm)then go to the Private service access tab to see the PSA endpoints created in that subnet.
- 

Use the[psa private-service-access list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/psa/private-service-access/list.html)command and required parameters to list the PSA endpoints available in a particular VCN and compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListPrivateServiceAccesses](https://docs.oracle.com/iaas/api/#/en/psasvc/latest/PrivateServiceAccessCollection/ListPrivateServiceAccesses)
