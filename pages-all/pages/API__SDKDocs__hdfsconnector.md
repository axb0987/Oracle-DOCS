# HDFS Connector for Object Storage
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/hdfsconnector.htm
- Fetched: 2026-09-05 01:36 CDT

# HDFS Connector for Object Storage

The Hadoop Distributed File System (HDFS) connector lets your Apache Hadoop application read and write data to and from the Oracle Cloud Infrastructure Object Storage service.

This SDK and sample is dual-licensed under the Universal Permissive License 1.0 and the Apache License 2.0; third-party content is separately licensed as described in the code.
- Services supported: Object Storage
- Download:[GitHub](https://github.com/oracle/oci-hdfs-connector/releases)or[Maven](https://search.maven.org/search?q=a:oci-hdfs-connector)
- API Documentation:[HDFS Connector API Reference](https://docs.oracle.com/iaas/tools/hdfs/latest/)

## Requirements

To use the HDFS connector, you must have:
- An Oracle Cloud Infrastructure account.
- A user created in that account, in a group with a policy that grants the desired permissions for any bucket you want to use. This can be a user for yourself, or another person/system that needs to call the API. For an example of how to set up a new user, group, compartment, and policy, see[Adding Users](https://docs.oracle.com/iaas/Content/GSG/Tasks/addingusers.htm). For a basic Object Storage policy, see[Let Object Storage admins manage buckets and objects](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#object-storage-admins-manage-buckets-objects).
- Java 8
- A TTL value of 60. For more information, see[Configuring JVM TTL for DNS Name Lookups](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/hdfsconnector.htm#one__java_ttl).

### Credentials and Passwords

If you use an encrypted PEM file for credentials, the passphrase will be read from configuration using the`getPassword`Hadoop Configuration method. The`getPassword`option checks for a password in a registered security provider. If the security provider doesn't contain the requested key, it will fallback to reading the plaintext passphrase directly from the configuration file.

### Configuring JVM TTL for DNS Name Lookups

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

## Installation

Copy the bundled jars from lib and third-party/lib the to each node of the Hadoop cluster so that they are included in Hadoop's CLASSPATH.

### SDK for Java and Maven Artifacts

Building an HDFS connector relies on Maven artifacts that are provided by the Oracle Cloud Infrastructure SDK for Java. To obtain the artifacts, you must[download the SDK for Java](https://github.com/oracle/oci-java-sdk/releases)and build it locally. You can then build the HDFS connector.
Important  
  
The SDK for Java file version that you download from the[Oracle Releases page](https://github.com/oracle/oci-java-sdk/releases)must match the HDFS connector version, which you can find in the`hdfs-connector/pom.xml`file in the dependency tag block that has the`groupId`attribute.

### HDFS Connector and Maven Artifacts

The HDFS connector is available on[Maven Central](https://search.maven.org/search?q=a:oci-hdfs-connector)and[JCenter](https://bintray.com/oracle/jars/oci-hdfs-connector).

To use the HDFS connector in your project, import the following project dependency. For example:
```

```

## Properties

You can set the following HDFS connector properties in the`core-site.xml`file. The[BmcProperties](https://docs.oracle.com/iaas/tools/hdfs/latest/com/oracle/bmc/hdfs/BmcProperties.html)page lists additional properties that you can configure for a connection to Object Storage.

Property Description Type Required
`fs.oci.client.hostname`

The URL of the host endpoint.

For example,`https://www.example.com`. String Yes
`fs.oci.client.auth.tenantId`

The OCID of your tenancy.

To get the value, see[Required Keys and OCIDs](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm). String Yes
`fs.oci.client.auth.userId`

The OCID of the user calling the API.

To get the value, see[Required Keys and OCIDs](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm). String Yes
`fs.oci.client.auth.fingerprint`

The fingerprint for the key pair being used.

To get the value, see[Required Keys and OCIDs](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm). String

Yes, unless you provide a custom authenticator.
`fs.oci.client.auth.pemfilepath`The full path and file name of the private key used for authentication. The file should be on the local file system. String Yes, unless you provide a custom authenticator.
`fs.oci.client.auth.passphrase`The passphrase used for the key, if it is encrypted. String Only if your key is encrypted.
`fs.oci.client.regionCodeOrId`The region code or region identifier used to establish Object Storage endpoint name. String No

Note  
  
You can specify that a property value applies to a specific bucket by appending`. <bucket_name> . <namespace_name>`to the property name.

Setting the Region Endpoint

There are several methods you can use to set the region endpoint for the HDFS Connector :
- Specifying the hostname property in`core-site.xml`
- Specifying the region code or region identifier property in`core-site.xml`
- Allowing the ObjectStorage client to pick up the endpoint via the instance metadata service

Configuring Properties with core-site.xml

This example shows how properties can be configured in a`core-site.xml`file (the OCIDs are shortened for brevity):
```

```

## Using Instance Principals for Authentication

Oracle provides instance principals so that you no longer need to configure user credentials or provide PEM files on services running on instances. Each of these instances has its own identity and authenticates by using certificates added to the instance by instance principals.

To use instance principals authentication with the HDFS connector, simply provide the property`fs.oci.client.custom.authenticator`and set the value to`com.oracle.bmc.hdfs.auth.InstancePrincipalsCustomAuthenticator`.

Because using instance principals provides the connector with a custom authenticator, it is no longer necessary to configure the following properties:
- `fs.oci.client.auth.tenantId`
- `fs.oci.client.auth.userId`
- `fs.oci.client.auth.fingerprint`
- `fs.oci.client.auth.pemfilepath`
- `fs.oci.client.auth.passphrase`

The following example code illustrates using instance principals for authentication with the HDFS connector:

```

```

For more information about instance principals, see[Announcing Instance Principals for Identity and Access Management](https://blogs.oracle.com/cloud-infrastructure/announcing-instance-principals-for-identity-and-access-management).

## Using Resource Principals for Authentication

Similar to instance principals, Oracle provides resource principals to authenticate the resources which are not instances (such as a jupyter notebook). Each resource has its own identity, and authenticates using the certificates that are added to it.

To use resource principals authentication with the HDFS connector, simply provide the property`fs.oci.client.custom.authenticator`and set the value to`com.oracle.bmc.hdfs.auth.ResourcePrincipalsCustomAuthenticator`.

Because using resource principals provides the connector with a custom authenticator, it is no long necessary to configure the following properties:
- `fs.oci.client.auth.tenantId`
- `fs.oci.client.auth.userId`
- `fs.oci.client.auth.fingerprint`
- `fs.oci.client.auth.pemfilepath`
- `fs.oci.client.auth.passphrase`

The following example code illustrates using resource principals for authentication with the HDFS connector:

```

```

For more information about instance principals, see[Using Resource Principals in the Data Science Service](https://blogs.oracle.com/ai-and-datascience/post/feature-highlight-using-resource-principals-in-the-data-science-service).

## Using Kerberos Authentication

Oracle supports Kerberos authentication to connect with Object Storage using the HDFS Connector.
To use Kerberos authentication with the HDFS Connector:
- In`core-site.xml`, set the`fs.oci.client.custom.authenticator`property to`com.oracle.bmc.hdfs.auth.spnego.UPSTAuthenticationCustomAuthenticator`.
- In`core-site.xml`, set the following properties:
- `fs.oci.client.upst.domainUrl`
- 

`fs.oci.client.upst.clientId`
- 

`fs.oci.client.upst.clientSecret`
- 

`fs.oci.client.upst.tokenExchangeServicePrincipal`
- 

`fs.oci.client.upst.userPrincipal`
- `fs.oci.client.upst.issuer`
- `fs.oci.client.keytab.path`
- `fs.oci.client.kinit.internal.mode`

The following example`core-site.xml`file illustrates using Kerberos with SPNEGO token authentication with the HDFS Connector:

```

```

For more information about Kerberos, see the[Kerberos Protocol Tutorial](https://kerberos.org/software/tutorial.html).

For more information about SPNEGO, see[RFC 4178](https://www.rfc-editor.org/rfc/rfc4178).

## Using the Jersey Default HttpUrlConnectorProvider

Starting with version 3.3.0.7.0.0, the HDFS supports using the Apache client by default to make OCI service calls. This is because the HDFS Connector relies on the SDK for Java to send requests to the server. The SDK for Java supports using the Jersey`ApacheConnectorProvider`by default instead of the Jersey`HttpUrlConnectorProvider`to allow the Apache HttpClient to make OCI service calls.

To switch back to the old Jersey default client, set the property`fs.oci.client.jersey.default.connector.enabled`in the`core-site.xml`file to`true`. By default, this value is set to`false`.

### Performance optimization with the Apache Connector for HDFS

The Apache Connector supports of two connection closing strategies:`ApacheConnectionClosingStrategy.GracefulClosingStrategy`and`ApacheConnectionClosingStrategy.ImmediateClosingStrategy`.

When using`ApacheConnectionClosingStrategy.GracefulClosingStrategy`, streams returned from a response are read until the end of the stream when closing the stream. This can introduce additional time when closing the stream with a partial read, depending on how large the remaining stream is. To avoid this delay, consider using`ApacheConnectionClosingStrategy.ImmediateClosingStrategy`for large files with partial reads. With`ApacheConnectionClosingStrategy.ImmediateClosingStrategy`, streams are not read until the end when closing the stream, which can improve performance. Note that`ApacheConnectionClosingStrategy.ImmediateClosingStrategy`takes longer when using partial read for smaller stream size (streams smaller than 1MB).

Setting the connection closing strategy

Set the connection closing strategy by setting`fs.oci.client.apache.connection.closing.strategy`property the in the`core-site.xml`file:

- To use`ApacheConnectionClosingStrategy.GracefulClosingStrategy`, set the`fs.oci.client.apache.connection.closing.strategy`to`graceful`.
- To use`ApacheConnectionClosingStrategy.ImmediateClosingStrategy`, set the`fs.oci.client.apache.connection.closing.strategy`to`immediate`.

Note  
  
These closing strategies only work with the Apache Connector for HDFS and are ignored when using the Jersey default connector.

Switching back to the Jersey default connector

The Jersey default connector reads streams to the end and then reuses the stream, which can lead to better performance than the Apache Connector for HDFS in some scenarios. If these Apache Connection closing strategies do not give you optimal results for your use cases, you can switch back to Jersey Default `HttpUrlConnectorProvider` You can switch back to the old Jersey default client by setting the`fs.oci.client.jersey.default.connector.enabled`property in the`core-site.xml`file to`true`. By default, this value is set to`false`.

For more information, see:[https://github.com/oracle/oci-java-sdk/blob/master/ApacheConnector-README.md](https://github.com/oracle/oci-java-sdk/blob/master/ApacheConnector-README.md).

## Connection Pooling in HDFS

You can set the maximum number of connections in the HDFS Connector connection pool.

To do this, change the property`fs.oci.client.apache.max.connection.pool.size`in the`core-site.xml`file to a positive integer that specifies how many connections to pool.

Note  
  
This property is only supported when using the`ApacheConnector`for HDFS; otherwise it is ignored.

## Dedicated Endpoints

Dedicated endpoints are the endpoint templates defined by a service for a specific realm at the client level. The OCI HDFS Connector allows you to enable the use of these realm-specific endpoint templates by either setting the host name`fs.oci.client.hostname`or the endpoint template flag`fs.oci.realmspecific.endpoint.template.enabled`property in`core-site.xml`.
Note  
  
If you set the endpoint template property, you also need to set`fs.oci.client.regionCodeOrId`in`core-site.xml`.
Note  
  
The value set via the host name in`core-site.xml`takes precedence over the value set using the endpoint template property in`core-site.xml`.
This example shows how to enable the realm-specific endpoint templates feature by setting the`fs.oci.client.hostname`property:
```

```

This example shows how to enabled the realm-specific endpoint templates feature by setting the`fs.oci.realmspecific.endpoint.template.enabled`property:
```

```

## Configuring a HTTP Proxy

You can set the following optional properties in the`core-site.xml`file to configure a HTTP proxy:

Property Description Type Required
`fs.oci.client.proxy.uri`

The URI of the proxy endpoint.

For example,`http://proxy.mydomain.com:80`. String No
`fs.oci.client.proxy.username`The username to authenticate with the proxy. String No
`fs.oci.client.proxy.password`The password to authenticate with the proxy. String No
`fs.oci.client.multipart.allowed`Enables the upload manager to support multipart uploads Boolean No
`fs.oci.client.multipart.minobjectsize.mb`

Specifies the minimum object size in mebibytes in order to use the upload manager. Integer No
`fs.oci.client.multipart.partsize.mb`Specifies the part size in mebibytes for the upload manager. Integer No
Note  
  
Configuring a proxy enables use of the`ApacheConnectorProvider`when making connections to Object Storage. It buffers requests into memory and can impact memory utilization when uploading large objects. It is recommended to enable multipart uploads and adjust the multipart properties to manage memory consumption.

## Large Object Uploads

Large objects are uploaded to Object Storage using multipart uploads. The file is split into smaller parts that are uploaded in parallel, which reduces upload times. This also enables the HDFS connector to retry uploads of failed parts instead of failing the entire upload. However, uploads may transiently fail, and the connector will attempt to abort partially uploaded files. Because these files accumulate (and you will be charged for storage), list the uploads periodically and then after a certain number of days abort them manually using the SDK for Java.

Information about using the Object Storage API for managing multipart uploads can be found in[Using Multipart Uploads](https://docs.oracle.com/iaas/Content/Object/Tasks/usingmultipartuploads.htm).
Note  
  
If you prefer not to use multipart uploads, you can disable them by setting the`fs.oci.client.multipart.allowed`property to`false`.

## Best Practices

The following sections contain best practices to optimize usage and performance.

### Directory Names

There are no actual directories in Object Storage. Directory grouping is a function of naming convention, where objects use`/`delimiters in their names. For example, an object named`a/example.json`implies there is a directory named`a`. However, if that object is deleted, the`a`directory is also deleted implicitly. To preserve filesystem semantics where the directory can exist without the presence of any files, the HDFS connector creates an actual object whose name ends in`/`with a path that represents the directory, (that is, create an object named`a/`). Now, deleting`a/example.json`doesn't affect the existence of the`a`directory, because the`a/`object maintains its presence. However, it's entirely possible that somebody could delete that`a/`object without deleting the files/directories beneath it. The HDFS connector will only delete the folder object if there are no objects beneath that path. The folder object itself is zero bytes.

### Inconsistent Filesystem

Deleting a directory means deleting all objects that start with the prefix representing that directory. HDFS allows you to query for the file status of a file or a directory. The file status of a directory is implemented by verifying that the folder object for that directory exists. However, it's possible that the folder object has been deleted, but some of the objects with that prefix still exist. For example, in a situation with these objects:
- `a/b/example.json`
- `a/b/file.json`
- `a/b/`

HDFS would know that directory`/a/b/`exists and is a directory, and scanning it would result in`example.json`and`file.json`. However, if object`a/b/`was deleted, the filesystem would appear to be in an inconsistent state. You could query it for all files in directory`/a/b/`and find the two entries, but querying for the status of the actual`/a/b/`directory would result in an exception because the directory doesn't exist. The HDFS connector does not attempt to repair the state of the filesystem.

### File Creation

Object Storage supports objects that can be many gigabytes in size. Creating files will normally be done by writing to a temp file and then uploading the contents of the file when the stream is closed. The temp space must be large enough to handle multiple uploads. The temp directory used is controlled by the`hadoop.tmp.dir`configuration property.

### Read/Seek Support

When in-memory buffers are enabled (`fs.oci.io.read.inmemory`), seek is fully supported because the entire file is buffered into a byte array. When in-memory buffer is not enabled (likely because object sizes are large), seek is implemented by closing the stream and making a new range request starting at the specified offset.

### Directory Listing

Listing a directory is essentially a List bucket operation with a prefix and delimiter specified. To create an HDFS FileStatus instance for each key, the connector performs an additional HEAD request to get ObjectMetadata for each individual key. This will be required until Object Storage supports richer list operation data.

## URI Format for Filesystems and Files

HDFS filesystems and files are referenced through URIs. The scheme specifies the type of filesystem, and the remaining part of the URI is largely free for the filesystem implementation to interpret as it wants.

Because Object Storage is an object store, its ability to name objects as if they were files in a filesystem is used to mimic an actual filesystem.

### Root

The root of Object Storage filesystem is denoted by a path where the authority component includes the bucket name and the namespace name, as shown:
Note  
  
In the examples, "`MyBucket`" and "`MyNamespace`" are placeholders and should be replaced with appropriate values.
```

```

This is always the root of the filesystem. The reason for using authority for both bucket and namespace is that HDFS only allows the authority portion to determine where the filesystem is; the path portion denotes just the path to the resource (so "oci//MyNamespace/MyBucket" won't work, for example). Note that the`@`character is not a valid character for buckets or namespaces, and should allow the authority to be parsed correctly.

### Sub-directories

Sub-directories do not actually exist, but can be mimicked by creating objects with`/`characters. For example, two files named`a/b/c/example.json`and`a/b/d/path.json`would appear as if they were in a common directory`a/b`. This would be achieved by using the Object Storage prefix- and delimiter-based querying. In the given example, referencing a sub-directory as a URI would be:
```

```

### Objects/Files

An object named`a/b/c/example.json`is referenced as:
```

```

## Logging

Logging in the connector is done through[SLF4J](https://www.slf4j.org/). SLF4J is a logging abstraction that allows the use of a user-supplied logging library (e.g., log4j). For more information, see, the[SLF4J manual](https://www.slf4j.org/manual.html).

The following example shows how to enable basic logging to standard output.
- Download the SLF4J Simple binding jar:[SLF4J Simple Binding](http://mvnrepository.com/artifact/org.slf4j/slf4j-simple)
- Add the jar to your classpath
- Add the following VM arg to enable debug level logging (by default, info level is used):`-Dorg.slf4j.simpleLogger.defaultLogLevel=debug`

You can configure more advanced logging options by using the log4j binding.

## Using the Monitoring Framework

HDFS Connector for Object Storage includes a monitoring framework that provides metrics on operations performed using the connector. The monitoring framework provides an interface that can be implemented to consume/listen to metrics generated by the connector. You can provide a custom implementation of this interface, or you can use the OCI public telemetry implementation included with this framework.

Getting Started

To start using the HDFS Connector monitoring framework, you will need to set the following properties. Once these properties are set for`OCIMonitoring`, you can use the Metric Explorer view in the OCI Console to observe the metrics emitted from the HDFS connector.

`fs.oci.mon.consumer.plugins`
The`fs.oci.mon.consumer.plugins`takes a comma separated list of fully qualified class names of implementations of the monitoring interface.`com.oracle.bmc.hdfs.monitoring.OCIMonitorPlugin`should be used in the list if you want the metrics to be emitted to OCI public telemetry.
```

```

`fs.oci.mon.grouping.cluster.id`
The`fs.oci.mon.grouping.cluster.id`property specifies the identifier for the HDFS cluster or any other ID that you want to group the metrics into. This is a mandatory property, which is also used by the`OCIMonitorPlugin`to tag metrics. This property is visible as a dimension in the OCI public telemetry user interface and API.
```

```

`com.oracle.bmc.hdfs.monitoring.OCIMonitorPlugin`properties

If the`com.oracle.bmc.hdfs.monitoring.OCIMonitorPlugin`property is enabled , then the following properties are applicable:

`fs.oci.mon.telemetry.ingestion.endpoint`
The`fs.oci.mon.telemetry.ingestion.endpoint`property helps configure the telemetry ingestion endpoint of OCI monitoring. For more information, see the[list of the available points](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/).
```

```

`fs.oci.mon.compartment.ocid`
The`fs.oci.mon.compartment.ocid`property is used to configure the OCI compartment to which the metrics will be attached. This will be usually the compartment to which the buckets belong.
```

```

`fs.oci.mon.bucket.level.enabled`
The`fs.oci.mon.bucket.level.enabled`property determines whether to attach the bucket name as a dimension to the emitted metrics.
```

```

`fs.oci.mon.ns.name`
The`fs.oci.mon.ns.name`property controls the namespace used for the metrics emitted by HDFS connector. An example namespace could be "hdfsconnector". This will reside along side other predefined namespaces like`oci_objectstorage`in the public telemetry.
```

```

`fs.oci.mon.rg.name`
The`fs.oci.mon.rg.name`property sets the resource group name used to contain the metrics. This can be any logical name for grouping resources which will be monitored together. This resource group name will show up under the namespace that was chosen earlier in the OCI public telemetry.
```

```

Creating your own consumer for metrics
To use the`com.oracle.bmc.hdfs.monitoring.OCIMonitorConsumerPlugin`interface, you'll have to define two methods:
- `accept`
- `shutdown`

Extending classes should have a constructor with the same signature as that of the`OCIMonitorConsumerPlugin`class.
For example:
```

```

This example demonstrates each method that needs to be implemented by a consumer plugin:
```

```

The`OCIMetric`class can be implemented in three ways:
A simple`OCIMetric`object with the following fields:
```

```

An implementation of the`OCIMetricWithThroughput`object that extends`OCIMetric`and has additional fields for throughput and bytes transferred. This is applicable to READ and WRITE operations:
```

```

An`OCIMetricWithFBLatency`object that extends`OCIMetricWithThroughput`, with an additional time to first byte latency field. This is applicable only for READ operations:
```

```

## Sample Hadoop Job

[hadoop_sample_hdfs](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../../Resources/Assets/hadoop_sample_hdfs.txt):

```

```

## Troubleshooting

This section contains troubleshooting information for the HDFS connector.

### Troubleshooting Service Errors

Any operation resulting in a service error will cause an exception of type com.oracle.bmc.model.BmcException to be thrown by the HDFS connector. For information about common service errors returned by OCI, see[API Errors](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../References/apierrors.htm).

### Java Encryption Key Size Errors

The HDFS connector can only handle keys of 128 bit or lower key length. Users get "Invalid Key Exception" and "Illegal key size" errors when they use longer keys, such as AES256. Use one of the following workarounds to fix this issue:
- Use a 128 bit key, such as AES128.
- 

Install the Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction from the following location:[http://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html](http://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html)

## Contributions

Got a fix for a bug, or a new feature you'd like to contribute? The SDK is open source and[accepting pull requests](https://github.com/oracle/oci-hdfs-connector/blob/master/CONTRIBUTING.md)on[GitHub](https://github.com/oracle/oci-hdfs-connector).

## Notifications

If you wish to be notified when a new version of the HDFS connector is released, subscribe to the[Atom feed](https://github.com/oracle/oci-hdfs-connector/releases.atom).

## Questions or Feedback

Ways to get in touch:
- [GitHub Issues](https://github.com/oracle/oci-hdfs-connector/issues): To file bugs and make feature requests
- [Stack Overflow](https://stackoverflow.com/): Please use the[oracle-cloud-infrastructure](https://stackoverflow.com/questions/tagged/oracle-cloud-infrastructure)and[oci-hdfs-connector](https://stackoverflow.com/questions/tagged/oci-hdfs-connector)tags in your post
- [Developer Tools section](https://cloudcustomerconnect.oracle.com/resources/9c8fa8f96f/search/posts?find=&daysBack=0&userName=&tagName=Developer+Tools&type=)of the Oracle Cloud forums
- [My Oracle Support](https://support.oracle.com)
