# Unlocking an Outbound Connector
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-outbound-connector.htm
- Fetched: 2026-09-05 02:05 CDT

# Unlocking an Outbound Connector

Unlock a locked File Storage outbound connector to allow deletions (in the case of a delete lock) or updates, moves, and deletions (in the case of a full lock).

You can also[override outbound connector locks](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/override-lock-outbound-connector.htm).

## Required IAM Policy

To remove locks, in addition to[permissions to manage the outbound connector](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managing-outbound-connectors.htm#required-policy), you need permissions to manage locks.

To unlock an outbound connector, you must have`RESOURCE_LOCK_REMOVE`permissions.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-outbound-connector.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-outbound-connector.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-outbound-connector.htm#)
- 

- On the Outbound Connectors list page, select the outbound connector that you want to work with. If you need help finding the list page or the outbound connector, see[Listing Outbound Connectors](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-outbound-connectors.htm).
- On the details page, from the Actions menu, select Resource lock and then select Remove .
- When prompted, confirm the removal.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/outbound-connector/remove.html)oci fs outbound-connector remove`command and required parameters to unlock an outbound connector:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[RemoveOutboundConnectorLock](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/OutboundConnector/RemoveOutboundConnectorLock)operation to unlock an outbound connector.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
