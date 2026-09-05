# Disable Kerberos Authentication for a Mount Target
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/disable-kerberos-on-mt.htm
- Fetched: 2026-09-05 02:03 CDT

# Disable Kerberos Authentication for a Mount Target

Disable Kerberos authentication for a mount target.

Note  
  
If you delete a Kerberos keytab from Vault, but don't disable the mount target's ability to use Kerberos, it can take some time for File Storage to fully reflect the update.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/disable-kerberos-on-mt.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/disable-kerberos-on-mt.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/disable-kerberos-on-mt.htm#)
- 

- Open the navigation menu and select Storage . Under File Storage , select Mount Targets .
- Select a compartment you have permissions to work in.
- Select the mount target that you're interested in, select the Actions menu (three dots) , and then select View details .
- Select the Actions menu, then select Manage Kerberos .
- In the Manage Kerberos window, turn off Enable Kerberos immediately disable Kerberos authentication for the mount target.
- Optionally, delete the Kerberos keytab from Vault.
- Select Update .
- 

Use the[`oci fs mount-target update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/update.html)command with the`--kerberos`option to update an existing mount target's with Kerberos details and specify that Kerberos is disabled.

```

```

An example`krb.json`file follows:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use[UpdateMountTarget](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/UpdateMountTarget)with the`kerberos`option to update a mount target's Kerberos details.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
