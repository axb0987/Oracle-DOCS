# Setting Up LDAP for Authorization
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap-setup.htm
- Fetched: 2026-09-05 02:03 CDT

# Setting Up LDAP for Authorization

Learn how to set up LDAP for authorization with File Storage.

- Ensure that you have the LDAP infrastructure required and gathered the required information. See[Prerequisites](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap.htm#ldap-prereqs)for more information.
- Add the[required IAM policies](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap.htm#ldap-permissions).
- Upload the LDAP password to OCI Vault in plain-text format. For more information, see[Overview of Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm).
- [Create two outbound connectors](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-outbound-connector.htm)to contact the LDAP server.
Note  
  
Using LDAP for authorization requires at least one outbound connector. A second outbound connector can be used as a backup or for failover. See[Secondary Group Lookup](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap.htm#ldap-mapping)and[Caching](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap.htm#ldap-caching)for details on how File Storage responds when it can't reach an LDAP server.
- [Add LDAP communication details to a mount target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap-setup.htm#updating-mts-for-ldap).
- [Create](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/creatingfilesystems.htm)or[update](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingfilesystems.htm)a file system that uses the LDAP-enabled mount target.
- [Enable LDAP on the file system export](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/enable-ldap-export.htm).
- Set any optional[NFS export options](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions.htm).
- [Mount the file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingfilesystems.htm).

## Configuring LDAP for a Mount Target

Add LDAP information to a mount target for use in authorization.

Note  
  
When you update an existing mount target to use LDAP, it can take some time for the updates to be fully reflected throughout File Storage.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap-setup.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap-setup.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap-setup.htm#)
- 

- Open the navigation menu and select Storage . Under File Storage , select Mount Targets .
- Select a Compartment .
- Select the mount you're interested in.
- Select the Actions menu, and then select Manage LDAP t
- 

In the Manage LDAP window, provide the following details:
- Schema type : The schema type of the LDAP account.

The only allowed values are RFC2307 and RFC2307bis.
- Cache refresh interval in seconds : How often the mount target should contact the LDAP server for updates.
- Cache lifetime in seconds : How long cached entries may be used.
- Negative cache lifetime in seconds : How long to cache if ID mapping information is missing.
- Search base for users : All LDAP searches are recursive starting at this user.
- Search base for groups : All LDAP searches are recursive starting at this group.
- Outbound Connector 1 : The first connector to use to communicate with the LDAP server.
- Outbound Connector 2 : The second connector to use to communicate with the LDAP server.
- Enable LDAP : Turn on this option to require the mount target to use an LDAP server for[secondary group lookup](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap.htm#ldap-mapping). The file system's export must also have Use LDAP for group list enabled.
- Select Update .
- 

Use the[`oci fs mount-target create`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/create.html)command with the`--idmap-type`and`--ldap-idmap`options to create a mount target and provide LDAP details.

```

```

Use the[`oci fs mount-target update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/update.html)command with the`--idmap-type`and`--ldap-idmap`options to update an existing mount target with LDAP details.

```

```

An example`ldap.json`file follows:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use[CreateMountTarget](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/CreateMountTarget)or[UpdateMountTarget](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/UpdateMountTarget)with the`idMapType`and`ldapIdmap`options to create or update a mount target with LDAP details.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
