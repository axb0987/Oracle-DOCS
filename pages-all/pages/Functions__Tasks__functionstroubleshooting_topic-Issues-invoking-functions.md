# Issues invoking functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm
- Fetched: 2026-09-05 02:09 CDT

# Issues invoking functions

Find out how to troubleshoot problems when invoking functions deployed to OCI Functions.

You might encounter these issues when invoking functions deployed to OCI Functions.

## Invoking a function returns an FunctionInvokeRequestContentTooLarge message and a 413 error

When you invoke a function that you've deployed to OCI Functions, you might see the following error message:
```

```

The message indicates the content of the request to OCI Functions exceeds the maximum allowed size of 6 MB.

If you see this error, double-check that the content of the request does not exceed the maximum allowed size.

## Invoking a function returns a TooManyRequests message and a 429 error

When you invoke a function that you've deployed to OCI Functions, you might see the following error message:
```

```

The message indicates that OCI Functions is already handling the maximum number of requests allowed for your tenancy, and cannot accept another request.

For more information about proactively anticipating and avoiding this error, see[Monitoring Memory Usage and Availability for OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsmonitoringcapacityusage.htm).

If you see this error, wait a few minutes before invoking the function again. Alternatively, or if the problem persists,[Contact Us](https://support.oracle.com/)to increase the total memory for concurrent function execution.

## Invoking a function causes the client to report a timeout, and a 444 error is shown in the function's logs

When you invoke a function that you've deployed to OCI Functions, the client might report a timeout.

Investigate further by checking the function's logs (see[Storing and Viewing Function Logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsexportingfunctionlogfiles.htm)). If the logs contain a status 444 message, the connection between the client and OCI Functions was interrupted during function execution. If you see a status 444 message in the function's logs, invoke the function again.

Note that how you invoke a function also determines the maximum amount of time the function can run for. For more information, see[Invoking Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm).

## Invoking a function returns a Function failed message and a 502 error

If there is a problem with a function's code, you will see the following error when you invoke the function:
```

```

To investigate the issue with the function's code, check the logs output by the function. The Oracle Cloud Infrastructure Logging service is the default and recommended option for accessing, searching, and storing function logs. Note that to store and view logs for a function, the function must include print statements. For more information, see[Storing and Viewing Function Logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsexportingfunctionlogfiles.htm).

## Invoking a function returns a FunctionInvokeSyslogUnavailable message and a 502 error

OCI Functions enables you to send a function's logs to an external logging destination (like Papertrail) by setting a syslog URL for the application. See[Storing and Viewing Function Logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsexportingfunctionlogfiles.htm).

If the syslog URL is invalid or unreachable, you will see the following error when you invoke the function:
```

```

To confirm that the external logging destination's URL is the cause of the error:
- Update the application to unset the syslog URL using the Fn Project CLI. For example, by entering:

```

```

- Deploy the function you want to run. See[Creating and Deploying Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsuploading.htm).
- Invoke the function. See[Invoking Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm).

If the function runs successfully, the external logging destination's URL is not reachable from the subnet in which the function is running. Double-check that:
- The external logging destination's URL is valid.
- The external logging destination's URL is publicly accessible.
- The subnet in which the function is running has outbound access to the public internet.

## Invoking a function returns a FunctionInvokeImageNotAvailable message and a 502 error

When you invoke a function, OCI Functions pulls the corresponding image from Oracle Cloud Infrastructure Registry using the VCN and subnets specified for the application.

If OCI Functions is unable to pull the image, the following message is returned when you invoke a function:
```

```

Possible solutions:
- Double-check that the image specified for the function still exists in the specified location in Oracle Cloud Infrastructure Registry.
- Double-check that Oracle Cloud Infrastructure is available (this message is returned if Oracle Cloud Infrastructure is unexpectedly unavailable).
- 

Double-check that the VCN includes an internet gateway or service gateway. For OCI Functions to be able to access Oracle Cloud Infrastructure Registry to pull an image, the VCN must include an internet gateway or a service gateway, as follows:
- If public subnets were specified for the application, the VCN must also include an internet gateway. A route table must include a route rule that targets the internet gateway, with its Destination CIDR Block property set to 0.0.0.0/0. A security list must include a stateful egress rule that allows access to Oracle Cloud Infrastructure Registry (for example, with its Destination Type property set to`Service`, its Destination Service property set to`All <region> services In Oracle Services Network`, and its IP Protocol property set to`All`).
- If private subnets were specified for the application, the VCN must also include a service gateway. The service gateway must be set up to allow access to`All <region> Services In Oracle Services Network`. A route table must include a route rule that targets the service gateway, with its Destination Service property set to`All <region> Services In Oracle Services Network`. A security list must include a stateful egress rule that allows access to Oracle Cloud Infrastructure Registry (for example, with its Destination Type property set to`Service`, its Destination Service property set to`All <region> services In Oracle Services Network`, and its IP Protocol property set to`All`).

If an internet gateway or service gateway has not been defined for the VCN already, define one now.

## Invoking a function returns a FunctionInvokeSubnetOutOfIPs message and a 502 error

When you invoke a function that you've deployed to OCI Functions, you might see the following error message:
```

```

If you see this error, double-check that each subnet in the VCN has at least the required minimum number of free IP addresses specified in[Creating the VCN and Subnets to Use with OCI Functions, if they don't exist already](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingvcn.htm).

## Invoking a function returns a FunctionInvokeSubnetNotAvailable message and a 502 error (due to a subnet issue)

When you invoke a function that you've deployed to OCI Functions, you might see the following error message:
```

```

If you see this error, double-check that the subnet specified for the application still exists.

## Invoking a function returns a FunctionInvokeSubnetNotAvailable message and a 502 error (due to a DHCP Options issue)

When you invoke a function that you've deployed to OCI Functions, you might see the following error message:
```

```

If you see this error, double-check that the set of DHCP Options in the VCN specified for the application still exists.

## Invoking a function returns a FunctionInvokeResponseBodyTooLarge message and a 502 error

When you invoke a function that you've deployed to OCI Functions, you might see the following error message:
```

```

The message indicates that the response returned by executing the function exceeds the maximum size allowed of 6 MB.

If you see this error, review the function code and reduce the size of responses that the function returns.

## Invoking a function returns a FunctionInvokeResponseHeaderTooLarge message and a 502 error

When you invoke a function that you've deployed to OCI Functions, you might see the following error message:
```

```

The message indicates that the response header returned by executing the function exceeds the maximum size allowed.

If you see this error, review the function code and reduce the number and/or size of any custom headers that the function returns.

## Invoking a function returns a FunctionInvokeSecurityAttributeNotAvailable message and a 502 error

When you invoke a function that you've deployed to OCI Functions, you might see the following error message:
```

```

The message indicates that a security attribute that was previously added to the application containing the function has been deleted using the Zero Trust Packet Routing (ZPR) Console, API, or CLI.

If you see this error, remove the security attribute from the application. For more information about security attributes, see[Adding Security Attributes to Applications, and Applying ZPR Policies](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingzpr.htm).

## Invoking a function returns a FunctionInvokeTooManyMatchingDGs message and a 502 error

When you invoke a function that you've deployed to OCI Functions, you might see the following error message:
```

```

The message indicates that the function belongs to more dynamic groups than the supported maximum number.

If you see this error, reduce the number of dynamic groups to which the function belongs by updating dynamic group matching rules. To find out the maximum number of dynamic groups to which a function can belong, see[Limits on Dynamic Groups](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#Limits_on_Instances_in_Dynamic_Groups)(the limit shown for a single compute instance applies to a function as well).

## Invoking a function returns a FunctionInvokeExecutionError message and a 502 error

When you invoke a function that you've deployed to OCI Functions, you might see the following error message:
```

```

The message indicates that the response from executing the function returns an error.

If you see this error unexpectedly, review the function code to understand the conditions in which the function does not execute successfully.

## Invoking a function returns a FunctionInvokeExecutionFailed message and a 502 error

When you invoke a function that you've deployed to OCI Functions, you might see the following error message:
```

```

The message indicates that an error was detected during function execution, which was most likely caused by a bug in the function code.

If you see this error, review the function code and fix any bugs you find.

## Invoking a function returns a FunctionInvokeInvalidResponse message and a 502 error

When you invoke a function that you've deployed to OCI Functions, you might see the following error message:
```

```

The message indicates that invoking the function returns an invalid HTTP response code (neither a function failure nor a timeout).

If you see this error, review the function code and fix any bugs you find.

## Invoking a function returns a FunctionInvokeSubnetConfigError message and a 502 error

When you invoke a function that you've deployed to OCI Functions, you might see the following error message:
```

```

The message indicates a VCN configuration problem, probably related to custom resolver configuration.

If you see this error, identify any subnet in the VCN that is using a custom resolver. Where a subnet is using a custom resolver (for example, located on the internet, in the VCN, or on your on-premises network), confirm that the custom resolver is reachable. Also verify that the custom resolver is working correctly. For more information about custom resolvers, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm).

If the error persists, check that the VCN configuration (and the custom resolver configuration, if used) is correct by invoking a new hello world function running in a new VCN:
- Create a new VCN using the VCN Wizard (select VCN with Internet Connectivity ).
- Create a new DHCP Options resource, and specify the same DNS options as before (if a custom resolver was used before, select Custom Resolver ).
- Create a new subnet in the VCN, and select the DHCP Options resource you just created.
- Create a new application, specifying the VCN and subnet you just created.
- Create a simple hello world function in the application you just created.
- Confirm that you can invoke the new hello world function successfully.

If the problem persists,[Contact Us](https://support.oracle.com/)to help you resolve the VCN configuration issue.

## Invoking a function returns "The combined uncompressed size of all Function images in an application has exceeded the allotted limit...." message and a 502 error

When you invoke a function that you've deployed to OCI Functions, the function's image is pulled from the Docker registry. Depending on the size of the image, and the size of the images for other functions in the application, you might see a message similar to the following:
```

```

This message indicates that pulling the function's image has increased the total uncompressed size of all the images for functions in the application beyond the maximum allowed limit.

If you see this error:
- Use standard techniques to reduce the size of the function's image, and/or the size of the images for other functions in the application.
- Reduce the number of functions in the application.

## Invoking a function returns a FunctionInvokeContainerInitFail error message, a 502 error, and a 'ModuleNotFoundError: No module named 'contextvars'' log message

When you invoke a Python 3.6 function that you've deployed to OCI Functions, you might see the following error message:
```

```

If you see this error, check the function's logs. If you see a "`ModuleNotFoundError: No module named 'contextvars'`message in the function's logs:
- Add the following line to the function's requirements.txt file:

```

```

- Re-deploy the function to OCI Functions.
- Invoke the function again.

## Invoking a function returns a FunctionInvokeServiceUnavailable message and a 503 error

When you invoke a function that you've deployed to OCI Functions, you might see the following error message:
```

```

The message indicates that OCI Functions is currently unable to handle the request, possibly because of insufficient capacity. Encountering this error message multiple times is not uncommon, because it can take some time to scale up OCI Functions capacity to meet demand from function invocations.

If you see this error, try invoking the function again. Do not be concerned if the message reappears. Continue to retry invoking the function, leaving a short period of time between invocation attempts. Note the following:
- If you continue to see this error, consider increasing the time interval between function invocations (perhaps using a standard technique like jittered exponential backoff to add a degree of randomness to the interval).
- If the message is displayed when a function is invoked as the result of an action triggered by an event, additional attempts to invoke the function will be retried automatically until the function is successfully invoked. No intervention on your part is required.
- If you set up alarms that are triggered by function error responses containing 503 error codes, you might see multiple notifications for which no intervention on your part is required
- If the message continues to appear after an extended period of time,[Contact Us](https://support.oracle.com/)for assistance.

If you are invoking a function associated with an application configured to use the GENERIC_ARM shape, repeated retries might not succeed if Arm shapes are not supported in the target region or if Arm capacity is currently unavailable in that region. If the issue persists:
- Verify whether Arm is supported and available in the target region.
- If Arm is not required for your workload, consider using the GENERIC_X86 shape instead.
- If your workload supports it, also consider using GENERIC_X86_ARM (multi-architecture option) to improve portability across regions and reduce the likelihood of region-specific architecture availability issues.

## Invoking a function returns FunctionInvokeContainerInitTimeout and 'Container initialization timed out' messages, and a 504 error

When you invoke a function that you've deployed to OCI Functions, the function execution is subject to a maximum memory threshold. If this limit is exceeded, function execution stops and the following error message is returned:
```

```

If you see this error, increase the function's maximum memory threshold. For example, to 256 MB, 512 MB, 1024 MB, 2048 MB, or 3072 MB. See[Changing Default Memory and Timeout Settings](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscustomizing.htm)for valid values for the maximum memory threshold.

For example, to set a function's maximum memory threshold to 256 MB, do one of the following:
- Select Edit on the function details page in the Console, and select 256 from the Memory (in MBs) drop-down list.
- 

Add the following line to the function's func.yaml file. This will set the maximum memory threshold to 256 MB whenever the function is invoked:

```

```

Note that if you edit the func.yaml file, you must re-deploy the function to OCI Functions before invoking it again.

It's a good idea to use the latest version of the Fn Project CLI when creating a helloworld Python function. When you enter the`fn init --runtime python <function-name>`command to create the helloworld function, the line`memory: 256`is added to the func.yaml file automatically.

## Invoking a function returns a FunctionInvokeTimeout message and a 504 error

When you invoke a function that you've deployed to OCI Functions, the function is only allowed to run for a certain amount of time. If this time limit is exceeded, function execution stops and the following error message is returned:
```

```

If you see this error, try increasing the maximum time a function is allowed to run for in the function definition. For example, to set the maximum time to 300 seconds, do one of the following:
- Select Edit on the function details page in the Console, and enter 300 in the Timeout (in seconds) field.
- 

Add the following line to the function's func.yaml file. This will set the maximum time limit to 300 seconds whenever the function is invoked:

```

```

Remember that if you edit the func.yaml file, you must re-deploy the function to OCI Functions before invoking it again.

Note that how you invoke a function also determines the maximum amount of time the function can run for. For more information, see[Invoking Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm).

You might also see this error message when a function running in a public subnet is unable to connect to an Oracle Autonomous AI Database instance that has access control lists (ACLs) enabled. If this is the case, see[Connecting to Oracle Autonomous AI Database Instances from Running Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsaccessingadbfromrunningfunctions.htm)for more information about:
- Configuring the subnet to send all outgoing internet traffic to a NAT gateway, and to allow internet traffic.
- Adding the NAT gateway's public IP address to the database's access control list.

## Invoking a function returns a FunctionInvokeContainerInitTimeout message and a 504 error

When you invoke a function that you've deployed to OCI Functions, the function's image is pulled from the Docker registry and run inside a container. Depending on the function's dependencies, the container might take a long time to start. If the container takes too long to start, you might see the following error message:
```

```

If you see this error, increase the function's maximum memory threshold. For example, to 256 MB, 512 MB, 1024 MB, 2048 MB, or 3072 MB. See[Changing Default Memory and Timeout Settings](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscustomizing.htm)for valid values for the maximum memory threshold.

For example, to set a function's maximum memory threshold to 256 MB, do one of the following:
- Select Edit on the function details page in the Console, and select 256 from the Memory (in MBs) drop-down list.
- 

Add the following line to the function's func.yaml file. This will set the maximum memory threshold to 256 MB whenever the function is invoked:

```

```

Note that if you edit the func.yaml file, you must re-deploy the function to OCI Functions before invoking it again.

It's a good idea to use the latest version of the Fn Project CLI when creating a helloworld Python function. When you enter the`fn init --runtime python <function-name>`command to create the helloworld function, the line`memory: 256`is added to the func.yaml file automatically.

## Invoking a function returns a FunctionInvokeImagePullTimeout message and a 504 error

When you invoke a function that you've deployed to OCI Functions, the function's image is pulled from the Docker registry. Depending on the size of the image, it might take a long time to pull the image. If it takes too long to pull the image, you might see the following error message:
```

```

If you see this error:
- Use standard techniques to reduce the size of the image.
-
