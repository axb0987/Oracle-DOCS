# Getting a Load Balancer Backend Set's Health Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_backend-set-health.htm
- Fetched: 2026-09-05 01:40 CDT

# Getting a Load Balancer Backend Set's Health Details

View the health status details of a backend set for a load balancer.

## Health Details

Here are the health levels and their descriptions:
- 

Critical (red): Fewer than half of the backend set's backend servers return a status of OK .
- 

Warning (yellow): Both of the following conditions are true:
- 

Half or more of the backend set's backend servers return a status of OK .
- 

At least one backend server returns a status of Warning , Critical , Pending , or Incomplete .
- 

Incomplete (yellow): The backend set does not have any backends attached.
- 

Pending (yellow): At least one of the following conditions is true:
- 

More than half of the backend set's backend servers return a status of Pending .
- 

The system could not retrieve metrics for any reason.
- 

OK (green): All backend servers in the backend set return a status of OK .

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_backend-set-health.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_backend-set-health.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_backend-set-health.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Backend sets .
The Backend sets tab opens. All backend sets in the selected load balancer are displayed in a table.
- Select the backend set that you want to work with.
- On the backend set's details page, view the Overall and Backend health details.
- 

Use the[oci lb backend-set-health get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/backend-set-health/get.html)command and required parameters to view the health status details of a backend set for a load balancer:

```

```

See the CLI online help for a list of options:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetBackendSetHealth](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/BackendSetHealth/GetBackendSetHealth)
