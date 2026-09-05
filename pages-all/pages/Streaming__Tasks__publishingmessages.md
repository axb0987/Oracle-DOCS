# Publishing a Test Message to a Stream
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/publishingmessages.htm
- Fetched: 2026-09-05 03:06 CDT

# Publishing a Test Message to a Stream

Emit (publish) a test message to a stream in the Streaming service to ensure the stream is working.

Use the CLI, API, or an SDK to populate a stream. For requirements and recommendations for publishing messages, see[Publishing Messages](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/publishing.htm). To publish messages using an SDK, see[Developer Guide to Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/developing.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/publishingmessages.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/publishingmessages.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/publishingmessages.htm#)
- 

- On the Streams list page, select the stream that you want to work with. If you need help finding the list page or the stream, see[Listing Streams](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Tasks/listing-streams.htm).
- On the details page, select Produce test message .
- On the Produce test message panel, in the Data box, enter the text-only message to publish.
- Select Produce .
- 

Use the[oci streaming stream message put](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/streaming/stream/message/put.html)command and required parameters to publish a test message to a stream:

```

```

Tip  
  
Provide input for`--messages`as valid formatted JSON. See[Passing Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#Managing_CLI_Input_and_Output)and[Using a JSON File for Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON)for information about JSON formatting.

For example,`file.txt`contains the properly formatted JSON. Its values are Base64-encoded:
```

```

The`--messages`parameter takes the file as its value:
```

```

- 

Run the[PutMessages](https://docs.oracle.com/iaas/api/#/en/streaming/latest/Message/PutMessages)
