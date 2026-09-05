# Editing a Load Balancer Listener
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Editing_Listeners.htm
- Fetched: 2026-09-05 01:41 CDT

# Editing a Load Balancer Listener

Update a listener's configuration for a load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Editing_Listeners.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Editing_Listeners.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Editing_Listeners.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Listeners .
- From the Actions menu for the listener, select Edit .
- From the Edit listener panel, update the settings as needed. For descriptions of the settings, see[Creating a Listener](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Creating_Listeners.htm).
- Select Save changes .
- 

Use the[oci lb listener update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/listener/update.html)command and required parameters to update a listener's configuration for a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateListener](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/Listener/UpdateListener)
