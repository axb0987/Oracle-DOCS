# Managing a Stream Pool's Security Attributes
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/manage-security-attributes.htm
- Fetched: 2026-09-05 03:06 CDT

# Managing a Stream Pool's Security Attributes

Add, update, and remove security attributes added to a stream pool.

You can use Zero Trust Packet Routing (ZPR) along with or in place of network security groups to manage network access to OCI resources . To do this, define ZPR policies that govern how resources communicate with each other, and then add security attributes to those resources. For more information, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm).

ZPR security attributes can be added only to stream pools with a private endpoint.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/manage-security-attributes.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/manage-security-attributes.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/manage-security-attributes.htm#)
- 

- On the Stream pool list page, find the stream pool that you want to work with. If you need help finding the list page or the stream pool, see[Listing Stream Pools](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Tasks/list-stream-pools.htm).
- From the Actions menu (three dots) for the stream pool, select Manage security attributes .
- Update the configuration of any existing security attribute listed.
You can also select the Add security attribute button to add another security attribute (to a maximum of three).
- To remove a security attribute, select the Delete Row button.
- Select Save .
The security attributes that you added or updated are viewable on the Security tab of the stream pool's[details](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/get-stream-pool.htm#top)page.
- 

Use the`--security-attribute`option when running the[oci streaming admin stream-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/streaming/admin/stream-pool/update.html)command to add Zero Trust Packet Routing (ZPR) security attributes when you're updating a stream pool:

```

```

Tip  
  
Provide input for`--custom-encryption-key-details`,`--private-endpoint-details`, and`--kafka-settings`as valid formatted JSON. See[Passing Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#Managing_CLI_Input_and_Output)and[Using a JSON File for Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON)for information about JSON formatting.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateStreamPool](https://docs.oracle.com/iaas/api/#/en/streaming/latest/StreamPool/UpdateStreamPool)operation to update a stream pool. Include the`securityAttribute`
