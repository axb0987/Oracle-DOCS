# Updates in Version 3 of the OCI SDK for Java
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/javasdk3.htm
- Fetched: 2026-09-05 01:36 CDT

# Updates in Version 3 of the OCI SDK for Java

This topic explains some of the key changes introduced in version 3 of the Oracle Cloud Infrastructure SDK for Java.

This topic explains some of the key changes introduced in version 3 of the Oracle Cloud Infrastructure SDK for Java.
Note  
  
See the[release notes](https://github.com/oracle/oci-java-sdk/releases/tag/v3.0.0)for full details and refer to the[Examples](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/javasdkexamples.htm)topic for more information.

## HTTP Client Libraries

No HTTP client library is configured by default. You must explicitly choose an HTTP client library. The OCI SDK for Java offers the following choices for HTTP client libraries:
- Jakarta EE 8/Jersey 2 -[`bmc-common-httpclient-jersey`](https://github.com/oracle/oci-java-sdk/tree/master/bmc-common-httpclient-choices/bmc-common-httpclient-jersey)
- Jakarta EE 9/Jersey 3 -[`bmc-common-httpclient-jersey3`](https://github.com/oracle/oci-java-sdk/tree/master/bmc-common-httpclient-choices/bmc-common-httpclient-jersey3)

Specify the HTTP client library by declaring a dependency on`oci-java-sdk-common-httpclient-jersey`or`oci-java-sdk-common-httpclient-jersey3`. For example:
```

```

## Invocation Callbacks

Instead of using`com.oracle.bmc.util.internal.Consumer<Invocation.Builder>`to register invocation callbacks, use`com.oracle.bmc.http.client.RequestInterceptor`instead. This decouples the implementation from the choice of the HTTP client.

## Simplified Client Configuration

The`customizeClient(HttpClientBuilder builder)`method for`com.oracle.bmc.http.ClientConfigurator`replaced the`customizeBuilder`,`customizeClient`, and`customizeRequest`methods. For example:

```

```

The properties that can be set depend on the HTTP client you're using. You can also define your own properties. For a comprehensive list of predefined settable properties, refer to the following:
- [StandardClientProperties.java](https://github.com/oracle/oci-java-sdk/blob/v3.0.0/bmc-common-httpclient/src/main/java/com/oracle/bmc/http/client/StandardClientProperties.java)
- [ApacheClientProperties.java](https://github.com/oracle/oci-java-sdk/blob/d4b2f51c9c69bf64deb124ca921deeac333c3d03/bmc-common-httpclient-choices/bmc-common-httpclient-jersey/src/main/java/com/oracle/bmc/http/client/jersey/ApacheClientProperties.java)
- [ApacheClientProperties.java](https://github.com/oracle/oci-java-sdk/blob/d4b2f51c9c69bf64deb124ca921deeac333c3d03/bmc-common-httpclient-choices/bmc-common-httpclient-jersey3/src/main/java/com/oracle/bmc/http/client/jersey3/ApacheClientProperties.java)(Jersey 3)

Client Configuration Examples
Configuration Example
Setting whether to buffer a request
```

```

Setting an Apache connection manager
```

```

Setting a trust store
```

```

Setting a key store
```

```

Setting the SSL context
```

```

Setting a proxy
```

```

Setting a hostname verifier
```

```

The following client configuration examples are also available:
- [ApacheConnectorPropertiesExample.java](https://github.com/oracle/oci-java-sdk/blob/v3.0.0/bmc-examples/src/main/java/ApacheConnectorPropertiesExample.java)
- [HttpProxyExample.java](https://github.com/oracle/oci-java-sdk/blob/v3.0.0/bmc-examples/src/main/java/HttpProxyExample.java)
- [DisableNoConnectionReuseStrategyUsingApacheConfiguratorExample.java](https://github.com/oracle/oci-java-sdk/blob/v3.0.0/bmc-other-examples/bmc-jersey-examples/src/main/java/DisableNoConnectionReuseStrategyUsingApacheConfiguratorExample.java)and[DisableNoConnectionReuseStrategyUsingApacheConfiguratorExample.java](https://github.com/oracle/oci-java-sdk/blob/v3.0.0/bmc-other-examples/bmc-jersey3-examples/src/main/java/DisableNoConnectionReuseStrategyUsingApacheConfiguratorExample.java)(Jersey 3)

## Apache Connector Changes

Several changes were made in order to decouple the Apache Connector implementation from the choice of the HTTP client.

`com.oracle.bmc.http.ApacheConfigurator`was replaced by`com.oracle.bmc.http.client.jersey.ApacheClientProperties`or`com.oracle.bmc.http.client.jersey3.ApacheClientProperties`(for Jersey 3).

The following example is for clients that shouldn't buffer requests into memory:

```

```

For clients that should buffer requests into memory, refer to the following example:

```

```

See[DisableNoConnectionReuseStrategyUsingApacheConfiguratorExample.java](https://github.com/oracle/oci-java-sdk/blob/v3.0.0/bmc-other-examples/bmc-jersey-examples/src/main/java/DisableNoConnectionReuseStrategyUsingApacheConfiguratorExample.java)and[DisableNoConnectionReuseStrategyUsingApacheConfiguratorExample.java](https://github.com/oracle/oci-java-sdk/blob/v3.0.0/bmc-other-examples/bmc-jersey3-examples/src/main/java/DisableNoConnectionReuseStrategyUsingApacheConfiguratorExample.java)(Jersey 3) for more information.

Also consider using`com.oracle.bmc.http.client.jersey.apacheconfigurator.ApacheConfigurator`from the`oci-java-sdk-addons-apache-configurator-jersey`add-on module, or`com.oracle.bmc.http.client.jersey3.apacheconfigurator.ApacheConfigurator`from the`oci-java-sdk-addons-apache-configurator-jersey3`add-on module. See[DisableNoConnectionReuseStrategyUsingApacheConfiguratorExample.java](https://github.com/oracle/oci-java-sdk/blob/v3.0.0/bmc-other-examples/bmc-jersey-examples/src/main/java/DisableNoConnectionReuseStrategyUsingApacheConfiguratorExample.java)and[DisableNoConnectionReuseStrategyUsingApacheConfiguratorExample.java](https://github.com/oracle/oci-java-sdk/blob/v3.0.0/bmc-other-examples/bmc-jersey3-examples/src/main/java/DisableNoConnectionReuseStrategyUsingApacheConfiguratorExample.java)(Jersey 3) for more information.

## Circuit Breaker Changes

The[circuit breaker](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/javasdkconcepts.htm#javasdkconcepts_topic_Retries_Circuit_Breakers)interface was renamed from`com.oracle.bmc.circuitbreaker.JaxRsCircuitBreaker`to`com.oracle.bmc.circuitbreaker.OciCircuitBreaker`.

Instead of using the constructor of`com.oracle.bmc.circuitbreaker.CircuitBreakerConfiguration`, use the builder. The constructor isn't public anymore.

The`com.oracle.bmc.util.CircuitBreakerUtils`class doesn't deal with circuit breakers anymore, just with`com.oracle.bmc.circuitbreaker.CircuitBreakerConfiguration`. Therefore, the`DEFAULT_CIRCUIT_BREAKER`field and the`getUserDefinedCircuitBreaker`method were removed. Construct a new circuit breaker from the default configuration if necessary using the build methods in`com.oracle.bmc.circuitbreaker.CircuitBreakerFactory`
