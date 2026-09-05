# Creating a Reserved Public IP
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-create.htm
- Fetched: 2026-09-05 02:46 CDT

# Creating a Reserved Public IP

Create a reserved public IP object in a pool of reserved public IP addresses in Oracle Cloud Infrastructure.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-create.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-create.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-create.htm#)
- 

- Open the navigation menu and select Networking . Under IP management , select Reserved public IPs .
- Select Reserve public IP address .
- Enter the information for the reserved public IP object:

- Reserved public IP address name : A descriptive name for the reserved public IP. The name doesn't have to be unique, and you can change it later. Avoid entering confidential information.
- Create in Compartment : The compartment in which you want to create the reserved public IP, which could be different from the compartment you're currently working in.
- IP address source : (Optional) The[IP pool](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/ip_pools.htm)that the reserved public IP address is drawn from. If necessary, change the compartment to find the IP address source you want. If you don't select a pool that you've created, the default Oracle pool is used.
- In the Tags section, add one or more tags to reserved public IO object.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Reserve public IP address .

The new reserved public IP is created and displayed on the page. You can now[assign it to an existing private IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-assign.htm).
- 

Use the[network public-ip create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/create.html)command and required parameters to create a reserved public IP address:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/CreatePublicIp)
