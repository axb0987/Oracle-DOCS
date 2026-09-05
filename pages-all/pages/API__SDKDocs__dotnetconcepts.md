# Concepts
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/dotnetconcepts.htm
- Fetched: 2026-09-05 01:36 CDT

# Concepts

This topic explains some of the key concepts for using the Oracle Cloud Infrastructure SDK for .NET.

This topic explains some of the key concepts for using the Oracle Cloud Infrastructure SDK for .NET.

## Raw Requests

Raw requests can be useful, and in some cases necessary. Typical use cases include using your own HTTP client, making a OCI-authenticated request to an alternate endpoint, or making a request to a OCI API that is not currently supported in the SDK. The SDK for .NET exposes the`OciHttpClientHandler`class that you can use to create a client handler which signs the request.

[This raw request example on GitHub](https://github.com/oracle/oci-dotnet-sdk/blob/master/Examples/RawRestCallExample.cs)shows how to use the`OciHttpClientHandler`.

## Setting the Endpoints

Service endpoints can be set in several ways:
- Call`SetEndpoint(<YOUR_ENDPOINT>)`on the service client instance. This lets you specify a full host name (for example,`https://www.example.com`).
- Call`SetRegion(<YOUR_REGION_ID>)`on the service client instance. This selects the appropriate host name for the service for the given region. However, if the service is not supported in the region you set, the SDK for .NET returns an error.
- Call`SetRegion(<Region>)`on the service client instance. For example,`SetRegion(Region.US_PHOENIX_1).`
- Pass the region in the configuration file. For more information, see[SDK and CLI Configuration File](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/sdkconfig.htm).

An example on setting endpoint can be found on[GitHub](https://github.com/oracle/oci-dotnet-sdk/blob/master/Examples/NonRegionalClientExample.cs).

Note that a service client instance cannot be used to communicate with different regions. If you need to make requests to different regions, create multiple service client instances.

### Dedicated Endpoints

Dedicated endpoints are the endpoint templates defined by the service for a specific realm at the client level. The OCI .NET SDK allows you to enable the use of this realm-specific endpoint templates feature at both the application level and at the client level. This feature is disabled by default.
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

For a full example, see the[UseRealmSpecificEndpointsExample on GitHub](https://github.com/oracle/oci-dotnet-sdk/blob/master/Examples/UseRealmSpecificEndpointsExample.cs).

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
For example, see[EnableDualStackEndpointsExample.cs](https://github.com/oracle/oci-dotnet-sdk/blob/master/Examples/EnableDualStackEndpointsExample.cs)

## New Region Support

If you are using a version of the SDK released prior to the announcement of a new region, you can use a workaround to reach it.

A region is a localized geographic area. For more information on regions and how to identify them, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

A realm is a set of regions that share entities. You can identify your realm by looking at the domain name at the end of the network address. For example, the realm for`xyz.abc.123.oraclecloud.com`is`oraclecloud.com`.

You must first call`Region.Register()`to register the new region, and then you can set the region by either using the configuration file or by calling the`SetRegion`method.

An example on adding a new region can be found on[GitHub](https://github.com/oracle/oci-dotnet-sdk/blob/master/Examples/AddNewRegionAndRealm.cs).

### oraclecloud.com Realm

For regions in the oraclecloud.com realm, you can pass new region names just as you would pass ones that are already defined in the`Region`enum for your SDK version.

To set the region:

```

```

### Other Realms

For regions in realms other than oraclecloud.com, you can use the following workarounds to reach new regions with earlier versions of the SDK.

To set the region:

```

```

## Uploading Large Objects

The Object Storage service supports multipart uploads to make large object uploads easier by splitting the large object into parts. The SDK for .NET supports raw multipart upload operations for advanced use cases, as well as a higher level upload class that uses the multipart upload APIs.[Using Multipart Uploads](https://docs.oracle.com/iaas/Content/Object/Tasks/usingmultipartuploads.htm)provides links to the APIs used for multipart upload operations. Higher level multipart uploads are implemented using the[UploadManager](https://docs.oracle.com/iaas/tools/java/latest/com/oracle/bmc/objectstorage/transfer/UploadManager.html), which will: split a large object into parts for you, upload the parts in parallel, and then recombine and commit the parts as a single object in storage.

The[UploadObject](https://github.com/oracle/oci-dotnet-sdk/blob/master/Examples/UploadManagerExample.cs)example shows how to use the UploadManager to automatically split an object into parts for upload to simplify interaction with the Object Storage service.

## Retries

You can configure the SDK for .NET to retry SDK operations that fail. The SDK allows you to specify the strategy to use for how retries are handled, including the number of times to retry, the condition under which the SDK should retry an operation, and when to stop retrying an operation. You can set these parameters at the client level and at the individual request level.

Delay Strategy

You can define your own delay strategy with the GetNextDelayInSeconds property. The SDK for .NET provides two different Delay Strategies::
- `GetFixedDelayInSeconds (seconds)`- Each retry is delayed by a specified number of seconds.
- `GetExponentialDelayInSeconds`- The delay time for subsequent retry calls increases by an exponential factor of 2.

Termination Strategy

You can define a termination strategy with two properties:
- `TotalElapsedTimeInSecs (seconds)`- Defines total duration in seconds for which the retry attempts.
- `MaxAttempts (attempts)`- Defines the total number of retry attempts.

Retryable Status Code Families
You can specify a list of status codes to retry using the`RetryableStatusCodeFamilies`property. For example:
```

```

Retryable Errors
This property is a collection of integer and string tuples containing status and error codes returned by a service error for which the SDK can retry. For example:
```

```

### Retry Examples

.NET

This example shows how to configure and use retries with the SDK for .NET:

```

```

## Paginated Responses

For large result sets, most OCI calls supported paginated responses. Paginated responses require you to make multiple calls to the list operation, passing in the value of the most recent response's next token. The pagination module allows you to:
- Load all possible results from a list call in one call
- Lazily load results using token-based paginated responses

For an example on how to use these functions, please see[GitHub](https://github.com/oracle/oci-dotnet-sdk/blob/master/Examples/PaginationExample.cs).

## Polling with Waiters

The SDK offers waiters that allow your code to wait until a specific resource reaches a desired state. A waiter can be invoked in both a blocking or a non-blocking (with asychronous callback) manner, and will wait until either the desired state is reached or a timeout is exceeded. Waiters abstract the polling logic you would otherwise have to write into an easy-to-use single method call.

Waiters are obtained through the service client (`client.Waiters`). Both a`Get<Resource>Request`and the desired lifecycle state are passed in to the`Waiters.For<Resource>`method.

For example:

```

```

Each`waiters.for<Resource>`method has two versions:

One version uses the default polling values. For example:

```

```

The other version gives you full control over how long to wait and how much time between polling attempts. For example:

```

```

Some API requests return work request identifiers to track the progress of the request. Waiters can be used to wait until the work request has reached the desired state.

For example:

```

```

Further examples on waiters can be found on[Github](https://github.com/oracle/oci-dotnet-sdk/blob/master/Examples/WaitersExample.cs).

## Exception Handling

When handling an exception, you can get more information about the HTTP request that caused it, such as the status code or service code. You can also get the request ID when handling an exception by looking at the`opcRequestId`property of the error object.

For example:

```

```

## Authenticating with Instance Principals

Instance principals is an IAM service feature that enables instances to be authorized actors (or principals) that can perform actions on service resources. Each compute instance has its own identity, and it authenticates using the certificates that are added to it. These certificates are automatically created, assigned to instances and rotated, preventing the need for you to distribute credentials to your hosts and rotate them.
Note  
  
For more information on instance principals, see[Calling Services from an Instance](https://docs.oracle.com/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm).
While using the .NET SDK on an OCI Instance, you can use`InstancePrincipalsAuthenticationDetailsProvider`class as shown in the following example. You will not need to provide your authentication details when you use this class.
```

```

A full working example of using instance principals with the OCI .NET SDK can be found on[GitHub](https://github.com/oracle/oci-dotnet-sdk/blob/master/Examples/InstancePrincipalExample.cs)
