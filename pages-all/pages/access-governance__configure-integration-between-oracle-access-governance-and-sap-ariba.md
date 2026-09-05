# Configure Integration Between Oracle Access Governance and SAP Ariba
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-sap-ariba.htm
- Fetched: 2026-09-05 03:13 CDT

# Configure Integration Between Oracle Access Governance and SAP Ariba

You can establish a connection between Oracle Access Governance and SAP Ariba SaaS application as a Managed System. To configure, use Orchestrated Systems in the Oracle Access Governance Console.

## Prerequisites

Before you install and configure the SAP Ariba Orchestrated System, you should consider the following prerequisites and tasks.

### Setup to Manage SAP Ariba Accounts - Configuring a New Integration Inbound Endpoint in SAP Ariba

Configure an inbound endpoint in SAP Ariba solution to enable provisioning and access management from Oracle Access Governance.
Required Roles :
- Member of the Customer Administrator or Integration Admin group
- Group with the Administrator or Integration Admin role
An end point consists of the URL and authentication information that controls access to the end point. Configure an inbound endpoint for initiating provisioning and access management operation from Oracle Access Governance.

Configure a New Integration Inbound Endpoint in SAP Ariba
- Sign in to SAP Ariba instance with administrator credentials.
- On the SAP Ariba Administrator dashboard, click Manage &gt; Administration .
- Expand the Integration Manager option and select End Point Configuration .
- To create a new endpoint, click Create New .
An End Point Configuration - Create End Point page opens.
- In the Name field, enter a name for the end point.
- Select the type as Inbound .
- Navigate to the HTTP Authentication section , to use HTTP Basic Authentication.
- Enter the user ID in the Sign In field.
- Enter password in the Password field.
You need to provide this information to configure orchestrated system in the Oracle Access Governance Console.
- Click Save .

### Setup for Data Load - Enable an API from the SAP Ariba API Developer Portal

You can reconcile data from your SAP Ariba application to Oracle Access Governance by enabling the application API.
Required Role : A user with the Organization Admin role requests approval for API access.
A single application cannot have access to more than one API. You may have only one application per realm/API combination.

Create Application on the SAP Developer API Portal

You may skip the task if you already have an SAP Ariba application.
- Sign in to the SAP Ariba developer portal.
- Navigate to Manage Applications , then click the + plus sign.
- Enter application name and description.
- Click Submit .

The application is created and is visible under the Applications list. A unique identifier for you application, Application Key , is also generated. You require this to configure with Oracle Access Governance

Request API Access for your application
- Sign in to the SAP Ariba developer portal as a user with the Organization admin role.
- On the SAP Ariba Administrator dashboard, click Manage &gt; Administration .
- Search the desired application in the application list that you want it enabled.
- On the application setting page, click Actions &gt; Request API access .
- Complete the following application details:
- In the API Names drop-down list, choose the API name that you want to access.
- In the Realm name , choose the solution for which you want to enable the application.
- In the AN-ID field, enter your Ariba Network Identification Number (ANID).
- In the realm type, select Production or Type .
- Click Submit .

The application is sent for approval. SAP Ariba user with the Organization Admin role can approve the API access request for your application.

Generate OAuth Secret and Base64 Encoded Client ID and Secret for your Application

Once the application is approved by your administrator, you can generate OAuth Secret credentials to authenticate your API. Follow the given instructions:
- Sign in to the SAP Ariba developer portal as a user with the Organization admin role.
- On the SAP Ariba Administrator dashboard, click Manage &gt; Administration .
- Search the desired application in the application list that you want it enabled.
- On the application setting page, click Actions &gt; Generate OAuth Secret .
- In the confirmation box, click Submit . The OAuth Secret and Base64 Encoded Client and Secret are displayed.
- Copy the OAuth Secret and Base64 Encoded Client and Secret and save it to a secure location.

You'll need this to configure orchestrated system in the Oracle Access Governance Console.

### Fetch OAuth Authentication Server URL

You must fetch OAuth Server URL for your API application to establish the connection.
Required Role : A user with the Organization Admin role in SAP Ariba Developer Portal.

You'll need the Master Data Retrieval API for Sourcing API Server URL to configure orchestrated system in the Oracle Access Governance Console.

- Sign in to the SAP Ariba developer portal as a user with the Organization admin role.
- Go to Discover section, and navigate to STRATEGIC SOURCING .
- Search for Master Data Retrieval API for Sourcing .
- Copy the OAuth Server URL Prefix value, and append v2.

Example : https://&lt; OAuth Server URL &gt;/v2

### Fetch Partition ID and Variant values from WSDL

You need to fetch variant and partition ID of the realm to maintain parameter for Master Data Set.

- Sign in to the Ariba application with admin credentials.
- In the Ariba Administrator dashboard, click Manage and select Administration from drop-down.
- Expand Integration Manager and select Integration Configuration .
- Search for Import Users web service, Task name= Import User .
- Click and open the Import Users web service.
- Click View WSDL and search for vrealm in WSDL.
- If you find vrealm_1234 in WSDL, you can use vrealm_1234 as Variant and prealm_1234 as Partition.

## Configure

You can establish a connection between SAP Ariba and Oracle Access Governance by entering connection details. To achieve this, use the orchestrated systems functionality available in the Oracle Access Governance Console.

### Navigate to the Orchestrated Systems Page

Identity orchestrations are set up from the Oracle Access Governance Console. Go to the Orchestrated Systems page to integrate SAP Ariba with Oracle Access Governance.
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

### Select System

On the Select system step of the workflow, you can specify the type of system that you want to integrate.

You can search for the required system by name using the Search field.
- Select SAP Ariba .
- Click Next .

### Enter Details

In the Enter Details step, give a meaningful name to your orchestrated system, add a supporting description, and determine if you can use this system as an authoritative source or for managing permissions. For SAP Ariba, you can use Oracle Access Governance to manage permissions for identity accounts.
On the Enter Details step of the workflow, enter the details for the orchestrated system:
- Enter a name for the system you want to connect to in the What do you want to call this system? field.
- Enter a description for the system in the How do you want to describe this system? field.
Note  
  
A message is displayed on the page indicating that Oracle Access Governance can manage permissions for this system, enabling provisioning of accounts.
- Click Next .

### Add Owners

In this step, add primary and additional owners for your orchestrated system.
You can associate resource ownership by adding primary and additional owners. This drives self-service as these owners can then manage (read, update or delete) the resources that they own. By default, the resource creator is designated as the resource owner. You can assign one primary owner and up to 20 additional owners for the resources.
Note  
  
When setting up the first Orchestrated System for your service instance, you can assign owners only after you enable the identities from the[Manage Identities](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm)section. To add owners:
- Select an Oracle Access Governance active user as the primary owner in the Who is the primary owner? field.
- Select one or more additional owners in the Who else owns it? list. You can add up to 20 additional owners for the resource. You can view the Primary Owner in the list. All the owners can view and manage the resources that they own.

### Account Settings

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

For this orchestrated system, the identity accounts can only be disabled and not be deleted. So, the choices to select for mover and leaver case will be grayed out.

### Integration Settings

On the Integration settings step of the workflow, enter the configuration details required to allow Oracle Access Governance to connect to SAP Ariba.

Fill the configuration information as explained in the following table, and then click Add .

Integration Details
Field Description Example Reference
What is the realm name hosting SAP Ariba? Enter the unique realm name for your solution. Typically, you can find this in the URL in the format`s1.ariba.com/sourcing/Main/xxxxxrealm=MyRealm-T`MyRealm-T[How do I find out my realm name?](https://support.ariba.com/item/view/165937#:~:text=The%20realm%20name%20is%20what,be%20the%20exact%20realm%20name)
What is the API Key to be used for loading data? Enter the unique API application key for the application you created 123abc12345ABXX
- [API's Application Key](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-sap-ariba.htm#sap-ariba-prereq-recon)
- [Finding Your Application's Application Key and OAuth Client ID](https://help.sap.com/docs/ariba-apis/help-for-sap-ariba-developer-portal/finding-your-application-s-application-key-and-oauth-client-id)
What is Oauth Client ID? Enter client ID for your API Application. This information is visible when you generate OAuth credentials for your application. 123ABC12345acxx[Generate OAuth Credentials](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-sap-ariba.htm#sap-ariba-prereq-recon)
What is OAuth Client Secret? Enter client Secret for your API Application. This information is visible when you generate OAuth credentials for your application. 123ABC12345aTT[Generate OAuth Credentials](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-sap-ariba.htm#sap-ariba-prereq-recon)
What is the authentication server URL to validate the client? Enter the OAuth Server URL and append v2`https://< OAuth Server URL >/v2`[Fetch OAuth Authentication Server URL](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-sap-ariba.htm#sap-ariba-prereq-generateauthurl)
What is username? Enter the user id for HTTP Basic authentication ag24sapariba[Setup to Manage SAP Ariba Accounts - Configuring a New Integration Inbound Endpoint in SAP Ariba](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-sap-ariba.htm#sap-ariba-prereq-request-inbound-api-endpoint)
What is password? Enter the password for HTTP Basic authentication ag24sapariba[Setup to Manage SAP Ariba Accounts - Configuring a New Integration Inbound Endpoint in SAP Ariba](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-sap-ariba.htm#sap-ariba-prereq-request-inbound-api-endpoint)
Confirm password Re-enter the password for confirmation. ag24sapariba[Setup to Manage SAP Ariba Accounts - Configuring a New Integration Inbound Endpoint in SAP Ariba](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-sap-ariba.htm#sap-ariba-prereq-request-inbound-api-endpoint)
What is the tenancy's unique partition name? Enter the unique partition name for your realm prealm_1234[Fetch Partition ID and Variant values from WSDL](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-sap-ariba.htm#sap-ariba-prereq-partition-variant)
What is the tenancy's unique variant name? Enter the unique variant name for your realm. vrealm_1234[Fetch Partition ID and Variant values from WSDL](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-sap-ariba.htm#sap-ariba-prereq-partition-variant)

### Finish Up

Review and configure your configuration setup. You are given a choice whether to further configure your orchestrated system before running a data load, or accept the default configuration and initiate a data load.
Select one from:
- Customize before enabling the system for data loads
- Activate and prepare the data load with the provided defaults

## Post Configuration
