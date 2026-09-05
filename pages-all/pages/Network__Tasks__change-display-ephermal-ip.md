# Changing the Display Name for an Ephemeral Public IP
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/change-display-ephermal-ip.htm
- Fetched: 2026-09-05 02:43 CDT

# Changing the Display Name for an Ephemeral Public IP

You can change the display name of an ephemeral public IP.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/change-display-ephermal-ip.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/change-display-ephermal-ip.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/change-display-ephermal-ip.htm#)
- 

- Open the navigation menu and select Compute . Under Compute , select Instances .
- Select the instance to view its details.
- On the Networking tab, go to the Attached VNICs section and select the VNIC that you're interested in.
- Select the IP administration tab to display the VNICs primary private IP and any secondary private IPs.
- For the VNIC's primary private IP, select the Actions menu (three dots) , and then select Edit .
- Under the Public IP type , select the radio button for Ephemeral public IP .
- Edit the Ephemeral Public IP Name . The name doesn't have to be unique, and you can change it later. Avoid entering confidential information.
- Select Update .
- 

Use the[network public-ip update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/update.html)command and required parameters to change the display name of an ephemeral public IP:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/UpdatePublicIp)
