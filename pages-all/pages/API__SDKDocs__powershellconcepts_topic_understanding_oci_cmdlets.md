# Working with Cmdlets
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellconcepts_topic_understanding_oci_cmdlets.htm
- Fetched: 2026-09-05 01:36 CDT

# Working with Cmdlets

This section describes how to use the OCI Modules for PowerShell cmdlets.

The OCI Modules for PowerShell cmdlets are built on the Oracle Cloud Infrastructure SDK for .NET. These cmdlets make calls to Oracle Cloud Infrastructure REST APIs with the passed cmdlet parameter values.

Note  
  
Cmdlet parameters are named corresponding to the respective REST API parameters as listed in the[API reference](https://docs.oracle.com/iaas/api/).

The OCI REST APIs use HTTPS requests and responses. For more information, see[About the API](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/usingapi.htm).

## Cmdlet Discovery

OCI Cmdlets are named using a verb -noun pair pattern, where verb is the operation performed on the resource denoted by the noun , which usually includes the service name followed by the name of the resource in that service.

For example, the following command returns all cmdlets available to work with a compute instance resource in the[Compute service](https://docs.oracle.com/iaas/Content/Compute/home.htm), which is part of the OCI Core PowerShell module:

```

```

Note  
  

The standard[Get-Command](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-command)can be used to find cmdlets present in any module.

## Sample Cmdlet

This example shows how to invoke a simple OCI cmdlet that calls the`[](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Namespace/GetNamespace)GetNamespace`operation of the[OCI Object Storage service](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm). This operation returns the name of the Object Storage namespace for the user making the request.

Note  
  
Install and import the ObjectStorage service before trying out this example. For more information, see[Installation](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellgettingstarted.htm#powershellsdkgettingstarted_topic_install_modules).

```

```

## Cmdlet Help

To get help information for a cmdlet, use the[Get-Help](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-help)cmdlet, passing in the name of the cmdlet as a parameter.

Note  
  
For more detailed help information, use the`-Full`parameter. This example shows help output for the`Get-OCIObjectStorageNamespace`cmdlet:

```

```

## Common Parameters

This section describes the optional global cmdlet parameters common to all cmdlets present in any OCI PowerShell service module.

### ConfigFile

The path to the[configuration file](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/sdkconfig.htm)that supplies credentials for the Oracle Cloud.

### Endpoint

Indicates the service endpoint to use for OCI API calls, including any required API version path. For example,`https://audit.us-ashburn-1.oraclecloud.com`

### FullResponse

By default, OCI Cmdlets output the response body of the REST API operation. Including the`FullResponse`[switch parameter](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced_parameters#switch-parameters)indicates that the cmdlet should output the complete response returned by the API operation wrapped in its associated .NET type (an object containing API response headers in-addition to an optional response body).

### NoRetry

A switch parameter to disable default retry logic for calls to services.

By default, OCI Modules for PowerShell retry failed API calls that return status codes 400, 401, 404, 409, 429 and 500. Retry attempts use an exponential backoff algorithm with a maximum of 5 attempts over a maximum time span of 10 minutes. Include this switch parameter in the cmdlet invocation to disable the default retry logic.

### Profile

Specifies which profile to load from the configuration file. This parameter expects a case-sensitive profile name existing in the configuration file.

### Region

Specifies the[Region-ID](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)of the region to make calls against. For example:`us-phoenix-1`or`ap-singapore-1`.

### TimeOutInMillis

Specifies the maximum wait time in milliseconds for the API request to complete. The default value is 100,000 milli-seconds (100 seconds).

### AuthType

Defines the type of authentication to use for making API requests. By default the API Key in your config file is used. Valid values are`ApiKey`or`InstancePrincipal`.

## Cmdlet Input and Output

This section describes how the OCI Cmdlets process input and output.

### Cmdlet Input

OCI Cmdlets currently accept inputs from command line parameters or through[pipeline by property names](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_pipelines?view=powershell-7#methods-of-accepting-pipeline-input). To see an example on passing inputs through pipeline by property name refer this[sample](https://github.com/oracle/oci-powershell-modules/blob/master/Examples/PipelineCleanup_ResourceSearch.ps1).

### Cmdlet Output

By default, OCI Cmdlets return only the API response body encapsulated in an associated .NET type. For use cases that require the users to inspect the complete API response including the response headers, use the`[](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellconcepts_topic_understanding_oci_cmdlets.htm#cmdlet_input_and_output)FullResponse`switch parameter in the cmdlet invocation.

In the following example, the`GetConfiguration`operation in the[OCI Audit service](https://docs.oracle.com/iaas/Content/Audit/Concepts/auditoverview.htm)returns a`Configuration`resource in the response body.

Note  
  
To run the following example, import`OCI.PSModules.Audit`.

```

```

In the example output above, the default invocation only returns the .NET object that encapsulates the API response body.

To get an output object that includes the complete API response include the`-FullResponse`parameter in the cmdlet invocation. For example:

```

```

### Asynchronous Calls

For Oracle Cloud APIs that return an[asynchronous work request](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/workrequests.htm)response, with`opc-work-request-id`in the response header and no response body, OCI PowerShell Cmdlets return a`Oci.PSModules.Common.Cmdlets.WorkRequest`object containing the`OpcWorkRequestId`property.

For example:

```

```

### Error Handling

If an error occurs when running an OCI Cmdlet, the cmdlet throws a[terminating error](https://docs.microsoft.com/en-us/powershell/scripting/developer/cmdlet/terminating-errors)
