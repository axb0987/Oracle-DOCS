# Deleting Instance Pools
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/deletinginstancepool.htm
- Fetched: 2026-09-05 01:51 CDT

# Deleting Instance Pools

Permanently delete instance pools that you no longer need.
Important  
  
When you delete an instance pool, the resources that are associated with the pool are permanently deleted. Resources include instances created by the pool, instances that are attached to the pool, and attached boot volumes and block volumes created by the pool. Block volumes attached to instances after they were created are detached but not deleted.

If an autoscaling configuration applies to the instance pool, then the autoscaling configuration is deleted asynchronously after the pool is deleted. You can also[manually delete the autoscaling configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-delete-configuration_tabs.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/deletinginstancepool.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/deletinginstancepool.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/deletinginstancepool.htm#)
- 

- Navigate to the Instance pools list page. If you need help finding the list page, see[Listing Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instance-pools-list.htm).
- From the Actions menu (three dots) for the instance you want to delete, select Terminate .
- 

Confirm deletion when prompted.

To track the progress of the operation and[troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm#instance-work-requests)that might occur when deleting an instance pool, use the associated[work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/terminate.html)instance-pool terminate`command and required parameters to delete an instance pool:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to delete an instance pool:
- [TerminateInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/TerminateInstancePool)
