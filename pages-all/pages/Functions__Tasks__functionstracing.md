# Distributed Tracing for Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstracing.htm
- Fetched: 2026-09-05 02:09 CDT

# Distributed Tracing for Functions

Find out how to enable tracing and view function traces when debugging with OCI Functions.

When a function is invoked but doesn't run or perform as expected, you need to investigate the issue at a detailed level. The distributed tracing feature observes the function's execution as it moves through the different components of the system. You can trace and instrument standalone functions to debug execution and performance issues. You can also use function tracing to debug issues with complete serverless applications comprising multiple functions and services, such as:
- a function calling another function
- a function calling other services such as the Object Storage service
- a function that serves as a backend for an API gateway deployed in the API Gateway service
- a function triggered in response to an event by the Events service, Notifications service, or Connector Hub

The OCI Functions tracing capabilities are provided by the Oracle Cloud Infrastructure Application Performance Monitoring service. Features in Application Performance Monitoring (APM) enable you to identify and troubleshoot failures and latency issues in the functions you create and deploy.

In the Application Performance Monitoring service:
- An APM domain contains the systems monitored by Application Performance Monitoring. An APM domain is an instance of a collector of trace and span data which stores, aggregates, displays, and visualizes the data.
- A trace is the complete flow of a request as it passes through all the components of a distributed system in a given time period. It consists of an entire tree of spans all related to the same single overall request flow.
- A span is an operation or a logical unit of work with a name, start time, and duration, within a trace. A span is a time segment associated with the duration of a unit of work within the overall request flow.

The Application Performance Monitoring Trace Explorer enables you to visualize the entire request flow and explore trace and span details for diagnostics. You can view and monitor slow traces and traces with errors. To isolate and identify trace issues, you can drill down into specific spans, such as page loads, AJAX calls, and service requests. For more information about the Application Performance Monitoring service, see[Application Performance Monitoring](https://docs.oracle.com/iaas/application-performance-monitoring/home.htm).

To enable tracing for a function, you must:
- Set up a policy to give the OCI Functions service permission to access APM domains, if the policy does not exist already (see[Policy Statements to Give the OCI Functions Service and OCI Functions Users Access to Tracing Resources](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingpolicies.htm#usertracingpolicy)).
- Set up an APM domain.
- Enable tracing for the Functions application and select the APM domain you created.
- Enable tracing for one or more functions.

When you enable tracing for a function, OCI Functions automatically generates a "default function invocation span." The default span captures information about the function's execution context including the overall time taken to process the request and return a response to the caller. In addition to the default function invocation span, you can add code to functions to define custom spans. Use custom spans to capture more function-specific information to help with debugging. For example, you might define custom spans to capture the start and end of specific units of work. For example, units of work could include getting the database password from the Vault, opening a database connection, and retrieving records from the database.

Four variables have been added to the OCI Functions context that provide helpful tracing information. These variables include:
- `FN_APP_NAME:`The function application name.
- `FN_FN_NAME:`The function name.
- `OCI_TRACE_COLLECTOR_URL`: The APM domain URL with data key.
- `OCI_TRACING_ENABLED:`Is tracing enabled?
- When retrieved from environment variables, returns 0 or 1.
- When retrieved from the function context, returns`true`or`false`as appropriate for the language used.

## Required IAM Policy for Enabling Tracing

Before you can enable tracing, the group to which you belong must have permission to access existing APM domains or to create APM domains. In addition, OCI Functions must have permission to access APM domains. See[Policy Statements to Give the OCI Functions Service and OCI Functions Users Access to Tracing Resources](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingpolicies.htm#usertracingpolicy).

## Using the Console to Enable Tracing and View Function Traces

A couple of steps are required to enable tracing and to view function traces for the Oracle Cloud Infrastructure Application Performance Monitoring (APM) service. First, enable tracing for the application containing the function. Then, enable tracing for one or more functions. You can then view function traces in the APM Trace Explorer.

### Using the Console to Enable Tracing

To enable tracing, follow these steps.
- On the Applications list page, select the application with functions for which you want to enable tracing. If you need help finding the list page or the application, see[Listing Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/list-applications.htm).
- Select the Monitoring tab and go to the Traces section.
- To enable tracing for the application:
- From the the Actions menu (three dots) , select Configure and specify:
- Compartment: The compartment in which to create the trace. By default, the current compartment.
- APM Domain: The APM domain (defined in the Application Performance Monitoring service) in which to create the trace. To use an existing APM Domain, select an existing APM domain from the list. Or, to create a new APM domain, select APM Domain . For more information about APM domains, see[Getting Started with Application Performance Monitoring](https://docs.oracle.com/iaas/application-performance-monitoring/doc/get-started-application-performance-monitoring.html).
Note  
  
The APM Domain needs to have both public and private data keys for function tracing to work. If the keys do not exist, you can create them through the console interface.
- Select Enable Trace to enable tracing for the application.

Having enabled tracing for the Functions application, you can now enable tracing for one or more functions in the application.
- To enable tracing for specific functions in the application:
- Select the Functions tab.
- Select the Enable Trace option from the the Actions menu (three dots) for the function(s) for which you want to enable tracing.

The Enable Trace option is only shown if you have previously enabled tracing for the application. Note the following:
- If the Enable Trace option is not shown, you must enable tracing for the application. If you haven't already enabled tracing for the application, see the previous step.
- If you previously enabled tracing for the application but later disabled it, an Enable application tracing link is shown. Select the Enable application tracing link to re-enable tracing for the application (see the previous step). Having re-enabled tracing for the application, you can then enable tracing for specific functions.

When you have enabled tracing for the application and one or more functions, you can view function traces.

### Using the Console to View Function Traces

To view the traces for functions that have tracing enabled:
- On the Applications list page, select the application containing the functions for which you want to view traces. If you need help finding the list page or the application, see[Listing Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/list-applications.htm).
- To see traces for functions:
- To see traces for all the functions that have tracing enabled in the application:
- Select the Monitoring tab and go to the Traces section.
- Select the name of the trace.
Note  
  
A trace name is only shown if you have already enabled tracing for the application.
- To see the trace for a specific function that has tracing enabled:
- Select the Functions tab.
- Select the View Trace option from the the Actions menu (three dots) for the function for which you want to view the trace.
Note  
  
The View Trace option is only shown if you have already enabled tracing for the function.

The traces for the functions you selected are shown in the APM Trace Explorer. By default, a trace is shown for the default function invocation span, and any custom spans defined for the function.
- In the APM Trace Explorer:
- Select a trace to see the spans for that trace.
- Select a span to see the details captured for that span.

For more information about using the APM Trace Explorer, see[Use Trace Explorer](https://docs.oracle.com/iaas/application-performance-monitoring/doc/use-trace-explorer.html).

## Tracing a Chain of Functions

By default, function tracing provides a trace for an entire function invocation. However, often with modern cloud applications, you need to chain function invocations. OCI Functions tracing provides the ability trace the execution of a function invoked by another function. This ability means you can examine the execution of each function in a chain of calls in a single tree of spans in APM trace explorer.

To trace a chain of functions, you need to propagate the X-B3 headers`X-B3-TraceId`,`X-B3-SpanId`,`X-B3-ParentSpanId`, and`X-B3-Sampled`in the function invocation request from your function code.

After the function has run, the trace data from your functions is collected and available in APM Trace Explorer. For more information about using the APM Trace Explorer, see[Use Trace Explorer](https://docs.oracle.com/iaas/application-performance-monitoring/doc/use-trace-explorer.html).

[Tracing a Chain of Functions with Python](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstracing.htm#)

Here's an example of how you can trace a chain of functions. If you want to try you this example, you need to create two sample functions. Follow these steps to set up your functions.
- Create your tracing Python function:`fn init --runtime python <your-function-name-1>`
- Create your "Hello World!" Python function:`fn init --runtime python <your-function-name-2>`
- Deploy both functions:`fn -v deploy --app <app-name>`
- Get the second functions OCID and invoke endpoint:`fn inspect function your-app-name your-function-name-2`
- Create JSON file to pass the required information into the first function. For example, your`test.json`file might look like this:

```

```

- When the first function is invoked, you can pass the second functions information using`test.json`:`fn invoke <app-name> <your-function-name-1> < test.json`

Now you are ready to update the first function with the required code updates.

#### Configure Packages

Update your`requirements.txt`file to include the following packages:

```

```

Save the file.

#### Update your Function Code to Propagate the X-B3 Headers

The Python function calls the`handler`function and passes in the JSON information from the invoke command. The`handler`function is broken in into several small blocks to simplicity. The complete source file is provided at the bottom of this section.

#### Load the JSON Data

In this first part, the JSON data is loaded from the function invocation.

```

```

#### Create Invoke Client and Gather Header Information

Create the Functions invoke client using the OCI Python SDK and Functions resource principals. Then, retrieve the`tracing_context`and extract the required information to create the HTTP headers.

```

```

#### Propagate the X-B3 Headers

The OCI Python SDK lets you[set custom headers](https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/customize_service_client/setting_custom_headers.html). Use this technique to pass the X-B3 headers in to the second function invocation. Header information is passed for`trace_id`,`span_id`,`parent_span_id`, and`is_sampled`. Finally, the second function is invoked with`client`and the response is passed to this function's response.

```

```

[Review Complete Function Source Code](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstracing.htm#)

Here is the complete source code for the sample Python function.

```

```

## Adding Custom Spans to Functions

With function tracing enabled, the default function invocation span provides a trace for the entire function invocation. The default span can provide good information, but when investigating your code you might want to dig deeper. Custom spans are added directly to your code and allow you to define spans for a method or a block of code. The resulting data provides a better picture of your function as it runs.

Before you can use custom spans, you must enable tracing for your application and functions using the Oracle Cloud Infrastructure Application Performance Monitoring (APM) service. To set up tracing, you must:
- Set up a policy to give the OCI Functions service permission to access APM domains, if the policy does not exist already (see[Policy Statements to Give the OCI Functions Service and OCI Functions Users Access to Tracing Resources](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingpolicies.htm#usertracingpolicy)).
- Set up an APM domain.
- Enable tracing for the Functions application and select the APM domain you created.
- Enable tracing for one or more functions.

These steps have already been covered. However, a couple more things are required for custom spans:
- Select a distributed tracing client library, for example Zipkin.
- Add client libraries to your function dependencies.
- In your function code, use the`OCI_TRACING_ENABLED`function context variable to check if tracing is enabled.
- In your function code, use the`OCI_TRACE_COLLECTOR_URL`function context variable to send your custom spans to your APM domain.
- Add instrumentation to your function code.
Note  
  

To use custom spans, you must have the following minimum versions of the Fn Project FDKs:
- Java FDK: 1.0.129
- Python FDK: 0.1.22
- Node FDK: 0.0.20

[Adding Custom Spans to Java Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstracing.htm#)

Here's an example of how to use Zipkin to add custom spans to your Java function. If you want to try you this example, you can create a Java "Hello World!" function and add custom span code. To create a sample function:
- Create a Java function:`fn init --runtime java apm-fn-java`
- For simplicity, remove the`src/test`directory.

#### Configure Maven

Add the following dependencies to the &lt;dependencies&gt; section of your Maven`pom.xml`file.

```

```

Save the file.

#### The HandleRequest Method

Observations about the method follow the`handleRequest`source code.

```

```

- The`TracingContext tracingConext`object passes in all the APM-related information needed to make connections to the APM service.
- The`intializeZipkin`method is called which updates the`tracingContext`and creates a`tracer`object which is used to set up custom spans.
- A`span`is created for the parent custom span. Then three methods are called in the scope of the parent span.
- Notice in the`finally`block all the tracing objects are closed out.

#### The initializeZipkin Method

Observations about the`intializeZipkin`method follow the source code.

```

```

- The`traceContext`is passed in to create all the objects used to create custom spans.
- The`apmURL`is retrieved from the`getTraceCollectorURL()`method. The URL is the endpoint to the APM domain and is used to create the`tracer`object which builds the custom spans.
- A builder takes the`zipkinSpanHandler`and the service name to create a`tracer`object. This`tracer`object is used to create custom spans.

#### Creating Custom Spans

With the`tracer`object initialized, custom spans can be created.

```

```

- The`method1`method creates a custom span named "Method1."

[Review Complete Function Source Code](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstracing.htm#)

Here is the complete source code for the sample Java tracing function.

```

```

[Adding Custom Spans to Python Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstracing.htm#)

Here's an example of how to use Zipkin to add custom spans to your Python function. If you want to try you this example, you can create a Python "Hello World!" function and add custom span code. To create a sample function:
- Create a Python function:`fn init --runtime python apm-fn-python`

#### Configure Packages

Update your`requirements.txt`file to include the following packages:

```

```

Save the file.

#### Creating Handler Class and Parent Custom Span

The Python function calls the`handler`function and passes in the function context to create custom spans.

```

```

- The`tracing_context`is passed from the function context and contains all the information needed to create and configure custom spans.
Note  
  
If tracing is not enabled, the tracing context is an empty object. With an empty tracing context, the`is_sampled`flag is set to`None`and`py_zipkin`does not emit spans.
- The`with zipkin_span`statement is used to create spans.
- The information in`tracing_context`is used to get the`service_name`, call the`transport_handler`, and set the`zipking_attrs`.
- A custom span name is specified just by setting`span_name`.
- Tracing attributes required for Zipkin are retrieved from the tracing context:`tracing_context.zipkin_attrs()`.
- With the custom span setup, the main block runs boilerplate "Hello World!" code. With the only exception, a call to the`example`function.

#### The transport_handler Function

The`transport_handler`function communicates with the APM domain with messages about span execution.

```

```

- The`trace_collector_url`is returned from the function context. This URL provides the communication endpoint for your custom spans to the APM domain.

#### Creating a Custom Span in Example Function

The example function demonstrates the creation of a custom span.

```

```

- The`with zipkin_span`statement is used to identify the custom span and give it a name.
- The`example_span_context`block raises an exception and returns an error message.

[Review Complete Function Source Code](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstracing.htm#)

Here is the complete source code for the sample Python tracing function.

```

```

[Adding Custom Spans to Node Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstracing.htm#)

Here's an example of how to use Zipkin to add custom spans to your Node.js function. If you want to try you this example, you can create a Node "Hello World!" function and add custom span code. To create a sample function:
- Create a Node function:`fn init --runtime node apm-fn-node`

#### Configure Node Dependencies

Update your`package.json`file to include the following packages:

```

```

Save the file.

#### Update Handle Method

Key observations about the`fdk.handle`method follow the source code.

```

```

- The`tracer`is created and then used to create a parent custom span. Then child spans are created for the`fetchResource`,`processResource`, and`updateResource`functions.

#### Reviewing the createOCITracer Function

Key observations about the function follow the source code.

```

```

- The function context (`ctx`) is passed to this function which provides the information required to connect to the APM domain. If you follow the function calls, you can see how the tracing IDs and fields are built.

[Review Complete Function Source Code](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstracing.htm#)

Here is the complete source code for the sample Node tracing function.

```

```

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use these API operations to enable and disable tracing for applications and the functions they contain:
- [CreateApplication](https://docs.oracle.com/iaas/api/#/en/functions/latest/Application/CreateApplication)
- [UpdateApplication](https://docs.oracle.com/iaas/api/#/en/functions/latest/Application/UpdateApplication)
- [CreateFunction](https://docs.oracle.com/iaas/api/#/en/functions/latest/Function/CreateFunction)
- [UpdateFunction](https://docs.oracle.com/iaas/api/#/en/functions/latest/Function/UpdateFunction)
