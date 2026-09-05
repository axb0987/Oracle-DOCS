# Integrate with Database User Management (Oracle)
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-database-user-management-oracle.htm
- Fetched: 2026-09-05 03:14 CDT

# Integrate with Database User Management (Oracle)

The Database User Management connector integrates Oracle Access Governance with database user management tables in Oracle Database. You can establish a connection between Oracle Database and Oracle Access Governance by entering connection details and configuring the connector. To achieve this, use the Orchestrated Systems functionality available in the Oracle Access Governance Console.

## Prerequisites

Before you install and configure a Database User Management (Oracle) orchestrated system, you must consider the following prerequisites and tasks.

### Certified Components

You can integrate any one of the following Oracle Database types with Oracle Access Governance:

- Exadata V2 .
- Oracle Database 12c as single database, pluggable database (PDB), or Oracle RAC implementation.
- Oracle Database 18c as single database, pluggable database (PDB), or Oracle RAC implementation.
- Oracle Database 19c as single database, pluggable database (PDB), or Oracle RAC implementation.
- Oracle Database 23ai as single database, pluggable database (PDB), or Oracle RAC implementation.
- Oracle Autonomous AI Database

### Supported Operations

The Database User Management (Oracle) orchestrated system supports the following operations:
- Create user
- Reset password
- Add roles
- Revoke Roles
- Add privileges
- Revoke privileges

### Default Supported Attributes

The Database User Management (Oracle) orchestrated system supports the following default attributes.

Default Attributes - Manage Permission Mode
DBUM User Entity Target Account Attribute Oracle Access Governance Account Attribute
Return Id uid
Username name
Authentication Type authenticationType
Global DN globalDN
Default Tablespace defaultTablespace
Default Tablespace Quota (in MB) defaultTablespaceQuotaInMB
Temporary Tablespace temporaryTablespace
Profile Name profileName
Account Status accountStatus
Status status
Password password

Role

DBUM (Oracle) roles are mapped to Oracle Access Governance entitlements
adminOption roleAdminOption

Privilege

DBUM (Oracle) privileges are mapped to Oracle Access Governance entitlements
adminOption privilegeAdminOption

### Default Matching Rule

The default matching rule for Database User Management (Oracle) orchestrated system is:

Default Matching Rules
Mode Default Matching Rule
Manage Permissions`userNameOracle = userLogin`

### Create a Target System User Account for Database User Management (Oracle) Orchestrated System Operations

Oracle Access Governance requires a user account to access the system during service operations. Depending on the system you're using, you can create the user, and assign specific permissions and roles to them.

For Oracle database:

- Create a service user using the following SQL statement:
```

```

- Assign the following permissions and roles to the service user created:
```

```

## Configure

You can establish a connection between Oracle Database and Oracle Access Governance by entering connection details and configuring your database environment. To achieve this, use the Orchestrated Systems functionality available in the Oracle Access Governance Console.

### Navigate to the Orchestrated Systems Page
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

### Select system

On the Select system step of the workflow, specify which type of system you would like to onboard. You can search for the required system by name using the Search field.
- Select the Database User Management (Oracle DB) tile. Once selected, a value of Database User Management (Oracle DB) is displayed on the right hand side under What I've selected .
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

### Add owners
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

On the Integration settings step of the workflow, enter the configuration details required to allow Oracle Access Governance to connect to the specified database.
- In the Easy Connect URL for Database field, enter the connect string for the database you want to integrate with Oracle Access Governance. For Oracle Database use the format host/port/database service/sid . For Oracle Autonomous AI Database use the format jdbc:oracle:thin:@&lt;SERVICE_NAME&gt;?TNS_ADMIN=&lt;WALLET-DIR&gt; as described in[Configure Wallet for Autonomous AI Database Integration](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-database-user-management-oracle.htm#oracle-db-user-postinstall).
- In the User Name field, enter the DB user you will use to connect to the database. This is the user you created in[Create a Target System User Account for Database User Management (Oracle) Orchestrated System Operations](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-database-user-management-oracle.htm#oracle-db-user-preinstall).
- Enter the password of the target database user in the Password field. Confirm the password in the Confirm password field.
- In Connection Properties enter any connection properties in the format prop1=val1#prop2=val2
- Check the right hand pane to view What I've selected. If you are happy with the details entered, select Add to create the orchestrated system.

### Finish up

On the Finish Up step of the workflow, you are asked to download the agent you will use to interface between Oracle Access Governance and Oracle Database. Select the Download link to download the agent zip file to the environment in which the agent will run.

After downloading the agent, follow the instructions explained in the[Agent Administration](https://docs.oracle.com/en-us/iaas/Content/access-governance/agent-administration.htm#install-oracle-access-governance-agent)article.
Finally, you are given a choice whether to further configure your orchestrated system before running a data load, or accept the default configuration and initiate a data load. Select one from:
- Customize before enabling the system for data loads
- Activate and prepare the data load with the provided defaults

## Post Configuration

### Configure Wallet for Autonomous AI Database Integration

To enable this feature, download the autonomous database wallet to your agent host, and then update the Easy Connect URL for Database field in the orchestrated system configuration. Complete the following steps to configure this feature:

Complete the following steps to configure Wallet for Autonomous AI Database:
- Create a Database User Management (Oracle) orchestrated system and configure the agent.
- Download the autonomous database wallet using the instructions in[Download Client Credentials (Wallets)](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/connect-download-wallet.html#GUID-B06202D2-0597-41AA-9481-3B174F75D4B1).
- Create a wallet directory inside the installed agent folder,`<PERSISTENT_VOLUME_LOCATION><WALLET-DIR>`. For example:
```

```

- Copy the zipfile containing the wallet you downloaded in Step 2, to the`<PERSISTENT_VOLUME_LOCATION><WALLET-DIR>`and unzip using the command:
```

```

- The unzipped wallet file contains the tnsnames.ora file, which contains the service names available for the Oracle Autonomous AI Database. Select the correct TNS name based on your workload:
- databasename _tpurgent
- databasename _tp
- databasename _high
- databasename _medium
- databasename _low For further details on Oracle Autonomous AI Database service names see[Database Service Names for Autonomous Transaction Processing and Autonomous JSON Database](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/service-names-tranaction-processing.html#ADBSB-GUID-610D50B3-A0F0-4059-B940-324E305C5F55).
- Edit the integration settings for your orchestrated system by following the instructions in[Configure settings for an Orchestrated System](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm).
- Open the`tnsnames.ora`file from the wallet directory and find the TNS label before the = that matches this description block.
For example, if the connection string is:
```

```

- Update the Easy Connect URL for Database field with the connect string for your database, based on the service name you selected in the previous step. The connect string takes the following format:
```

```
For example:
```

```
