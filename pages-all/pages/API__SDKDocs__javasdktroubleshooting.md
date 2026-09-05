# Troubleshooting
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/javasdktroubleshooting.htm
- Fetched: 2026-09-05 01:36 CDT

# Troubleshooting

This section contains troubleshooting information for the Oracle Cloud Infrastructure SDK for Java.

This section contains troubleshooting information for the Oracle Cloud Infrastructure SDK for Java.

## Program hangs for an indefinite time

If a request to the server hangs for an indefinite time, it could be because the connection was not released from the connection pool. The SDK for Java now supports the Apache Connector for sending requests and managing connections to the service. The Apache Connector supports connection pooling. If a stream is not closed, the connections do not get released from the connection pool, which can result in an indefinite wait time.
The SDK automatically closes the stream to release the connection from the connection pool, but only when the stream is read completely.
To avoid program hangs, be sure to close all streams returned from the response to release the connections from the connection pool to avoid indefinite wait times. For example:
```

```

You can also switch back to the Jersey default connector`HttpUrlConnector`. For more information, see[Using the Jersey Default HttpUrlConnectorProvider](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/javasdkconfig.htm#apache).

## Server drops Apache Client Library connection with no response

In some cases, usually under heavy load, the server receives but does not process a request. This may cause the server to drop the connection to the client without giving any response. The Apache HttpClient throws a`NoHttpResponseException`when it encounters such a condition. In such cases, the underlying Apache HttpClient will retry requests to the server and emit INFO level logs about retries to the server. If the retries fail and the request fails to complete, you should switch back to the Jersey default connector`HttpUrlConnector`. For more information, see[Using the Jersey Default HttpUrlConnectorProvider](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/javasdkconfig.htm#apache).

## ObjectStorage client does not close connections when client is closed.

Too many file descriptors are opened up, and it takes too long to close existing ones. An exception may look like this:
```

```

Use one of the following workarounds to fix this issue.
- Make this call before creating a client:`System.setProperty("http.keepAlive", "false");`
- Use this command line argument when running Java:`-Dhttp.keepAlive=false`

## Serialization errors when making requests or handling responses

An`UnrecognizedPropertyException`error when handling a response indicates that the version of the Jackson library does not support a feature that was injected at runtime from another dependency in your application's class path. This happens even if the`FAIL_ON_UNKNOWN_PROPERTIES`deserialization property is set to`false`for the configured`ObjectMapper`.

### Solution:

Determine which version of Jackson libraries are referenced in your application's class path and, if necessary, upgrade to version 2.9.5. For a complete list of Jackson libraries that the SDK for Java depends on, please refer to the[pom.xml file](https://github.com/oracle/oci-java-sdk/blob/master/pom.xml#L443-L477)that is hosted on[GitHub](https://github.com/oracle/oci-java-sdk).
Note  
  
If you customize a client when instantiated in your application, ensure that you reference the preconfigured`ObjectMapper`from the`RestClientFactory`using the`RestClientFactory#getObjectMapper()`method.

An alternative solution is to to use the shaded version of the SDK for Java jar file, which includes a bundled version of the Jackson libraries.

## Encryption key size errors

By default, the SDK for Java can only handle keys of 128 bit or lower key length. Users get "Invalid Key Exception" and "Illegal key size" errors when they use longer keys, such as AES256.

Use one of the following workarounds to fix this issue.
- 

Use a 128 bit key, such as AES128.
- 

Install the Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction from the following location:[http://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html](http://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html)

## Troubleshooting Service Errors

Any operation resulting in a service error will cause an exception of type com.oracle.bmc.model.BmcException to be thrown by the SDK. For information about common service errors returned by OCI, see[API Errors](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../References/apierrors.htm)
