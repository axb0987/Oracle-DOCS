# Managing a Network Load Balancer's Security Attributes
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/security-attributes-network-load-balancer.htm
- Fetched: 2026-09-05 02:49 CDT

# Managing a Network Load Balancer's Security Attributes

Add, update, and remove security attributes associated with a network load balancer.

Use Zero Trust Packet Routing (ZPR) along with, or in place of, network security groups to control network access to OCI resources by applying security attributes to them and creating ZPR policies to control communication among them. For more information, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm).

ZPR security attributes added to a network load balancer are always configured as the Enforce mode.

- [Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/security-attributes-network-load-balancer.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/security-attributes-network-load-balancer.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/security-attributes-network-load-balancer.htm#)
- 

## Adding Security Attributes

- On the Network load balancers list page, find the network load balancer that you want to work with. If you need help finding the list page or the network load balancer, see[Listing Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm).
- From the Actions menu for the network load balancer you want, select Manage security attributes .
The Manage Security Attributes panel opens.
- Enter the following information:

- Namespace : Select a security attribute namespace from the list. This list contains those security attribute namespaces already configured. See[Creating a Security Attribute Namespace](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/create-security-attribute-namespace.htm)for more information.
- Key : Select a key from the list.
- Value : Select a value for the corresponding key from the list.
- Select the Add security attribute button to add another attribute. You can also update the configuration of any existing security attribute listed here.

Note  
  
The number of security attributes you can configure for your network load balancer is limited. See[Limits](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/overview.htm#limits)for details.

- Select Add security attributes at the bottom of the panel to complete the task and return to the network load balancer's details page.
The security attributes you added are viewable Security tab in the network load balancer's Details page.

## Editing Security Attributes

To update a network load balancer's existing security attributes, follow these steps

- Open the Manage Security Attributes panel in the details page as described earlier in this topic.
- Find the network load balancer whose security attributes you want to update.
- From the Actions menu , select Update .
The Update security attribute panel opens.
- Update the security attributes as described earlier in this topic.
- Select Save changes .
The security attributes you added or updated are viewable in the Security tab in the network load balancer's details page.

## Deleting Security Attributes

To delete a network load balancer's existing security attributes, follow these steps

- Open the Manage Security Attributes panel in the details page as described earlier in this topic.
- Find the network load balancer whose security attributes you want to delete.
- From the Actions menu , select Delete .
- When prompted, confirm the deletion.
- 

## Adding Security Attributes

You can include ZPR security attributes when using[oci nlb network-load-balancer create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/network-load-balancer/create.html)command by including the`security-attributes`option and corresponding value:
```

```

where`security_attributes`are ZPR security attributes for this network load balancer.

For example:
```

```

For information on creating a network load balancer using the CLI, see[Creating a Network Load Balancer](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/create-network-load-balancer.htm).

Similarly, you can use the`security-attributes`option when running the[oci opensearch cluster update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/opensearch/cluster/update.html)command to add ZPR security attributes when you're updating it:

```

```

For information on updating a network load balancer using the CLI, see[Editing a Network Load Balancer](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/update-network-load-balancer.htm).

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).

## Editing Security Attributes

Use the`security-attributes`option when running the[oci nlb network-load-balancer update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/network-load-balancer/update.html)command to change the settings of existing ZPR security attributes.

## Deleting Security Attributes

Use the`security-attributes`option with the value "`{}`" when running the[oci nlb network-load-balancer update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/network-load-balancer/update.html)command to delete the settings of ZPR security attributes. For example:
```

```

- 

## Adding Security Attributes

Run the[CreateNetworkLoadBalancer](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/NetworkLoadBalancer/CreateNetworkLoadBalancer)operation to add security attributes to a network load balancer you're creating. Include the`securityAttributes`attributes and it values.

Run the[UpdateNetworkLoadBalancer](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/NetworkLoadBalancer/UpdateNetworkLoadBalancer)operation to add security attributes to an existing network load balancer. Include the`securityAttributes`attributes and it values.

## Editing Security Attributes

Run the[UpdateNetworkLoadBalancer](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/NetworkLoadBalancer/UpdateNetworkLoadBalancer)operation to update a network load balancer. Include the`securityAttributes`attributes and update their existing values.

## Deleting Security Attributes

Run the[UpdateNetworkLoadBalancer](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/NetworkLoadBalancer/UpdateNetworkLoadBalancer)operation to update a network load balancer. Include the`securityAttributes`
