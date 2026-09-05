# Invoking Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm
- Fetched: 2026-09-05 02:08 CDT

# Invoking Functions

Find out the different ways to invoke functions deployed to OCI Functions.

You can invoke a function that you've deployed to OCI Functions in different ways:
- Using the Fn Project CLI (suitable for development environments, but not recommended for production systems).
- Using the Oracle Cloud Infrastructure CLI.
- Using the Oracle Cloud Infrastructure SDKs.
- Making a signed HTTP request to the function's invoke endpoint. Every function has an invoke endpoint.

Each of the above invokes the function via requests to the API. Any request to the API must be authenticated by including a signature and the OCID of the compartment to which the function belongs in the request header. Such a request is referred to as a 'signed' request. The signature includes Oracle Cloud Infrastructure credentials in an encrypted form.

If you use the Fn Project CLI or the Oracle Cloud Infrastructure CLI to invoke a function, authentication is handled for you. See[Using the Fn Project CLI to Invoke Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm#usingfncli)and[Using the Oracle Cloud Infrastructure CLI to Invoke Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm#usingocicli).

If you use an Oracle Cloud Infrastructure SDK to invoke a function, you can use the SDK to handle authentication. See[Using SDKs to Invoke Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm#usingsdks).

If you make a signed HTTP request to a function's invoke endpoint, you'll have to handle authentication yourself by including a signature and the OCID of the compartment to which the function belongs in the request header. You can do this in different ways:
- Using the Oracle Cloud Infrastructure CLI`raw-request`command. See[Sending a Signed Request to a Function's Invoke Endpoint (using the Oracle Cloud Infrastructure CLI raw-request command)](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm#rawrequestinvoke).
- Writing code to programmatically sign requests. For information about the required credentials and how to sign the requests, see[Request Signatures](https://docs.oracle.com/iaas/Content/API/Concepts/signingrequests.htm).

How you invoke a function, and the invocation type you specify, determines the maximum amount of time the function can run and other execution behaviors.

Using the Fn Project CLI to invoke functions is only suitable for development environments. We do not recommend using the Fn Project CLI to invoke functions in production systems.
Tip  
  
If you aren't able to successfully complete one of the steps in this topic, review the solutions for common problems (see[Troubleshooting OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting.htm)).

## Synchronous and Detached Invocation Types

When you invoke a function, you can specify a type for the function invocation. The function invocation type determines responsibility for result handling, when control is returned to the caller, and the HTTP status code that is returned, as follows:
- Sync: If you specify Sync as the function invocation type (the default), OCI Functions executes the request synchronously. On successful completion, OCI Functions issues an HTTP 200 status code and returns the result to the caller, along with control.
- Detached: If you specify Detached as the function invocation type, OCI Functions executes the request asynchronously. As soon as processing begins, OCI Functions issues an HTTP 202 status code and returns control to the caller. The function itself is responsible for result handling.

Specifying Sync as the function invocation type is also known as invoking the function in Sync mode, or as synchronous invocation. Specifying Detached as the function invocation type is also known as invoking the function in Detached mode, or as detached invocation.

Detached invocation can be better than synchronous invocation for functions that take a long time to run, because detached invocation supports a longer execution timeout, and also supports additional configuration options for post-execution delivery destinations (see[Invoking Functions in Detached Mode](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm#functionsinvokingdetachedfunctions)).The benefits of detached invocation are typically very useful for functions that you schedule to run on a recurring schedule. Therefore, functions that you schedule are always invoked with Detached as the invocation type (see[Scheduling Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsschedulingfunctions-about.htm)).

To specify the function invocation type:
- When invoking a function using the OCI CLI`fn function invoke`command, use the`--fn-invoke-type`parameter. For example:
```

```

- When invoking a function from another function using one of the FDKs, specify the invocation type in the function call. For example, using the Python FDK:
```

```

- When invoking a function using the OCI CLI`raw-request`command, include`"fn-invoke-type"`in the`--request- headers`parameter. For example:
```

```

## Function Timeout, Function Invocation Timeout, and Function Execution Timeout

Function timeout can be more precisely defined as:
- Function invocation timeout , which refers to the length of time a client invoking a function will wait for a response from the function before giving up.
- Function execution timeout , which refers to the length of time OCI Functions will allow a function to run for, before terminating the execution.

When you invoke a function with Sync as the invocation type, the function invocation timeout and the function execution timeout are effectively the same. However, when you invoke a function with Detached as the invocation type, the Detached invocation timeout (`detachedModeTimeoutInSeconds`) parameter controls the function execution timeout, and is separate to the function invocation timeout.

How you invoke a function, and the invocation type you specify, determine the maximum amount of time the function can run for, as follows:
- If you invoke a function using the Fn Project CLI (with Sync as the invocation type), the Synchronous invocation timeout (`timeoutInSeconds`) parameter you specify in the function definition is applied (default is 30 seconds). See[Changing Default Memory and Timeout Settings](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscustomizing.htm).
- If you invoke a function using the Oracle Cloud Infrastructure CLI (with Sync as the invocation type), the value of the OCI CLI`--read-timeout`global parameter is applied (default is 60 seconds). See[oci fn function invoke](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fn/function/invoke.html).
- If you invoke a function using the Oracle Cloud Infrastructure SDKs (with Sync as the invocation type), the read timeout specified for the client is applied. For example, see the[Java SDK](https://docs.oracle.com/iaas/tools/java/latest/)and[Python SDK](https://docs.oracle.com/iaas/tools/python/latest//api/functions/client/oci.functions.FunctionsInvokeClient.html)documentation.
- If you invoke a function using the PL/SQL SDK, the value of`UTL_HTTP.set_transfer_timeout`is applied (default is 60 seconds).
- If you invoke a function from the DBMS_CLOUD REST API using DBMS_CLOUD.SEND_REQUEST, the value of`UTL_HTTP.set_transfer_timeout`is applied (default is 60 seconds).
- 

If you invoke a function with Detached as the invocation type, the Detached invocation timeout (`detachedModeTimeoutInSeconds`) parameter you specify in the function definition is applied (between 5 seconds and 3600 seconds, or 1 hour). If you invoke a function with Detached as the invocation type and the Detached invocation timeout (`detachedModeTimeoutInSeconds`) parameter is not set, the value of the Synchronous invocation timeout (`timeoutInSeconds`) parameter is applied. See[Invoking Functions in Detached Mode](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm#functionsinvokingdetachedfunctions).

## Using the Fn Project CLI to Invoke Functions

Note  
  
Using the Fn Project CLI to invoke functions is only suitable for development environments. We do not recommend using the Fn Project CLI to invoke functions in production systems.

To invoke a function deployed to OCI Functions using the Fn Project CLI:
- 

Log in to your development environment as a functions developer.
- 

In a terminal window, enter:

```

```

where:
- `<app-name>`is the name of the application containing the function you want to invoke
- `<function-name>`is the name of the function you want to invoke

For example:

```

```

Output:
```

```

Enter`fn invoke functions --help`to see more invoke options.
Tip  
  

If you want to pass arguments and values to a function, prefix the`fn invoke`command with`echo -n '<argument>=<value>' |`

If the function is expecting the argument and value as JSON, use a valid JSON format. For example:

```

```

Output:
```

```

## Using the Oracle Cloud Infrastructure CLI to Invoke Functions

If you have installed the Oracle Cloud Infrastructure CLI, you can use it to send API requests to invoke functions. Among other things, the Oracle Cloud Infrastructure CLI will facilitate Oracle Cloud Infrastructure authentication. For information about using the Oracle Cloud Infrastructure CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).

These instructions assume:
- you have already installed and configured the Oracle Cloud Infrastructure CLI
- you want to invoke a function as the functions developer that's configured for your development environment

To invoke a function using the Oracle Cloud Infrastructure CLI:
- 

Log in to your development environment as a functions developer.
- 

In a terminal window, enter:

```

```

where:
- `<function-ocid>`is the OCID of the function you want to invoke. To find out a function's OCID, use the`fn inspect`command to see the value of the function's`id`property (see[Listing Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsviewingfunctionsapps.htm)).
- `<output-filepath>`is the path and name of a file to write the response to. To write the response to stdout, specify`--file "-"`
- `<request-parameters>`are optionally arguments and values to pass to the function. If the function is expecting arguments and values as JSON, use a valid JSON format. For example,`--body '{"name":"John"}'`. Note that you must include`--body ""`in the request, even if there are no request parameters to pass.

For example:
- 

```

```

Output:
```

```

- 

```

```

Output:
```

```

## Using SDKs to Invoke Functions

If you're writing a program to invoke a function in a language for which an Oracle Cloud Infrastructure SDK exists, we recommend you use that SDK to send API requests to invoke the function. Among other things, the SDK will facilitate Oracle Cloud Infrastructure authentication.

Note that when using an SDK to invoke a function, you do not specify the entire invoke endpoint that you specify when using the Oracle Cloud Infrastructure CLI`raw-request`command (see[Obtaining a Function's Invoke Endpoint](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm#obtainingendpoint)). Instead, only specify the first part of the function's invoke endpoint. For example, when using an SDK, do not specify the function's invoke endpoint as`https://fht7ns4mn2q.us-phoenix-1.functions.oci.oraclecloud.com/20181201/functions/ocid1.fnfunc.oc1.phx.aaaa____uxoa/actions/invoke`. Instead, specify the function's invoke endpoint as`https://fht7ns4mn2q.us-phoenix-1.functions.oci.oraclecloud.com`.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[InvokeFunction](https://docs.oracle.com/iaas/api/#/en/functions/latest/Function/InvokeFunction)API operation to invoke functions.

## Obtaining a Function's Invoke Endpoint

When invoking a function using the Oracle Cloud Infrastructure CLI`raw-request`command, you have to specify the function's invoke endpoint.

To obtain a function's invoke endpoint:
- 

Log in to your development environment as a functions developer.
- 

In a terminal window, enter:

```

```

where:
- `<app-name>`is the name of the application containing the function for which you want to obtain the invoke endpoint
- `<function-name>`is the name of the function for which you want to obtain the invoke endpoint

For example:

```

```

Output:
```

```

The function's invoke endpoint is the value of`"fnproject.io/fn/invokeEndpoint"`. For example,`"https://fht7ns4mn2q.us-phoenix-1.functions.oci.oraclecloud.com/20181201/functions/ocid1.fnfunc.oc1.phx.aaaa____uxoa/actions/invoke"`(abbreviated for readability).

## Sending a Signed Request to a Function's Invoke Endpoint (using the Oracle Cloud Infrastructure CLI raw-request command)

If you have installed the Oracle Cloud Infrastructure CLI, you can use it to send API requests to invoke functions. Among other things, the CLI will facilitate Oracle Cloud Infrastructure authentication. For more information about using the Oracle Cloud Infrastructure CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).

These instructions assume:
- you have already installed and configured the Oracle Cloud Infrastructure CLI
- you want to invoke a function as the functions developer that's configured for your development environment

To invoke a function deployed to OCI Functions by sending a signed request to the function's invoke endpoint using the Oracle Cloud Infrastructure CLI`raw-request`command:
- 

Log in to your development environment as a functions developer.
- 

Obtain the function's invoke endpoint (see[Obtaining a Function's Invoke Endpoint](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm#obtainingendpoint)).

For example,`"fnproject.io/fn/invokeEndpoint": "https://fht7ns4mn2q.us-phoenix-1.functions.oci.oraclecloud.com/20181201/functions/ocid1.fnfunc.oc1.phx.aaaa____uxoa/actions/invoke"`(abbreviated for readability).
- 

Use the Oracle Cloud Infrastructure CLI`raw-request`command to invoke the function by sending a signed POST request to the function's invoke endpoint by entering:

```

```

where:
- `<invoke-endpoint>`is the endpoint you obtained in the earlier step.
- `<request-parameters>`are optionally arguments and values to pass to the function. If the function is expecting arguments and values as JSON, use a valid JSON format. Note that you must include`--request-body ""`in the request, even if there are no request parameters to pass.

For example:
- 

```

```

Output:

```

```

- 

```

```

Output:
```

```

- If a passphrase was provided to encrypt the API signing key, enter the passphrase when prompted.

## Invoking Functions in Detached Mode

Invoke a function with Detached as the invocation type when:
- You want to invoke a function that takes a long time to run.
- You want the function to run asynchronously, so that control is returned to the caller immediately after the function is invoked without waiting for the results of the invocation.
- You want to specify destinations to which to send the results of successful and failed invocations.

Detached invocation enables long-running workloads (such as large ETL tasks, AI/ML jobs, and integrations) to finish without being constrained by the synchronous invocation timeout.

### Specifying the Timeout and Destinations for Detached Invocations of a Function

When creating or updating a function, you can optionally set:
- the Detached invocation timeout (`detachedModeTimeoutInSeconds`) parameter to specify the function execution timeout for detached invocations
- the Success destination and Failure destination (`successDestination`and`failureDestination`respectively), to specify destinations to which to send the results of detached invocations. Note that the success and failure destinations apply only to detached invocations. If you specify a success and/or failure destination, OCI Functions delivers:
- An invocation record to the success destination when a detached invocation succeeds.
- An invocation record to the failure destination when a detached invocation fails.

Supported destinations for the results of detached invocations are the Notifications service, the Queue service, and the Streaming service. Note that to write to the destination service, OCI Functions requires IAM policy permissions (see[Creating IAM Policies for Detached Invocation Success and Failure Destinations](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm#functionsinvokingdetachedfunctions__section_detached-invocation-policies)).

You can use the Console, the Fn Project CLI, the OCI CLI, and the API to specify the timeout and destinations for detached invocations.

For example, you might enter the following OCI CLI command to create a function that, when invoked with an invocation type of Detached, executes for up to 1800 seconds before timing out, and for which the results of successful and failed invocations are sent to the destinations specified in`success-dest.json`and`failure-dest.json`respectively:
```

```

where:
- `success-dest.json`contains the following JSON string:
```

```

- `failure-dest.json`contains the following JSON string:
```

```

See[`SuccessDestinationDetails`](https://docs.oracle.com/iaas/api/#/en/functions/latest/datatypes/SuccessDestinationDetails)and[`FailureDestinationDetails`](https://docs.oracle.com/iaas/api/#/en/functions/latest/datatypes/FailureDestinationDetails)in the API documentation for the attributes to specify for different destination services.

### Creating IAM Policies for Detached Invocation Success and Failure Destinations

OCI Functions requires IAM permissions to write the results of detached invocations to the success and failure destinations you specify in function definitions. The Notifications service, the Streaming service, and the Queue service are supported success and failure destinations. If the permissions don't exist already, you have to create appropriate IAM policies that include the necessary policy statements.

For example:
- To enable OCI Functions to write the results of detached invocations to success and failure destinations in the Notifications service, include a policy statement similar to the following in an IAM policy:
```

```

- To enable OCI Functions to write the results of detached invocations to success and failure destinations in the Queue service, include a policy statement similar to the following in an IAM policy:
```

```

- To enable OCI Functions to write the results of detached invocations to success and failure destinations in the Streaming service, include a policy statement similar to the following in an IAM policy:
```

```

### Invoking Functions in Detached Mode

Having set a function's Detached invocation timeout (`detachedModeTimeoutInSeconds`) property to the required function execution timeout, and optionally provided success and failure destinations for invocation results (along with appropriate policy statements to enable OCI Functions to access those destinations), you are ready to invoke the function and specify Detached as the invocation type.

For example:
- 

To invoke a function in detached mode using the OCI CLI`fn function invoke`, enter a command similar to the following:
```

```

- 

To invoke a function in detached mode using the OCI CLI`raw-request`command, enter a command similar to the following:
```

```

### Detached Invocation Results Delivery

If you provided success and failure destinations for the results of detached invocations of a function (and created appropriate policy statements to enable OCI Functions to access those destinations), OCI Functions delivers:
- An invocation record to the success destination when a detached invocation succeeds.
- An invocation record to the failure destination when a detached invocation fails.

Example invocation record for successful invocation:
```

```

Example invocation record for failed invocation:
```

```

OCI Functions delivers invocation records in the format expected by the destination.

If OCI Functions cannot deliver an invocation record to its destination (for example, due to missing permissions), you can use logs and metrics to track delivery failures.

### Monitoring and Metrics

To differentiate between Sync and Detached invocation types, the`FunctionExecutionDuration`,`FunctionInvocationCount`, and`FunctionResponseCount`metrics include the`InvokeType`dimension.

To track successful and failed deliveries of invocation records to destinations, use the`FunctionDetachedDeliveries`metric.

For more information about OCI Functions metrics, see[Function Metrics](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Reference/functionsmetrics.htm).

### Tips for Troubleshooting Issues with Detached Invocations

If you encounter issues with detached invocations, or if invocation records are not delivered:
- Double-check that the necessary IAM permissions exist to grant OCI Functions access to the target destination (see[Creating IAM Policies for Detached Invocation Success and Failure Destinations](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm#functionsinvokingdetachedfunctions__section_detached-invocation-policies)).
- Use the OCI Logging service to review failure messages. If OCI Functions could not deliver an invocation record to a target destination, it includes the reason in the invoke logs in OCI Logging. The log entry begins`Invocation record delivery to failure destination failed due to - ...`(see[Storing and Viewing Function Logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsexportingfunctionlogfiles.htm)).
- Use the`FunctionDetachedDeliveries`metric to review delivery details and errors (see[Function Metrics](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Reference/functionsmetrics.htm)). For failed deliveries to target destinations, the metric's`responseType`
