# Integrate with Microsoft Entra ID
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-microsoft-entra-id.htm
- Fetched: 2026-09-05 03:14 CDT

# Integrate with Microsoft Entra ID

## Prerequisites

Before you install and configure a Microsoft Entra ID orchestrated system, you must consider the following prerequisites and tasks.

### Certified Components

The Microsoft Entra ID system can be any one of the following:

Certified Components
Component Type Component
System
- Microsoft Entra ID
- Microsoft Entra ID with Business-to-Consumer (B2C) enabled tenant
System API Version
- Microsoft Entra ID
- Microsoft Graph API v1.0
- Microsoft Authentication API version v2.0 (OAuth 2.0)

### Supported Modes

Microsoft Entra ID orchestrated system supports the following modes:
- Authoritative Source
- Managed System

### Supported Operations
The Microsoft Entra ID orchestrated system supports the following operations on Microsoft Entra ID:
- Create user
- Delete user
- Reset Password
- Assign Roles to a user
- Revoke Roles from a user
- Assign Licences to a user
- Remove Licences from a user
- Assign SecurityGroup to a user
- Remove SecurityGroup from a user
- Assign OfficeGroup to a user
- Remove OfficeGroup from a user

### Default Supported Attributes
The Microsoft Entra ID orchestrated system supports the following default attributes. These attributes are mapped depending on the direction of the connection, for example:
- Data being ingested by Oracle Access Governance from Microsoft Entra ID:`User.givenName`will map to`Identity.firstName`
- Data being provisioned into Microsoft Entra ID from Oracle Access Governance:`account.lastName`will map to`User.surname`

Default Attributes - Authoritative Source
Microsoft Entra ID/Microsoft Entra ID B2C-Enabled Tenant Entity Attribute Name On Managed System Oracle Access Governance Identity Attribute Name Oracle Access Governance Identity Attribute Display Name
User id uid Unique Id
mailNickname name Employee user name
userPrincipalName email Email
givenName firstName First name
surname lastName Last name
displayName displayName Name
usageLocation usageLocation Locality name
manager managerLogin Manager
preferredLanguage preferredLanguage Preferred language
accountEnabled status Status
Additional Attributes for B2C-enabled Tenant identities identities.issuerAssignedId identities
identities identities.signInType Sign in type
identities identities.issuer Issuer
passwordPolicies passwordPolicy Password policy

Default Attributes - Managed System
Microsoft Entra ID/Microsoft Entra ID B2C-Enabled Tenant Entity Attribute Name On Managed System Oracle Access Governance Account Attribute Name Oracle Access Governance Account Attribute Display Name
User id uid Unique Id
userPrincipalName name User login
givenName firstName First name
surname lastName Last name
displayName displayName Name
mailNickname mailNickname Mail nick name
mail email Email
usageLocation usageLocation Usage location
city city City
country country Country
manager managerLogin Manager
passwordProfile.forceChangePasswordNextSignIn forceChangePasswordNextSignIn Change password on next logon
preferredLanguage preferredLanguage Preferred language
userType userType Employee type
accountEnabled status Status
password password Password
Additional Attributes for B2C-enabled Tenant
identities.issuerAssignedId issuerAssignedId Issuer assigned id
identities.signInType signInType Signin type
identities.issuer issuer Issuer
passwordPolicies passwordPolicy Password Policy
Licenses licenses as entitlement

### Microsoft Enterprise Application Configuration and Settings
Before you can establish a connection, you need to perform the following tasks in your Microsoft Entra ID Admin Center for the Enterprise application:
- Create and register an enterprise application that you want to integrate with Oracle Access Governance. For more information, refer[Microsoft documentation](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app).
- Generate a client secret for the application
- Grant the following delegated and application permissions for the Microsoft Graph API:

Delegated Permission
- Directory.ReadWrite.All
- Group.ReadWrite.All
- GroupMember.ReadWrite.All
- User.Read
- User.ReadWrite

Application Permission

- Directory.ReadWrite.All
- Group.ReadWrite.All
- GroupMember.ReadWrite.All
- User.ReadWrite.All
- RoleManagement.ReadWrite.Directory
- Select the Grant Admin Consent button to provide directory-wide full permissions to perform the related API tasks for an integrated system

For more information, see the[Microsoft documentation](https://learn.microsoft.com/en-us/graph/notifications-integration-app-registration).

### Default Matching Rules

To map accounts to identities in Oracle Access Governance you need to have a matching rule for each orchestrated system.The default matching rule for the Microsoft Entra ID orchestrated system is:

Default Matching Rules
Mode Default Matching Rule
Authoritative Source

Identity matching checks if incoming identities match an existing identity or are new.

For Microsoft Entra ID/For Microsoft Entra ID B2C-Enabled Tenant:

Screen value :

`User login = Email`

Attribute name :

`Account.userPrincipalName = Identity.name`
Managed System

Account matching checks if incoming accounts match with existing identities.

For Microsoft Entra ID:

Screen value :

`User login = Email`

Attribute name :

`Account.userPrincipalName = Identity.name`

For Microsoft Entra ID B2C-Enabled Tenant:

Screen value :

`Email = Email`

Attribute name :

`Account.mail = Identity.email`

## Configure

You can establish a connection between Microsoft Entra ID (formerly Azure Active Directory) and Oracle Access Governance by entering connection details. To achieve this, use the orchestrated systems functionality available in the Oracle Access Governance Console.

### Navigate to the Orchestrated Systems Page
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

### Select system

On the Select system step of the workflow, you can specify which type of system you would like to onboard. You can search for the required system by name using the Search field.
- Select Microsoft Entra ID .
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
Note  
  
The Microsoft Entra ID orchestrated system allows you to manage groups in Microsoft Entra ID using the I want to manage identity collections for this orchestrated system option. If selected, this checkbox allows you to manage Microsoft Entra ID groups from within Oracle Access Governance. Any changes made to Microsoft Entra ID groups will be reconciled between Oracle Access Governance and the orchestrated system. Similarly, any changes made in Microsoft Entra ID, will be reflected in Oracle Access Governance

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

## Integration Settings

On the Integration Settings step of the workflow, choose how you want to provide the access credentials that Oracle Access Governance uses to connect to Microsoft Entra ID:
- You can enter and store the credentials in Oracle Access Governance
- You can retrieve the credentials from an OCI Vault secret Using an OCI Vault secret provides centralized secret management, reduces credential exposure, and provides controlled access through OCI IAM policies.
Note  
  
You can migrate Microsoft Entra ID orchestrations that previously stored credentials in Oracle Access Governance to use an OCI Vault secret instead. See[Migrate Credentials to OCI Vault](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-microsoft-entra-id.htm#migrate-integration-settings-to-oci-vault).

### Integration Settings in Oracle Access Governance

On the Integration Settings step of the workflow, enter the configuration details required to allow Oracle Access Governance to connect to Microsoft Entra ID.
- In the Host field, enter the host name of the machine hosting your Managed System. For example, for the Microsoft Graph API, you may enter graph.microsoft.com
- In the Port field, enter the port number at which the system will be accessible. By default, Microsoft Entra ID uses port 443.
- To provide access credentials, select Credentials received and stored in Access Governance .
- Enter the URL of the authentication server that validates the client ID and client secret for your Managed System in the Authentication Server Url field. For example, to authenticate the application using the OAuth 2.0 API, enter in the following syntax
```

```
To know how to fetch your Primary domain or tenant ID, refer[Microsoft documentation](https://learn.microsoft.com/en-us/partner-center/find-ids-and-domain-names#find-the-microsoft-entra-tenant-id-and-primary-domain-name).
- Enter the client identifier (a unique string) issued by the authorization server to your client system during the registration process, into the Client ID field. The client ID, also known as Application ID, is obtained when registering an application in Microsoft Entra ID. This value identifies your application in the Microsoft identity platform. For more details refer to[Microsoft documentation](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/application-properties).
- In the Client secret field, enter the secret ID value to authenticate the identity of your system. You need to create a new client secret for your system and enter the value in this field. Only use this value when you are not using private key for authentication.
Note  
  
You must note or copy this client secret value, as you won't be able access or view it once you leave the page. For more details refer[Microsoft documentation](https://learn.microsoft.com/en-us/graph/notifications-integration-app-registration#app-certificates-and-secrets).
- Enter PEM private key into the Private key field, only when you are not using Client secret for authentication.

For test purposes only, you can generate a self-signed certificate using the following steps:
- Create an encrypted private key which you will load into the Entra ID instance.
```

```

- Decrypt the private key to create a .pem (decrypted_key.pem in the example) file which you can enter as the value for the Private key when configuring Oracle Access Governance.
```

```

- Optionally, if your private key is in PKCS1 format, convert the decrypted key for PKCS8 format which is supported in Oracle Access Governance.
```

```

- Enter the value for the certificate fingerprint (X509) in the Certificate fingerprint , only when you're not using Client secret for authentication.

To obtain the certificate fingerprint use the following steps:
- Convert the hex value of the certificate thumbprint to binary.
```

```

- Convert the binary thumbprint to base64 which can be used in the Certificate fingerprint field.
```

```

- Select the Is this B2C tenant enabled environment? checkbox to ingests identity attributes ( Issuer , Signin type , Issuer id ) for each user. If any of the identity attributes is returned null or empty, then Oracle Access Governance skips data load for that user and doesn't ingest the user.
- In What is the request timeout? field, enter the maximum amount of time to wait for a server to respond to a request.
- Click Add to create the orchestrated system.

### Integration Settings From OCI Vault

Use this option to retrieve the access credentials from OCI Vault instead of entering and storing the credentials in Oracle Access Governance. Before you configure this option, create an OCI Vault, encryption key, and secret that contain the credentials for Microsoft Entra ID. See[Creating a Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_create_a_new_vault.htm).

The vault secret contains the following details:`authenticationServerUrl`,`clientId`,`clientSecret`,`privateKey`, and`thumbPrint`.
Note  
  

- When using client credentials, the`private key`and`thumbPrint`values must be empty strings. For example:
```

```

- When using certificate authentication, the`clientSecret`value must be an empty string.
- In the Host field, enter the host name of the machine hosting your Managed System. For example, for the Microsoft Graph API, you may enter graph.microsoft.com
- In the Port field, enter the port number at which the system will be accessible. By default, Microsoft Entra ID uses port 443.
- To provide access credentials, select From an OCI vault secret .
- In the secretOCID field, enter the OCI Secret OCID for the service account credentials used to connect to the target system.
- In the OCI tenancy field, enter the tenancy OCID where the vault with service account credentials resides.
- Select the Is this B2C tenant enabled environment? checkbox to ingests identity attributes ( Issuer , Signin type , Issuer id ) for each user. If any of the identity attributes is returned null or empty, then Oracle Access Governance skips data load for that user and doesn't ingest the user.
- In What is the request timeout? field, enter the maximum amount of time to wait for a server to respond to a request.
- Expand Required OCI Policies . Providing the tenancy OCID and secret OCID generates the required IAM policy. For information about creating policies, see[Creating a Policy](https://docs.oracle.com/iaas/Content/Identity/policymgmt/managingpolicies_topic-To_create_a_policy.htm).
- Copy the generated policy statements and create them in the root compartment of the Oracle Access Governance tenancy where you created the vault.
- Select Test integration to validate integration.
- Select Add to create the orchestrated system.

## Finish up

Finally, you are given a choice whether to further configure your orchestrated system before running a data load, or accept the default configuration and initiate a data load. Select one from:
- Customize before enabling the system for data loads
- Activate and prepare the data load with the provided defaults

## Post Configuration

There are no post install steps associated with a Microsoft Entra ID system.

## Migrate Credentials to OCI Vault

You can migrate Microsoft Entra ID orchestrations that previously stored credentials in Oracle Access Governance to use an OCI Vault secret instead.

Before you can migrate credentials, you must create an OCI Vault, encryption key, and secret that contain the credentials for Microsoft Entra ID. See[Creating a Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_create_a_new_vault.htm).

The vault secret contains the following details:`authenticationServerUrl`,`clientId`,`clientSecret`,`privateKey`, and`thumbPrint`.
Note  
  

- When using client credentials, the`private key`and`thumbPrint`values must be empty strings. For example:
```

```

- When using certificate authentication, the`clientSecret`value must be an empty string.
- Access and the integration settings for the Microsoft Entra ID orchestrated system with credentials in Oracle Access Governance and select Learn more about migrating .
- In the OCI tenancy field, enter the tenancy OCID where the vault with service account credentials resides.
- In the secretOCID field, enter the OCI Secret OCID for the service account credentials used to connect to the target system.
- Expand Required OCI Policies . Providing the tenancy OCID and secret OCID generates the required IAM policy. For information about creating policies, see[Creating a Policy](https://docs.oracle.com/iaas/Content/Identity/policymgmt/managingpolicies_topic-To_create_a_policy.htm).
- Copy the generated policy statements and create them in the root compartment of the Oracle Access Governance tenancy where you created the vault.
- Select Test integration to validate integration.
-
