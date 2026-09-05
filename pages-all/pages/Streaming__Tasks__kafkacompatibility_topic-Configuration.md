# Using Kafka APIs
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility_topic-Configuration.htm
- Fetched: 2026-09-05 03:06 CDT

# Using Kafka APIs

Configure Apache Kafka for API compatibility with Oracle Cloud Infrastructure Streaming. When your producers use Kafka APIs to interact with Streaming, the decision of which partition to publish a unique message to is handled client-side by Kafka.

The following information provides Java examples. For Python examples, see[Kafka Python Client and Streaming Quickstart](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-kafka-python-client-quickstart.htm).

Refer to[Kafka API Support](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility.htm#kafka_apis)for additional information.

## Endpoints

For bootstrap servers, use your region endpoint on port 9092. For example:

```

```

## Authentication

Authentication with the Kafka protocol uses auth tokens and the SASL/PLAIN mechanism. You can generate tokens in the Console user details page. See[Working with Auth Tokens](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcredentials.htm#Working)for more information.
Tip  
  
Create a dedicated group/user and grant that group the permission to manage streams in the appropriate compartment or tenancy. The policy in[Let streaming admins manage streaming resources](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#streaming-manage-streams)lets the specified group do everything with streaming and related Streaming service resources. You then can generate an auth token for the user you created and use it in your Kafka client configuration.

Your username must be in the following format:

```

```

Tip  
  
If you are using the Java SDK, you can also use[instance principal authorization](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility_topic-Configuration.htm#top__InstancePrincipalAuth).

## Kafka Configuration

Set the following properties for your Kafka client. For the Java SDK

Recommended settings for Java SDK:

```

```

Recommended settings for Java SDK producers:

```

```

Recommended settings for Java SDK consumers:

```

```
For the Librdkafka SDK

Recommended settings for Librdkafka SDK:

```

```

Recommended settings for Librdkafka SDK producers:

```

```

Recommended settings for Librdkafka SDK consumers:

```

```

## Instance Principal Authorization for the Java SDK

If you are using the Java SDK, you can authorize an instance to interact with Streaming instead of using auth tokens.

To configure the Java SDK for instance principal authorization:
- Verify that you have a valid Oracle Cloud Infrastructure (OCI)[SDK and CLI configuration file](https://docs.oracle.com/iaas/Content/API/Concepts/sdkconfig.htm).
- Import the Oracle Cloud Infrastructure SDK for Java into your project. See[Getting Started with the SDK for Java](https://docs.oracle.com/iaas/Content/API/SDKDocs/javasdkgettingstarted.htm#Getting_Started)for more information.
- Add the following Oracle Cloud Infrastructure SDK for Java dependency:

```

```

- Modify the`sasl.mechanism`property of your[Kafka client configuration](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility_topic-Configuration.htm#top__Configuration-SDKs):

```

```

- Modify the`sasl.jaas.config`property of your[Kafka client configuration](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility_topic-Configuration.htm#top__Configuration-SDKs)using one of the following options:

```

```

```

```

- If`config`is not specified, the default config path is used (`~/.oci/config`).
- If`profile`is not specified, the default profile is used (DEFAULT).

## For More Information
- [Apache Kafka documentation](https://kafka.apache.org/documentation/)
- Blog post:[Oracle Streaming Service Producer and Consumer](https://blogs.oracle.com/developers/oracle-streaming-service-producer-consumer)
