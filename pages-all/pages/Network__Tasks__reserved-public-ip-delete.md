# Deleting a Reserved Public IP
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-delete.htm
- Fetched: 2026-09-05 02:46 CDT

# Deleting a Reserved Public IP

Delete a reserved public IP object in Oracle Cloud Infrastructure.

The reserved public IP object can be in the Assigned state. Deleting a reserved public IP object automatically unassigns it from the private IP address to which it's assigned and returns the public IP address to the pool of unused public IP addresses.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-delete.htm#)
- 

- Open the navigation menu and select Networking . Under IP management , select Reserved public IPs .
- Select the compartment that contains the reserved public IP object that you want to delete.
- For the reserved public IP object you want to delete, select the Actions menu (three dots) , and then select Terminate .
- Confirm when prompted.

After a few seconds, the reserved public IP object is unassigned (if it was assigned) and the address is returned to the pool it came from.
- 

Use the[network public-ip delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/delete.html)command and required parameters to delete a reserved public IP address:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeletePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/DeletePublicIp)
