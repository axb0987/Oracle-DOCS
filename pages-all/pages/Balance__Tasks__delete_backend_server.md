# Deleting a Load Balancer's Backend Server
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_backend_server.htm
- Fetched: 2026-09-05 01:40 CDT

# Deleting a Load Balancer's Backend Server

Remove a backend server from a load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_backend_server.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_backend_server.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_backend_server.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Backend sets .
- Select Backends .
The Backends tab opens. All backend servers in the selected backend set are displayed in a table.
- From the Actions menu for the backend server, select Delete .
You can select several servers to delete them in bulk. Select Delete from the Actions menu above the Backends list.
- When prompted, confirm the deletion.
- 

Use the[oci lb backend delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/backend/delete.html)command and required parameters to delete a backend server from a load balancer's backend set:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteBackend](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/Backend/DeleteBackend)
