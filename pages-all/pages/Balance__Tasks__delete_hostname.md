# Deleting a Load Balancer Virtual Hostname
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_hostname.htm
- Fetched: 2026-09-05 01:40 CDT

# Deleting a Load Balancer Virtual Hostname

Remove a hostname from a load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_hostname.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_hostname.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_hostname.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Hostnames .
- From the Actions menu for the hostname, select Delete .
- When prompted, confirm the deletion.
- 

Use the[oci lb hostname delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/hostname/delete.html)command and required parameters to remove a hostname from a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteHostname](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/Hostname/DeleteHostname)
