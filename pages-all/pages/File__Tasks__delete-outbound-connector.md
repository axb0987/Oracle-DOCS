# Deleting an Outbound Connector
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-outbound-connector.htm
- Fetched: 2026-09-05 02:03 CDT

# Deleting an Outbound Connector

Delete an outbound connector.

You can't delete an outbound connector that's used by a mount target.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-outbound-connector.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-outbound-connector.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-outbound-connector.htm#)
- 

- On the Outbound Connectors list page, find the outbound connector that you want to work with. If you need help finding the list page or the outbound connector, see[Listing Outbound Connectors](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-outbound-connectors.htm).
- Select the connector you want to delete.
- On the details page, from Actions menu, select Delete .
- When prompted, confirm the deletion.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/outbound-connector/delete.html)oci fs outbound-connector delete`command and required parameters to delete an outbound connector.

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Use[DeleteOutboundConnector](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/OutboundConnector/DeleteOutboundConnector)to delete an outbound connector.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
