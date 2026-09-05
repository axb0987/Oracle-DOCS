# Integrate with Oracle e-Business User Management (UM)
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-oracle-e-business-user-management-um.htm
- Fetched: 2026-09-05 03:14 CDT

# Integrate with Oracle e-Business User Management (UM)

You can establish a connection between Oracle e-Business Suite User Management (UM) and Oracle Access Governance by entering connection details and configuring the connector. To achieve this, use the Orchestrated Systems functionality available in the Oracle Access Governance Console.

## Preinstall

Before you install and configure an Oracle e-Business User Management (UM) orchestrated system, you should consider the following pre-requisites and tasks.

### Certified Components

The system can be any one of the following:

- Oracle E-Business Suite 12.1.1 through 12.1.3
- Oracle E-Business Suite 12.2.x
These applications may run on Oracle Database 10g, 11g, 12c, or 19c as either single database or Oracle RAC implementation.
Note  
  
If your target system is running on Oracle Database release 19.x, then download and apply the Oracle Database patch 31142749 from[My Oracle Support](https://support.oracle.com/portal/). Applying this patch ensures that provisioning operations work fine.

### Supported Operations
The Oracle e-Business User Management (UM) orchestrated system supports the following operations:
- Create user
- Add role
- Update role
- Remove role
- Add responsibility
- Update responsibility
- Remove responsibility
In Oracle E-Business an FND_USER record represents a User Management account. This record is the main component of the account data whose management is enabled by the Oracle E-Business User Management (UM) orchestrated system. This orchestrated system can be used to manage either the FND_USER records or FND_USER records with TCA records. In other words, this connector is used to manage plain user accounts, or user accounts with parties. You can use the Oracle e-Business User Management (UM) orchestrated system to create Oracle E-Business Suite user accounts (FND_USER records) for OIG users, and to grant user roles and responsibilities to these accounts. You can also reconcile newly created users and modified user accounts (FND_USER records) from the managed system. These reconciled records are used to create and update Oracle E-Business User Management accounts assigned to OIG Users. In addition to creating Oracle E-Business User Management accounts, you can use this orchestrated system to create Party or Vendors (Suppliers) in the managed system. Party or vendors represent a Trading Community Architecture (TCA) record in the HZ_PARTIES table. Some applications such as iStore or iProcurement in the Oracle E-Business Suite require users to have a TCA record that is a representative or employee of parties and vendors in your organization. The following are the types of TCA records that this connector supports:
- Parties
- Vendors or Suppliers

The object class used for the Oracle E-Business User Management (UM) orchestrated system with TCA party is ACCOUNT. Roles and responsibilities are handled as child data. You can use this orchestrated system to remove existing roles and responsibilities as well. During user provisioning, if you enter the party or supplier information along with the Oracle E-Business user information, the connector creates an E-Business user account first, creates the party or vendor next, and then establishes the link between the user record and TCA record. For target system users that are linked with Party or Supplier records, the value in the PERSON_PARTY_ID column in the FND_USER table is the same as the value in the PARTY_ID column of the HZ_PARTIES table.During a create or update user provisioning operation, you can link the managed system user account with an existing HRMS employee record by providing Person ID.

### Create a System User Account for Oracle e-Business User Management ( UM ) Orchestrated System Operations

Oracle Access Governance requires a user account to access the system, that can be used by the connector to perform connector operations. Depending on the system you are using, you can create the user in your system and assign specific permissions and roles to the user.

For Oracle e-Business User Management (UM):

- 

Download all the files present in the`https://github.com/oracle/docker-images/tree/main/OracleIdentityGovernance/samples/scripts/Oracle_EBS_UM/1.0`location and copy them to a temporary directory on either the system host computer, or a computer on which the Oracle Database Client has been installed.
Alternatively, you can run the following steps to get the scripts:
- 

`wget https://github.com/oracle/docker-images/archive/refs/heads/main.zip`
- 

`unzip main.zip`
- 

`cp docker-images-main/OracleIdentityGovernance/samples/scripts/Oracle_EBS_UM/1.0/* TEMP_DIR`

Where`TEMP_DIR`is a temporary directory on either the system host computer or a computer on which the Oracle Database Client has been installed.
- 

On the computer where you copy the scripts directory, verify that there is a TNS entry in the`tnsnames.ora`file for the system database.
- 

Change to the directory containing the scripts directory and depending on the host platform, run either the`Run_UM_DBScripts.sh`or`Run_UM_DBScripts.bat`file. These files are present at`https://github.com/oracle/docker-images/tree/main/OracleIdentityGovernance/samples/scripts/Oracle_EBS_UM/1.0`location.
- 

When you run the script, you are prompted for the following information:
- 

`Enter the ORACLE_HOME`

Set a value for the`ORACLE_HOME`environment variable. This prompt is displayed only if the`ORACLE_HOME`environment variable has not been set on the computer on which you are running the script.
- 

`Enter the System User Name`

Enter the login (user name) of a DBA account with the privileges to create and configure a new system user.
- 

`Enter the name of the database`

Enter the connection string or service name given in the`tnsnames.ora`file to connect to the system database.

This connects you to the SQL*Plus client.
- 

`Enter password`

Enter the password of the APPS user in the system. The Type and Package are created, and then the connection to the database is disconnected.
- 

`Enter password`

Enter the password of the dba user.
- 

`Enter New database Username to be created`

Enter a user name for the database account that you want to create.
- 

`Enter the New user password`

Enter a password for the database account that you want to create.

This installs all wrappers packages under the APPS schema, creates the new database account, and then grants all the required privileges on the tables and packages.
- 

`Connecting with newly created database user`

Enter the connection string or service name that you provided earlier.

The user account for connector operations is created.

## Install

You can establish a connection between Oracle e-Business User Management (UM) and Oracle Access Governance by entering connection details and configuring your environment. To achieve this, use the Orchestrated Systems functionality available in the Oracle Access Governance Console.

### Navigate to the Orchestrated Systems Page
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

### Select system

On the Select system step of the workflow, you can specify which type of application you would like to onboard.
- Select Oracle E-Business User Management .
- Click Next .

### Add details
On the Add Details step of the workflow, enter the details for the orchestrated system:
- Enter a name for the system you want to connect to in the Name field.
- Enter a description for the system in the Description field.
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

On the Integration settings step of the workflow, enter the configuration details required to allow Oracle Access Governance to connect to the system.
- In JDBC URL Template field, specify the database connection string in the format host:post:sid syntax format. For example,`jdbc:oracle:thin:@%host:%port:%sid`. For more information on JDBC URL formats, refer to the Determining Values for the JDBC URL and Connection Properties Parameters
- In the User field, enter the user ID of the DB user account that Oracle Access Governance uses to connect to the Oracle E-Business Suite User Management system. For example,`sys`as`sysdba`.
- Enter the password of the target database user in the Password field. Confirm the password in the Confirm password field.
- Click Add .

### Finish Up

The final step of the workflow is Finish Up where you are prompted to download the agent for your Orchestrated System. Once you have downloaded the agent, you can install and configure the agent in your environment using the instructions in[Install Oracle Access Governance Agent](https://docs.oracle.com/en-us/iaas/Content/access-governance/agent-administration.htm#install-oracle-access-governance-agent).
You are given a choice whether to further configure your orchestrated system before running a data load, or accept the default configuration and initiate a data load. Select one from:
- Customize before enabling the system for data loads
- Activate and prepare the data load with the provided defaults

## Postinstall
