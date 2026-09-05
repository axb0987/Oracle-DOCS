# Getting Details for a Security List
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/getting_details-securitylist.htm
- Fetched: 2026-09-05 02:41 CDT

# Getting Details for a Security List

Get the details for a security list in a Virtual Cloud Network (VCN).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/getting_details-securitylist.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/getting_details-securitylist.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/getting_details-securitylist.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the security list you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/list-vcn.htm).
- Perform one of the following actions depending on the option that you see:

- On the Security tab, go to the Security lists section and select the security list that you want to view rules for. Security Lists is the first section on the page.
- Under Resources , select Security lists , and then select the security list that you want to view rules for.

The details page for the security list opens and displays information about the security list. Access the rules associated with the security list by selecting their links or tabs.
- On the details page for the security list, perform one of the following actions depending on the option that you see:

- Select the Security rules tab. Ingress Rules is the first section on the page. Egress Rules is the second section on the page.
- Under Resources , select Ingress Rules or Egress Rules , depending on the type of rules that you want to view. The rules are displayed in a table.
- 

Use the[network security-list get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/security-list/get.html)command and required parameters to get details for a security list:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/GetSecurityList)
