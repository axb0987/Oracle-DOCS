# Configuration
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/javasdkconfig.htm
- Fetched: 2026-09-05 01:36 CDT

# Configuration

This topic provides details on compatibility, advanced configurations, and add-ons for the Oracle Cloud Infrastructure SDK for Java.

This topic provides details on compatibility, advanced configurations, and add-ons for the Oracle Cloud Infrastructure SDK for Java.

## Security Manager Permissions

If your application needs to run inside the[Java Security Manager](https://docs.oracle.com/javase/tutorial/essential/environment/security.html), you must grant additional permissions by updating a policy file, or by specifying an additional or a different policy file at runtime.

The SDK requires the following permissions:
- 

Required by Jersey:

```

```

- 

Required by the SDK to overwrite reserved headers:

```

```

- 

Required by the SDK to open socket connections:

```

```

To include another policy file, in addition to Java Runtime Environment's default policy file, launch the Java Virtual Machine with:

```

```

To replace the default policy file, launch the Java Virtual Machine with:

```

```

Note  
  
Use a single equals sign (=) when supplying an additional policy file. Use a double equals sign (==) only if you wish to replace the default policy file.

## Java Virtual Machine TTL for DNS Name Lookups

The Java Virtual Machine (JVM) caches DNS responses from lookups for a set amount of time, called time-to-live (TTL). This ensures faster response time in code that requires frequent name resolution.

The JVM uses the[networkaddress.cache.ttl](http://docs.oracle.com/javase/8/docs/technotes/guides/net/properties.html)property to specify the caching policy for DNS name lookups. The value is an integer that represents the number of seconds to cache the successful lookup. The default value for many JVMs,`-1`, indicates that the lookup should be cached forever.

Because resources in Oracle Cloud Infrastructure use DNS names that can change, we recommend that you change the TTL value to 60 seconds. This ensures that the new IP address for the resource is returned on next DNS query. You can change this value globally or specifically for your application:
- 

To set TTL globally for all applications using the JVM, add the following in the`$JAVA_HOME/jre/lib/security/java.security`file:
```

```

- 

To set TTL only for your application, set the following in your application's initialization code:
```

```

## Using the Jersey Default HttpUrlConnectorProvider

Starting with version 2.0.0, the SDK for Java supports using the Jersey`ApacheConnectorProvider`instead of the Jersey default`HttpUrlConnectorProvider`to allow the Apache HttpClient to make OCI service calls.

### To change to the Jersey default connector at the client level

At the client level, the SDK provides the following way to switch back to the old Jersey default connector:

```

```

Note  
  
Overriding the`clientConfigurator`property of the client will revert back to the Jersey defaults. For configuring`clientConfigurator`with the use of Apache Connector, use`additionalClientConfigurator`or`additionalClientConfigurators`.

### To change to the Jersey default connector at the global levelYou can exclude the Apache HttpClient dependencies or use an environment variable. Excluding HttpClient Dependencies

If you are managing dependencies yourself:
- Remove the`org.apache.httpcomponents.httpclient`and`org.glassfish.jersey.connectors.jersey-apache-connector`JARs from the classpath

If you are using Maven to manage your dependencies:

- Add exclusions for the`org.apache.httpcomponents.httpclient`and`org.glassfish.jersey.connectors.jersey-apache-connector`dependencies.
- 

To add an exclusion if you use Jersey 2:

```

```

- 

To add an exclusion if you use Jersey 3:

```

```
Switching back using an environment variable

The SDK for Java provides an environment variable to switch back to the old Jersey default connector at the global level. Set the value of the`OCI_JAVASDK_JERSEY_CLIENT_DEFAULT_CONNECTOR_ENABLED`environment variable to`true`. By default, this value is set to`false`.

### Switching off auto-close of streams

For API calls that return binary/stream response, the SDK will auto-close the stream once the stream has been completely read. This is because the SDK for Java supports the Apache Connector for sending requests and managing connections to the service. By default, the Apache Connector supports connection pooling. In the cases where the stream from the response is not closed, the connections don't get released from the connection pool.

To disable the auto-close behavior, call`ResponseHelper.shouldAutoCloseResponseInputStream(false)`.

### Choosing connection closing strategies with the Apache Connector to optimize performance

The Apache Connector supports of two connection closing strategies:`ApacheConnectionClosingStrategy.GracefulClosingStrategy`and`ApacheConnectionClosingStrategy.ImmediateClosingStrategy`.

When using`ApacheConnectionClosingStrategy.GracefulClosingStrategy`, streams returned from a response are read until the end of the stream when closing the stream. This can introduce additional time when closing the stream with a partial read, depending on how large the remaining stream is. To avoid this delay, consider using`ApacheConnectionClosingStrategy.ImmediateClosingStrategy`for large files with partial reads. Note that`ApacheConnectionClosingStrategy.ImmediateClosingStrategy`takes longer when using partial read for smaller stream size (streams smaller than 1MB).
Note  
  
If these Apache Connection closing strategies do not give you optimal results for your use cases, you can switch back to Jersey Default`HttpUrlConnectorProvider`using the method stated above.

For more information, see:[https://github.com/oracle/oci-java-sdk/blob/master/ApacheConnector-README.md](https://github.com/oracle/oci-java-sdk/blob/master/ApacheConnector-README.md).

## Using BC-FIPS Instead of Bouncy Castle

If you need FIPS compliance, you must download and use a FIPS-certified version. The SDK supports bc-fips 1.0.2 and bcpkix-fips 1.0.3. You can download them at:[https://www.bouncycastle.org/fips-java/](https://www.bouncycastle.org/fips-java/)

For help installing and configuring Bouncy Castle FIPS, see "BC FIPS Documentation" in the User Guides and Security Policy of the[Bouncy Castle Documentation](https://www.bouncycastle.org/documentation.html).

Self-Managed Dependencies

If you are managing dependencies yourself:
- Remove the non-FIPS Bouncy Castle jar files from the class path:
- `bcprov-jdk15on-1.60.jar`
- `bcpkix-jdk15on-1.60.jar`
- Add the FIPS Bouncy Castle jar files to the class path instead:
- `bc-fips-1.0.2.jar`
- `bcpkix-fips-1.0.3.jar`

Maven-Managed Dependencies

If you are using Maven to manage your dependencies:

- Add the correct versions of`bc-fips`and`bcpkix-fips`to your dependencies:
```

```

- Since you are depending on an`oci-java-sdk*`package, you need to remove the non-FIPS Bouncy Castle dependencies:
```

```

## Using Your Own JAX-RS Implementation

The SDK for Java is bundled with Jersey, but you can also use your own JAX-RS implementation.

### RESTEasy Client Configurator Add-On

The`oci-java-sdk-addons-resteasy-client-configurator`is provided to demonstrate how to configure an alternate JAX-RS implementation. The add-on can be found in the`bmc-addons`directory of the SDK.

For details on installation and configuration, see the[Readme](https://github.com/oracle/oci-java-sdk/blob/master/bmc-addons/bmc-resteasy-client-configurator/README.md)for the add-on.

For code samples that demonstrate how to configure the client, see:
- [ResteasyClientExample.java](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/ResteasyClientExample.java)
- [ResteasyClientWithObjectStorageExample.java](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/ResteasyClientWithObjectStorageExample.java)
- [InstancePrincipalsAuthenticationDetailsProviderWithResteasyClientExample.java](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/InstancePrincipalsAuthenticationDetailsProviderWithResteasyClientExample.java)

## Using SLF4J for Logging

Logging in the SDK is done through[SLF4J](https://www.slf4j.org/). SLF4J is a logging abstraction that allows the use of a user-supplied logging library (e.g., log4j). For more information, see the[SLF4J manual](https://www.slf4j.org/manual.html).

The following is an example that enables basic logging to standard out. More advanced logging options can be configured by using the log4j binding.
- Download the SLF4J Simple binding jar:[SLF4J Simple Binding](https://mvnrepository.com/artifact/org.slf4j/slf4j-simple)
- Add the jar to your classpath (e.g., add it to the`/third-party/lib`directory of the SDK download)
- Add the following VM arg to enable debug level logging (by default, info level is used):`-Dorg.slf4j.simpleLogger.defaultLogLevel=debug`
