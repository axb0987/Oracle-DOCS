# Configure Integration with Oracle Configure, Price, Quote (CPQ)
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/cpq-configure-integration-with-cpq.htm
- Fetched: 2026-09-05 03:13 CDT

# Configure Integration with Oracle Configure, Price, Quote (CPQ)

You can establish a connection between Oracle Access Governance and Oracle Configure, Price, Quote (CPQ) application as a Managed System. To configure, use Orchestrated Systems in the Oracle Access Governance Console.

## Prerequisites

Before you install and configure the Oracle Configure, Price, Quote (CPQ) orchestrated system. You should consider the following prerequisites and tasks.

Understanding Prerequisites Workflow
- Basic Authentication : Create a Service user with User Administrator permissions. See[Create a Service User in Oracle Configure, Price, Quote (CPQ) for Basic Authentication](https://docs.oracle.com/en-us/iaas/Content/access-governance/cpq-configure-integration-with-cpq.htm#cpq-prereq-create-service-user-cpq)
- OAuth Authentication
- [Create an Integrated Confidential Type Application](https://docs.oracle.com/en-us/iaas/Content/access-governance/cpq-configure-integration-with-cpq.htm#cpq-createintegratedapp)
- Download the Certificate and Generate the Certificate Thumbprint. See[Extract Private Key and Compute Certificate Thumbprint](https://docs.oracle.com/en-us/iaas/Content/access-governance/cpq-configure-integration-with-cpq.htm#cpq-create-signing-certificate-1)or[Saving the IdP X509 Certificate](https://docs.oracle.com/en/cloud/paas/identity-cloud/idcsc/oraclecpqcloud.html#Configuring-SSO-for-CPQ-Cloud).
- Enable OAuth Provider in Oracle Configure, Price, Quote (CPQ). See[Configure OAuth Provider in Oracle Configure, Price, Quote (CPQ) Integration Center](https://docs.oracle.com/en-us/iaas/Content/access-governance/cpq-configure-integration-with-cpq.htm#cpq-prereq-enable-oauth-cpq)
- Create a Service User in OCI IAM and associate Service User in Oracle Configure, Price, Quote (CPQ). See[Create a Service user in Oracle Configure, Price, Quote (CPQ) for OCI IAM Integration](https://docs.oracle.com/en-us/iaas/Content/access-governance/cpq-configure-integration-with-cpq.htm#cpq-prereq-enable-cpq-ociiam-integrations)

### Create a Service User in Oracle Configure, Price, Quote (CPQ) for Basic Authentication

Create a new service user in Oracle Configure, Price, Quote (CPQ) as a User Administrator.
Create a service user account in the Oracle Configure, Price, Quote (CPQ) cloud account and assign Full Access and User Administrator user. This is required for Basic Authentication.

- Go to the Oracle Configure, Price, Quote (CPQ) cloud account.
- From the user profile settings, select Users .
- Enter the user details, as follows:
- Login : User name for this user.
- Password : Enter the password.
- Email : Enter the email address.
- First Name : Enter user's first name
- In the User Settings section, in the Type list, select FullAccess .
- Click Add . The group
Create Groups with User Access
- From the user profile settings, select Groups .
- Select Add . The Group Administration page is opened.
- Enter Group Name and Variable Name .
- In the Type list, select Administrator .
- In the Available Access list, select Users with all permissions selected
Assign Required Permissions and Groups to the Service User
- Search and open the service user.
- In the Permissions option, select User Administrator .
- From the Administrator Group List , assign the custom group created above.
- Select Update .

### Create an Integrated Confidential Type Application

To create an integrated application of Confidential type in OCI IAM, you must have the Identity Domain Administrator role.

- Navigate to Identity &amp; Security , and click Domains .
- Select Domains .
- Click the Integrated applications tab.
- Click Add application .
- Select Confidential Application tile, and then click Launch workflow .
- In the Details page, enter the following:
- Enter name and description for the confidential application.
- Click Submit .
Edit OAuth configurations
- Select the OAuth configuration tab.
- Select Edit OAuth configuration .
Resource server configuration
- Select Configure this application as a resource server now .
- Enter Primary audience:[https://cpq12354.cpq.[region_identifier].ocs.oraclecloud.com](https://cpqqa254.cpq.us-phoenix-1.ocs.oc-test.com).
Scopes
- Enable the Add scopes button.
- Add and enter scope as`/api`, enter display name and description.
- Click Add .
Client configuration
- Select Configure this application as a client now .
- Select the following grant types: and Refresh token grant types:
- JWT assertion
- Client Credentials
- Authorization code
- Enter the Redirect URL in the following format:`https://cpq12354.cpq.[region_identifier].ocs.oraclecloud.com/ sso/openid_connect_redirect.jsp .`
- Enter the Logout URL in the following format:`https://cpq12354.cpq.[region_identifier].ocs.oraclecloud.com/ logout.jsp`
- Enter the Post-logout URL in the following format:`https://cpq12354.cpq.[region_identifier].ocs.oraclecloud.com/ sso/openid_connect_request.jsp`
- Choose Trusted as the Client type option.
- Import the certificate. See[Configure OAuth Provider in Oracle Configure, Price, Quote (CPQ)](https://docs.oracle.com/en-us/iaas/Content/access-governance/cpq-configure-integration-with-cpq.htm#cpq-prereq-enable-oauth-cpq).
- Click Submit .
- Activate the application, click the Actions icon and then select Activate . The status should change from Inactive to Active .
Copy and save the Client ID .

### Extract Private Key and Compute Certificate Thumbprint

Use certificate thumbprint, private key, public certificate from a Java keystore (.jks) file.
Retrieve the Certificate Thumbprint

Generate the certificate thumbprint from the downloaded certificate.

- Export public certificate from Java keystore file (.jks)

```

```

Obtain`cpq.keystore`securely from your CPQ system administrator or backend server.
- Enter the keystore password.
- For compatibility, convert JKS to PKCS12 using:

```

```

- Enter the destination keystore new password and the source keystore password.
- Extract the Private Key from PKCS12

```

```

- Enter the password set in Step 4.
- Convert Public Certificate from DER to PEM Format

```

```

- Compute Certificate Thumbprint (SHA-1, base64url)

```

```

### Configure OAuth Provider in Oracle Configure, Price, Quote (CPQ) Integration Center

Configure OAuth assertion in the Oracle Configure, Price, Quote (CPQ) integration center.

- Go to the Oracle Configure, Price, Quote (CPQ) cloud account.
- Select the Admin icon. The Administration Platform is opened.
- On the Integration Platform section, select Integration Center .
- On the left pane, select OAuth Provider - Identity Cloud Service
- Configure the OAuth details, as follows:

Option Description
Issuer Enter the OCI IAM URL.
```

```

Tenant URL Enter the Domain URL. To find your Domain URL, see[Finding an Identity Domain URL](https://docs.oracle.com/iaas/Content/Identity/api-getstarted/locate-identity-domain-url.htm)
```

```

Token Endpoint Enter OAuth endpoint
```

```

Scope Enter the scope of the OCI IAM Domain
```

```

Certification Setup Enter the following:
- JWKS Endpoint : Enter JSON Web Key Set Endpoint. For example,`/admin/v1/SigningCert/jwk`
- Enter the integrated application client ID
Note  
  
Contact your business operation team to fetch certification details for your service instance.
Client App Configuration Enter the integrated application client ID.
- Download the CPQ Public Key.
Import certificate in the Integrated Application
- In the[Integrated application](https://docs.oracle.com/en-us/iaas/Content/access-governance/cpq-configure-integration-with-cpq.htm#cpq-createintegratedapp), click Edit OAuth Configuration
- Click Import certificate and import the downloaded certificate.
- Submit and save it.

### Create a Service user in Oracle Configure, Price, Quote (CPQ) for OCI IAM Integration

Create a service user in Oracle Configure, Price, Quote (CPQ) to integrate with OCI IAM.
In the Oracle Configure, Price, Quote (CPQ) console, from the Admin menu, select System Properties . Set`BMContext.user_management_delegated_to_idp = true`. You can also contact Oracle Support for Enabling User Management Delegation to IDP.

Create a Service User in OCI IAM
- [Create a User](https://docs.oracle.com/iaas/Content/Identity/users/create-user-accounts.htm)
Create a corresponding Service User for enabling provisioning in Oracle Configure, Price, Quote (CPQ)
- Go to the Oracle Configure, Price, Quote (CPQ) cloud account.
- From the user profile settings, select Users .
- Enter the user details, as follows:
- Login : User name for this user. It should match the OCI IAM username.
- Password : Enter the password.
- Email : Enter the email address.
- First Name : Enter user's first name
- In the User Settings section, in the Type list, select FullAccess .
- Select Enabled for SSO .
- Click Add .
Assign Required Permissions and Groups to the Service User
- Search and open the service user.
- In the Permissions option, select User Administrator and Web Services Only .
- Select Update .
Assign Required Permissions and Groups to the Service User
- Open the service user that you just created.
- Select User Integration .
- In the CRM/IdP tab, enter the login details of the service user.

## Configure

You can establish a connection between Oracle Configure, Price, Quote (CPQ) and Oracle Access Governance by entering connection details. To achieve this, use the orchestrated systems functionality available in the Oracle Access Governance Console.

### Navigate to the Orchestrated Systems Page

The Orchestrated Systems page of the Oracle Access Governance Console is where you start configuration of your orchestrated system.
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

### Select system

On the Select system step of the workflow, you can specify which type of system you would like to integrate with Oracle Access Governance.

You can search for the required system by name using the Search field.
- Select Oracle Configure, Price, Quote (CPQ) .
- Click Next .

### Add details

Add details such as name, description, and configuration mode.
On the Add Details step of the workflow, enter the details for the orchestrated system:
- Enter a name for the system you want to connect to in the Name field.
- Enter a description for the system in the Description field.
- For this orchestrated system, Oracle Access Governance can manage permissions
- Click Next .

### Account settings

Manage account settings when setting up your orchestrated system including notification settings, and default actions when an identity moves or leaves your organization.
- Select to allow Oracle Access Governance to create new accounts when a permission is requested, if the account does not already exist. By default, the account is be created if it doesn't exist, when a permission is requested. If the option is cleared, then permissions can only be provisioned where the account already exists in the orchestrated system. If permission is requested where no user exists then the provisioning operation is failed.
- 
Select where and who to send notification emails when an account is created. The default setting is User . You can select one, both, or none of these options. If you select no options then notifications is not sent when an account is created.
- User
- User manager
- When an identity leaves your enterprise you must remove access to their accounts. You can select what to do with the account when this happens. Select one of the following options:
- Delete
- Disable
- No action
Note  
  
These options are displayed only if supported in the orchestrated system type being configured. For example, if Delete isn't supported, then Disable and No action options are displayed.
- When all permissions for an account are removed, for example when moving from one department to another, you might need to adjust what accounts the identity has access to. You can select what to do with the account when this happens. Select one of the following options:
- Delete
- Disable
- No action
Note  
  
These options are displayed only if supported in the orchestrated system type being configured. For example, if Delete isn't supported, then Disable and No action options are displayed.
- If you want Oracle Access Governance to manage accounts created directly in the orchestrated system you can select the Manage accounts that are not created by Access Governance option. This reconciles accounts in the managed system and allows to manage them from Oracle Access Governance.

### Add Owners

Add primary and additional owners to your orchestrated system to allow them to manage resources.
You can associate resource ownership by adding primary and additional owners. This drives self-service as these owners can then manage (read, update or delete) the resources that they own. By default, the resource creator is designated as the resource owner. You can assign one primary owner and up to 20 additional owners for the resources.
Note  
  
When setting up the first Orchestrated System for your service instance, you can assign owners only after you enable the identities from the[Manage Identities](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm)section. To add owners:
- Select an Oracle Access Governance active user as the primary owner in the Who is the primary owner? field.
- Select one or more additional owners in the Who else owns it? list. You can add up to 20 additional owners for the resource. You can view the Primary Owner in the list. All the owners can view and manage the resources that they own.

### Integration settings

Enter details of the connection to your Oracle Configure, Price, Quote (CPQ) system.
- On the Integration settings step of the workflow, enter the details.

Integration settings
Authentication Parameter Name Description
Basic Authentication Do you want to use basic authentication? Select the checkbox to allow authentication using user credentials.

- Basic Authentication
- OAuth Host Name Enter the host name/instance value from the URL. For example, in the URL`https://cpq12354.cpq.[region_identifier].ocs.oraclecloud.com/ui`, enter
```

```

- Basic Authentication
- OAuth Username Enter username
Basic Authentication Password Enter password
Basic Authentication Confirm Password Confirm your password
OAuth

Authentication Server URL Client ID of the OCI IAM confidential application.
Client ID Client ID of the OCI IAM confidential application.
Private Key Enter the contents in the private key (.PEM) file.

Certificate fingerprint Enter the value between &lt;dsign:X509Certificate&gt; and &lt;/dsign:X509Certificate&gt; from the IdP metadata file. See[Saving the IdP X509 Certificate](https://docs.oracle.com/en/cloud/paas/identity-cloud/idcsc/oraclecpqcloud.html#Configuring-SSO-for-CPQ-Cloud)or Generate one for your certificate, see[Generate Certificate Thumbprint](https://docs.oracle.com/en-us/iaas/Content/access-governance/cpq-configure-integration-with-cpq.htm#cpq-create-signing-certificate-1).

What is the scope? Enter applicable scopes allowed to your confidential application. For example:
```

```

- Click Add to create the orchestrated system.

### Finish Up

Finish up configuration of your orchestrated system by providing details of whether to perform further customization, or activate and run a data load.

The final step of the workflow is Finish Up .
You are given a choice whether to further configure your orchestrated system before running a data load, or accept the default configuration and initiate a data load. Select one from:
- Customize before enabling the system for data loads
-
