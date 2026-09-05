# Changing the Display Name of a Reserved Public IP
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-change-display-name.htm
- Fetched: 2026-09-05 02:46 CDT

# Changing the Display Name of a Reserved Public IP

Change the display name of a reserved public IP object in Oracle Cloud Infrastructure.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-change-display-name.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-change-display-name.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-change-display-name.htm#)
- 

- Open the navigation menu and select Networking . Under IP management , select Reserved public IPs .
- Select the compartment that contains the reserved public IP object in Oracle Cloud Infrastructure.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see[Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/accesscontrol.htm).
- For the reserved public IP object that you want to change, select the Actions menu (three dots) , and then select Rename .
- Enter a new display name. The name doesn't have to be unique. Avoid entering confidential information.
- Select Save changes .
- 

Use the[network public-ip update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/update.html)command and required parameters to change the display name of a public IP:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/UpdatePublicIp)
