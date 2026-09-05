# Deleting a Load Balancer's Backend Set
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets_topic-Deleting_Backend_Sets.htm
- Fetched: 2026-09-05 01:41 CDT

# Deleting a Load Balancer's Backend Set

Remove a backend set from a load balancer.
Note  
  
You can't delete a backend set used by an active listener.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets_topic-Deleting_Backend_Sets.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets_topic-Deleting_Backend_Sets.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets_topic-Deleting_Backend_Sets.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Backend sets .
The Backend sets tab opens. All backend sets in the selected load balancer are displayed in a table.
- From the Actions menu for the backend set, select Delete .
- When prompted, confirm the deletion.
- 

Use the[oci lb backend-set delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/backend-set/delete.html)command and required parameters to remove a backend set from a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteBackendSet](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/BackendSet/DeleteBackendSet)
