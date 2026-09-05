# Detaching a Load Balancer from an Instance Pool
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool_topic-To_detach_a_load_balancer_from_an_instance_pool.htm
- Fetched: 2026-09-05 01:52 CDT

# Detaching a Load Balancer from an Instance Pool

Detach a load balancer or network load balancer from an instance pool.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool_topic-To_detach_a_load_balancer_from_an_instance_pool.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool_topic-To_detach_a_load_balancer_from_an_instance_pool.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool_topic-To_detach_a_load_balancer_from_an_instance_pool.htm#)
- 

- Navigate to the Instance pools list page. If you need help finding the list page, see[Listing Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instance-pools-list.htm).
- Select the name of the instance pool from which you want to detach a load balancer or network load balancer to display the details page.
- Navigate to Load balancers select the option you see.
- From the Networking tab go to the Load Balancers section.
- In the Resources section, select Load balancers .
- From the Actions menu (three dots) for the load balancer or network load balancer you want to detach and then select Detach load balancer .
- Select Detach to confirm.
Note  
  
To track the progress of the operation and[troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm#instance-work-requests)that might occur, use the associated[work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
- 

Use the[instance-pool detach-lb](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/detach-lb.html)command to detach a load balancer from an instance pool.

```

```

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[DetachLoadBalancer](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/DetachLoadBalancer)
