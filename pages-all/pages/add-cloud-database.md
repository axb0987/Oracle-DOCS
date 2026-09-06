# Add a Cloud Service Database
- Source: https://docs.oracle.com/iaas/operations-insights/doc/add-cloud-database.html
- Fetched: 2026-09-05 19:00 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/operations-insights/doc/add-cloud-database.html#dcoc-content-body)

# Add a Cloud Service Database

With a private endpoint defined, you are ready to add a database that uses that endpoint. You can add databases from the Private endpoint details page or from the Database fleet administration page.

Before adding a database make sure you run the best practice script steps for Ops Insights databases outlined in[OCI : Best Practices / Troubleshooting Guide For Monitoring Databases In Ops Insights (Article ID KB78518)](https://support.oracle.com/support/?documentId=KB78518). It is strongly recommended the script be run every 6 months or if any databases are missing the storage or tablespace data.
Note  
  
If you are onboarding an Exadata Cloud Service database, see[Add an Exadata Database Service on Dedicated Infrastructure](https://docs.oracle.com/iaas/operations-insights/doc/add-exadata-cloud-service-system.html#GUID-48C2D091-1EFC-4C4A-B4F0-A912ECE87157).

If you are onboarding an Exadata Database Service on Cloud@Customer System, see[Add an Exadata Database Service on Cloud@Customer Service System](https://docs.oracle.com/iaas/operations-insights/doc/add-exadata-database-service-cloudcustomer-system.html#GUID-E8D9A6B0-2BC2-4EAE-B856-60476C4A86D9).

To onboard an Autonomous AI Database, see[Enable Autonomous AI Databases &amp; Full Feature Support](https://docs.oracle.com/iaas/operations-insights/doc/autonomous-database-full-feature-support.html#GUID-27B9ABB0-BBC4-4F7D-9EC7-40EF09F8726B).
- Open the navigation menu, click Observability &amp; Management , and then click Ops Insights .
- In the left pane, click Administration , and then click Database fleet .
The Database fleet administration page displays.
Note  
  
If deprecated policy statements are detected, Policy Advisor will display a banner requiring a policy update to the new CRISP format, to update click Update prerequisites polices . For information on deprecated policies, see[Service Principal Policy Removal](https://docs.oracle.com/iaas/operations-insights/doc/create-manage-policies-policy-advisor.html#GUID-0B0CFCC4-C5C0-449E-9BB0-795D5A308C23__GUID-343AAE7A-DB21-49A4-8FE0-C7D0570E8A5B).
- Click Add databases .
- Under Telemetry , select Cloud Infrastructure .
- In the Database type field, select the appropriate database type.
- Enter the required database selection information:
- Depending on the database type, select the required resource:
- For Bare metal, VM , select the Database system compartment and Database system .
- For Exadata Database Service on Dedicated Infrastructure , select the VM cluster compartment and VM cluster .
- Database home : Select a database home (system or cluster). All database homes in the database system are available in the drop-down selector.
- Database : Select a database from the database home. Databases are identified as either container or non-container . If you select a container database, you’ll be provided with the option of selecting all PDBs in the container or a single PDB.
Note  
  
When PDBs are added or removed from the DB System or VM Cluster, they will automatically be enabled or disabled:
- When performing disable, you should simply select the CDB and disable that target alone. That will disable all the PDBs as well.
- When performing a delete, you should simply select the CDB and disable that target alone. That will disable all the PDBs as well.
- If you previously disabled the CDB (and thus all the PDBs) and you want to re-enable Ops Insights, you should do so just on the CDB resource.
- Pluggable database (optional): When a container database is selected, you can select all PDBs or a single PDB.
- Service name : If no pluggable database was specified above, enter the service name corresponding to the container database (CDB). If one was specified, enter the service name corresponding to the specified pluggable database.
- Protocol :Select either TCP (default) or TCPS, depending on your configuration.
Note  
  
If Oracle Data Guard is enabled on a Bare Metal or Virtual Machine DB system after Database Management was enabled for it using the TCPS protocol, then TCPS will have to be reconfigured. Enabling Oracle Data Guard is causing TCPS configuration to be overwritten, and it's recommended that TCPS is configured on a Bare Metal or Virtual Machine DB system after enabling Oracle Data Guard.
- Port : Enter the port number, the default Oracle recommended TCP port is 1521.
- Database Wallet Secret (only for TCPS): When using a TCPS connection protocol a database wallet secret is required. Select the corresponding secret from the drop down list or click Create new wallet secret to create a new secret, the Create database wallet secret window appears.
In the Create database wallet secret panel, enter the following information:
- Name: Wallet secret name.
- Description (optional): Description for the wallet.
- Create in compartment: Database compartment where the wallet will be used.
- Vault: Vault within the compartment where the wallet will be stored.
- Encryption key: Encryption key to be used, select from drop down menu.
- Wallet format:
- For Java key store (JKS files) wallets the following is additionally required:
- Key store password: Enter the key store password for the Java key store wallet..
- Key store content: Drag the JKS file into the Ops Insights UI from a local machine.
- Trust store password: Enter the Trust store password required for the Java key store wallet.
- Trust store content: Drag the Trust score JKS file into the Ops Insights UI from a local machine.
- For PKCS#12 (P12 files) wallets the following is additionally required:
- Wallet password: Enter the required PKCD#12 wallet password.
- PKCS#12 wallet content: Drag the P12 file into the Ops Insights UI from a local machine.
- Certificate DN: Enter the certificate chain to be used.
- Specify credentials for the connection : Choose the credentials to be used for the connection, you use IAM or local database credentials. If no pluggable database (PDB) was specified above, enter the common user name for the CDB and all the PDBs and choose the secret corresponding to the password for the container database (CDB) user. If an individual PDB was specified, enter the user name and choose the corresponding secret for the specified pluggable database.
Note  
  
For Government realms, the password for the database user monitoring the Oracle Cloud Database must meet the following Federal Information Processing Standards (FIPS) requirements:
- Password length must be between 14 to 127 characters.
- Password must have at least two lowercase, two uppercase, two digits, and two special characters.

To create a new secret, click Create new secret .
Note  
  
In order to create a secret within OCI Vault, the encryption key being used must be set as follows: Click on Key Shape: Algorithm , and select: AES . Advanced Encryption Standard (AES) keys are symmetric keys that you can use to encrypt data at rest.

Key types, like RSA and ECDSA will not work for encrypting data at rest and are not recommended for Ops Insights operations. For more information see:[Creating a Master Encryption Key](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_create_a_new_key.htm).

To change the monitoring user or secret reference, you need to disable the database and then re-enable it (upon re-enable a pop-up displays to allow you to make changes).

For more information, see[Overview of Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm).
- Private endpoint information : Select a Private endpoint that has network access to this database via a VCN.

For information about creating private endpoints, see[Create a Private Endpoint](https://docs.oracle.com/iaas/operations-insights/doc/create-private-endpoint.html#GUID-9B6BCD6D-DEF8-4228-BF17-1C86F3C03404).
- Click Add databases . The newly added database will appear in the Database fleet administration page as well as the Private endpoint details page.

Change a TCPS Cloud Service Database to TCP

To change a TCPS-monitored cloud database to the default TCP connection, first disable the database by clicking the Actions menu for the database. Once disabled, click Edit connection details , select TCP as the protocol and update the port number. Once complete re-enable the database.

You can also change a TCP-monitored database to a TCPS connection by first clicking the Actions menu for the database and disabling the database. Once disabled, click Edit connection details , select TCPS as the protocol and update the port number. Once complete re-enable the database.

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
