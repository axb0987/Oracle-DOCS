# Integrate with Microsoft Teams
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-microsoft-teams.htm
- Fetched: 2026-09-05 03:14 CDT

# Integrate with Microsoft Teams

## Prerequisites

Before you install and configure a Microsoft Teams orchestrated system, you should consider the following prerequisites and tasks.

### Certified Components

The system must be the following:

- Microsoft Teams

### Supported Modes
Microsoft Teams orchestrated system supports the following modes:
- Managed System

### Supported Operations
The Microsoft Teams orchestrated system supports the following operations:
- Create User
- Delete User
- Reset Password
- Add Teams Group
- Remove Teams Group

### Microsoft Teams Application Configuration and Settings
Before you can establish a connection, you need to perform the following tasks in your Microsoft Teams application:
- Create and register an enterprise application that you want to integrate with Oracle Access Governance. For more information, refer[Microsoft documentation](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app).
- Generate a client secret for the application
- Assign the following delegated permissions that the client application requires on Microsoft Teams Directory:

Delegated Permission
- 

Read and write directory data
- 

Read and write all groups
- 

Read all groups
- 

Access the directory as the signed-in user
- 

Read directory data
- 

Read all user’s full profiles
- 

Read all user’s basic profiles
- 

Sign in and read user profile
- Add the client application to "Company Administrator" and “User Account Administrator” in the Microsoft Teams administrative roles.

For more information, refer[Microsoft documentation](https://learn.microsoft.com/en-us/graph/notifications-integration-app-registration).

## Configure

You can establish a connection between Microsoft Teams and Oracle Access Governance by entering connection details. To achieve this, use the orchestrated systems functionality available in the Oracle Access Governance Console.

### Navigate to the Orchestrated Systems Page
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

### Select system

On the Select system step of the workflow, you can specify which type of system you would like to onboard.
- Select Microsoft Teams .
- Click Next .

### Add Owners
You can associate resource ownership by adding primary and additional owners. This drives self-service as these owners can then manage (read, update or delete) the resources that they own. By default, the resource creator is designated as the resource owner. You can assign one primary owner and up to 20 additional owners for the resources.
Note  
  
When setting up the first Orchestrated System for your service instance, you can assign owners only after you enable the identities from the[Manage Identities](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm)section. To add owners:
- Select an Oracle Access Governance active user as the primary owner in the Who is the primary owner? field.
- Select one or more additional owners in the Who else owns it? list. You can add up to 20 additional owners for the resource. You can view the Primary Owner in the list. All the owners can view and manage the resources that they own.

### Enter details

On the Add Details step of the workflow, enter the details for the orchestrated system:
- Enter a name for the system you want to connect to in the Name field.
- Enter a description for the system in the Description field.
- Select Next .

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

On the Integration settings step of the workflow, enter the configuration details required to allow Oracle Access Governance to connect to Microsoft Teams.
- In the Host field, enter the host name of the machine hosting your Microsoft Teams system.

For example, for the Microsoft Graph API, you may enter graph.microsoft.com
- In the Port field, enter the port number at which the system will be accessible.
Note  
  
This field is not mandatory.
- Enter the client ID (a unique string) value. The client ID, also known as Application ID, is obtained when registering an application on Microsoft Entra ID (formerly Azure Active Directory). This value identifies your application in the Microsoft identity platform. For more details refer[Microsoft documentation](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/application-properties).
- In the Client secret field, enter the secret ID value to authenticate the identity of your client application. You need to create a new client secret for your application and enter the value in this field.
- In the Authentication Server Url field, enter the URL of the authentication server that validates the client ID and client secret for your target system in the Authentication Server Url field.
- Click Add to create the orchestrated system.

## Postconfiguration
