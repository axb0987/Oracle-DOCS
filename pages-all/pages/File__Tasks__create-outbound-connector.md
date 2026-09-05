# Creating an Outbound Connector
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-outbound-connector.htm
- Fetched: 2026-09-05 02:03 CDT

# Creating an Outbound Connector

Create an outbound connector.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-outbound-connector.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-outbound-connector.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-outbound-connector.htm#)
- 

- On the Outbound Connectors list page, select Create outbound connector . If you need help finding the list page, see[Listing Outbound Connectors](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-outbound-connectors.htm)
- In the Create Outbound Connector panel, provide the following details:

- Outbound connector name: The File Storage service creates a default name using`OutboundConnector-YYYYMMDD-HHMM-SS`. Optionally, change the default name for the connector. Avoid entering confidential information.
- Availability domain : The first availability domain selected is used as default.
- Create in compartment : Specify the compartment you want to create the connector in.
- Connector type : Only the LDAP Bind connector type is supported.
- Server DNS name and Port : Enter the DNS name and port of the endpoint to be used to connect using the LDAP bind account.
- Bind distinguished name : Enter the LDAP distinguished name of the bind account.
- Vault compartment and Vault : Select compartment and vault that contains the LDAP secret that you want to use.
- LDAP secret compartment and LDAP secret : Select the compartment and secret. For more information about encryption, see[Overview of Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm).
Caution  
  
Be sure to back up vaults and keys. Deleting a vault and key otherwise means losing the ability to decrypt any resource or data that the key was used to encrypt. For more information, see[Backing Up and Restoring Vaults and Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys.htm).
- To tag the outbound connector, select Add tag .

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Optionally, if your LDAP server uses a certificate that isn't issued by a public certificate authority (CA) (for example, a private CA or self-signed certificate), and you have saved the certificate in OCI Vault as a plain text[secret](https://docs.oracle.com/iaas/Content/secret-management/Tasks/create-secret.htm), turn on Enable trusted certificate and enter these details:

- Trusted certificate secret : Select the secret that contains the trusted certificate (root CA and, if required, the intermediate chain). The values available are fetched from the Vault you selected earlier.
- Trusted certificate secret version : Select the version to use.

Note  
  
After you create the outbound connector, you can't edit the trusted certificate settings (Trusted certificate secret or version) on that outbound connector. To use a different trusted certificate, create a new outbound connector.
- In the Resource locks section, select a lock level for the resource:

- No Lock : No restrictions.
- Delete : Prevents the resource from being deleted.
- Full : Prevents all modifications except reading the resource.
- To create the outbound connector, select Create .
- (Optional) To save the configuration as a Resource Manager stack, select Save as stack . For more information, see[Managing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/stacks.htm).
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/outbound-connector/create_ldap_bind_connector.html)oci fs outbound-connector create_ldap_bind_connector`command to create an outbound connector and specify LDAP connection details.

```

```

An example`endpoints.json`file follows:
```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Use[CreateOutboundConnector](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/OutboundConnector/CreateOutboundConnector)to create outbound connectors.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
