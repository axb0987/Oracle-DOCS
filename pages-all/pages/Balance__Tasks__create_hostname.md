# Creating a Load Balancer Virtual Hostname
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_hostname.htm
- Fetched: 2026-09-05 01:40 CDT

# Creating a Load Balancer Virtual Hostname

Create a virtual hostname for a load balancer.

For prerequisite information, see[Virtual Hostnames for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/hostname_management.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_hostname.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_hostname.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_hostname.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Hostnames .
- In the Hostnames section, select Create hostname .
- Enter the following information:

- Name : Enter a friendly name for the hostname. The name must be unique, and can't be changed.
- Hostname : Specify the virtual hostname. See[Virtual Hostnames](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/hostname_management.htm)for more information.
- Select Create .
The Work request submitted panel opens.
- (Optional) Select View all work requests to open the Work requests page and view the status of the work request.
- Select Close .
- 

Use the[oci lb hostname create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/hostname/create.html)command and required parameters to create a virtual hostname for a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateHostname](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/Hostname/CreateHostname)
