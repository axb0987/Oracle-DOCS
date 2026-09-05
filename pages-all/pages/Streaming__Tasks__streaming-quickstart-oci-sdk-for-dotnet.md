# SDK for .NET Streaming Quickstart
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-quickstart-oci-sdk-for-dotnet.htm
- Fetched: 2026-09-05 03:06 CDT

# SDK for .NET Streaming Quickstart

Publish and consume messages in the Streaming service using OCI SDK for .NET.

This quickstart shows you how to use the Oracle Cloud Infrastructure (OCI)[SDK for .NET](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON__json_complex_input)and Oracle Cloud Infrastructure Streaming to publish and consume messages. These examples use C# language.

For key concepts and more Streaming details, see[Overview of Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Concepts/streamingoverview.htm). For more information about using the OCI SDKs, see the[SDK Guides](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

## Prerequisites

Note  
  
In this quickstart, we create and run a simple .NET console application by using Visual Studio Code and the .NET CLI. Project tasks, such as creating, compiling, and running a project are done by using the .NET CLI. If you prefer, you can follow this tutorial with a different IDE and run commands in a terminal.
- 

To use the SDK for .NET, you must have the following:
- An Oracle Cloud Infrastructure account.
- A user created in that account, in a group with a policy that grants the required permissions. This user can be yourself, or another person/system that needs to call the API. For an example of how to set up a new user, group, compartment, and policy, see[Adding Users](https://docs.oracle.com/iaas/Content/GSG/Tasks/addingusers.htm). For a list of typical policies you may want to use, see[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).
- A key pair used for signing API requests, with the public key uploaded to Oracle. Only the user calling the API should possess the private key. For more information, see[SDK configuration file](https://docs.oracle.com/iaas/Content/API/Concepts/sdkconfig.htm).
- Collect the Messages endpoint and OCID of a stream. For steps to get details for a stream, see[Getting Details for a Stream](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/get-stream.htm). For the purposes of this quickstart, the stream should use a public endpoint and let Oracle manage encryption. Refer to[Creating a Stream](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/creatingstreamsandstreampools_create-stream.htm)and[Creating a Stream Pool](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/creating-stream-pools.htm)if you do not have an existing stream.
- Install[.NET 5.0 SDK or later](https://dotnet.microsoft.com/download). Ensure that`dotnet`is set in your`PATH`environment variable.
- 

Visual Studio Code (recommended) with the[C# extension](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp)installed. For information about how to install extensions on Visual Studio Code, see[VS Code Extension Marketplace](https://code.visualstudio.com/docs/editor/extension-gallery).
- Ensure that you have a valid[SDK configuration file](https://docs.oracle.com/iaas/Content/API/Concepts/sdkconfig.htm). For production environments, you should use[instance principal authorization](https://docs.oracle.com/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm).

## Producing Messages

- Open your favorite editor, such as Visual Studio Code, from the empty working directory`wd`.
- Open the terminal and`cd`into the`wd`directory.
- 

Create a C# .NET console application by running the following command in the terminal:

```

```

You should see a message indicating that the application was created:
```

```

This creates a`Program.cs`file with C# code for a simple "HelloWorld" application.
- 

Add OCI SDK packages for basic IAM authentication and Streaming to your C# project as follows:

```

```

```

```

- 

Replace the code in`Program.cs`in the`wd`directory with following code. Replace values of variables`configurationFilePath`,`profile`,`ociStreamOcid`, and`ociMessageEndpoint`in the following code snippet with the values applicable for your tenancy.

```

```

- 

From the`wd`directory, run the following command:

```

```

- [Show latest messages sent to the stream](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/show-recent-messages.htm)to see the latest messages sent to the stream to verify that production was successful.

## Consuming Messages

- First, ensure that the stream you want to consume messages from contains messages. You could[use the Console to produce a test message](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/publishingmessages.htm#console), or use the stream and messages we[created in this quickstart](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-quickstart-oci-sdk-for-dotnet.htm#produce-messages-dotnet).
- Open your favorite editor, such as Visual Studio Code, from the empty working directory`wd`.
- 

Create a C# .NET console application by running the following command on the terminal:

```

```

You should see a message indicating that the application was created:
```

```

This creates a`Program.cs`file with C# code for a simple "HelloWorld" application.
- 

Add OCI SDK packages for basic IAM authentication and Streaming to your C# project as follows:

```

```

```

```

- 

Replace the code in`Program.cs`in the`wd`directory with following code. Replace values of variables`configurationFilePath`,`profile`,`ociStreamOcid`, and`ociMessageEndpoint`in the following code snippet with the values applicable for your tenancy.

```

```

- 

From the`wd`directory, run the following command:

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
- [OCI SDK for .NET on GitHub](https://github.com/oracle/oci-dotnet-sdk)
- [OCI SDK for .NET examples](https://github.com/oracle/oci-dotnet-sdk/tree/master/Streaming)
