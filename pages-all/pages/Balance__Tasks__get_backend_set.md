# Getting a Load Balancer Backend Set's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_backend_set.htm
- Fetched: 2026-09-05 01:40 CDT

# Getting a Load Balancer Backend Set's Details

View the details of a backend set for a load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_backend_set.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_backend_set.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_backend_set.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Backend sets .
The Backend sets tab opens. All backend sets in the selected load balancer are displayed in a table.
- Select the backend set that you want to work with.
The backend set's details page contains information about the backend set, both general information and links to its resources. Some items in the page are read-only, while other items let you edit and update the backend set's configuration.
- 

Use the[oci lb backend-set get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/backend-set/get.html)command and required parameters to view the details of a backend set for a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetBackendSet](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/BackendSet/GetBackendSet)
