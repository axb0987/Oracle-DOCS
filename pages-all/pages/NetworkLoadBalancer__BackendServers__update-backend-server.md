# Editing a Network Load Balancer Backend Server
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/update-backend-server.htm
- Fetched: 2026-09-05 02:48 CDT

# Editing a Network Load Balancer Backend Server

Update backend server's configuration for a network load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/update-backend-server.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/update-backend-server.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/update-backend-server.htm#)
- 

- On the Network load balancers list page, select the network load balancer that you want to work with. If you need help finding the list page or the network load balancer, see[Listing Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm).
- On the details page, select Backend sets .
All backend sets in the selected network load balancer are displayed in a table.
- On the details page for the backend set, select Backends .
All backend servers in the selected backend set are displayed in a table.
- On the details page for the backend set, select Backends .
- In the Backends section, select the backend server and select Edit .
You can select several backend servers and update them all at the same time.
- Update the settings as needed. Avoid entering confidential information.

- Weight : Change the load balancing policy weight number assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic.
- Drain : If you set the server's drain status to True , the network load balancer stops forwarding new TCP connections and new non-sticky HTTP requests to this backend server. This setting lets administrators take the server out of rotation for maintenance purposes.
- Offline : If you set the server's offline status to True , the network load balance forwards no ingress traffic to this backend server.
- Backup : If you set the server's backup status to True , the network load balancer forwards ingress traffic to this backend server only when all other backend servers not marked as backup fail the health check policy. This configuration is useful for handling disaster recovery scenarios.
- Select Save changes .
- 

Use the[oci nlb backend update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/backend/update.html)command and required parameters to edit a network load balancer's backend server:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateBackend](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/Backend/UpdateBackend)
