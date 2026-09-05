# Configure Integration with Oracle APEX
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-apex-configure-integration-with-oracle-apex.htm
- Fetched: 2026-09-05 03:15 CDT

# Configure Integration with Oracle APEX

## Prerequisites

Before you install and configure a Oracle APEX Orchestrated System, you should consider the following prerequisites and tasks.

### Certification

Check that your Oracle APEX system is certified with Oracle Access Governance by referring to[Components Certified for Integration with Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-apex-oracle-apex-integration-reference.htm#oracle-apex-components-certified-for-integration-with-oracle-access-governance)for details of the versions supported.

### Before You Begin

Before you begin configuring the Oracle REST Data Services (ORDS) REST module for Oracle APEX, ensure the following requirements are met.
- Access to ORDS Web Developer UI : Ensure you have access to the ORDS Web Developer UI, which is accessible via a URL in the format`https://<hostname>/ords/sql-developer`.
- Administrative Privileges : You must have an account possessing administrative privileges (such as`ADMIN`), or with a user authorized to:
- Create and manage database users.
- Grant necessary REST roles and privileges.
- Enable REST access for users and schemas.
- Obtain the ORDS Module Script : Ensure you have access to the oracle.ag.sql script, which is required to register a REST module in Oracle ORDS.

You can find the script at:[https://github.com/oracle/docker-images/tree/main/OracleIdentityGovernance/samples/scripts/Oracle_APEX/1.0](https://github.com/oracle/docker-images/tree/main/OracleIdentityGovernance/samples/scripts/Oracle_APEX/1.0)

#### Configure the ORDS REST Module for Oracle APEX

Once all prerequisites have been completed, perform the following steps to configure the ORDS REST Module for Oracle APEX.
- [Create a REST-Enabled ORDS User Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-apex-configure-integration-with-oracle-apex.htm#oracle-apex-createserviceuseraccount)
- [Import Oracle REST Data Services (ORDS) Module Script](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-apex-configure-integration-with-oracle-apex.htm#oracle-apex-import-oracle-rest-data-services-ords-module-script)
- [Configure OAuth 2.0 for ORDS Module](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-apex-configure-integration-with-oracle-apex.htm#oracle-apex-configure-oauth-2-0-for-ords-module)

### Create a REST-Enabled ORDS User Account

Oracle Access Governance requires a ORDS user account to access the Oracle APEX system during service operations. Create and set up a dedicated database user for hosting and exposing REST modules using SQL Developer web, so external clients can securely access APIs.
This REST-enabled database user will:
- Own all REST modules.
- Provide the execution context for RESTful API calls.
- Act as the principal identity associated for the exposed APIs.
Note  
  
Do not use privileged accounts like`SYS`,`SYSTEM`, or`ADMIN`to expose REST modules. Instead, always create a separate, REST-enabled database user to serve as the REST module owner.

#### Step 1: Create a REST-Enabled ORDS User Account
- Log in to the ORDS Web Developer UI, such as`https://apex.example.com/ords/sql-developer`) using an account with administrative privileges, such as`ADMIN`.
- Click the navigation menu icon, and select Administration and then select Database Users .
- Click + Create User .

The Create User page is displayed with User tab selected.
- Enter the following information to create a REST-enabled database user:
- User Name : Provide a user name.
- Password : Provide a password.
- Confirm Password : Confirm the password:
- Enable REST, GraphQL, MongoDB API, and Web access .
- Click the Granted Roles tab for the following roles:

CONNECT Choose Granted and Default .
RESOURCE Choose Granted and Default .
APEX_ADMINISTRATOR_ROLE Choose Granted and Default .
ORDS_ADMINISTRATOR_ROLE Choose Granted and Default .
Note  
  
These roles are essential for managing APEX and ORDS REST modules securely.
- Click Create User .

#### Step 2: Verify the REST-Enabled ORDS Service User Account

Verify that the ORDS user appears on the Current User page using the following steps:
- Click the navigation menu icon, and select Administration and then Database Users .

The Current User page appears.
- Search for the new user.

### Import Oracle REST Data Services (ORDS) Module Script

Learn how to register a REST module in Oracle ORDS by importing the oracle.ag.sql script through Oracle SQL Developer workspace.

#### Register a REST Module in Oracle ORDS

To register a REST module in Oracle ORDS, perform the following steps:
- Download the oracle.ag.sql script:[Oracle APEX Module Script](https://github.com/oracle/docker-images/tree/main/OracleIdentityGovernance/samples/scripts/Oracle_APEX/1.0)
- Log in to the ORDS Web Developer UI using the REST-Enabled ORDS Service User Account created in Section[Create a REST-Enabled ORDS User Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-apex-configure-integration-with-oracle-apex.htm#oracle-apex-createserviceuseraccount).
- Click the navigation menu icon, and select SQL .

The SQL worksheet page appears where you can execute the script.
- Open the downloaded oracle.ag.sql script file in an editor, and copy the contents of the script.
- On the SQL worksheet pane, paste the script content.
- Click the Run Statement icon to execute the script.

In the Query Result pane, you will see a successful message.

#### Verify the REST Module Registration in Oracle ORDS

To verify that the REST module is registered successfully with all the templates and handlers visible and executable, perform the following steps:
- Click the navigation menu icon, and select REST , and then click the Modules tab.
- Click the Refresh icon.

You should now see the oracle.ag REST module listed.
- Click the oracle.ag REST module to validate that all the associated templates and handlers are available.
Note  
  
The total number of templates and handlers associated with the REST module are displayed below the oracle.ag REST module. You must ensure that the count of templates and handlers should be greater than`0`.
- Click any registered REST module template (for instance privileges ), and click the icon, and then select Edit to view the respective handlers for the same.

Under Protected by Privilege , ensure it shows oracle.ag .
- For additional verification to check that the privilege has been added, click the Security tab, and then select Privileges .

On the Privileges page, you will see oracle.ag REST module listed.

### Configure OAuth 2.0 Client Credentials for Oracle REST Data Services (ORDS) Module

Configuring an OAuth 2.0-based authentication ensures that your REST modules are accessed securely by specific users or clients.
- Log in to the ORDS Web Developer UI using the REST-Enabled ORDS Service User Account created in Section[Create a REST-Enabled ORDS User Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-apex-configure-integration-with-oracle-apex.htm#oracle-apex-createserviceuseraccount).
- Click the navigation menu icon, and then select REST .
- On the Security tab, select OAuth Clients .

The OAuth Clients page appears.
- Click + Create OAuth Client to create an OAuth client in ORDS.

The Create OAuth Client page appears.
- On the Client Definintion tab, enter the following information:
- Name : Name for the client.
- Grant type : From the list, select the authorization grant type as CLIENT_CRED .
- Description : A short description of the client purpose.
- Support Email : Email where end users can contact the support team in the format. Example: support-team@example.com .
- Support URI : This is an optional attribute. Enter the URI where end users can contact the client for support. Example: https:// www.example.com/help/ .
- On the Roles tab, from the Available Roles list select RESTful Services and move it under Selected Roles pane to associate the client with the designated role.
- On the Allowed Origins tab, leave it blank.
- On the Privileges tab, from the Available Privileges list select the REST module oracle.ag and move it under Selected Privileges pane to assign a privilege that grants access to the ORDS module you want to protect.
Note  
  
This privilege is imported when you execute the oracle.ag.sql script and is automatically mapped to the oracle.ag REST module and its templates.
- Click Create .

The new OAuth Client registered appears on the OAuth Clients page, and a Auth client dialog box appears displaying the Client Secret value.
- Use Copy to Clipboard icon to copy the Client Secret value, and click OK .
Note  
  
You must save this Client Secret securely as it will not appear again.
- On the OAuth Clients page, locate the OAuth Client card you created in the above step to copy the Client ID by using the Copy to Clipboard icon.
Note  
  
The Client ID and Client Secret values represent the secret credentials for the OAuth client. Save these credentials securely for future use.

You can now test the secured ORDS REST service endpoint using a REST client.

## Configure

You can establish a connection between Oracle APEX and Oracle Access Governance by entering connection details. To achieve this, use the orchestrated systems functionality available in the Oracle Access Governance Console.

### Navigate to the Orchestrated Systems Page

The Orchestrated Systems page of the Oracle Access Governance Console is where you start configuration of your orchestrated system.
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

### Select system

On the Select system step of the workflow, you can specify which type of system you would like to integrate with Oracle Access Governance.

You can search for the required system by name using the Search field.
- Select Oracle Application Express (APEX) .
- Click Next .

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

### Account settings

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

### Integration settings

Enter details of the connection to your Oracle APEX system.
- 

On the Integration settings step of the workflow, enter the details required to allow Oracle Access Governance to connect to your Oracle APEX system.

Integration settings
Parameter Name Mandatory? Description
What is the host? Yes Enter the host name from the Oracle APEX URL. For the URL
```

```
Enter`apex.example.com/ords/[base_path]/[context_path]`
What is the port number? No Enter the port name
What is the authentication server url? Yes Enter the OAuth URL in the`{{host}}/ords/{{base_path}}/oauth/token`. For example`https://apex.example.com/ords/admin/oauth/token`
What is the client id? Yes Enter the client id from the ORDS application. Follow the steps:

Go to ORDS application &gt; Navigation Menu &gt; REST &gt; Security &gt; OAuth Clients
What is the client secret? Yes Enter the client secret from the ORDS application.
What is the APEX workspace? No Enter the workspace name in upper case. If provided, Oracle Access Governance manages accounts and permissions within this workspace. For example,`APEXWORK1`
- Click Add to create the orchestrated system.

### Finish Up

Finish up configuration of your orchestrated system by providing details of whether to perform further customization, or activate and run a data load.

The final step of the workflow is Finish Up .
You are given a choice whether to further configure your orchestrated system before running a data load, or accept the default configuration and initiate a data load. Select one from:
- Customize before enabling the system for data loads
- Activate and prepare the data load with the provided defaults

## Post Configuration
