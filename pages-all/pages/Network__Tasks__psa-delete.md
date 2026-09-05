# Deleting a PSA Endpoint
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/psa-delete.htm
- Fetched: 2026-09-05 02:46 CDT

# Deleting a PSA Endpoint

Delete a PSA endpoint in a Virtual Cloud Network (VCN) to remove access to a service in the Oracle Services Network (OSN).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/psa-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/psa-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/psa-delete.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the PSA endpoint that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- Go to the Private service access tab.
- From the Actions menu (three dots) for the PSA endpoint you want to delete, select Delete .
- When prompted, confirm the deletion.
- 

Use the[psa private-service-access delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/psa/private-service-access/delete.html)command and required parameters to delete a PSA endpoint:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeletePrivateServiceAccess](https://docs.oracle.com/iaas/api/#/en/psasvc/latest/PrivateServiceAccess/DeletePrivateServiceAccess)
