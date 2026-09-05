# Listing Autoscaling Configurations
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-listing-configurations_tabs.htm
- Fetched: 2026-09-05 01:50 CDT

# Listing Autoscaling Configurations

To list autoscaling configurations in a compartment, see the following steps.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-listing-configurations_tabs.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-listing-configurations_tabs.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-listing-configurations_tabs.htm#)
- 

- 

Open the navigation menu and select Compute . Under Compute , select Autoscaling Configurations .

The Autoscaling Configurations list page opens. All existing autoscaling configurations in the selected compartment are displayed in a list table.
- 

To view the resources in a different compartment, use the Compartment filter to switch compartments.
Note  
  
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

Optionally, you can do the following with an autoscaling configuration from the list.
- Select an autoscaling configuration to view the details page.
- From the Actions menu, edit, delete or move an autoscaling configuration.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/autoscaling/configuration/list.html)autoscaling configuration list`command and required parameters to list autoscaling configurations:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to list autoscaling configurations:
- [ListAutoScalingConfigurations](https://docs.oracle.com/iaas/api/#/en/autoscaling/latest/AutoScalingConfigurationSummary/ListAutoScalingConfigurations)
