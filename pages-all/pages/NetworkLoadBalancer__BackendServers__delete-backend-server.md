# Deleting a Network Load Balancer Backend Server
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/delete-backend-server.htm
- Fetched: 2026-09-05 02:48 CDT

# Deleting a Network Load Balancer Backend Server

Remove a backend server from a network load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/delete-backend-server.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/delete-backend-server.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/delete-backend-server.htm#)
- 

- On the Network load balancers list page, select the network load balancer that you want to work with. If you need help finding the list page or the network load balancer, see[Listing Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm).
- On the details page, select Backend sets .
All backend sets in the selected network load balancer are displayed in a table.
- On the details page for the backend set, select Backends .
All backend servers in the selected backend set are displayed in a table.
- On the details page for the backend set, select Backends .
- In the Backends section, select the backend server that you want the to delete in the list and select Delete .
You can select several backend servers and delete them all at the same time.
- When prompted, confirm the deletion.
- 

Use the[oci nlb backend delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/backend/delete.html)command and required parameters to delete the backend server from a network load balancer's backend set:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteBackend](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/Backend/DeleteBackend)
