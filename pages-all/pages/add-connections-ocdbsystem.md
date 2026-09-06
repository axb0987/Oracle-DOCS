# Add Connections
- Source: https://docs.oracle.com/iaas/database-management/doc/add-connections-ocdbsystem.html
- Fetched: 2026-09-05 19:00 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/database-management/doc/add-connections-ocdbsystem.html#dcoc-content-body)

# Add Connections

You must add connections to the Oracle Cloud Database System components to enable Database Management to monitor the component.

Connections can be added to the components in the Oracle Cloud Database System during the discovery process or later from the details pages of the components. The topics in this section provide information on how to add connections to components (other than databases) as part of the Oracle Cloud Database System discovery process.

### Add Connections to Clusters

- On the Managed databases page, select the Oracle Database cloud solution in the Deployment type filter on the left pane, and click Discover Cloud Database System to start the Oracle Cloud Database System discovery process. For information, see[Discover Oracle Cloud Database Systems](https://docs.oracle.com/iaas/database-management/doc/discover-oracle-cloud-database-systems.html#GUID-3BE646F2-2954-4718-B5AE-667B17B7DFFE).
- On the Select components page of the Discover Cloud Database System panel, scroll down to the Cluster section, and click Add connection in the Connection column.
- In the Add connection panel:

- Provide connector information:
- Connector display name : Optionally, edit the default name assigned to the connector to easily identify the connector.
- Agent : Select the Management Agent installed on the respective cluster node to establish a connection with the cluster.
Note  
  
To connect to and monitor clusters, the`mgmt_agent`user must be available on all the nodes in the cluster. For more information, see[Perform Prerequisite Tasks](https://docs.oracle.com/iaas/database-management/doc/perform-prerequisite-tasks-ocdbsystem.html#GUID-7432B644-ECC9-49F0-850B-1FCE9122B0EA).
- Click Add connection .
If there are more cluster nodes, then follow the same process to add connections.

### Add Connections to ASM

- On the Managed databases page, select the Oracle Database cloud solution in the Deployment type filter on the left pane, and click Discover Cloud Database System to start the Oracle Cloud Database System discovery process. For information, see[Discover Oracle Cloud Database Systems](https://docs.oracle.com/iaas/database-management/doc/discover-oracle-cloud-database-systems.html#GUID-3BE646F2-2954-4718-B5AE-667B17B7DFFE).
- On the Select components page of the Discover Cloud Database System panel, scroll down to the ASM section, and click Add connection in the Connection column.
- In the Add connection panel:

- Provide connector information:
- Connector display name : Optionally, edit the default name assigned to the connector to easily identify the connector.
- Agent : Select the Management Agent to establish a connection with ASM.
- Specify connection string information:
- ASM hostname : Specify the host where the ASM instance is installed. Note that you can add comma-separated host names of the ASM instances.
- Port : Specify the port number.
- ASM service : Specify the service name.
- Protocol : Select the TCP protocol to connect to ASM.
- Specify the credentials required to connect to ASM in the Oracle Cloud Database System:
- User name : Enter the user name to connect to ASM. It's recommended that you use the default`ASMSNMP`user or any user with both the`SYSASM`and`SYSDBA`privileges.
- ASM user password secret : Select the Oracle Cloud Infrastructure Vault service secret that contains the ASM user password. If an existing secret with the ASM user password is not available, then select Create new secret... in the drop-down list. The Create password secret panel is displayed and you can create a new secret. For information on how to save the ASM user password as a secret in the Vault service, see[Perform Prerequisite Tasks](https://docs.oracle.com/iaas/database-management/doc/perform-prerequisite-tasks-ocdbsystem.html#GUID-7432B644-ECC9-49F0-850B-1FCE9122B0EA).
- Role : Select the role from the available options.
- Click Add connection .

- [Add Connections](https://docs.oracle.com/iaas/database-management/doc/add-connections-ocdbsystem.html#DBMSD-GUID-59D550A0-23D2-4585-BA80-EC503710268B)
- [Add Connections to Clusters](https://docs.oracle.com/iaas/database-management/doc/add-connections-ocdbsystem.html#DBMSD-GUID-9C19EFB1-2288-42AB-8C36-243A4DFAA466)
- [Add Connections to ASM](https://docs.oracle.com/iaas/database-management/doc/add-connections-ocdbsystem.html#DBMSD-GUID-BB3BB07C-A34A-4192-9128-EFC5FF3C72FF)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
