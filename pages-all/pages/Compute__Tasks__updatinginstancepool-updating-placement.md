# Updating Instance Placement in an Instance Pool
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-updating-placement.htm
- Fetched: 2026-09-05 01:52 CDT

# Updating Instance Placement in an Instance Pool

Update the location where the instances in an instance pool are placed. The placement includes the availability domains, fault domains, and subnets for the instances in the instance pool.
Important  
  
When you remove an availability domain from an instance pool, the pool permanently deletes all of its instances in that availability domain. The pool replaces the instances with new instances in the availability domains that are still associated with the pool.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-updating-placement.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-updating-placement.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-updating-placement.htm#)
- 

- Navigate to the Instance pools list page.If you need help finding the list page, see[Listing Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instance-pools-list.htm).
- Select the name of the instance pool that you want to update to display the details page.
- Select Edit .
- Navigate to Availability domains to create the instances in.
- Availability domain : Select the availability domain you want to create instances in.
- Fault domains : Do one of the following actions:
- If you want the system to make a best effort to distribute instances across fault domains based on capacity, then leave the field empty.
- If you want to require that the instances in the pool are distributed evenly in one or more fault domains, then select the fault domains to place the instances in. If sufficient capacity is unavailable in the selected fault domains, then the pool won't launch or scale successfully. For more information, see[Distributing Instances Across Fault Domains for High Availability](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Concepts/instance-pools.htm#instance-pools-fault-domains).
- In the Primary VNIC section, configure the following network details for the instances:
- Virtual cloud network : The virtual cloud network (VCN) to create the instances in.
- Subnet : A subnet within the VCN to attach the instances to. The subnets are either public or private. Private means the instances in that subnet can't have public IP addresses. For more information, see[Access to the Internet](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#Private). Subnets are either specific to an availability domain or regional (regional subnets have "regional" after the name). We recommend using[regional subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm#Overview__regional_subnet).
- If secondary VNICs are defined by the instance configuration, then in the Secondary VNIC section, select the secondary VCN and subnet for the instance pool.
- (Optional) If you want the instance pool to create instances in more than one availability domain, then select + Another availability domain and repeat the previous steps.
- (Optional) If you no longer want the instance pool to contain instances in a specific availability domain, then select the X next to the availability domain that you want to remove.
Important  
  
Any existing instances in that availability domain are deleted and replaced with new instances in an availability domain that is still associated with the pool.
- Select Save .
- 

Use the[instance-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/update.html)command to update the placement for an instance pool.

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[UpdateInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/UpdateInstancePool)
