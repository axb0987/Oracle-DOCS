# Deleting an Ephemeral Public IP From an Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/deleting-ephemeral-public-ip-from-instance.htm
- Fetched: 2026-09-05 02:43 CDT

# Deleting an Ephemeral Public IP From an Instance

Deleting an ephemeral public IP automatically unassigns it from its private IP.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/deleting-ephemeral-public-ip-from-instance.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/deleting-ephemeral-public-ip-from-instance.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/deleting-ephemeral-public-ip-from-instance.htm#)
- 

- Open the navigation menu and select Compute . Under Compute , select Instances .
- Select the instance to view its details.
- On the Networking tab, go to the Attached VNICs section and select the VNIC that you're interested in.
- Select the IP administration tab to display the VNICs primary private IP and any secondary private IPs.
- For the VNIC's primary private IP, select the Actions menu (three dots) , and then select Edit .
- Under Public IP type , select No public IP .
- Select Update .
- 

Use the[network public-ip delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/delete.html)command and required parameters to delete an ephemeral public IP:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeletePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/DeletePublicIp)
