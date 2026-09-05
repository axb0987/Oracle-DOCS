# Integrate with Oracle Siebel CRM
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-oracle-siebel-crm.htm
- Fetched: 2026-09-05 03:15 CDT

# Integrate with Oracle Siebel CRM

## Prerequisites

Before you install and configure a Oracle Siebel CRM orchestrated system, you should consider the following prerequisites and tasks.

### Certified Components

The system can be any one of the following:

- 

Siebel CRM 7.5 through Siebel CRM 8.2.2
- 

Siebel Innovation Pack 2015
- 

Siebel Innovation Pack 2016
- 

Siebel Innovation Pack 2017
- 

Siebel Innovation Pack 2018
- 

Siebel 19.x, 20.x, 23.x

### Supported Modes
Oracle Siebel CRM orchestrated system supports the following modes:
- Authoritative Source
- Managed System

### Supported Operations
The Siebel orchestrated system supports the following operations:
- Create user
- Delete user
- Assign Position
- Revoke Position
- Assign Responsibility
- Revoke Responsibility

### Create Siebel User Account

Note  
  
The system user account for connector operations must be created in the LDAP repository. As a security precaution, ensure that this account does not have access to areas protected by Oracle Access Manager.
To create the user account on Siebel, perform the following:
- Log in to Siebel .
- Click Site Map icon.
- Click Administration → User .
- Click Employees .
- Click New .
Enter the following details for the account that you are creating:
- Last Name
- First Name
- Job Title
- User ID
- Responsibility: Select Siebel Administrator.
- Position: Select Siebel Administrator.
- Organization: Select Default Organization.
- Employee Type
To create the user account on the Siebel database, perform the following:
- Open the Siebel home directory.
- Open the dbsrvr directory.
- Open one of the following directories:
- For IBM DB2 UDB: DB2
- For Microsoft SQL Server: MSSQL
- For Oracle Database: Oracle

To open one of the following files in a text editor:

- For IBM DB2 UDB: grantusrdb2.sql

For Microsoft SQL Server: addusrmsql.sql

For Oracle Database: grantusroracle.sql

In the file that you open:

- Specify the User ID of the user that you create in Step 1.
- Set a password for the user.
- Provide other required details.
- Run the script.

Additional Configuration Steps and Guidelines for the Target System

Siebel needs to be configured to use either a database or an LDAP repository to store user information. If an LDAP repository is used, then you must ensure that the following prerequisites are addressed:

If Microsoft Active Directory is used as the LDAP repository, then use the ADSI Security Adapter. Ensure that the Propagate Change attribute of the ADSI Security Adapter is set to False on Siebel.

### Manually Making Configuration Changes

Perform the followings tasks to manually make the configuration changes:
- Log in to Siebel Web Tools.
- Create Workspace as follows:
- Click Workspace located next to Main .
- Click Create .
- Enter the name for your Workspace and provide comments.

The workspace is now available under Main .
- Close the window.
- Open the newly created workspace and locate the Employee BusComp option as follows.
- Under Type , select Expand Business Component .
- Click Field .
- From the Business Component drop-down, select Name and search for the employee.
- In the Fields option, add a new field with the following attributes:

Attribute Value
Name User Status
Join S_USER
Column STATUS_CD
Picklist User Status Picklist
Text Length 30
Type DTYPE_TEXT
- Create a child Pick Map for this field as follows:
- Expand the option Field under Business component .
- Select Pick Map .
- Add the following attributes under Pick Map .

Attribute Value
Field User Status
Picklist Field Value
- Navigate to Employee List Applet option as follows.
- Expand Applet, and select List .
- Under the Applet drop-down list, select Name and search for Employee List.
- In the List Column under List, you must add a new list column with the following attributes:

Attribute Value
Name User Status
Field User Status
Available TRUE
Display Name – String Reference SBL_USER_STATUS-1004233658-7EI
Display Name User Status
HTML Display Mode EncodeData
HTML List Edit TRUE
HTML Row Sensitive TRUE
HTML Type Field
Runtime TRUE
Text Alignment Left
Show in List TRUE
Text Alignment-Label Left
- For the same applet, choose the Edit List Applet Web Template to add the newly created list column to any empty placeholder in the list as follows:
- Expand Applet and select Applet Web Template .
- Under Applet Web Template , choose an empty place holder in Edit List and select Edit.
- Click Controls/Columns , and deselect the option show unmapped controls only and select User Status
- Unit test the changes:
- Open the Siebel Call Center to Open and Inspect the workspace for ensuring that the newly added column User Status appears in the user interface to change from Active to Inactive and oppositely.
- Change the status to Inactive for different known users.
- Log out.
- Try to log in as other user.
Note  
  
This test should fail.
- Deliver the workspace.
- Log in to Siebel Web Tools.
- Click the Workspace dashboard button and click Open .
- Click Version to provide the comments and create the version.
- Click Submit and submit the delivery.
- Click Deliver to provide the comments and deliver the workspace.

### Importing SIF File
Importing SIF File option allows a developer to make changes (without the manual modifications described above) by importing an archive file (SIF) containing the repository changes. Importing SIF file helps in enabling the status features.
Note  
  

- By default, this option is disabled.
- The steps to import a SIF file must be followed if you are not performing the manual configuration steps provided in Manually Making Configuration Changes section.

Perform the following steps:
- In Siebel Web Tools, create a Developer Workspace under a upcoming release branch (Integration Workspace).
- Click Workspace dashboard option located next to Main .
- Click Create.
- Enter the name of your Workspace and provide comments to create the workspace.

The workspace is now visible under Main.
- Open the newly created workspace.
- Select Archive &gt; Import from Archive menu item.
- Follow the wizard to import the file.
- Checkpoint and submit the workspace for delivery, rebasing if necessary.
- Deliver the workspace as follows:
- Click the Workspace dashboard option and select your workspace then click Open .
- Click Version to provide your comments and create the version.
- Click Submit and submit for delivery.
- Click Deliver to provide the comments and deliver the workspace.
- Test the changes by following the below:
- Open the Siebel Call Center and click Open to inspect the workspace for ensuring that the newly added column is visible under User Status in the user interface and can be changed from Active to Inactive and the opposite.
- Change the status to Inactive for different known users.
- Log out.
- Try to log in as other user.
Note  
  
This test should fail.

## Configure

You can establish a connection between Oracle Siebel CRM and Oracle Access Governance by entering connection details. To achieve this, use the Orchestrated Systems functionality available in the Oracle Access Governance Console.

### Navigate to the Orchestrated Systems Page
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

### Select system

On the Select system step of the workflow, you can specify which type of system you would like to onboard.
- Select Siebel .
- Click Next .

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

On the Integration settings step of the workflow, enter the configuration details required to allow Oracle Access Governance to connect to the Siebel system.
- In the GatewayServer field, enter the name of the gateway server. A gateway server is a Windows service or UNIX daemon process that stores component definitions and assignments, operational parameters, and connectivity information.
Sample value:
```

```

- In the ServerPort field, enter the port number at which the target system is listening.
- In the User name field, enter the User ID of the target system user account that you want to use for connector operations.

Sample value: johnsmith
- In the Password field, enter the password of the target system user account that you want to use for connector operations and confirm the password.
- In the Object manager field, enter the name of the object manager. The term Object Manager refers to any of several Siebel Server components that support users accessing Siebel Business Applications through the Siebel Web Client and a Web server.
A different Siebel Application Object Manager component is provided for each base application among the Siebel Business Applications or Siebel Industry Applications.
Note  
  
Separate Siebel Application Object Managers are provided for each installed language in which you can run your Siebel applications.

For example, you can refer to any one of the following for the specific language:
For English:
```

```

For Brazilian Portuguese:
```

```

For French:
```

```

For German:
```

```

For Italian:
```

```

For Japanese:
```

```

For Korean:
```

```

For Simplified Chinese:
```

```

For Spanish:
```

```

For Traditional Chinese:
```

```
.
- In the Siebel server field, enter the name of the system server
Sample value:
```

```

- In the Version field, enter the version of the system supported by this connector.

Sample value: 15.5
Note  
  
If the system version that you are using is Siebel CRM 7.5.x or 7.5.x.x then enter 7.5 only as the value of this parameter. For example, if you are using Siebel CRM 7.5.3.7 as the target system, then enter 7.5.
- In the Trusted token field, enter the trusted token value that you specify while configuring the system to communicate with the SSO system. If you have not configured SSO authentication, then enter No.

Sample value: No
- In the Enterprise server field, enter the name of an enterprise, which is a logical collection of Siebel servers that access a single database server and file system.

Sample value: siebel
- In the User Type field, you can specify one of the following Siebel user types:
- Employee: This user is an internal employee and this user is associated with a position in a division within your company.
- User: This user is also a self-registered partner having no position in your company. However, this user has a responsibility that specifies the application views the user can access.
- Click Add to create the orchestrated system.

### Finish Up
The final step of the workflow is Finish Up , where you are given a choice whether to further configure your orchestrated system before running a data load, or accept the default configuration and initiate a data load. Select one from:
- Customize before enabling the system for data loads
- Activate and prepare the data load with the provided defaults

## Postinstall
