# Deleting Autoscaling Configurations
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-delete-configuration_tabs.htm
- Fetched: 2026-09-05 01:50 CDT

# Deleting Autoscaling Configurations

Complete the following steps to delete an autoscaling configuration.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-delete-configuration_tabs.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-delete-configuration_tabs.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-delete-configuration_tabs.htm#)
- 

Navigate to the Autoscaling configurations list page. If you need help finding the list page, see[Listing Autoscaling Configurations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/autoscaling-listing-configurations_tabs.htm).
- From the Actions menu (three dots) for your target configuration, select Delete .
- Select Delete again to confirm.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/autoscaling/configuration/delete.html)autoscaling configuration delete`command and required parameters to delete an autoscaling configuration:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to delete an autoscaling configuration:
- [DeleteAutoScalingConfiguration](https://docs.oracle.com/iaas/api/#/en/autoscaling/latest/AutoScalingConfiguration/DeleteAutoScalingConfiguration)
