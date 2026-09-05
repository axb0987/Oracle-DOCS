# Configure Integration with SAP User Management (UM)
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/sap-user-configure-integration-with-sap-user-management-um.htm
- Fetched: 2026-09-05 03:16 CDT

# Configure Integration with SAP User Management (UM)

## Prerequisites

Before you install and configure a SAP User Management (UM) Orchestrated System, you should consider the following prerequisites and tasks.

### Certification

- Check that your SAP User Management (UM) system is certified with Oracle Access Governance by referring to[Components Certified for Integration with Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/sap-user-sap-user-management-um-integration-reference.htm#sap-user-components-certified-for-integration-with-oracle-access-governance)for details of the versions supported.

### Create a Service User Account

Oracle Access Governance requires a user account to access the SAP User Management (UM) system during service operations. Depending on the system you are using, you can create the user in your managed system and assign specific groups, roles, parameters, and profiles to the user.

#### Create a Service User Account for Orchestrated System Operations in SAP User Management (UM)

To create the SAP User Management (UM) user account for operations:

- Create a CPIC User with the`S_IDOC_ALL`profile.
- Add the following authorizations along with the corresponding default parameter values:
- S_RFC
- S_TABU_DIS
- S_TABU_NAM
- S_USER_AGR
- S_USER_AUT
- S_USER_GRP
- S_USER_PRO
- S_USER_SAS
- S_USER_SYS
- Modify the parameter values as follows:

For S_RFC
- ACTVT:`16`
- RFC_NAME:`*`
- RFC_TYPE:`FUGR`

For S_TABU_DIS
- ACTVT:`03,02`
- DICBERCLS:`SUSR,*`

For S_TABU_NAM
- ACTVT:`03,02`
- TABLE:`USH*,USR*,USZ*,AGR_TEXTS`

For For S_USER_AGR
- ACTVT:`03,22,02`
- ACT_GROUP:`*`

For S_USER_AUT
- ACTVT:`03`
- AUTH:`*`
- OBJECT:`*`

For S_USER_GRP
- ACTVT:`01,02,03,05,06,08,22,78,PP`
- CLASS:`*`

For S_USER_PRO
- ACTVT:`03,22`
- PROFILE:`*`

For S_USER_SAS
- ACTVT:`01,06,22`
- ACT_GROUP:`*`
- CLASS:`*`
- PROFILE:`*`
- SUBSYSTEM:`*`

For S_USER_SYS
- ACTVT:`78`
- SUBSYSTEM:`*`

## Configure

You can establish a connection between SAP User Management (UM) and Oracle Access Governance by entering connection details. To achieve this, use the orchestrated systems functionality available in the Oracle Access Governance Console.

### Navigate to the Orchestrated Systems Page

The Orchestrated Systems page of the Oracle Access Governance Console is where you start configuration of your orchestrated system.
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

### Select system

On the Select system step of the workflow, you can specify which type of system you would like to integrate with Oracle Access Governance.

You can search for the required system by name using the Search field.
- Select SAP User Management (UM) .
- Click Next .

### Add details

Add details such as name, description, and configuration mode.
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
Note  
  
The SAP User Management (UM) orchestrated system allows you to manage groups in SAP User Management (UM) using the I want to manage identity collections for this orchestrated system option. If selected, this checkbox allows you to manage SAP User Management (UM) groups from within Oracle Access Governance. Any changes made to SAP User Management (UM) groups will be reconciled between Oracle Access Governance and the orchestrated system. Similarly, any changes made in SAP User Management (UM), will be reflected in Oracle Access Governance

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

Enter details of the connection to your SAP User Management (UM) system.
- 

On the Integration settings step of the workflow, enter the details required to allow Oracle Access Governance to connect to your SAP User Management (UM) system.

Integration settings
Parameter Name Mandatory? Description
What is the SAP host? Yes The hostname or IP address for the directory you want to integrate with Oracle Access Governance, for example`example.com, 172.20.55.120`.
What is the SAP client? Yes The value of the SAP User Management (UM) client setting. For example,`800`.
What is SAP master system? Yes Enter the RFC Destination value that is used for identification of the SAP User Management (UM) system. This value must be same as that of the Logical System name.

Sample value:`OH2CLNT800`

The master system value is a combination of`< SYSTEM_ID >CLNT< CLIENT_NUM >`.

In the preceding sample value,`OH2`is the System ID of the managed system and`800`is the client number.
What is the SAP instance number? Yes It is a two-digit identifier assigned to a SAP User Management (UM) instance during installation.

For example`00`.
What is the destination used to interact with the SAP system? Yes Enter a unique value to establish a connection with the SAP User Management (UM) system.

For example:`dest123`.
What is the username to log into the SAP? Yes Enter the user name of the SAP User Management (UM) system.
What is the password of the user used to log into the SAP? Yes Enter the password of the SAP User Management (UM) System.
Confirm password Yes Confirm the password.
What is the dummy password value? Yes Enter the dummy password that you want the managed system to use during a Create User provisioning operation. The managed system first sets the password as this value and then changes it to the password specified on the process form.
Confirm password Yes Confirm the password.
What is the SAP router string? No Use this parameter for a system protected by a firewall.
Which type of roles to be reconciled? Yes Select the type of role to reconcile from SAP User Management (UM) system.
- Both : Fetches both Single roles and Composite roles from the target.
- Single roles : Fetches only Single roles from the target system.
- Composite roles : Fetches only Composite roles from the target.
Custom jar details Yes Provide the details of the sapjco3.jar file in the form of &lt;`JAR NAME`&gt;::&lt;`JAR CHECKSUM`&gt;
- Click Add to create the orchestrated system.

### Finish Up

Finish up configuration of your orchestrated system by providing details of whether to perform further customization, or activate and run a data load.

The final step of the workflow is Finish Up .

On the Finish Up step of the workflow, you are asked to download the agent you will use to interface between Oracle Access Governance and SAP User Management (UM). Select the Download link to download the agent zip file to the environment in which the agent will run.

After downloading the agent, follow the instructions explained in the[Agent Administration](https://docs.oracle.com/en-us/iaas/Content/access-governance/agent-administration.htm#install-oracle-access-governance-agent)article.

Pre-Startup Configuration for Agent Initialization

Before starting the agent, ensure that you have added the custom JAR to the agent and completed the following configurations in the config.json and config.properties files:

To add custom JAR :
- Navigate to the custom JAR folder.

`<AGENT_HOME>/<PERSISTENT_VOLUME_LOCATION>/data/customJars`
- Add the SAPJco JAR file.

For config.json :
- Navigate to the default location of the config.json file.

`<AGENT_HOME>/<PERSISTENT_VOLUME_LOCATION>/data/conf/config.json`
- Update the following property:

`"numberOfOperationsWorkerThread": 1,`

For config.properties :
- Navigate to the default location of the config.properties file.

`<AGENT_HOME>/<PERSISTENT_VOLUME_LOCATION>/data/conf/config.properties`
- Update the following property:

`idoConfig.numberOfOperationsWorkerThread=1`

After updating the configuration files, you can start the agent.
Finally, you are given a choice whether to further configure your orchestrated system before running a data load, or accept the default configuration and initiate a data load. Select one from:
- Customize before enabling the system for data loads
- Activate and prepare the data load with the provided defaults

## Post Configuration
