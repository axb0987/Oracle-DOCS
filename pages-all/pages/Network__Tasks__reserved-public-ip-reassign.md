# Reassigning a Reserved Public IP to a Different Private IP
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-reassign.htm
- Fetched: 2026-09-05 02:47 CDT

# Reassigning a Reserved Public IP to a Different Private IP

Move a reserved public IP object from one private IP address to another private IP address.

As an example, let's say that you want to move a reserved public IP object from private IP address A to private IP address B. First, you must ensure that private IP address B doesn't have a public IP address already assigned to it. Then, you assign the reserved public IP address to private IP address B. When you do so, it's automatically unassigned from private IP address A.
Note  
  

IP CIDR addresses don't support assigning a public IP address.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-reassign.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-reassign.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-reassign.htm#)
- 

- Open the navigation menu and select Compute . Under Compute , select Instances .
- Select the compartment that contains the instance using the private IP address to which you want to unassign a public IP object.
- Select the name of the instance to view its details.
- On the Networking tab, go to the Attached VNICs section and select the VNIC that you're interested in.
- Select the IP administration tab to display the VNIC's primary private IP and any secondary private IPs.
- For private IP address to which you want to assign the reserved public IP object, select the Actions menu (three dots) , and then select Edit .
- If the private IP address already has a public IP assigned to it, perform these steps:

- Under Public IP type section, select No public IP .
- Select Update .
- Again for the same private IP address 2, select the Actions menu (three dots) , and then select Edit .
- Under the Public IP type section, select Reserved public IP .
- Select the Select Existing Reserved IP Address option.
- In the Reserved Public IP list, select the reserved public IP that you want to assign, changing the compartment as needed. The reserved public IP object is moved from the public IP it's assigned to.
- Select Update .
- 

Use the[network public-ip update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/update.html)command and required parameters to reassign a reserved public IP address to a different private IP:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/UpdatePublicIp)
