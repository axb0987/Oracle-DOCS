# Zero Quota Policy Creator Function
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_catalog_zero_quota_policy_creator.htm
- Fetched: 2026-09-05 02:07 CDT

# Zero Quota Policy Creator Function

Find out how to use the Zero Quota Policy Creator pre-built function in OCI Functions to create a quota policy on compartments to prevent the creation of OCI resources, and so help to enforce budgets and manage OCI spending.

## Common Usage Scenarios

Create a zero quota policy that prevents creation of OCI resources after reaching a spending threshold. To do this, perform the following two steps:
- Create a budget for a compartment and a budget alert rule to set a budget alert based on an actual or forecasted spending threshold. For more information on budgets, see[Managing Budgets](https://docs.oracle.com/iaas/Content/Billing/Tasks/managingbudgets.htm).
- Configure an event rule in the root compartment to trigger from the budget alert and to invoke a function created from this pre-built function. For more information on event rules, see[Using the Console to Create a Rule](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsgetstarted.htm#Console).

Services related to the Zero Quota Policy Creator function include:
- [Events](https://docs.oracle.com/iaas/Content/Events/home.htm)
- [Budget Service](https://docs.oracle.com/iaas/Content/Billing/Concepts/budgetsoverview.htm#Budgets_Overview)
- [Compartment Quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm#top)
- [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm)

## Scope

Scope considerations for this function include:
- This pre-built function supports budgets created for compartment scope only. For more information, see[Managing Budgets](https://docs.oracle.com/iaas/Content/Billing/Tasks/managingbudgets.htm).

## Prerequisites And Recommendations

The following are best practices when using this pre-built function:
- Set the pre-built function timeout to 300 seconds.
- Make sure that the VCN linked to the application facilitates access to other OCI services by using a service gateway, internet gateway, or NAT gateway.
- Create event rules only in the root compartment.
- 

Both budgets and quota policy are tenancy level features. Configure this pre-built function in the home region. When configured in the home region, use a Service Gateway in a VCN.

If the pre-built function is configured in another region, an Internet Gateway or a NAT gateway is required to make cross-region calls.

## Configuring the Zero Quota Policy Creator Function

To configure a Zero Quota Policy Creator function, perform the following steps:

- On the Pre-Built Functions page, select Zero Quota Policy Creator , and then select Create function .
- Configure the Name , Compartment , and Application as follows:

- Name: A name of your choice for the new function. The name must start with a letter or underscore, followed by letters, numbers, hyphens, or underscores. Length can be 1–255 characters. Avoid entering confidential information.

To create the function in a different compartment, select Change Compartment .
- Application: Select the application in which you want to create the function.

If a suitable application doesn't already exist in the current compartment, select Create new application and specify the following details:
- Name: A name for the new application. Avoid entering confidential information.
- VCN: The VCN (virtual cloud network) in which to run functions in the application. Optionally, select VCN compartment: to select a VCN from a different compartment.
- Subnets: The subnet (or subnets, up to a maximum of three) in which to run functions. Optionally, select Subnets compartment: to select a subnet from a different compartment.
- Shape: The processor architecture of the compute instances on which to deploy and run functions in the application. All the functions in the application are deployed and run on compute instances with the same architecture. The function's image must contain the necessary dependencies for the architecture you select.
- Tags: If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Security attributes: If you have permissions to create a resource, then you might also have permissions to add security attributes to that resource. To add a security attribute, you must have permissions to use the security attribute namespace. For more information about security attributes and security attribute namespaces, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm). If you're not sure whether to add security attributes, skip this option or ask an administrator. You can add security attributes later.
- Configure the IAM policy for pre-built functions.

By default, OCI Functions creates a dynamic group and an IAM policy with the policy statements required to run the pre-built function. Proceed as follows:
- If you want OCI Functions to automatically create the dynamic group and policy, make no changes to accept the default behavior.
- If you don't want OCI Functions to automatically create the dynamic group and policy, select Do not create a dynamic group and IAM policy .
Important  
  
If you select the Do not create a dynamic group and IAM policy option, you must define the dynamic group and the IAM policy yourself. For more information, see[Permissions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_catalog_zero_quota_policy_creator.htm#pbf-zero-quota-policies-plus__permissions-zero-quota).
- Configure function memory and timeout values as follows:

- Memory (in MBs): The maximum amount of memory that the function can use while running, in megabytes. This is the memory available to the function image. (Default: 256 MB)
- Timeout (in seconds): The maximum amount of time that the function can run for, in seconds. If the function doesn’t complete in the specified time, the system cancels the function. (Default: 300)
- (Optional) Configure Provisioned concurrency to minimize any initial delays when invoking the function by specifying a minimum number of concurrent function invocations for which you want to have execution infrastructure constantly available. (Default: Not selected)

If selected, specify the number of provisioned concurrency units assigned to this function. Default: 20.

For more information about provisioned concurrency, see[Reducing Initial Latency Using Provisioned Concurrency](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingprovisionedconcurrency.htm).
- Set the function configuration parameters as described in[Configuration Parameters](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_catalog_zero_quota_policy_creator.htm#pbf-zero-quota-policies-plus__pbf-zero-quota-config-parameters).
- Optionally enter any tags in the Tags section. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create .

The deploy dialog displays the tasks to deploy the function (see[Finishing Pre-Built Function Deployment](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_finishing_prebuilt_deploy.htm)).

## Configuration Options

### Configuration Parameters

Name Description Required
`SERVICE_FAMILY_NAMES`A comma separated list of service family names to be used in the quota policy statement. The default value includes all the service family names that support the Quota Service. For more information, see[Available Quotas by Service](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas_topic-Available_Quotas_by_Service.htm#AvailableQuotasByService). No
`PBF_LOG_LEVEL`Logging level, options are`DEBUG`,`INFO`,`WARN`, and`ERROR`. Defaults to`INFO`. No

### Permissions

Running a function requires certain IAM policies. If you selected the Do not create a dynamic group and IAM policy option when creating the function, you must define the dynamic group and the IAM policy yourself.

To set the proper policies, perform the following steps:
- Create a dynamic group with the rule:

```

```

- Configure an IAM policy using the dynamic group:

```

```

Note  
  
Replace`<function-ocid>`with the OCID of the function that you created in preceding steps.
Note  
  
Replace`<dynamic-group-name>`with the name of the dynamic group that you created using the function's OCID.
Note  
  
Replace`<compartment_ocid>`with the OCID of the compartment that contains the function.

### Invoking This Function

You can invoke the function in the following ways:
- Create an event rule to match the budget threshold spending events to a rule that creates a quota policy to prevent creation of new resources.

### Response Body
- Timestamps: Using UTC to avoid time zone issues.
- Code: The function returns a 200 code if the task completes successfully.
- Status: The function returns "Success" as the status if the task completes successfully.
- Message: A JSON message body that includes specific response information for the task.

Example

The following example shows the JSON return data:

```

```

### Troubleshooting

OCI Functions common status codes

The following table summarizes common OCI Functions errors that you might encounter when working with pre-built functions:

Error Code Error Message Action
200 Success None
404 NotAuthorizedOrNotFound Verify that the required policies are configured (see[Running Fn Project CLI commands returns a 404 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionstroubleshooting_topic-Issues-setting-up-and-running-Oracle-Functions.htm#Running_Fn_Project_CLI_commands_returns_a_404_error)).
444 Timeout

The connection between the client and OCI Functions was interrupted during function execution (see[Invoking a function causes the client to report a timeout, and a 444 error is shown in the function's logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#functionstroubleshooting_topic_Function_timeout_client_message_and_a_444_error)). A retry might solve the issue.

Note that most clients have an inner timeout of 60 seconds. Even when the pre-built function timeout is set to 300 seconds, the following might be required:
- When using the OCI CLI : Use --read-timeout 300
- When using the OCI SDK : Set the read timeout to 300 when creating the client
- When using DBMS_CLOUD.SEND_REQUEST : Use UTL_HTTP.set_transfer_timeout(300);

For more information, see[Invoking Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionsinvokingfunctions.htm).
502, 504 (various) Most issues return a 502 status code (see[Invoking a function returns a Function failed message and a 502 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#Invoking_a_function_returns_a_Functionfailed_message_and_a_502_error)). A 502 error with the message "error receiving function response" might be resolved by increasing the memory allocation. A 502 might occur occasionally when the function is in some transient state. A retry might solve the issue.

To further identify the cause, enable logging features for the pre-built function (see[Storing and Viewing Function Logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionsexportingfunctionlogfiles.htm)). For detailed information on troubleshooting a function, see[Troubleshooting OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionstroubleshooting.htm).

Zero Quota Policy Creator pre-built function status codes

The following table summarizes the errors that you might encounter when working with this pre-built function:

Error Code Error Message Action
400 Function payload has wrong Event Type Verify whether the event type is "AlertRule - Create".

To further identify the cause, enable logging features for the pre-built function (see[Storing and Viewing Function Logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionsexportingfunctionlogfiles.htm)).

Log Analysis Tips

All the pre-built functions provide an option to specify the logging level as a configuration parameter. You can set the logging level to`DEBUG`to get more information.

Since an application has multiple functions, the pre-built function log entries are identified by the prefix "PBF | &lt;PBF NAME&gt; ".

For example, a log entry for the Media Workflow Job Spawner pre-built function looks similar to the following:
```

```
