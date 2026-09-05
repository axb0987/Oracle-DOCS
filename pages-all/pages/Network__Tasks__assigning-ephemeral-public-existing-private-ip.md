# Assigning an Ephemeral Public IP to an Existing Primary Private IP
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assigning-ephemeral-public-existing-private-ip.htm
- Fetched: 2026-09-05 02:43 CDT

# Assigning an Ephemeral Public IP to an Existing Primary Private IP

Assign an ephemeral public IP address to an instance to enable communication with the internet.

Prerequisite: The primary private IP must not have a reserved or ephemeral public IP already assigned to it. If it does, first[delete the public ephemeral IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/deleting-ephemeral-public-ip-from-instance.htm), or[unassign the reserved public IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-unassign.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assigning-ephemeral-public-existing-private-ip.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assigning-ephemeral-public-existing-private-ip.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assigning-ephemeral-public-existing-private-ip.htm#)
- 

- Open the navigation menu and select Compute . Under Compute , select Instances .
- On the Networking tab, go to the Attached VNICs section and select the VNIC that you're interested in.
- Select the IP administration tab to display the VNIC's primary private IP and any secondary private IPs.
- For the VNIC's primary private IP, select the Actions menu (three dots) , and then select Edit .
- Under Public IP type , select Ephemeral public IP .
- In the Ephemeral Public IP Name field, enter an optional friendly name for the public IP. The name doesn't have to be unique, and you can change it later. Avoid entering confidential information.
- Select Update .
- 

Use the[network public-ip create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/create.html)command and required parameters to assign a public IP:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/CreatePublicIp)
