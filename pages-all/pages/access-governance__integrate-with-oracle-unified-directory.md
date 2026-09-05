# Integrate with Oracle Unified Directory
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-oracle-unified-directory.htm
- Fetched: 2026-09-05 03:15 CDT

# Integrate with Oracle Unified Directory

The Oracle Unified Directory connector integrates Oracle Access Governance with Oracle Unified Directory. You can establish a connection between Oracle Unified Directory and Oracle Access Governance by entering connection details and configuring the connector. To achieve this, use the Orchestrated Systems functionality available in the Oracle Access Governance Console.

## Preinstall

Before you install and configure an Oracle Unified Directory orchestrated system, you must consider the following pre-requisites and tasks.

### Certified Components

The system can be any one of the following:

- Oracle Unified Directory 11g 11.1.1.5.0, 11.1.2.0.0, 11.1.2.2.0, and 11.1.2.3.0
- Oracle Unified Directory 12c 12.2.1.3.0 and 12.2.1.4.0
- Oracle Unified Directory 14c 14.1.2.1.0

### Supported Operations (Authoritative)

The Oracle Unified Directory orchestrated system supports the following operations where Oracle Unified Directory is the authoritative source for identities:
- Create user
- Update user
- Delete user
- Enable user
- Disable user
- Reset password
- Create group or organization unit
- Update group name or organization unit name
- Delete group or organization unit
- Update container DN
- Add groups
- Revoke groups

### Supported Operations (Non-Authoritative)

The Oracle Unified Directory orchestrated system supports the following operations where Oracle Unified Directory is a managed system:
- Create user
- Reset password
- Add groups
- Revoke groups

### Create a System User Account for Oracle Unified Directory Orchestrated System Operations

Oracle Access Governance requires a user account to access the system during service operations. Depending on the system you are using, you can create the user in your system and assign specific permissions and roles to the user.

For Oracle Unified Directory:
You must create a system user account for performing the following functions.
- Create, modify, and delete entries related to the managed objects, including accounts, groups, roles (if supported), and organizational units (ou).
- Update passwords for users.
Create an admin user account on the Oracle Unified Directory system. For details of how to do this, see the relevant sections in the following:
- Oracle Unified Directory 11g :[Configuring Root Users](https://docs.oracle.com/cd/E52734_01/oud/OUDAG/root_users.htm#OUDAG00545)
- Oracle Unified Directory 12c :[Configuring Root Users](https://docs.oracle.com/en/middleware/idm/unified-directory/12.2.1.4/oudag/managing-users-and-groups.html#GUID-F73A86D4-BC86-4B0F-B2B6-D39599DF5A4F)

## Install

You can establish a connection between Oracle Unified Directory and Oracle Access Governance by entering connection details and configuring your OUD environment. To achieve this, use the Orchestrated Systems functionality available in the Oracle Access Governance Console.

### Navigate to the Orchestrated Systems Page
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

### Select system

On the Select system step of the workflow, specify which type of system you would like to onboard.
- Select Oracle Unified Directory and click Next .

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

On the Integration settings step of the workflow, enter the configuration details required to allow Oracle Access Governance to connect to the target Oracle Unified Directory.
- In the Host field, enter the hostname or IP address for the directory you want to integrate with Oracle Access Governance.
- In the Port field, enter the value of the TCP/IP port number used to communicate with the LDAP server.
- Enter the distinguished name which you will use to authenticate to the directory, in the Administrator Username field. This is the user you created in[Create a Target System User Account for Oracle Unified Directory Orchestrated System Operations](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-oracle-unified-directory.htm#oracle-ud-preinstall).
- Enter the password of the target distinguished name in the Password field. Confirm the password in the Confirm password field.
- Enter a base context from which to begin searches for users and groups into the Base Contexts field.
- In the Failover field, enter a list of failover servers in the format`<servername>:<port>, <servername>:<port>, ...`, for example`OUDExample1:636, OUDExample1:636, ...`
- In the SSL Enabled field, ensure that the value true is selected.
- Check the right hand pane to view What I've selected. If you are happy with the details entered, select Add to create the orchestrated system.

### Finish Up

The final step of the workflow is Finish Up where you are prompted to download the agent for your Orchestrated System. Once you have downloaded the agent, you can install and configure the agent in your environment using the instructions in[Install Oracle Access Governance Agent](https://docs.oracle.com/en-us/iaas/Content/access-governance/agent-administration.htm#install-oracle-access-governance-agent).
You are given a choice whether to further configure your orchestrated system before running a data load, or accept the default configuration and initiate a data load. Select one from:
- Customize before enabling the system for data loads
- Activate and prepare the data load with the provided defaults

## Postinstall

There are no postinstall steps associated with a Oracle Unified Directory system.

## Reference

Oracle Access Governance supports the following default Oracle Unified Directory attributes.

Account Attribute Mapping (Authoritative Mode)
Entity Oracle Unified Directory Account Attribute Oracle Access Governance Account Attribute Oracle Access Governance Display name
User User Login uid Unique Id
uid name Employee user name
full DN fullDN Full DN
mail email Email
givenName firstName First name
initials middleName Middle name
sn lastName Last name
manager managerLogin Manager
Status status Status
departmentnumber department Department
l location Location

Account Attribute Mapping (Manage Permission Mode)
Entity Oracle Unified Directory Account Attribute Oracle Access Governance Account Attribute Oracle Access Governance Display name
User NsuniqueID uid Unique Id
uid name User login
Full DN fullDn Full DN
Password password Password
title title Title
givenname firstName First name
initials middleName Middle name
sn lastName Last name
ContainerDN containerDN Container DN
mail emailID Email
cn commonName Common name
departmentnumber department Department
l location Location
telephonenumber telephone Telephone
preferredlanguage preferredlanguage Preferred language
login Disabled loginDisabled Login disabled
Status status Status
buildingName buildingName Building name
displayName displayName Display name
o organizationName Organization name
homePhone homePhone Home phone
mobile mobile Mobile
orclActiveStartDate startDate Start date
orclActiveEndDate endDate End date
orclTimeZone timeZone Time zone
orclGuid orclGUID GUID
Group Name groups as entitlement Groups
