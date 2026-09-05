# Setting Up Kerberos Authentication
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos-oci-setup.htm
- Fetched: 2026-09-05 02:03 CDT

# Setting Up Kerberos Authentication

Kerberos information is configured on a per-mount target basis using the following steps.

Note  
  
These steps assume that you're using LDAP authorization to enable per-user Kerberos authentication. Anonymous access with Kerberos authentication is possible without the LDAP requirements and corresponding steps. For more information, see[LDAP Lookups and Anonymous Access](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm#overview__ldap-anon).

- Ensure that you have the LDAP and Kerberos infrastructure required. See[Prerequisites](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm#prerequisites)for more information.
- If the default VCN resolver isn't used, add forward and reverse name records to the customer-managed DNS server.
- Add the mount target principal to the KDC and extract a binary keytab from KDC. The steps to extract a keytab differ based on the type of KDC in use (Linux based or Active Directory).
- Convert the binary Kerberos keytab to Base64, then use it to create a secret in OCI Vault. Ensure that you select Base64 as the format of the secret when you paste in the converted keytab. For more information, see[Overview of Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm).
- Upload the LDAP password to OCI Vault as a secret in plain-text format. For more information, see[Overview of Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm).
- Add the[required IAM policies](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm#kerberos-permissions).
- [Create two outbound connectors](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-outbound-connector.htm)to contact the LDAP server.
Note  
  
Using LDAP for authorization requires at least one outbound connector. A second outbound connector can be used as a backup or for failover. See[LDAP Lookups and Anonymous Access](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm#overview__ldap-anon)for details on how File Storage responds when it can't reach an LDAP server.
- [Add LDAP configuration details to a mount target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap-setup.htm#updating-mts-for-ldap).
- [Add Kerberos authentication details to the same mount target and validate the keytab](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos-oci-setup.htm#enable-kerberos).
Note  
  
Kerberos configuration isn't shared across mount targets.
- 
Verify that the mount target used for Kerberos authentication has:
- A fully qualified domain name (FQDN) that matches the instance of the Kerberos keytab principal. For example:`nfs/<FQDN_of_mount_target>@<REALM>`.
Note  
  
When the default Internet and VCN Resolver, the File Storage service constructs a FQDN by combining the mount target's hostname with the FQDN of the subnet the mount target is located in. For more information, see[Managing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm).
- A FQDN that was added to the DNS server with both forward and reverse lookup.
- [Create](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/creatingfilesystems.htm)or[update](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingfilesystems.htm)a file system using the LDAP and Kerberos-enabled mount target.
- Add a Kerberos-enabled[export](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions.htm)to the mount target. See[Use Kerberos for Authentication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions.htm#kerberos-scenario)for an example.
- [Mount the file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingfilesystems.htm). For more information, see[Mounting Kerberos-enabled File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos-oci-setup-mounting.htm).
Note  
  
Use the FQDN of the mount target instead of the IP address.

## Enable Kerberos Authentication for a Mount Target

Configure Kerberos authentication for a File Storage mount target.

Note  
  
When you update an existing mount target to use Kerberos, it can take some time for File Storage to fully reflect the updates.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos-oci-setup.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos-oci-setup.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos-oci-setup.htm#)
- 

- Open the navigation menu and select Storage . Under File Storage , select Mount Targets .
- In the List scope section, under Compartment , select a compartment.
- Find the mount target that you're interested in, click the Actions menu (three dots) , and then click View details .
- Click the NFS tab to view or edit the existing NFS settings for the mount target.
- Next to Kerberos, click Manage .
- 

In the Manage Kerberos window, provide the following details:
- Kerberos realm : Enter the Kerberos realm that this mount target joins.
- In Keytab information section, provide the following details:
- Select the Vault that contains the keytab secret you want to use.
- Select the Keytab Secret .
- Select the Current keytab Secret version and the Backup keytab Secret version .
Caution  
  
Be sure to back up your vaults and keys. Deleting a vault and key otherwise means losing the ability to decrypt any resource or data that the key was used to encrypt. For more information, see[Backing Up and Restoring Vaults and Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys.htm).
- 

Click Validate keytab before enabling Kerberos to inspect the contents of the keytab.
Caution  
  
An improperly configured keytab can cause NFS clients to lose access to file systems.
- Enable Kerberos : Enable this option to use Kerberos. See[Using Kerberos Authentication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm)for more information.
- Click Save .
- 

Use the[`oci fs mount-target create`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/create.html)command with the`--kerberos`,`--idmap-type`, and`--ldap-idmap`options to create a mount target and provide Kerberos and LDAP details.

```

```

Use the[`oci fs mount-target update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/update.html)command with the`--kerberos`,`--idmap-type`, and`--ldap-idmap`options to update an existing mount target with Kerberos and LDAP details.

```

```

An example`krb.json`file follows:
```

```

An example`ldap.json`file follows:
```

```

Use the`oci fs mount-target validate-key-tabs`command to test the Kerberos keytab that the outbound connector associated with the mount target uses.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use[CreateMountTarget](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/CreateMountTarget)or[UpdateMountTarget](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/UpdateMountTarget)with the`kerberos`,`idMapType`, and`ldapIdmap`options to create or update a mount target with LDAP and Kerberos details.

Use ValidateKeyTabs to validate the Kerberos keytab associated with the mount target.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
