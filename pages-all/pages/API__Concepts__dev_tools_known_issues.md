# Known Issues for Developer Tools
- Source: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/dev_tools_known_issues.htm
- Fetched: 2026-09-05 01:35 CDT

# Known Issues for Developer Tools

This section lists the known issues that have been identified for Developer Tools and SDKs.

## OCI Java SDK token refresh might remain stuck after a refresh failure

Important  
  
OCI Java SDK 3.x is not affected by this specific incomplete-refresh-state defect. Details

In affected OCI Java SDK releases, a failure while refreshing a session key or X509 certificate can leave the security-token refresh operation incomplete. Later requests using the same authentication provider might wait and time out instead of starting another refresh.

`X509FederationClient`coordinates concurrent token-refresh requests so that one request performs the refresh while other requests wait for its result.

In the affected versions, some session-key and certificate-refresh failures could occur before the shared refresh operation was completed and cleared. The SDK could therefore continue to report that token refresh was running even after the request performing it had exited.

Later requests could fail with:
```

```

This condition could affect multiple OCI service clients if they shared the same authentication provider. Recreating the authentication provider or restarting the application could provide temporary recovery.

The SDK does not cause the original certificate or metadata-service failure. The defect prevented the SDK from recovering correctly after such a failure.

Affected versions:`2.91.0`,`2.93.0`, and`2.95.0`Solution

Upgrade to version`2.97.0`or later. The issue is fixed in version`2.97.0`.

## OCI Java SDK version 2.81.0 is incompatible with Java 8
Details

Version[2.81.0](https://github.com/oracle/oci-java-sdk/releases/tag/v2.81.0)of the OCI Java SDK is incompatible with Java 8. If you're using version 2.81.0 with Java 8, you might get the following error message at runtime:
```

```

For more information, see the issue on[GitHub](https://github.com/oracle/oci-java-sdk/issues/665). Workaround

This issue has been fixed in version[2.82.0](https://github.com/oracle/oci-java-sdk/releases/tag/v2.82.0), which restores compatibility with Java 8. All versions before 2.81.0 are also compatible with Java 8.

If you're using Java 8, don't use version 2.81.0, use version 2.82.0 or newer instead.

## Increased memory consumption when uploading streams in OCI Java SDK version 2.66.0
Details

If you are using OCI Java SDK version[2.66.0](https://github.com/oracle/oci-java-sdk/releases/tag/v2.66.0), then you could see increased memory consumption when uploading streams due to unnecessary buffering of the entire stream in memory. Workaround

This issue has been fixed in version[2.72.0](https://github.com/oracle/oci-java-sdk/releases/tag/v2.72.0)and later. If you are using the impacted version, upgrade to version 2.72.0 or later. For more information and other possible workarounds,[see the issue on GitHub](https://github.com/oracle/oci-java-sdk/issues/601).

## Thread leak in IdleConnectionMonitor in OCI Java SDK versions 3.31.0 to 3.38.0
Details If you are using any OCI Java SDK version(s) from 3.31.0 to 3.38.0 then you could see a thread leak in`IdleConnectionMonitor`. An increase in CPU or memory usage might occur due to the proliferation of threads of type`idle-connection-monitor-thread`. Workaround

This issue has been fixed in version 3.39.0 and later. If you are using any of the impacted earlier versions, we recommend upgrading to version 3.39.1 or later. For more information and other possible workarounds,[see the issue on GitHub](https://github.com/oracle/oci-java-sdk/issues/587).

## Retries for operations that upload binary data without request-level retries fail in OCI Java SDK versions 3.0.0 to 3.31.0
Details If you are using any of the OCI Java SDK synchronous clients that upload streams of data (such as`ObjectStorageClient`or`DataSafeClient`) and you do not define the`RetryConfiguration`at[request level](https://github.com/oracle/oci-java-sdk/blob/v3.30.0/bmc-examples/src/main/java/RetryExample.java#L67-L71), your requests will not be automatically retried in versions 3.0.0 to 3.31.0. There is no chance of silent data corruption. Workaround

This problem is fixed in version 3.31.1 and later. If you are using any of the impacted earlier versions, we recommend that you upgrade to version 3.31.1 or later. For more information and other possible workarounds,[see the issue on GitHub](https://github.com/oracle/oci-java-sdk/issues/566).

## Errors while using the Java SDK after updating to JDK versions 8u381, 11.0.20, 17.0.8, or 21.0.0
Details
The following error message might be encountered after updating to JDK versions 8u381, 11.0.20, 17.0.8, or 21.0.0 :
```

```

This issue occurs because the listed Java versions have a default maximum signature file size smaller than some Java SDK JARs. The low default value in Java will be addressed and resolved in upcoming minor Java version releases. Workaround #1
To resolve this problem, you can run Maven with the following parameter:
```

```

If you're compiling with`javac`, you can use the following command:
```

```

## Java SDK race condition in CircuitBreaker leading to NoSuchElementException in OCI Java SDK
Details If you are using an OCI Java SDK from version 2.47.0 to versions prior to 2.51.2, you may encounter a bug in the CircuitBreaker that raises a NoSuchElementException. For more information, see[https://github.com/oracle/oci-java-sdk/issues/491](https://github.com/oracle/oci-java-sdk/issues/491)Workaround #1

This issue was resolved in OCI Java SDK 2.51.2. Update to OCI Java SDK version[version 2.51.2](https://github.com/oracle/oci-java-sdk/releases/tag/v2.51.2)or[newer](https://github.com/oracle/oci-java-sdk/releases). Workaround #2

If you cannot update to version 2.51.2 or newer, you can[disable and opt out of the Java SDK default support for circuit breakers](https://docs.oracle.com/iaas/Content/API/SDKDocs/javasdkconcepts.htm#javasdkconcepts_topic_Retries_Circuit_Breakers)for service clients that have enabled default SDK circuit breakers.

## Python SDK potential memory leak issue when repeatedly creating new signers/clients
Details When repeatedly creating new signers/client objects with Instance Principals, Resource Principal, and Delegation token authentication, some underlying objects are not cleared from memory, causing a memory leak. From our tests, the rate of memory growth is ~10 MiB/hour when only client/signer objects are created in an infinite loop. Cloud Shell is affected by the same issue when new client objects are created repeatedly using the Python SDK. This seems to be coming from an underlying memory leak in the requests package. For more information, see[https://github.com/psf/requests/issues/4601](https://github.com/psf/requests/issues/4601). Workaround #1 Avoid creating new signer/client objects, and reuse existing objects if possible. If you are using delegation token authentication, and need to update the value of the delegation token, the following example shows how to update an existing signer instead of creating a new signer:
```

```
Workaround #2 Use the[raw request signer](https://docs.oracle.com/iaas/tools/python/latest/raw-requests.html).

## Potential data corruption issue in OCI Java SDK with binary data upload using default retries

Details: If you are using any of the OCI Java SDK synchronous clients that upload streams of data (for example ObjectStorageClient or DataSafeClient) and you do not define the RetryConfiguration at the[client level](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/RetryExample.java#L47-L56)or[request level](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/RetryExample.java#L59-L68), you may be affected by silent data corruption.

Workaround: We are actively working on fixing this issue. For more information and possible workarounds,[see the issue on GitHub](https://github.com/oracle/oci-java-sdk/issues/402).

Direct link to this issue:[Potential data corruption issue in OCI Java SDK with binary data upload using default retries](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/dev_tools_known_issues.htm#knownissues_topic_Potential_data_corruption_issuein_OCI_Java_SDK_with_binary_data_upload_using_default_retries)

## Performance regression in OCI Java SDK versions 2.14.1 and later for all API operations

Details: If you're using versions 2.14.1 and later of the OCI Java SDK, you may encounter performance regressions when using the SDK to call API operations on any of the OCI services. The regression causes a 30% to 60% increase in latency in SDK operations on any of the OCI services.

Workaround: For more information and possible workarounds,[see the issue on GitHub](https://github.com/oracle/oci-java-sdk/issues/378).

Direct link to this issue:[Performance regression in OCI Java SDK versions 2.14.1 and later for all API operations](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/dev_tools_known_issues.htm#knownissues_topic_java_sdk_performance_regression_2141)

## Performance regression with the Apache Connector Provider in OCI SDK for Java

Details: Starting with version 2.0.0, the OCI SDK for Java supports using the Jersey`ApacheConnectorProvider`instead of the Jersey default`HttpUrlConnectorProvider`to allow the Apache HttpClient to make OCI service calls.

The`ApacheConnectorProvider`supports the use of`Expect`header by default for some Object Storage service operations (see[https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/100](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/100)). This has been observed to cause performance regression in the same Object Storage service operations.
Workaround: You can disable the use of the`Expect`header by switching back to Jersey Default Connector (see[https://docs.oracle.com/iaas/Content/API/SDKDocs/javasdkconfig.htm](https://docs.oracle.com/iaas/Content/API/SDKDocs/javasdkconfig.htm)), or if you're already using the`ApacheConnectorProvider`, you can disable the`Expect`header with the`ApacheConnectorProvider`by doing the following when initializing the client :
```

```

Direct link to this issue:[Performance regression with the Apache Connector Provider in OCI SDK for Java](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/dev_tools_known_issues.htm#knownissues_topic_apache_connector_performance_regression_java_sdk)

## Truncated response for operations that return binary data with the OCI Java SDK

Details: In versions 2.0.0 to 2.13.0 of the OCI Java SDK API, some operations that return a stream of data but don't return the content-length header in the response might return truncated data. This is caused by the SDK prematurely closing the stream before reading all the data.

Workaround: Update the OCI Java SDK client to version 2.13.1 or later. For more information about this issue and workarounds, see[https://github.com/oracle/oci-java-sdk/issues/357](https://github.com/oracle/oci-java-sdk/issues/357)

Direct link to this issue:[Truncated response for operations that return binary data with the OCI Java SDK](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/dev_tools_known_issues.htm#knownissues_topic_truncated_binary_response_data_java_sdk)

## Go SDK cannot automatically find some regions while running in Cloud Shell

Details: Due to some issues with one of its dependencies, the Go SDK feature which allows customers to automatically use new realms which might be unknown to the SDK is not functioning from within Cloud Shell.
Attempting to run code in Cloud Shell that uses this feature will result in the following error message:
```

```

Workaround: To resolve this issue, enable resolving regions using the instance metadata service for Go SDK. For more information, see:[Adding Regions](https://docs.oracle.com/iaas/Content/API/Concepts/sdk_adding_new_region_endpoints.htm)

## Increased latency issues in operations for some OCI services using the SDKS and other tools

Details: You may encounter an increase in latency for operations made to some OCI services using the SDKs, Terraform, Ansible, and the CLI. This issue has been confirmed to impact the OCI Streaming service, and likely impacts the Email Delivery, Health Checks, NoSQL Database Cloud, Registry, Generic Artifacts, and Web Application Acceleration and Security services as well. This list is not comprehensive, and it is possible you may encounter the issue against other OCI services as well. The issue has been confirmed to NOT affect the OCI Object Storage and Functions services.

The following SDKs and tools are impacted:

- Go SDK (version 41.2.0 and later)
- .NET SDK (version 14.2.0 and later)
- Java SDK (version 2.0.0 and later)
- Python SDK (version 2.38.4 and later)
- CLI (version 2.25.0 and later)
- PowerShell Modules (version 9.2.0 and later)
- Ansible Modules (version 2.23.0 and later)
- Terraform Provider (version 4.30.0 and later)

Workarounds and more information: We are actively working on fixing this issue. For more information and possible workarounds, please see the following:

- [Go SDK](https://github.com/oracle/oci-go-sdk/issues/306)
- [.NET SDK](https://github.com/oracle/oci-dotnet-sdk/issues/63)
- [Java SDK](https://github.com/oracle/oci-java-sdk/issues/320)
- [Python SDK](https://github.com/oracle/oci-python-sdk/issues/367)
- [CLI](https://github.com/oracle/oci-cli/issues/428)
- [PowerShell Modules](https://github.com/oracle/oci-powershell-modules/issues/51)
- [Ansible Modules](https://github.com/oracle/oci-ansible-collection/issues/90)
- [Terraform Provider](https://github.com/oracle/terraform-provider-oci/issues/1407)

Direct link to this issue:[Increased latency issues in operations for some OCI services using the SDKS and other tools](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/dev_tools_known_issues.htm#increased_latency_SDK_100_continue)

## Python SDK composite operations throw a 404 NotAuthorizedOrNotFound error even though operation is a success

Details: The copy_boot_volume_backup_and_wait_for_state and copy_volume_backup_and_wait_for_state from the BlockStorage Client Composite operations throw a 404/NotAuthorizedOrNotFound when copying a backup from one region to another. For more information see:[https://github.com/oracle/oci-python-sdk/issues/344](https://github.com/oracle/oci-python-sdk/issues/344).

Workaround: Instead of using the composite operations, use two different clients for this operation; one client in the Source Region to send the request for copying the backup from Region A to Region B, and a second client in Destination region to wait for the backup to become available. See example here:[https://github.com/oracle/oci-python-sdk/blob/master/examples/copy_volume_backup_example.py](https://github.com/oracle/oci-python-sdk/blob/master/examples/copy_volume_backup_example.py)

Direct link to this issue:[Python SDK composite operations throw a 404 NotAuthorizedOrNotFound error even though operation is a success](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/dev_tools_known_issues.htm#block_volume_python_sdk_composite_operation_404_SDK)

## Potential data rounding issue for big numbers with OCI SDK for TypeScript and JavaScript

Details: The OCI SDK for TypeScript and JavaScript have a known issue with big numbers greater than JavaScript's Number.MAX_SAFE_INTEGER. Any Numbers greater than Number.MAX_SAFE_INTEGER will result in rounding issue.

Workaround: We are aware of the issue where an API response may send back a number greater than JavaScript's Number.MAX_SAFE_INTERGER. At the moment the number rounding issue is not an impact to calling any APIs.

Direct link to this issue:[Potential data rounding issue for big numbers with OCI SDK for TypeScript and JavaScript](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/dev_tools_known_issues.htm#javaSDKStreamDataCorrupt)

## Potential data corruption issue with OCI Java SDK on binary data upload with RefreshableOnNotAuthenticatedProvider

Details: When using version 1.25.1 or earlier of the OCI Java SDK clients that upload streams of data (for example`ObjectStorageClient`or`FunctionsInvokeClient`), either synchronously and asynchronously, and you use a`RefreshableOnNotAuthenticatedProvider`(for example, for Resource Principals or Instance Principals) you may be affected by silent data corruption.

Workaround: Update the OCI Java SDK client to version 1.25.2 or later. For more information about this issue and workarounds, see[Potential data corruption issue for OCI Java SDK on binary data upload with RefreshableOnNotAuthenticatedProvider](https://github.com/oracle/oci-java-sdk/issues/255).

Direct link to this issue:[Potential data corruption issue with OCI Java SDK on binary data upload with RefreshableOnNotAuthenticatedProvider](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/dev_tools_known_issues.htm#javaSDKStreamDataCorrupt-9)

## Potential data corruption issue with OCI HDFS Connector on binary data upload with RefreshableOnNotAuthenticatedProvider

Details: If you are using version 3.2.1.1 or earlier of the OCI HDFS Connector clients and you use a RefreshableOnNotAuthenticatedProvider (e.g. InstancePrincipalsCustomAuthenticator, or generally for Resource Principals or Instance Principals) you may be affected by silent data corruption .

Workaround: Update the OCI HDFS Connector client to version 3.2.1.3 or later. For more information about this issue and workarounds, see[Potential data corruption issue for OCI HDFS Connector with RefreshableOnNotAuthenticatedProvider](https://github.com/oracle/oci-hdfs-connector/issues/35).

Direct link to this issue:[Potential data corruption issue with OCI HDFS Connector on binary data upload with RefreshableOnNotAuthenticatedProvider](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/dev_tools_known_issues.htm#knownissues_topic_Potential_data_corruption_with_OCI_Java_SDK_on_binary_data_upload_with_RefreshableOnNotAuthenticatedProvider_HDFS)

## Potential data corruption with SDK for Python on binary upload

Details: When using the SDK for Python to perform binary upload operations you may encounter an issue with data corruption if retries are enabled or if you are using`UploadManager.upload_file`.

Workaround: We're working on a resolution. For more information about this issue and workarounds, see[Potential data corruption issue for PythonSDK retry on binary data upload](https://github.com/oracle/oci-python-sdk/issues/203).

Direct link to this issue:[Potential data corruption with SDK for Python on binary upload](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/dev_tools_known_issues.htm#pythonDataCorrupt)

## Potential data corruption issue with SDK for Python and upload streams

Update: The root cause of the issue causing data corruption has been fixed with the release of v2.54.0. Please use oci v2.54.0 or above to avoid data corruption. The behavior of older versions of the OCI Python SDK regarding this issue has been explained below.

Details: Customers using the OCI SDK for Python and`oci.object_storage.UploadManager.upload_stream`in FIPS mode might be vulnerable to silent data corruption. If the circumstances to produce the issue are true for your environment, the SDK reports success for the upload operation, but a 0-length object is uploaded.

The resolution differs depending on the state of your environment:
- Using`UploadManager.upload_stream()`in an environment which uses a FIPS-compliant OpenSSL version where the SDK for Python is not operating in FIPS mode as described in[Using FIPS validated libraries](https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/fips-libraries.html).

To determine if you fall under this scenario:
- 

Verify that you are using a FIPS-compliant OpenSSL version by running the command`openssl version`. If "fips" is part of the version name, and you are not operating the SDK in FIPS mode, then you would fall under this scenario.
- 

If`oci.fips.is_fips_mode()`does not return True, then the SDK is not operating in FIPS mode.
Workaround: Upgrade the OCI SDK for Python to version 2.53.1 or greater and operate the SDK for Python in FIPS mode as described in[Using FIPS validated libraries](https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/fips-libraries.html).
Important  
  
Not operating the SDK in FIPS mode while using a FIPS-compliant OpenSSL version will still result in data corruption while using`UploadManager.upload_stream()`.
- Using`UploadManager.upload_stream()`when the SDK for Python is operating in FIPS mode as described in[Using FIPS validated libraries](https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/fips-libraries.html)and the SDK for Python is v2.53.0 or lower.

If`oci.fips.is_fips_mode()`returns True, then the SDK is operating in FIPS mode.

Resolution: Upgrade the OCI SDK for Python to version 2.53.1 or greater.

For more information about this issue, see[Potential data corruption issue for multipart stream upload for OCI Python SDK](https://github.com/oracle/oci-python-sdk/issues/410)on GitHub.

Direct link to this issue :[Potential data corruption issue with SDK for Python and upload streams](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/dev_tools_known_issues.htm#pythonUploadStreamsCorrupt)

## WebLogic Management

For known issues with WebLogic Management, see[Known Issues](https://docs.oracle.com/iaas/wlms/doc/known-issues.htm)
