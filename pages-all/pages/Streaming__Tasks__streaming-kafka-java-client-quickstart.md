# Kafka Java Client and Streaming Quickstart
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-kafka-java-client-quickstart.htm
- Fetched: 2026-09-05 03:06 CDT

# Kafka Java Client and Streaming Quickstart

Publish and consume messages in the Streaming service using the Kafka Java client.

This quickstart shows you how to use the[Kafka Java client](https://docs.confluent.io/clients-kafka-java/current/overview.html)with Oracle Cloud Infrastructure Streaming to publish and consume messages.

For more information, see[Using Streaming with Apache Kafka](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility.htm). For key concepts and more Streaming details, see[Overview of Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Concepts/streamingoverview.htm)

## Prerequisites

- 

To use the Kafka Java client with Streaming, you must have the following:
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
- JDK 8 or above installed. Ensure that Java is in your PATH.
- Maven 3.0 or installed. Ensure that Maven is in your PATH.
- Intellij (recommended) or any other integrated development environment (IDE).
- 

Add the latest version of the Maven dependency or jar for[Kafka Java SDK](https://mvnrepository.com/artifact/org.apache.kafka/kafka-clients)to your`pom.xml`as follows:

```

```

- 

Assuming`wd`as your working directory for your Java project of this example, your`pom.xml`will look similar to the following:

```

```

- 

Authentication with the Kafka protocol uses auth tokens and the SASL/PLAIN mechanism. Refer to[Working with Auth Tokens](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcredentials.htm#Working)for auth token generation. If you created the stream and stream pool in OCI, you are already authorized to use this stream according to OCI IAM, so you should create auth tokens for your OCI user.
Note  
  
OCI user auth tokens are visible only at the time of creation. Copy it and keep it somewhere safe for future use.

## Producing Messages

- Open your favorite editor, such as Visual Studio Code, from the directory`wd`. You should already have the Kafka SDK dependencies for Java as part of the`pom.xml`of your Maven Java project after you've met the[prerequisites](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-kafka-java-client-quickstart.htm#prerequisites).
- 

Create a new file named`Producer.java`in directory`wd`under the path`/src/main/java/kafka/sdk/oss/example/`with following code. Replace the values of variables in the code as directed by the code comments, namely`bootstrapServers`through`streamOrKafkaTopicName`. These variables are for Kafka connection settings which you gathered in the[prerequisites](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-kafka-java-client-quickstart.htm#prerequisites).

```

```

- 

From the`wd`directory, run the following command:

```

```

- [Show latest messages sent to the stream](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/show-recent-messages.htm)to see the latest messages sent to the stream to verify that production was successful.

## Consuming Messages

- First, ensure that the stream you want to consume messages from contains messages. You could[use the Console to produce a test message](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/publishingmessages.htm#console), or use the stream and messages we[created in this quickstart](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-kafka-java-client-quickstart.htm#produce-messages).
- Open your favorite editor, such as Visual Studio Code, from the directory`wd`under the path`/src/main/java/kafka/sdk/oss/example/`. You should already have the Kafka SDK dependencies for Java as part of the`pom.xml`of your Maven Java project after you've met the[prerequisites](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-kafka-java-client-quickstart.htm#prerequisites).
- 

Create a new file named`Consumer.java`in directory`wd`with following code. Replace the values of variables in the code as directed by the code comments, namely`bootstrapServers`through`consumerGroupName`. These variables are for Kafka connection settings which you gathered in the[prerequisites](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-kafka-java-client-quickstart.htm#prerequisites).

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
- [Kafka Producer API Java Docs](https://kafka.apache.org/22/javadoc/org/apache/kafka/clients/producer/ProducerConfig.html)
- [Kafka Consumer API Java Docs](https://kafka.apache.org/22/javadoc/org/apache/kafka/clients/consumer/KafkaConsumer.html)
