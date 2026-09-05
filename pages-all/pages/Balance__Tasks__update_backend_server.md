# Editing a Load Balancer's Backend Server
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/update_backend_server.htm
- Fetched: 2026-09-05 01:42 CDT

# Editing a Load Balancer's Backend Server

Update a backend server for a load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/update_backend_server.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/update_backend_server.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/update_backend_server.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Backend sets .
- Select Backends .
The Backends tab opens. All backend servers in the selected backend set are displayed in a table.
- From the Actions menu for the backend server, select Edit backend .

To apply the same edit to several backend servers listed, select each one and then select Edit settings on selected backends from the Action menu above the list, next to the Add backends button. You can select several servers to apply the same action to each one.
- From the Edit backend panel, edit to any of the following:

- Port : Opens a dialog box in which you can change the application port setting. Ensure your backend set's health check port matches the backend server's port number.
- Weight : Change the load balancing weight.
- Drain backends : Select True to disable new connections. The load balancer stops forwarding new TCP connections and new non-sticky HTTP requests to this backend server. This setting allows you to take the server out of rotation for maintenance purposes.
- Set backends to offline mode : Select True to prevent the load balance from forwarding ingress traffic to this backend server.
- Set backends to be a backup : Select True to set the backend server as a backup unit. The load balancer forwards ingress traffic to the backend server only when all other backend servers not marked as "backup" fail the[health check policy](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/../Concepts/balanceoverview_topic-Load_Balancing_Concepts.htm). This configuration is useful for handling disaster recovery scenarios. Backend servers marked as Backup aren't compatible with a load balancer that uses the IP Hash policy.
- Max backend connections : Enable Set Limit and specify the uniform maximum listener connection value for the backend server, and also create overrides to the uniform value for one or more specified IPs. The minimum value is 256. The maximum is 65535.
- Select Save changes .
- 

Use the[oci lb backend get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/backend/get.html)command and required parameters to edit a load balancer's backend server:

```

```

The`backup`parameter indicates whether (`true`) or not (`false`) the load balancer treats this server as a backup unit. If the value is`true`, the load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as "backup" fail the health check policy. You cannot add a backend server marked as`backup`to a backend set that uses the IP Hash policy.

The`drain`parameter indicates whether (`true`) or not (`false`) the load balancer drains this backend server. If the value is`true`, the backend server receives no new incoming traffic.

The`weight`parameter indicates the load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives three times the number of new connections as a server weighted '1.' For more information on load balancing policies, see[How Load Balancing Policies Work](https://docs.oracle.com/iaas/Content/Balance/Reference/lbpolicies.htm).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateBackend](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/Backend/UpdateBackend)
