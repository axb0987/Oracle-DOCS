# Network Load Balancer Management
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/network-load-balancer-management.htm
- Fetched: 2026-09-05 02:48 CDT

# Network Load Balancer Management

Create and manage network load balancers, including creating, updating, and deleting them.

The primary component of the Network Load Balancer service is the network load balancer resource. Each network load balancer you create contains subordinate resources for backend sets, backends servers, listeners, and so forth.

You can perform the following network load balancer management tasks:

[List the network load balancers in a compartment.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm)

[Create a new network load balancer.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/create-network-load-balancer.htm)

[Get a network load balancer's details.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/get-network-load-balancer.htm)

[Edit a network load balancer's settings.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/update-network-load-balancer.htm)

[Move a network load balancer to a different compartment.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/change-compartment-network-load-balancer.htm)

[Manage a network load balancer's security attributes.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/security-attributes-network-load-balancer.htm)

[Enable source/destination preservation in a network load balancer.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/preserve-source-id.htm)

[Update a network load balancer's network security groups.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/update-network-load-balancer-security.htm)

[List a network load balancer's policies.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer-policy.htm)

[List a network load balancer's traffic protocols.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer-protocol.htm)

[Delete a network load balancer within your tenancy.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/delete-network-load-balancer.htm)

## Proxy Protocol

You can use the proxy protocol feature on network load balancers with TCP-based listeners to send source and destination IP addresses and ports to their backend servers across layers of network address translation (NAT) or TCP proxies. Proxy protocol allows network load balancers to send your client IP information to backend applications even when the[source/destination header preservation](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/../BackendSets/preserve-backend-set-source-id.htm)feature isn't available or disabled. Use proxy protocol to support network requirements such as application security (IP ACLs) and compliance logging.
Note  
  
You can't enable proxy protocol on your network load balancer if the source/destination header preservation feature in enabled.

Ensure that your backend applications expect and can parse the proxy protocol v2 header before enabling proxy protocol on your network load balancer. To get more information on proxy protocol version 2, go to the following website and access the proxy protocol documentation:[https://www.haproxy.org/](https://www.haproxy.org/).

The following diagram shows how proxy protocol works to send data traffic between the client, the network load balancer, and its backend server.
  
  

Proxy protocol header and type length values (TLVs) are sent by the network load balancer in a new TCP packet immediately after the final acknowledgement (ACK) from the client is sent. This is part of the three-way TCP handshake. The network load balancer only inserts the proxy protocol headers. It doesn't overwrite or discard any existing data. The network load balancer also marks the PSH flag in the TCP packet. The server side application can immediately process the proxy protocol header information. If the final ACK isn't a bare ACK and has data, the network load balancer sends the proxy protocol packet before sending the data out.

You can enable the proxy protocol in your network load balancer using the following methods:
- Oracle Cloud Infrastructure Console : Enable proxy protocol in the Configure listener section of the Create network load balancer dialog box when you create a network load balancer, or in the Edit listener dialog box of an existing network load balancer's listener.
- CLI : Include the`is-ppv2-enabled`parameter with the value`true`when running the[oci nlb network-load-balancer create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/network-load-balancer/create.html)or[oci nlb listener update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/listener/update.html)commands. For example:

```

```

or

```

```

- API : Include the`isPpv2Enabled`option when creating the network load balancer or updating a listener.

### Limitations

Note the following limitations with using proxy protocol with network load balancers:
- Network load balancers in transparent mode aren't allowed to use proxy protocol as both the preserve source and preserve source destination settings are enabled.
- Proxy protocol can only be enabled for network load balancers using the TCP protocol. If you enable proxy protocol on the wildcard listener or on the multi-protocol TCP/UDP listener, proxy protocol is only available for TCP traffic.
- Proxy protocol on a network load balancer only supports IPv4.

## Communicating Between Virtual Machine Instances

Virtual machine instances that reside within Oracle Cloud VMware Solution (OCVS) can't communicate to VM instances outside of OCVS if both OCVS and the network load balancer are on the same VCN. Here are workarounds to this issue:
- Use a load balancer in front of your non-OCVS virtual machines. For information on how load balancers and network load balancers differ, see[Comparing Load Balancer and Network Load Balancer](https://docs.oracle.com/iaas/Content/Balance/Reference/lb-vs-nlb.htm).
- Move the network load balancer and the non-OCVS virtual machine instances to a different VCN with a OCI Dynamic Routing Gateway (DRG) connecting the OCVS VCN and the other VCN.
-
