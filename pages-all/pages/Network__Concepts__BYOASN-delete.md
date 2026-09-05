# Deleting an ASN
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-delete.htm
- Fetched: 2026-09-05 02:40 CDT

# Deleting an ASN

Delete an ASN and disassociate your BYOIP CIDR block from the deleted Autonomous System Number (ASN).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-delete.htm#)
- 

- Open the navigation menu and select Networking . Under IP management , select BYOASN .
- Select the name of the ASN that you want to delete.
- On the details page, select the Actions menu (three dots) and then select Delete .
A confirmation window appears stating a default ASN will be used to used to associate with your BYOIP CIDR block.
- Select Advertise to confirm that you want to advertise your BYOIP CIDR block with the default ASN.
- Select Update Origin ASN to confirm disassociation of your BYOIP CIDR block from the deleted ASN.
- 

Use the`network byoasn delete`command and required parameters to rename your ASN:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

- 

Run the[DeleteByoasn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Byoasn/DeleteByoasn)
