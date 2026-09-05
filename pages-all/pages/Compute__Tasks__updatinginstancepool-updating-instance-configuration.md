# Updating the Instance Configuration for an Instance Pool
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-updating-instance-configuration.htm
- Fetched: 2026-09-05 01:52 CDT

# Updating the Instance Configuration for an Instance Pool

Update the instance configuration that an instance pool uses when creating instances.

To update the instance configuration that an instance pool uses when creating instances,[create an instance configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm)with the appropriate settings (if such a configuration doesn't already exist), and then attach the new instance configuration to the pool, as described in this topic.

If you want the instances in the pool to use the settings from the new instance configuration, such as a new shape, then[detach the existing instances from the instance pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-detaching-an-instance-from-an-instance-pool.htm)and provision new instances.
Note  
  
When you detach instances from an instance pool, the existing instances are detached before new instances are provisioned. Depending on your requirements, you might want to increase the size of the instance pool before detaching instances.

If you only want to update the display name or tags of an existing instance configuration, then you can[update the pool's existing instance configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstanceconfig.htm). For any other updates, create an instance configuration and then attach it with the settings that you want to use.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-updating-instance-configuration.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-updating-instance-configuration.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-updating-instance-configuration.htm#)
- 

- Navigate to the Instance pools list page. If you need help finding the list page, see[Listing Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instance-pools-list.htm).
- Select the name of the instance pool that has the instance configuration you want to update to display the details page.
- Select Edit .
- For the Instance configuration , select an instance configuration to use when you create instances.
- Select Save .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/update.html)instance-pool update`command to update the instance configuration for an instance pool.

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[UpdateInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/UpdateInstancePool)
