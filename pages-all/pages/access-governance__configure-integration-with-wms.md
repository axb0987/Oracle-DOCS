# Configure Integration with Oracle Warehouse Management Cloud (WMS)
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-with-wms.htm
- Fetched: 2026-09-05 03:13 CDT

# Configure Integration with Oracle Warehouse Management Cloud (WMS)

You can establish a connection between Oracle Access Governance and Oracle Warehouse Management Cloud (WMS) application as a Managed System. To configure, use Orchestrated Systems in the Oracle Access Governance Console.

## Prerequisites - Create a User and Assign Group

Create an administrator user or a user with the required permissions in Oracle Warehouse Management Cloud (WMS).

- Create a user or use an existing user. See[Creating Users](https://docs.oracle.com/en/cloud/saas/warehouse-management/26a/owmol/how-to-create-new-users.html#How-to-Create-New-Users).
- Assign Administrator role.
- Assign Groups to Users. See[Assigning Groups to Users](https://docs.oracle.com/en/cloud/saas/warehouse-management/26a/owmol/assigning-groups-to-users.html).
- Assign the following permissions to the group from the Group Configuration tab:
- lgfapi_read_access – GET
- HEAD“lgfapi_create_access” – POST
- “lgfapi_update_access” – PATCH
- “lgfapi_delete_access” – DELETE
- 

OAuth2 / Manage OAuth2 Applications
Users with Administrator permissions are granted these permissions by default. These permissions are crucial for CRUD application-level permission to access the supported HTTP methods. See[Application Permissions](https://docs.oracle.com/en/cloud/saas/warehouse-management/26a/owmre/application-permissions.html).
- Sign in with this user to create the OAuth application.

## Prerequisites - Creating an OAuth in Oracle WMS Cloud (Classic UI)

Create an OAuth application in and save the authentication details.

- Sign in to Oracle Warehouse Management Cloud (WMS) instance with administrator credentials.
- Use the Quick Launch by typing`oauth2`in the search bar.
- On the OAuth screen, select New Application .
- Complete the Application form.
- Name : Enter a name for your app
- Client Type : Select **Confidential** for integrations
- Authorization grant type : Select Client credentials
- Redirect URI : Select redirect URIs if required. For example,`https://oauth.pstmn.io/v1/callback`
- Authorized Scopes
- Select Save .
- Copy and save Client ID and Client secret for the OAuth application.

## Configure

You can establish a connection between Prisma Cloud and Oracle Access Governance by entering connection details. To achieve this, use the orchestrated systems functionality available in the Oracle Access Governance Console.

### Navigate to the Orchestrated Systems Page

The Orchestrated Systems page of the Oracle Access Governance Console is where you start configuration of the orchestrated system.
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

### Add details

Add details such as name, description, and configuration mode.
On the Add Details step of the workflow, enter the details for the orchestrated system:
- Enter a name for the system you want to connect to in the Name field.
- Enter a description for the system in the Description field.
- Select Next .

### Add Owners

Add primary and additional owners to your orchestrated system to allow them to manage resources.
You can associate resource ownership by adding primary and additional owners. This drives self-service as these owners can then manage (read, update or delete) the resources that they own. By default, the resource creator is designated as the resource owner. You can assign one primary owner and up to 20 additional owners for the resources.
Note  
  
When setting up the first Orchestrated System for your service instance, you can assign owners only after you enable the identities from the[Manage Identities](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm)section. To add owners:
- Select an Oracle Access Governance active user as the primary owner in the Who is the primary owner? field.
- Select one or more additional owners in the Who else owns it? list. You can add up to 20 additional owners for the resource. You can view the Primary Owner in the list. All the owners can view and manage the resources that they own.

### Account Settings

Outline details of how to manage account settings when setting up your orchestrated system including notification settings, and default actions when an identity moves or leaves your organization.
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

### Integration Settings

On the Integration settings step of the workflow, enter the configuration details to connect to.

Fill the configuration information as explained in the following table, and then select Add .

Authentication Mode (OAuth, Basic Authentication Parameter Name Description
Allow basic authentication Select the checkbox to authenticate with username and password.
Host Name

Base URL to access the Oracle Warehouse Management Cloud (WMS) application. For example:
```

```

Basic Authentication Username Enter username for the Oracle Warehouse Management Cloud (WMS) application.
Basic Authentication Password Enter the password
Basic Authentication Confirm Password Confirm the password
OAuth Authentication server URI

Enter endpoint (URI) for the OAuth 2.0 authorization server.
```

```

OAuth Client ID A unique identifier for the registered OAuth client application. See Prerequisites -[Creating an OAuth in Oracle WMS Cloud (Classic UI)](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-with-wms.htm#prerequisites-create-oauth-wms-classic-ui).
OAuth Client Secret Enter secret key associated with the client application.
Environment code

Enter environment label being referenced. You can get the environment code from the application URL. For example, enter &lt;env_id&gt; from the URL.
```

```

Top level company code Company code registered for a company. In case of parent-child company hierarchy, enter the parent company code.
Parent company code Enter the name of the business entity that's owning the business. In the WMS Cloud application, type Companies in the search box. Select and view the company details.
Document Version Release version of the Oracle Warehouse Management Cloud (WMS) instance with which you want to connect. For example`25D`.

### Finish Up

Review and configure your configuration setup. You're given a choice whether to further configure the orchestrated system before running a data load, or accept the default configuration and begin a data load.
Select one from:
- Customize before enabling the system for data loads
- Activate and prepare the data load with the provided defaults

## Post Configuration
