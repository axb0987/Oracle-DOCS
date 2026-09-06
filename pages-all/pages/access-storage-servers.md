# Set Up Access to Storage Servers
- Source: https://docs.oracle.com/iaas/database-management/doc/access-storage-servers.html
- Fetched: 2026-09-05 18:58 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/database-management/doc/access-storage-servers.html#dcoc-content-body)

# Set Up Access to Storage Servers

You must perform certain tasks to set up access to the storage servers that you want to monitor using Database Management.

The following tasks must be performed before adding a connection to the storage server during the Exadata Infrastructure discovery process because the storage server user credentials and the SSL certificate imported to the Management Agent truststore are tested against the storage server. The connection to the storage server from the Management Agent can be added only after a test query is sent from the Management Agent to the storage server.
- 

[Ensure the availability of an ExaCLI user to access and monitor storage servers](https://docs.oracle.com/iaas/database-management/doc/access-storage-servers.html#GUID-F55FDCD2-595F-4D2C-A8D8-B07D4E1687F0__SECTION_VHB_HTP_WWB)
- 

[Ensure the availability of the storage server's SSL certificate in the Management Agent truststore](https://docs.oracle.com/iaas/database-management/doc/access-storage-servers.html#GUID-F55FDCD2-595F-4D2C-A8D8-B07D4E1687F0__SECTION_HRT_HTP_WWB)

Ensure the availability of an ExaCLI user to access and monitor storage servers

The Management Agent used to connect to the storage servers requires ExaCLI credentials to collect metrics through the storage server's REST endpoint.

For External Exadata Infrastructure

Recommended option : It's recommended that you use the out-of-the-box`cellmonitor`user.

Secondary option : You also have the option of creating a new ExaCLI administrative user. If you choose to create a new ExaCLI administrative user, then the new user must be created in all storage servers. Also, the new user must have`list`privileges on all objects. For example:
```

```

To create a new ExaCLI user across multiple storage servers using the`dcli`utility:
```

```

For information on how to:
- Create a new ExaCLI administrative user, see[Creating Users for Use with ExaCLI](https://docs.oracle.com/en/engineered-systems/exadata-database-machine/dbmmn/creating-users-use-exacli.html)in Oracle Exadata Database Machine Maintenance Guide .
- Use CellCLI utility, see[Using the CellCLI Utility](https://docs.oracle.com/en/engineered-systems/exadata-database-machine/sagug/using-cellcli-utility1.html)in Oracle Exadata System Software User's Guide .
- Use`dcli`utility, see[Using the dcli Utility](https://docs.oracle.com/en/engineered-systems/exadata-database-machine/sagug/using-dcli-utility1.html)in Oracle Exadata System Software User's Guide .

For Oracle Cloud Exadata Infrastructure deployed in ExaDB-D or ExaDB-C@C

Use the preconfigured ExaCLI user available with the service to access and monitor storage servers. The preconfigured user is`cloud_user_<clustername>`, where`<clustername>`is the name of your VM cluster. For more information, see:
- [Monitoring and Managing Exadata Storage Servers with ExaCLI](https://docs.oracle.com/iaas/exadatacloud/doc/ecs-using-excli.html)in Exadata Database Service on Dedicated Infrastructure documentation
- [Monitoring and Managing Exadata Storage Servers with ExaCLI](https://docs.oracle.com/iaas/exadata/doc/ecc-using-exacli.html)in Exadata Database Service on Cloud@Customer documentation

Ensure the availability of the storage server's SSL certificate in the Management Agent truststore

SSL certificates are required to verify the identity of storage servers in the Exadata Infrastructure to the Management Agent. Communication between the storage servers and the Management Agent uses`HTTPS`and requires the storage server's SSL certificates to be present in the Management Agent truststore.

Before importing the storage server's SSL certificate into the Management Agent truststore, it's recommended that you test the certificate against the storage server REST endpoint in the agent host:
```

```

For example:
```

```

You can import the storage server's SSL certificate into the Management Agent's default truststore within the agent installation directory or into a custom truststore located outside the agent installation directory.
- To use the Management Agent's default truststore:
- Download the certificate from the storage server:
```

```

- Import the certificate into the Management Agent truststore. The Management Agent truststore has an optional password, which is defined in the`CredentialWalletPassword`parameter of the agent installation response file. Here are the agent truststore locations:
- For a standalone Management Agent:
```

```

- For a Management Agent installed as an Oracle Cloud Agent (OCA) plug-in:
```

```

Note  
  
If you're using custom SSL certificates with a common domain name for all storage servers (where all storage servers use the same certificate), you only need to import the certificate once into the truststore, even if you're using the same Management Agent to monitor multiple storage servers.
- To use a custom truststore outside the agent directory:
- Download the certificate from the storage server:
```

```

- Import it into the custom truststore using the following command:
```

```

Note  
  
If you use a truststore located outside the agent installation directory, for example`/etc/pki/ca-trust/extracted/java/cacerts`, ensure that the`mgmt_agent`user has the required permissions to access the`cacerts`truststore file and its parent directories.

For more information, see[Import Certificates for Management Agent](https://docs.oracle.com/iaas/management-agents/doc/management-agents-administration-tasks.html#GUID-0CBD6BA7-7512-4318-9D3D-D6322CD120EF).

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
