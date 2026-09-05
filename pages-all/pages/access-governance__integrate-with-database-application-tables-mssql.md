# Integrate with Database Application Tables (MSSQL)
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-database-application-tables-mssql.htm
- Fetched: 2026-09-05 03:14 CDT

# Integrate with Database Application Tables (MSSQL)

## Prerequisites

Before you install and configure a Database Application Tables (MSSQL) Orchestrated System, you should consider the following prerequisites and tasks.

- The Database Application Tables (MSSQL) system is certified with Oracle Access Governance. See[Database Application Tables Components Certified for Integration with Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/database-application-tables-integration-reference.htm#db-tables-dbat-components-certified-for-integration-with-oracle-access-governanc)for details of the versions supported.

## Configure

You can establish a connection between customer databases and Oracle Access Governance by entering connection details. To achieve this, use the orchestrated systems functionality available in the Oracle Access Governance Console.

### Navigate to the Orchestrated Systems Page
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

### Select system

On the Select system step of the workflow, you can specify which type of system you would like to onboard. You can search for the required system by name using the Search field.
- Select Database Application Table (MSSQL DB) .
- Click Next .

### Add details
On the Add Details step of the workflow, enter the details for the orchestrated system:
- Enter a name for the system you want to connect to in the Name field.
- Enter a description for the system in the Description field.
- Decide if this orchestrated system is an authoritative source, and if Oracle Access Governance can manage permissions by setting the following check boxes.
- This is the authoritative source for my identities

Select one of the following:
- Source of identities and their attributes : System acts as a source identities and associated attributes. New identities are created through this option.
- Source of identity attributes only : System ingests additional identity attributes details and apply to existing identities. This option doesn't ingest or creates new identity records.
- I want to manage permissions for this system The default value in each case is Unselected .
- Select Next .

### Add Owners
You can associate resource ownership by adding primary and additional owners. This drives self-service as these owners can then manage (read, update or delete) the resources that they own. By default, the resource creator is designated as the resource owner. You can assign one primary owner and up to 20 additional owners for the resources.
Note  
  
When setting up the first Orchestrated System for your service instance, you can assign owners only after you enable the identities from the[Manage Identities](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm)section. To add owners:
- Select an Oracle Access Governance active user as the primary owner in the Who is the primary owner? field.
- Select one or more additional owners in the Who else owns it? list. You can add up to 20 additional owners for the resource. You can view the Primary Owner in the list. All the owners can view and manage the resources that they own.

### Account settings
On the Account settings step of the workflow, enter how you want Oracle Access Governance to manage accounts when the system is configured as a managed system:
- When a permission is requested and the account doesn't already exist, select this option to create new accounts . This option is selected by default. When selected, Oracle Access Governance creates an account if one doesn't exist when a permission is requested. If you clear this option, permissions are provisioned only for existing accounts in the orchestrated system. If no account exists, the provisioning operation fails.
- Select the recipients for notification emails when an account is created. The default recipient is User . If no recipients are selected, notifications aren't sent when accounts are created.
- User
- User manager
- Configure Existing Accounts
Note  
  
You can only set these configurations if allowed by the system administrator. When global account termination settings are enabled, application administrators can't manage account termination settings at the orchestrated-system level.
- Select what to do with accounts when early termination begins : Choose the action to perform when an early termination begins. This happens when you need to revoke identity accesses before official termination date.
- Delete : Deletes all accounts and permissions managed by Oracle Access Governance.
Note  
  
If specific orchestrated system doesn't support the action, no action is taken.
- Disable : Disables all accounts and disables permissions managed by Oracle Access Governance.
- Delete the permissions for disabled accounts : To ensure zero residual access, select this to delete directly assigned permissions and policy-granted permissions during account disablement.
- No action : No action is taken when an identity is flagged for early termination by Oracle Access Governance.
- Select what to do with accounts on the termination date : Select the action to perform during official termination. This happens when you need to revoke identity accesses on the official termination date.
- Delete : Deletes all accounts and permissions managed by Oracle Access Governance.
Note  
  
If specific orchestrated system doesn't support Delete action, then no action is taken.
- Disable : Disables all accounts and disables permissions managed by Oracle Access Governance.
- Delete the permissions for disabled accounts : To ensure zero residual access, select this to delete directly assigned permissions and policy-granted permissions during account disablement.
Note  
  
If specific orchestrated system doesn't support the Disable action, then account is deleted.
- No action : No action is taken on accounts and permissions by Oracle Access Governance.
- When an identity leaves your enterprise you must remove access to their accounts.
Note  
  
You can only set these configurations if allowed by your system administrator. When global account termination settings are enabled, application administrators cannot manage account termination settings at the orchestrated-system level.

Select one of the following actions for the account:
- Delete : Delete all accounts and permissions managed by Oracle Access Governance.
- Disable : Disable all accounts and mark permissions as inactive.
- Delete the permissions for disabled accounts : Delete directly assigned and policy-granted permissions during account disablement to ensure zero residual access.
- No action : Take no action when an identity leaves the organization.
Note  
  
These actions are available only if supported by the orchestrated system type. For example, if Delete is not supported, you will only see the Disable and No action options.
- When all permissions for an account are removed, for example when an identity moves between departments, you may need to decide what to do with the account. Select one of the following actions, if supported by the orchestrated system type:
- Delete
- Disable
- No action
- Manage accounts that aren't created by Access Governance : Select to manage accounts that are created directly in the orchestrated system. With this, you can reconcile existing accounts and manage them from Oracle Access Governance.
- Do not allow users to do password resets : Select to prevent users from resetting the passwords for the orchestrated system. If the orchestrated system doesn't support password change operation, password resets are unavailable, and a message is displayed.
Note  
  
If you don't configure the system as a managed system then this step in the workflow will display but is not enabled. In this case you proceed directly to the Integration settings step of the workflow.
Note  
  
If your orchestrated system requires dynamic schema discovery, as with the Generic REST and Database Application Tables integrations, then only the notification email destination can be set (User, Usermanager) when creating the orchestrated system. You cannot set the disable/delete rules for movers and leavers. To do this you need to create the orchestrated system, and then update the account settings as described in[Configure Orchestrated System Account Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-orchestrated-system-account-settings).

### Integration settings

On the Integration settings step of the workflow, enter the details required to allow Oracle Access Governance to connect to your customer database.

Integration settings
Parameter Name Mandatory? Description

Easy connect URL for Microsoft SQL Server database

Yes

URL of the server hosting the customer database system you want to integrate with.

Use the format host/port/database/encrypt/trustServerCertificate , for example jdbc:sqlserver://[host]:[port];[databaseName];[encrypt];[trustServerCertificate] . For further details refer to the MSSQL JDBC documentation for your version.
User name

Yes The username required to connect to the customer database system to perform data reconciliation and provisioning.

Password? / Confirm password

Yes

The password that authenticates the user you are connecting to the customer database system with.
Database name Yes The customer database to which you need to connect (such as master database).

Custom jar details Yes MSSQL Server database driver jar. Please refer to the MSSQL JDBC documentation for your version for details. The jar name and checksum should be in the format of`<jarName>::<jarChecksum>`.Calculate the checksum using SHA-512. Details of how this is used by the agent can be found in[Custom Jar Support](https://docs.oracle.com/en-us/iaas/Content/access-governance/agent-administration.htm#custom-jar-support).

User account table name

Yes

The name of the table containing your user accounts.
Note  
  
For a key column which is non auto increment, Create Account provisioning will be supported only with custom script. For further details on scripting with the Database Application Tables integration, see[Develop Custom Scripts for Database Application Tables (MSSQL) Using Groovy](https://docs.oracle.com/en-us/iaas/Content/access-governance/develop-custom-scripts-for-database-application-tables-mssql-using-groovy.htm).
Note  
  
Do not include the user name of the table owner in the table name e.g. MYUSER.MYDBAT_PERSON else you will see errors. User name is passed as a separate parameter as detailed in this table.

Permission tables

Add the names of your permission tables in a comma-separated list. This parameter only applies if your orchestrated system is configured in managed system mode.
Note  
  
Do not include the user name of the table owner in the table name e.g. MYUSER.MYDBAT_PERMISSION else you will see errors. User name is passed as a separate parameter as detailed in this table.

Account permission tables

If you have account data resident in parent and child tables, then provide a comma-separated list of the child tables names.
Note  
  
Do not include the user name of the table owner in the table name e.g. MYUSER.MYDBAT_ACCOUNTPERMISSION else you will see errors. User name is passed as a separate parameter as detailed in this table.
Affiliation tables Comma-separated list of affiliation tables created. For more information, see[DBAT Affiliation Support for Custom Multivalued Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/database-application-tables-integration-reference.htm#db-tables-dbataffiliations).

Lookup tables

Comma-separated list of lookup tables for attributes such as country.
Note  
  
Do not include the user name of the table owner in the table name e.g. MYUSER.MYDBAT_LOOKUP else you will see errors. User name is passed as a separate parameter as detailed in this table.

Key column mappings

Yes Comma-separated list of key column mappings. These mappings should be entered in the format`Table:KeyColumn`.
Note  
  
This parameter is applicable for ACCOUNT, ENTITLEMENT, and LOOKUP tables only.

Name column mappings

Yes Comma-separated list of name column mappings. These mappings should be entered in the format`Table:NameColumn`.
Note  
  
This parameter is applicable for ACCOUNT, ENTITLEMENT, and LOOKUP tables only.

User account table password column mapping

Password column mapping for user account table in the format`Table:PasswordColumn`.

User account table status column mapping Yes

Status column mapping for the user account table in the format`Table:StatusColumn`. The status column holds the status of a user record. In case of special values, please configure the enable/disabled value.

User account enabled status value

This value will be used as the enable value if the status column is configured, and it is a String type. If no value is provided for this parameter, then it defaults to 'ACTIVE'.

User account disabled status value

This value is used as the disabled value if the status column is configured, and it's a String type. If no value is provided for this parameter, then it defaults to 'INACTIVE'.
Column identifiers to be quoted Select the delimiter that's used in generating SQL statements when referencing column names. Select the following column delimiters used by the database:
- None (Default): Generates column names without delimiters, for example,`USER_ID`.
- Brackets ([ ]): Uses bracket-delimited column names, for example,`[USER_ID]`.
- Double Quotes (" "): Generates double-quote-delimited column names, for example,`"USER_ID"`.

User account filter condition

A WHERE clause which defines the subset of user account records that you want to bring from the customer database into Oracle Access Governance. For example: COUNTRY in ('IN','US').

Create script

Custom script to use custom stored procedures or SQL statements rather than the default SQL statements for performing provisioning operations. Enter the file URL of the Groovy script created for the create user account provisioning operation. You must enter the file URL in the following format:`/directoryName/fileName`.

Sample value:

`/app/scripts/create_user.groovy`

For further details on scripting with the Database Application Tables integration, see[Develop Custom Scripts for Database Application Tables (MSSQL) Using Groovy](https://docs.oracle.com/en-us/iaas/Content/access-governance/develop-custom-scripts-for-database-application-tables-mssql-using-groovy.htm).

Update script

Custom script to use custom stored procedures or SQL statements rather than the default SQL statements for performing provisioning operations. Enter the file URL of the Groovy script created for the update user account provisioning operation. This script is called when you update the account attribute form, enable or disable the user account. You must enter the file URL in the following format:`/directoryName/fileName`.

Sample value:

`/app/scripts/update_user.groovy`

For further details on scripting with the Database Application Tables integration, see[Develop Custom Scripts for Database Application Tables (MSSQL) Using Groovy](https://docs.oracle.com/en-us/iaas/Content/access-governance/develop-custom-scripts-for-database-application-tables-mssql-using-groovy.htm).

Delete script

Custom script to use custom stored procedures or SQL statements rather than the default SQL statements for performing provisioning operations. Enter the file URL of the Groovy script created for the delete user account provisioning operation. This script is called when you revoke or delete an account. You must enter the file URL in the following format:`/directoryName/fileName`.

Sample value:

`/app/scripts/delete_user.groovy`

For further details on scripting with the Database Application Tables integration, see[Develop Custom Scripts for Database Application Tables (MSSQL) Using Groovy](https://docs.oracle.com/en-us/iaas/Content/access-governance/develop-custom-scripts-for-database-application-tables-mssql-using-groovy.htm).

Dataload script

Custom script to use custom stored procedures or SQL statements rather than the default SQL statements for performing provisioning operations. Enter the file URL of the Groovy script created for reconciliation. The connector delegates the data load operation to the Groovy script, which is responsible for passing the information (connector object) to the callback handler. This script is called while performing an account search (operations such as full data load). You must enter the file URL in the following format:`/directoryName/fileName`.

Sample value:

`/app/scripts/full_data_load.groovy`

For further details on scripting with the Database Application Tables integration, see[Develop Custom Scripts for Database Application Tables (MSSQL) Using Groovy](https://docs.oracle.com/en-us/iaas/Content/access-governance/develop-custom-scripts-for-database-application-tables-mssql-using-groovy.htm).

Add relationship data script

Custom script to use custom stored procedures or SQL statements rather than the default SQL statements for performing provisioning operations. Enter the file URL of the Groovy script created for the add multivalued attribute (including permissions for account) provisioning operation. This script is called when you add multivalued child attributes. You must enter the file URL in the following format:`/directoryName/fileName`.

Sample value:

`/app/scripts/add_mulval_attr.groovy`

For further details on scripting with the Database Application Tables integration, see[Develop Custom Scripts for Database Application Tables (MSSQL) Using Groovy](https://docs.oracle.com/en-us/iaas/Content/access-governance/develop-custom-scripts-for-database-application-tables-mssql-using-groovy.htm).

Remove relationship data script

Custom script to use custom stored procedures or SQL statements rather than the default SQL statements for performing provisioning operations. Enter the file URL of the Groovy script created for the remove multivalued attribute (including permissions for account) provisioning operation. This script is called while removing multivalued child attributes. You must enter the file URL in the following format:`/directoryName/fileName`.

Sample value:

`/app/scripts/remove_mulval_attr.groovy`

For further details on scripting with the Database Application Tables integration, see[Develop Custom Scripts for Database Application Tables (MSSQL) Using Groovy](https://docs.oracle.com/en-us/iaas/Content/access-governance/develop-custom-scripts-for-database-application-tables-mssql-using-groovy.htm).
- Select Add to create the orchestrated system.

### Finish Up

The final step of the workflow is Finish Up where you are prompted to download the agent for your Orchestrated System. Once you have downloaded the agent, you can install and configure the agent in your environment using the instructions in[Manage Oracle Access Governance Agent for Indirect Integrations](https://docs.oracle.com/en-us/iaas/Content/access-governance/agent-administration.htm).
You are given a choice whether to further configure your orchestrated system before running a data load, or accept the default configuration and initiate a data load. Select one from:
- Customize before enabling the system for data loads
- Activate and prepare the data load with the provided defaults

## Post Configuration

### Update Intermediate Schema JSON File
When you have completed installation of your agent, an intermediate schema JSON file,`schema.json`is created on the agent host. This file maps the tables in the integrated database with the schema which is represented on Oracle Access Governance. The initial schema JSON file is created with basic attributes enabled for data load, UID, NAME, STATUS and PASSWORD (if configured by user). The full data load operation can execute with this initial schema JSON file, loading data for only these basic attributes. You can then further modify the schema JSON file to include more attributes for the next data load operations.
Note  
  
Ensure that you have granted read/write permissions on the schema JSON file for the operating system user that will be running the agent.

For full details on the structure and options available when editing the`schema.json`, refer to[Schema JSON File Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/schema-json-file-reference.htm).

### Fetch Latest Custom Attributes

You should perform a schema discovery operation which will fetch the latest custom attribute information. For details on how to perform this task, see[Fetch Latest Custom Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#fetch-attributes)
