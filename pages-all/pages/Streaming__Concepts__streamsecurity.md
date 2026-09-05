# Security Best Practices for Streaming
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/streamsecurity.htm
- Fetched: 2026-09-05 03:05 CDT

# Security Best Practices for Streaming

Review encryption and private access options for securing streams in the Streaming service.

Streaming data is[encrypted](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/streamsecurity.htm#stream_encryption)both at rest and in transit.[Private endpoints](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/streamsecurity.htm#private_endpoints)within your virtual cloud network (VCN) can be used to restrict access to your streams so they cannot be accessed through the internet.

Both encryption and private access are configured at the[stream pool](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/../Tasks/managing-stream-pools.htm)level to make managing groups of streams easier. For more information, see[Creating a Stream Pool](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/../Tasks/creating-stream-pools.htm)and[Updating a Stream Pool](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/../Tasks/updating-stream-pools.htm).

## Encryption

By default, all encryption-related matters are handled by Oracle, but you can manage your own encryption keys using OCI Vault. Vault allows you to bring your own Advanced Encryption Standard (AES) symmetric keys and manage, rotate, disable, and delete them as needed.

Because encryption keys are managed at the stream pool level, you can use a different encryption key for each logical stream grouping or virtual Kafka cluster.

To use your own encryption key:
- Ensure that you have the[required IAM policies](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/streaminggettingstarted.htm#creating_stream_pools_iam).
- [Import your key](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/importingkeys.htm).
- [Change the master encryption key assigned to the stream pool](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/../Tasks/updating-stream-pools.htm).

For more information, see[Overview of Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)and[Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm).

## Private Endpoints

Private endpoints associate a private IP address within a VCN to the stream pool, allowing Streaming traffic to avoid traversing the internet.

To create a private endpoint for Streaming, you need access to a VCN with a private subnet when you create the stream pool. See[About Private Endpoints](https://docs.oracle.com/iaas/Content/Network/Concepts/privateaccess.htm#private-endpoints)and[VCN and Subnet Management](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm)for more information.

To use private endpoints:
- Ensure that you have the[required IAM policies](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/streaminggettingstarted.htm#creating_stream_pools_iam).
- Select Private Endpoint and provide the required information when you[create your stream pool](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/../Tasks/creating-stream-pools.htm#console).

Because streams using private endpoints aren't accessible from the internet, you can't use the Console to[show their latest messages](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/../Tasks/show-recent-messages.htm)
