# Configure Integration Between Oracle Access Governance and Atlassian JIRA
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-atlassian-jira.htm
- Fetched: 2026-09-05 03:13 CDT

# Configure Integration Between Oracle Access Governance and Atlassian JIRA

## Prerequisites

Before you install and configure a Atlassian Jira Orchestrated System, you must consider the following prerequisites and tasks.

### Certification

Check that your Atlassian Jira system is certified with Oracle Access Governance by referring to[Components Certified for Integration with Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/atlassian-jira-integration-reference.htm#jira-components-certified-for-integration-with-oracle-access-governance)for details of the versions supported.

### Create a Service User

You must create a service user to use when connecting to the target Atlassian Jira system. This user must have the following minimum recommended privileges to allow for integration.
- org-admins
- jira-users-&lt;organization&gt;
- jira-servicemanagement-users-&lt;organization&gt;
- confluence-users-&lt;organization&gt;
- confluence-user-access-admins-&lt;organization&gt;
- confluence-admins-&lt;organization&gt;

### Create an API Key

Use this task when configuring the experimental API configuration to fetch organization ID and API key.
To create API key:

- Sign in to[Atlassian Administration Console](https://admin.atlassian.com).
- On the left side pane, select the organization if you have more than one.
- Select Organization settings and then API keys .
- Select Create API key .
- Select one of the following:
- Select API keys without scopes to access all APIs
- Select API keys with scopes to access specific actions in the organization using APIs
- In the Name field, enter API key name.
- Select the Expiration date for the API key. Keys can last no longer than a year.
- Select Create to save the API key.
- Copy and save the API key and organization ID. You'll require this to configure experimental APIs in Oracle Access Governance.

### Run Get Directories in an Organization API

Use this API to get directories in an organization.
For a specific organization, retrieve all the available user directories.

- Run the following API and replace the values in the variables.

```

```

- From the response, select and copy`directoryId`. You'll need the`directoryId`while configuring experimental APIs.

## Configure

You can establish a connection between Atlassian Jira and Oracle Access Governance by entering connection details. To achieve this, use the orchestrated systems functionality available in the Oracle Access Governance Console.

### Navigate to the Orchestrated Systems Page

The Orchestrated Systems page of the Oracle Access Governance Console is where you start configuration of this orchestrated system.
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

### Select system

On the Select system step of the workflow, you can specify which type of system you would like to integrate with Oracle Access Governance.

You can search for the required system by name using the Search field.
- Select Atlassian Jira .
- Select Next .

### Add details

Add details such as name, description, and configuration mode.
On the Add Details step of the workflow, enter the details for the orchestrated system:
- Enter a name for the system you want to connect to in the Name field.
- Enter a description for the system in the Description field.
- Select Next .

### Add Owners

Add primary and additional owners to the orchestrated system to allow them to manage resources.
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

Enter details of the connection to the Atlassian Jira system.
- 

On the Integration settings step of the workflow, enter the details required to allow Oracle Access Governance to connect to the Atlassian Jira system.

Integration settings
Parameter Name Mandatory? Description
What is the host? Yes The proxy host used to connect to Atlassian Jira, for example`jira.atlassian.net`.
What is the port number? The port number of the proxy host used to connect to Atlassian Jira.
What is the username? The username of the user you will use to connect to Atlassian Jira.
What is the password? Enter password to connect to Atlassian Jira.
Do you want to use the experimental API? Select to use experimental API to ensure all necessary attributes are reliably retrieved. See[Create an API key](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-atlassian-jira.htm#create-api-key)and[Run Get Directories in an Organization API](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-atlassian-jira.htm#run-directories-api).
What are custom authentication headers? Use the API key and enter in the format:
```

```
See[Create an API key](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-atlassian-jira.htm#create-api-key).
- Select Add to create the orchestrated system.

### Finish Up

Finish up configuration of your orchestrated system by providing details of whether to perform further customization, or activate and run a data load.

The final step of the workflow is Finish Up .
You are given a choice whether to further configure your orchestrated system before running a data load, or accept the default configuration and initiate a data load. Select one from:
- Customize before enabling the system for data loads
- Activate and prepare the data load with the provided defaults

## Post Configuration
