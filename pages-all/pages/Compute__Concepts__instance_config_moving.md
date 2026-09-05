# Moving an Instance Configuration
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/instance_config_moving.htm
- Fetched: 2026-09-05 01:49 CDT

# Moving an Instance Configuration

Move a Compute instance configuration from one compartment to another compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/instance_config_moving.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/instance_config_moving.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/instance_config_moving.htm#)
- 

- Navigate to the Instance Configurations list page. Select an instance configuration to view its details page. If you need help finding the list page, see[Listing Instance Configurations](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Tasks/list-instance-configurations.htm).
- In the details page, select one of the following options based on what you see:
- Select Actions and then Move resource .
- Select Move Resource .
- Select the destination compartment from the list.
- Select Move Resource .

Tip  
  
If alarms are monitoring the instance configuration, update the alarms to reference the new compartment. See[Updating an Alarm After Moving a Resource](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-after-resource-move.htm)for more information.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-configuration/change-compartment.html)instance configuration change compartment`command and required parameters to move an instance configuration to another compartment:

```

```

Or use a JSON file to set parameters:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[ChangeInstanceConfigurationCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceConfiguration/ChangeInstanceConfigurationCompartment)
