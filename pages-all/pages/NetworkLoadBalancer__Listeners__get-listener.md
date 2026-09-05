# Getting Network Load Balancer Listener Details
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/get-listener.htm
- Fetched: 2026-09-05 02:48 CDT

# Getting Network Load Balancer Listener Details

View the details of a listener for a network load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/get-listener.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/get-listener.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/get-listener.htm#)
- 

- On the Network load balancers list page, select the network load balancer that you want to work with. If you need help finding the list page or the network load balancer, see[Listing Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm).
- On the details page, select Listeners .
All listeners in the selected network load balancer are displayed in a table.
- Find the listener you want in the Listeners list.
The list contains columns for all the details of the listeners, such as IP protocol version, protocol, and port.
- 

Use the[oci nlb listener get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/listener/get.html)command and required parameters to get the details of a network load balancer's listener:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetListener](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/Listener/GetListener)
