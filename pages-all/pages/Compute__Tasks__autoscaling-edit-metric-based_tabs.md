# Editing a Metric-based Autoscaling Configuration
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-edit-metric-based_tabs.htm
- Fetched: 2026-09-05 01:50 CDT

# Editing a Metric-based Autoscaling Configuration

To edit a metric-based autoscaling configuration, see the following steps.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-edit-metric-based_tabs.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-edit-metric-based_tabs.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-edit-metric-based_tabs.htm#)
- 

Navigate to the Autoscaling configurations list page. If you need help finding the list page, see[Listing Autoscaling Configurations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/autoscaling-listing-configurations_tabs.htm).

## Edit name and cooldown

- Select an autoscaling configuration.
- Select Edit . You can edit Name and Cooldown in seconds .
- Select Update to save changes.

## Edit autoscaling policies

To edit autoscaling policies for this configuration:
- Select an autoscaling configuration.
- Select the Autoscaling polices tab.
- From the Actions menu (three dots) for the policy select Edit .
- Make your updates. Avoid entering confidential information.

See[Creating a Metric-based Autoscaling Configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-create-metric-based_tabs.htm)for a list of fields.
- Select Update to save changes.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/autoscaling/configuration/update.html)autoscaling configuration update`command and required parameters to edit an autoscaling configuration:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to edit an autoscaling configuration:
- [UpdateAutoScalingConfiguration](https://docs.oracle.com/iaas/api/#/en/autoscaling/latest/AutoScalingConfiguration/UpdateAutoScalingConfiguration)
