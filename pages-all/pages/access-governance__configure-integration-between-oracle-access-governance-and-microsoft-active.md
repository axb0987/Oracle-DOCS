# Configure Integration Between Oracle Access Governance and Microsoft Active Directory
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-microsoft-active.htm
- Fetched: 2026-09-05 03:13 CDT

# Configure Integration Between Oracle Access Governance and Microsoft Active Directory

## Prerequisites

Before you install and configure a Microsoft Active Directory or Microsoft Active Directory Lightweight Directory Services (AD LDS) orchestrated system, you should consider the following prerequisites and tasks.

### Certification

- Check that your Microsoft Active Directory or Microsoft Active Directory Lightweight Directory Services (AD LDS) system is certified with Oracle Access Governance by referring to[Components Certified for Integration with Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/microsoft-ad-microsoft-active-directory-integration-reference.htm#microsoft-ad-components-certified-for-integration-with-oracle-access-governance)for details of the versions supported.

### Create a User Account

Oracle Access Governance requires a user account to access the Microsoft Active Directory or Microsoft Active Directory Lightweight Directory Services (AD LDS) systems during service operations. Depending on the system you're using, you can create the user in the managed system and assign specific permissions and roles to the user.

#### Create a User Account for Orchestrated System Operations in Microsoft Active Directory

For Microsoft Active Directory:

You can use a Microsoft Windows 2008 Server (Domain Controller) administrator account for operations. Alternatively, you can create a user account and assign the minimum required rights to the user account.

To create the Microsoft Active Directory user account for operations:

See Also: Microsoft Active Directory documentation for detailed information about performing this procedure.

- Create a group (for example, AGGroup) on the system. While creating the group, select Security Group as the group type and Global or Universal as the group scope.
Note  
  
In a parent-child domain setup, create the group in the parent domain.
- If you are setting the orchestrated system up in managed system mode then you must make this group a member of the Account Operators group.
- If you are setting the orchestrated system up in managed system mode set the following permissions for the Authenticated Users group to Allow.
- Create all child objects
- Delete all child abjects
- Assign all read permissions to this group. If there are several child domains in the forest, then sign in to each child domain and add the previous group to the Account Operators group of each child domain.
Note  
  
You assign read permissions on the Security tab of the Properties dialog box for the user account. This tab is displayed only in Advanced Features view. To switch to this view, select Advanced Features from the View menu on the Microsoft Active Directory Console.
- Create a user (for example, AGUser) on the target system. In a parent-child domain setup, create the user in the parent domain.
- Make the user a member of the group (for example, AGGroup) created in Step 1.

#### Create a User Account for Orchestrated System Operations in Microsoft Active Directory Lightweight Directory Services (AD LDS)

For Microsoft Active Directory Lightweight Directory Services (AD LDS):

You must create and use a user account that is a member of the Administrators group for performing operations.

To create the Microsoft Active Directory Lightweight Directory Services (AD LDS) user account for operations:

See Also: Microsoft Active Directory Lightweight Directory Services (AD LDS) documentation for detailed information about performing this procedure.

- Create a user account in Microsoft Active Directory Lightweight Directory Services (AD LDS).
- Set a password for the user account.
- Enable the user account by setting the`msDS-UserAccountDisabled`field to`false`.
- Ensure that the`msDS-UserDontExpirePassword`and`ms-DS-UserPasswordNotRequired`fields are available.
- Enter a value in the`userPrincipalName`field.
Note  
  
The value must be in the format`username@domain_name`, for example:`OAGuser@example.com`.
- Add the user's distinguished name (DN) to the Administrators group.
Note  
  
To create a user account for performing operations in a standalone Microsoft Active Directory Lightweight Directory Services (AD LDS) instance, follow these steps:
- Create a user account in the standalone computer.
- Add the newly created user to the AD LDS Administrators group:`CN=Administrators,CN=Roles,DC=X`.

## Configure

You can establish a connection between Microsoft Active Directory and Oracle Access Governance by entering connection details. To achieve this, use the orchestrated systems functionality available in the Oracle Access Governance Console.

### Navigate to the Orchestrated Systems Page

The Orchestrated Systems page of the Oracle Access Governance Console is where you start configuration of your orchestrated system.
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

### Select system

On the Select system step of the workflow, you can specify which type of system you would like to integrate with Oracle Access Governance.

You can search for the required system by name using the Search field.
- Select Microsoft Active Directory .
- Select Next .

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
  
The Microsoft Active Directory orchestrated system allows you to manage groups in Microsoft Active Directory using the I want to manage identity collections for this orchestrated system option. If selected, this checkbox allows you to manage Microsoft Active Directory groups from within Oracle Access Governance. Any changes made to Microsoft Active Directory groups will be reconciled between Oracle Access Governance and the orchestrated system. Similarly, any changes made in Microsoft Active Directory, will be reflected in Oracle Access Governance

### Add Owners

Add primary and additional owners to the orchestrated system to allow them to manage resources.
You can associate resource ownership by adding primary and additional owners. This drives self-service as these owners can then manage (read, update or delete) the resources that they own. By default, the resource creator is designated as the resource owner. You can assign one primary owner and up to 20 additional owners for the resources.
Note  
  
When setting up the first Orchestrated System for your service instance, you can assign owners only after you enable the identities from the[Manage Identities](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm)section. To add owners:
- Select an Oracle Access Governance active user as the primary owner in the Who is the primary owner? field.
- Select one or more additional owners in the Who else owns it? list. You can add up to 20 additional owners for the resource. You can view the Primary Owner in the list. All the owners can view and manage the resources that they own.

### Account settings

Outline details of how to manage account settings when setting up the orchestrated system including notification settings, and default actions when an identity moves or leaves the organization.
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

Enter details of the connection to the Microsoft Active Directory system.
- 

On the Integration settings step of the workflow, enter the details required to connect to the Microsoft Active Directory system.

Integration settings
Parameter Name Mandatory? Description
What is the host name? Yes The hostname or IP address for the directory you want to integrate with Oracle Access Governance, for example`example.com, 172.20.55.120`.
What is the port number? Yes The value of the TCP/IP port number used to communicate with the LDAP server. The default is`636`.
What is the principal? Yes The distinguished name with which to authenticate the LDAP server.

This is the user you created in[Create a User Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-microsoft-active.htm#microsoft-ad-createuseraccount).
What is the password? Yes The password of the target distinguished name.
Confirm password Yes Confirm the password.
What is the base context? Yes Enter a base context from which to begin searches for users and groups. For example,`OU=new,DC=test,DC=com`.
Account search filter? No

Enter LDAP search filter that each account must match to be included in search results. A few examples:
- Default value :`objectClass=*`
- Returns all person accounts where the account name ends with "a" in the account name and employee type "ADM", use
```

```

- Returns all user accounts classified as "person" with an employee type of either "EMP" or "NON", use
```

```

What is the failover server? No Enter a list of failover servers in the format`<servername>:<port>, <servername>:<port>, ...`, for example`ADExample1:636, ADExample1:636, ...`.
SSL enabled Yes Ensure that the value true is selected.

Following are the steps to configure SSL on agent:
- Use JDK to install and run an agent.
- As part of agent installation process, copy`cacerts`of JDK used for agent under agent Installation directory.
- Import AD cert to previous`cacerts`file using the command
```

```

- `Config.properties`should include the following:
```

```

What is the domain name? Yes Name of the windows domain, for example`windowsdomain.mycompany.com`.
Do you want to use the Global Catalog to perform a forest-wide object search? Yes

You can search for objects (such as users, groups, and resources) across the entire Microsoft Active Directory forest, rather than restricting queries to a single domain.
- 

No, don't use global catalog : Only retrieves objects from the parent domain, excluding any child domains in the forest.
- 

Yes, use global catalog over non ssl : Enables searching across both parent and child domains (entire forest) using a non-secure connection. This is only applicable during the data load operation using the Global port 3268.
- 

Yes, use global catalog over ssl : Enables searching across both parent and child domains (entire forest) using a secure connection. This is only applicable during the data load operation using the Global port 3269.
What are the account object classes? Yes The object class or classes that will be used for creating user objects in the LDAP tree.
What are the organization object classes? Yes Specify the object classes for organization, organizational unit, and container in Microsoft Active Directory.
What is the scope level of ldap search? Yes
- 

Search the base object (OBJECT) : Limits the search to just the specified base object. Use this when you need to retrieve or verify a single directory object.
- 

Search immediate children of a base object (ONE_LEVEL) : Searches to only the container specified in the base context, not including its child containers. For example, if the search base is`OU=abc,DC=corp,DC=com`, only the`abc`OU will be searched.
- 

Search all child objects and the base object (SUBTREE) : Searches the base object and all its descendants in the directory. For example, if the base context is set to`OU=abc,DC=corp,DC=com`, the search will cover both the`abc`OU and all child OUs.
What is the type of referrals? Yes

A referral allows queries to be routed across multiple LDAP servers. This is useful for provisioning and account management operations.
- 

Ignore referrals : Referrals would not be chased, and provisioning is performed only within the parent domain.
- 

Follow referrals automatically : All referrals are chased by Oracle Access Governance integration, supporting data load and provisioning operations across several sub domains in a single forest.
- 

Throw exception when a referral is encountered : Select this option if any referral returned by the LDAP query must be reported as an error.
What are the custom date-type target attribute names? No

Enter a list of custom target system attribute names that have a Large Integer syntax type and require transformation into an LDAP-compatible numeric format.
Is this Active Directory is a Lightweight Directory Services(AD LDS) environment? No Select this checkbox if you're configuring this as an Active Directory Lightweight Directory Services (AD LDS) instance.

By default, it's`false`.

Note: There are prerequisites for schema attributes in AD LDS. You must review[Default Supported Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/microsoft-ad-microsoft-active-directory-integration-reference.htm#microsoft-ad-supportedattributes).
- Select Add to create the orchestrated system.

### Finish Up

Finish up configuration of the orchestrated system by providing details of whether to perform further customization, or activate and run a data load.

The final step of the workflow is Finish Up .

On the Finish Up step of the workflow, you're asked to download the agent you will use to interface between Oracle Access Governance and Microsoft Active Directory. Select the Download link to download the agent zip file to the environment in which the agent will run.

After downloading the agent, follow the instructions explained in the[Agent Administration](https://docs.oracle.com/en-us/iaas/Content/access-governance/agent-administration.htm#install-oracle-access-governance-agent)article.
Finally, you're given a choice whether to further configure the orchestrated system before running a data load, or accept the default configuration and initiate a data load. Select one from:
- Customize before enabling the system for data loads
- Activate and prepare the data load with the provided defaults

## Post Configuration
