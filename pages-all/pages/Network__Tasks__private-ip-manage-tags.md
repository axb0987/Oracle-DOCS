# Managing Tags For a Private IP Object
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-manage-tags.htm
- Fetched: 2026-09-05 02:46 CDT

# Managing Tags For a Private IP Object

Update tag information for a private IP object.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-manage-tags.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-manage-tags.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-manage-tags.htm#)
- 

- Open the navigation menu and select Compute . Under Compute , select Instances .
- Select the name of the instance to open its details page.
- On the Networking tab, go to the Attached VNICs section and select the VNIC that you're interested in.
- Select the IP administration tab.
The IP addresses associated with the VNIC are listed in tabular form.
- Find the IP object you want to update, select its Actions menu (three dots), and then select Manage tags .
- From there you can view the existing tags, edit them, and apply new ones. For more information see,[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- 

Use the[private-ip update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/private-ip/update.html)command and required parameters to update tags for the private IP address:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdatePrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/UpdatePrivateIp)
