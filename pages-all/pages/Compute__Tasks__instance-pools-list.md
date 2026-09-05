# Listing Instance Pools
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-list.htm
- Fetched: 2026-09-05 01:51 CDT

# Listing Instance Pools

Get a list of the instance pools in an Oracle Cloud Infrastructure compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-list.htm#)
- 

- 

Open the navigation menu and select Compute . Under Compute , select Instance Pools .

The Instance pools list page opens. All existing instance pools in the selected compartment are displayed in a list table.
- 

To view the resources in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

Optionally, you can do the following from the list.
- Select an instance pool to view the details page.
- For an instance pool, from the Actions menu (three dots) select start, reboot, or terminate an instance pool.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/list.html)instance-pool list`command and required parameters to list instance pools:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to list instance pools:
- [ListInstancePools](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePoolSummary/ListInstancePools)
