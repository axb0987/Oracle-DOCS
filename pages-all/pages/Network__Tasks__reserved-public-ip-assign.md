# Assigning a Reserved Public IP to a Private IP
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-assign.htm
- Fetched: 2026-09-05 02:46 CDT

# Assigning a Reserved Public IP to a Private IP

Assign a reserved public IP object to a private IP address in Oracle Cloud Infrastructure.

The VNIC's private IP address must not have an ephemeral or reserved public IP object already assigned to it. If it does, first either[delete the public ephemeral IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/deleting-ephemeral-public-ip-from-instance.htm), or[unassign the reserved public IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/deleting-ephemeral-public-ip-from-instance.htm).
Note  
  
IP CIDR addresses don't support assigning a public IP address.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-assign.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-assign.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-assign.htm#)
- 

- Open the navigation menu and select Compute . Under Compute , select Instances .
- Select the compartment that contains the instance using the private IP address to which you want to assign a public IP object.
- Select the name of the instance to view its details.
- On the Networking tab, go to the Attached VNICs section and select the name of the VNIC that uses a private IP.
- Select the IP administration tab to display the VNIC's primary private IP address and any secondary private IP addresses.
- For the private IP address to which you want to assign a public IP object, select the Actions menu (three dots) , and select Edit .
- Under Public IP type , select Reserved public IP .
- Select one of the following options:

- Select Existing Reserved IP Address : If you select this option, perform the following:

Select the reserved public IP from the Reserved IP Address in &lt;compartment&gt; list. Change the compartment to find the IP address source you want if it resides in a different compartment.
- Create new Reserved IP Address : If you select this option, enter the following information:
- Public IP Name : A descriptive name for the reserved public IP object. The name doesn't have to be unique, and you can change it later. Avoid entering confidential information.
- Create in Compartment : The compartment in which you want to create the reserved public IP, which could be different from the compartment you're working in.
- IP Address Source : (Optional) The[IP pool](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/ip_pools.htm)that the IP address is drawn from. Change the compartment to find the IP address source you want if it resides in a different compartment. If you don't select a pool, the default Oracle pool is used.
- Select Update .
- 

Use the[network public-ip update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/update.html)command and required parameters to assign a reserved public IP address to a private IP:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/UpdatePublicIp)
