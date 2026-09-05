# Editing Private IP Address Information
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-update.htm
- Fetched: 2026-09-05 02:46 CDT

# Editing Private IP Address Information

Update information for a private IP address such as hostname or associated IP type.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-update.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-update.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-update.htm#)
- 

- Open the navigation menu and select Compute . Under Compute , select Instances .
- Select the name of the instance to open its details page.
- On the Networking tab, go to the Attached VNICs section and select the VNIC that you're interested in.
- Select the IP administration tab.
The IP addresses associated with the VNIC are listed in tabular form.
- Find the IP address you want to update, select its Actions menu (three dots), and then select Edit .
- Update the hostname, public IP type, and route table as needed. For more information, see[Assigning a New Secondary Private IP to a VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-create.htm)
- Select Update .
- 

Use the[private-ip update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/private-ip/update.html)command and required parameters to update information for the private IP address:

```

```

Optionally, use the[network private-ip bulk-update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/private-ip/bulk-update.html)command and required parameters to move more than one secondary private IP to a single VNIC with a single command.:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdatePrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/UpdatePrivateIp)operation to update a private IP address.

Optionally, run the[BulkUpdatePrivateIps](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/BulkUpdatePrivateIps)
