# Creating a Metric-based Autoscaling Configuration
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-create-metric-based_tabs.htm
- Fetched: 2026-09-05 01:50 CDT

# Creating a Metric-based Autoscaling Configuration

To create a metric-based autoscaling configuration, see the following steps.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-create-metric-based_tabs.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-create-metric-based_tabs.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-create-metric-based_tabs.htm#)
- 

Navigate to the Autoscaling configurations list page. If you need help finding the list page, see[Listing Autoscaling Configurations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/autoscaling-listing-configurations_tabs.htm).

Select Create autoscaling configuration .

## 1. Add basic details

On the Add basic details page, do the following:
- Enter a name for the autoscaling configuration. Avoid entering confidential information.
- Select the compartment to create the autoscaling configuration in.
- Select the compartment for the instance pool.
- Select the Instance pool to apply the autoscaling configuration to.
- Tags: If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Next .

## 2. Create autoscaling configuration

On the Configure autoscaling policy page, select Metric-based autoscaling . Then, enter the required information.
Tip  
  
Toggle Instance pool information to see the instance pool details.

Configure autoscaling policy
- Autoscaling policy name: Enter a name for the autoscaling policy. Avoid entering confidential information.
- Cooldown in seconds: In the Cooldown in seconds box, enter the minimum amount of time to wait between scaling events. The cooldown period gives the system time to stabilize before rescaling. The minimum value is 300 seconds, which is also the default.
- Performance metric: Select the Performance metric that triggers an increase or decrease in the number of instances in the instance pool.

Scale-out rule

In the Scale-out rule area, specify the threshold that the performance metric must reach to increase the pool size.
- Scale-out operator: Select a Scale-out operator , for example`>`or`>=`.
- Scale-out threshold percentage: The threshold at which the number of instances in the instance pool increase.
- Number of instances to add: The number of instances to add to the pool.

For example, when CPU utilization is greater than 90%, add 10 instances to the pool.

Scale-in rule

In the Scale-in rule area, specify the threshold that the performance metric must reach to decrease the pool size.
- Scale-in operator: Select the operator to scale-in, for example &lt; or &lt;=.
- Threshold percentage: The threshold at which the number of instances in the instance pool decreases.
- Number of instances to remove: Enter the number of instance to remove from the pool.

For example, when CPU utilization is less than 20%, remove 5 instances from the pool.

Scaling limits

In the Scaling limits area, specify the number of instances in the instance pool.
- Minimum number of instances: The minimum number of instances that the pool is allowed to decrease to.
- Maximum number of instances: The maximum number of instances that the pool is allowed to increase to.
Important  
  
The number of instances that can be provisioned is also limited by your tenancy's[service limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm).
- Initial number of instances: The number of instances to launch in the instance pool immediately after autoscaling is enabled. After autoscaling retrieves performance metrics, the number of instances is automatically adjusted from this initial number to a number that is based on the scaling limits that you set.

Select Next .

## Review

Review the autoscaling configuration, and then select Create .

Autoscaling runs. The cooldown period starts when the instance pool's state changes from Scaling to Running .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/autoscaling/configuration/create.html)autoscaling configuration create`command and required parameters to create an autoscaling configuration:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to create an autoscaling configuration:
- [CreateAutoScalingConfiguration](https://docs.oracle.com/iaas/api/#/en/autoscaling/latest/AutoScalingConfiguration/CreateAutoScalingConfiguration)
