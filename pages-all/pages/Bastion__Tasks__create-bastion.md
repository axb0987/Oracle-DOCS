# Creating a Bastion
- Source: https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-bastion.htm
- Fetched: 2026-09-05 01:42 CDT

# Creating a Bastion

Create a bastion to provide restricted access to target resources that don't have public endpoints.

Before you begin, ensure that you have the following information about the target resource, such as an instance or database) that you intend to use this bastion to host sessions for:
- The VCN (virtual cloud network) that the target was created in
Tip  
  
If you haven't created a VCN, consider using a[Virtual Networking Quickstart](https://docs.oracle.com/iaas/Content/Network/Tasks/quickstartnetworking.htm#Virtual_Networking_Quickstart)wizard.
- A private subnet in the VCN
- The name of the subnet that the target resource was created in
- Another subnet that has access to the target resource's subnet if the target's subnet allows ingress network traffic from the selected subnet
- The IPv4 addresses from which you plan to connect to sessions hosted by the bastion

The VCN must include a service gateway and a route rule for the service gateway. See[Access to Oracle Services: Service Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm).
Note  
  

A bastion is associated with a single VCN. You can't create a bastion in one VCN and then use it to access target resources in a different VCN.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-bastion.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-bastion.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-bastion.htm#)
- 

- On the Bastions list page, select Create bastion . If you need help finding the list page, see[Listing Bastions](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/../common/../Tasks/list-bastion.htm).
- Enter a name for the bastion. Avoid entering any confidential information in this field. Only alphanumeric characters are supported.
- Under Configure networking , select the following options:

- Select the target VCN of the target resource that you intend to connect to by using sessions hosted on this bastion. If needed, change the compartment to find the VCN.
- Select the target subnet. The subnet must either be the same as the target resource's subnet or it must be a subnet from which the target resource's subnet accepts network traffic. If needed, change the compartment to find the subnet.
- (Optional) Select Enable FQDN Support and SOCKS5 to extend the local port forwarding session type to accept domain names as a target resource identifier, or to enable the bastion to use the dynamic port forwarding (SOCKS5) session type.
- For CIDR block allowlist , add one or more address ranges in CIDR notation that you want to allow to connect to sessions hosted by this bastion. For example,`203.0.113.0/24`.

Enter a CIDR block into the input field, and then either select the value or press Enter to add the value to the list. The maximum allowed number of CIDR blocks is 20.

A more limited address range offers better security.
- Expand Advanced options and enter the following information as needed:

- Management : (Optional) Change the maximum amount of time that any session on this bastion can remain active by entering a value for Maximum session time-to-live . Provide a value of at least 30 minutes that doesn't exceed 180 minutes (3 hours). You can delete a session before it expires.
- Tags : (Optional) Add one or more tags to the bastion. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Security attributes : (Optional) Add security attributes to the bastion to control access through the Zero Trust Packet Routing (ZPR) service. You can add up to three security attributes per bastion. For more information, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm).
- When you're finished, select one of the following options:

- To create the bastion, select Create bastion .
- To save the resource definition as a Terraform configuration, select Save as Stack .

For more information about saving stacks from resource definitions, see[Creating a Stack from a Resource Creation Page](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-stack-resource.htm).

After you create a bastion, you can create a session. For options, see[Managing Sessions](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/managingsessions.htm).
- 

Use the[oci bastion bastion create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bastion/bastion/create.html)command and required parameters to create a bastion:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[
