# Adding a Load Balancer Backend Server
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_backend_server.htm
- Fetched: 2026-09-05 01:40 CDT

# Adding a Load Balancer Backend Server

Add a backend server to a load balancer.

For prerequisite information, see[Backend Servers for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendservers.htm).
Note  
  

If the load balancer has no backend sets, you must create one before you can specify a backend server. See[Creating a Load Balancer Backend Set](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets_topic-Creating_Backend_Sets.htm)for more information. To ensure reachability between the public load balancer and its public IP address based backends, configure a NAT Gateway. See[NAT Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/NATgateway.htm)for more information.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_backend_server.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_backend_server.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_backend_server.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Backend sets .
- Select Backends .
The Backends tab opens. All backend servers in the selected backend set are displayed in a table.
- Select Add backends .
You can't add a backend server marked as Backup to a backend set that uses the IP Hash policy.

From the Add backends panel, enter the following information:

Choose how to add backend servers : Specify how you want to add backend servers to the backend set:
- Compute Instances : Select this option to select from a list of available compute instances.
- Instances in &lt;compartment&gt; : Select the instances you want to include in the backend set.

To select instances from a different compartment, use the Change compartment link and select a compartment from the list. You can select instances from one compartment at a time. After you add instances from one compartment, you must repeat the Add backends process to add instances from another compartment.

After you select an instance to add to the backend set, you can specify:

Port : The backend server port to which the load balancer must direct traffic. Whether your backend server uses SSL (HTTPS) is determined by the backend set configuration.

Weight : The load balancing weight assigned to the server. For more information, see[Load Balancer Policies](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/../Reference/lbpolicies.htm).
- Select to manually configure subnet security list rules that allow the intended traffic or let the Load Balancer service create security list rules for you. To learn more about these rules, see[Parts of a Security Rule](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm#sec_rules_parts).

Manually configure security list rules after the load balancer is created : When you choose this option, you must[create your own rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm)after adding the backend servers.

Automatically add security list rules : When you select this option, the Load Balancer service creates security list rules for you. The system displays a table for egress rules and a table for ingress rules. Each table lets you select the security list that applies to the relevant subnet. You can then choose whether to apply the proposed rules for each affected subnet.
- IP addresses : Select this option to enter the IP addresses of the backend servers (Compute instances) to add.
- IP address : Specify the IP address of a backend server you want to add to the backend set.
- Port : Specify the server port to which the load balancer must direct traffic.
- Weight : Specify the load balancing weight to apply to this server. For more information, see[Load Balancer Policies](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/../Reference/lbpolicies.htm).

Select the plus + icon to add another server to the list.
- Select Add .
- 

Use the[oci lb backend create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/backend/create.html)command and required parameters to add a backend server to a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateBackend](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/Backend/CreateBackend)
