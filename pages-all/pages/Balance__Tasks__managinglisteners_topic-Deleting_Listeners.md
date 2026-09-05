# Deleting a Load Balancer Listener
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Deleting_Listeners.htm
- Fetched: 2026-09-05 01:41 CDT

# Deleting a Load Balancer Listener

Remove a listener from a load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Deleting_Listeners.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Deleting_Listeners.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Deleting_Listeners.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Listeners .
- From the Actions menu for the listener, select Delete .
- When prompted, confirm the deletion.
- 

Use the[oci lb listener delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/listener/delete.html)command and required parameters to remove a listener from a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteListener](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/Listener/DeleteListener)
