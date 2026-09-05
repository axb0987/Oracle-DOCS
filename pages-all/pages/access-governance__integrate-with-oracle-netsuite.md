# Integrate with Oracle NetSuite
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-oracle-netsuite.htm
- Fetched: 2026-09-05 03:15 CDT

# Integrate with Oracle NetSuite

## Prerequisites

Before you install and configure an Oracle NetSuite orchestrated system, you should consider the following pre-requisites and tasks.

### Certified Components

The system can be any one of the following:

Certified Components
Component Type Component
Target System Oracle NetSuite Release 2023.1
Target API Version NetSuite v1 and NetSuitePort_2022_1

### Supported Modes

Oracle NetSuite orchestrated system supports the following modes:
- Managed System

### Supported Operations
The Oracle NetSuite orchestrated system supports the following operations:
- Create user
- Delete user
- Reset Password
- Assign Roles to a user
- Revoke Roles from a user
- Assign Group to a user
- Remove Group from a user

### Configuring NetSuite System to Perform Operations

This is a high-level summary of the tasks to be performed on the target system before you create the application.

Pre-installation for the NetSuite connector involves performing a series of tasks on the NetSuite system.

Pre-installation involves the following tasks:
- Login to Oracle NetSuite.
- Go to Setup &gt; Company &gt; Enable Features .
- Click SuiteCloud sub-tab and enable the following features from the respective menu items.
- SuiteBuilder

Enable the following boxes:
- ITEM OPTIONS
- CUSTOM RECORDS
- ADVANCED PDF/HTML TEMPLATES
- REMOVE PERSONAL INFORMATION
- SuiteScript :
- CLIENT SUITESCRIPT
- SERVER SUITESCRIPT
- SuiteFlow
- SUITEFLOW
- SuiteGL
- CUSTOM GL LINES
- CUSTOM TRANSACTIONS
- CUSTOM SEGMENTS
- SuiteBundler
- CREATE BUNDLES WITH SUITEBUNDLER
- SuiteTalk
- SOAP WEB SERVICES
- REST WEB SERVICES
- Manage Authentication
- SUITESIGNON
- TOKEN-BASED AUTHENTICATION
- OAUTH 2.0
- SuiteCloud Development Framework
- SUITECLOUD DEVELOPMENT FRAMEWORK
- Click SAVE .

To create an integration record for an application, follow the below steps:
- 
- Go to Setup &gt; Integration&gt; Manage Integration &gt; New .
- Enter a name for your application in the Name field.
- Enter a description in the Description field, if preferred.
- Select Enabled in the State field.
- Enter a note in the Note field, if preferred.
- On the Authentication tab, check the appropriate boxes for your application:
- Token-based Authentication
- 
- TOKEN-BASED AUTHENTICATION
- TBA: AUTHORIZATION FLOW
- Define the CALLBACK URL.
- O-Auth 2.0
- AUTHORIZATION CODE GRANT
- Scope
- RESTLETS
- REST WEB SERVICES
- Provide a valid REDIRECT URI
- Click SAVE .
- Ensure to copy the Client Credentials details that will appear on the screen as it is one-time display.

For Example:

consumerKey = "fcb9ec7e7d386fab36566e9c4159bXXXXXXX2875841d828aee7e"

consumerSecret = "bd7780d4396715f5f4586d874379XXXXXX38c42a525c95f70"

To create and assign a Token Based Authentication token:
- Log in as a user with the Access Token Management permission.
- Go to Setup &gt; Users/Roles &gt; Access Tokens.
- On the Access Tokens page, click New Access Token .
- On the Access Token page:
- Select the Application Name .
- Select the User .
- Select the Role .
- The Token Name is already populated by default with a concatenation of Application Name, User, and Role. Enter your own name for this token, if preferred.
- Click Save .
- Ensure to copy the Token details that will appear on the screen as it is one-time display. For example:

tokenId = "0948d37f7XXXXXXXXXXXXXX8075";

tokenSecret = "86b7bb19cXXXXXXXXabfa0eb401e2c2c24b”

### OAuth2.0 Flow to Generate the User-Level Tokens

To generate the user-level access and refresh tokens, there are two steps you must complete manually, and these values should be provided in authToken in Oracle NetSuite Connector basic configuration for authentication.

The following steps must be completed by users who are opting in for Authorization Code Grant:

You must pass the Authorization code grant URL in the internet browser or use Postman to generate the tokens.

- Requesting the Authorization Code
Note  
  
The token URI for the developer environment is as follows:

`https://<host name>/services/rest/auth/oauth2/v1/token.`
- Enter the following URL in a browser as provided in the example.

Example:

`https://<host name> /app/login/oauth2/authorize.nl?redirect_uri={callback}&response_type=code&scope=restlets+rest_webservices&state=ykv2XLx1BpT5Q0F3MRPHb94j&client_id={ConsumerKey}`.

Replace`{ConsumerKey}`with your Consumer key / Client id and`{callback}`with your redirect URI. The URL above includes the signature scope required for the eSignature REST API.

This URL opens the Oracle NetSuite authentication screen.
- After you enter your Oracle NetSuite account email address and password and give consent for the requested scopes and then once you redirect to the login Browser Enter the user Credentials to Login and authenticate then Click on the Continue to allow Oracle NetSuite to access your information to Provide the code. The browser will redirect to your redirect URI with a long string returned for the code parameter embedded in the URL.

Request :

`https://<host name>/app/login/oauth2/authorize.nl?redirect_uri=http://example.com&response_type=code&scope=restlets+rest_webservices&state=ykv2XLx1BpT5Q0F3MRPHb94j&client_id=7e1c238e-xxxx-xxxx-xxxx-abcea08a3171`

Response :`https://example.com/?state=ykv2XLx1BpT5Q0F3MRPHb94j&role=3&entity=4622&company=TSTDRVXXXXXX&code=096835b6aced….......457b00e3c`
- Generating Refresh Tokens Using the Code Generated in Step 1
- To request a refresh token, send a POST request containing your authorization code to the NetSuite authentication service.
- Paste the values of Consumer Key and Consumer secret key as User name and Password respectively under Authorization in the Refresh token request with the type as Basic Auth in Postman.
- In addition, the refresh token request contains a set of body parameters namely grant_type and code.
- Update the key as code with value &lt;code&gt;.
Note  
  
&lt;code&gt; is nothing but the authorization code that you received from the callback in step 1.

For example, code=096835b6aced..........457b00e3c.
- Similarly, update one or more body parameter with the key as`grant_type`and value as`authorization_code`and another body parameter with key as`redirect_uri`and value as the same provided in the step 1.
- Execute the Authorize Code Grant Refresh Token request to generate an access token and a refresh token.
- In the response, you will get elements, namely, access_token, token_type, refresh_token, and expires_in.
- Copy/save the values of refresh_token.

For more information about how to get a refresh token with Auth Code Grant, see[NetSuite Applications Suite](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_158074210415.html#OAuth-2.0-Authorization-Code-Grant-Flow).

Examples:

Request :

`curl --location --request POST " https://<host name>/services/rest/auth/oauth2/v1/token"--header "Authorization: Basic N2UxYzIzOGU1Zj........GI3Njg3MzMzMTZm" --header "Content-Type: application/x-www-form-urlencoded" --data-urlencode "code=34e8dec4289........a52fe26" --data-urlencode "redirect_uri=https://example.com" --data-urlencode "grant_type=authorization_code"`

Response :

`{ "access_token":"eyJ0eXAi......mX9f7k1g", "token_type":"Bearer", "refresh_token":"eyJ0eXAi......mruC5c3A", "expires_in":3600 }`

Required element for OAuth2.0 authentication
Element Description
refresh_token

A token that is used to obtain a new access token without requiring user consent and Use this token in the Authorization header of all NetSuite API calls.

Providing Values for NetSuite Connector Basic Configuration.

After you have obtained the refresh_token value, you must provide these values in authToken under NetSuite Connector basic configuration. For information about configuration, see Configuring the NetSuite Connector. For example, eyJ0eXAi......mX9f7k1g
refresh_token value The full refresh token value that is received from authentication.

## Configure

You can establish a connection between Oracle NetSuite and Oracle Access Governance by entering connection details. To achieve this, use the Orchestrated Systems functionality available in the Oracle Access Governance Console.

### Navigate to the Orchestrated Systems Page
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

### Select system

On the Select system step of the workflow, you can specify which type of system you would like to onboard.
- Select NetSuite .
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

### Add Owners
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

On the Integration settings step of the workflow, enter the configuration details required to allow Oracle Access Governance to connect to the Oracle NetSuite instance.
- In the Host field, enter the host name of the system on which your NetSuite application is running.

Sample Value :`TSTDRVXXXXXXXX.suitetalk.api.netsuite.com`
- In the Account name field, enter the name for the account created on the NetSuite application to perform operations.

Sample Value :`TSTDRVXXXXXXXX`
- In the Consumer key field, enter the consumerKey.

Sample Value :`7e1c238e538bafXXXXXXXXbcea08a3171`
- In the Consumer secret field, enter the consumerSecret.

Sample Value :`fff0b23810704056XXXXXXXXXX0b768733316f`
- In the Token ID field, enter the token Id.

Sample Value :`3e23ecc14bc7dXXXXXXXd400e56177ed`
- In the Token secret field, enter the Token secret.

Sample Value :`cd750404ee67653aXXXXXXXXXX646422da64c`
- In the Auth URL field, Enter the URL of the authentication server that validates the client ID and client secret for your system.

Default value :`/services/rest/auth/oauth2/v1/token`
- In the Auth token field, enter the Refresh Token Values. This value can be fetched by performing OAuth code authorization flow.

Sample value :`eyJ0eXAiOiJNVCIsImFsZyI6IlJTMjU2Iiwia2lkIjoiNjgxODVmZjEtNGU1MS00Y2U5LWFmMWMtNjg5ODEyMjAzMzE3In0.AQoAAAABAAUABwCA8Kx7sbjaSAgAgDDQifS42kgCAGcjU3expKxCtXXXXXXXXXXXFAAAADQAkAAAANDdhZWE4OWQtNWViYy00NmMyLWI0YmYtNjE5MDRhMjE0MTE1IgAkAAAANDdhZWE4OWQtNWViYy00NmMyLWI0YmYtNjE5MDRhMjE0MTE1MACABwhGsbjaSDcAC1hTwTsYB0GKF0Qif6kfLg.Lk45d4mcBPIrBghYun1S2pVa0EE0XHYTU66cqWpEuPMgSieVTRgwF3wyTOSgyPuiJNf18QTJcG6js4LvVL7sPw8IJwQ6bd`
- In the Port field, enter the port number the target system is listening on.

Sample value:`443`
- Click Add to create the orchestrated system.

### Finish Up
The final step of the workflow is Finish Up , where you are given a choice whether to further configure your orchestrated system before running a data load, or accept the default configuration and initiate a data load. Select one from:
- Customize before enabling the system for data loads
- Activate and prepare the data load with the provided defaults

## Post Configuration
