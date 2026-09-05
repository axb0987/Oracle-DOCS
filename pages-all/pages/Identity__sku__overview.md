# IAM Identity Domain Types
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm
- Fetched: 2026-09-05 02:29 CDT

# IAM Identity Domain Types

Learn about identity domain types and the features and limits associated with each.

An IAM identity domain is deployed with one of several identity domain types. Each identity domain type is associated with a different set of features and object limits. Use this information to decide which identity domain type is appropriate for what you want to do.

This section summarizes:
- The different identity domain types, see[Understand Identity Domain Types](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#understand).
- The features associated with each type, see[Feature Availability for Identity Domain Types](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#features).
- The number of different types of object for each identity domain type, see[IAM Identity Domain Object Limits](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#iam-object-limits).
- Supported data types for custom attributes and their limits, see[Data Types for Custom Attributes](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#data-types-custom-attr).
- Rate limiting for APIs for different identity domain types, see[API Rate Limits](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#api-rate-limits).
- Meters used for different identity domain types, see[Meters for Identity Domain Types](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#meters).
- How to change to a different identity domain type, see[Changing your Identity Domain Type](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#changing-domain-type).

This section has information about identity domains and the various features and limits associated with each identity domain type. For information about IAM tenancy level limits, see[IAM With Identity Domains Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#iam-service-limits).

## Understand Identity Domain Types

IAM has several different identity domain types to address different organizational needs. Start here to understand which suits your requirements best, and which type to select when you create an identity domain.

Here's a summary of the identity domain types. Decide which provides the best fit for your requirements and check the features and limits below to that you get with that identity domain type to select the identity domain type that's right for you.

### Free

When you create an OCI tenancy, you're automatically provisioned with a Free identity domain. This domain type allows you to use the IAM service to manage access to OCI Infrastructure and Platform resources. Use this domain type to learn about the IAM service, and to manage access to OCI IaaS and PaaS resources. This domain type should include everything you need to manage OCI. But if you require higher limits or additional features, you can change to a different identity domain type.

Example Use case: Your organization uses Oracle Cloud and your cloud administrators need secure access to manage subscribed OCI services.

### Oracle Apps

Some Oracle PaaS services and SaaS applications offer their customers an Oracle Apps identity domain which allows you to use the IAM service to manage access to the subscribed service. Usually, the identity domain is either provided by the service at provisioning time, or a preexisting domain will automatically become an Oracle Apps domain when a registered service is attached to it. This domain type should include everything you need to manage access to your subscribed Oracle service. But if you require higher limits or additional features, you can change to a different identity domain type.

Example Use Case: Your organization subscribes to an Oracle PaaS or SaaS service that provides an Oracle Apps identity domain with their service. You can use this domain type to manage access to Oracle PaaS and SaaS services. You might also have one or two third-party applications for which you'd like users to seamlessly sign-in without having to reauthenticate.

### Oracle Apps Premium

Oracle Apps Premium identity domains add support for hybrid IAM scenarios which extend the IAM service to manage access for on-premises or OCI hosted Oracle applications such as Oracle E-Business Suite, PeopleSoft, and Oracle Database. While this identity domain type is intended primarily for use with Oracle applications, it also allows you to manage access for a limited number of third-party or custom applications.

Example Use Case: Your organization would like to enable authentication and single sign-on for your workforce users to access Oracle SaaS applications as well as on-premises or cloud-hosted Oracle applications such as E-Business Suite, JD Edwards, PeopleSoft, Siebel, and/or Oracle Database. You might also want bidirectional synchronization with Microsoft Active Directory or other on-premises systems, and you might have a few third-party or custom applications for which you'd like users to seamlessly sign-in without having to reauthenticate.

### Premium

Premium identity domains provide the full IAM feature set and highest limits for employee and workforce use cases giving you enterprise-ready access management across hybrid IT environments. It includes all supported integration types and unlimited third-party applications. This is the ideal domain type if you're standardizing OCI IAM as your enterprise Identity and Access Management provider.

Example Use Case: You want an Identity-as-a-Service (IDaaS) solution to manage workforce authentication and access to all your Oracle and third-party applications whether they're SaaS apps, on-premises enterprise apps, or apps that are hosted in the cloud. You want to use modern authentication and authorization features such as passwordless authentication, FIDO2 hardware tokens, and adaptive security. You might also want automated provisioning and deprovisioning of accounts across these systems.

### External User

External User identity domains provide a robust IAM feature set for non employee use cases, consumer-facing apps, and custom app development. This domain type provides relevant features for these scenarios such as user self-service, social sign in, and consent management. This domain type is billed based on the quantity of stored users.
Note  
  
External identity domains are only licensed for non employee user accounts. If your business needs require that you have employee user accounts stored within an External identity domain (for example, if an app only supports one identity provider), that's allowed only if those user accounts also exist in another identity domain of type Free, Oracle Apps, Oracle Apps Premium, or Premium.

Example Use Case: You want a full-featured Identity-as-a-Service (IDaaS) solution that helps you manage authentication and access to custom or consumer-facing applications. The solution should support social sign in, user self-service password and profile management, and terms of use consent. And you might need the solution to scale to support millions of users.

### External Active User

External Active User identity domains provide a robust IAM feature set for non employee use cases, consumer-facing apps, and custom app development. This domain type provides relevant features for these scenarios such as user self-service, social sign in, and consent management. This domain type is billed based on the quantity of users who are active each month.
Note  
  
External identity domains are only licensed for non employee user accounts. If your business needs require that you have employee user accounts stored within an External identity domain (for example, if an app only supports one identity provider), that's allowed only if those user accounts also exist in another identity domain of type Free, Oracle Apps, Oracle Apps Premium, or Premium.

Example Use Case: You want a full-featured Identity-as-a-Service (IDaaS) solution that helps you manage authentication and access to custom or consumer-facing applications. The solution should support social sign in, user self-service password and profile management, and terms of use consent. And you might need the solution to scale to support millions of users.

## Feature Availability for Identity Domain Types

Understand the features available for the different identity domain types.

This table shows the features available to each domain type.

Feature Free Oracle Apps Oracle Apps Premium Premium External User External Active User
Core IAM features
User and group management
End-user self-registration -
Self-service profile management
Account recovery (self-service password reset by way of email, SMS, security questions)

SMS isn't part of the Free domain type
Default password policy
Group-based password policy
Support for External Apps[1
Outbound SSO to third-party apps
Provisioning to third-party apps using App Catalog - -
OAuth/token mgmt for third-party apps
Generic SCIM app template
Manage Access to Oracle Cloud Infrastructure
All current Infrastructure as a Service IAM features - -
Manage access to OCI resources - -
Dynamic groups (for OCI) - -
Credential types specific to OCI) - -
Security Options
External IdPs and social login (Federation / Inbound SSO)
Flexible IdP routing policies
Terms of use
Just in time provisioning
PIV / CAC card support
Schema extension
Delegated administration
Uni-directional Active Directory sync which supports inbound sync from AD to the IAM identity domain - -
Authentication Options: Oracle Mobile Authenticator (MFA) and adaptive security (MFA - TOTP and push, phone call, security questions, FIDO2, DUO, email).

SMS isn't part of the Free domain type
Passwordless authentication
Sign in policies (conditions - authenticated by, groups, administrators, exclusions, network perimeter, built-in risk engine)
Application SDKs
Oracle SaaS Integration
SSO for Oracle Cloud services
User provisioning for Oracle Cloud services (with account form, custom attributes, filters, and so on) - -
OAuth/Token management for Oracle App and SaaS extensions[2 - -
Reports
Auditing and reporting
Branding
Customized look and feel
Hosted sign-in - -
Advanced and hybrid identity and access management features
Advanced IAM
Bi-directional sync with LDAP by way of provisioning bridge - - - -
Bi-directional sync with AD bridge - - - -
Delegated authentication by way of AD bridge - - - -
SSO for any application
Hybrid IAM
Application Gateway (for any enterprise app) - -

Oracle enterprise apps only

Any enterprise app

Any enterprise app

Any enterprise app
EBS Asserter[3 - -
RADIUS proxy (all - Oracle DB, VPNs, network devices, and so forth) - -

Oracle DB only

All - Oracle DB, VPNs, Network Devices, and so on - -
Linux PAM - - - -

1 External or third-party apps are defined as either commercial applications offered by a provider other than Oracle or as custom-developed applications (including, for example, applications built on OCI using APEX). Note that custom applications built using Visual Builder Cloud Service don't count against the limit on external apps.

2 SaaS Extensions are custom-developed applications that are only used as extensions to subscribed Oracle SaaS applications such as HCM, ERP, SCM, and so on. The sole purpose of these applications is to augment Oracle SaaS apps. These don't count against the limit on external apps.

3 The right to use Oracle E-Business Suite Asserter also includes the right to use WebLogic Server Enterprise Edition solely for the purposes of running the asserter application in accordance with all terms and conditions as described in the[Oracle Fusion Middleware Licensing Information User Manual](https://docs.oracle.com/en/middleware/fusion-middleware/fmwlc/).

## IAM Identity Domain Object Limits

Understand the number of different types of object allowed in each identity domain type.

You can create different identity domain types subject to the limit allowed by your subscription type. To find out the identity domain limits for each subscription type, see[IAM With Identity Domains Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#iam-service-limits).
This table shows the limits of the number of each type of object for each identity domain type.

Resource Free Oracle Apps Oracle Apps Premium Premium External User External Active User
[Users](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../users/about-managing-users.htm)2,000 1,000,000 1,000,000 1,000,000 100,000,000 10,000,000
[Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../groups/managinggroups.htm)250 10,000 100,000 100,000 100,000 100,000
[Users in a group](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../users/about-managing-users.htm)2,000 10,000 100,000 100,000 100,000 100,000
[Groups per user](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../groups/managinggroups.htm)250 500 5,000 5,000 5,000 5,000
[Default password and group-based password policies](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../passwordpolicies/Managing-Password-Policies.htm)10 10 10 10 10 10
[Non Oracle apps](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../applications/oracle-and-custom-applications.htm)[1 2 2[2 10[2 5,000 5,000 5,000
[Oracle Cloud apps](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../applications/oracle-and-custom-applications.htm)2,000 2,000 2,000 2,000 - -
[Enterprise apps](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../applications/enterprise-applications.htm)- - 500

(Only Oracle enterprise apps) 500 500 500
[RADIUS proxy](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../radiusproxy/overview.htm)- - 50 50 - -
[Active Directory (AD) domains](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../msadbridge/microsoft-active-directory-ad-bridge1.htm)2 10 20 20 - -
[Active domain bridges per AD domain](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../msadbridge/microsoft-active-directory-ad-bridge1.htm)4 10 10 10 - -
[Provisioning bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../provisioningbridges/managing-provisioning-bridge.htm)4 10 10 10 - -
[Application Gateway](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../appgateways/understand-app-gateway.htm)- - 20 20 20 20
[External Identity Providers and Social Login (IdPs)](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../identityproviders/manage-identity-providers.htm)(Federation / inbound SSO) 5 5 30 30 30 30
[IdP policies](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../idppolicies/manage-idp-policies.htm)5 50 100 100 100 100
[Terms of use](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../termsofuse/manage-terms-use.htm)500 500 500 500 500 500
[Sign in policies](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../signonpolicies/managingsignonpolicies.htm)5 50 200 200 200 200
[Self-registration profiles](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../selfregistrationprofiles/overview.htm)- 50 50 50 50 50
[Dynamic groups](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../dynamicgroups/managingdynamicgroups.htm)50 50 50 50 - -
[API key per user](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../access/managing-user-credentials.htm)3 3 3 3 - -
[Auth token per user](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../access/managing-user-credentials.htm)2 2 2 2 - -
[OAuth2 client credentials per user](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../access/managing-user-credentials.htm)10 10 10 10 - -
[SMTP credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../access/managing-user-credentials.htm)2 2 2 2 - -
[Customer secret key per user](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../access/managing-user-credentials.htm)2 2 2 2 - -
[DB credentials per user](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../access/managing-user-credentials.htm)2 2 2 2 - -
OAuth Client Certificate 20 200 200 20,000 20,000 20,000
OAuth Partner Certificates 20 20 100 100 100 100
Trusted Partner Certificates 20 20 100 100 100 100
Identity Propagation Trust 30 30 30 30 30 30

1 Non Oracle or third-party apps are defined as either commercial applications offered by a provider other than Oracle or as custom-developed applications (including, for example, applications built on OCI) using APEX). Note that custom applications built using Visual Builder Cloud Service don't count against the limit on external apps.

2 The limits for the number of non Oracle or third-party apps for the domain types Oracle Apps and Oracle Apps Premium are temporarily not enforced. They will be enforced in future.

## Data Types for Custom Attributes

See the supported data types for custom attributes and their limits. These apply to all identity domain types.

Data Type Limit
4K char String Indexed (searchable) 84
40 char String Indexed (searchable) 5
4K char String Unindexed 36
40 char String Unindexed 15
Integer 20

## API Rate Limits

Understand the rate limiting for APIs for different identity domain types.

Oracle APIs are subject to rate limiting to protect the API service usage for all Oracle's customers. If you reach the API limit for the identity domain type, then IAM returns a 429 error code.

### Rate Limits for all Identity Domain Types

API Group Per Free Oracle Apps Oracle Apps Premium Premium External User External Active User
AuthN second 10 50 80 95 90 90
AuthN minute 150 1000 2100 4500 3100 3100
BasicAuthN second 10 100 160 95 90 90
BasicAuthN minute 150 3000 4000 4500 3100 3100
Token Mgmt second 10 40 50 65 60 60
Token Mgmt minute 150 1000 1700 3400 2300 2300
Others second 20 50 55 90 80 80
Others minute 150 1500 1750 5000 4000 4000
Bulk second 5 5 5 5 5 5
Bulk minute 200 200 200 200 200 200
Import and export day 4 8 10 10 10 10
Import and export hour 2 3 3 3 3 3
Note  
  
The maximum number of Identity Propagation Trust objects that can be created is restricted to 30. Contact support if the limit needs to be increased. For more information on object limits, see[IAM Identity Domain Object Limits](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#iam-object-limits).

### APIs in API Groups

API limits apply to the total of all APIs within a group.

[Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#)

- `login/sso/v1/user/`
- `/sso/v1/user/secure/login`
- `/sso/v1/user/logout`
- `/sso/v1/user/callback/login`
- `/sso/v1/sdk/authenticate`
- `/sso/v1/sdk/session`
- `/sso/v1/sdk/idp`
- `/sso/v1/sdk/secure/session`
- `/mfa/v1/requests`
- `/mfa/v1/users/{userguid}/factors`
- `/oauth2/v1/authorize`
- `/oauth2/v1/userlogout`
- `/oauth2/v1/consent`
- `/fed/v1/user/request/login`
- `/fed/v1/sp/sso`
- `/fed/v1/idp/sso`
- `/fed/v1/idp/usernametoken`
- `/fed/v1/metadata`
- `/fed/v1/mex`
- `/fed/v1/sp/slo`
- `/fed/v1/sp/initiatesso`
- `/fed/v1/sp/ssomtls`
- `/fed/v1/idp/slo`
- `/fed/v1/idp/initiatesso`
- `/fed/v1/idp/wsfed`
- `/fed/v1/idp/wsfedsignoutreturn`
- `/fed/v1/user/response/login`
- `/fed/v1/user/request/logout`
- `/fed/v1/user/response/logout`
- `/fed/v1/user/testspstart`
- `/fed/v1/user/testspresult`
- `/admin/v1/SigningCert/jwk`
- `/admin/v1/Asserter`
- `/admin/v1/MyAuthenticationFactorInitiator`
- `/admin/v1/MyAuthenticationFactorEnroller`
- `/admin/v1/MyAuthenticationFactorValidator`
- `/admin/v1/MyAuthenticationFactorsRemover`
- `/admin/v1/TermsOfUseConsent`
- `/admin/v1/MyTermsOfUseConsent`
- `/admin/v1/TrustedUserAgents`
- `/admin/v1/AuthenticationFactorInitiator`
- `/admin/v1/AuthenticationFactorEnroller`
- `/admin/v1/AuthenticationFactorValidator`
- `/admin/v1/MePasswordResetter`
- `/admin/v1/UserPasswordChanger`
- `/admin/v1/UserLockedStateChanger`
- `/admin/v1/AuthenticationFactorsRemover`
- `/admin/v1/BypassCodes`
- `/admin/v1/MyBypassCodes`
- `/admin/v1/MyTrustedUserAgents`
- `/admin/v1/Devices`
- `/admin/v1/MyDevices`
- `/admin/v1/TermsOfUses`
- `/admin/v1/TermsOfUseStatements`
- `/admin/v1/AuthenticationFactorSettings`
- `/admin/v1/SsoSettings`
- `/admin/v1/AdaptiveAccessSettings`
- `/admin/v1/RiskProviderProfiles`
- `/admin/v1/Threats`
- `/admin/v1/UserDevices`
- `/session/v1/SessionsLogoutValidator`
- `/ui/v1/signin`

[Basic Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#)

- `/admin/v1/HTTPAuthenticator`
- `/admin/v1/PasswordAuthenticator`

[Tokens](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#)

- `/oauth2/v1/token`
- `/oauth2/v1/introspect`
- `/oauth2/v1/revoke`
- `/oauth2/v1/device`

[Import/Export](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#)

- `/job/v1/JobSchedules?jobType=UserImport`
- `/job/v1/JobSchedules?jobType=UserExport`
- `/job/v1/JobSchedules?jobType=GroupImport`
- `/job/v1/JobSchedules?jobType=GroupExport`
- `/job/v1/JobSchedules?jobType=AppRoleImport`
- `/job/v1/JobSchedules?jobType=AppRoleExport`

[Bulk](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#)

- `/admin/v1/Bulk`
- `/admin/v1/BulkUserPasswordChanger`
- `/admin/v1/BulkUserPasswordResetter`
- `/admin/v1/BulkSourceEvents`

[Other](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#)

Any API not in one of the other API Groups is included in the Other API Group

### Other Restrictions

These restrictions are for Bulk, Import, and Export for all tiers:
- Payload size: 1 MB
- Bulk API: 50 operations limit per call
- Only one of these can be run at a time:
- Import: For Users, Groups &amp; App Role Memberships
- Full sync from apps
- Bulk APIs
- Export: For Users, Groups &amp; App Role Memberships
- CSV Import: 100 K rows limit per CSV &amp; Max file size: 10 MB
- CSV Export: 100 K rows limit

## Meters for Identity Domain Types

Understand the meters used for different identity domain types.

Free and Oracle Apps identity domain types don't use meters.

Oracle Apps Premium, Premium, External User, and External Active User identity domain types use these meters:

- 

Users per Month: The number of active and inactive users in the system, reported per hour. These meters are aggregated at the end of the billing cycle.
- 

SMS: The number of SMS messages sent from the system, reported every hour. These meters are aggregated at the end of the billing cycle.
- 

Tokens: The number of tokens issued by the system, reported every hour.
- 

Replicated Users per Month: If you configure replication to more regions, this meter applies to the number of active and inactive users in each replicated region, reported per hour. These meters are aggregated at the end of the billing cycle.
- Monthly Active Users: For active users only. The number of active users in the system, reported per month. These meters are aggregated at the end of the billing cycle.

After you have provisioned your service, Oracle Cloud Infrastructure has tools to help you analyze and understand the costs associated with your account. See[Checking Your Expenses and Usage](https://docs.oracle.com/iaas/Content/Billing/Concepts/costs.htm).

## Changing your Identity Domain Type

When you change the identity domain type, IAM validates the change you're making.
- You can't change the default domain to External User of the External Active User identity domain type.
- Your subscription type controls the number of identity domains of each type. If the change would exceed the number of identity domains of that type for your subscription type, you can't change to the new identity domain type. See[IAM With Identity Domains Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#iam-service-limits).
- If the number of objects of any type in your identity domain is higher than is allowed in the target identity domain type, you can't change to the new identity domain type. See[IAM Identity Domain Object Limits](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#iam-object-limits).
- The features available in your current identity domain type are checked. See[Feature Availability for Identity Domain Types](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#features). A warning message appears reminding you to exercise caution when changing from one identity domain type to another. You can proceed after the warning message, but some of your existing features might no longer work.
- You can't change a Free, Premium, or External User External Active User, identity domain to an Oracle Apps identity domain.

For information about how to change the domain type, see[Changing an Identity Domain's Type](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/../domains/to-change-identity-domain-type.htm)
