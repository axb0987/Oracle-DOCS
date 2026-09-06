# Add Connections
- Source: https://docs.oracle.com/iaas/database-management/doc/add-connections-extdbsystem.html
- Fetched: 2026-09-05 19:00 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/database-management/doc/add-connections-extdbsystem.html#dcoc-content-body)

# Add Connections

You must add connections to the External Database System components to enable Database Management to monitor the component.

Connections can be added to the components in the External Database System during the discovery process or later from the details pages of the components. The topics in this section provide information on how to add connections to components (other than databases) as part of the External Database System discovery process. The process to add connections to databases in the Database Management interface is the same as in the External Database service. For information, see[Create a Connection to an External Database](https://docs.oracle.com/iaas/external-database/doc/create-connection-external-database.html).

### Add Connections to Clusters

- On the Managed databases page, click Actions , click Discover Database System , select External Database System , and then click Launch wizard to start the External Database System discovery process. For information, see[Discover External Database Systems](https://docs.oracle.com/iaas/database-management/doc/discover-external-database-systems.html#GUID-CC5468E7-19AB-4B9E-B115-E67B0A035F0E).
- In the Select components section of the Discover External Database System wizard, scroll down to the Cluster section, click the Actions icon ( ) for a cluster node, and click Add connection .
- In the Add connection panel:

- Provide connector information:
- Connector display name : Optionally, edit the default name assigned to the connector to easily identify the connector.
- Agent : Select the Management Agent installed on the respective cluster node to establish a connection with the cluster.
Note  
  
To connect to and monitor clusters, the`mgmt_agent`user must be available on all the nodes in the cluster. For more information, see[Perform Prerequisite Tasks](https://docs.oracle.com/iaas/database-management/doc/perform-prerequisite-tasks-extdbsystem.html#GUID-FF1437E6-1009-4711-B949-F42E34991020).
- Click Add connection .
If there are more cluster nodes, then follow the same process to add connections.

### Add Connections to ASM

- On the Managed databases page, click Actions , click Discover Database System , select External Database System , and then click Launch wizard to start the External Database System discovery process. For information, see[Discover External Database Systems](https://docs.oracle.com/iaas/database-management/doc/discover-external-database-systems.html#GUID-CC5468E7-19AB-4B9E-B115-E67B0A035F0E).
- In the Select components section of the Discover External Database System wizard, scroll down to the ASM section, and click the Actions icon ( ), and click Add connection .
- In the Add connection panel:

- Provide connector information:
- Connector display name : Optionally, edit the default name assigned to the connector to easily identify the connector.
- Agent : Select the Management Agent to establish a connection with ASM.
- Specify connection string information:
- ASM hostname : Specify the host where the ASM instance is installed. Note that you can add comma-separated host names of the ASM instances.
- Port : Specify the port number.
- ASM service : Specify the service name.
- Protocol : Select the TCP protocol to connect to ASM.
- Specify the credentials required to connect to ASM in the External Database System:
- User name : Enter the user name to connect to ASM. It's recommended that you use the default`ASMSNMP`user or any user with both the`SYSASM`and`SYSDBA`privileges.
- Password secret : Select the Oracle Cloud Infrastructure Vault service secret that contains the ASM user password. For information on how to save the ASM user password as a secret in the Vault service, see[Perform Prerequisite Tasks](https://docs.oracle.com/iaas/database-management/doc/perform-prerequisite-tasks-extdbsystem.html#GUID-FF1437E6-1009-4711-B949-F42E34991020).
- Role : Select the role from the available options.
- Click Add connection .

- [Add Connections](https://docs.oracle.com/iaas/database-management/doc/add-connections-extdbsystem.html#DBMSD-GUID-23540874-6032-49A1-8240-13671CCD99FF)
- [Add Connections to Clusters](https://docs.oracle.com/iaas/database-management/doc/add-connections-extdbsystem.html#DBMSD-GUID-4D84EFC9-5CBF-4A7E-9458-F4BD2E00236F)
- [Add Connections to ASM](https://docs.oracle.com/iaas/database-management/doc/add-connections-extdbsystem.html#DBMSD-GUID-2602A4EE-2426-4704-A160-F4E87F1A5CB8)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
