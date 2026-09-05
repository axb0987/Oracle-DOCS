# Troubleshooting OCI Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting.htm
- Fetched: 2026-09-05 02:09 CDT

# Troubleshooting OCI Functions

Find out how to troubleshoot problems with OCI Functions, and possible solutions to common issues.

This topic covers common issues related to OCI Functions and how to address them.

Use the following techniques to find out more about an error or issue:
- Use the Errors chart on the Metrics page in the Console to see error codes and messages for individual functions: If a function doesn't run or perform as expected when you invoke it, you can use the Errors chart on the Metrics page in the Console to see error codes and error messages for that function. For more information, see[Function Metrics](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Reference/functionsmetrics.htm).
- Use tracing to observe function execution: If a function doesn't run or perform as expected when you invoke it, you can use tracing to debug execution and performance issues. To use tracing, you have to enable tracing for the application containing the function, and then enable tracing for one or more functions. You can then view function traces in the APM Trace Explorer. For more information, see[Distributed Tracing for Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstracing.htm).
- Use function logs to review function invocation information: The Oracle Cloud Infrastructure Logging service is the default and recommended option for accessing, searching, and storing function logs. Note that to store and view logs for a function, the function must include print statements. For more information, see[Storing and Viewing Function Logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsexportingfunctionlogfiles.htm).
- 

Use DEBUG=1 to see details about requests and responses sent to and from the OCI Functions service: If you encounter an unexpected error when using an Fn Project CLI command, you can see more details about the HTTP requests and responses sent to and from the OCI Functions service. Start the command with the string`DEBUG=1`and run the command again. For example:
```

```

Note that`DEBUG=1`must appear before the command, and that`DEBUG`must be in upper case.

If you engage with Oracle Support and raise a support ticket, you can attach the output to the ticket.

Note also that if you have set up a local machine as your OCI Functions development environment (specifying`--provider oracle`in the Fn Project CLI context), you must set the environment variable`OCI_GO_SDK_DEBUG=v`as well as starting the command with`DEBUG=1`.

The issues in this topic are organized in the following broad categories:
- [Setting up and running OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting.htm#Troubleshooting_Oracle_Functions__Troubleshooting-Setting-up-and-running)
- [Creating applications and functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting.htm#Troubleshooting_Oracle_Functions__Troubleshooting-Creating-apps-and-functions)
- [Deploying applications and functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting.htm#Troubleshooting_Oracle_Functions__Troubleshooting-Deploying-apps-and-functions)
- [Invoking functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting.htm#Troubleshooting_Oracle_Functions__Troubleshooting-Invoking-functions)
- [Miscellaneous](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting.htm#Troubleshooting_Oracle_Functions__Troubleshooting-Miscellaneous)

## Setting up and running OCI Functions

Error number and message (if applicable) Description and link
`401: Not authenticated`[Running Fn Project CLI commands returns a 401 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-setting-up-and-running-Oracle-Functions.htm#runningcli401gerror)
`404: Resource is not authorized or not found`[Running Fn Project CLI commands returns a 404 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-setting-up-and-running-Oracle-Functions.htm#Running_Fn_Project_CLI_commands_returns_a_404_error)
`x509: decryption password incorrect`[Running Fn Project CLI commands returns an X509: decryption password incorrect error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-setting-up-and-running-Oracle-Functions.htm#incorrectpassphrase)
`Error response from daemon... unknown: Unauthorized`[Performing Docker-related operations with the Fn Project CLI displays an "Error response from daemon... unknown: Unauthorized" message](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-setting-up-and-running-Oracle-Functions.htm#Performing_Dockerrelated_operations_with_the_Fn_Project_CLI_displays_an_Error_response_from_daemon_unknown_Unauthorized_message)
`asn1:structure error: tags don't match`[Running an Fn Project CLI command displays an "Fn: asn1:structure error: tags don't match" message](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-setting-up-and-running-Oracle-Functions.htm#Running_an_Fn_Project_CLI_command_displays_an_Fn_asn1structure_error_tags_dont_match_message)
`Client version: n.n.nn is not latest: n.n.nn`[Running fn version shows that a more recent version of the Fn Project CLI is available](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-setting-up-and-running-Oracle-Functions.htm#fnversion)

## Creating applications and functions

Error number and message (if applicable) Description and link
`Unable to create your app, please try again.`[Creating a new application displays an error message in the New Application dialog](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-creating-applications-and-functions.htm#newapperror)

## Deploying applications and functions

Error number and message (if applicable) Description and link
`unauthorized: incorrect username or password`[Deploying an application returns an "unauthorized: incorrect username or password" message](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-deploying-applications-and-functions.htm#Deploying_an_application_returns_an_unauthorized_incorrect_username_or_password_message)

`denied: requested access to the resource is denied`

`Fn: error running docker push, are you logged into docker?: exit status 1`[Deploying a function returns an "error running docker push, are you logged into docker?" message](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-deploying-applications-and-functions.htm#dockerio)
`500: Internal server error`[Deploying a function returns a ListTriggers message and a 500 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-deploying-applications-and-functions.htm#Deploying_a_function_returns_a_ListTriggers_message_and_a_500_error)
`Image <image-name> does not exist or you do not have access to use it.`[Deploying a function returns an "Image does not exist or you do not have access to use it" message](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-deploying-applications-and-functions.htm#Deploying_a_function_returns_an_Image_does_not_exist_or_you_do_not_have_access_to_use_it_message)
`401: Missing subnets annotation`[Deploying a function to OCI Functions returns "Fn: Missing subnets annotation" message](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-deploying-applications-and-functions.htm#Deploying_a_function_to_Oracle_Functions_returns_Fn_Missing_subnets_annotation_message)
`Getting image source signatures Error: trying to reuse blob ... at destination: checking whether a blob ... exists in .... :StatusCode: 403, Fn: error running docker push: exit status 125`[Deploying a function returns a "Getting image source signatures Error: trying to reuse blob ... at destination: checking whether a blob ... exists in .... :StatusCode: 403, Fn: error running docker push: exit status 125" message](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-deploying-applications-and-functions.htm#functionstroubleshooting_topic_Deploying_a_function_returns_a_Getting_image_source_signatures_and_a_403_error)
`Function's image architecture 'x86' is incompatible with the application's shape type 'GENERIC_X86_ARM'`[Deploying a function to OCI Functions returns "Function's image architecture 'x86' is incompatible..." message](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-deploying-applications-and-functions.htm#functionstroubleshooting_topic-Deploying_a_function_to_Oracle_Functions_returns_incompatible_image_architecture_message)
`OL8 CloudShell does not support cross-compilation and multi-arch functions builds. Please ensure the architecture of your App matches the CloudShell architecture.`[Deploying a function to OCI Functions in Cloud Shell returns "OL8 Cloud Shell does not support cross-compilation and multi-arch functions builds..." message](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-deploying-applications-and-functions.htm#functionstroubleshooting_topic_Deploying_a_function_to_Oracle_Functions_on_CloudShell_returns_incompatible_image_architecture_message)
`Invalid or unsupported image manifest. Unable to get architecture from the OCIR Manifest/Headers…`[Deploying a function returns an "Invalid or unsupported image manifest. Unable to get architecture from the OCIR Manifest/Headers…" message](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-deploying-applications-and-functions.htm#functionstroubleshooting_topic_Deploying_an_application_returns_an_invalid_or_unsupported_image_manifest_message)
`toomanyrequests: You have reached your unauthenticated pull rate limit`[Building or deploying a function returns "toomanyrequests: You have reached your unauthenticated pull rate limit" error message](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-deploying-applications-and-functions.htm#functionstroubleshooting_topic_Building_or_deploying_a_function_returns_unauthenticated_pull_rate_limit_error_message)

## Invoking functions

Error number and message (if applicable) Description and link

`413: Request content too large`

`FunctionInvokeRequestContentTooLarge`

[Invoking a function returns an FunctionInvokeRequestContentTooLarge message and a 413 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#Invoking_a_function_returns_a_FunctionInvokeRequestContentTooLarge_message_and_a_413_error)

`429: User-rate limit exceeded`

`TooManyRequests`

[Invoking a function returns a TooManyRequests message and a 429 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#Invoking_a_function_returns_a_TooManyRequests_message_and_a_429_error)
`444`[Invoking a function causes the client to report a timeout, and a 444 error is shown in the function's logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#functionstroubleshooting_topic_Function_timeout_client_message_and_a_444_error)
`502: Function failed`[Invoking a function returns a Function failed message and a 502 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#Invoking_a_function_returns_a_Functionfailed_message_and_a_502_error)
`502: Syslog endpoint unavailable`[Invoking a function returns a FunctionInvokeSyslogUnavailable message and a 502 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#Invoking_a_function_returns_a_FunctionInvokeSyslogUnavailable_message_and_a_502_error)
`502: Failed to pull function image`[Invoking a function returns a FunctionInvokeImageNotAvailable message and a 502 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#imagenotavailable)
`502: subnet ocid1.subnet.... is out of IPs`[Invoking a function returns a FunctionInvokeSubnetOutOfIPs message and a 502 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#freeipsnotavailable)
`502: subnet ocid1.subnet.... does not exist or Oracle Functions is not authorized to use it`[Invoking a function returns a FunctionInvokeSubnetNotAvailable message and a 502 error (due to a subnet issue)](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#subnetnotavailable)
`502: dhcp options ocid1.dhcpoptions.... does not exist or Oracle Functions is not authorized to use it`[Invoking a function returns a FunctionInvokeSubnetNotAvailable message and a 502 error (due to a DHCP Options issue)](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#dhcpnotavailable)

`502: function response body too large`

`FunctionInvokeResponseBodyTooLarge`

[Invoking a function returns a FunctionInvokeResponseBodyTooLarge message and a 502 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#Invoking_a_function_returns_a_FunctionInvokeResponseBodyTooLarge_message_and_a_502_error)

`502: FunctionInvokeResponseHeaderTooLarge`

`function response header too large`

[Invoking a function returns a FunctionInvokeResponseHeaderTooLarge message and a 502 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#Invoking_a_function_returns_a_FunctionInvokeResponseHeaderTooLarge_message_and_a_502_error)

`502: FunctionInvokeSecurityAttributeNotAvailable`

`Functions has no access to security attributes or the security attributes not found`

[Invoking a function returns a FunctionInvokeSecurityAttributeNotAvailable message and a 502 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#functionstroubleshooting_topic_function_invoke_security_attribute_not_available_and_a_502_error_Copy)

`502: Unable to get resource authorization token due to Function resource matching too many Dynamic Groups. Update your Dynamic Groups' matching rules`

`FunctionInvokeTooManyMatchingDGs`[Invoking a function returns a FunctionInvokeTooManyMatchingDGs message and a 502 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#functionstroubleshooting_topic_too_many_matching_dynamic_groups_and_a_502_error)

`502: error receiving function response`

`FunctionInvokeExecutionError`

[Invoking a function returns a FunctionInvokeExecutionError message and a 502 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#Invoking_a_function_returns_a_FunctionInvokeExecutionError_message_and_a_502_error)

`502: function failed`

`FunctionInvokeExecutionFailed`

[Invoking a function returns a FunctionInvokeExecutionFailed message and a 502 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#Invoking_a_function_returns_a_FunctionInvokeExecutionFailed_message_and_a_502_error)

`502: invalid function response`

`FunctionInvokeInvalidResponse`

[Invoking a function returns a FunctionInvokeInvalidResponse message and a 502 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#Invoking_a_function_returns_a_FunctionInvokeInvalidResponse_message_and_a_502_error)

`502: Customer subnet DNS resolver error. Please fix the subnet configuration and try again`[Invoking a function returns a FunctionInvokeSubnetConfigError message and a 502 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#functionstroubleshooting_topic-subnet-config-error_response_and_a_502_error)

`502: The combined uncompressed size of all Function images in an application has exceeded the allowed limit. Please reduce the size of the images or number of functions from the application.`[Invoking a function returns "The combined uncompressed size of all Function images in an application has exceeded the allotted limit...." message and a 502 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#functionstroubleshooting_topic_Deploying_a_function_returns_uncompressed_size_of_images_exceeded_limit)

`502: Container failed to initialize, please ensure you are using the latest fdk and check the logs`

`'ModuleNotFoundError: No module named 'contextvars'`[Invoking a function returns a FunctionInvokeContainerInitFail error message, a 502 error, and a 'ModuleNotFoundError: No module named 'contextvars'' log message](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#modulenotfounderror)

`503: Timed out - server too busy`

`FunctionInvokeServiceUnavailable`[Invoking a function returns a FunctionInvokeServiceUnavailable message and a 503 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#functionstroubleshooting_topic_service_unavailable_response_and_a_503_error)
`504: Container failed to initialize, please ensure you are using the latest fdk and check the logs`[Invoking a function returns FunctionInvokeContainerInitTimeout and 'Container initialization timed out' messages, and a 504 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#pythontimeout)
`504: Timed out`[Invoking a function returns a FunctionInvokeTimeout message and a 504 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#timeoutexceeded)

`504: Container initialization timed out, please ensure you are using the latest fdk and check the logs`

`FunctionInvokeContainerInitTimeout`

[Invoking a function returns a FunctionInvokeContainerInitTimeout message and a 504 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#Invoking_a_function_returns_a_FunctionInvokeContainerInitTimeout_message_and_a_504_error)

`504: Image pull timed out`

`FunctionInvokeImagePullTimeout`

[Invoking a function returns a FunctionInvokeImagePullTimeout message and a 504 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#Invoking_a_function_returns_a_FunctionInvokeImagePullTimeout_message_and_a_504_error)

## Miscellaneous

Error number and message (if applicable) Description and link
`error getting credentials - err: exit status 1, out: Error spawning command line 'dbus-launch --autolaunch...`[When running OCI Functions on Ubuntu, Docker login returns an "error getting credentials - err: exit status 1..." message](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Miscellaneous-issues-when-using-Oracle-Functions.htm#When_running_Oracle_Functions_on_Ubuntu_Docker_login_returns_an_error_getting_credentials__err_exit_status_1_message)
