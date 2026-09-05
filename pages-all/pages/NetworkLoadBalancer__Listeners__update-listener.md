# Editing a Network Load Balancer Listener
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/update-listener.htm
- Fetched: 2026-09-05 02:48 CDT

# Editing a Network Load Balancer Listener

Update a listener's configuration for a network load balancer.
Note  
  
If you selected L3 IP as the listener traffic type, the backend set you select must have the preserve source ID feature enabled. Only those backend sets with that feature enabled are available to select from the Backend set list.

- [Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/update-listener.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/update-listener.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/update-listener.htm#)
- 

- On the Network load balancers list page, select the network load balancer that you want to work with. If you need help finding the list page or the network load balancer, see[Listing Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm).
- On the details page, select Listeners .
All listeners in the selected network load balancer are displayed in a table.
- Find the listener you want in the Listeners list.
- From the Actions menu for the listener you want, select Edit .
- Update the settings as needed. Avoid entering confidential information. For descriptions of the settings, see[Creating a Listener](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/create-listener.htm).

Note  
  
If you selected L3 IP as the listener traffic type, the backend set you select must have the preserve source ID feature enabled. Only those backend sets with that feature enabled are available to select from the Backend set list.
- Select Save changes .
- 

Use the[oci nlb listener update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/listener/update.html)command and required parameters to edit a network load balancer's listener:

```

```

See[Changing a Listener's Idle Timeout](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/../NetworkLoadBalancers/configure-idle-timeout.htm)to change the default idle timeout settings for UDP and TCP listeners.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateListener](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/Listener/UpdateListener)
