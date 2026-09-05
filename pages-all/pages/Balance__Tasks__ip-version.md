# Managing a Load Balancer's IP Version
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/ip-version.htm
- Fetched: 2026-09-05 01:41 CDT

# Managing a Load Balancer's IP Version

Specify whether you want your load balancer to support only IPv4, or enable IPv6 addressing to create a dual-stack IPv4/IPv6 load balancer.

You can update an existing load balancer that only supports IPv4 to support IPv6 as well, resulting in a dual-stack IPv4/IPv6 load balancer. For more information on how the Load Balancer service uses IPv6, see[IPv6 Support](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/../Concepts/balanceoverview.htm#ipv6-support).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/ip-version.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/ip-version.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/ip-version.htm#)
- 

You can't perform this activity using the Console.
- 

Use the[oci lb load-balancer update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/load-balancer/update.html)command and required parameters to update a load balancer. Include the optional`ip-mode`parameter with the value`IPV6`:

```

```

This command adds IPv6 support to the existing IPv4 support, creating a dual-stack IPv4 and IPv6 load balancer.

When you add IPv6 support, you have the option of having the IPv6 address draw from a specific subnet. Include the`--ipv6-subnet-cidr`parameter with an appropriate CIDR value. For example:

```

```

To use a pre-reserved IPv6 addresses, include the`reserved-ips`parameter and the list of IP address as the value. For example:

```

```

The`reserved-ips`value is a complex type whose value must be valid JSON. You can provide the value as a string on the command line or passed in as a file using the`file://path/to/file`syntax. For more information, see[ReservedIP Reference](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/datatypes/ReservedIP).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

## Converting a Dual Stack Load Balancer Back to Single Stack IPv4

If you have a dual stack IPv4 and IPv6 load balancer, and you want to convert it into a single stack IPv4 only, run the`oci lb load-balancer update`CLI command and give the`ip-mode`parameter the value`IPV4`.

```

```

This command removes the IPv6 support.
- 

Run the[UpdateLoadBalancer](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/LoadBalancer/UpdateLoadBalancer)operation to update a load balancer. Include the optional`ipMode`parameter with the value`IPV6`. This operation adds IPv6 support to the existing IPv4 support, creating a dual-stack IPv4 and IPv6 load balancer.

## Converting a Dual Stack Load Balancer Back to Single Stack IPv4

If you have a dual stack IPv4 and IPv6 load balancer, and you want to convert it into a single stack IPv4 only, run the[UpdateLoadBalancer](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/LoadBalancer/UpdateLoadBalancer)operation and give the`ipMode`parameter the value`IPV4`.
