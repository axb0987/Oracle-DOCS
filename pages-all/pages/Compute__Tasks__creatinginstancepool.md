# Creating Instance Pools
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstancepool.htm
- Fetched: 2026-09-05 01:50 CDT

# Creating Instance Pools

Use instance pools to create and manage multiple compute instances within the same region as a group.

When you create an instance pool, you use an[instance configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm)as the template to create instances in the pool. You can also[attach existing instances to a pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-attaching-an-instance-to-an-instance-pool.htm)by updating the pool.

Optionally, you can associate one or more[load balancers](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm)and[network load balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/overview.htm)with an instance pool. If you do this, when you add an instance to the instance pool, the instance is automatically added to the load balancer's or network load balancer's backend set . After the instance reaches a healthy state (the instance is listening on the configured port number), incoming traffic is automatically routed to the new instance.

To determine whether capacity is available for a specific shape before you create an instance pool, use the[CreateComputeCapacityReport](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReport/CreateComputeCapacityReport)API operation.

## Before You Begin

Before you can create an instance pool, you need:
- 

An instance configuration. An instance configuration is a template that defines the settings to use when creating instances. When you create the instance pool,[monitoring is enabled](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm)by default on instances that support monitoring, regardless of the settings in the instance configuration. For more information, see[Creating an Instance Configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm).
Note  
  
You cannot create an instance pool from an instance configuration where the image source is a boot volume.
- If you want to associate the instance pool with a load balancer or network load balancer, you need a load balancer or network load balancer and backend set. For steps to create a load balancer, see[Load Balancer Management](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingloadbalancer.htm). For steps to create a network load balancer, see[Network Load Balancer Management](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/network-load-balancer-management.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstancepool.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstancepool.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstancepool.htm#)
- 

To create an instance pool:
- Navigate to the Instance pools list page. If you need help finding the list page, see[Listing Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instance-pools-list.htm).
- 

Select Create instance pool .

## 1. Add basic details

Fill out the information depending on the form that you see:

Option 1
- Name : Enter a name for the instance pool. The name doesn't have to be unique. You can change it later. Avoid entering confidential information.
- Number of instances : Specify the target number of instances.
- Compartment : Select the compartment to create the instance pool in.
- Instance configuration : Select an instance configuration.
- (Optional) Formatter options : Customize instance display name and instance host name for instances you create in the pool.
- Use the Instance display name formatter field to customize the display name of an instance that you create for this pool. Enter a text string that includes lowercase alphanumeric characters, symbols, and dashes. The string must also include the`${launchCount}`token. For example:`my-string-${launchCount}`.
- Use the Instance host name formatter field to enter a text string that includes lowercase alphanumeric characters, symbols, and dashes. The string must also include the`${launchCount}`token. For example:`my-string-${launchCount}`.
- (Optional) Tags : Add tags for the instance pool.

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Next .

Option 2
- Name : Enter a name for the instance pool. The name doesn't have to be unique. You can change it later. Avoid entering confidential information.
- Compartment : Select the compartment to create the instance pool in.
- Instance configuration : Select an instance configuration.
- Number of instances : Specify the target number of instances.
- Select Advanced options to display tagging and instance display and host name formatter options.
- (Optional) Formatter options : Customize instance display name and instance host name for instances you create in the pool.
- Use the Instance display name formatter field to customize the display name of an instance that you create for this pool. Enter a text string that includes lowercase alphanumeric characters, symbols, and dashes. The string must also include the`${launchCount}`token. For example:`my-string-${launchCount}`.
- Use the Instance host name formatter field to enter a text string that includes lowercase alphanumeric characters, symbols, and dashes. The string must also include the`${launchCount}`token. For example:`my-string-${launchCount}`.
- (Optional) Tags : Add tags for the instance pool.

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Next .

## 2. Configure pool placement

Fill out the information in the form.
- Availability domain : Select the availability domain to create the instances in.
- 

Fault domains : Perform one of the following actions:
- If you want the system to make a best effort to distribute instances across fault domains based on capacity, then leave the field empty.
- To require that the instances in the pool are distributed evenly in one or more fault domains, select the fault domains to place the instances in. If sufficient capacity is unavailable in the selected fault domains, then the pool won't launch or scale successfully. For more information, see[Distributing Instances Across Fault Domains for High Availability](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Concepts/instance-pools.htm#instance-pools-fault-domains).
- 

Primary VNIC :
- Virtual cloud network: Select the virtual cloud network (VCN) to create the instances in. Change the compartment if needed.
- Subnet: Select a subnet within the cloud network to attach the instances to. Change the compartment if needed. The subnets are either public or private. Private means the instances in that subnet can't have public IP addresses. For more information, see[Access to the Internet](https://docs.oracle.com/iaas/Content/Network/Concepts/internetaccess.htm). Subnets are either specific to an availability domain or regional (regional ones have "regional" after the name). We recommend using[regional subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs_topic-Overview_of_VCNs_and_Subnets.htm#Overview__regional_subnet).

For more information about the settings in this section, see[Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm).
Note  
  
If secondary VNICs are defined by the instance configuration, then a Secondary VNIC section appears. Select the secondary VCN and subnet for the instance pool.

Primary VNIC IP addresses : Select the public and private IP addresses for this pool. For more information about the settings in this section, see[Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm).
- + Another availability domain : If you want the instance pool to create instances in more than one availability domain, then select this option. Then, repeat the previous steps.
- 

(Optional) Attach a load balancer : To associate a load balancer or network load balancer with the instance pool, select the check box:
- 

Load Balancer type : Specify the type of load balancer.

For more information, see[Overview of Load Balancer](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm)or[Overview of Flexible Network Load Balancer](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/overview.htm).
- Compartment : Select the load balancer compartment.
- Load balancer : Select the load balancer from the Load Balancer list.

The choices available in the list are determined by the load balancer type, compartment, and available load balancers.
- Backend set : Select the backend set on the load balancer or network load balancer to add instances to.
- Port : Enter the server port on the instances to which the load balancer or network load balancer must direct traffic. This value applies to all instances that use this load balancer or network load balancer attachment.
- Load balancer port values range from 1 to 65535.
- Network load balancer ports range from 1 to 65535 when the load balancer is configured for a specific port. If the network load balancer is configured for all ports, then the value in the Port field defaults to Any and cannot be changed.
- VNIC : Select the VNIC to use when adding the instance to the backend set. Instances that belong to a backend set are also called backend servers. The private IP address is used. This value applies to all instances that use this load balancer or network load balancer attachment.
- + Another load balancer : To associate additional load balancers and network load balancers with the instance pool, then select this option and repeat the previous steps.

For background information about load balancers, see[Overview of Load Balancer](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm).
- Select Next .

## 3. Review

Review the instance pool details, and then select Submit or Create .

Tip  
  
To track the progress of the operation and[troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instances.htm#instance-work-requests)that occur during instance creation, use the associated[work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
- 

To create an instance pool, use the[instance-pool create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/create.html)command:

```

```

To specify the CLI options using JSON:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to create an instance pool:
- [CreateInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/CreateInstancePool)
