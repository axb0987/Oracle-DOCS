# Integrate with Database Application Tables (Oracle)
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-database-application-tables-oracle.htm
- Fetched: 2026-09-05 03:14 CDT

# Integrate with Database Application Tables (Oracle)

## Prerequisites

Before you install and configure a Database Application Tables Orchestrated System, you must consider the following prerequisites and tasks.

- The Database Application Tables system is certified with Oracle Access Governance. See[Database Application Tables Components Certified for Integration with Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/database-application-tables-integration-reference.htm#db-tables-dbat-components-certified-for-integration-with-oracle-access-governanc)for details of the versions supported.

## Configure

Establish a connection between customer databases and Oracle Access Governance by entering connection details. To achieve this, use the orchestrated systems functionality available in the Oracle Access Governance Console.

### Navigate to the Orchestrated Systems Page
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

### Select system

On the Select system step of the workflow, you can specify which type of system you would like to onboard. You can search for the required system by name using the Search field.
- Select Database Application Table (Oracle DB) .
- Select Next .

### Enter details
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

On the Integration settings step of the workflow, enter the details to connect to the customer database. After connection, the orchestrated system can support full and partial data load. See[Configure Partial Data Load Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-partial-data-load-settings).

Integration settings
Parameter Name Mandatory? Description

Easy Connect URL for Oracle database

Yes

URL of the server hosting the customer database system you want to integrate with.

For Oracle Database use the format host/port/database service/sid . For Oracle Autonomous AI Database use the format jdbc:oracle:thin:@&lt;SERVICE_NAME&gt;?TNS_ADMIN=&lt;WALLET-DIR&gt; as described in[Configure Wallet for Autonomous AI Database Integration](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-database-application-tables-oracle.htm#db-table-oracle-configure).
User name

Yes The username required to connect to the user database system to perform data reconciliation and provisioning.

Password / Confirm password

Yes

The password that authenticates the user you are connecting to the user database system with.

User account table name

Yes

The name of the database table containing your user accounts.
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

Lookup tables

Comma-separated list of lookup tables for attributes such as country.
Note  
  
Do not include the user name of the table owner in the table name e.g. MYUSER.MYDBAT_LOOKUP else you will see errors. User name is passed as a separate parameter as detailed in this table.
Affiliation tables Comma-separated list of affiliation tables created. For more information, see[DBAT Affiliation Support for Custom Multivalued Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/database-application-tables-integration-reference.htm#db-tables-dbataffiliations).

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

This value will be used as the disable value if the status column is configured, and it is a String type. If no value is provided for this parameter, then it defaults to 'INACTIVE'.

Date format

Format for date data that is being converted to strings. If you want to handle date data as a date editor, then do not enter any value for this parameter. If you want to handle date data as text, then you must enter the date format. Specifying a value for this parameter invalidates the allNative parameter.

Timestamp format

Format for timestamp data that is being converted to strings. Specifying this property invalidates the nativeTimestamps and allNative properties

User account filter condition

A WHERE clause which defines the subset of user account records that you want to bring from your customer database into Oracle Access Governance.

Create script

Custom script to use custom stored procedures or SQL statements rather than the default SQL statements for performing provisioning operations. Enter the file URL of the Groovy script created for the create user account provisioning operation. You must enter the file URL in the following format:`/directoryName/fileName`.

Sample value:

`/app/scripts/create_user.groovy`

For further details on scripting with the Database Application Tables integration, see[Develop Custom Scripts for Database Application Tables (Oracle) Using Groovy](https://docs.oracle.com/en-us/iaas/Content/access-governance/develop-custom-scripts-for-database-application-tables-oracle-using-groovy.htm)

Update script

Custom script to use custom stored procedures or SQL statements rather than the default SQL statements for performing provisioning operations. Enter the file URL of the Groovy script created for the update user account provisioning operation. This script is called when you update the account attribute form, enable or disable the user account. You must enter the file URL in the following format:`/directoryName/fileName`.

Sample value:

`/app/scripts/update_user.groovy`

For further details on scripting with the Database Application Tables integration, see[Develop Custom Scripts for Database Application Tables (Oracle) Using Groovy](https://docs.oracle.com/en-us/iaas/Content/access-governance/develop-custom-scripts-for-database-application-tables-oracle-using-groovy.htm)

Delete script

Custom script to use custom stored procedures or SQL statements rather than the default SQL statements for performing provisioning operations. Enter the file URL of the Groovy script created for the delete user account provisioning operation. This script is called when you revoke or delete an account. You must enter the file URL in the following format:`/directoryName/fileName`.

Sample value:

`/app/scripts/delete_user.groovy`

For further details on scripting with the Database Application Tables integration, see[Develop Custom Scripts for Database Application Tables (Oracle) Using Groovy](https://docs.oracle.com/en-us/iaas/Content/access-governance/develop-custom-scripts-for-database-application-tables-oracle-using-groovy.htm)

Dataload script

Custom script to use custom stored procedures or SQL statements rather than the default SQL statements for performing provisioning operations. Enter the file URL of the Groovy script created for reconciliation. The connector delegates the data load operation to the Groovy script, which is responsible for passing the information (connector object) to the callback handler. This script is called while performing an account search (operations such as full data load). You must enter the file URL in the following format:`/directoryName/fileName`.

Sample value:

`/app/scripts/full_data_load.groovy`

For further details on scripting with the Database Application Tables integration, see[Develop Custom Scripts for Database Application Tables (Oracle) Using Groovy](https://docs.oracle.com/en-us/iaas/Content/access-governance/develop-custom-scripts-for-database-application-tables-oracle-using-groovy.htm)

Add relationship data script

Custom script to use custom stored procedures or SQL statements rather than the default SQL statements for performing provisioning operations. Enter the file URL of the Groovy script created for the add multivalued attribute (including permissions for account) provisioning operation. This script is called when you add multivalued child attributes. You must enter the file URL in the following format:`/directoryName/fileName`.

Sample value:

`/app/scripts/add_mulval_attr.groovy`

For further details on scripting with the Database Application Tables integration, see[Develop Custom Scripts for Database Application Tables (Oracle) Using Groovy](https://docs.oracle.com/en-us/iaas/Content/access-governance/develop-custom-scripts-for-database-application-tables-oracle-using-groovy.htm)

Remove relationship data script

Custom script to use custom stored procedures or SQL statements rather than the default SQL statements for performing provisioning operations. Enter the file URL of the Groovy script created for the remove multivalued attribute (including permissions for account) provisioning operation. This script is called while removing multivalued child attributes. You must enter the file URL in the following format:`/directoryName/fileName`.

Sample value:

`/app/scripts/remove_mulval_attr.groovy`

For further details on scripting with the Database Application Tables integration, see[Develop Custom Scripts for Database Application Tables (Oracle) Using Groovy](https://docs.oracle.com/en-us/iaas/Content/access-governance/develop-custom-scripts-for-database-application-tables-oracle-using-groovy.htm)
- Select Add to create the orchestrated system.

### Finish Up

The final step of the workflow is Finish Up where you're prompted to download the agent for the Orchestrated System. After you have downloaded the agent, you can install and configure the agent in your environment using the instructions in[Manage Oracle Access Governance Agent for Indirect Integrations](https://docs.oracle.com/en-us/iaas/Content/access-governance/agent-administration.htm).
You're given a choice whether to further configure the orchestrated system before running a data load, or accept the default configuration and start a data load. Select one from:
- Customize before enabling the system for data loads . You can also configure for incremental data load. See[Configure Partial Data Load Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-partial-data-load-settings).
- Activate and prepare the data load with the provided defaults

## Post Configuration

### Update Intermediate Schema JSON File
When you have completed installation of your agent, an intermediate schema JSON file,`schema.json`is created on the agent host. This file maps the tables in the integrated database with the schema which is represented on Oracle Access Governance. The initial schema JSON file is created with basic attributes enabled for data load, UID, NAME, STATUS and PASSWORD (if configured by user). The full data load operation can run with this initial schema JSON file, loading data for only these basic attributes. You can then further change the schema JSON file to include more attributes for the next data load operations.
Note  
  
Ensure that you have granted read/write permissions on the schema JSON file for the OS user that will be running the agent.

After Day0, to apply outbound transformation, you must update it from the Oracle Access Governance Console. Any transformation rule applied within`Schema.json`would not be considered. To apply transformation rule, see[Apply Outbound Transformations for Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#apply-outbound-transformations-for-identity-attributes). However, if you change the attribute or delete an attribute in`Schema.json`, the transformation rules, related to that particular account attribute, gets deleted during Schema Discovery operation.

For full details on the structure and options available when editing the`schema.json`, refer to[Schema JSON File Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/schema-json-file-reference.htm).

### Fetch Latest Custom Attributes

You should perform a schema discovery operation which will fetch the latest custom attribute information. For details on how to perform this task, see[Fetch Latest Custom Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#fetch-attributes).

### Configuring SSL/TLS Communication in Oracle Database
To secure communication between your Oracle Access Governance agent and the Oracle database, you can configure Secure Sockets Layer/Transport Layer Security (SSL/TLS). To do this, ensure that you have completed the following steps:
- Configure Data Encryption and Integrity in Oracle Database

See[Configuring Transport Layer Security Authentication](https://docs.oracle.com/en/database/oracle/oracle-database/19/dbseg/configuring-secure-sockets-layer-authentication.html)for information about configuring data encryption and integrity.
- To configure your Oracle Access Governance agent to use SSL/TLS when communicating with the database, perform the following steps:
- Export the certificate on the Oracle Database host computer.
- Copy the database certificate to your Oracle Access Governance agent host.
- Import the database certificate into the Java truststore of the agent using the command:
```

```

- Update the agent`config.properties`file to include the following:
```

```

### Configure Wallet for Autonomous AI Database Integration

A connection to Oracle Autonomous AI Database requires the client, in this case the Oracle Access Governance agent, to be configured to support SSL communication between the agent and the database service. To enable this feature, you should download the autonomous database wallet to your agent host, and then update the Easy Connect URL for Database field in the orchestrated system configuration. Complete the following steps to configure this feature:
- Create a Database User Management (Oracle) orchestrated system and configure the agent.
- Download the autonomous database wallet using the instructions in[Download Client Credentials (Wallets)](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/connect-download-wallet.html#GUID-B06202D2-0597-41AA-9481-3B174F75D4B1).
- Create a wallet directory on the agent host, under the`<agent-vol-location>/app`directory. For example:
```

```

- Copy the zipfile containing the wallet you downloaded in Step 2, to the wallet folder, and unzip using the command:
```

```

- The unzipped wallet file will contain the`tnsnames.ora`file, which contains the service names available for the Oracle Autonomous AI Database. Choose from one of the following depending on your workload:
- databasename _tpurgent
- databasename _tp
- databasename _high
- databasename _medium
- databasename _low For further details on Oracle Autonomous AI Database service names see[Database Service Names for Autonomous Transaction Processing and Autonomous JSON Database](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/service-names-tranaction-processing.html#ADBSB-GUID-610D50B3-A0F0-4059-B940-324E305C5F55).
- Edit the integration settings for your orchestrated system by following the instructions in[Configure settings for an Orchestrated System](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm). Update the Easy Connect URL for Database field with the connect string for your database, based on the service name you selected in the previous step. The connect string should take the following format:
```

```
For example:
```

```
