# Adding a Network Load Balancer Backend Server
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/create-backend-server.htm
- Fetched: 2026-09-05 02:48 CDT

# Adding a Network Load Balancer Backend Server

Add a backend server that receives incoming traffic to a network load balancer.

For prerequisite information, see[Backend Servers for Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/backend-server-management.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/create-backend-server.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/create-backend-server.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/create-backend-server.htm#)
- 

- On the Network load balancers list page, select the network load balancer that you want to work with. If you need help finding the list page or the network load balancer, see[Listing Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm).
- On the details page, select Backend sets .
All backend sets in the selected network load balancer are displayed in a table.
- On the details page for the backend set, select Backends .
- Select Add backends .
- From the Add backends panel, enter the following information:

- Backend type : Select one of the following options:
- Compute instances : Enter the following information under Backend :
- Instance compartment : Select the compartment containing the compute instance you want to use for the backend server from the list.
- Instance : Select the compute instance you want for the backend server from the list.
- IP address : Select the IP address for the backend server from the list.
- Availability domain : This value is automatically assigned based on the instance you selected.
- Port : Enter the communication port for the backend server. Sometimes the port value is fixed as "Any."
- Weight : (Optional) Enter the load balancing policy weight number assigned to the server. Backend servers with a greater weight receive a larger proportion of incoming traffic.

Select Add another backend to configure another backend server of the same type (Compute instance).
- IP address : Enter the following information under Backend :
- IP address : Enter the IP address of the backend server.
- Port : Enter the communication port for the backend server. Sometimes the port value is fixed as "Any."
- Weight : (Optional) Enter the load balancing policy weight number assigned to the server. Backend servers with a greater weight receive a larger proportion of incoming traffic.
Note  
  
Preserve source IP must be disabled in the backend set to add an IP address-based backend server.

Select Add another backend to configure another backend server of the same type (Compute instance).
- Select Add more backends to add another backend.
- Select Add backends .
The backend server you added appears in the backend list of the backend set.
- 

Use the[oci nlb backend create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/backend/create.html)command and required parameters to add a backend server to a network load balancer:

```

```

where`backend_server_name`is an optional unique name for the backend server. If you don't include a name when creating the backend server, Network Load Balancer generates a name automatically.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateBackend](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/Backend/CreateBackend)
