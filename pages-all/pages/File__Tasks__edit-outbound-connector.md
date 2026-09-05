# Editing an Outbound Connector
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-outbound-connector.htm
- Fetched: 2026-09-05 02:03 CDT

# Editing an Outbound Connector

Outbound connectors can't be changed after they're created. You can only rename or add tags to an outbound connector that already exists.

If you need to change the outbound connector that a mount target uses, see[Creating an Outbound Connector](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-outbound-connector.htm)and[Rotating Outbound Connectors](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/rotate-outbound-connector.htm).

When you edit an outbound connector, you can also update its tags. For instructions, see[Updating a Tag for a Single Resource](https://docs.oracle.com/iaas/Content/General/Tasks/resourcetags-updating-tags-single-resource.htm). For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-outbound-connector.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-outbound-connector.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-outbound-connector.htm#)
- 

- On the Outbound Connectors list page, select the outbound connector that you want to work with. If you need help finding the list page or the outbound connector, see[Listing Outbound Connectors](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-outbound-connectors.htm).
- To rename the outbound connector, select Rename and change the name. Avoid entering confidential information.
- To manage for the outbound connector, select Tags . Next to a tag, select Menu (three dots), and then select Edit .

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Update .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/outbound-connector/update.html)oci fs outbound-connector update`command and required parameters to edit an outbound connector.

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Use[UpdateOutboundConnector](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/OutboundConnector/UpdateOutboundConnector)to edit an outbound connector.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
