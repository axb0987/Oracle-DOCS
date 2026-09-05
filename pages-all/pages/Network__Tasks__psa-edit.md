# Editing a PSA Endpoint
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/psa-edit.htm
- Fetched: 2026-09-05 02:46 CDT

# Editing a PSA Endpoint

You can update the name of a PSA endpoint in a Virtual Cloud Network (VCN).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/psa-edit.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/psa-edit.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/psa-edit.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that has the PSA endpoint you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- Go to the Private service access tab.
- Find the PSA endpoint in the Private service access list, select the Actions menu (three dots) for it, and then select Edit .
- Update the Name as needed. Avoid entering confidential information.
- Select Update .
No other attributes can be changed from this screen.
- To change security settings ([ZPR Security Attributes](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm)and Network security groups ) for the PSA endpoint, select the name of the endpoint from the Private service access list, change to the Security tab, and scroll to the section with the details you want to update.
- 

Use the[psa private-service-access update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/psa/private-service-access/update.html)command and required parameters to update information for a PSA endpoint:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdatePrivateServiceAccess](https://docs.oracle.com/iaas/api/#/en/psasvc/latest/PrivateServiceAccess/UpdatePrivateServiceAccess)
