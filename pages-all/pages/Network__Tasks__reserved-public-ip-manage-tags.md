# Managing Tags for a Reserved Public IP
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-manage-tags.htm
- Fetched: 2026-09-05 02:47 CDT

# Managing Tags for a Reserved Public IP

Update the tag information for a reserved public IP address.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-manage-tags.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-manage-tags.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-manage-tags.htm#)
- 

- Open the navigation menu and select Networking . Under IP management , select Reserved public IPs .
- For the reserved public IP you want to edit, select the Actions menu (three dots) , and then select Manage tags .
From there you can view the existing tags, edit them, and apply new ones. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- 

Use the[network public-ip update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/update.html)command and required parameters to manage tags for a public IP:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/UpdatePublicIp)
