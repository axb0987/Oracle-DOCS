# Cost Reports FOCUS Converter Function
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_catalog_cost_reports_focus_converter.htm
- Fetched: 2026-09-05 02:07 CDT

# Cost Reports FOCUS Converter Function

Find out how to use the Cost Reports FOCUS Converter pre-built function in OCI Functions to convert OCI-generated cost report csv files to FinOps Open Cost and Usage Specification (FOCUS) schema zip files, and save the zip files to a specified target bucket in OCI Object Storage.

## Common Usage Scenarios

Common ways to use the Cost Reports FOCUS Converter function include:
- Read OCI-generated cost report files that exist in an object storage bucket in the Billing and Cost Management service tenancy, and directly invoke a function to convert the files and store the resulting zip file in an object storage bucket in your tenancy.

Services related to the Cost Reports FOCUS Converter function include:
- [Object Storage](https://docs.oracle.com/iaas/Content/Object/home.htm)

## Scope

Scope considerations for this function include:
- The pre-built function works best if the default timeout is set to 300 seconds.
- The function execution time varies according to the number of input files that exist between the start date and the end date.

## Prerequisites and Recommendations

To use the Cost Reports FOCUS Converter pre-built function, you must manually add an additional endorse IAM policy in your tenancy's root compartment. The additional endorse IAM policy enables cross-tenancy calls to the Billing and Cost Management service tenancy. The pre-built function requires the endorse IAM policy. Note that without the endorse policy, the pre-built function cannot access the cost reports. For more information about creating the endorse IAM policy, see[Permissions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_catalog_cost_reports_focus_converter.htm#functions_pbf_catalog_cost_reports_focus_converter_policies_plus__permissions-cost-reports-focus-converter).

You must create this pre-built function in your home region.

The following are best practices when using this pre-built function:
- Set the pre-built function timeout to 300 seconds.
- Make sure that the VCN linked to the application facilitates access to other OCI services by using a service gateway, internet gateway, or NAT gateway.
- Set the default memory size to the maximum memory allowed for a function.

## Configuring the Cost Reports FOCUS Converter Function

To configure a Cost Reports FOCUS Converter function, perform the following steps:

- On the Pre-Built Functions page, select Cost Reports FOCUS Converter , and then select Create function .
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
  
If you select the Do not create a dynamic group and IAM policy option, you must define the dynamic group and the IAM policy yourself. For more information, see[Permissions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_catalog_cost_reports_focus_converter.htm#functions_pbf_catalog_cost_reports_focus_converter_policies_plus__permissions-cost-reports-focus-converter).

Note that to use the Cost Reports FOCUS Converter pre-built function, you must also manually add an additional endorse IAM policy in your tenancy's root compartment. The additional endorse IAM policy enables cross-tenancy calls to the Billing and Cost Management service tenancy. The pre-built function requires the endorse IAM policy. Note that without the endorse policy, the pre-built function cannot access the cost reports. For more information about creating the endorse IAM policy, see[Permissions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_catalog_cost_reports_focus_converter.htm#functions_pbf_catalog_cost_reports_focus_converter_policies_plus__permissions-cost-reports-focus-converter).
- Configure function memory and timeout values as follows:

- Memory (in MBs): The maximum amount of memory that the function can use while running, in megabytes. This is the memory available to the function image.
- Timeout (in seconds): The maximum amount of time that the function can run for, in seconds. If the function doesn’t complete in the specified time, the system cancels the function. (Default: 300)
- (Optional) Configure Provisioned concurrency to minimize any initial delays when invoking the function by specifying a minimum number of concurrent function invocations for which you want to have execution infrastructure constantly available. (Default: Not selected)

If selected, specify the number of provisioned concurrency units assigned to this function. Default: 10.

For more information about provisioned concurrency, see[Reducing Initial Latency Using Provisioned Concurrency](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingprovisionedconcurrency.htm).
- Set the function configuration parameters as described in[Configuration Parameters](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_catalog_cost_reports_focus_converter.htm#functions_pbf_catalog_cost_reports_focus_converter_policies_plus__configuration-parameters-cost-reports-focus-converter).
- Optionally enter any tags in the Tags section. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create .

The deploy dialog displays the tasks to deploy the function (see[Finishing Pre-Built Function Deployment](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_finishing_prebuilt_deploy.htm)).

## Configuration Options

### Configuration Parameters

Name Description Required
`PBF_LOG_LEVEL`Logging level, options are`DEBUG`,`INFO`,`WARN`, and`ERROR`. Defaults to INFO. No

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

To run the Cost Reports FOCUS Converter pre-built function, you must manually add the following endorse IAM policy in your tenancy's root compartment to enable the function to access cost reports stored in the Billing and Cost Management service tenancy:

```

```

Important  
  
The pre-built function requires the endorse IAM policy, and you have to create the policy manually. Without the endorse policy, the pre-built function cannot access cost reports.

### Invoking This Function

You can invoke the function in the following ways:
- Invoke the function directly as documented in[Invoking Functions](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm)by creating a request body as shown in the following JSON example.

HTTP Request JSON Values

Name Description Required
COMPARTMENT_ID OCID of a compartment in your tenancy. If the target bucket doesn't already exist in this compartment, the pre-built function creates a new target bucket in this compartment. This compartment is also used when creating the required IAM policies. Yes
REGION The name of your home region. You must create this pre-built function in your home region. Yes
NAMESPACE The Billing and Cost Management service tenancy namespace (that is, bling). This namespace is used to read OCI-generated cost report csv files from the source bucket. Yes
SOURCE_BUCKET Name of the source bucket in the Billing and Cost Management service tenancy that contains the OCI-generated cost report csv files. This value must be your tenancy's OCID. Yes
TARGET_BUCKET Name of the target bucket in your tenancy. If a target bucket with this name doesn't exist, the pre-built function creates the bucket in the compartment specified by COMPARTMENT_ID. Yes
START_DATE The pre-built function only reads files from the source bucket that were created on or after this date. The start date is required to limit the number of files that the pre-built function processes, because of the timeout limit of 300 seconds. Yes
END_DATE The pre-built function only reads files from the source bucket that were created on or before this date. Yes

Sample Request Body

```

```

### Response Body
- Timestamp: Using UTC to avoid time zone issues.
- Code: The function returns a 200 code if the task completes successfully.
- Status: The function returns "Success" as the status if the task completes successfully.
- data: A JSON message body that includes specific response information for the task. The additional information provides a confirmation message if the conversion operation is successful.

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

Cost Reports FOCUS Converter pre-built function status codes

The following table summarizes the errors that you might encounter when working with this pre-built function:

Error Code Error Message Action
400 Missing mandatory configuration value The error message indicates the required field name. Verify the correct field is provided in the request body.

To further identify the cause, enable logging features for the pre-built function (see[Storing and Viewing Function Logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionsexportingfunctionlogfiles.htm)).

Log Analysis Tips

All the pre-built functions provide an option to specify the logging level as a configuration parameter. You can set the logging level to`DEBUG`to get more information.

Since an application has multiple functions, the pre-built function log entries are identified by the prefix "PBF | &lt;PBF NAME&gt; ".

For example, a log entry for the Cost Reports FOCUS Converter pre-built function looks similar to the following:
```

```
