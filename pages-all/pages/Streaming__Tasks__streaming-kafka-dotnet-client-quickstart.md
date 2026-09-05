# Kafka .NET Client and Streaming Quickstart
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-kafka-dotnet-client-quickstart.htm
- Fetched: 2026-09-05 03:06 CDT

# Kafka .NET Client and Streaming Quickstart

Publish and consume messages in the Streaming service using the Kafka .NET client.

This quickstart shows you how to use the[Kafka .NET client](https://docs.confluent.io/clients-confluent-kafka-dotnet/current/overview.html)with Oracle Cloud Infrastructure Streaming to publish and consume messages. These examples use C# language.

For more information, see[Using Streaming with Apache Kafka](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility.htm). For key concepts and more Streaming details, see[Overview of Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Concepts/streamingoverview.htm)

## Prerequisites

Note  
  
In this quickstart, we create and run a simple .NET console application by using Visual Studio Code and the .NET CLI. Project tasks, such as creating, compiling, and running a project are done by using the .NET CLI. If you prefer, you can follow this tutorial with a different IDE and run commands in a terminal.
- 

To use the Kafka .NET client with Streaming, you must have the following:
- An Oracle Cloud Infrastructure account.
- A user created in that account, in a group with a policy that grants the required permissions. For an example of how to set up a new user, group, compartment, and policy, see[Adding Users](https://docs.oracle.com/iaas/Content/GSG/Tasks/addingusers.htm). For a list of typical policies you may want to use, see[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).
- 

Collect the following details:
- Stream OCID
- Messages endpoint
- Stream pool OCID
- Stream pool FQDN
- Kafka connection settings:
- Bootstrap servers
- SASL connection strings
- Security protocol

For steps to create and manage streams and stream pools, see[Managing Streams](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/managingstreams.htm)and[Managing Stream Pools](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/managing-stream-pools.htm). Streams correspond to a Kafka topic.
- Install[.NET 5.0 SDK or later](https://dotnet.microsoft.com/download). Ensure that`dotnet`is set in your`PATH`environment variable.
- 

Visual Studio Code (recommended) with the[C# extension](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp)installed. For information about how to install extensions on Visual Studio Code, see[VS Code Extension Marketplace](https://code.visualstudio.com/docs/editor/extension-gallery).
- 

Authentication with the Kafka protocol uses auth tokens and the SASL/PLAIN mechanism. Refer to[Working with Auth Tokens](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcredentials.htm#Working)for auth token generation. If you created the stream and stream pool in OCI, you are already authorized to use this stream according to OCI IAM, so you should create auth tokens for your OCI user.
Note  
  
OCI user auth tokens are visible only at the time of creation. Copy it and keep it somewhere safe for future use.
- 

Install the SSL CA root certificates on the host where you are developing and running this quickstart. The client uses CA certificates to verify the broker's certificate.

For[Windows](https://docs.confluent.io/platform/current/tutorials/examples/clients/docs/csharp.html#prerequisites), download the`cacert.pem`file distributed with curl ([download cacert.pm](https://curl.haxx.se/ca/cacert.pem)). For other platforms, refer to[Configure SSL trust store](https://docs.confluent.io/platform/current/tutorials/examples/clients/docs/csharp.html#configure-ssl-trust-store).

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

To reference the`confluent-kafka-dotnet`library in your new .NET Core project, run the following command in your project's directory`wd`:

```

```

- 

Replace the code in`Program.cs`in the`wd`directory with following code. Replace values of variables in the map`ProducerConfig`and the name of`topic`with the details you gathered in the[prerequisites](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-kafka-dotnet-client-quickstart.htm#prerequisites):

```

```

- 

From the`wd`directory, run the following command:

```

```

- [Show latest messages sent to the stream](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/show-recent-messages.htm)to verify that production was successful.

## Consuming Messages

- First, ensure that the stream you want to consume messages from contains messages. You could[use the Console to produce a test message](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/publishingmessages.htm#console), or use the stream and messages we[created in this quickstart](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-kafka-dotnet-client-quickstart.htm#produce-messages).
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

To reference the`confluent-kafka-dotnet`library in your new .NET Core project, run the following command in your project's directory`wd`:

```

```

- 

Replace the code in`Program.cs`in the`wd`directory with following code. Replace values of variables in the map`ProducerConfig`and the name of`topic`with the details you gathered in the[prerequisites](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-kafka-dotnet-client-quickstart.htm#prerequisites):

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
- [Using Streaming with Apache Kafka](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility.htm)and[Using Kafka APIs](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility_topic-Configuration.htm)
- [OCI SDK for .NET Streaming Quickstart](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-quickstart-oci-sdk-for-dotnet.htm)
