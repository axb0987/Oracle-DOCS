# Deleting a Security List
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/deleting-securitylist.htm
- Fetched: 2026-09-05 02:41 CDT

# Deleting a Security List

Delete a security list in a Virtual Cloud Network (VCN).

To delete a security list, it must not be associated with a subnet. You can't delete a VCN's default security list.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/deleting-securitylist.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/deleting-securitylist.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/deleting-securitylist.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the security list you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Security tab, go to the Security Lists section.
- Under Resources , select Security Lists .
- From the Actions menu (three dots) for the security list, select Terminate .
- When prompted, confirm the deletion.
- 

Use the[network security-list delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/security-list/delete.html)command and required parameters to delete a security list:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/DeleteSecurityList)
