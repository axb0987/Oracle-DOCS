# Add an Autonomous Database Serverless to a Disaster Recovery Protection Group
- Source: https://docs.oracle.com/iaas/disaster-recovery/doc/add-autonomous-database-protection-group.html
- Fetched: 2026-09-05 18:59 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/disaster-recovery/doc/add-autonomous-database-protection-group.html#dcoc-content-body)

# Add an Autonomous Database Serverless to a Disaster Recovery Protection Group

Learn how to add an Oracle Autonomous AI Database Serverless to a Disaster Recovery (DR) Protection Group. These steps apply regardless of whether the database service is running in OCI, Oracle AI Database@Azure, Oracle AI Database@AWS, or Oracle AI Database@Google Cloud.
- From the Resource type menu, select Autonomous database .
- Select the Autonomous database in the compartment you want to add.
- Select the Standby type for DR drill . The following options are available:

- Refreshable clone
- Full clone :
- Select the Database password secret in your compartment .
- Snapshot standby
- If you select Full clone , then the following options are available:

- Database password secret in your compartment
- Select the Destination vault in your compartment .
- Select the Destination encryption key in your compartment .
Note  
  
Currently, only the Start drill and Stop drill plans are supported.
- If prompted, accept the warning that adding or removing members requires you to refresh and verify all existing plans in the protection group.

Note  
  
Ensure to add the resources only to the primary DR Protection group.
- Click Add to add the Autonomous database Serverless to the DR Protection Group.

Parent topic:[Add Members to a Disaster Recovery Protection Group](https://docs.oracle.com/iaas/disaster-recovery/doc/add-members-protection-group.html#GUID-C7C2C66A-3066-4D6E-9D61-FD7A32D5EF22)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
