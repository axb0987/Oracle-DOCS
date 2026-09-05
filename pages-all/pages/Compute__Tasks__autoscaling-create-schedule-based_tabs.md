# Creating Schedule-based Autoscaling Configuration
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-create-schedule-based_tabs.htm
- Fetched: 2026-09-05 01:50 CDT

# Creating Schedule-based Autoscaling Configuration

Complete the following steps to create an schedule-based autoscaling configuration.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-create-schedule-based_tabs.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-create-schedule-based_tabs.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-create-schedule-based_tabs.htm#)
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

On the Configure autoscaling policy page, select Schedule-based autoscaling . Then, do the following tasks.
Tip  
  
Toggle Instance pool information to see the instance pool details.

Autoscaling policy 1
- Autoscaling policy name: Enter a name for the autoscaling policy. Avoid entering confidential information.
- Action to perform:

For Action to perform , select Scale pool size or Change lifecycle state of all instances .
- Scale pool size: In the Target pool size box, enter the number of instances that the pool should scale to at the scheduled time.
Important  
  
The number of instances that can be provisioned is also limited by your tenancy's[service limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm).
- Change lifecycle state of all instances: In the Lifecycle action menu, select the action to run on the instance pool. Examples include: Start, Force reboot, Reboot, Force stop, Stop.
- Execution schedule: Define the schedule for implementing this autoscaling policy in UTC. Use a Quartz cron expression. For more information about cron expressions, see[About Cron Expressions](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm#about-cron-expressions).
- To schedule more scaling events, select Another Policy and then repeat the previous steps.
- Select Next .

## Review

Review the autoscaling configuration, and then select Create .

Autoscaling runs at the scheduled time.
- 

Use the[autoscaling configuration create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/autoscaling/configuration/create.html)command and required parameters to create an autoscaling configuration:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to create an autoscaling configuration:
- [CreateAutoScalingConfiguration](https://docs.oracle.com/iaas/api/#/en/autoscaling/latest/AutoScalingConfiguration/CreateAutoScalingConfiguration)
