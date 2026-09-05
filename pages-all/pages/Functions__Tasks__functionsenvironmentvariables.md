# Environment Variables Populated by OCI Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsenvironmentvariables.htm
- Fetched: 2026-09-05 02:08 CDT

# Environment Variables Populated by OCI Functions

Find out about the environment variables that OCI Functions populates.

OCI Functions populates a number of pre-defined environment variables that you can use within function code. Running functions can access environment variables directly, and can also access many environment variables via the FDK using a context variable passed to your handler function.

Custom configuration parameters are also available as environment variables (for more information, see[Passing Custom Configuration Parameters to Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionspassingconfigparams-about.htm)).

Running functions can access the following pre-defined environment variables:
- OCI Functions environment variables, which have names prefixed with`FN_`.
- OCI environment variables, which have names prefixed with`OCI_`. These variables are typically used to authenticate access to other OCI resources (see[Accessing Other Oracle Cloud Infrastructure Resources from Running Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsaccessingociresources.htm)).

## FN_ environment variables

Name Description
FN_FN_ID The OCID of the function.
FN_APP_ID The OCID of the application into which the function is grouped.
FN_FN_NAME The name of the function.
FN_APP_NAME The name of the application into which the function is grouped.
FN_MEMORY The amount of memory available to the function, in MB.
FN_TYPE How the function is being executed. Either`sync`(synchronously) or`async`(asynchronously).
FN_LISTENER The path to the file descriptor to which the FDK binds in order to receive invocations.

## OCI_ environment variables

Name Description
OCI_RESOURCE_PRINCIPAL_REGION The region in which the function is running (for example,`us-phoenix-1`).
OCI_RESOURCE_PRINCIPAL_VERSION The resource principal version in use by the function (for example,`2.2`).
OCI_RESOURCE_PRINCIPAL_RPST The path to a file containing the resource principal session token for the function.
OCI_RESOURCE_PRINCIPAL_PRIVATE_PEM The path to the private key file used to sign requests that use the function's resource principal.
OCI_TRACING_ENABLED Whether Application Performance Monitoring (APM) tracing is enabled for the function (see[Distributed Tracing for Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstracing.htm)). Either`0`(APM tracing is not enabled) or`1`(APM tracing is enabled).
OCI_TRACE_COLLECTOR_URL If Application Performance Monitoring (APM) tracing is enabled, the APM domain URL with data key for the function.
OCI_REGION_METADATA

A JSON object containing information describing where the function is running. For example:
```

```
