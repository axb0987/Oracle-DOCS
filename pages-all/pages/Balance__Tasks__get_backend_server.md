# Getting a Load Balancer Backend Server's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_backend_server.htm
- Fetched: 2026-09-05 01:40 CDT

# Getting a Load Balancer Backend Server's Details

View the details of a backend server for a load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_backend_server.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_backend_server.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_backend_server.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Backend sets .
- Select Backends .
The Backends tab opens. All backend servers in the selected backend set are displayed in a table.
The Backends list show details for all the backend servers associated with the backend set, such as IP status, port, and weight.
- 

Use the[oci lb backend get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/backend/get.html)command and required parameters to view the details of a backend server for a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetBackend](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/Backend/GetBackend)
