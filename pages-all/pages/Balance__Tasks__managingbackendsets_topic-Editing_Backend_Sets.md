# Editing a Load Balancer's Backend Set
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets_topic-Editing_Backend_Sets.htm
- Fetched: 2026-09-05 01:41 CDT

# Editing a Load Balancer's Backend Set

Update the configuration of a backend set for a load balancer.

When you edit a backed set, you can select a new load balancing policy and change the SSL configuration. To change the backend set's health check policy, see[Health Check Policies for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/load_balancer_health_management.htm)for more information.

To add or remove backend servers from the backend set, see[Backend Servers for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendservers.htm)for more information.
Note  
  
Changing the load balancing policy of a backend set temporarily interrupts traffic and can drop active connections.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets_topic-Editing_Backend_Sets.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets_topic-Editing_Backend_Sets.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets_topic-Editing_Backend_Sets.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Backend sets .
The Backend sets tab opens. All backend sets in the selected load balancer are displayed in a table.
- From the Actions menu for the backend set, select Edit .
- Edit any of the following:

- Traffic distribution policy
- SSL
- Session persistence
- Max Backend Connections

See[Creating a Backend Set](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets_topic-Creating_Backend_Sets.htm)for more information.
- Select Update backend set .
- 

Use the[oci lb backend-set update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/backend-set/update.html)command and required parameters to update the configuration of a backend set for a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateBackendSet](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/BackendSet/UpdateBackendSet)
