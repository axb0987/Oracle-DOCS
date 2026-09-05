# Detaching an Instance from an Instance Pool
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-detaching-an-instance-from-an-instance-pool.htm
- Fetched: 2026-09-05 01:52 CDT

# Detaching an Instance from an Instance Pool

Detach an instance from an instance pool when you no longer want to manage the instance as part of the pool.

When you detach an instance from a pool, you can choose whether to delete the instance or to retain it. You can also choose whether to replace the detached instance by creating an instance in the pool. If you don't replace the detached instance, then the pool size decreases.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-detaching-an-instance-from-an-instance-pool.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-detaching-an-instance-from-an-instance-pool.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-detaching-an-instance-from-an-instance-pool.htm#)
- 

- Navigate to the Instance pools list page. If you need help finding the list page, see[Listing Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instance-pools-list.htm).
- Select the name of the instance pool from which you want to detach an instance to display the details page.
- Navigate to Attached instances using the option you see.
- From the Details tab, scroll down to Attached instances .
- In the Resources section, select Attached instances .
- For the instance that you want to detach, from the Actions menu (three dots) select Detach instance .
- Select Permanently terminate (delete) this instance and its attached boot volume to delete the instance and its boot volume.
- Select Replace the instance with a new instance, using the pool's instance configuration as a template for the instance . If you want the pool to remain the same size after you detach the instance, then you can provision a replacement instance.
- Select Detach (or Detach and terminate , if you're also deleting the instance).

Tip  
  
To track the progress of the operation and[troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instances.htm#instance-work-requests)that occur during instance creation, use the associated[work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
- 

Use the[instance-pool-instance detach](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool-instance/detach.html)command to detach an instance from an instance pool.

```

```

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[DetachInstancePoolInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePoolInstance/DetachInstancePoolInstance)
