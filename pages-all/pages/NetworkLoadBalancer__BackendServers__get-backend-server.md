# Getting Network Load Balancer Backend Server Details
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/get-backend-server.htm
- Fetched: 2026-09-05 02:48 CDT

# Getting Network Load Balancer Backend Server Details

View the details of a backend server for a network load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/get-backend-server.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/get-backend-server.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/get-backend-server.htm#)
- 

- On the Network load balancers list page, select the network load balancer that you want to work with. If you need help finding the list page or the network load balancer, see[Listing Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm).
- On the details page, select Backend sets .
All backend sets in the selected network load balancer are displayed in a table.
- On the details page for the backend set, select Backends .
All backend servers in the selected backend set are displayed in a table.
- Find the backend server you want in the Backends list.
The list contains columns for all the details of the backend servers, such as IP address, availability domain, and port.
- 

Use the[oci nlb backend get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/backend/get.html)command and required parameters to get the details of a network load balancer's backend server:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetBackend](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/Backend/GetBackend)
