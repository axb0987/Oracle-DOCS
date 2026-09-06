# Add Connections to Storage Servers
- Source: https://docs.oracle.com/iaas/database-management/doc/add-connections-storage-servers.html
- Fetched: 2026-09-05 19:00 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/database-management/doc/add-connections-storage-servers.html#dcoc-content-body)

# Add Connections to Storage Servers

You must add connections to the storage servers in the Exadata Infrastructure to monitor them.
Connections can be added to the storage servers during the discovery process or later from the Storage Server details page if you've deleted a connector and want to add a new connection. This topic provides information on how to add connections to storage servers as part of the Exadata Infrastructure discovery process. For information on how to add a connection when the previous connector was deleted for a single storage server, see[Monitor a Single Storage Server](https://docs.oracle.com/iaas/database-management/doc/monitor-single-storage-server.html#GUID-1EA66E09-8174-4AD1-9D14-483F4668C897).

To add a connection to storage servers during the Exadata Infrastructure discover process:
- On the Managed databases page, start the Exadata Infrastructure discovery process. For information, see[Discover External Exadata Infrastructure](https://docs.oracle.com/iaas/database-management/doc/discover-external-exadata-infrastructure.html#GUID-BAD287BE-435B-4B07-BF8A-F1903FF00F1B)or[Discover Oracle Cloud Exadata Infrastructure](https://docs.oracle.com/iaas/database-management/doc/discover-oracle-cloud-exadata-infrastructure.html#GUID-42542417-90F1-48A0-ACF6-66351FC1B0EB).
- On the Add connectors page of the Discover Exadata infrastructure panel, scroll down to the Storage Servers section, and click Configure connector in the Connector column.

You also have the option of clicking Configure all connectors in the Storage Servers section to add a connection to all storage servers. Note that the Configure all connectors option is only available if adding connections to all storage servers during the discovery process, and assuming that the storage servers are going to be monitored by the same Management Agent and the storage servers have the same user account and password.
- In the Configure connector panel:

- Specify the connector details and the REST endpoint to monitor the storage server:
- Connector display name : Optionally, edit the default name assigned to the connector to easily identify the connector.
- Storage Server REST endpoint URL : Enter the storage server REST endpoint URL. For example,`https://cellnode:443/MS/RESTService`.

If you're adding connections to all storage servers using the Configure all connectors option, you can use the`<server_name>`or`<server_ip>`placeholders to specify a custom endpoint URL, for example,`https://<server_name>.example.com/MS/RESTService`. When the connector is added for each storage server, the server name or IP address will replace the placeholder. If the placeholders are not explicitly specified, then the default behavior is to append the storage server name as a path segment to the end of the endpoint URL, for example,`https://cellnode.example.com/MS/RESTService/<server_name>`.

The`cellnode`could be the storage server host name such as`cellserver01`, a fully qualified name such as`cellserver01.example.com`, or an IP address such as`10.1.101.2`. The`cellnode`should be accessible from the monitoring Management Agent's host without relying on a proxy. It should also match the URL from which the SSL certificate required to confirm the identity of the storage servers in the Exadata Infrastructure to the Management Agent was downloaded. Note that the SSL certificate downloaded from the`cellserver01.example.com`URL may not work with the`https://cellserver01//MS/RESTService`endpoint. For information on how to test the SSL certificate against the storage server REST endpoint in the agent host, see[Ensure the availability of the storage server's SSL certificate in the Management Agent truststore](https://docs.oracle.com/iaas/database-management/doc/access-storage-servers.html#GUID-F55FDCD2-595F-4D2C-A8D8-B07D4E1687F0__SECTION_HRT_HTP_WWB).
- Monitoring agent : Select the Management Agent to establish a connection with the storage server. You can use the same Management Agent used to discover the DB system or any other Management Agent that has direct access to the storage server REST endpoint. If the Management Agent resides in a different compartment, click Change compartment and select the other compartment.
- Specify the credentials required to connect to the storage server:
- Admin username : Enter the storage administrator user name. It's recommended that you use the out-of-the-box`cellmonitor`ExaCLI user, however, you also have the option of creating a new ExaCLI administrator user. For more information, see[Ensure the availability of an ExaCLI user to access and monitor storage servers](https://docs.oracle.com/iaas/database-management/doc/access-storage-servers.html#GUID-F55FDCD2-595F-4D2C-A8D8-B07D4E1687F0__SECTION_VHB_HTP_WWB).
- Admin password : Enter the storage administrator password.
- HTTPS truststore type : Select the truststore type: JKS or BCFKS .
- Truststore location : Enter the truststore location. The truststore must have the SSL certificates downloaded from the storage servers. For information, see[Ensure the availability of the storage server's SSL certificate in the Management Agent truststore](https://docs.oracle.com/iaas/database-management/doc/access-storage-servers.html#GUID-F55FDCD2-595F-4D2C-A8D8-B07D4E1687F0__SECTION_HRT_HTP_WWB).
- Truststore password Optional : Optionally, enter the truststore password.
- Click Configure connector .
The name of the connector is displayed in the Connector column in the Storage Servers section.

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
