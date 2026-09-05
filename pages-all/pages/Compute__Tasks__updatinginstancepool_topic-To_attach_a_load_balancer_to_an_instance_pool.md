# Attaching a Load Balancer to an Instance Pool
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool_topic-To_attach_a_load_balancer_to_an_instance_pool.htm
- Fetched: 2026-09-05 01:52 CDT

# Attaching a Load Balancer to an Instance Pool

Attach a load balancer or network load balancer to an instance pool.

If you choose to associate (attach) a load balancer or network load balancer with an instance pool, then when you add an instance to the instance pool, the instance is automatically added to the load balancer's or network load balancer's backend set . After the instance reaches a healthy state (the instance is listening on the configured port number), incoming traffic is automatically routed to the new instance. For background information about the Load Balancer service, see[Overview of Load Balancer](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool_topic-To_attach_a_load_balancer_to_an_instance_pool.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool_topic-To_attach_a_load_balancer_to_an_instance_pool.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool_topic-To_attach_a_load_balancer_to_an_instance_pool.htm#)
- 

Note  
  
You must have a load balancer or network load balancer and backend set to associate with the instance pool.
- Navigate to the Instance pools list page. If you need help finding the list page, see[Listing Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instance-pools-list.htm).
- Select the name of the instance pool to which you want to attach a load balancer or network load balancer to display the details page.
- Navigate to Load balancers using the option you see.
- From the Networking tab go to the Load Balancers section.
- In the Resources section select Load balancers .
- Select Attach a load balancer .
- Specify the load balancer type that you want to associate with the instance pool, and then enter the following values:
- Load balancer: The load balancer or network load balancer to associate with the instance pool.
- Backend set: The name of the backend set on the load balancer or network load balancer to add instances to.
- Port: The server port on the instances to which the load balancer or network load balancer must direct traffic. This value applies to all instances that use this load balancer or network load balancer attachment.
- VNIC: The VNIC to use when adding the instance to the backend set. Instances that belong to a backend set are also called backend servers. The private IP address is used. This value applies to all instances that use this load balancer or network load balancer attachment.
- To associate additional load balancers and network load balancers with the instance pool, click + Another load balancer and repeat the previous steps.
- Select Attach .
- 

Use the[instance-pool attach-lb](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/attach-lb.html)command to attach a load balancer to an instance pool.

```

```

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[AttachLoadBalancer](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/AttachLoadBalancer)
