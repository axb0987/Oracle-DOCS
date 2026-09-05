# Rotating Outbound Connectors
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/rotate-outbound-connector.htm
- Fetched: 2026-09-05 02:04 CDT

# Rotating Outbound Connectors

Change the outbound connector that a mount target uses.

If a mount target already uses a functioning outbound connector, but you need to update the mount target to use a new outbound connector, we recommend using two outbound connectors when making the change. While it's not a requirement to use two outbound connectors, this strategy can prevent unnecessary outages.

When using two outbound connectors, the existing, functional outbound connector should be used as a backup in case the new outbound connector fails. Outbound Connector 1 , the new outbound connector, is used unless the bind operation fails, in which case Outbound Connector 2 , the previous outbound connector, is used.
Tip  
  
At any time, including after changing the outbound connector that a mount target uses, you can use[metrics](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Reference/filemetrics.htm)or[enable NFS Logs](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/logging.htm)for the mount target and search for "connection established" to verify connection details.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/rotate-outbound-connector.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/rotate-outbound-connector.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/rotate-outbound-connector.htm#)
- 

- On the Mount Targets list page, select the mount target that you want to work with. If you need help finding the list page or the mount target, see[Listing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-mount-targets.htm).
- Select NFS to view the existing NFS settings for the mount target.
- From the Actions menu, select Manage LDAP .
- 

In the Manage LDAP dialog box, update the outbound connectors as follows:
- Outbound connector 1 : Select the new outbound connector that the mount target will use to communicate with the LDAP server.
- Outbound connector 2 : Select the outbound connector that was previously used by this mount target to communicate with the LDAP server.
- Select Update .
- 

Use the[`fs mount-target update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/update.html)command and`--ldap-idmap`parameter to update the outbound connectors a mount target uses:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateMountTarget](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/UpdateMountTarget)operation and`ldapIdmap`along with`outboundConnector1Id`and`outboundConnector2Id`to update the outbound connector that a mount target uses.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
