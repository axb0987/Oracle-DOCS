# Concepts
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/typescriptsdkconcepts.htm
- Fetched: 2026-09-05 01:37 CDT

# Concepts

This topic explains some of the key concepts for using the SDK for TypeScript and JavaScript.

This topic explains some of the key concepts for using the SDK for TypeScript and JavaScript.

## Raw Requests

Raw requests are useful, and in some cases necessary. Typical use cases are: when using your own HTTP client, making a OCI-authenticated request to an alternate endpoint, and making a request to a OCI API that is not currently supported in the SDK. The SDK for TypeScript and JavaScript exposes the DefaultRequestSigner class that you can use to create an instance and call signHttpRequest.

The[Raw Request example on GitHub](https://github.com/oracle/oci-typescript-sdk/tree/master/examples/typescript/raw-request.ts)shows how to create an instance of DefaultRequestSigner and call signHttpRequest.

## Uploading Large Objects

The Object Storage service supports multipart uploads to make large object uploads easier by splitting the large object into parts. The SDK for TypeScript and JavaScript supports a higher level upload class that uses the multipart upload APIs.[Managing Multipart Uploads](https://docs.oracle.com/iaas/Content/Object/Tasks/usingmultipartuploads.htm#Using_Multipart_Uploads)provides links to the APIs used for multipart upload operations. Higher level multipart uploads are implemented using the[UploadManager](https://docs.oracle.com/iaas/tools/typescript/latest/classes/_objectstorage_lib_upload_manager_upload_manager_.uploadmanager.html), which will: split a large object into parts for you, upload the parts in parallel, and then recombine and commit the parts as a single object in storage. The[UploadObject](https://github.com/oracle/oci-typescript-sdk/blob/master/examples/typescript/uploadmanager.ts)example shows how to use the UploadManager to automatically split an object into parts for upload to simplify interaction with the Object Storage service.

## Retries

Starting with version 2.8.0, the SDK for TypeScript and JavaScript is configured by default to retry SDK operations that fail using the default retry policy. To determine which service operations have retries enabled by default, refer to the service operations's description in the SDK.
Note  
  
Default retry attempts for operations with binary or stream bodies (for example putObject or uploadPart) are only made if the`backupBinaryBody`property for the default retry configuration is set to`true`, or if you do not provide the content-length in the request.

By default, the SDK will retry operations HTTP response status codes 409 (with an IncorrectState error code), 429, 500, 502, 503, 504, timeout errors (such as HTTP connection and read timeouts), request connection errors, request exceptions, and circuit breaker exceptions.

Note  
  
The most current default retry configuration and the list of errors that can be retried can be seen on[Github](https://github.com/oracle/oci-typescript-sdk/blob/master/lib/common/lib/retrier.ts#L90).

Disabling Default Retries
To opt-out of the default retries feature, you can do one of the following :
- Set the environment variable`OCI_SDK_DEFAULT_RETRY_ENABLED`to`false`to disable default retries globally.
- Override the global default retry configuration:
```

```

- Override the default retries for a particular client instance. This example shows overriding the default retries for the`objectStorageClient`:
```

```

- Override default retries for a particular request instance. This example shows overriding retries for`putObjectRequest`:
```

```

Retry Behavior Precedence
- Any retry configuration that you explicitly define at the request level will override the client level retry configuration or the global level default retry configuration and the environment variable override for that specific request.
- Any retry configuration explicitly defined at the client level will override the global default retry configuration and the environment variable level override for the particular client.
- Default retry configuration set at the global level programmatically will override the environment variable level override.

### Retry Strategies

You can specify the strategy to use for how retries are handled, including the number of times to retry, the condition under which the SDK should retry an operation, and when to stop retrying an operation. You can set these parameters at the client level and at the individual request level.

Delay Strategy

The`delayStrategy`parameter determines how long to wait between each retry call. There are two options for this parameter:
- `FixedTimeDelayStrategy (seconds)`- Each retry is delayed by a specified number of seconds.
- `ExponentialBackoffStrategy (seconds)`- The delay time for subsequent retry calls increases by an exponential factor of 2 until it reaches the defined maximum delay (in seconds), with a base value of one second.

The default delay strategy is set to`ExponentialBackoffDelayStrategy`with a jitter value between 0-1000 milliseconds and a maximum wait time between calls of 30 seconds.

Retry Condition
The`retryCondition`defines a function with an error argument that returns a boolean indicating whether to retry or not. The operation will be retried if this function returns`true`.
Note  
  
For all requests with binary/stream bodies, retries are only attempted if`RetryConfiguration.backupBinaryBody`is set to`true`, or if the original stream body is able to be retried. By default, stream bodies will be not be backed up. Stream bodies will only be backed up if`backupBinaryBody`is set to`true`or if you don't provide the content-length in the request.

Termination Strategy

The`terminationStrategy`parameter defines when to terminate the retry attempts. This parameter supports the following options:
- `MaxTimeTerminationStrategy (seconds)`- Defines total duration in seconds for which the retry attempts.
- `MaxAttemptsTerminationStrategy (attempts)`- Defines the total number of retry attempts.

The default termination strategy for OCI SDKs is a`MaxAttemptsTerminationStrategy`value of`8`.

#### Retry Examples

TypeScript

This example sets the retry configuration at the client level:

```

```

This example sets the retry configuration at the request level:
```

```

To change the default retry condition programmatically:
```

```

JavaScript

This example sets the retry configuration at the client level:
```

```

This example sets the retry configuration at the request level:
```

```

To change the default retry condition programmatically:
```

```

## Polling with Waiters

The OCI SDK for TypeScript offers waiters that allow your code to wait until a specific resource reaches a desired state. A waiter will wait until either the desired state is reached or a timeout is exceeded. Waiters abstract the polling logic you would otherwise have to write into an easy-to-use single method call.

Waiters are obtained through the service client`client.createWaiter()`. Waiters take in an optional configuration object for users to control over how long to wait and how much time between polling attempts. The following example demonstrates how to create a waiter with the optional configuration:
```

```

## Circuit Breakers

Starting with version 2.8.0, the SDK for Typescript and Javascript provides default support for circuit breakers . Circuit breakers help prevent the client from overwhelming the service by blocking the requests from being sent to the service after a certain failure threshold is reached. For default circuit breakers, all errors that can be retried will be treated as failures for the circuit breakers.

Note  
  
The default circuit breaker configuration can be viewed on[Github](https://github.com/oracle/oci-typescript-sdk/blob/master/lib/common/lib/circuit-breaker.ts).

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

- Set the environment variable`OCI_SDK_DEFAULT_CIRCUITBREAKER_ENABLED`to`false`to disable default circuit breakers globally.
- Disable the global default circuit breakers programmatically:
```

```

- Override the global default circuit breaker configuration:
```

```

Note  
  
Overriding the global default retry configuration will enable circuit breakers with the defined configuration for all the service clients.
- Override the default circuit breaker configuration for a particular client instance. This example shows overriding the default circuit breaker for the`objectStorageClient`:
```

```

Circuit Breaker Behavior Precedence

Any circuit breaker configuration that you explicitly define at the client level will override the global default circuit breaker configuration and the environment level override for that particular client.

Circuit Breaker Examples

For TypeScript examples, see[Github](https://github.com/oracle/oci-typescript-sdk/blob/master/examples/typescript/circuit-breaker.ts).

For JavaScript examples, see[Github](https://github.com/oracle/oci-typescript-sdk/blob/master/examples/javascript/circuit-breaker.js).

## Setting Endpoints

Service endpoints can be set in three ways:
- Set .endpoint = '&lt;YOUR_ENDPOINT&gt;' on the service instance. This lets you specify a full host name (for example, https://www.example.com).
- Set .region = '&lt;YOUR_REGION_ID&gt; on the service instance. This selects the appropriate host name for the service for the given region. However, if the service is not supported in the region you set, the SDK for TypeScript and JavaScript returns an error. You can refer to the list of regionIds in: ./oci-typescript-sdk/common/lib/region.ts
- Pass the region in the configuration file. For more information, see SDK and CLI Configuration File.

Note that a service instance cannot be used to communicate with different regions. If you need to make requests to different regions, create multiple service instances.

### Dedicated Endpoints

Dedicated endpoints are the endpoint templates defined by the service for a specific realm at the client level. The OCI TypeScript and JavaScript SDK allows you to enable the use of this realm-specific endpoint templates feature at both the application level and at the client level. This feature is disabled by default.
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

For full examples, see the[TypeScript](https://github.com/oracle/oci-typescript-sdk/blob/master/examples/typescript/use-realm-specific-endpoint.ts)and[JavaScript](https://github.com/oracle/oci-typescript-sdk/blob/master/examples/javascript/use-realm-specific-endpoint.js)examples on GitHub.

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
For example, see[use-realm-specific-endpoint.ts](https://github.com/oracle/oci-typescript-sdk/blob/master/examples/typescript/use-realm-specific-endpoint.ts)and[use-realm-specific-endpoint.js](https://github.com/oracle/oci-typescript-sdk/blob/master/examples/javascript/use-realm-specific-endpoint.js)

## New Region Support

If you are using a version of the SDK released prior to the announcement of a new region, you can use a workaround to reach it.

A region is a localized geographic area. For more information on regions and how to identify them, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

A realm is a set of regions that share entities. You can identify your realm by looking at the domain name at the end of the network address. For example, the realm for xyz.abc.123.oraclecloud.com is oraclecloud.com.

You must first call Region.register to register the new region, and then you can set the region by either using the configuration file or by set .region = &lt;Your_new_registered_region&gt;.

## oraclecloud.com Realm

For regions in the oraclecloud.com realm, you can pass new region names just as you would pass ones that are already defined in the[Region](https://github.com/oracle/oci-typescript-sdk/tree/master/lib/common/lib/region.ts)enum for your SDK version.

To set the region:

```

```

## Other Realms

For regions in realms other than oraclecloud.com, you can use the following workarounds to reach new regions with earlier versions of the SDK.

To set the endpoint:

```

```

## Paginated Responses

Sometimes it is better to lazy load a result. In order to retrieve more data from lazy load, you have to continue to make calls to the list operation, passing in the value of the most recent response's next token. The pagination module allows you:
- Eagerly load all possible results from a list call
- Lazily load results

For an example on how to use these functions, please check[GitHub](https://github.com/oracle/oci-typescript-sdk/tree/master/examples).

## Exception Handling

When handling an exception, you can get more information about the HTTP request that caused it, such as the status code or timeout. You can also get the request ID when handling an exception by looking at the opcRequestId property of the error object.

```

```

## Logging

The SDK for Typescript and JavaScript enables you to integrate your own logger. Logging in the SDK is done through the[Logger interface](https://github.com/oracle/oci-typescript-sdk/blob/master/lib/common/lib/log.ts). This interface is a logging abstraction that allows the use of a user-supplied logging library, such as log4js, bunyan, or winston.

For more information, see the[logging example on GitHub](https://github.com/oracle/oci-typescript-sdk/blob/master/examples/typescript/logging.ts).
To enable logging:
```

```

```

```
