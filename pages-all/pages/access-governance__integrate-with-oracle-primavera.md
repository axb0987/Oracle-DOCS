# Integrate with Oracle Primavera Administration
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-oracle-primavera.htm
- Fetched: 2026-09-05 03:15 CDT

# Integrate with Oracle Primavera Administration

## Prerequisites

Before you install and configure an Oracle Primavera Administration orchestrated system, you must consider the following prerequisites and tasks.

### Certified Components

The system must be the following:

- Oracle Primavera Administration (Cloud) – Version 28.8 and later

### Supported Modes
Oracle Primavera Administration orchestrated system supports the following mode:
- Managed System

### Supported Operations
The Oracle Primavera Administration orchestrated system supports the following operations. These operations are started during provisioning of the Oracle Primavera Administration system from Oracle Access Governance.
- [Create Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-create-account)
- [Reset Password](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-change-password)
- [Assign](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-assign-permissions)or[Remove](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-remove-permissions)roles

### Default Supported Attributes
The Oracle Primavera Administration orchestrated system supports the following default attributes. These attributes are mapped depending on the direction of the connection, for example:
- Data being ingested by Oracle Access Governance from Oracle Primavera Administration:`Identity.firstName`would map to`Account.firstName`
- Data being provisioned into Oracle Primavera Administration from Oracle Access Governance:`Account.lastName`would map to`Identity.lastName`

Default Attributes - Managed System Mode
Primavera Entity Attribute Name On Managed System Oracle Access Governance Account Attribute Name Oracle Access Governance Account Attribute Display Name
User id uid Unique Id
loginId name User Login
password password Password
firstName firstName First Name
lastName lastName Last Name
userType userType Person Type
status status Status
emailAddress email Email
Company company Company

### Default Matching Rule

The default matching rule for Oracle Primavera Administration orchestrated system is:

Default Matching Rules
Mode Default Matching Rule
Managed System

Screen value :

`User login = Employee user name`

Attribute name :

`Account.name = Identity.userName`

### Create Oracle Primavera Administration User Account
To create a user account for the Oracle Primavera Administration Orchestrated System perform the following steps:
- Create a user account on the Orchestrated System with the following:
- Username
- Password
- Host
- Port
- TenantId
- Assign necessary privileges such as,`Cloud administrator`and`P6`to the same user to perform the integration operations.

## Configure

You can establish a connection between Primavera and Oracle Access Governance by entering connection details. To achieve this, use the Orchestrated Systems functionality available in the Oracle Access Governance Console.

### Navigate to the Orchestrated Systems Page
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

### Select system

On the Select system step of the workflow, you can specify which type of system you would like to onboard. You can search for the required system by name using the Search field.
- Select Primavera .
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
On the Integration settings step of the workflow, enter the configuration details required to allow Oracle Access Governance to connect to the required Oracle Primavera instance.
Note  
  
The following fields are mandatory, except for the Port field.
- In the User Name field, enter the username of a user you have created on the Primavera system for performing integration operations.

Sample Value :`johnsmith`
- In the Password field enter the password of the user on your Primavera system.

Sample Value :`password`
- In the Confirm password field, confirm the password of the user on your Primavera system.
- In the Host field, enter the host name of the machine hosting your system.

Sample value:`myhost.example.com`
- In the Port field, enter the port number the system is listening on.
- In the TenantId field, enter the value for TenantID. This information is mandatory and the information specified is used for calling the API details.
- Click Add to create the orchestrated system.

### Finish Up
The final step of the workflow is Finish Up , where you are given a choice whether to further configure your orchestrated system before running a data load, or accept the default configuration and initiate a data load. Select one from:
- Customize before enabling the system for data loads
- Activate and prepare the data load with the provided defaults

## Post Configuration
