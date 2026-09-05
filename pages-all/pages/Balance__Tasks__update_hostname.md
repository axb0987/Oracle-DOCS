# Editing a Load Balancer Virtual Hostname
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/update_hostname.htm
- Fetched: 2026-09-05 01:42 CDT

# Editing a Load Balancer Virtual Hostname

Update a virtual hostname's configuration for a load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/update_hostname.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/update_hostname.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/update_hostname.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Hostnames .
- From the Actions menu for the hostname, select Edit .
- Make your updates to the Hostname field. You can't edit the Name field of an existing virtual hostname.
- Select Save changes . The Work request submitted dialog box opens.
- To close the dialog box, select Close . To open the Work requests page and view the status of the work request, select View all work requests .
- 

Use the[oci lb hostname get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/hostname/get.html)command and required parameters to update a virtual hostname's configuration for a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateHostname](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/Hostname/UpdateHostname)
