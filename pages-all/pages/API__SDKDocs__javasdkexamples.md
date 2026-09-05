# Examples
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/javasdkexamples.htm
- Fetched: 2026-09-05 01:36 CDT

# Examples

This topic describes how to find and install some OCI SDK for Java code examples.

Examples of SDK usage can be found on[GitHub](https://github.com/oracle/oci-java-sdk/tree/master/bmc-examples), including:
- [Example: Synchronous Object Storage](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/ObjectStorageSyncExample.java)
- [Example: Asynchronous Object Storage](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/ObjectStorageAsyncExample.java)
- [Example: Create an instance](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/CreateInstanceExample.java)
- [Example: Get an instance's public IP address](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/GetInstancePublicIpExample.java)

The examples are also in the downloadable .zip file for the SDK. Examples for older versions of the SDK are in the downloadable .zip for the specific version, available[on GitHub](https://github.com/oracle/oci-java-sdk/releases).

If you'd like to see another example not already covered, file a[GitHub issue](https://github.com/oracle/oci-java-sdk/issues).

## Examples Using Jersey 2 as the HTTP Client Library (OCI SDK for Java 3)

In order to use Jersey 2 as the HTTP client library, a dependency on`oci-java-sdk-common-httpclient-jersey`needs to be explicitly declared in the application's`pom.xml`. Refer to[bmc-jersey-examples/pom.xml](https://github.com/oracle/oci-java-sdk/blob/master/bmc-other-examples/bmc-jersey-examples/pom.xml).

Examples using Jersey 2 as the HTTP client library can be found in[bmc-other-examples/bmc-jersey-examples](https://github.com/oracle/oci-java-sdk/blob/master/bmc-other-examples/bmc-jersey-examples).

## Examples Using Jersey 3 as the HTTP Client Library (OCI SDK for Java 3)

In order to use Jersey 3 as the HTTP client library, a dependency on`oci-java-sdk-common-httpclient-jersey3`needs to be explicitly declared in application's`pom.xml`. Refer to[bmc-jersey3-examples/pom.xml](https://github.com/oracle/oci-java-sdk/blob/master/bmc-other-examples/bmc-jersey3-examples/pom.xml).

Examples using Jersey 3 as the HTTP client library can be found in[bmc-other-examples/bmc-jersey3-examples](https://github.com/oracle/oci-java-sdk/blob/master/bmc-other-examples/bmc-jersey3-examples).

## Examples for the Legacy OCI SDK for Java (OCI SDK for Java 1 and 2)

Examples for the legacy OCI SDK for Java can be found[here](https://github.com/oracle/oci-java-sdk/tree/legacy/v2/master#examples).

## SDK Reference

In addition to the examples found on GitHub, the[SDK for Java API reference](https://docs.oracle.com/iaas/tools/java/latest/)contains code examples that you can copy and modify to run in your own environment.

## Running Examples

- Download the SDK to a directory named`oci`. See[GitHub](https://github.com/oracle/oci-java-sdk/releases)for the download.
- Unzip the SDK into the`oci`directory. For example:`tar -xf oci-java-sdk-dist.zip`
- Create your configuration file in your home directory (`~/.oci/config`). See[Configuring the SDK](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/javasdkgettingstarted.htm#Configur).
- 

Use`javac`to compile one of the previous example classes from the`examples`directory, ex:

```

```

- 

You should now have a class file in the`examples`directory. Run the example:

```

```

### Third-Party Dependencies and Shading

The SDK requires a number of third-party dependencies, which are available in the`third-party/lib`directory. To use the SDK library`lib/oci-java-sdk-full- <version> .jar`, all of the third-party dependencies in`third-party/lib`have to be on the class path.

The SDK also includes a second version of the SDK library,`shaded/lib/oci-java-sdk-full-shaded- <version> .jar`, which contains most of the third-party dependencies already. Only a few more third-party libraries in`shaded/third-party/lib`have to be on the class path when you use this version of the SDK library.

These two versions of the SDK library are functionally the same, however the second version,`shaded/lib/oci-java-sdk-full-shaded- <version> .jar`can simplify dealing with different versions of third-party dependencies. This is because all the dependencies that are included in`shaded/lib/oci-java-sdk-full-shaded- <version> .jar`were shaded, which means they will not interfere with other versions of themselves you may want to include along with this SDK.

You can use either`lib/oci-java-sdk-full-<version>.jar`or`shaded/lib/oci-java-sdk-full-shaded- <version> .jar`, but not both. When using`lib/oci-java-sdk-full-<version>.jar`, use all the third-party libraries in`third-party/lib`. When using`shaded/lib/oci-java-sdk-full-shaded- <version> .jar`, use all the third-party libraries in`shaded/third-party/lib`.

To use the shaded version of the SDK, replace the`javac`commands in steps 4 and 5 with the following:
- 

Step 4:
```

```

- 

Step 5:
```

```
