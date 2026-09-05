# Enabling Network Load Balancer Backend Set Source Preservation
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/preserve-backend-set-source-id.htm
- Fetched: 2026-09-05 02:48 CDT

# Enabling Network Load Balancer Backend Set Source Preservation

Configure your network load balancer's backend set so that the original source IP of the packet is preserved when it's forwarded to the member backend servers.

These instructions are for enabling the source preservation feature in an existing network load balancer backend set. You can enable this feature when you first create the backend set. For more information, see[Creating a Backend Set](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/create-backend-set.htm).
Note  
  
If you selected L3 IP for your listener traffic type, the Preserve Source IP option is automatically enabled. You can't disable it.

If you enable this option, the network load balancer preserves the source IP of the packet when it's forwarded to backend servers that are members of the configured backend set. Backend servers see the original source IP. If source/destination preservation is enabled for the network load balancer (see[Enabling Network Load Balancer Backend Set Source Preservation](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/preserve-backend-set-source-id.htm)), then this parameter can't be disabled. The value is true by default. No network address translation (NAT) occurs on the source IP and port.

If enabled, the compute instance selects the backend servers. Otherwise, you can add the backend servers using IP addresses.
Note  
  

There can be about 21,500 active connections to the backend server listener port per availability domain (AD) when source preservation isn't enabled in the backend set configuration. If incoming connections from all the ADs are distributed evenly, the number of active connections per backend server listener port in a three-AD region can reach 64,500.

You can either add more listeners or add more backend servers into the existing backend set for the same listener port to scale the number of active connections per network load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/preserve-backend-set-source-id.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/preserve-backend-set-source-id.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/preserve-backend-set-source-id.htm#)
- 

- On the Network load balancers list page, select the network load balancer that you want to work with. If you need help finding the list page or the network load balancer, see[Listing Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm).
- On the details page, select Backend sets .
All backend sets in the selected network load balancer are displayed in a table.
- From the Actions menu for the backend set you want, select Edit .
- In the Edit Backend set dialog box, select Preserve source IP to preserve the header information (IP addresses and ports) of incoming packets all the way to the backend server. Clear to disable this feature.
- Select Save changes .
- 

Use the`--is-preserve-source true`option when running the[oci nlb backend-set create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/backend-set/create.html)or[oci nlb backend-set update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/backend-set/update.html)commands to create or update a network load balancer's backend set, respectively, to preserve the source IP:

```

```

or

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Include the`isPreserveSource=true`option when creating or updating a network load balancer's backend set to preserve the source IP. See[CreateBackendSet](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/BackendSet/CreateBackendSet)or[UpdateBackendSet](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/BackendSet/UpdateBackendSet)
