# Controlling Traffic for a Service Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/sgw-traffic.htm
- Fetched: 2026-09-05 02:47 CDT

# Controlling Traffic for a Service Gateway

You can block or allow traffic for a service gateway in a virtual cloud network (VCN).

You create a service gateway in the context of a specific VCN. That is, the service gateway is always attached to that one VCN. However, you can block or allow traffic through the service gateway at any time. By default, the gateway allows traffic flow upon creation. Blocking the service gateway traffic prevents all traffic from flowing, regardless of what service CIDR labels are enabled, or any existing route rules or security rules in the VCN.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/sgw-traffic.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/sgw-traffic.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/sgw-traffic.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the gateway that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Gateways tab, go to the Service Gateways section.
- Under Resources , select Service Gateways .
- From the Actions menu (three dots) for the service gateway that you're interested in, select Block Traffic (or Allow Traffic if you're enabling traffic for the service gateway).
When the traffic is blocked, the service gateway's icon turns gray, and the State label changes to Blocked. When the traffic is allowed, the service gateway's icon turns green, and the State label changes to Available.
- 

Use the[network service-gateway update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/service-gateway/update.html)command and required parameters to block or allow traffic for a service gateway:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateServiceGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ServiceGateway/UpdateServiceGateway)operation to block or allow traffic for a service gateway, using the`blockTraffic`
