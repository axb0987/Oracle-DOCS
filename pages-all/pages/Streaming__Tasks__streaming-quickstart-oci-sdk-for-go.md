# SDK for Go Streaming Quickstart
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-quickstart-oci-sdk-for-go.htm
- Fetched: 2026-09-05 03:06 CDT

# SDK for Go Streaming Quickstart

Publish and consume messages in the Streaming service using OCI SDK for Go.

This quickstart shows you how to use the Oracle Cloud Infrastructure (OCI)[SDK for Go](https://docs.oracle.com/iaas/Content/API/SDKDocs/gosdk.htm#SDK_for_Go)and Oracle Cloud Infrastructure Streaming to publish and consume messages.

For key concepts and more Streaming details, see[Overview of Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Concepts/streamingoverview.htm). For more information about using the OCI SDKs, see the[SDK Guides](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

## Prerequisites

- 

To use the SDK for Go, you must have the following:
- An Oracle Cloud Infrastructure account.
- A user created in that account, in a group with a policy that grants the required permissions. This user can be yourself, or another person/system that needs to call the API. For an example of how to set up a new user, group, compartment, and policy, see[Adding Users](https://docs.oracle.com/iaas/Content/GSG/Tasks/addingusers.htm). For a list of typical policies you may want to use, see[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).
- A key pair used for signing API requests, with the public key uploaded to Oracle. Only the user calling the API should possess the private key. For more information, see[SDK configuration file](https://docs.oracle.com/iaas/Content/API/Concepts/sdkconfig.htm).
- Collect the Messages endpoint and OCID of a stream. For steps to get details for a stream, see[Getting Details for a Stream](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/get-stream.htm). For the purposes of this quickstart, the stream should use a public endpoint and let Oracle manage encryption. Refer to[Creating a Stream](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/creatingstreamsandstreampools_create-stream.htm)and[Creating a Stream Pool](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/creating-stream-pools.htm)if you do not have an existing stream.
- Go installed locally. Follow[these instructions](https://golang.org/doc/install)if necessary. Ensure that`go`is in your`PATH`.
- 

Visual Studio Code (recommended) or any other integrated development environment (IDE) or text editor.
- Ensure that you have a valid[SDK configuration file](https://docs.oracle.com/iaas/Content/API/Concepts/sdkconfig.htm). For production environments, you should use[instance principal authorization](https://docs.oracle.com/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm).

## Producing Messages

- Open your favorite editor, such as Visual Studio Code, from the empty working directory`wd`.
- Create a file named`Producer.go`in this directory.
- 

Add the following code to`Producer.go`. Replace values of variables`ociConfigFilePath`,`ociProfileName`,`ociStreamOcid`, and`ociMessageEndpoint`in the following code snippet with the values applicable for your tenancy.

```

```

- Save`Producer.go`.
- 

Open the terminal and`cd`to the`wd`directory, run the following commands, in order:
- 

This command creates the`go.mod`file in the`wd`directory:

```

```

- 

This command installs the OCI SDK for Go and for Streaming:

```

```

- 

This command runs the example:

```

```

- [Show latest messages sent to the stream](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/show-recent-messages.htm)to see the latest messages sent to the stream to verify that production was successful.

## Consuming Messages

- First, ensure that the stream you want to consume messages from contains messages. You could[use the Console to produce a test message](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/publishingmessages.htm#console), or use the stream and messages we[created in this quickstart](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-quickstart-oci-sdk-for-go.htm#produce-messages-go).
- 

Add the following code to`Consumer.go`. Replace values of variables`ociConfigFilePath`,`ociProfileName`,`ociStreamOcid`, and`ociMessageEndpoint`in the following code snippet with the values applicable for your tenancy.

```

```

- Save`Consumer.go`.
- 

Open the terminal and`cd`to the`wd`directory, run the following commands, in order:
- 

This command creates the`go.mod`file in the`wd`directory:

```

```

- 

This command installs the OCI SDK for Go and for Streaming:

```

```

- 

This command runs the example:

```

```

- 

You should see messages similar to the following:
```

```

Note  
  
If you[used the Console to produce a test message](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/publishingmessages.htm#console), the key for each message is`Null`

## Next Steps

See the following resources for more information:
- [OCI SDK for Go on GitHub](https://github.com/oracle/oci-go-sdk)
- [OCI SDK for Go examples](https://github.com/oracle/oci-go-sdk/tree/master/streaming)
