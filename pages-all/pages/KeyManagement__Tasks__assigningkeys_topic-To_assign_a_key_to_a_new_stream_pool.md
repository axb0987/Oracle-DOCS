# Assigning a key to a stream pool
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_a_new_stream_pool.htm
- Fetched: 2026-09-05 02:31 CDT

# Assigning a key to a stream pool

Assign a key to a new stream pool using the OCI Console and CLI interface.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_a_new_stream_pool.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_a_new_stream_pool.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_a_new_stream_pool.htm#)
- 

- Open the navigation menu and select Analytics &amp; AI . Under Messaging , select Streaming .
- Under List Scope , in the Compartment list, choose the compartment where you want to create a stream pool that's encrypted with a Vault service master encryption key.
- 

Select Create Stream Pool , and then follow the instructions in[Creating Stream Pools](https://docs.oracle.com/iaas/Content/Streaming/Tasks/creating-stream-pools.htm#create-stream-pool-console)in[Creating Stream Pools](https://docs.oracle.com/iaas/Content/Streaming/Tasks/creating-stream-pools.htm).
- 

This task cannot be performed using the CLI.
- 

Run the[CreateStreamPool](https://docs.oracle.com/iaas/api/#/en/streaming/latest/StreamPool/CreateStreamPool)and[UpdateStreamPool](https://docs.oracle.com/iaas/api/#/en/streaming/latest/StreamPool/UpdateStreamPool)operations to create and update a stream pool.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
