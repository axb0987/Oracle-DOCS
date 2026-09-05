# SDK for Python Streaming Quickstart
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-quickstart-oci-sdk-for-python.htm
- Fetched: 2026-09-05 03:06 CDT

# SDK for Python Streaming Quickstart

Publish and consume messages in the Streaming service using OCI SDK for Python.

This quickstart shows you how to use the Oracle Cloud Infrastructure (OCI)[SDK for Python](https://docs.oracle.com/iaas/Content/API/SDKDocs/pythonsdk.htm#SDK_for_Python)and Oracle Cloud Infrastructure Streaming to publish and consume messages.

For key concepts and more Streaming details, see[Overview of Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Concepts/streamingoverview.htm). For more information about using the OCI SDKs, see the[SDK Guides](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

## Prerequisites

- 

To use the SDK for Python, you must have the following:
- An Oracle Cloud Infrastructure account.
- A user created in that account, in a group with a policy that grants the required permissions. This user can be yourself, or another person/system that needs to call the API. For an example of how to set up a new user, group, compartment, and policy, see[Adding Users](https://docs.oracle.com/iaas/Content/GSG/Tasks/addingusers.htm). For a list of typical policies you may want to use, see[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).
- A key pair used for signing API requests, with the public key uploaded to Oracle. Only the user calling the API should possess the private key.
Note  
  
For more information, see[Configuring the SDK](https://docs.oracle.com/iaas/tools/python/latest/installation.html#configuring-the-sdk).
- Collect the Messages endpoint and OCID of a stream. For steps to get details for a stream, see[Getting Details for a Stream](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/get-stream.htm). For the purposes of this quickstart, the stream should use a public endpoint and let Oracle manage encryption. Refer to[Creating a Stream](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/creatingstreamsandstreampools_create-stream.htm)and[Creating a Stream Pool](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/creating-stream-pools.htm)if you do not have an existing stream.
- Python 3.6 or later, with PIP installed and updated.
- Visual Studio Code (recommended) or any other integrated development environment (IDE).
- 

Install`oci-sdk`packages for Python using the following command:

```

```

Note  
  
We recommend that you use a Python virtual environment when installing`oci`. See[Downloading and Installing the SDK](https://docs.oracle.com/iaas/tools/python/latest/installation.html#downloading-and-installing-the-sdk)for more information.
- Ensure that you have a valid[SDK configuration file](https://docs.oracle.com/iaas/Content/API/Concepts/sdkconfig.htm). For production environments, you should use[instance principal authorization](https://docs.oracle.com/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm).

## Producing Messages

- Open your favorite editor, such as Visual Studio Code, from the directory`wd`. You should already have`oci-sdk`packages for Python installed for your current Python environment after you've met the[prerequisites](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-quickstart-oci-sdk-for-python.htm#prerequisites-python).
- 

Create a file named`Producer.py`in the`wd`directory with following code. Replace values of variables`ociConfigFilePath`,`ociProfileName`,`ociStreamOcid`, and`ociMessageEndpoint`in the following code snippet with the values applicable for your tenancy.

```

```

- 

From the`wd`directory, run the following command:

```

```

- [Show latest messages sent to the stream](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/show-recent-messages.htm)to see the latest messages sent to the stream to verify that production was successful.

## Consuming Messages

- First, ensure that the stream you want to consume messages from contains messages. You could[use the Console to produce a test message](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/publishingmessages.htm#console), or use the stream and messages we[created in this quickstart](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-quickstart-oci-sdk-for-python.htm#produce-messages-python).
- Open your favorite editor, such as Visual Studio Code, from the directory`wd`. You should already have`oci-sdk`packages for Python installed for your current Python environment after ensuring you have the[prerequisites](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-quickstart-oci-sdk-for-python.htm#prerequisites-python).
- 

Create a file named`Consumer.py`in directory`wd`with following code. Replace values of variables`ociConfigFilePath`,`ociProfileName`,`ociStreamOcid`, and`ociMessageEndpoint`in the following code snippet with the values applicable for your tenancy.

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
- [OCI SDK for Python on GitHub](https://github.com/oracle/oci-python-sdk)
- [OCI SDK for Python Streaming examples](https://github.com/oracle/oci-python-sdk/blob/master/examples/stream_example.py)
