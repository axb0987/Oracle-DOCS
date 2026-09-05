# Advanced Concepts
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellconcepts.htm
- Fetched: 2026-09-05 01:36 CDT

# Advanced Concepts

This section covers PowerShell SDK concepts.

This section covers PowerShell SDK concepts.

## Managing Session Preferences

The OCI Modules for PowerShell support the use of environment variables in a PowerShell session to specify values some optional[common parameters](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellconcepts_topic_understanding_oci_cmdlets.htm#powershellconcepts_topic_understanding_oci_cmdlets_common_parameters). These[environment variables](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables)can be configured directly in the PowerShell session or by using the`Set-OCIClientSession`cmdlet. Values assigned to these environment variables are used for making API calls only in the PowerShell session in which they are set.

### Set Environment Variables Directly from PowerShellThe following environment variables can be used to specify values for some parameters used by the OCI Modules for PowerShell:

Cmdlet Parameter Environment Variable Name Note
[Region](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellconcepts_topic_understanding_oci_cmdlets.htm#powershellconcepts_topic_understanding_oci_cmdlets_common_parameters)OCI_PS_REGION If a value is not specfied, region value from the user preferred profile is used.
[Profile](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellconcepts_topic_understanding_oci_cmdlets.htm#powershellconcepts_topic_understanding_oci_cmdlets_common_parameters)OCI_PS_PROFILE If a value is not specified, the`DEFAULT`profile is used.
[ConfigFile](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellconcepts_topic_understanding_oci_cmdlets.htm#powershellconcepts_topic_understanding_oci_cmdlets_common_parameters)OCI_PS_CONFIG If a value is not specfied, config file at`~/.oci/config`will be used.
[NoRetry](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellconcepts_topic_understanding_oci_cmdlets.htm#powershellconcepts_topic_understanding_oci_cmdlets_common_parameters)OCI_PS_NORETRY If a value is not specified, default retry strategy is used to attempt retries.
[TimeOutInMillis](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellconcepts_topic_understanding_oci_cmdlets.htm#powershellconcepts_topic_understanding_oci_cmdlets_common_parameters)OCI_PS_TIMEOUT If a value is not specified, the default value of 100,000 milliseconds (100 seconds) is used.
[AuthType](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellconcepts_topic_understanding_oci_cmdlets.htm#powershellconcepts_topic_understanding_oci_cmdlets_common_parameters)OCI_PS_AUTH If a value is not specified, the API key defined in the config file is used.

For example, to set the region:

```

```

### Set Environment Variables using Cmdlets

You can use the Set-OCIClientSession and Get-OCIClientSession cmdlets to set and retrieve the session preference environment variables.

### Set-OCIClientSession

This cmdlet sets the`Region`,`Profile`and`Config`file preferences for the PowerShell session through the environment variables shown above.

Note  
  
Import`OCI.PSModules.Common`before running the following example.

```

```

To remove a session preference environment variable, run the`Clear-OCIClientSession`cmdlet with the appropriate parameters.

### Get-OCIClientSession

The`Get-OCIClientSession`cmdlet in the common module is used to retrieve the session preference values set for the[common parameters](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellconcepts_topic_understanding_oci_cmdlets.htm#powershellconcepts_topic_understanding_oci_cmdlets_common_parameters)from the current PowerShell session.

```

```

## Parameter Precedence

When evaluating parameters, the OCI Modules for PowerShell follows this order of precedence:
- The value specified in the[cmdlet parameter](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellconcepts_topic_understanding_oci_cmdlets.htm#powershellconcepts_topic_understanding_oci_cmdlets_common_parameters).
- The value specified in the[session preferences](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellconcepts.htm#powershellconcepts_topic_session_preferences).
- The value specified in the user-selected profile of the OCI configuration file located at`~/.oci/config`.
Note  
  

The OCI Modules for PowerShell use the`DEFAULT`profile as a fall back profile. Any value that isn't explicitly defined for a given profile is inherited from the DEFAULT profile.

## History Store

By default, OCI Cmdlets output the response body of the underlying REST API operation. The history store provides users with a PowerShell variable that can be used to look into OCI Cmdlet invocations and their complete API responses from OCI services.
Note  
  
Each PowerShell session gets its own history store.

You can use the history store to:

- Use the previous Cmdlet's response object values in the next Cmdlet
- Inspect the complete API response, including the response headers - for example, the use of e-tags for optimistic concurrency, or the`OpcNextPage`header for pagination
- Examine cmdlet invocation sequences for diagnostic purposes

The history store is encapsulated as an`Oci.PSModules.Common.Cmdlets.CmdletHistory.OCICmdletHistoryStore`object in a[PowerShell variable](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_variables)named`$OCICmdletHistory`.

For more information. see the[History Store example on GitHub](https://github.com/oracle/oci-powershell-modules/tree/master/Examples/HistoryStore_Identity.ps1).

### History Store Properties

This section explains the properties contained in the history store object stored in $OCICmdletHistory.

```

```

#### Size

Indicates the maximum number of commands that can be saved in the history store. The default value is 20. Valid values are from 1 and 100000 (inclusive). To modify the size of history store, use`Set-OCICmdletHistory`.

Note  
  
We recommend keeping the history size to a minimum to limit memory usage.

#### Entries

Collection of`Oci.PSModules.Common.Cmdlets.CmdletHistory.OCICmdletHistory`objects that allows indexed access to the stored history.

The`Oci.PSModules.Common.Cmdlets.CmdletHistory.OCICmdletHistory`object has the following properties:

Name Type Description
StartTime[System.DateTime](https://docs.microsoft.com/en-us/dotnet/api/system.datetime)Start time of cmdlet execution.
EndTime[System.DateTime](https://docs.microsoft.com/en-us/dotnet/api/system.datetime)End time of cmdlet execution.
Command[System.Management.Automation.InvocationInfo](https://docs.microsoft.com/en-us/dotnet/api/system.management.automation.invocationinfo)Describes how and where this command was invoked.
Response[System.Management.Automation.PSObject](https://docs.microsoft.com/en-us/dotnet/api/system.management.automation.psobject)Output object returned by the cmdlet.

#### LastResponse

A`System.Management.Automation.PSObject`object encapsulating the last OCI Cmdlet response in a PowerShell session.

### History Store Cmdlets

Oci.PSModules.Common module provides the following cmdlets for working with the History Store. See the[GitHub example](https://github.com/oracle/oci-powershell-modules/blob/master/Examples/HistoryStore_Identity.ps1).

#### Get-OCICmdletHistory

Gets the cmdlet history stored in the current PowerShell session.

#### Set-OCICmdletHistory

Sets properties of the history store.

#### Clear-OCICmdletHistory

Deletes the cmdlet history stored in the current PowerShell session.

## Pagination

OCI Cmdlets that invokes list API operations have the ability to paginate results, allowing you to retrieve the available results in batches (automatically following pagination tokens) until no more records are available.

Note  
  
Examples in this topic call the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/ListImages)ListImages`operation in the[Compute](https://docs.oracle.com/iaas/Content/Compute/home.htm)service. Be sure to import`OCI.PSModules.Core`before trying out the examples in this section.

### Get First Page Results

The default behavior of a cmdlet that supports pagination is to get only the first page of results when invoked without the`-Page`parameter specified.

For example, to get the first page of compute images available invoke the`Get-OCIComputeImagesList`with your[compartment ID](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm):

```

```

The above example implicitly sets the -Page parameter to NULL.

Note  
  
The maximum number of results per page is defined by the service and can be found in the service API reference.

### Limit Results

The`-Limit`parameter specifies the maximum number of results returned per page.

This example sets the maximum number of results returned per page to 5:

```

```

### Get Next Page Results

The`-Page`parameter is used to get the next page of results by passing the pagination token from the `opc-next-page` response header contained in the previous cmdlet response.
Note  
  

You can use the[history store](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellconcepts.htm#powershellconcepts_topic_history_store)to get the previous cmdlet response.

This example shows how to retrieve the results remaining from a previous paginated call by passing the`$OCICmdletHistory.LastResponse.OpcNextPage`property from the history store as the argument to the`-Page`parameter:.

```

```

### Get All Results

OCI Cmdlets that support pagination can auto paginate and fetch results from all available pages. Let the cmdlet do the pagination by passing`-All`switch parameter when running the cmdlet.

```

```

## Waiters and Asynchronous Calls

Most Oracle Cloud Infrastructure resources, such as compute instances, have lifecycles . In many cases, you want your command to wait until a resource or[work request](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/workrequests.htm)reaches a specific state, or a timeout is exceeded, before taking further action. You can poll a resource to determine its state.

OCI Modules for PowerShell offer waiter parameters that allow your cmdlet to wait until a resource reaches a desired state. A cmdlet with waiter parameters can be invoked in a blocking manner to wait until either one of the desired states is reached or a timeout is exceeded. Waiters abstract the polling logic that you would otherwise have to add before taking further actions on a resource or a workrequest.

For example, when you call`LaunchInstance`in the Compute service, the response header contains a`work-request-id`. The OCI Modules for PowerShell uses this ID when you specify the`-WaitForStatus`parameter, which causes your script to wait until the work request succeeds before proceeding.
For example:
```

```

### Waiter parameters

This section describes the parameters used for asynchronous calls.

WaitForStatus

Specify this parameter to perform the action and then wait until the resource reaches the desired lifecycle state. Multiple states can be specified, returning when the resource reaches one of the desired states.

WaitIntervalSeconds

Check every WaitIntervalSeconds to see whether the resource has reached one of the desired states. Default value for this parameter is 30 seconds.

MaxWaitAttempts

Maximum number of attempts to be made until the resource reaches one of the desired states. Default value for this parameter is 3 attempts.
Note  
  

Currently, OCI Cmdlets do not accept maximum wait time for cmdlets that support waiters. You can work around this limitation by controlling the values of MaxWaitAttempts and/or WaitIntervalSeconds.

On successful completion, the cmdlet returns the original response object received. In case of an error like the resource failing to reach the desired state within the given limits, an exception containing the error message would be thrown.

## Stream Inputs and Outputs

Some OCI Cmdlets interact with APIs that accept or return stream type objects (for example, the`InvokeFunctions`operation in the Functions service). These OCI cmdlets accept parameters that can take a file path and implicitly convert files to streams and back.
Note  
  
You can either pass a stream parameter or the equivalent file parameter, but not both. The file input parameter is named after the corresponding stream input parameter and file output parameter is named as`OutputFile`.
Note  
  
For an example, see the help text for the`Invoke-OCIFunctionsInvokeFunction`cmdlet in`OCI.PSModules.Functions`.

This[sample on GitHub](https://github.com/oracle/oci-powershell-modules/blob/master/Examples/Streams_ObjectStorage.ps1)shows how to work with streams.

## Logging

To facilitate troubleshooting, OCI Modules for PowerShell supports logging`debug`- and`verbose`-level messages on the console in addition to error messages. This feature has been integrated with the standard PowerShell[Debug](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_commonparameters#debug)and[Verbose](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_commonparameters#verbose)parameters.

Pass the`-Debug`or`-Verbose`parameters in the cmdlet invocation to see log messages on the console.

For example:

```

```

## Authenticating with Instance Principals

Instance principals is an IAM service feature that enables instances to be authorized actors (or principals) that can perform actions on service resources. Each compute instance has its own identity, and it authenticates using the certificates that are added to it. These certificates are automatically created, assigned to instances and rotated, preventing the need for you to distribute credentials to your hosts and rotate them.

Note  
  
For more information on instance principals, see[Calling Services from an Instance](https://docs.oracle.com/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm).

To enable instance principal authentication from OCI Cmdlets, call[authorize the instance](https://docs.oracle.com/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm#setup)and set the[AuthType](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellconcepts_topic_understanding_oci_cmdlets.htm#powershellconcepts_topic_understanding_oci_cmdlets_common_parameters)parameter. For example:

`PS /> Get-OCIIdentityRegionsList -AuthType``InstancePrincipal`

## Dedicated Endpoints

Dedicated endpoints are the endpoint templates defined by the service for a specific realm at the client level. The OCI Modules for PowerShell allow you to enable the use of this realm-specific endpoint templates feature at both the application level and at the client level. This feature is disabled by default.
Note  
  
The value set at client level takes precedence over the value set at the application level.

Enabling realm-specific endpoint templates at the application level:
To enable the realm-specific endpoint templates feature at the application level, set the environment variable`OCI_REALM_SPECIFIC_SERVICE_ENDPOINT_TEMPLATE_ENABLED`to`true`.
Note  
  
The boolean value is case-insensitive.

Enabling realm-specific endpoint templates at the client level:
To enable the realm-specific endpoint templates feature at the client level, set the flag in code as shown below:
```

```

For a full example, see the[CreateBucketUsingRealmSpecificEndpoint_ObjectStorage example on GitHub](https://github.com/oracle/oci-powershell-modules/tree/master/Examples/CreateBucketUsingRealmSpecificEndpoint_ObjectStorage.ps1).

## Dual-Stack Endpoints

Use dual-stack endpoints to connect to Oracle Cloud Infrastructure (OCI) services over both IPv6 and IPv4. Dual-stack support improves compatibility across modern and legacy networks and helps clients communicate seamlessly regardless of the IP protocol they use.

How dual-stack support works
- Many OCI services offer endpoints that support both IPv6 and IPv4.
- The OCI Java SDK lets you enable dual-stack at the application level or at the individual client level.
- If both are set, the client-level setting overrides the application-level setting.
- Dual-stack is disabled by default.

You can enable dual-stack endpoints in either of the following ways:
- At application level , set the environment variable`OCI_DUAL_STACK_ENDPOINT_ENABLED`to true. The value is a Boolean and is case-insensitive.
- At client level , set the flag in code as follows:

```

```
For example, see[CreateBucketUsingDualStackEndpoint_ObjectStorage.psl](https://github.com/oracle/oci-powershell-modules/tree/master/Examples/CreateBucketUsingDualStackEndpoint_ObjectStorage.ps1)
