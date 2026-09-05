# Kafka Python Client and Streaming Quickstart
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-kafka-python-client-quickstart.htm
- Fetched: 2026-09-05 03:06 CDT

# Kafka Python Client and Streaming Quickstart

Publish and consume messages in the Streaming service using the Kafka Python client.

This quickstart shows you how to use the[Kafka Python client](https://docs.confluent.io/clients-confluent-kafka-python/current/overview.html)with Oracle Cloud Infrastructure Streaming to publish and consume messages.

For more information, see[Using Streaming with Apache Kafka](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility.htm). For key concepts and more Streaming details, see[Overview of Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Concepts/streamingoverview.htm)

## Prerequisites

- 

To use the Kafka Python client with Streaming, you must have the following:
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
- Python 3.6 or later, with PIP installed and updated.
- Visual Studio Code (recommended) or any other integrated development environment (IDE).
- 

Install`Confluent-Kafka`packages for Python using the following command:

```

```

Note  
  
You can install these packages globally, or within a[virtualenv](https://docs.python.org/3/library/venv.html). The`librdkafka`package is used by the`confluent-kafka`package and embedded in wheels for the latest`confluent-kafka`release. For more details, refer to the[Confluent Python client documentation](https://github.com/confluentinc/confluent-kafka-python/blob/master/README.md#prerequisites).
- 

Install the SSL CA root certificates on the host where you are developing and running this quickstart. The client uses CA certificates to verify the broker's certificate.

For Windows, download the`cacert.pem`file distributed with curl ([download cacert.pm](https://curl.haxx.se/ca/cacert.pem)). For other platforms, refer to[Configure SSL trust store](https://docs.confluent.io/platform/current/tutorials/examples/clients/docs/python.html#configure-ssl-trust-store).
- 

Authentication with the Kafka protocol uses auth tokens and the SASL/PLAIN mechanism. Refer to[Working with Auth Tokens](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcredentials.htm#Working)for auth token generation. If you created the stream and stream pool in OCI, you are already authorized to use this stream according to OCI IAM, so you should create auth tokens for your OCI user.
Note  
  
OCI user auth tokens are visible only at the time of creation. Copy it and keep it somewhere safe for future use.

## Producing Messages

- Open your favorite editor, such as Visual Studio Code, from the empty working directory`wd`. You should already have`confluent-kafka`packages for Python installed for your current Python environment after you've met the[prerequisites](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-kafka-python-client-quickstart.htm#prerequisites).
- 

Create a file named`Producer.py`in the`wd`directory with following code. Replace the config values in the map`conf`and the name of topic is the name of stream you created.

```

```

- 

From the`wd`directory, run the following command:

```

```

- [Show latest messages sent to the stream](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/show-recent-messages.htm)to see the latest messages sent to the stream to verify that production was successful.

## Consuming Messages

- First, ensure that the stream you want to consume messages from contains messages. You could[use the Console to produce a test message](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/publishingmessages.htm#console), or use the stream and messages we[created in this quickstart](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-kafka-python-client-quickstart.htm#produce-messages).
- Open your favorite editor, such as Visual Studio Code, from the empty working directory`wd`. You should already have`confluent-kafka`packages for Python installed for your current Python environment after you've met the[prerequisites](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-kafka-python-client-quickstart.htm#prerequisites).
- 

Create a file named`Consumer.py`in the`wd`directory with following code. Replace the config values in the map`conf`and the name of topic is the name of stream you created.

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
- [Confluent Kafka Python client](https://docs.confluent.io/clients-confluent-kafka-python/current/overview.html#ak-python)
- [Confluent Kafka Python client GitHub](https://github.com/confluentinc/confluent-kafka-python)
