# Renaming an ASN
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-rename.htm
- Fetched: 2026-09-05 02:40 CDT

# Renaming an ASN

Change the display name of an Autonomous System Number (ASN) in Oracle Cloud Infrastructure.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-rename.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-rename.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOASN-rename.htm#)
- 

- Open the navigation menu and select Networking . Under IP management , select BYOASN .
- For the ASN that you want to change, select the Actions menu (three dots) , and then select Rename .
- On the Rename page, enter a new ASN name. The name doesn't have to be unique. Avoid entering confidential information.
- Select Update .

View the work request to see the status.
- 

Use the`network byoasn update`command and required parameters to rename your ASN:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

-
