# Deleting a Network Load Balancer Listener
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/delete-listener.htm
- Fetched: 2026-09-05 02:48 CDT

# Deleting a Network Load Balancer Listener

Remove a listener from a network load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/delete-listener.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/delete-listener.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/delete-listener.htm#)
- 

- On the Network load balancers list page, select the network load balancer that you want to work with. If you need help finding the list page or the network load balancer, see[Listing Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm).
- On the details page, select Listeners .
All listeners in the selected network load balancer are displayed in a table.
- Find the listener you want in the Listeners list.
- From the Actions menu for the listener you want, select Delete .
- When prompted, confirm the deletion.
- 

Use the[oci nlb listener delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/listener/delete.html)command and required parameters to delete a listener from a network load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteListener](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/Listener/DeleteListener)
