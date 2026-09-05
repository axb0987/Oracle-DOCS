# Unassigning a Reserved Public IP
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-unassign.htm
- Fetched: 2026-09-05 02:47 CDT

# Unassigning a Reserved Public IP

Unassign a reserved public IP object in Oracle Cloud Infrastructure.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-unassign.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-unassign.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-unassign.htm#)
- 

- Open the navigation menu and select Compute . Under Compute , select Instances .
- Select the compartment that contains the instance using the private IP address to which you want to assign a public IP object.
- Select the name of the instance to view its details.
- On the Networking tab, go to the Attached VNICs section and select the VNIC that uses the private IP address.
- Select the IP administration tab to display the VNIC's primary private IP address and any secondary private IP addresses.
- For the private IP to which you want to assign the public address, select the Actions menu (three dots) , and select Edit .
- If the private IP address already has a public IP assigned to it, unassign it as follows:
- Under Public IP type , select n for No public IP .
- Select Update .
- Again for the private IP address, select the Actions menu (three dots) , and select Edit .
- Under Public IP Type , select Reserved Public IP , and then select the Select Existing Reserved IP Address option.
- In the Reserved IP Address list, select the reserved public IP object that you want to assign, changing the compartment as needed.

The public IP object is moved from the private IP address that it's currently assigned to.
- Select Update .
- 

Use the[network public-ip update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/update.html)command and required parameters to unassign a reserved public IP address from a private IP:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/UpdatePublicIp)
