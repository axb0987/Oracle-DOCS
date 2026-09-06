# Add an Autonomous Database on Dedicated Exadata Infrastructure to a Disaster Recovery Protection Group
- Source: https://docs.oracle.com/iaas/disaster-recovery/doc/add-autonomous-container-database-protection-group.html
- Fetched: 2026-09-05 18:59 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/disaster-recovery/doc/add-autonomous-container-database-protection-group.html#dcoc-content-body)

# Add an Autonomous Database on Dedicated Exadata Infrastructure to a Disaster Recovery Protection Group

Learn how to add an Autonomous Database on Dedicated Exadata Infrastructure (Autonomous container database) to a Disaster Recovery (DR) Protection Group. These steps apply regardless of whether the database service is running in OCI, Oracle AI Database@Azure, Oracle AI Database@AWS, or Oracle AI Database@Google Cloud.
- From the Resource type menu, select Autonomous container database .
- Select the Autonomous container database in compartment you want to add. The following options are available:

- Autonomous container database on dedicated infrastructure
- Autonomous container database on Exadata Cloud@Customer
- In the Connection string type , select any one of the following options:

- Primary service :

During DR drills, reuse the same connection strings for the snapshot standby, as those used by the primary database.
- Snapshot service :

During DR drills, create new snapshot connection strings for the snapshot standby.
- If prompted, accept the warning that adding or removing members requires you to refresh and verify all existing plans in the protection group.

Note  
  
Ensure to add the resources only to the primary DR Protection group.
- Click Add to add the Autonomous container database to the DR Protection Group.

Related Topics
- [Snapshot Standby Features](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/autonomous-data-guard-snapshot-standby.html)
- [About Connecting to an Autonomous Database Instance](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/connect-introduction.html)

Parent topic:[Add Members to a Disaster Recovery Protection Group](https://docs.oracle.com/iaas/disaster-recovery/doc/add-members-protection-group.html#GUID-C7C2C66A-3066-4D6E-9D61-FD7A32D5EF22)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
