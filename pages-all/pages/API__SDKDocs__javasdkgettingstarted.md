# Getting Started
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/javasdkgettingstarted.htm
- Fetched: 2026-09-05 01:36 CDT

# Getting Started

This topic describes how to install and configure the Oracle Cloud Infrastructure SDK for Java.

This topic describes how to install and configure the Oracle Cloud Infrastructure SDK for Java.
Tip  
  
The SDK for Java is pre-configured with your credentials and ready to use immediately from within[Cloud Shell](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/cloudshellintro.htm). For more information on using the SDK for Java from within Cloud Shell, see[SDK for Java Cloud Shell Quick Start](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/cloudshellquickstart_java.htm).

## Installing with Resource Manager

You can use[Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/home.htm)to[install the Oracle Cloud Development Kit on a Compute instance in your compartment](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/devtools.htm). The Oracle Cloud Development Kit includes the SDK for Java, along with other Oracle development tools.

## Downloading the SDK from GitHub

You can download the SDK for Java as a zip archive from[GitHub](https://github.com/oracle/oci-java-sdk/releases). It contains the SDK, all of its dependencies, documentation, and examples. For best compatibility and to avoid issues, use the version of the dependencies included in the archive. Some notable issues are:
- Bouncy Castle: The SDK bundles 1.60 (included in this distribution). If you need FIPS compliance, see[Using BC-FIPS Instead of Bouncy Castle](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/javasdkconfig.htm#javasdkconfig_topic_Using_BC_FIPS_Instead_of_bouncy_castle).
- Jersey Core and Client: The SDK bundles 2.24.1, which is required to support large object uploads to Object Storage. Older versions will not support uploads greater than ~2.1 GB.
- Jax-RS API: The SDK bundles 2.0.1 of the spec. Older versions will cause issues.
Note  
  
The SDK for Java is bundled with Jersey (included in this distribution), but you can also use your own JAX-RS implementation. For details, see[Using Your Own JAX-RS Implementation](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/javasdkconfig.htm#Using)

## Downloading the SDK from Maven or JCenter

[Maven Central](https://search.maven.org/search?q=g:com.oracle.oci.sdk)and

[JCenter](https://bintray.com/oracle/jars/oci-java-sdk).

## Installing with yum

If you're using Oracle Linux 7 or 8, you can use yum to install the OCI SDK for Java.

For Oracle Linux 7:

```

```

For Oracle Linux 8:
```

```

The OCI jar file will be located in:`/usr/lib64/java-oci-sdk/lib/oci-java-sdk-full-<version>.jar`, and third-party libraries will be in`/usr/lib64/java-oci-sdk/third-party/lib`. You can add the following entries to your classpath:`/usr/lib64/java-oci-sdk/lib/oci-java-sdk-full-<version>.jar:/usr/lib64/java-oci-sdk/third-party/lib/*`For example:

```

```

## Configuring the SDK

The SDK services need two types of configuration: credentials and client-side HTTP settings.

### Configuring Credentials

First, you need to set up your credentials and config file. For instructions, see[SDK and CLI Configuration File](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/sdkconfig.htm).

Next you need to set up the client to use the credentials. The credentials are abstracted through an`AuthenticationDetailsProvider`interface. Clients can implement this however you choose. We have included a simple POJO/builder class to help with this task (`SimpleAuthenticationDetailsProvider`).
- 

You can load a config with or without a profile:

```

```

- 

The private key supplier can be created with the file path directly, or using the config file:

```

```

- 

To create an auth provider using the builder:

```

```

- 

To create an auth provider using the builder with a config file:

```

```

- 

Finally, if you use standard config file keys and the standard config file location, you can simplify this further by using`ConfigFileAuthenticationDetailsProvider`:

```

```

### Configuring Client-side Options

Create a client-side configuration through the`ClientConfiguration`class. If you do not provide your own configuration, the SDK for Java uses a default configuration. To provide your own configuration, use the following:

```

```

After you have both a credential configuration and the optional client configuration, you can start creating service instances.

For a code sample that demonstrates how to set up and use connection and read timouts in your client configuration, see the[Client Configuration Timeout example on GitHub](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/ClientConfigurationTimeoutExample.java).

### Configuring Custom Options

In the config file, you can insert custom key-value pairs that you define, and then reference them as necessary. For example, you can specify a frequently used compartment ID in the config file:

```

```

Then you can retrieve the value:

```

```

## Using the SDK for Java

There are two ways to use the Oracle Cloud Infrastructure SDK for Java in your project.
- 

Import the`oci-java-sdk-bom`, followed by the HTTP client library and your project dependencies.

The HTTP client library is configurable, and no library is chosen by default. The OCI SDK for Java currently offers the following HTTP client libraries to choose from:
- Jakarta EE 8/Jersey 2 -[`oci-common-httpclient-jersey`](https://github.com/oracle/oci-java-sdk/tree/master/bmc-common-httpclient-choices/bmc-common-httpclient-jersey)
- Jakarta EE 9/Jersey 3 -[`oci-common-httpclient-jersey3`](https://github.com/oracle/oci-java-sdk/tree/master/bmc-common-httpclient-choices/bmc-common-httpclient-jersey3)

You must explicitly choose the library by declaring a dependency on`oci-java-sdk-common-httpclient-jersey`or`oci-java-sdk-common-httpclient-jersey3`. For example:

```

```

- 

Add the`oci-java-sdk-shaded-full`shaded dependency to your pom file. You can use the shaded dependency to include all the third-party classes and its transitive dependencies by renaming and including them in your project. It contains an Uber JAR, which is basically a combination of multiple JARs. All the packages inside the Uber JAR are renamed. This will prevent conflicts between the Oracle Cloud Infrastructure SDK dependencies and third-party dependencies that you might be using in your project.

For example, the classes in`org.apache.commons`are relocated to`shaded.com.oracle.oci.javasdk.org.apache.commons`.

The contents of the Uber JAR are as follows:
```

```

If you're using Maven to manage your dependencies, you can find the latest shaded dependency in the[Maven repository](https://mvnrepository.com/artifact/com.oracle.oci.sdk/oci-java-sdk-shaded-full).

Add the latest version of`oci-java-sdk-shaded-full`to your dependencies:
```

```
