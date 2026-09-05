# Concepts
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/javasdkconcepts.htm
- Fetched: 2026-09-05 01:36 CDT

# Concepts

This topic explains some of the key concepts for using the Oracle Cloud Infrastructure SDK for Java.

## Synchronous Calls

To make synchronous calls, create an instance of the synchronous client. The general pattern for synchronous clients is that for a service named Example, there will be an interface named ExampleService, and the synchronous client implementation will be called ExampleServiceClient. Here's an example of creating an Object Storage client:

```

```

Synchronous calls will block until the response is available. All SDK APIs return a response object (regardless of whether or not the API sends any content back). The response object typically contains at least a request ID that you can use when contacting Oracle support for help on a particular request.

```

```

## Asynchronous Calls

To make asynchronous calls, create an instance of the asynchronous client. The general pattern for asynchronous clients is that for a service named Example, there will be an interface named ExampleServiceAsync, and the asynchronous client implementation will be called ExampleServiceAsyncClient. Here's an example of creating an Object Storage client:

```

```

Asynchronous calls return immediately. You need to provide an AsyncHandler that will be invoked after the call completes either successfully or unsuccessfully:

```

```

## Polling with Waiters

The SDK offers waiters that allow your code to wait until a specific resource reaches a desired state. A waiter can be invoked in both a blocking or a non-blocking (with asychronous callback) manner, and will wait until either the desired state is reached or a timeout is exceeded. Waiters abstract the polling logic you would otherwise have to write into an easy-to-use single method call.

Waiters are obtained through the service client (`client.getWaiters()`). Both a`Get<Resource>Request`and the desired lifecycle state are passed in to the`waiters.for<Resource>`method. For example:

```

```

Each`waiters.for<Resource>`method has two versions:
- 

One version uses the default polling values. For example:
```

```

- 

The other version gives you full control over how long to wait and how much time between polling attempts. For example:
```

```

## Threading Model

A client becomes thread-safe when it is initialized. After setting its endpoint, you can safely use a client in multiple threads and concurrently call methods on it.

You can reuse a client on multiple requests, both across concurrent threads or within a single thread. Unless the environment's resources are constrained, you should only close the client immediately before it goes out of scope.
Note  
  
This guarantee applies only to the default JAX-RS implementation, Jersey. When using an alternate implementation, you must manage thread safety yourself. For more information, see[Configuring the SDK](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/javasdkgettingstarted.htm#Configur)

## Uploading Large Objects

The Object Storage service supports multipart uploads to make large object uploads easier by splitting the large object into parts. The SDK for Java supports raw multipart upload operations for advanced use cases, as well as a higher level upload class that uses the multipart upload APIs.[Using Multipart Uploads](https://docs.oracle.com/iaas/Content/Object/Tasks/usingmultipartuploads.htm)provides links to the APIs used for multipart upload operations. Higher level multipart uploads are implemented using the[UploadManager](https://docs.oracle.com/iaas/tools/java/latest/com/oracle/bmc/objectstorage/transfer/UploadManager.html), which will: split a large object into parts for you, upload the parts in parallel, and then recombine and commit the parts as a single object in storage.

The[UploadObject](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/UploadObjectExample.java)example shows how to use the UploadManager to automatically split an object into parts for upload to simplify interaction with the Object Storage service.

## Retries

Starting with version 2.10.0, the SDK for Java is configured by default to retry certain SDK operations that fail. The SDK allows you to specify the strategy to use for how retries are handled, including the number of times to retry, the condition under which the SDK should retry an operation, and when to stop retrying an operation. You can set these parameters at the client level and at the individual request level.

To determine which service operations have retries enabled by default, refer to the service operations's description in the SDK.

Note  
  
Retries are not currently supported for asynchronous clients

By default, the SDK will retry operations HTTP response status codes 409 (with an IncorrectState error code), 429, 500, 502, 503, 504, timeout errors (such as HTTP connection and read timeouts), request connection errors, request exceptions, and circuit breaker exceptions.

The most current default retry configuration and the list of errors that can be retried can be[viewed on Github](https://github.com/oracle/oci-java-sdk/blob/master/bmc-common/src/main/java/com/oracle/bmc/retrier/RetryConfiguration.java#L31).

Disabling Default Retries

To opt-out of the default retries feature, you can do one the following :
- Set the environment variable`OCI_SDK_DEFAULT_RETRY_ENABLED`to`false`to disable default retries globally
- 

Override the default retries for a particular client instance. This example shows overriding the default retries for the`objectStorageClient`:
```

```

```

```

- 

Override default retries for a particular request instance. This example shows overriding retries for`putObjectRequest`:
```

```

Retry Behavior Precedence

- Any retry configuration that you explicitly define at the request level will override the client level retry configuration or the global level retry configuration and the environment variable override, for that specific request instance.
- Any retry configuration explicitly defined at the client level will override the global retry configuration and the environment variable level override, for that particular client instance.

### Retry Strategies

You can specify the strategy to use for how retries are handled, including the number of times to retry, the condition under which the SDK should retry an operation, and when to stop retrying an operation. You can set these parameters at the client level and at the individual request level.
Note  
  
The most current default retry configuration and the list of errors that can be retried can be[viewed on Github](https://github.com/oracle/oci-java-sdk/blob/master/bmc-common/src/main/java/com/oracle/bmc/retrier/RetryConfiguration.java#L31).

Delay Strategy

The`delayStrategy`parameter determines how long to wait between each retry call. There are two options for this parameter:
- `FixedTimeDelayStrategy (milliseconds)`- Each retry is delayed by a specified number of milliseconds.
- `ExponentialBackoffDelayStrategy (milliseconds)`- The delay time for subsequent retry calls increases by an exponential factor of 2 until it reaches the defined maximum delay (in milliseconds), with a base value of one millisecond.

The default delay strategy is set to`ExponentialBackoffDelayStrategy`with a jitter value between 0-1000 milliseconds and a maximum wait time between calls of 30 seconds.

Retry Condition

The`retryCondition`defines a function with an error argument that returns a boolean indicating whether to retry or not. The operation will be retried if this function returns`true`.

Termination Strategy

The`terminationStrategy`parameter defines when to terminate the retry attempts. This parameter supports the following options:
- `MaxTimeTerminationStrategy (milliseconds)`- Defines total duration in milliseconds for which the retry attempts.
- `MaxAttemptsTerminationStrategy (attempts)`- Defines the total number of retry attempts.

The default termination strategy for OCI SDKs is a`MaxAttemptsTerminationStrategy`of`8`.

#### Retry Examples

Java

This example shows how to configure and use retries with the SDK for Java:

```

```

## Circuit Breakers

Starting with version 2.10.0, the SDK for Java provides default support for circuit breakers for service clients that have enabled default SDK circuit breakers. Circuit breakers help prevent the client from overwhelming the service by blocking the requests from being sent to the service after a certain failure threshold is reached.

Note  
  
Default circuit breakers are not currently supported for asynchronous clients.

For default circuit breakers, all errors that can be retried will be treated as failures for the circuit breakers. To determine which service clients have circuit breakers enabled, refer to the service client's description in the SDK.

Note  
  
The default circuit breaker configuration can be viewed on[Github](https://github.com/oracle/oci-java-sdk/blob/master/bmc-circuitbreaker/src/main/java/com/oracle/bmc/circuitbreaker/CircuitBreakerConfiguration.java).

Circuit Breaker Configuration

The following parameters define a circuit breaker:

- Failure Rate Threshold - the state of the circuit breaker changes from CLOSED to OPEN when the failure rate is equal or greater than this hreshold. For example, when more than 50% of the recorded calls have failed, the circuit breaker will open.
- Reset Timeout - the timeout after which an open circuit breaker will attempt a request if a request is made
- Failure Exceptions - the list of exceptions that will be regarded as failures for the circuit
- Minimum number of calls/ Volume threshold - the minimum number of calls which are required (per sliding window period) before the circuit breaker can calculate the error rate

Default Circuit Breaker Configuration

The following is the default circuit breaker configuration:

- Failure Rate Threshold: 80%. When 80% of the requests calculated for a time window of 120 seconds have failed, the circuit will transition from closed to open.
- Minimum number of calls / volume threshold : 10, for the above defined time window of 120 seconds.
- Reset Timeout : The circuit breaker will wait 30 seconds before setting the breaker to the`halfOpen`state and trying the action again.
- Failure Exceptions : The failures for the circuit will only be recorded for retryable or transient exceptions. HTTP response codes 409 (with an IncorrectState), 429, 500, 502, 503, and 504, HTTP request and other timeouts, request connection errors and exceptions are all treated as failures that will trigger a circuit breaker.

Disabling the Default Circuit Breaker

To opt out of the default circuit breaker feature, you can do one of the following:

- Set the environment variable`OCI_SDK_DEFAULT_CIRCUITBREAKER_ENABLED`to`false`.
- Change the default circuit breaker configuration for a client instance. The following example shows how to do this with an`IdentityClient`instance:
```

```

Circuit Breaker Behavior Precedence

Any circuit breaker configuration that you explicitly define at the client level will override the global default circuit breaker configuration and the environment level override for that client.

For additional information on circuit breakers and the default circuit breaker configuration, see[this example on Github](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/CircuitBreakerExample.java).

## Raw Requests

Raw requests are useful, and in some cases necessary. Typical use cases are: when using your own HTTP client, making a OCI-authenticated request to an alternate endpoint, and making a request to a OCI API that is not currently supported in the SDK. The SDK for Java exposes the`DefaultRequestSigner`class that you can use to create a`RequestSigner`instance for non-standard requests.

The[Raw Request](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/RawRestCallExample.java)example on GitHub shows how to:
- create an authentication provider and request signer
- integrate with an HTTP client (Jersey in this example) to authenticate requests

## Setting the Endpoints

Service endpoints can be set in three ways.
- Call`setEndpoint()`on the service instance. This lets you specify a full host name (for example, https://www.example.com).
- Call`setRegion()`on the service instance. This selects the appropriate host name for the service for the given region. However, if the service is not supported in the region you set, the SDK for Java returns an error.
- Pass the region in the configuration file. For more information, see[SDK and CLI Configuration File](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/sdkconfig.htm).

Note that a service instance cannot be used to communicate with different regions. If you need to make requests to different regions, create multiple service instances.

### Dedicated Endpoints

Dedicated endpoints are the endpoint templates defined by the service for a specific realm at the client level. OCI Java SDK allows you to enable the use of the realm-specific endpoint templates feature at both the application level and at the client level. This feature is disabled by default.
Note  
  
The value set at client level takes precedence over the value set at the application level.

Enabling realm-specific endpoint templates at the application level:
To enable the realm-specific endpoint templates feature at the application level, set the environment variable`OCI_REALM_SPECIFIC_SERVICE_ENDPOINT_TEMPLATE_ENABLED`to`true`.
Note  
  
The boolean value is case-insensitive.

Enabling realm-specific endpoint templates at the application level:

To enable the realm-specific endpoint templates feature at the client level, set the flag in code as shown:

For the OCI SDK for Java:

```

```

For a full example, see the[UseRealmSpecificEndpointsExample on Github](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/UseRealmSpecificEndpointsExample.java).

For the legacy OCI SDK for Java:
```

```

For a full example, see the[UseRealmSpecificEndpointsExample on GitHub](https://github.com/oracle/oci-java-sdk/blob/legacy/v2/master/bmc-examples/src/main/java/UseRealmSpecificEndpointsExample.java).

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
For example, see[EnableDualStackEndpointsExample.java](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/EnableDualStackEndpointsExample.java)

## Forward Compatibility and enums

If you have conditional logic based on an enum, be sure that your code handles the`UnknownEnumValue`case to ensure forward compatibility. Some response fields are of type enum, but in the future, individual services might return values not covered by existing enums for that field. To address this possibility, every response field of type enum has an additional value named`UnknownEnumValue`. If a service returns a value that's not recognized by the SDK version, then the response field is set to this value.

## New Region Support

If you're using a version of the SDK released prior to the announcement of a new region, you can use a workaround to reach it.

A region is a localized geographic area. For more information on regions and how to identify them, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

A realm is a set of regions that share entities. You can identify your realm by looking at the domain name at the end of the network address. For example, the realm for`xyz.abc.123.oraclecloud.com`is`oraclecloud.com`.

You must first call`Region.register`to register the new region, and then you can set the region by either using the configuration file or by calling the`setRegion`method.

Note  
  
After a region is registered, the federation endpoint is no longer required while using instance principals. For an example, see[https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/NewRegionAndRealmSupportWithoutSDKUpdate.java](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/NewRegionAndRealmSupportWithoutSDKUpdate.java).

### oraclecloud.com Realm

For regions in the`oraclecloud.com`realm, you can pass new region names just as you would pass ones that are already defined in the[Region](https://docs.oracle.com/iaas/tools/java/latest/com/oracle/bmc/Region.html)enum for your SDK version.
Note  
  
For the following code samples, be sure to supply the appropriate endpoints for your region.

If you're using version 1.2.34 or later of the SDK for Java, you can pass the new region name as a string using one of the following methods:
- 

To set the region on a previously created client:

```

```

- 

To set a region when building a new client:

```

```

- You can also pass the region in the configuration file. For more information, see[SDK and CLI Configuration File](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/sdkconfig.htm).

### Other Realms

For regions in realms other than`oraclecloud.com`, you can use the following workarounds to reach new regions with earlier versions of the SDK.
To specify the endpoint:

```

```

If you're authenticating via instance principals, you can set the endpoint and federationEndpoint via the following process:

```

```

## Paginated Responses

Some APIs return paginated result sets, so you must check for additional items and if necessary, fetch the next page. You can do so manually or you can use an iterator.

### Manually Fetching Pages

The Response objects contain a method to fetch the next page token. If the token is null, there are no more items. If it is not null, you can make an additional request, by setting the token on the`Request`object, to get the next page of responses.
Note  
  
Some APIs may return a token even if there are no additional results. Be sure to also check whether any items were returned and stop if there are none.

This example shows how to handle page tokens returned by the Object Storage API:

```

```

### Using an Iterator

Instead of manually working with page tokens, you can use an iterator. Each service client exposes a`getPaginators()`method that returns a`Paginator`object. This object contains methods to return objects of type[Iterable](https://docs.oracle.com/javase/7/docs/api/java/lang/Iterable.html). We support two approaches to using iterable :
- Response Iterator : You can iterate over the`Response`objects that are returned by the list operation. These are referred to as ResponseIterators , and their methods are suffixed with "ResponseIterator," for example, listUsersResponseIterator .

```

```

- Record Iterator : You can iterate over the resources/records that are listed. These are referred to as RecordIterator , and their methods are suffixed with "RecordIterator," for example, listUsersRecordIterator .

```

```

## Client-Side Encyption

Client Side Encryption allows you to encrypt data on the client side before storing it locally or using it with other Oracle Cloud Infrastructure services.

To use client-side encryption, you must create a master encryption key (MEK) using the Key Management Service. This can be done using the[CreateKey](https://docs.oracle.com/iaas/api/#/en/key/latest/Key/CreateKey)or[ImportKey](https://docs.oracle.com/iaas/api/#/en/key/latest/Key/ImportKey)operations.

The MEK is used to generate a Data Encryption Key (DEK) to encrypt each payload. A encrypted copy of this DEK (encrypted under the MEK) and other pieces of metadata are included in the encrypted payload returned by the SDKs so that they can be used for decryption.

### Java Prerequisites

The[unlimited policy files for earlier releases](https://www.oracle.com/java/technologies/javase-jce8-downloads.html)are required only for JDK 8, 7, and 6 updates earlier than 8u161, 7u171, and 6u16. For those versions and later the policy files are included but not enabled by default.

Current versions of the JDK do not require these policy files. They are provided here for use with older versions of the JDK. JDK 9 and later ship with the unlimited policy files and use them by default.

### Examples

The following code example shows how to encrypt a string:

```

```

The following example shows how to encrypt a file stream:

```

```

## Exception Handling

When handling an exception, you can get more information about the HTTP request that caused it, such as the status code or timeout. You can also get the request ID when handling a`BmcException`by using the`getOpcRequestId`method.

This example shows a try-catch block that handles a`BmcException`and prints the request ID.

```

```

Exceptions in the SDK for Java are runtime exceptions (unchecked), so they do not show up in method signatures. All APIs can throw a`BmcException`
