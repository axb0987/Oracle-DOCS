# Locking an Outbound Connector
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-outbound-connector.htm
- Fetched: 2026-09-05 02:04 CDT

# Locking an Outbound Connector

Lock a File Storage outbound connector to prevent updates, moves, and deletions. Locks help protect resources against tampering.

Note  
  
A lock on an outbound connector resource doesn't prevent the outbound connector from being used by a mount target to communicate with the external server.

OCI resource locks include the following types:
- Delete lock : Prevents deletion of the locked resource.
- Full lock: Prevents update, move, and deletion of the locked resource.

You can only add or remove one lock type at a time, but both locks can be applied to a resource. For example, you might initially apply a delete lock, but choose to apply a full lock at a later time.

The user who places a lock is the lock owner. Any authorized user with lock privilege or users with global manage permission of the tenancy has the authorization to create and remove any lock in the tenancy. You can[override](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/override-lock-outbound-connector.htm)or[remove](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/unlock-outbound-connector.htm)locks.

## Required IAM Policy

To create locks, in addition to[permissions to manage the outbound connector](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managing-outbound-connectors.htm#required-policy), you need permissions to manage locks.

To lock an outbound connector, you must have`RESOURCE_LOCK_ADD`permissions.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-outbound-connector.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-outbound-connector.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-outbound-connector.htm#)
- 

- On the Outbound Connectors list page, select the outbound connector that you want to work with. If you need help finding the list page or the outbound connector, see[Listing Outbound Connectors](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-outbound-connectors.htm).
- On the details page, from the Actions menu, select Resource lock and then select Add .
- In the Add lock panel, select the type of resource lock you want:

- Delete : Prevents the resource from being deleted.
- Full : Prevents all modifications except reading the resource.
- ssss
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/outbound-connector/add.html)oci fs outbound-connector add`command and required parameters to lock an outbound connector:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[AddOutboundConnectorLock](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/OutboundConnector/AddOutboundConnectorLock)operation to lock an outbound connector.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
