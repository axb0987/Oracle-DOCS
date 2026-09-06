# Add an Oracle Database to a Disaster Recovery Protection Group
- Source: https://docs.oracle.com/iaas/disaster-recovery/doc/add-database-protection-group.html
- Fetched: 2026-09-05 19:00 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/disaster-recovery/doc/add-database-protection-group.html#dcoc-content-body)

# Add an Oracle Database to a Disaster Recovery Protection Group

Learn how to add an Oracle Base Database Service, an Oracle Exadata Database Service on Dedicated Infrastructure, an Oracle Exadata Database Service on Exascale Infrastructure, an Oracle Exadata Database Service on Cloud@Customer to a Disaster Recovery (DR) Protection Group. These steps apply regardless of whether the database service is running in OCI, Oracle AI Database@Azure, Oracle AI Database@AWS, or Oracle AI Database@Google Cloud.

Note  
  
You can only add databases of type Oracle Base Database Service deployed on bare metal or virtual machines or Oracle Exadata Database Service on Cloud@Customer, Oracle Exadata Database Service on Exascale Infrastructure, Oracle Exadata Database Service on Dedicated Infrastructure as members of a DR Protection Group.

Add an Oracle Base Database Service
- From the Resource type menu, select Database .
- From the Database type list, select Oracle Base Database .
- Select the Database system which hosts the database to add.
- Select the Database home for the database to add.
- Select the Database to add.
- Select a Database password secret which contains the database password.
- If prompted, accept the warning that adding or removing members requires you to refresh and verify all the existing plans in the protection group.
Note  
  
Ensure to add the resources from primary database to the primary DR Protection group and the standby database to the standby DR Protection group.
- Click Add to add the database to the DR Protection Group.

Add an Oracle Exadata on Exascale Infrastructure
- From the Resource type menu, select Database .
- From the Database type list, select Oracle Exadata on Exascale Infrastructure .
- Select the VM cluster which hosts the Exadata database to add.
- Select the Database to add.
- Select a Database password secret which contains the database password.
- If prompted, accept the warning that adding or removing members requires you to refresh and verify all the existing plans in the protection group.
Note  
  
Ensure to add the resources from primary database to the primary DR Protection group and the standby database to the standby DR Protection group.
- Click Add to add the database to the DR Protection Group.

Add an Oracle Exadata Cloud@Customer
- From the Resource type menu, select Database .
- From the Database type list, select Oracle Exadata Cloud@Customer .
- Select the VM cluster which hosts the Exadata database to add.
- Select the Database to add.
- Select a Database password secret which contains the database password.
- If prompted, accept the warning that adding or removing members requires you to refresh and verify all the existing plans in the protection group.
Note  
  
Ensure to add the resources from primary database to the primary DR Protection group and the standby database to the standby DR Protection group.
- Click Add to add the database to the DR Protection Group.

Add an Oracle Exadata on Oracle Public Cloud
- From the Resource type menu, select Database .
- From the Database type list, select Oracle Exadata on Oracle Public Cloud .
- Select the VM cluster which hosts the Exadata database to add.
- Select the Database for the database to add.
- Select a Database password secret which contains the database password.
- If prompted, accept the warning that adding or removing members requires you to refresh and verify all the existing plans in the protection group.
Note  
  
Ensure to add the resources from primary database to the primary DR Protection group and the standby database to the standby DR Protection group.
- Click Add to add the database to the DR Protection Group.

Note  
  
Database passwords stored as Secrets (in the Vault Service) are only retrieved and used when performing database DR operations such as switchover or failover. They are not stored locally anywhere within the Full Stack Disaster Recovery Service. To setup a Vault with a Secret, see[Preparing Oracle Databases for Full Stack Disaster Recovery](https://docs.oracle.com/iaas/disaster-recovery/doc/prepare-database-disaster-recovery.html#GUID-1F5A7D12-AC76-4285-BE00-63D053C15FBC).

Related Topics
- [Full Stack DR Built-in Plan Groups for DR Plans](https://docs.oracle.com/iaas/disaster-recovery/doc/built-in-plan-groups.html)

Parent topic:[Add Members to a Disaster Recovery Protection Group](https://docs.oracle.com/iaas/disaster-recovery/doc/add-members-protection-group.html#GUID-C7C2C66A-3066-4D6E-9D61-FD7A32D5EF22)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
