# Using Kafka Connect
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility_topic-Kafka_Connect.htm
- Fetched: 2026-09-05 03:06 CDT

# Using Kafka Connect

Use Kafka Connect with Oracle Cloud Infrastructure Streaming.

[Managing Kafka Connect Configurations](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/managingkafkaconnectharnesses.htm)provides steps for using the Console, CLI, and API.

To use your Kafka connectors with Oracle Cloud Infrastructure Streaming,[create a Kafka Connect configuration . The[Streaming API](https://docs.oracle.com/iaas/api/#/en/streaming/)calls these configurations harnesses .
Note  
  
Kafka Connect configurations work only for streams in the same compartment.

You can use multiple Kafka connectors with the same Kafka Connect configuration. In cases that require producing or consuming streams in separate compartments, or where more capacity is required to avoid hitting throttle limits on the Kafka Connect configuration (for example: too many connectors, or connectors with too many workers), you can create more Kafka Connector configurations.

For more information on managing Kafka Connect configurations, see[Managing Kafka Connect Configurations](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/managingkafkaconnectharnesses.htm).

## Kafka Connectors

The Kafka Connect compatibility in Streaming means that you can take advantage of the many existing first- and third-party connectors to move data from your sources to your targets.

Kafka connectors for Oracle products:
- Oracle Cloud Infrastructure Object Storage (Using Kafka Connect for S3)
- [Kafka Connect Amazon S3 source connector](https://docs.confluent.io/current/connect/kafka-connect-s3-source/index.html), for producers
- [Kafka Connect Amazon S3 sink connector](https://docs.confluent.io/current/connect/kafka-connect-s3/index.html), for consumers
- [Oracle Integration Cloud](https://docs.oracle.com/en/cloud/paas/integration-cloud/apache-kafka-adapter/kafka-adapter-capabilities.html)
- [Oracle GoldenGate](https://docs.oracle.com/en/middleware/goldengate/big-data/12.3.2.1/gadbd/using-kafka-connect-handler.html)
- [JDBC source Kafka connect from Confluent](https://docs.confluent.io/current/connect/kafka-connect-jdbc/index.html)

For a complete list of third-party Kafka source and sink connectors, see[the official Confluent Kafka hub](https://www.confluent.io/hub/).

## Kafka Connect Topics

The Streaming service automatically creates the three topics ( config , offset , and status ) that are required to use Kafka Connect when you create the Kafka Connect configuration. These topics contain the OCID of the Kafka Connect configuration in their names.

Place these topic names in the`connect-distributed.properties`file of the Kafka connector that you want to use with Streaming.

For example:

```

```

Note  
  
These three compacted topics are meant to be used by Kafka Connect and Streaming to store configuration and state management data. Don't use them to store your data. To ensure that the Kafka Connect configuration topics are being used for their intended purpose by the connectors, there are hard throttle limits of 50 kb/s and 50 rps in place for these topics.

## Bootstrap Server

Set the bootstrap server in your Kafka connector properties file to the endpoint for Streaming on port 9092. For example:

```

```

Note  
  
For a list of endpoints for Streaming, see the Streaming section in[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

## Authentication

Authentication with the Kafka protocol uses auth tokens and the SASL/PLAIN mechanism. You can generate tokens in the Console user details page. See[Working with Auth Tokens](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcredentials.htm#Working)for more information.
Tip  
  
Create a dedicated group and grant that group the permission to manage streams in the appropriate compartment or tenancy. You then can generate an auth token for the user you created and use it in your Kafka client configuration.

## Example Kafka Connector Properties File

The following shows an example Kafka connector`connect-distributed.properties`file:

```

```

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

To allow a group to manage Kafka Connect configurations, you need to create the correct policy in your tenancy. For example:
```

```

For administrators: The policy in[Let streaming admins manage streaming resources](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#streaming-manage-streams)lets the specified group do everything with streaming and related Streaming service resources.

If you're new to policies, see[IAM Policies Overview](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm). For more information, see:

- [Details for the Streaming Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/streamingpolicyreference.htm)in the IAM policy reference
- [Accessing Streaming Resources Across Tenancies](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/accessing-streaming-resources-across-tenancies.htm)
- [Official Kafka Connect documentation](https://docs.confluent.io/current/connect/index.html)
- Blog post:[Oracle Streaming Service with Kafka Connect](https://blogs.oracle.com/developers/oracle-streaming-service-with-kafka-connect)
