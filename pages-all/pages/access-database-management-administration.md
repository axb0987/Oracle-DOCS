# Access Database Management Administration
- Source: https://docs.oracle.com/iaas/database-management/doc/access-database-management-administration.html
- Fetched: 2026-09-05 18:58 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/database-management/doc/access-database-management-administration.html#dcoc-content-body)

# Access Database Management Administration

On obtaining the required permissions and completing the prerequisite tasks, you can access Database Management Administration and use the Managed databases page to perform the tasks pertaining to External Databases and External Database Systems.

To access the Managed databases page for the External Database ecosystem:
- Sign in to the Oracle Cloud Infrastructure console.
- Open the navigation menu, click Observability &amp; Management . Under Database Management , click Administration .
- Ensure that the correct compartment is selected in the Compartment applied filter.
- Click inside the Search by database display name field, select Deployment type , select External , and then click Apply filter .

On the Managed databases page for the External Database ecosystem, you can:
- View the External Databases in the compartment, which were registered either in the Oracle Cloud Infrastructure External Database service or in Database Management. By default, the following information pertaining to External Databases is displayed:
- Database name : The name of the database.
- Type : The type of database that indicates if the database is a single instance or RAC database, and if it's a CDB, PDB, or non-CDB.
- Deployment type : The deployment type of the database.
- Diagnostics &amp; Management : The enablement status for the Diagnostics &amp; Management feature set.
- Management status : The management or license option of the database.
- Connection status : The connection status of the database.
- Database System : The link to the associated Database System details page, if the External Database System is discovered.
- Exadata : The link to the Exadata infrastructure details page, if the Exadata Infrastructure associated with the External Database System is discovered.

On the Managed databases page for External Databases, you can:
- Click inside the Search by database display name field to filter the External Databases listed on the Managed databases page. You can select a filter such as Database name , Type , and Deployment type , specify the filter value, and then click Apply filter .
- Click Named Credentials under Administration to create a named credential or view the named credentials in the compartment. Named credentials are resources that contain user authentication information for Oracle Databases, namely, the database user name and the Oracle Cloud Infrastructure Vault service secret that contains the database user password. In the context of the External Database ecosystem, named credentials can be created and used to access the databases in the External Database System and perform Database Management tasks. For information on named credentials, see[Create and Manage Named Credentials](https://docs.oracle.com/iaas/database-management/doc/create-and-manage-named-credentials.html).
- Click Actions and click one of the following options:
- Discover Database System : Click to discover and create an External Database System and add connections to the components. For information, see[Discover and Connect to External Database Systems](https://docs.oracle.com/iaas/database-management/doc/discover-connect-external-database-systems.html#GUID-D896F279-05CA-4CC6-A7ED-0738709814EB).
- Discover Exadata infrastructure : Click to discover the Exadata Infrastructure associated with a discovered External Database System and add connections to storage servers. For information, see[Discover and Connect to Exadata Infrastructure](https://docs.oracle.com/iaas/database-management/doc/discover-connect-exadata-infrastructure.html#GUID-CAA7E6D3-8991-45B5-9E2B-65B24B2F52A5).
- Register external database : Click to register an External Database. On registering the External Database, you can click the Actions icon ( ) for an External Database, and:
- Click Connect to add a connection to the External Database.
- Click View features to enable Database Management features.

The following table lists tasks pertaining to External Databases, including registering and connecting to External Databases and enabling Database Management features, with links to more information.

Task More Information
Register an External Database For information, see[Create a Handle for an External Database](https://docs.oracle.com/iaas/external-database/doc/create-handle-external-database.html).
Create a connection to an External Database For information, see[Create a Connection to an External Database](https://docs.oracle.com/iaas/external-database/doc/create-connection-external-database.html).
Enable Diagnostics &amp; Management for an External Database For information, see[Enable Diagnostics &amp; Management for External Databases](https://docs.oracle.com/iaas/database-management/doc/enable-database-management-external-databases.html).

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
