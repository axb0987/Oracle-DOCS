# Managing a Load Balancer's Security Attributes
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/zpr-security-attributes.htm
- Fetched: 2026-09-05 01:42 CDT

# Managing a Load Balancer's Security Attributes

Add, update, and remove security attributes associated with a load balancer.

Use Zero Trust Packet Routing (ZPR) along with, or in place of, network security groups to control network access to OCI resources by applying security attributes to them and creating ZPR policies to control communication among them. For more information, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm).

You can apply security attributes to a load balancer when you create it, or apply them to an existing load balancer. For more information, see[Creating a Load Balancer](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Creating_Load_Balancers.htm)and[Editing a Load Balancer](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Editing_Load_Balancers.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/zpr-security-attributes.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/zpr-security-attributes.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/zpr-security-attributes.htm#)
- 

The following steps describe how to add security attributes to an existing load balancer in the Console. To add security attributes to a load balancer you're creating, see[Creating a Load Balancer](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Creating_Load_Balancers.htm).

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- From the Actions menu for the load balancer, select Add security attributes .
- From the Add security attributes panel, select the Add security attributes button.
Enter the following information:
- Namespace : Select a security attribute namespace from the list. This list contains those security attribute namespaces already configured. See[Creating a Security Attribute Namespace](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/create-security-attribute-namespace.htm)for more information.
- Key : Select a key from the list.
- Value : Select a value for the corresponding key from the list.
- Select the Add security attribute button to add another attribute (to a maximum of three).
You can also update the configuration of any existing security attribute listed here.
- Select Add security attributes at the bottom of the panel to complete the task and return to the load balancer's details page.
The security attributes you added or updated are viewable on the Security tab in the load balancer's Details page.
- 

Use the`security-attributes`parameter to add ZPR security attributes when you're creating a new load balancer or updating an existing one:

```

```

or

```

```

where`security_attributes`are ZPR tags for this load balancer.

For example:
```

```

This is a complex type whose value must be valid JSON. For more information, see[Security Attributes](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/security-attributes.htm).

For more information on how to create or update a load balancer, see[Creating a Load Balancer](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Creating_Load_Balancers.htm)and[Editing a Load Balancer](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Editing_Load_Balancers.htm).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateLoadBalancer](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/LoadBalancer/UpdateLoadBalancer)operation to update a load balancer. Include the`securityAttributes`
